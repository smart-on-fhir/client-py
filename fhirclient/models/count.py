#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Count) on 2019-01-22.
#  2019, SMART Health IT.


from . import quantity

class Count(quantity.Quantity):
    """ 
    A
    m
    e
    a
    s
    u
    r
    e
    d
    o
    r
    m
    e
    a
    s
    u
    r
    a
    b
    l
    e
    a
    m
    o
    u
    n
    t
    .
    
    
    A
    m
    e
    a
    s
    u
    r
    e
    d
    a
    m
    o
    u
    n
    t
    (
    o
    r
    a
    n
    a
    m
    o
    u
    n
    t
    t
    h
    a
    t
    c
    a
    n
    p
    o
    t
    e
    n
    t
    i
    a
    l
    l
    y
    b
    e
    m
    e
    a
    s
    u
    r
    e
    d
    )
    .
    N
    o
    t
    e
    t
    h
    a
    t
    m
    e
    a
    s
    u
    r
    e
    d
    a
    m
    o
    u
    n
    t
    s
    i
    n
    c
    l
    u
    d
    e
    a
    m
    o
    u
    n
    t
    s
    t
    h
    a
    t
    a
    r
    e
    n
    o
    t
    p
    r
    e
    c
    i
    s
    e
    l
    y
    q
    u
    a
    n
    t
    i
    f
    i
    e
    d
    ,
    i
    n
    c
    l
    u
    d
    i
    n
    g
    a
    m
    o
    u
    n
    t
    s
    i
    n
    v
    o
    l
    v
    i
    n
    g
    a
    r
    b
    i
    t
    r
    a
    r
    y
    u
    n
    i
    t
    s
    a
    n
    d
    f
    l
    o
    a
    t
    i
    n
    g
    c
    u
    r
    r
    e
    n
    c
    i
    e
    s
    .
    
    """
    
    resource_type = "Count"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        super(Count, self).__init__(jsondict=jsondict, strict=strict)


