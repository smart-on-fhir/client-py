#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for all FHIR elements.

import logging


class FHIRElement(object):
    """ Base class for all FHIR elements.
    """
    
    def __init__(self, jsondict=None):
        self.id = None
        """ Logical id of this artefact. """
        
        self.contained = None
        """ Contained resources. """
        
        self._resolved = None
        """ Dictionary of resolved resources. """
        
        self._owner = None
        """ Points to the parent resource, if there is one. """
        
        self.extension = None
        self.modifierExtension = None
        
        if jsondict is not None:
            self.update_with_json(jsondict)
    
    
    # MARK: Instantiation from JSON
    
    @classmethod
    def with_json(cls, jsonobj):
        """ Initialize an element from a JSON dictionary or array.
        
        :param jsonobj: A dict or list of dicts to instantiate from
        :returns: An instance or a list of instances created from JSON data
        """
        if isinstance(jsonobj, dict):
            return cls(jsonobj)
        
        arr = []
        for jsondict in jsonobj:
            arr.append(cls(jsondict))
        return arr
    
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
        be serialized, as: ("name", "json_name", type, is_list)
        """
        from . import extension
        return [
            ("id", "id", str, False),
            ("extension", "extension", extension.Extension, True),
            ("modifierExtension", "modifierExtension", extension.Extension, True),
        ]
    
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
        for prop, name, typ, is_list in self.elementProperties():
            if not name in jsondict:
                continue
            
            if hasattr(typ, 'with_json_and_owner'):
                setattr(self, prop, typ.with_json_and_owner(jsondict[name], self))
            else:
                setattr(self, prop, jsondict[name])
        
        # extract contained resources
        if 'contained' in jsondict:
            from . import fhircontainedresource
            self.contained = self.contained or {}
            for js in jsondict['contained']:         # "contained" should be an array
                res = fhircontainedresource.FHIRContainedResource(jsondict=js, owner=self)
                if res.id:
                    self.contained[res.id] = res
                else:
                    logging.warning("Contained resource {} does not have an id, ignoring".format(res))
    
    def as_json(self):
        """ Serializes to JSON by inspecting `elementProperties()` and creating
        a JSON dictionary of all registered properties.
        """
        js = {}
        
        # JSONify all registered properties
        for prop, name, typ, is_list in self.elementProperties():
            val = getattr(self, prop)
            if val is None:
                continue
            if is_list:
                js[name] = [v.as_json() if hasattr(v, 'as_json') else v for v in val]
            else:
                js[name] = val.as_json() if hasattr(val, 'as_json') else val
        
        # handle contained resources
        if self.contained is not None and len(self.contained) > 0:
            # TODO: look at resolved (and newly added?) contained resources
            js['contained'] = [v.as_json() for k, v in self.contained.items()]
        
        return js
    
    
    # MARK: Handling References
    
    def containedReference(self, refid):
        """ Looks for the contained reference with the given id.
        
        :returns: An instance of FHIRContainedResource, if it was found
        """
        if self.contained and refid in self.contained:
            return self.contained[refid]
        return self._owner.containedReference(refid) if self._owner is not None else None
    
    def resolvedReference(self, refid):
        """ Returns the resolved reference with the given id, if it has been
        resolved already.
        """
        if self._resolved and refid in self._resolved:
            return self._resolved[refid]
        return self._owner.resolvedReference(refid) if self._owner is not None else None
    
    def didResolveReference(self, refid, resolved):
        """ Called by FHIRResource when it resolves a reference. Stores the
        resolved reference into the `_resolved` dictionary of the topmost
        owner.
        """
        if self._resolved is not None:
            self._resolved[refid] = resolved
        else:
            self._resolved = {refid: resolved}

