#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-ResourceReference.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirelement


class ResourceReference(fhirelement.FHIRElement):
    """ A reference from one resource to another.
    """
    
    resource_name = "ResourceReference"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.display = None
        """ Text alternative for the resource.
        Type `str`. """
        
        self.reference = None
        """ Relative, internal or absolute URL reference.
        Type `str`. """
        
        super(ResourceReference, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ResourceReference, self).update_with_json(jsondict)
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'reference' in jsondict:
            self.reference = jsondict['reference']

