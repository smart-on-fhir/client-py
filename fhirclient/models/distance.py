#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Distance) on 2015-07-06.
#  2015, SMART Health IT.


from . import quantity


class Distance(quantity.Quantity):
    """ A measure of distance.
    
    There SHALL be a code if there is a value and it SHALL be an expression of
    length.  If system is present, it SHALL be UCUM.
    """
    
    resource_name = "Distance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Distance, self).__init__(jsondict)

