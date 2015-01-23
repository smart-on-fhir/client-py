#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (Narrative.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import fhirelement


class Narrative(fhirelement.FHIRElement):
    """ A human-readable formatted text, including images.
    """
    
    resource_name = "Narrative"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.div = None
        """ Limited xhtml content.
        Type `str`. """
        
        self.status = None
        """ generated | extensions | additional.
        Type `str`. """
        
        super(Narrative, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Narrative, self).update_with_json(jsondict)
        if 'div' in jsondict:
            self.div = jsondict['div']
        if 'status' in jsondict:
            self.status = jsondict['status']

