#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Range) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Range(element.Element):
    """ 
    S
    e
    t
    o
    f
    v
    a
    l
    u
    e
    s
    b
    o
    u
    n
    d
    e
    d
    b
    y
    l
    o
    w
    a
    n
    d
    h
    i
    g
    h
    .
    
    
    A
    s
    e
    t
    o
    f
    o
    r
    d
    e
    r
    e
    d
    Q
    u
    a
    n
    t
    i
    t
    i
    e
    s
    d
    e
    f
    i
    n
    e
    d
    b
    y
    a
    l
    o
    w
    a
    n
    d
    h
    i
    g
    h
    l
    i
    m
    i
    t
    .
    
    """
    
    resource_type = "Range"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.high = None
        """ 
        H
        i
        g
        h
        l
        i
        m
        i
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.low = None
        """ 
        L
        o
        w
        l
        i
        m
        i
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(Range, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Range, self).elementProperties()
        js.extend([
            ("high", "high", quantity.Quantity, False, None, False),
            ("low", "low", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
