#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Range) on 2015-06-19.
#  2015, SMART Health IT.


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
    
    def elementProperties(self):
        js = super(Range, self).elementProperties()
        js.extend([
            ("high", "high", quantity.Quantity, False),
            ("low", "low", quantity.Quantity, False),
        ])
        return js

