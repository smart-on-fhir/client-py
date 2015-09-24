#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/SampledData) on 2015-09-24.
#  2015, SMART Health IT.


from . import fhirelement
from . import quantity


class SampledData(fhirelement.FHIRElement):
    """ A series of measurements taken by a device.
    
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    
    resource_name = "SampledData"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.data = None
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """
        
        self.dimensions = None
        """ Number of sample points at each time point.
        Type `int`. """
        
        self.factor = None
        """ Multiply data by this before adding to origin.
        Type `float`. """
        
        self.lowerLimit = None
        """ Lower limit of detection.
        Type `float`. """
        
        self.origin = None
        """ Zero value and units.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.period = None
        """ Number of milliseconds between samples.
        Type `float`. """
        
        self.upperLimit = None
        """ Upper limit of detection.
        Type `float`. """
        
        super(SampledData, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("data", "data", str, False),
            ("dimensions", "dimensions", int, False),
            ("factor", "factor", float, False),
            ("lowerLimit", "lowerLimit", float, False),
            ("origin", "origin", quantity.Quantity, False),
            ("period", "period", float, False),
            ("upperLimit", "upperLimit", float, False),
        ])
        return js

