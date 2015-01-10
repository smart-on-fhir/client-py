#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (boolean.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import fhirelement


class bool(fhirelement.FHIRElement):
    """ Primitive Type boolean.
    
    Value of "true" or "false"
    """
    
    resource_name = "boolean"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(bool, self).__init__(jsondict)

