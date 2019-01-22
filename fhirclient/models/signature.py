#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Signature) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Signature(element.Element):
    """ 
    A
    S
    i
    g
    n
    a
    t
    u
    r
    e
    -
    X
    M
    L
    D
    i
    g
    S
    i
    g
    ,
    J
    W
    S
    ,
    G
    r
    a
    p
    h
    i
    c
    a
    l
    i
    m
    a
    g
    e
    o
    f
    s
    i
    g
    n
    a
    t
    u
    r
    e
    ,
    e
    t
    c
    .
    .
    
    
    A
    s
    i
    g
    n
    a
    t
    u
    r
    e
    a
    l
    o
    n
    g
    w
    i
    t
    h
    s
    u
    p
    p
    o
    r
    t
    i
    n
    g
    c
    o
    n
    t
    e
    x
    t
    .
    T
    h
    e
    s
    i
    g
    n
    a
    t
    u
    r
    e
    m
    a
    y
    b
    e
    a
    d
    i
    g
    i
    t
    a
    l
    s
    i
    g
    n
    a
    t
    u
    r
    e
    t
    h
    a
    t
    i
    s
    c
    r
    y
    p
    t
    o
    g
    r
    a
    p
    h
    i
    c
    i
    n
    n
    a
    t
    u
    r
    e
    ,
    o
    r
    s
    o
    m
    e
    o
    t
    h
    e
    r
    s
    i
    g
    n
    a
    t
    u
    r
    e
    a
    c
    c
    e
    p
    t
    a
    b
    l
    e
    t
    o
    t
    h
    e
    d
    o
    m
    a
    i
    n
    .
    T
    h
    i
    s
    o
    t
    h
    e
    r
    s
    i
    g
    n
    a
    t
    u
    r
    e
    m
    a
    y
    b
    e
    a
    s
    s
    i
    m
    p
    l
    e
    a
    s
    a
    g
    r
    a
    p
    h
    i
    c
    a
    l
    i
    m
    a
    g
    e
    r
    e
    p
    r
    e
    s
    e
    n
    t
    i
    n
    g
    a
    h
    a
    n
    d
    -
    w
    r
    i
    t
    t
    e
    n
    s
    i
    g
    n
    a
    t
    u
    r
    e
    ,
    o
    r
    a
    s
    i
    g
    n
    a
    t
    u
    r
    e
    c
    e
    r
    e
    m
    o
    n
    y
    D
    i
    f
    f
    e
    r
    e
    n
    t
    s
    i
    g
    n
    a
    t
    u
    r
    e
    a
    p
    p
    r
    o
    a
    c
    h
    e
    s
    h
    a
    v
    e
    d
    i
    f
    f
    e
    r
    e
    n
    t
    u
    t
    i
    l
    i
    t
    i
    e
    s
    .
    
    """
    
    resource_type = "Signature"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.data = None
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
        s
        i
        g
        n
        a
        t
        u
        r
        e
        c
        o
        n
        t
        e
        n
        t
        (
        X
        M
        L
        D
        i
        g
        S
        i
        g
        .
        J
        W
        S
        ,
        p
        i
        c
        t
        u
        r
        e
        ,
        e
        t
        c
        .
        )
        .
        Type `str`. """
        
        self.onBehalfOf = None
        """ 
        T
        h
        e
        p
        a
        r
        t
        y
        r
        e
        p
        r
        e
        s
        e
        n
        t
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sigFormat = None
        """ 
        T
        h
        e
        t
        e
        c
        h
        n
        i
        c
        a
        l
        f
        o
        r
        m
        a
        t
        o
        f
        t
        h
        e
        s
        i
        g
        n
        a
        t
        u
        r
        e
        .
        Type `str`. """
        
        self.targetFormat = None
        """ 
        T
        h
        e
        t
        e
        c
        h
        n
        i
        c
        a
        l
        f
        o
        r
        m
        a
        t
        o
        f
        t
        h
        e
        s
        i
        g
        n
        e
        d
        r
        e
        s
        o
        u
        r
        c
        e
        s
        .
        Type `str`. """
        
        self.type = None
        """ 
        I
        n
        d
        i
        c
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
        r
        e
        a
        s
        o
        n
        t
        h
        e
        e
        n
        t
        i
        t
        y
        s
        i
        g
        n
        e
        d
        t
        h
        e
        o
        b
        j
        e
        c
        t
        (
        s
        )
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.when = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        s
        i
        g
        n
        a
        t
        u
        r
        e
        w
        a
        s
        c
        r
        e
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.who = None
        """ 
        W
        h
        o
        s
        i
        g
        n
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Signature, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("sigFormat", "sigFormat", str, False, None, False),
            ("targetFormat", "targetFormat", str, False, None, False),
            ("type", "type", coding.Coding, True, None, True),
            ("when", "when", fhirdate.FHIRDate, False, None, True),
            ("who", "who", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
