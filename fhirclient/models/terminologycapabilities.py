#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class TerminologyCapabilities(domainresource.DomainResource):
    """ 
    A
    s
    t
    a
    t
    e
    m
    e
    n
    t
    o
    f
    s
    y
    s
    t
    e
    m
    c
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    .
    
    
    A
    T
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    C
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    r
    e
    s
    o
    u
    r
    c
    e
    d
    o
    c
    u
    m
    e
    n
    t
    s
    a
    s
    e
    t
    o
    f
    c
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    (
    b
    e
    h
    a
    v
    i
    o
    r
    s
    )
    o
    f
    a
    F
    H
    I
    R
    T
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    S
    e
    r
    v
    e
    r
    t
    h
    a
    t
    m
    a
    y
    b
    e
    u
    s
    e
    d
    a
    s
    a
    s
    t
    a
    t
    e
    m
    e
    n
    t
    o
    f
    a
    c
    t
    u
    a
    l
    s
    e
    r
    v
    e
    r
    f
    u
    n
    c
    t
    i
    o
    n
    a
    l
    i
    t
    y
    o
    r
    a
    s
    t
    a
    t
    e
    m
    e
    n
    t
    o
    f
    r
    e
    q
    u
    i
    r
    e
    d
    o
    r
    d
    e
    s
    i
    r
    e
    d
    s
    e
    r
    v
    e
    r
    i
    m
    p
    l
    e
    m
    e
    n
    t
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "TerminologyCapabilities"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.closure = None
        """ 
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
        t
        h
        e
        [
        C
        o
        n
        c
        e
        p
        t
        M
        a
        p
        /
        $
        c
        l
        o
        s
        u
        r
        e
        ]
        (
        c
        o
        n
        c
        e
        p
        t
        m
        a
        p
        -
        o
        p
        e
        r
        a
        t
        i
        o
        n
        -
        c
        l
        o
        s
        u
        r
        e
        .
        h
        t
        m
        l
        )
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `TerminologyCapabilitiesClosure` (represented as `dict` in JSON). """
        
        self.codeSearch = None
        """ 
        e
        x
        p
        l
        i
        c
        i
        t
        |
        a
        l
        l
        .
        Type `str`. """
        
        self.codeSystem = None
        """ 
        A
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        s
        u
        p
        p
        o
        r
        t
        e
        d
        b
        y
        t
        h
        e
        s
        e
        r
        v
        e
        r
        .
        List of `TerminologyCapabilitiesCodeSystem` items (represented as `dict` in JSON). """
        
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
        
        self.copyright = None
        """ 
        U
        s
        e
        a
        n
        d
        /
        o
        r
        p
        u
        b
        l
        i
        s
        h
        i
        n
        g
        r
        e
        s
        t
        r
        i
        c
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
        .
        Type `str`. """
        
        self.expansion = None
        """ 
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
        t
        h
        e
        [
        V
        a
        l
        u
        e
        S
        e
        t
        /
        $
        e
        x
        p
        a
        n
        d
        ]
        (
        v
        a
        l
        u
        e
        s
        e
        t
        -
        o
        p
        e
        r
        a
        t
        i
        o
        n
        -
        e
        x
        p
        a
        n
        d
        .
        h
        t
        m
        l
        )
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `TerminologyCapabilitiesExpansion` (represented as `dict` in JSON). """
        
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
        
        self.implementation = None
        """ 
        I
        f
        t
        h
        i
        s
        d
        e
        s
        c
        r
        i
        b
        e
        s
        a
        s
        p
        e
        c
        i
        f
        i
        c
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `TerminologyCapabilitiesImplementation` (represented as `dict` in JSON). """
        
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
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
        
        self.kind = None
        """ 
        i
        n
        s
        t
        a
        n
        c
        e
        |
        c
        a
        p
        a
        b
        i
        l
        i
        t
        y
        |
        r
        e
        q
        u
        i
        r
        e
        m
        e
        n
        t
        s
        .
        Type `str`. """
        
        self.lockedDate = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        l
        o
        c
        k
        e
        d
        D
        a
        t
        e
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
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
        
        self.software = None
        """ 
        S
        o
        f
        t
        w
        a
        r
        e
        t
        h
        a
        t
        i
        s
        c
        o
        v
        e
        r
        e
        d
        b
        y
        t
        h
        i
        s
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        y
        s
        t
        a
        t
        e
        m
        e
        n
        t
        .
        Type `TerminologyCapabilitiesSoftware` (represented as `dict` in JSON). """
        
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
        
        self.title = None
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
        (
        h
        u
        m
        a
        n
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
        
        self.translation = None
        """ 
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
        t
        h
        e
        [
        C
        o
        n
        c
        e
        p
        t
        M
        a
        p
        /
        $
        t
        r
        a
        n
        s
        l
        a
        t
        e
        ]
        (
        c
        o
        n
        c
        e
        p
        t
        m
        a
        p
        -
        o
        p
        e
        r
        a
        t
        i
        o
        n
        -
        t
        r
        a
        n
        s
        l
        a
        t
        e
        .
        h
        t
        m
        l
        )
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `TerminologyCapabilitiesTranslation` (represented as `dict` in JSON). """
        
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
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
        
        self.validateCode = None
        """ 
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
        t
        h
        e
        [
        V
        a
        l
        u
        e
        S
        e
        t
        /
        $
        v
        a
        l
        i
        d
        a
        t
        e
        -
        c
        o
        d
        e
        ]
        (
        v
        a
        l
        u
        e
        s
        e
        t
        -
        o
        p
        e
        r
        a
        t
        i
        o
        n
        -
        v
        a
        l
        i
        d
        a
        t
        e
        -
        c
        o
        d
        e
        .
        h
        t
        m
        l
        )
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `TerminologyCapabilitiesValidateCode` (represented as `dict` in JSON). """
        
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
        .
        Type `str`. """
        
        super(TerminologyCapabilities, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilities, self).elementProperties()
        js.extend([
            ("closure", "closure", TerminologyCapabilitiesClosure, False, None, False),
            ("codeSearch", "codeSearch", str, False, None, False),
            ("codeSystem", "codeSystem", TerminologyCapabilitiesCodeSystem, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("expansion", "expansion", TerminologyCapabilitiesExpansion, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("implementation", "implementation", TerminologyCapabilitiesImplementation, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("lockedDate", "lockedDate", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("software", "software", TerminologyCapabilitiesSoftware, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("translation", "translation", TerminologyCapabilitiesTranslation, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("validateCode", "validateCode", TerminologyCapabilitiesValidateCode, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class TerminologyCapabilitiesClosure(backboneelement.BackboneElement):
    """ 
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
    t
    h
    e
    [
    C
    o
    n
    c
    e
    p
    t
    M
    a
    p
    /
    $
    c
    l
    o
    s
    u
    r
    e
    ]
    (
    c
    o
    n
    c
    e
    p
    t
    m
    a
    p
    -
    o
    p
    e
    r
    a
    t
    i
    o
    n
    -
    c
    l
    o
    s
    u
    r
    e
    .
    h
    t
    m
    l
    )
    o
    p
    e
    r
    a
    t
    i
    o
    n
    .
    
    
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
    $
    c
    l
    o
    s
    u
    r
    e
    o
    p
    e
    r
    a
    t
    i
    o
    n
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
    
    """
    
    resource_type = "TerminologyCapabilitiesClosure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.translation = None
        """ 
        I
        f
        c
        r
        o
        s
        s
        -
        s
        y
        s
        t
        e
        m
        c
        l
        o
        s
        u
        r
        e
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
        
        super(TerminologyCapabilitiesClosure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesClosure, self).elementProperties()
        js.extend([
            ("translation", "translation", bool, False, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystem(backboneelement.BackboneElement):
    """ 
    A
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    s
    u
    p
    p
    o
    r
    t
    e
    d
    b
    y
    t
    h
    e
    s
    e
    r
    v
    e
    r
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
    a
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    t
    h
    a
    t
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
    b
    y
    t
    h
    e
    s
    e
    r
    v
    e
    r
    .
    I
    f
    t
    h
    e
    r
    e
    i
    s
    a
    n
    o
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    U
    R
    L
    ,
    t
    h
    e
    n
    t
    h
    i
    s
    d
    e
    c
    l
    a
    r
    e
    s
    t
    h
    e
    g
    e
    n
    e
    r
    a
    l
    a
    s
    s
    u
    m
    p
    t
    i
    o
    n
    s
    a
    c
    l
    i
    e
    n
    t
    c
    a
    n
    m
    a
    k
    e
    a
    b
    o
    u
    t
    s
    u
    p
    p
    o
    r
    t
    f
    o
    r
    a
    n
    y
    C
    o
    d
    e
    S
    y
    s
    t
    e
    m
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
    
    resource_type = "TerminologyCapabilitiesCodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.subsumption = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        s
        u
        b
        s
        u
        m
        p
        t
        i
        o
        n
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
        
        self.uri = None
        """ 
        U
        R
        I
        f
        o
        r
        t
        h
        e
        C
        o
        d
        e
        S
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.version = None
        """ 
        V
        e
        r
        s
        i
        o
        n
        o
        f
        C
        o
        d
        e
        S
        y
        s
        t
        e
        m
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
        List of `TerminologyCapabilitiesCodeSystemVersion` items (represented as `dict` in JSON). """
        
        super(TerminologyCapabilitiesCodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystem, self).elementProperties()
        js.extend([
            ("subsumption", "subsumption", bool, False, None, False),
            ("uri", "uri", str, False, None, False),
            ("version", "version", TerminologyCapabilitiesCodeSystemVersion, True, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystemVersion(backboneelement.BackboneElement):
    """ 
    V
    e
    r
    s
    i
    o
    n
    o
    f
    C
    o
    d
    e
    S
    y
    s
    t
    e
    m
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
    
    
    F
    o
    r
    t
    h
    e
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    ,
    a
    l
    i
    s
    t
    o
    f
    v
    e
    r
    s
    i
    o
    n
    s
    t
    h
    a
    t
    a
    r
    e
    s
    u
    p
    p
    o
    r
    t
    e
    d
    b
    y
    t
    h
    e
    s
    e
    r
    v
    e
    r
    .
    
    """
    
    resource_type = "TerminologyCapabilitiesCodeSystemVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        V
        e
        r
        s
        i
        o
        n
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
        v
        e
        r
        s
        i
        o
        n
        .
        Type `str`. """
        
        self.compositional = None
        """ 
        I
        f
        c
        o
        m
        p
        o
        s
        i
        t
        i
        o
        n
        a
        l
        g
        r
        a
        m
        m
        a
        r
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
        
        self.filter = None
        """ 
        F
        i
        l
        t
        e
        r
        P
        r
        o
        p
        e
        r
        t
        i
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
        List of `TerminologyCapabilitiesCodeSystemVersionFilter` items (represented as `dict` in JSON). """
        
        self.isDefault = None
        """ 
        I
        f
        t
        h
        i
        s
        i
        s
        t
        h
        e
        d
        e
        f
        a
        u
        l
        t
        v
        e
        r
        s
        i
        o
        n
        f
        o
        r
        t
        h
        i
        s
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        .
        Type `bool`. """
        
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
        D
        i
        s
        p
        l
        a
        y
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
        
        self.property = None
        """ 
        P
        r
        o
        p
        e
        r
        t
        i
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
        f
        o
        r
        $
        l
        o
        o
        k
        u
        p
        .
        List of `str` items. """
        
        super(TerminologyCapabilitiesCodeSystemVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersion, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("filter", "filter", TerminologyCapabilitiesCodeSystemVersionFilter, True, None, False),
            ("isDefault", "isDefault", bool, False, None, False),
            ("language", "language", str, True, None, False),
            ("property", "property", str, True, None, False),
        ])
        return js


class TerminologyCapabilitiesCodeSystemVersionFilter(backboneelement.BackboneElement):
    """ 
    F
    i
    l
    t
    e
    r
    P
    r
    o
    p
    e
    r
    t
    i
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
    """
    
    resource_type = "TerminologyCapabilitiesCodeSystemVersionFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        C
        o
        d
        e
        o
        f
        t
        h
        e
        p
        r
        o
        p
        e
        r
        t
        y
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
        Type `str`. """
        
        self.op = None
        """ 
        O
        p
        e
        r
        a
        t
        i
        o
        n
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
        f
        o
        r
        t
        h
        e
        p
        r
        o
        p
        e
        r
        t
        y
        .
        List of `str` items. """
        
        super(TerminologyCapabilitiesCodeSystemVersionFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesCodeSystemVersionFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("op", "op", str, True, None, True),
        ])
        return js


class TerminologyCapabilitiesExpansion(backboneelement.BackboneElement):
    """ 
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
    t
    h
    e
    [
    V
    a
    l
    u
    e
    S
    e
    t
    /
    $
    e
    x
    p
    a
    n
    d
    ]
    (
    v
    a
    l
    u
    e
    s
    e
    t
    -
    o
    p
    e
    r
    a
    t
    i
    o
    n
    -
    e
    x
    p
    a
    n
    d
    .
    h
    t
    m
    l
    )
    o
    p
    e
    r
    a
    t
    i
    o
    n
    .
    """
    
    resource_type = "TerminologyCapabilitiesExpansion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.hierarchical = None
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
        r
        v
        e
        r
        c
        a
        n
        r
        e
        t
        u
        r
        n
        n
        e
        s
        t
        e
        d
        v
        a
        l
        u
        e
        s
        e
        t
        s
        .
        Type `bool`. """
        
        self.incomplete = None
        """ 
        A
        l
        l
        o
        w
        r
        e
        q
        u
        e
        s
        t
        f
        o
        r
        i
        n
        c
        o
        m
        p
        l
        e
        t
        e
        e
        x
        p
        a
        n
        s
        i
        o
        n
        s
        ?
        .
        Type `bool`. """
        
        self.paging = None
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
        r
        v
        e
        r
        s
        u
        p
        p
        o
        r
        t
        s
        p
        a
        g
        i
        n
        g
        o
        n
        e
        x
        p
        a
        n
        s
        i
        o
        n
        .
        Type `bool`. """
        
        self.parameter = None
        """ 
        S
        u
        p
        p
        o
        r
        t
        e
        d
        e
        x
        p
        a
        n
        s
        i
        o
        n
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
        List of `TerminologyCapabilitiesExpansionParameter` items (represented as `dict` in JSON). """
        
        self.textFilter = None
        """ 
        D
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
        e
        x
        t
        s
        e
        a
        r
        c
        h
        i
        n
        g
        w
        o
        r
        k
        s
        .
        Type `str`. """
        
        super(TerminologyCapabilitiesExpansion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansion, self).elementProperties()
        js.extend([
            ("hierarchical", "hierarchical", bool, False, None, False),
            ("incomplete", "incomplete", bool, False, None, False),
            ("paging", "paging", bool, False, None, False),
            ("parameter", "parameter", TerminologyCapabilitiesExpansionParameter, True, None, False),
            ("textFilter", "textFilter", str, False, None, False),
        ])
        return js


class TerminologyCapabilitiesExpansionParameter(backboneelement.BackboneElement):
    """ 
    S
    u
    p
    p
    o
    r
    t
    e
    d
    e
    x
    p
    a
    n
    s
    i
    o
    n
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
    
    resource_type = "TerminologyCapabilitiesExpansionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ 
        D
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
        s
        u
        p
        p
        o
        r
        t
        f
        o
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
        .
        Type `str`. """
        
        self.name = None
        """ 
        E
        x
        p
        a
        n
        s
        i
        o
        n
        P
        a
        r
        a
        m
        e
        t
        e
        r
        n
        a
        m
        e
        .
        Type `str`. """
        
        super(TerminologyCapabilitiesExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesExpansionParameter, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
        ])
        return js


class TerminologyCapabilitiesImplementation(backboneelement.BackboneElement):
    """ 
    I
    f
    t
    h
    i
    s
    d
    e
    s
    c
    r
    i
    b
    e
    s
    a
    s
    p
    e
    c
    i
    f
    i
    c
    i
    n
    s
    t
    a
    n
    c
    e
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
    a
    s
    p
    e
    c
    i
    f
    i
    c
    i
    m
    p
    l
    e
    m
    e
    n
    t
    a
    t
    i
    o
    n
    i
    n
    s
    t
    a
    n
    c
    e
    t
    h
    a
    t
    i
    s
    d
    e
    s
    c
    r
    i
    b
    e
    d
    b
    y
    t
    h
    e
    t
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    c
    a
    p
    a
    b
    i
    l
    i
    t
    y
    s
    t
    a
    t
    e
    m
    e
    n
    t
    -
    i
    .
    e
    .
    a
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    i
    n
    s
    t
    a
    l
    l
    a
    t
    i
    o
    n
    ,
    r
    a
    t
    h
    e
    r
    t
    h
    a
    n
    t
    h
    e
    c
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    o
    f
    a
    s
    o
    f
    t
    w
    a
    r
    e
    p
    r
    o
    g
    r
    a
    m
    .
    
    """
    
    resource_type = "TerminologyCapabilitiesImplementation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        D
        e
        s
        c
        r
        i
        b
        e
        s
        t
        h
        i
        s
        s
        p
        e
        c
        i
        f
        i
        c
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.url = None
        """ 
        B
        a
        s
        e
        U
        R
        L
        f
        o
        r
        t
        h
        e
        i
        m
        p
        l
        e
        m
        e
        n
        t
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(TerminologyCapabilitiesImplementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesImplementation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


class TerminologyCapabilitiesSoftware(backboneelement.BackboneElement):
    """ 
    S
    o
    f
    t
    w
    a
    r
    e
    t
    h
    a
    t
    i
    s
    c
    o
    v
    e
    r
    e
    d
    b
    y
    t
    h
    i
    s
    t
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    c
    a
    p
    a
    b
    i
    l
    i
    t
    y
    s
    t
    a
    t
    e
    m
    e
    n
    t
    .
    
    
    S
    o
    f
    t
    w
    a
    r
    e
    t
    h
    a
    t
    i
    s
    c
    o
    v
    e
    r
    e
    d
    b
    y
    t
    h
    i
    s
    t
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    c
    a
    p
    a
    b
    i
    l
    i
    t
    y
    s
    t
    a
    t
    e
    m
    e
    n
    t
    .
    I
    t
    i
    s
    u
    s
    e
    d
    w
    h
    e
    n
    t
    h
    e
    s
    t
    a
    t
    e
    m
    e
    n
    t
    d
    e
    s
    c
    r
    i
    b
    e
    s
    t
    h
    e
    c
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    o
    f
    a
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    s
    o
    f
    t
    w
    a
    r
    e
    v
    e
    r
    s
    i
    o
    n
    ,
    i
    n
    d
    e
    p
    e
    n
    d
    e
    n
    t
    o
    f
    a
    n
    i
    n
    s
    t
    a
    l
    l
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "TerminologyCapabilitiesSoftware"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ 
        A
        n
        a
        m
        e
        t
        h
        e
        s
        o
        f
        t
        w
        a
        r
        e
        i
        s
        k
        n
        o
        w
        n
        b
        y
        .
        Type `str`. """
        
        self.version = None
        """ 
        V
        e
        r
        s
        i
        o
        n
        c
        o
        v
        e
        r
        e
        d
        b
        y
        t
        h
        i
        s
        s
        t
        a
        t
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        super(TerminologyCapabilitiesSoftware, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class TerminologyCapabilitiesTranslation(backboneelement.BackboneElement):
    """ 
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
    t
    h
    e
    [
    C
    o
    n
    c
    e
    p
    t
    M
    a
    p
    /
    $
    t
    r
    a
    n
    s
    l
    a
    t
    e
    ]
    (
    c
    o
    n
    c
    e
    p
    t
    m
    a
    p
    -
    o
    p
    e
    r
    a
    t
    i
    o
    n
    -
    t
    r
    a
    n
    s
    l
    a
    t
    e
    .
    h
    t
    m
    l
    )
    o
    p
    e
    r
    a
    t
    i
    o
    n
    .
    """
    
    resource_type = "TerminologyCapabilitiesTranslation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.needsMap = None
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
        c
        l
        i
        e
        n
        t
        m
        u
        s
        t
        i
        d
        e
        n
        t
        i
        f
        y
        t
        h
        e
        m
        a
        p
        .
        Type `bool`. """
        
        super(TerminologyCapabilitiesTranslation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesTranslation, self).elementProperties()
        js.extend([
            ("needsMap", "needsMap", bool, False, None, True),
        ])
        return js


class TerminologyCapabilitiesValidateCode(backboneelement.BackboneElement):
    """ 
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
    t
    h
    e
    [
    V
    a
    l
    u
    e
    S
    e
    t
    /
    $
    v
    a
    l
    i
    d
    a
    t
    e
    -
    c
    o
    d
    e
    ]
    (
    v
    a
    l
    u
    e
    s
    e
    t
    -
    o
    p
    e
    r
    a
    t
    i
    o
    n
    -
    v
    a
    l
    i
    d
    a
    t
    e
    -
    c
    o
    d
    e
    .
    h
    t
    m
    l
    )
    o
    p
    e
    r
    a
    t
    i
    o
    n
    .
    """
    
    resource_type = "TerminologyCapabilitiesValidateCode"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.translations = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        r
        a
        n
        s
        l
        a
        t
        i
        o
        n
        s
        a
        r
        e
        v
        a
        l
        i
        d
        a
        t
        e
        d
        .
        Type `bool`. """
        
        super(TerminologyCapabilitiesValidateCode, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TerminologyCapabilitiesValidateCode, self).elementProperties()
        js.extend([
            ("translations", "translations", bool, False, None, True),
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
