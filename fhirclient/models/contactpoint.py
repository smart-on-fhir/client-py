#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ContactPoint) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class ContactPoint(element.Element):
    """ 
    D
    e
    t
    a
    i
    l
    s
    o
    f
    a
    T
    e
    c
    h
    n
    o
    l
    o
    g
    y
    m
    e
    d
    i
    a
    t
    e
    d
    c
    o
    n
    t
    a
    c
    t
    p
    o
    i
    n
    t
    (
    p
    h
    o
    n
    e
    ,
    f
    a
    x
    ,
    e
    m
    a
    i
    l
    ,
    e
    t
    c
    .
    )
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    f
    o
    r
    a
    l
    l
    k
    i
    n
    d
    s
    o
    f
    t
    e
    c
    h
    n
    o
    l
    o
    g
    y
    m
    e
    d
    i
    a
    t
    e
    d
    c
    o
    n
    t
    a
    c
    t
    p
    o
    i
    n
    t
    s
    f
    o
    r
    a
    p
    e
    r
    s
    o
    n
    o
    r
    o
    r
    g
    a
    n
    i
    z
    a
    t
    i
    o
    n
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
    t
    e
    l
    e
    p
    h
    o
    n
    e
    ,
    e
    m
    a
    i
    l
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "ContactPoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ 
        T
        i
        m
        e
        p
        e
        r
        i
        o
        d
        w
        h
        e
        n
        t
        h
        e
        c
        o
        n
        t
        a
        c
        t
        p
        o
        i
        n
        t
        w
        a
        s
        /
        i
        s
        i
        n
        u
        s
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.rank = None
        """ 
        S
        p
        e
        c
        i
        f
        y
        p
        r
        e
        f
        e
        r
        r
        e
        d
        o
        r
        d
        e
        r
        o
        f
        u
        s
        e
        (
        1
        =
        h
        i
        g
        h
        e
        s
        t
        )
        .
        Type `int`. """
        
        self.system = None
        """ 
        p
        h
        o
        n
        e
        |
        f
        a
        x
        |
        e
        m
        a
        i
        l
        |
        p
        a
        g
        e
        r
        |
        u
        r
        l
        |
        s
        m
        s
        |
        o
        t
        h
        e
        r
        .
        Type `str`. """
        
        self.use = None
        """ 
        h
        o
        m
        e
        |
        w
        o
        r
        k
        |
        t
        e
        m
        p
        |
        o
        l
        d
        |
        m
        o
        b
        i
        l
        e
        -
        p
        u
        r
        p
        o
        s
        e
        o
        f
        t
        h
        i
        s
        c
        o
        n
        t
        a
        c
        t
        p
        o
        i
        n
        t
        .
        Type `str`. """
        
        self.value = None
        """ 
        T
        h
        e
        a
        c
        t
        u
        a
        l
        c
        o
        n
        t
        a
        c
        t
        p
        o
        i
        n
        t
        d
        e
        t
        a
        i
        l
        s
        .
        Type `str`. """
        
        super(ContactPoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContactPoint, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("rank", "rank", int, False, None, False),
            ("system", "system", str, False, None, False),
            ("use", "use", str, False, None, False),
            ("value", "value", str, False, None, False),
        ])
        return js


import sys
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
