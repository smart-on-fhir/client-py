#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Quantity) on 2015-07-06.
#  2015, SMART Health IT.


from . import fhirelement


class Quantity(fhirelement.FHIRElement):
    """ A measured or measurable amount.
    
    A measured amount (or an amount that can potentially be measured). Note
    that measured amounts include amounts that are not precisely quantified,
    including amounts involving arbitrary units and floating currencies.
    """
    
    resource_name = "Quantity"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Coded form of the unit.
        Type `str`. """
        
        self.comparator = None
        """ < | <= | >= | > - how to understand the value.
        Type `str`. """
        
        self.system = None
        """ System that defines coded unit form.
        Type `str`. """
        
        self.units = None
        """ Unit representation.
        Type `str`. """
        
        self.value = None
        """ Numerical value (with implicit precision).
        Type `float`. """
        
        super(Quantity, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Quantity, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("comparator", "comparator", str, False),
            ("system", "system", str, False),
            ("units", "units", str, False),
            ("value", "value", float, False),
        ])
        return js

