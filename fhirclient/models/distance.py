#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Distance) on 2019-01-22.
#  2019, SMART Health IT.


from . import quantity

class Distance(quantity.Quantity):
    """ 
    A
    l
    e
    n
    g
    t
    h
    -
    a
    v
    a
    l
    u
    e
    w
    i
    t
    h
    a
    u
    n
    i
    t
    t
    h
    a
    t
    i
    s
    a
    p
    h
    y
    s
    i
    c
    a
    l
    d
    i
    s
    t
    a
    n
    c
    e
    .
    """
    
    resource_type = "Distance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Distance, self).__init__(jsondict=jsondict, strict=strict)


