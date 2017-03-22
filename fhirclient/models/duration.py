#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Duration) on 2017-03-22.
#  2017, SMART Health IT.


from . import quantity

class Duration(quantity.Quantity):
    """ A length of time.
    """
    
    resource_type = "Duration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Duration, self).__init__(jsondict=jsondict, strict=strict)


