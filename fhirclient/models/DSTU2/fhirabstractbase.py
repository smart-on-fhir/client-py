#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for all FHIR elements.

import logging


class FHIRAbstractBase(object):
    """ Abstract base class for all FHIR elements.
    """
    
    def __init__(self, jsondict=None):
        
        self._resolved = None
        """ Dictionary of resolved resources. """
        
        self._owner = None
        """ Points to the parent resource, if there is one. """
        
        if jsondict is not None:
            self.update_with_json(jsondict)
    
    
    # MARK: Instantiation from JSON
    
    @classmethod
    def with_json(cls, jsonobj):
        """ Initialize an element from a JSON dictionary or array.
        
        If the JSON dictionary has a "resourceType" entry and the specified
        resource type is not the receiving classes type, uses
        `FHIRElementFactory` to return a correct class instance.
        
        :param jsonobj: A dict or list of dicts to instantiate from
        :returns: An instance or a list of instances created from JSON data
        """
        if isinstance(jsonobj, dict):
            return cls._with_json_dict(jsonobj)
        
        arr = []
        for jsondict in jsonobj:
            arr.append(cls._with_json_dict(jsondict))
        return arr
    
    @classmethod
    def _with_json_dict(cls, jsondict):
        if not isinstance(jsondict, dict):
            raise Exception("Cannot use this method with anything but a JSON dictionary, got {}"
                .format(jsondict))
        return cls(jsondict)
    
    @classmethod
    def with_json_and_owner(cls, jsonobj, owner):
        """ Instantiates by forwarding to `with_json()`, then remembers the
        "owner" of the instantiated elements. The "owner" is the resource
        containing the receiver and is used to resolve contained resources.
        
        :param dict jsonobj: Decoded JSON dictionary
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
        """
        if jsondict is None:
            return
        if not isinstance(jsondict, dict):
            logging.warning("Non-dict type {} fed to `update_with_json` on {}"
                .format(type(jsondict), type(self)))
            return
        
        # loop all registered properties and instantiate
        found = set(['resourceType', 'fhir_comments'])
        nonoptionals = set()
        for name, jsname, typ, is_list, of_many, not_optional in self.elementProperties():
            if not jsname in jsondict:
                if not_optional:
                    nonoptionals.add(of_many or jsname)
                continue
            
            if hasattr(typ, 'with_json_and_owner'):
                setattr(self, name, typ.with_json_and_owner(jsondict[jsname], self))
            else:
                setattr(self, name, jsondict[jsname])
                # TODO: look at `_name` if this is a primitive
            found.add(jsname)
            found.add('_'+jsname)
            if of_many is not None:
                found.add(of_many)
        
        # were there missing non-optional entries?
        if len(nonoptionals - found) > 0:
            for miss in nonoptionals - found:
                logging.warning("Non-optional property '{}' on {} is missing from JSON"
                    .format(miss, self))
        
        # were there superfluous dictionary keys?
        if len(set(jsondict.keys()) - found) > 0:
            for supflu in set(jsondict.keys()) - found:
                logging.warning("Superfluous entry '{}' in JSON for {}"
                    .format(supflu, self))
    
    def as_json(self):
        """ Serializes to JSON by inspecting `elementProperties()` and creating
        a JSON dictionary of all registered properties.
        """
        js = {}
        
        # JSONify all registered properties
        found = set()
        nonoptionals = set()
        for name, jsname, typ, is_list, of_many, not_optional in self.elementProperties():
            if not_optional:
                nonoptionals.add(of_many or jsname)
            
            val = getattr(self, name)
            if val is None:
                continue
            if is_list:
                if len(val) > 0:
                    found.add(of_many or jsname)
                js[jsname] = [v.as_json() if hasattr(v, 'as_json') else v for v in val]
            else:
                found.add(of_many or jsname)
                js[jsname] = val.as_json() if hasattr(val, 'as_json') else val
        
        # any missing non-optionals?
        if len(nonoptionals - found) > 0:
            for nonop in nonoptionals - found:
                logging.warning("Element '{}' is not optional, you should provide a value for it on {}"
                    .format(nonop, self))
        return js
    
    
    # MARK: Handling References
    
    def owningResource(self):
        """ Walks the owner hierarchy and returns the next parent that is a
        `DomainResource` instance.
        """
        owner = self._owner
        while owner is not None and not hasattr(owner, "contained"):
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

