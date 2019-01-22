#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/HumanName) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class HumanName(element.Element):
    """ 
    N
    a
    m
    e
    o
    f
    a
    h
    u
    m
    a
    n
    -
    p
    a
    r
    t
    s
    a
    n
    d
    u
    s
    a
    g
    e
    .
    
    
    A
    h
    u
    m
    a
    n
    '
    s
    n
    a
    m
    e
    w
    i
    t
    h
    t
    h
    e
    a
    b
    i
    l
    i
    t
    y
    t
    o
    i
    d
    e
    n
    t
    i
    f
    y
    p
    a
    r
    t
    s
    a
    n
    d
    u
    s
    a
    g
    e
    .
    
    """
    
    resource_type = "HumanName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.family = None
        """ 
        F
        a
        m
        i
        l
        y
        n
        a
        m
        e
        (
        o
        f
        t
        e
        n
        c
        a
        l
        l
        e
        d
        '
        S
        u
        r
        n
        a
        m
        e
        '
        )
        .
        Type `str`. """
        
        self.given = None
        """ 
        G
        i
        v
        e
        n
        n
        a
        m
        e
        s
        (
        n
        o
        t
        a
        l
        w
        a
        y
        s
        '
        f
        i
        r
        s
        t
        '
        )
        .
        I
        n
        c
        l
        u
        d
        e
        s
        m
        i
        d
        d
        l
        e
        n
        a
        m
        e
        s
        .
        List of `str` items. """
        
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
        n
        a
        m
        e
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
        
        self.prefix = None
        """ 
        P
        a
        r
        t
        s
        t
        h
        a
        t
        c
        o
        m
        e
        b
        e
        f
        o
        r
        e
        t
        h
        e
        n
        a
        m
        e
        .
        List of `str` items. """
        
        self.suffix = None
        """ 
        P
        a
        r
        t
        s
        t
        h
        a
        t
        c
        o
        m
        e
        a
        f
        t
        e
        r
        t
        h
        e
        n
        a
        m
        e
        .
        List of `str` items. """
        
        self.text = None
        """ 
        T
        e
        x
        t
        r
        e
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        o
        f
        t
        h
        e
        f
        u
        l
        l
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.use = None
        """ 
        u
        s
        u
        a
        l
        |
        o
        f
        f
        i
        c
        i
        a
        l
        |
        t
        e
        m
        p
        |
        n
        i
        c
        k
        n
        a
        m
        e
        |
        a
        n
        o
        n
        y
        m
        o
        u
        s
        |
        o
        l
        d
        |
        m
        a
        i
        d
        e
        n
        .
        Type `str`. """
        
        super(HumanName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("family", "family", str, False, None, False),
            ("given", "given", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("text", "text", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


import sys
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
