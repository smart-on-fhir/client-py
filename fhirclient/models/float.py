#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (decimal.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import fhirelement


class float(fhirelement.FHIRElement):
    """ Primitive Type decimal.
    
    A rational number with implicit precision
    """
    
    resource_name = "decimal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(float, self).__init__(jsondict)

