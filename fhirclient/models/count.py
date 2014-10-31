#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Count.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import quantity


class Count(quantity.Quantity):
    """ Profile for Count on Quantity.
    
    Basic Profile for Count on Quantity for validation support
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Count, self).__init__(jsondict)

