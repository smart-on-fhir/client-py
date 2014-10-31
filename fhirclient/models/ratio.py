#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Ratio.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirelement
import quantity


class Ratio(fhirelement.FHIRElement):
    """ A ratio of two Quantity values - a numerator and a denominator.
    """
    
    resource_name = "Ratio"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.denominator = None
        """ Denominator value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.numerator = None
        """ Numerator value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Ratio, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Ratio, self).update_with_json(jsondict)
        if 'denominator' in jsondict:
            self.denominator = quantity.Quantity.with_json(jsondict['denominator'])
        if 'numerator' in jsondict:
            self.numerator = quantity.Quantity.with_json(jsondict['numerator'])

