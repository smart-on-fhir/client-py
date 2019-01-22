#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Duration) on 2019-01-22.
#  2019, SMART Health IT.


from . import quantity

class Duration(quantity.Quantity):
    """ 
    A
    l
    e
    n
    g
    t
    h
    o
    f
    t
    i
    m
    e
    .
    """
    
    resource_type = "Duration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Duration, self).__init__(jsondict=jsondict, strict=strict)


