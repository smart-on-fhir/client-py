#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Base class for all FHIR elements.

import logging


class FHIRElement(object):
    """ Base class for all FHIR elements.
    """
    
    def __init__(self, jsondict=None):
        self.extension = None
        self.modifierExtension = None
        self.contained = None
        self._resolved = None
        
        if jsondict is not None:
            self.update_with_json(jsondict)
    
    def update_with_json(self, jsondict):
        """ Update the receiver with data in a JSON dictionary.
        """
        if jsondict is None:
            return
        
        # extract extensions
        if 'extension' in jsondict:
            self.extension = extension.Extension.with_json(jsondict['extension'])
        if 'modifierExtension' in jsondict:
            self.modifierExtension = extension.Extension.with_json(jsondict['modifierExtension'])
        
        # extract contained resources
        if 'contained' in jsondict:
            self.contained = self.contained or {}
            for js in jsondict['contained']:         # "contained" should be an array
                res = fhircontainedresource.FHIRContainedResource(jsondict=js)
                if res.id:
                    self.contained[res.id] = res
                else:
                    logging.warning("Contained resource {} does not have an id, ignoring".format(res))
    
    @classmethod
    def with_json(cls, jsonobj):
        """ Initialize an element from a JSON dictionary or array.
        
        :param jsonobj: A dict or list of dicts to instantiate from
        :returns: An instance or a list of instances created from JSON data
        """
        if dict == type(jsonobj):
            return cls(jsonobj)
        
        arr = []
        for jsondict in jsonobj:
            arr.append(cls(jsondict))
        return arr
    
    
    # MARK: Handling References
    
    def containedReference(self, refid):
        """ Returns the contained reference with the given id, if it exists.
        """
        return self.contained.get(refid) if self.contained is not None else None
    
    def resolvedReference(self, refid):
        """ Returns the resolved reference with the given id, if it has been
        resolved already.
        """
        return self._resolved[refid] if self._resolved is not None else None
    
    def didResolveReference(self, refid, resolved):
        """ Called by FHIRResource when it resolves a reference. Stores the
        resolved reference into the `_resolved` dictionary.
        """
        if self._resolved is not None:
            self._resolved[refid] = resolved
        else:
            self._resolved = {refid: resolved}
    

# these are subclasses of FHIRElement, import last
import extension
import fhircontainedresource
