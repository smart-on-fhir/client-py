#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Create FHIR search params from NoSQL-like query structures.
#  2014, SMART Health IT.

try:
    from urllib import quote_plus
except Exception as e:
    from urllib.parse import quote_plus


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
        
        return '{}?{}'.format(self.resource_type.resource_name, '&'.join(parts))
    
    def perform(self, server):
        """ Construct the search URL and execute it against the given server.
        
        :param server: The server against which to perform the search
        :returns: A Bundle resource
        """
        if server is None:
            raise Exception("Need a server to perform search")
        
        from . import bundle
        res = server.request_json(self.construct())
        bundle = bundle.Bundle(res)
        bundle._server = server
        return bundle
    
    def perform_resources(self, server):
        """ Performs the search by calling `perform`, then extracts all Bundle
        entries and returns a list of Resource instances.
        
        :param server: The server against which to perform the search
        :returns: A list of Resource instances
        """
        bundle = self.perform(server)
        resources = []
        if bundle is not None and bundle.entry is not None:
            for entry in bundle.entry:
                resources.append(entry.resource)
            
        return resources


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
        """ Return a string that represents the reciever as "key=value".
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
            raise Exception('Unknown operator "{}" for "{}"'.format(self.key, parent.name))
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

