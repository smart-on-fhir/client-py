#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CompartmentDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CompartmentDefinition(domainresource.DomainResource):
    """ 
    C
    o
    m
    p
    a
    r
    t
    m
    e
    n
    t
    D
    e
    f
    i
    n
    i
    t
    i
    o
    n
    f
    o
    r
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
    
    
    A
    c
    o
    m
    p
    a
    r
    t
    m
    e
    n
    t
    d
    e
    f
    i
    n
    i
    t
    i
    o
    n
    t
    h
    a
    t
    d
    e
    f
    i
    n
    e
    s
    h
    o
    w
    r
    e
    s
    o
    u
    r
    c
    e
    s
    a
    r
    e
    a
    c
    c
    e
    s
    s
    e
    d
    o
    n
    a
    s
    e
    r
    v
    e
    r
    .
    
    """
    
    resource_type = "CompartmentDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        |
        E
        n
        c
        o
        u
        n
        t
        e
        r
        |
        R
        e
        l
        a
        t
        e
        d
        P
        e
        r
        s
        o
        n
        |
        P
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        |
        D
        e
        v
        i
        c
        e
        .
        Type `str`. """
        
        self.contact = None
        """ 
        C
        o
        n
        t
        a
        c
        t
        d
        e
        t
        a
        i
        l
        s
        f
        o
        r
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        D
        a
        t
        e
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
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
        d
        e
        s
        c
        r
        i
        p
        t
        i
        o
        n
        o
        f
        t
        h
        e
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.experimental = None
        """ 
        F
        o
        r
        t
        e
        s
        t
        i
        n
        g
        p
        u
        r
        p
        o
        s
        e
        s
        ,
        n
        o
        t
        r
        e
        a
        l
        u
        s
        a
        g
        e
        .
        Type `bool`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        (
        c
        o
        m
        p
        u
        t
        e
        r
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.publisher = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        (
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
        o
        r
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        )
        .
        Type `str`. """
        
        self.purpose = None
        """ 
        W
        h
        y
        t
        h
        i
        s
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        i
        s
        d
        e
        f
        i
        n
        e
        d
        .
        Type `str`. """
        
        self.resource = None
        """ 
        H
        o
        w
        a
        r
        e
        s
        o
        u
        r
        c
        e
        i
        s
        r
        e
        l
        a
        t
        e
        d
        t
        o
        t
        h
        e
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        .
        List of `CompartmentDefinitionResource` items (represented as `dict` in JSON). """
        
        self.search = None
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
        e
        s
        e
        a
        r
        c
        h
        s
        y
        n
        t
        a
        x
        i
        s
        s
        u
        p
        p
        o
        r
        t
        e
        d
        .
        Type `bool`. """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        a
        c
        t
        i
        v
        e
        |
        r
        e
        t
        i
        r
        e
        d
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        self.url = None
        """ 
        C
        a
        n
        o
        n
        i
        c
        a
        l
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        ,
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
        a
        s
        a
        U
        R
        I
        (
        g
        l
        o
        b
        a
        l
        l
        y
        u
        n
        i
        q
        u
        e
        )
        .
        Type `str`. """
        
        self.useContext = None
        """ 
        T
        h
        e
        c
        o
        n
        t
        e
        x
        t
        t
        h
        a
        t
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
        i
        s
        i
        n
        t
        e
        n
        d
        e
        d
        t
        o
        s
        u
        p
        p
        o
        r
        t
        .
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        v
        e
        r
        s
        i
        o
        n
        o
        f
        t
        h
        e
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(CompartmentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompartmentDefinition, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("resource", "resource", CompartmentDefinitionResource, True, None, False),
            ("search", "search", bool, False, None, True),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """ 
    H
    o
    w
    a
    r
    e
    s
    o
    u
    r
    c
    e
    i
    s
    r
    e
    l
    a
    t
    e
    d
    t
    o
    t
    h
    e
    c
    o
    m
    p
    a
    r
    t
    m
    e
    n
    t
    .
    
    
    I
    n
    f
    o
    r
    m
    a
    t
    i
    o
    n
    a
    b
    o
    u
    t
    h
    o
    w
    a
    r
    e
    s
    o
    u
    r
    c
    e
    i
    s
    r
    e
    l
    a
    t
    e
    d
    t
    o
    t
    h
    e
    c
    o
    m
    p
    a
    r
    t
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "CompartmentDefinitionResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        N
        a
        m
        e
        o
        f
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
        .
        Type `str`. """
        
        self.documentation = None
        """ 
        A
        d
        d
        i
        t
        i
        o
        n
        a
        l
        d
        o
        c
        u
        m
        e
        n
        t
        a
        t
        i
        o
        n
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
        a
        n
        d
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.param = None
        """ 
        S
        e
        a
        r
        c
        h
        P
        a
        r
        a
        m
        e
        t
        e
        r
        N
        a
        m
        e
        ,
        o
        r
        c
        h
        a
        i
        n
        e
        d
        p
        a
        r
        a
        m
        e
        t
        e
        r
        s
        .
        List of `str` items. """
        
        super(CompartmentDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CompartmentDefinitionResource, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("param", "param", str, True, None, False),
        ])
        return js


import sys
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
