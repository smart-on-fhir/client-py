#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Quantity) on 2015-04-08.
#  2015, SMART Health IT.


import fhirelement


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
    
    def update_with_json(self, jsondict):
        super(Quantity, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'comparator' in jsondict:
            self.comparator = jsondict['comparator']
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'units' in jsondict:
            self.units = jsondict['units']
        if 'value' in jsondict:
            self.value = jsondict['value']

