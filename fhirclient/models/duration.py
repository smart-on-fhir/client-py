#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Duration.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import quantity


class Duration(quantity.Quantity):
    """ Profile for Duration on Quantity.
    
    Basic Profile for Duration on Quantity for validation support
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Duration, self).__init__(jsondict)

