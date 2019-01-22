#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Meta) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Meta(element.Element):
    """ 
    M
    e
    t
    a
    d
    a
    t
    a
    a
    b
    o
    u
    t
    a
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    
    T
    h
    e
    m
    e
    t
    a
    d
    a
    t
    a
    a
    b
    o
    u
    t
    a
    r
    e
    s
    o
    u
    r
    c
    e
    .
    T
    h
    i
    s
    i
    s
    c
    o
    n
    t
    e
    n
    t
    i
    n
    t
    h
    e
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
    i
    s
    m
    a
    i
    n
    t
    a
    i
    n
    e
    d
    b
    y
    t
    h
    e
    i
    n
    f
    r
    a
    s
    t
    r
    u
    c
    t
    u
    r
    e
    .
    C
    h
    a
    n
    g
    e
    s
    t
    o
    t
    h
    e
    c
    o
    n
    t
    e
    n
    t
    m
    i
    g
    h
    t
    n
    o
    t
    a
    l
    w
    a
    y
    s
    b
    e
    a
    s
    s
    o
    c
    i
    a
    t
    e
    d
    w
    i
    t
    h
    v
    e
    r
    s
    i
    o
    n
    c
    h
    a
    n
    g
    e
    s
    t
    o
    t
    h
    e
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    """
    
    resource_type = "Meta"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.lastUpdated = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        r
        e
        s
        o
        u
        r
        c
        e
        v
        e
        r
        s
        i
        o
        n
        l
        a
        s
        t
        c
        h
        a
        n
        g
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.profile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        s
        t
        h
        i
        s
        r
        e
        s
        o
        u
        r
        c
        e
        c
        l
        a
        i
        m
        s
        t
        o
        c
        o
        n
        f
        o
        r
        m
        t
        o
        .
        List of `str` items. """
        
        self.security = None
        """ 
        S
        e
        c
        u
        r
        i
        t
        y
        L
        a
        b
        e
        l
        s
        a
        p
        p
        l
        i
        e
        d
        t
        o
        t
        h
        i
        s
        r
        e
        s
        o
        u
        r
        c
        e
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.source = None
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
        w
        h
        e
        r
        e
        t
        h
        e
        r
        e
        s
        o
        u
        r
        c
        e
        c
        o
        m
        e
        s
        f
        r
        o
        m
        .
        Type `str`. """
        
        self.tag = None
        """ 
        T
        a
        g
        s
        a
        p
        p
        l
        i
        e
        d
        t
        o
        t
        h
        i
        s
        r
        e
        s
        o
        u
        r
        c
        e
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.versionId = None
        """ 
        V
        e
        r
        s
        i
        o
        n
        s
        p
        e
        c
        i
        f
        i
        c
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        .
        Type `str`. """
        
        super(Meta, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend([
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("security", "security", coding.Coding, True, None, False),
            ("source", "source", str, False, None, False),
            ("tag", "tag", coding.Coding, True, None, False),
            ("versionId", "versionId", str, False, None, False),
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
