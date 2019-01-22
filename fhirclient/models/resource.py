#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Resource) on 2019-01-22.
#  2019, SMART Health IT.


from . import fhirabstractresource

class Resource(fhirabstractresource.FHIRAbstractResource):
    """ 
    B
    a
    s
    e
    R
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
    t
    h
    e
    b
    a
    s
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
    y
    p
    e
    f
    o
    r
    e
    v
    e
    r
    y
    t
    h
    i
    n
    g
    .
    
    """
    
    resource_type = "Resource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.id = None
        """ 
        L
        o
        g
        i
        c
        a
        l
        i
        d
        o
        f
        t
        h
        i
        s
        a
        r
        t
        i
        f
        a
        c
        t
        .
        Type `str`. """
        
        self.implicitRules = None
        """ 
        A
        s
        e
        t
        o
        f
        r
        u
        l
        e
        s
        u
        n
        d
        e
        r
        w
        h
        i
        c
        h
        t
        h
        i
        s
        c
        o
        n
        t
        e
        n
        t
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
        Type `str`. """
        
        self.language = None
        """ 
        L
        a
        n
        g
        u
        a
        g
        e
        o
        f
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
        n
        t
        e
        n
        t
        .
        Type `str`. """
        
        self.meta = None
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
        Type `Meta` (represented as `dict` in JSON). """
        
        super(Resource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Resource, self).elementProperties()
        js.extend([
            ("id", "id", str, False, None, False),
            ("implicitRules", "implicitRules", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("meta", "meta", meta.Meta, False, None, False),
        ])
        return js


import sys
try:
    from . import meta
except ImportError:
    meta = sys.modules[__package__ + '.meta']
