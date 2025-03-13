#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Create FHIR search params from NoSQL-like query structures.
#  2014, SMART Health IT.

import logging
import warnings
from typing import Iterator, TYPE_CHECKING


from . import fhirreference
from .._utils import iter_pages

try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus

if TYPE_CHECKING:
    from fhirclient.models.resource import Resource
    from fhirclient.models.bundle import Bundle

logger = logging.getLogger(__name__)


class FHIRSearch(object):
    """ Create a FHIR search from NoSQL-like query structures.
    """
    
    def __init__(self, resource_type, struct=None):
        self.resource_type = resource_type
        """ The resource type class. """
        
        self.params = []
        """ FHIRSearchParam instances. """
        
        self.wants_expand = False
        """ Used internally; whether or not `params` must be expanded first. """

        self.includes = []
        """ Used internally; stores list of included resources for the search. """
        
        if struct is not None:
            if dict != type(struct):
                raise Exception("Must pass a Python dictionary, but got a {}".format(type(struct)))
            self.wants_expand = True
            for key, val in struct.items():
                self.params.append(FHIRSearchParam(key, val))
    
    
    # MARK: Execution
    
    def construct(self):
        """ Constructs the URL with query string from the receiver's params.
        """
        if self.resource_type is None:
            raise Exception("Need resource_type set to construct a search query")
        
        parts = []
        if self.params is not None:
            for param in self.params:
                if self.wants_expand:
                    for expanded in param.handle():
                        parts.append(expanded.as_parameter())
                else:
                    parts.append(param.as_parameter())

        for reference_model, reference_field, reverse in self.includes:
            key = '_revinclude' if reverse else '_include'
            parameter = '{}={}:{}'.format(
                key, reference_model.resource_type, reference_field
            )
            parts.append(parameter)

        return '{}?{}'.format(self.resource_type.resource_type, '&'.join(parts))

    def include(self, reference_field, reference_model=None, reverse=False):
        """ Add a resource to be included in the search results. Includes will
        fetch additional resources referred to by the search results, or
        additional resources which themselves refer to the search results
        (reverse include). Recursive or iterative includes are not supported.
        Provides a fluent interface to allow method chaining.

        To include Patient resources when searching Observations:
            `s = FHIRSearch(Observation).include('subject')`
        To include Observation resources when searching Patients:
            `s = FHIRSearch(Patient).include('subject', Observation, reverse=True)`

        :param reference_field: The name of the search parameter (must be
                                FHIRReference type)
        :param reference_model: The type of the source resource from which the
                                join comes (only used for reverse includes)
        :param reverse: Whether this is a reverse include
        :returns: This FHIRSearch instance
        """

        if reference_model is None:
            reference_model = self.resource_type

        model_fields = {
            name: typ
            for name, _, typ, _, _, _
            in reference_model().elementProperties()
        }

        if model_fields.get(reference_field) is not fhirreference.FHIRReference:
            logging.warning(
                '%s does not have a reference type element named %s',
                reference_model.resource_type, reference_field
            )
            return self

        if reference_model is not self.resource_type and not reverse:
            logging.warning('Only reverse includes can have a different reference model')
            reverse = True

        self.includes.append((reference_model, reference_field, reverse))
        return self

    def _read_bundle(self, server) -> 'Bundle':
        """ Construct the search URL and execute it against the given server.

        :param server: The server against which to perform the search
        :returns: A Bundle resource
        """
        if server is None:
            raise Exception("Need a server to perform search")

        from .bundle import Bundle
        return Bundle.read_from(self.construct(), server)

    def perform(self, server) -> 'Bundle':
        """ Construct the search URL and execute it against the given server.
        
        :param server: The server against which to perform the search
        :returns: A Bundle resource
        """
        # Old method with deprecation warning
        warnings.warn(
            "perform() is deprecated and will be removed in a future release. "
            "Please use perform_iter() instead.",
            DeprecationWarning,
        )

        return self._read_bundle(server)

    # Use forward references to avoid circular imports
    def perform_iter(self, server) -> Iterator['Bundle']:
        """ Perform the search by calling `perform` and return an iterator that yields
        Bundle instances.

        :param server: The server against which to perform the search
        :returns: An iterator of Bundle instances
        """
        return iter_pages(self._read_bundle(server), server)

    def perform_resources(self, server) -> 'list[Resource]':
        """ Performs the search by calling `perform_resources_iter` and returns a list of Resource instances.
        
        :param server: The server against which to perform the search
        :returns: A list of Resource instances
        """
        # Old method with deprecation warning
        warnings.warn(
            "perform_resources() is deprecated and will be removed in a future release. "
            "Please use perform_resources_iter() instead.",
            DeprecationWarning,
        )

        return list(self.perform_resources_iter(server))

    # Use forward references to avoid circular imports
    def perform_resources_iter(self, server) -> Iterator['Resource']:
        """ Performs the search by calling `perform_iter` and yields Resource instances
        from each Bundle returned by the search.

        :param server: The server against which to perform the search
        :returns: An iterator of Resource instances
        """
        for bundle in self.perform_iter(server):
            entries = bundle.entry or []
            for entry in entries:
                if entry.resource:
                    yield entry.resource


class FHIRSearchParam(object):
    """ Holds one search parameter.
    
    The instance's `value` can either be a string value or a search construct
    dictionary. In the latter case the class's `handle` method must be called
    to arrive at search parameter instances that can be converted into a URL
    query.
    """
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def copy(self):
        clone = object.__new__(self.__class__)
        clone.__dict__ = self.__dict__.copy()
        return clone
    
    def handle(self):
        """ Parses the receiver's value and returns a list of FHIRSearchParam
        instances. Needs only be called if the param needs to be handled, i.e.
        its value is a query structure.
        
        :returns: A list with one or more FHIRSearchParam instances, not
        altering the receiver
        """
        handler = FHIRSearchParamHandler.handler_for(self.name)(None, self.value)
        return handler.handle(self.copy())
    
    def as_parameter(self):
        """ Return a string that represents the receiver as "key=value".
        """
        return '{}={}'.format(self.name, quote_plus(self.value, safe=',<=>'))


class FHIRSearchParamHandler(object):
    handles = None
    handlers = []
    
    @classmethod
    def announce_handler(cls, handler):
        cls.handlers.append(handler)
    
    @classmethod
    def handler_for(cls, key):
        for handler in cls.handlers:
            if handler.can_handle(key):
                return handler
        return cls
    
    @classmethod
    def can_handle(cls, key):
        if cls.handles is not None:
            return key in cls.handles
        return True         # base class handles everything else, so be sure to test it last!
    
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.modifier = []
        self.multiplier = []
    
    def handle(self, param):
        """ Applies all handlers to the given search parameter.
        :returns: A list of one or more new `FHIRSearchParam` instances
        """
        self.prepare()
        return self.expand(param)
    
    def prepare(self, parent=None):
        """ Creates sub-handlers as needed, then prepares the receiver.
        """
        if dict == type(self.value):
            for key, val in self.value.items():
                handler = FHIRSearchParamHandler.handler_for(key)(key, val)
                handler.prepare(self)
        
        if parent is not None:
            parent.multiplier.append(self)
    
    def expand(self, param):
        """ Executes the receiver's modifier and multiplier on itself, applying
        changes to the given search param instance.
        
        :returns: A list of one or more FHIRSearchParam instances
        """
        for handler in self.modifier:
            handler.expand(param)
        
        self.apply(param)
        
        # if we have multiplier, expand sequentially
        if len(self.multiplier) > 0:
            expanded = []
            for handler in self.multiplier:
                clone = param.copy()
                expanded.extend(handler.expand(clone))
            
            return expanded
        
        # no multiplier, just return the passed-in paramater
        return [param]
    
    def apply(self, param):
        if self.key is not None:
            param.name = '{}.{}'.format(param.name, self.key)
        if 0 == len(self.multiplier):
            param.value = self.value


class FHIRSearchParamModifierHandler(FHIRSearchParamHandler):
    modifiers = {
        '$asc': ':asc',
        '$desc': ':desc',
        '$exact': ':exact',
        '$missing': ':missing',
        '$null': ':missing',
        '$text': ':text',
    }
    handles = modifiers.keys()
    
    def apply(self, param):
        if self.key not in self.__class__.modifiers:
            raise Exception('Unknown modifier "{}" for "{}"'.format(self.key, param.name))
        param.name += self.__class__.modifiers[self.key]
        param.value = self.value


class FHIRSearchParamOperatorHandler(FHIRSearchParamHandler):
    operators = {
        '$gt': '>',
        '$lt': '<',
        '$lte': '<=',
        '$gte': '>=',
    }
    handles = operators.keys()
    
    def apply(self, param):
        if self.key not in self.__class__.operators:
            raise Exception('Unknown operator "{}" for "{}"'.format(self.key, param.name))
        param.value = self.__class__.operators[self.key] + self.value


class FHIRSearchParamMultiHandler(FHIRSearchParamHandler):
    handles = ['$and', '$or']
    
    def prepare(self, parent):
        if list != type(self.value):
            raise Exception('Expecting a list argument for "{}" but got {}'.format(parent.key, self.value))
        
        handlers = []
        for val in self.value:
            if dict == type(val):
                for kkey, vval in val.items():
                    handlers.append(FHIRSearchParamHandler.handler_for(kkey)(kkey, vval))
            else:
                handlers.append(FHIRSearchParamHandler.handler_for(parent.key)(None, val))
        
        if '$and' == self.key:
            for handler in handlers:
                handler.prepare(parent)
        elif '$or' == self.key:
            ors = [h.value for h in handlers]
            handler = FHIRSearchParamHandler.handler_for(parent.key)(None, ','.join(ors))
            handler.prepare(parent)
        else:
            raise Exception('I cannot handle "{}"'.format(self.key))


class FHIRSearchParamTypeHandler(FHIRSearchParamHandler):
    handles = ['$type']
    
    def prepare(self, parent):
        parent.modifier.append(self)
    
    def apply(self, param):
        param.name = '{}:{}'.format(param.name, self.value)
    

# announce all handlers
FHIRSearchParamHandler.announce_handler(FHIRSearchParamModifierHandler)
FHIRSearchParamHandler.announce_handler(FHIRSearchParamOperatorHandler)
FHIRSearchParamHandler.announce_handler(FHIRSearchParamMultiHandler)
FHIRSearchParamHandler.announce_handler(FHIRSearchParamTypeHandler)

