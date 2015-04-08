#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Ratio) on 2015-04-08.
#  2015, SMART Health IT.


import fhirelement
import quantity


class Ratio(fhirelement.FHIRElement):
    """ A ratio of two Quantity values - a numerator and a denominator.
    
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
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
            self.denominator = quantity.Quantity.with_json_and_owner(jsondict['denominator'], self)
        if 'numerator' in jsondict:
            self.numerator = quantity.Quantity.with_json_and_owner(jsondict['numerator'], self)

