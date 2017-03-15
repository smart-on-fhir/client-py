#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.11641 (http://hl7.org/fhir/StructureDefinition/Age) on 2017-03-15.
#  2017, SMART Health IT.


from . import quantity

class Age(quantity.Quantity):
    """ A duration of time during which an organism (or a process) has existed.
    """
    
    resource_type = "Age"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Age, self).__init__(jsondict=jsondict, strict=strict)


