#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Class to hold contained resources until they are resolved.


class FHIRContainedResource(object):
    """ Class to hold contained resources until they are resolved.
    
    The id of contained resources will be referenced from their parents as URL
    fragment, meaning "med1" will be referenced as "#med1". FHIRReference
    handles id normalization.
    
    http://hl7.org/implement/standards/fhir/references.html#contained
    """
    
    def __init__(self, jsondict=None, owner=None):
        self.id = None
        self.type = None
        self.json = None
        self.owner = owner
        
        if jsondict is not None:
            self.update_with_json(jsondict)
    
    def update_with_json(self, jsondict):
        if jsondict is not None:
            self.id = jsondict.get('id')
            self.type = jsondict.get('resourceType')
            self.json = jsondict
    
    def as_json(self):
        return self.json
