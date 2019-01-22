#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Binary) on 2019-01-22.
#  2019, SMART Health IT.


from . import resource

class Binary(resource.Resource):
    """ 
    P
    u
    r
    e
    b
    i
    n
    a
    r
    y
    c
    o
    n
    t
    e
    n
    t
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
    f
    o
    r
    m
    a
    t
    o
    t
    h
    e
    r
    t
    h
    a
    n
    F
    H
    I
    R
    .
    
    
    A
    r
    e
    s
    o
    u
    r
    c
    e
    t
    h
    a
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
    s
    t
    h
    e
    d
    a
    t
    a
    o
    f
    a
    s
    i
    n
    g
    l
    e
    r
    a
    w
    a
    r
    t
    i
    f
    a
    c
    t
    a
    s
    d
    i
    g
    i
    t
    a
    l
    c
    o
    n
    t
    e
    n
    t
    a
    c
    c
    e
    s
    s
    i
    b
    l
    e
    i
    n
    i
    t
    s
    n
    a
    t
    i
    v
    e
    f
    o
    r
    m
    a
    t
    .
    A
    B
    i
    n
    a
    r
    y
    r
    e
    s
    o
    u
    r
    c
    e
    c
    a
    n
    c
    o
    n
    t
    a
    i
    n
    a
    n
    y
    c
    o
    n
    t
    e
    n
    t
    ,
    w
    h
    e
    t
    h
    e
    r
    t
    e
    x
    t
    ,
    i
    m
    a
    g
    e
    ,
    p
    d
    f
    ,
    z
    i
    p
    a
    r
    c
    h
    i
    v
    e
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "Binary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ 
        M
        i
        m
        e
        T
        y
        p
        e
        o
        f
        t
        h
        e
        b
        i
        n
        a
        r
        y
        c
        o
        n
        t
        e
        n
        t
        .
        Type `str`. """
        
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
        c
        o
        n
        t
        e
        n
        t
        .
        Type `str`. """
        
        self.securityContext = None
        """ 
        I
        d
        e
        n
        t
        i
        f
        i
        e
        s
        a
        n
        o
        t
        h
        e
        r
        r
        e
        s
        o
        u
        r
        c
        e
        t
        o
        u
        s
        e
        a
        s
        p
        r
        o
        x
        y
        w
        h
        e
        n
        e
        n
        f
        o
        r
        c
        i
        n
        g
        a
        c
        c
        e
        s
        s
        c
        o
        n
        t
        r
        o
        l
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Binary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Binary, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, True),
            ("data", "data", str, False, None, False),
            ("securityContext", "securityContext", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
