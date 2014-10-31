#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Age.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import quantity


class Age(quantity.Quantity):
    """ Profile for Age on Quantity.
    
    Basic Profile for Age on Quantity for validation support
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Age, self).__init__(jsondict)

