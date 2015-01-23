#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (Range.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import fhirelement
import quantity


class Range(fhirelement.FHIRElement):
    """ Set of values bounded by low and high.
    
    A set of ordered Quantities defined by a low and high limit.
    """
    
    resource_name = "Range"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.high = None
        """ High limit.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.low = None
        """ Low limit.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Range, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Range, self).update_with_json(jsondict)
        if 'high' in jsondict:
            self.high = quantity.Quantity.with_json_and_owner(jsondict['high'], self)
        if 'low' in jsondict:
            self.low = quantity.Quantity.with_json_and_owner(jsondict['low'], self)

