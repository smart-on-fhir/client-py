#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Range) on 2016-06-23.
#  2016, SMART Health IT.


from . import element

class Range(element.Element):
    """ Set of values bounded by low and high.
    
    A set of ordered Quantities defined by a low and high limit.
    """
    
    resource_name = "Range"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.high = None
        """ High limit.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.low = None
        """ Low limit.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        super(Range, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Range, self).elementProperties()
        js.extend([
            ("high", "high", quantity.Quantity, False, None, False),
            ("low", "low", quantity.Quantity, False, None, False),
        ])
        return js


from . import quantity
