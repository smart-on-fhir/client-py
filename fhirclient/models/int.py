#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (integer.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import fhirelement


class int(fhirelement.FHIRElement):
    """ Primitive Type integer.
    
    A whole number
    """
    
    resource_name = "integer"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(int, self).__init__(jsondict)

