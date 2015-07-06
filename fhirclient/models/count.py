#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Count) on 2015-07-06.
#  2015, SMART Health IT.


from . import quantity


class Count(quantity.Quantity):
    """ A count of a discrete element (no unit).
    
    There SHALL be a code with a value of "1" if there is a value and it SHALL
    be an expression of length.  If system is present, it SHALL be UCUM.  If
    present, the value SHALL a whole number.
    """
    
    resource_name = "Count"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Count, self).__init__(jsondict)

