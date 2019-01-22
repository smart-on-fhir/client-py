#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Ratio) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Ratio(element.Element):
    """ 
    A
    r
    a
    t
    i
    o
    o
    f
    t
    w
    o
    Q
    u
    a
    n
    t
    i
    t
    y
    v
    a
    l
    u
    e
    s
    -
    a
    n
    u
    m
    e
    r
    a
    t
    o
    r
    a
    n
    d
    a
    d
    e
    n
    o
    m
    i
    n
    a
    t
    o
    r
    .
    
    
    A
    r
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    o
    f
    t
    w
    o
    Q
    u
    a
    n
    t
    i
    t
    y
    v
    a
    l
    u
    e
    s
    -
    e
    x
    p
    r
    e
    s
    s
    e
    d
    a
    s
    a
    n
    u
    m
    e
    r
    a
    t
    o
    r
    a
    n
    d
    a
    d
    e
    n
    o
    m
    i
    n
    a
    t
    o
    r
    .
    
    """
    
    resource_type = "Ratio"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.denominator = None
        """ 
        D
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        v
        a
        l
        u
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.numerator = None
        """ 
        N
        u
        m
        e
        r
        a
        t
        o
        r
        v
        a
        l
        u
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Ratio, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Ratio, self).elementProperties()
        js.extend([
            ("denominator", "denominator", quantity.Quantity, False, None, False),
            ("numerator", "numerator", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
