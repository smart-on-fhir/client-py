#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Age) on 2015-07-06.
#  2015, SMART Health IT.


from . import quantity


class Age(quantity.Quantity):
    """ A duration (length of time) with a UCUM code.
    
    There SHALL be a code if there is a value and it SHALL be an expression of
    time.  If system is present, it SHALL be UCUM.  If value is present, it
    SHALL be positive.
    """
    
    resource_name = "Age"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Age, self).__init__(jsondict)

