#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Range.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import FHIRElement
import Quantity


class Range(FHIRElement.FHIRElement):
    """ Set of values bounded by low and high.
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
            self.high = Quantity.Quantity.with_json(jsondict['high'])
        if 'low' in jsondict:
            self.low = Quantity.Quantity.with_json(jsondict['low'])

