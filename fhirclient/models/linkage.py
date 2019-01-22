#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Linkage) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Linkage(domainresource.DomainResource):
    """ 
    L
    i
    n
    k
    s
    r
    e
    c
    o
    r
    d
    s
    f
    o
    r
    '
    s
    a
    m
    e
    '
    i
    t
    e
    m
    .
    
    
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
    t
    w
    o
    o
    r
    m
    o
    r
    e
    r
    e
    c
    o
    r
    d
    s
    (
    r
    e
    s
    o
    u
    r
    c
    e
    i
    n
    s
    t
    a
    n
    c
    e
    s
    )
    t
    h
    a
    t
    r
    e
    f
    e
    r
    t
    o
    t
    h
    e
    s
    a
    m
    e
    r
    e
    a
    l
    -
    w
    o
    r
    l
    d
    "
    o
    c
    c
    u
    r
    r
    e
    n
    c
    e
    "
    .
    
    """
    
    resource_type = "Linkage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        i
        s
        l
        i
        n
        k
        a
        g
        e
        a
        s
        s
        e
        r
        t
        i
        o
        n
        i
        s
        a
        c
        t
        i
        v
        e
        o
        r
        n
        o
        t
        .
        Type `bool`. """
        
        self.author = None
        """ 
        W
        h
        o
        i
        s
        r
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        f
        o
        r
        l
        i
        n
        k
        a
        g
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
        """ 
        I
        t
        e
        m
        t
        o
        b
        e
        l
        i
        n
        k
        e
        d
        .
        List of `LinkageItem` items (represented as `dict` in JSON). """
        
        super(Linkage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Linkage, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("item", "item", LinkageItem, True, None, True),
        ])
        return js


from . import backboneelement

class LinkageItem(backboneelement.BackboneElement):
    """ 
    I
    t
    e
    m
    t
    o
    b
    e
    l
    i
    n
    k
    e
    d
    .
    
    
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
    i
    c
    h
    r
    e
    c
    o
    r
    d
    c
    o
    n
    s
    i
    d
    e
    r
    e
    d
    a
    s
    t
    h
    e
    r
    e
    f
    e
    r
    e
    n
    c
    e
    t
    o
    t
    h
    e
    s
    a
    m
    e
    r
    e
    a
    l
    -
    w
    o
    r
    l
    d
    o
    c
    c
    u
    r
    r
    e
    n
    c
    e
    a
    s
    w
    e
    l
    l
    a
    s
    h
    o
    w
    t
    h
    e
    i
    t
    e
    m
    s
    s
    h
    o
    u
    l
    d
    b
    e
    e
    v
    a
    l
    u
    a
    t
    e
    d
    w
    i
    t
    h
    i
    n
    t
    h
    e
    c
    o
    l
    l
    e
    c
    t
    i
    o
    n
    o
    f
    l
    i
    n
    k
    e
    d
    i
    t
    e
    m
    s
    .
    
    """
    
    resource_type = "LinkageItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resource = None
        """ 
        R
        e
        s
        o
        u
        r
        c
        e
        b
        e
        i
        n
        g
        l
        i
        n
        k
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        s
        o
        u
        r
        c
        e
        |
        a
        l
        t
        e
        r
        n
        a
        t
        e
        |
        h
        i
        s
        t
        o
        r
        i
        c
        a
        l
        .
        Type `str`. """
        
        super(LinkageItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LinkageItem, self).elementProperties()
        js.extend([
            ("resource", "resource", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
