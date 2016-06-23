#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for all FHIR elements.

import sys
import logging


class FHIRValidationError(Exception):
    """ Exception raised when one or more errors occurred during model
    validation.
    """
    
    def __init__(self, errors, path=None):
        """ Initializer.
        
        :param errors: List of Exception instances. Also accepts a string,
            which is converted to a TypeError.
        :param str path: The property path on the object where errors occurred
        """
        if not isinstance(errors, list):
            errors = [TypeError(errors)]
        msgs = "\n  ".join([str(e).replace("\n", "\n  ") for e in errors])
        message = "{}:\n  {}".format(path or "{root}", msgs)
        
        super(FHIRValidationError, self).__init__(message)
        
        self.errors = errors
        """ A list of validation errors encountered. Typically contains
        TypeError, KeyError, possibly AttributeError and others. """
        
        self.path = path
        """ The path on the object where the errors occurred. """
    
    def prefixed(self, path_prefix):
        """ Creates a new instance of the receiver, with the given path prefix
        applied. """
        path = '{}.{}'.format(path_prefix, self.path) if self.path is not None else path_prefix
        return self.__class__(self.errors, path)


class FHIRAbstractBase(object):
    """ Abstract base class for all FHIR elements.
    """
    
    def __init__(self, jsondict=None, strict=True):
        """ Initializer. If strict is true, raises on errors, otherwise uses
        `logging.warning()`.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self._resolved = None
        """ Dictionary of resolved resources. """
        
        self._owner = None
        """ Points to the parent resource, if there is one. """
        
        if jsondict is not None:
            if strict:
                self.update_with_json(jsondict)
            else:
                try:
                    self.update_with_json(jsondict)
                except FHIRValidationError as e:
                    for err in e.errors:
                        logging.warning(err)
    
    
    # MARK: Instantiation from JSON
    
    @classmethod
    def with_json(cls, jsonobj):
        """ Initialize an element from a JSON dictionary or array.
        
        If the JSON dictionary has a "resourceType" entry and the specified
        resource type is not the receiving classes type, uses
        `FHIRElementFactory` to return a correct class instance.
        
        :raises: TypeError on anything but dict or list of dicts
        :raises: FHIRValidationError if instantiation fails
        :param jsonobj: A dict or list of dicts to instantiate from
        :returns: An instance or a list of instances created from JSON data
        """
        if isinstance(jsonobj, dict):
            return cls._with_json_dict(jsonobj)
        
        if isinstance(jsonobj, list):
            return [cls._with_json_dict(jsondict) for jsondict in jsonobj]
        
        raise TypeError("`with_json()` on {} only takes dict or list of dict, but you provided {}"
            .format(cls, type(jsonobj)))
    
    @classmethod
    def _with_json_dict(cls, jsondict):
        """ Internal method to instantiate from JSON dictionary.
        
        :raises: TypeError on anything but dict
        :raises: FHIRValidationError if instantiation fails
        :returns: An instance created from dictionary data
        """
        if not isinstance(jsondict, dict):
            raise TypeError("Can only use `_with_json_dict()` on {} with a dictionary, got {}"
                .format(type(self), type(jsondict)))
        return cls(jsondict)
    
    @classmethod
    def with_json_and_owner(cls, jsonobj, owner):
        """ Instantiates by forwarding to `with_json()`, then remembers the
        "owner" of the instantiated elements. The "owner" is the resource
        containing the receiver and is used to resolve contained resources.
        
        :raises: TypeError on anything but dict or list of dicts
        :raises: FHIRValidationError if instantiation fails
        :param dict jsonobj: Decoded JSON dictionary (or list thereof)
        :param FHIRElement owner: The owning parent
        :returns: An instance or a list of instances created from JSON data
        """
        instance = cls.with_json(jsonobj)
        if isinstance(instance, list):
            for inst in instance:
                inst._owner = owner
        else:
            instance._owner = owner
        
        return instance
    
    
    # MARK: (De)Serialization
    
    def elementProperties(self):
        """ Returns a list of tuples, one tuple for each property that should
        be serialized, as: ("name", "json_name", type, is_list, "of_many", not_optional)
        """
        return []
    
    def update_with_json(self, jsondict):
        """ Update the receiver with data in a JSON dictionary.
        
        :raises: FHIRValidationError on validation errors
        :param dict jsondict: The JSON dictionary to use to update the receiver
        :returns: None on success, a list of errors if there were errors
        """
        if jsondict is None:
            return
        
        if not isinstance(jsondict, dict):
            raise FHIRValidationError("Non-dict type {} fed to `update_with_json` on {}"
                .format(type(jsondict), type(self)))
        
        # loop all registered properties and instantiate
        errs = []
        found = set(['resourceType', 'fhir_comments'])
        nonoptionals = set()
        for name, jsname, typ, is_list, of_many, not_optional in self.elementProperties():
            if not jsname in jsondict:
                if not_optional:
                    nonoptionals.add(of_many or jsname)
                continue
            
            # bring the value in shape
            err = None
            value = jsondict[jsname]
            if hasattr(typ, 'with_json_and_owner'):
                try:
                    value = typ.with_json_and_owner(value, self)
                except Exception as e:
                    value = None
                    err = e
            
            # got a value, test if it is of required type and assign
            if value is not None:
                testval = value
                if is_list:
                    if not isinstance(value, list):
                        err = TypeError("Wrong type {} for list property \"{}\" on {}, expecting a list of {}"
                            .format(type(value), name, type(self), typ))
                        testval = None
                    else:
                        testval = value[0] if value and len(value) > 0 else None
                
                if testval is not None and not self._matches_type(testval, typ):
                    err = TypeError("Wrong type {} for property \"{}\" on {}, expecting {}"
                        .format(type(testval), name, type(self), typ))
                else:
                    setattr(self, name, value)
                    # TODO: look at `_name` if this is a primitive
            
            if err is not None:
                errs.append(err.prefixed(name) if isinstance(err, FHIRValidationError) else FHIRValidationError([err], name))

            found.add(jsname)
            found.add('_'+jsname)
            if of_many is not None:
                found.add(of_many)
        
        # were there missing non-optional entries?
        if len(nonoptionals - found) > 0:
            for miss in nonoptionals - found:
                errs.append(KeyError("Non-optional property \"{}\" on {} is missing"
                    .format(miss, self)))
        
        # were there superfluous dictionary keys?
        if len(set(jsondict.keys()) - found) > 0:
            for supflu in set(jsondict.keys()) - found:
                errs.append(AttributeError("Superfluous entry \"{}\" in data for {}"
                    .format(supflu, self)))
        
        if len(errs) > 0:
            raise FHIRValidationError(errs)
    
    def as_json(self):
        """ Serializes to JSON by inspecting `elementProperties()` and creating
        a JSON dictionary of all registered properties. Checks:
        
        - whether required properties are not None (and lists not empty)
        - whether not-None properties are of the correct type
        
        :raises: FHIRValidationError if properties have the wrong type or if
            required properties are empty
        :returns: A validated dict object that can be JSON serialized
        """
        js = {}
        errs = []
        
        # JSONify all registered properties
        found = set()
        nonoptionals = set()
        for name, jsname, typ, is_list, of_many, not_optional in self.elementProperties():
            if not_optional:
                nonoptionals.add(of_many or jsname)
            
            err = None
            value = getattr(self, name)
            if value is None:
                continue
            
            if is_list:
                if not isinstance(value, list):
                   err = TypeError("Expecting property \"{}\" on {} to be list, but is {}"
                       .format(name, type(self), type(value)))
                elif len(value) > 0:
                    if not self._matches_type(value[0], typ):
                        err = TypeError("Expecting property \"{}\" on {} to be {}, but is {}"
                            .format(name, type(self), typ, type(value[0])))
                    else:
                        lst = []
                        for v in value:
                            try:
                                lst.append(v.as_json() if hasattr(v, 'as_json') else v)
                            except FHIRValidationError as e:
                                err = e.prefixed(name)
                        found.add(of_many or jsname)
                        js[jsname] = lst
            else:
                if not self._matches_type(value, typ):
                    err = TypeError("Expecting property \"{}\" on {} to be {}, but is {}"
                        .format(name, type(self), typ, type(value)))
                else:
                    try:
                        found.add(of_many or jsname)
                        js[jsname] = value.as_json() if hasattr(value, 'as_json') else value
                    except FHIRValidationError as e:
                        err = e.prefixed(name)
            
            if err is not None:
                errs.append(err if isinstance(err, FHIRValidationError) else FHIRValidationError([err], name))
        
        # any missing non-optionals?
        if len(nonoptionals - found) > 0:
            for nonop in nonoptionals - found:
                errs.append(KeyError("Property \"{}\" on {} is not optional, you must provide a value for it"
                    .format(nonop, self)))
        
        if len(errs) > 0:
            raise FHIRValidationError(errs)
        return js
    
    def _matches_type(self, value, typ):
        if value is None:
            return True
        if isinstance(value, typ):
            return True
        if int == typ or float == typ:
            return (isinstance(value, int) or isinstance(value, float))
        if (sys.version_info < (3, 0)) and (str == typ or unicode == typ):
            return (isinstance(value, str) or isinstance(value, unicode))
        return False
    
    
    # MARK: Handling References
    
    def owningResource(self):
        """ Walks the owner hierarchy and returns the next parent that is a
        `DomainResource` instance.
        """
        owner = self._owner
        while owner is not None and not hasattr(owner, "contained"):
            owner = owner._owner
        return owner
    
    def owningBundle(self):
        """ Walks the owner hierarchy and returns the next parent that is a
        `Bundle` instance.
        """
        owner = self._owner
        while owner is not None and not 'Bundle' == owner.resource_name:
            owner = owner._owner
        return owner
    
    def resolvedReference(self, refid):
        """ Returns the resolved reference with the given id, if it has been
        resolved already. If it hasn't, forwards the call to its owner if it
        has one.
        
        You should probably use `resolve()` on the `FHIRReference` itself.
        
        :param refid: The id of the resource to resolve
        :returns: An instance of `Resource`, if it was found
        """
        if self._resolved and refid in self._resolved:
            return self._resolved[refid]
        return self._owner.resolvedReference(refid) if self._owner is not None else None
    
    def didResolveReference(self, refid, resolved):
        """ Called by `FHIRResource` when it resolves a reference. Stores the
        resolved reference into the `_resolved` dictionary.
        
        :param refid: The id of the resource that was resolved
        :param refid: The resolved resource, ready to be cached
        """
        if self._resolved is not None:
            self._resolved[refid] = resolved
        else:
            self._resolved = {refid: resolved}

