#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Distance.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import quantity


class Distance(quantity.Quantity):
    """ Profile for Distance on Quantity.
    
    Basic Profile for Distance on Quantity for validation support
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Distance, self).__init__(jsondict)

