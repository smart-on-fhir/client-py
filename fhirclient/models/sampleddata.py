#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SampledData) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class SampledData(element.Element):
    """ 
    A
    s
    e
    r
    i
    e
    s
    o
    f
    m
    e
    a
    s
    u
    r
    e
    m
    e
    n
    t
    s
    t
    a
    k
    e
    n
    b
    y
    a
    d
    e
    v
    i
    c
    e
    .
    
    
    A
    s
    e
    r
    i
    e
    s
    o
    f
    m
    e
    a
    s
    u
    r
    e
    m
    e
    n
    t
    s
    t
    a
    k
    e
    n
    b
    y
    a
    d
    e
    v
    i
    c
    e
    ,
    w
    i
    t
    h
    u
    p
    p
    e
    r
    a
    n
    d
    l
    o
    w
    e
    r
    l
    i
    m
    i
    t
    s
    .
    T
    h
    e
    r
    e
    m
    a
    y
    b
    e
    m
    o
    r
    e
    t
    h
    a
    n
    o
    n
    e
    d
    i
    m
    e
    n
    s
    i
    o
    n
    i
    n
    t
    h
    e
    d
    a
    t
    a
    .
    
    """
    
    resource_type = "SampledData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.data = None
        """ 
        D
        e
        c
        i
        m
        a
        l
        v
        a
        l
        u
        e
        s
        w
        i
        t
        h
        s
        p
        a
        c
        e
        s
        ,
        o
        r
        "
        E
        "
        |
        "
        U
        "
        |
        "
        L
        "
        .
        Type `str`. """
        
        self.dimensions = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        s
        a
        m
        p
        l
        e
        p
        o
        i
        n
        t
        s
        a
        t
        e
        a
        c
        h
        t
        i
        m
        e
        p
        o
        i
        n
        t
        .
        Type `int`. """
        
        self.factor = None
        """ 
        M
        u
        l
        t
        i
        p
        l
        y
        d
        a
        t
        a
        b
        y
        t
        h
        i
        s
        b
        e
        f
        o
        r
        e
        a
        d
        d
        i
        n
        g
        t
        o
        o
        r
        i
        g
        i
        n
        .
        Type `float`. """
        
        self.lowerLimit = None
        """ 
        L
        o
        w
        e
        r
        l
        i
        m
        i
        t
        o
        f
        d
        e
        t
        e
        c
        t
        i
        o
        n
        .
        Type `float`. """
        
        self.origin = None
        """ 
        Z
        e
        r
        o
        v
        a
        l
        u
        e
        a
        n
        d
        u
        n
        i
        t
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        m
        i
        l
        l
        i
        s
        e
        c
        o
        n
        d
        s
        b
        e
        t
        w
        e
        e
        n
        s
        a
        m
        p
        l
        e
        s
        .
        Type `float`. """
        
        self.upperLimit = None
        """ 
        U
        p
        p
        e
        r
        l
        i
        m
        i
        t
        o
        f
        d
        e
        t
        e
        c
        t
        i
        o
        n
        .
        Type `float`. """
        
        super(SampledData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("dimensions", "dimensions", int, False, None, True),
            ("factor", "factor", float, False, None, False),
            ("lowerLimit", "lowerLimit", float, False, None, False),
            ("origin", "origin", quantity.Quantity, False, None, True),
            ("period", "period", float, False, None, True),
            ("upperLimit", "upperLimit", float, False, None, False),
        ])
        return js


import sys
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
