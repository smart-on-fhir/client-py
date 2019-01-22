#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ 
    S
    e
    a
    r
    c
    h
    p
    a
    r
    a
    m
    e
    t
    e
    r
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
    s
    e
    a
    r
    c
    h
    p
    a
    r
    a
    m
    e
    t
    e
    r
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
    a
    n
    a
    m
    e
    d
    s
    e
    a
    r
    c
    h
    i
    t
    e
    m
    t
    h
    a
    t
    c
    a
    n
    b
    e
    u
    s
    e
    d
    t
    o
    s
    e
    a
    r
    c
    h
    /
    f
    i
    l
    t
    e
    r
    o
    n
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
    
    """
    
    resource_type = "SearchParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.base = None
        """ 
        T
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
        y
        p
        e
        (
        s
        )
        t
        h
        i
        s
        s
        e
        a
        r
        c
        h
        p
        a
        r
        a
        m
        e
        t
        e
        r
        a
        p
        p
        l
        i
        e
        s
        t
        o
        .
        List of `str` items. """
        
        self.chain = None
        """ 
        C
        h
        a
        i
        n
        e
        d
        n
        a
        m
        e
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
        List of `str` items. """
        
        self.code = None
        """ 
        C
        o
        d
        e
        u
        s
        e
        d
        i
        n
        U
        R
        L
        .
        Type `str`. """
        
        self.comparator = None
        """ 
        e
        q
        |
        n
        e
        |
        g
        t
        |
        l
        t
        |
        g
        e
        |
        l
        e
        |
        s
        a
        |
        e
        b
        |
        a
        p
        .
        List of `str` items. """
        
        self.component = None
        """ 
        F
        o
        r
        C
        o
        m
        p
        o
        s
        i
        t
        e
        r
        e
        s
        o
        u
        r
        c
        e
        s
        t
        o
        d
        e
        f
        i
        n
        e
        t
        h
        e
        p
        a
        r
        t
        s
        .
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """
        
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
        
        self.derivedFrom = None
        """ 
        O
        r
        i
        g
        i
        n
        a
        l
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
        f
        o
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
        p
        a
        r
        a
        m
        e
        t
        e
        r
        .
        Type `str`. """
        
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
        s
        e
        a
        r
        c
        h
        p
        a
        r
        a
        m
        e
        t
        e
        r
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
        
        self.expression = None
        """ 
        F
        H
        I
        R
        P
        a
        t
        h
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        t
        h
        a
        t
        e
        x
        t
        r
        a
        c
        t
        s
        t
        h
        e
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.jurisdiction = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        j
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        f
        o
        r
        s
        e
        a
        r
        c
        h
        p
        a
        r
        a
        m
        e
        t
        e
        r
        (
        i
        f
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.modifier = None
        """ 
        m
        i
        s
        s
        i
        n
        g
        |
        e
        x
        a
        c
        t
        |
        c
        o
        n
        t
        a
        i
        n
        s
        |
        n
        o
        t
        |
        t
        e
        x
        t
        |
        i
        n
        |
        n
        o
        t
        -
        i
        n
        |
        b
        e
        l
        o
        w
        |
        a
        b
        o
        v
        e
        |
        t
        y
        p
        e
        |
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
        |
        o
        f
        T
        y
        p
        e
        .
        List of `str` items. """
        
        self.multipleAnd = None
        """ 
        A
        l
        l
        o
        w
        m
        u
        l
        t
        i
        p
        l
        e
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
        (
        a
        n
        d
        )
        .
        Type `bool`. """
        
        self.multipleOr = None
        """ 
        A
        l
        l
        o
        w
        m
        u
        l
        t
        i
        p
        l
        e
        v
        a
        l
        u
        e
        s
        p
        e
        r
        p
        a
        r
        a
        m
        e
        t
        e
        r
        (
        o
        r
        )
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
        s
        e
        a
        r
        c
        h
        p
        a
        r
        a
        m
        e
        t
        e
        r
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
        s
        e
        a
        r
        c
        h
        p
        a
        r
        a
        m
        e
        t
        e
        r
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
        
        self.target = None
        """ 
        T
        y
        p
        e
        s
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
        (
        i
        f
        a
        r
        e
        s
        o
        u
        r
        c
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
        )
        .
        List of `str` items. """
        
        self.type = None
        """ 
        n
        u
        m
        b
        e
        r
        |
        d
        a
        t
        e
        |
        s
        t
        r
        i
        n
        g
        |
        t
        o
        k
        e
        n
        |
        r
        e
        f
        e
        r
        e
        n
        c
        e
        |
        c
        o
        m
        p
        o
        s
        i
        t
        e
        |
        q
        u
        a
        n
        t
        i
        t
        y
        |
        u
        r
        i
        |
        s
        p
        e
        c
        i
        a
        l
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
        s
        e
        a
        r
        c
        h
        p
        a
        r
        a
        m
        e
        t
        e
        r
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
        s
        e
        a
        r
        c
        h
        p
        a
        r
        a
        m
        e
        t
        e
        r
        .
        Type `str`. """
        
        self.xpath = None
        """ 
        X
        P
        a
        t
        h
        t
        h
        a
        t
        e
        x
        t
        r
        a
        c
        t
        s
        t
        h
        e
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.xpathUsage = None
        """ 
        n
        o
        r
        m
        a
        l
        |
        p
        h
        o
        n
        e
        t
        i
        c
        |
        n
        e
        a
        r
        b
        y
        |
        d
        i
        s
        t
        a
        n
        c
        e
        |
        o
        t
        h
        e
        r
        .
        Type `str`. """
        
        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", str, True, None, True),
            ("chain", "chain", str, True, None, False),
            ("code", "code", str, False, None, True),
            ("comparator", "comparator", str, True, None, False),
            ("component", "component", SearchParameterComponent, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivedFrom", "derivedFrom", str, False, None, False),
            ("description", "description", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("modifier", "modifier", str, True, None, False),
            ("multipleAnd", "multipleAnd", bool, False, None, False),
            ("multipleOr", "multipleOr", bool, False, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("target", "target", str, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("xpathUsage", "xpathUsage", str, False, None, False),
        ])
        return js


from . import backboneelement

class SearchParameterComponent(backboneelement.BackboneElement):
    """ 
    F
    o
    r
    C
    o
    m
    p
    o
    s
    i
    t
    e
    r
    e
    s
    o
    u
    r
    c
    e
    s
    t
    o
    d
    e
    f
    i
    n
    e
    t
    h
    e
    p
    a
    r
    t
    s
    .
    
    
    U
    s
    e
    d
    t
    o
    d
    e
    f
    i
    n
    e
    t
    h
    e
    p
    a
    r
    t
    s
    o
    f
    a
    c
    o
    m
    p
    o
    s
    i
    t
    e
    s
    e
    a
    r
    c
    h
    p
    a
    r
    a
    m
    e
    t
    e
    r
    .
    
    """
    
    resource_type = "SearchParameterComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ 
        D
        e
        f
        i
        n
        e
        s
        h
        o
        w
        t
        h
        e
        p
        a
        r
        t
        w
        o
        r
        k
        s
        .
        Type `str`. """
        
        self.expression = None
        """ 
        S
        u
        b
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        r
        e
        l
        a
        t
        i
        v
        e
        t
        o
        m
        a
        i
        n
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        .
        Type `str`. """
        
        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("expression", "expression", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
