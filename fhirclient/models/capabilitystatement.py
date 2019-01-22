#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CapabilityStatement) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CapabilityStatement(domainresource.DomainResource):
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
    C
    a
    p
    a
    b
    i
    l
    i
    t
    y
    S
    t
    a
    t
    e
    m
    e
    n
    t
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
    S
    e
    r
    v
    e
    r
    f
    o
    r
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
    v
    e
    r
    s
    i
    o
    n
    o
    f
    F
    H
    I
    R
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
    
    resource_type = "CapabilityStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        Type `str`. """
        
        self.document = None
        """ 
        D
        o
        c
        u
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
        List of `CapabilityStatementDocument` items (represented as `dict` in JSON). """
        
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
        
        self.fhirVersion = None
        """ 
        F
        H
        I
        R
        V
        e
        r
        s
        i
        o
        n
        t
        h
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
        s
        .
        Type `str`. """
        
        self.format = None
        """ 
        f
        o
        r
        m
        a
        t
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
        (
        x
        m
        l
        |
        j
        s
        o
        n
        |
        t
        t
        l
        |
        m
        i
        m
        e
        t
        y
        p
        e
        )
        .
        List of `str` items. """
        
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
        Type `CapabilityStatementImplementation` (represented as `dict` in JSON). """
        
        self.implementationGuide = None
        """ 
        I
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
        g
        u
        i
        d
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
        
        self.imports = None
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
        U
        R
        L
        o
        f
        a
        n
        o
        t
        h
        e
        r
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
        t
        h
        i
        s
        a
        d
        d
        s
        t
        o
        .
        List of `str` items. """
        
        self.instantiates = None
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
        U
        R
        L
        o
        f
        a
        n
        o
        t
        h
        e
        r
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
        t
        h
        i
        s
        i
        m
        p
        l
        e
        m
        e
        n
        t
        s
        .
        List of `str` items. """
        
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
        
        self.messaging = None
        """ 
        I
        f
        m
        e
        s
        s
        a
        g
        i
        n
        g
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
        List of `CapabilityStatementMessaging` items (represented as `dict` in JSON). """
        
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
        
        self.patchFormat = None
        """ 
        P
        a
        t
        c
        h
        f
        o
        r
        m
        a
        t
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
        
        self.rest = None
        """ 
        I
        f
        t
        h
        e
        e
        n
        d
        p
        o
        i
        n
        t
        i
        s
        a
        R
        E
        S
        T
        f
        u
        l
        o
        n
        e
        .
        List of `CapabilityStatementRest` items (represented as `dict` in JSON). """
        
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
        Type `CapabilityStatementSoftware` (represented as `dict` in JSON). """
        
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
        Type `str`. """
        
        super(CapabilityStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatement, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("document", "document", CapabilityStatementDocument, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, True),
            ("format", "format", str, True, None, True),
            ("implementation", "implementation", CapabilityStatementImplementation, False, None, False),
            ("implementationGuide", "implementationGuide", str, True, None, False),
            ("imports", "imports", str, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("messaging", "messaging", CapabilityStatementMessaging, True, None, False),
            ("name", "name", str, False, None, False),
            ("patchFormat", "patchFormat", str, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("rest", "rest", CapabilityStatementRest, True, None, False),
            ("software", "software", CapabilityStatementSoftware, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class CapabilityStatementDocument(backboneelement.BackboneElement):
    """ 
    D
    o
    c
    u
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
    
    
    A
    d
    o
    c
    u
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
    
    """
    
    resource_type = "CapabilityStatementDocument"
    
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
        d
        o
        c
        u
        m
        e
        n
        t
        s
        u
        p
        p
        o
        r
        t
        .
        Type `str`. """
        
        self.mode = None
        """ 
        p
        r
        o
        d
        u
        c
        e
        r
        |
        c
        o
        n
        s
        u
        m
        e
        r
        .
        Type `str`. """
        
        self.profile = None
        """ 
        C
        o
        n
        s
        t
        r
        a
        i
        n
        t
        o
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
        s
        u
        s
        e
        d
        i
        n
        t
        h
        e
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `str`. """
        
        super(CapabilityStatementDocument, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementDocument, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("profile", "profile", str, False, None, True),
        ])
        return js


class CapabilityStatementImplementation(backboneelement.BackboneElement):
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
    
    resource_type = "CapabilityStatementImplementation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.custodian = None
        """ 
        O
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
        t
        h
        a
        t
        m
        a
        n
        a
        g
        e
        s
        t
        h
        e
        d
        a
        t
        a
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        Type `str`. """
        
        super(CapabilityStatementImplementation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementImplementation, self).elementProperties()
        js.extend([
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


class CapabilityStatementMessaging(backboneelement.BackboneElement):
    """ 
    I
    f
    m
    e
    s
    s
    a
    g
    i
    n
    g
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
    
    
    A
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
    m
    e
    s
    s
    a
    g
    i
    n
    g
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
    t
    h
    e
    s
    o
    l
    u
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "CapabilityStatementMessaging"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ 
        M
        e
        s
        s
        a
        g
        i
        n
        g
        i
        n
        t
        e
        r
        f
        a
        c
        e
        b
        e
        h
        a
        v
        i
        o
        r
        d
        e
        t
        a
        i
        l
        s
        .
        Type `str`. """
        
        self.endpoint = None
        """ 
        W
        h
        e
        r
        e
        m
        e
        s
        s
        a
        g
        e
        s
        s
        h
        o
        u
        l
        d
        b
        e
        s
        e
        n
        t
        .
        List of `CapabilityStatementMessagingEndpoint` items (represented as `dict` in JSON). """
        
        self.reliableCache = None
        """ 
        R
        e
        l
        i
        a
        b
        l
        e
        M
        e
        s
        s
        a
        g
        e
        C
        a
        c
        h
        e
        L
        e
        n
        g
        t
        h
        (
        m
        i
        n
        )
        .
        Type `int`. """
        
        self.supportedMessage = None
        """ 
        M
        e
        s
        s
        a
        g
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
        b
        y
        t
        h
        i
        s
        s
        y
        s
        t
        e
        m
        .
        List of `CapabilityStatementMessagingSupportedMessage` items (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessaging, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("endpoint", "endpoint", CapabilityStatementMessagingEndpoint, True, None, False),
            ("reliableCache", "reliableCache", int, False, None, False),
            ("supportedMessage", "supportedMessage", CapabilityStatementMessagingSupportedMessage, True, None, False),
        ])
        return js


class CapabilityStatementMessagingEndpoint(backboneelement.BackboneElement):
    """ 
    W
    h
    e
    r
    e
    m
    e
    s
    s
    a
    g
    e
    s
    s
    h
    o
    u
    l
    d
    b
    e
    s
    e
    n
    t
    .
    
    
    A
    n
    e
    n
    d
    p
    o
    i
    n
    t
    (
    n
    e
    t
    w
    o
    r
    k
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
    a
    d
    d
    r
    e
    s
    s
    )
    t
    o
    w
    h
    i
    c
    h
    m
    e
    s
    s
    a
    g
    e
    s
    a
    n
    d
    /
    o
    r
    r
    e
    p
    l
    i
    e
    s
    a
    r
    e
    t
    o
    b
    e
    s
    e
    n
    t
    .
    
    """
    
    resource_type = "CapabilityStatementMessagingEndpoint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ 
        N
        e
        t
        w
        o
        r
        k
        a
        d
        d
        r
        e
        s
        s
        o
        r
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
        o
        f
        t
        h
        e
        e
        n
        d
        -
        p
        o
        i
        n
        t
        .
        Type `str`. """
        
        self.protocol = None
        """ 
        h
        t
        t
        p
        |
        f
        t
        p
        |
        m
        l
        l
        p
        +
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        super(CapabilityStatementMessagingEndpoint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingEndpoint, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, True),
            ("protocol", "protocol", coding.Coding, False, None, True),
        ])
        return js


class CapabilityStatementMessagingSupportedMessage(backboneelement.BackboneElement):
    """ 
    M
    e
    s
    s
    a
    g
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
    b
    y
    t
    h
    i
    s
    s
    y
    s
    t
    e
    m
    .
    
    
    R
    e
    f
    e
    r
    e
    n
    c
    e
    s
    t
    o
    m
    e
    s
    s
    a
    g
    e
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
    s
    f
    o
    r
    m
    e
    s
    s
    a
    g
    e
    s
    t
    h
    i
    s
    s
    y
    s
    t
    e
    m
    c
    a
    n
    s
    e
    n
    d
    o
    r
    r
    e
    c
    e
    i
    v
    e
    .
    
    """
    
    resource_type = "CapabilityStatementMessagingSupportedMessage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ 
        M
        e
        s
        s
        a
        g
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
        i
        s
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.mode = None
        """ 
        s
        e
        n
        d
        e
        r
        |
        r
        e
        c
        e
        i
        v
        e
        r
        .
        Type `str`. """
        
        super(CapabilityStatementMessagingSupportedMessage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementMessagingSupportedMessage, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("mode", "mode", str, False, None, True),
        ])
        return js


class CapabilityStatementRest(backboneelement.BackboneElement):
    """ 
    I
    f
    t
    h
    e
    e
    n
    d
    p
    o
    i
    n
    t
    i
    s
    a
    R
    E
    S
    T
    f
    u
    l
    o
    n
    e
    .
    
    
    A
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
    o
    f
    t
    h
    e
    r
    e
    s
    t
    f
    u
    l
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
    t
    h
    e
    s
    o
    l
    u
    t
    i
    o
    n
    ,
    i
    f
    a
    n
    y
    .
    
    """
    
    resource_type = "CapabilityStatementRest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
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
        s
        s
        e
        r
        v
        e
        d
        /
        u
        s
        e
        d
        b
        y
        s
        y
        s
        t
        e
        m
        .
        List of `str` items. """
        
        self.documentation = None
        """ 
        G
        e
        n
        e
        r
        a
        l
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
        
        self.interaction = None
        """ 
        W
        h
        a
        t
        o
        p
        e
        r
        a
        t
        i
        o
        n
        s
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
        ?
        .
        List of `CapabilityStatementRestInteraction` items (represented as `dict` in JSON). """
        
        self.mode = None
        """ 
        c
        l
        i
        e
        n
        t
        |
        s
        e
        r
        v
        e
        r
        .
        Type `str`. """
        
        self.operation = None
        """ 
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
        o
        f
        a
        s
        y
        s
        t
        e
        m
        l
        e
        v
        e
        l
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
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        
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
        s
        e
        r
        v
        e
        d
        o
        n
        t
        h
        e
        R
        E
        S
        T
        i
        n
        t
        e
        r
        f
        a
        c
        e
        .
        List of `CapabilityStatementRestResource` items (represented as `dict` in JSON). """
        
        self.searchParam = None
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
        s
        f
        o
        r
        s
        e
        a
        r
        c
        h
        i
        n
        g
        a
        l
        l
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
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.security = None
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
        s
        e
        c
        u
        r
        i
        t
        y
        o
        f
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
        Type `CapabilityStatementRestSecurity` (represented as `dict` in JSON). """
        
        super(CapabilityStatementRest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRest, self).elementProperties()
        js.extend([
            ("compartment", "compartment", str, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestInteraction, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("resource", "resource", CapabilityStatementRestResource, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("security", "security", CapabilityStatementRestSecurity, False, None, False),
        ])
        return js


class CapabilityStatementRestInteraction(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    o
    p
    e
    r
    a
    t
    i
    o
    n
    s
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
    ?
    .
    
    
    A
    s
    p
    e
    c
    i
    f
    i
    c
    a
    t
    i
    o
    n
    o
    f
    r
    e
    s
    t
    f
    u
    l
    o
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
    b
    y
    t
    h
    e
    s
    y
    s
    t
    e
    m
    .
    
    """
    
    resource_type = "CapabilityStatementRestInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        |
        b
        a
        t
        c
        h
        |
        s
        e
        a
        r
        c
        h
        -
        s
        y
        s
        t
        e
        m
        |
        h
        i
        s
        t
        o
        r
        y
        -
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.documentation = None
        """ 
        A
        n
        y
        t
        h
        i
        n
        g
        s
        p
        e
        c
        i
        a
        l
        a
        b
        o
        u
        t
        o
        p
        e
        r
        a
        t
        i
        o
        n
        b
        e
        h
        a
        v
        i
        o
        r
        .
        Type `str`. """
        
        super(CapabilityStatementRestInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class CapabilityStatementRestResource(backboneelement.BackboneElement):
    """ 
    R
    e
    s
    o
    u
    r
    c
    e
    s
    e
    r
    v
    e
    d
    o
    n
    t
    h
    e
    R
    E
    S
    T
    i
    n
    t
    e
    r
    f
    a
    c
    e
    .
    
    
    A
    s
    p
    e
    c
    i
    f
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
    s
    t
    f
    u
    l
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
    t
    h
    e
    s
    o
    l
    u
    t
    i
    o
    n
    f
    o
    r
    a
    s
    p
    e
    c
    i
    f
    i
    c
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
    
    """
    
    resource_type = "CapabilityStatementRestResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conditionalCreate = None
        """ 
        I
        f
        a
        l
        l
        o
        w
        s
        /
        u
        s
        e
        s
        c
        o
        n
        d
        i
        t
        i
        o
        n
        a
        l
        c
        r
        e
        a
        t
        e
        .
        Type `bool`. """
        
        self.conditionalDelete = None
        """ 
        n
        o
        t
        -
        s
        u
        p
        p
        o
        r
        t
        e
        d
        |
        s
        i
        n
        g
        l
        e
        |
        m
        u
        l
        t
        i
        p
        l
        e
        -
        h
        o
        w
        c
        o
        n
        d
        i
        t
        i
        o
        n
        a
        l
        d
        e
        l
        e
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
        Type `str`. """
        
        self.conditionalRead = None
        """ 
        n
        o
        t
        -
        s
        u
        p
        p
        o
        r
        t
        e
        d
        |
        m
        o
        d
        i
        f
        i
        e
        d
        -
        s
        i
        n
        c
        e
        |
        n
        o
        t
        -
        m
        a
        t
        c
        h
        |
        f
        u
        l
        l
        -
        s
        u
        p
        p
        o
        r
        t
        .
        Type `str`. """
        
        self.conditionalUpdate = None
        """ 
        I
        f
        a
        l
        l
        o
        w
        s
        /
        u
        s
        e
        s
        c
        o
        n
        d
        i
        t
        i
        o
        n
        a
        l
        u
        p
        d
        a
        t
        e
        .
        Type `bool`. """
        
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
        i
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
        u
        s
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
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.interaction = None
        """ 
        W
        h
        a
        t
        o
        p
        e
        r
        a
        t
        i
        o
        n
        s
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
        ?
        .
        List of `CapabilityStatementRestResourceInteraction` items (represented as `dict` in JSON). """
        
        self.operation = None
        """ 
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
        o
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
        List of `CapabilityStatementRestResourceOperation` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ 
        B
        a
        s
        e
        S
        y
        s
        t
        e
        m
        p
        r
        o
        f
        i
        l
        e
        f
        o
        r
        a
        l
        l
        u
        s
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
        .
        Type `str`. """
        
        self.readHistory = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        v
        R
        e
        a
        d
        c
        a
        n
        r
        e
        t
        u
        r
        n
        p
        a
        s
        t
        v
        e
        r
        s
        i
        o
        n
        s
        .
        Type `bool`. """
        
        self.referencePolicy = None
        """ 
        l
        i
        t
        e
        r
        a
        l
        |
        l
        o
        g
        i
        c
        a
        l
        |
        r
        e
        s
        o
        l
        v
        e
        s
        |
        e
        n
        f
        o
        r
        c
        e
        d
        |
        l
        o
        c
        a
        l
        .
        List of `str` items. """
        
        self.searchInclude = None
        """ 
        _
        i
        n
        c
        l
        u
        d
        e
        v
        a
        l
        u
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
        List of `str` items. """
        
        self.searchParam = None
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
        List of `CapabilityStatementRestResourceSearchParam` items (represented as `dict` in JSON). """
        
        self.searchRevInclude = None
        """ 
        _
        r
        e
        v
        i
        n
        c
        l
        u
        d
        e
        v
        a
        l
        u
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
        List of `str` items. """
        
        self.supportedProfile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        s
        f
        o
        r
        u
        s
        e
        c
        a
        s
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
        
        self.type = None
        """ 
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
        y
        p
        e
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
        .
        Type `str`. """
        
        self.updateCreate = None
        """ 
        I
        f
        u
        p
        d
        a
        t
        e
        c
        a
        n
        c
        o
        m
        m
        i
        t
        t
        o
        a
        n
        e
        w
        i
        d
        e
        n
        t
        i
        t
        y
        .
        Type `bool`. """
        
        self.versioning = None
        """ 
        n
        o
        -
        v
        e
        r
        s
        i
        o
        n
        |
        v
        e
        r
        s
        i
        o
        n
        e
        d
        |
        v
        e
        r
        s
        i
        o
        n
        e
        d
        -
        u
        p
        d
        a
        t
        e
        .
        Type `str`. """
        
        super(CapabilityStatementRestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResource, self).elementProperties()
        js.extend([
            ("conditionalCreate", "conditionalCreate", bool, False, None, False),
            ("conditionalDelete", "conditionalDelete", str, False, None, False),
            ("conditionalRead", "conditionalRead", str, False, None, False),
            ("conditionalUpdate", "conditionalUpdate", bool, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("interaction", "interaction", CapabilityStatementRestResourceInteraction, True, None, False),
            ("operation", "operation", CapabilityStatementRestResourceOperation, True, None, False),
            ("profile", "profile", str, False, None, False),
            ("readHistory", "readHistory", bool, False, None, False),
            ("referencePolicy", "referencePolicy", str, True, None, False),
            ("searchInclude", "searchInclude", str, True, None, False),
            ("searchParam", "searchParam", CapabilityStatementRestResourceSearchParam, True, None, False),
            ("searchRevInclude", "searchRevInclude", str, True, None, False),
            ("supportedProfile", "supportedProfile", str, True, None, False),
            ("type", "type", str, False, None, True),
            ("updateCreate", "updateCreate", bool, False, None, False),
            ("versioning", "versioning", str, False, None, False),
        ])
        return js


class CapabilityStatementRestResourceInteraction(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    o
    p
    e
    r
    a
    t
    i
    o
    n
    s
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
    ?
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
    r
    e
    s
    t
    f
    u
    l
    o
    p
    e
    r
    a
    t
    i
    o
    n
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
    o
    l
    u
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "CapabilityStatementRestResourceInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        r
        e
        a
        d
        |
        v
        r
        e
        a
        d
        |
        u
        p
        d
        a
        t
        e
        |
        p
        a
        t
        c
        h
        |
        d
        e
        l
        e
        t
        e
        |
        h
        i
        s
        t
        o
        r
        y
        -
        i
        n
        s
        t
        a
        n
        c
        e
        |
        h
        i
        s
        t
        o
        r
        y
        -
        t
        y
        p
        e
        |
        c
        r
        e
        a
        t
        e
        |
        s
        e
        a
        r
        c
        h
        -
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.documentation = None
        """ 
        A
        n
        y
        t
        h
        i
        n
        g
        s
        p
        e
        c
        i
        a
        l
        a
        b
        o
        u
        t
        o
        p
        e
        r
        a
        t
        i
        o
        n
        b
        e
        h
        a
        v
        i
        o
        r
        .
        Type `str`. """
        
        super(CapabilityStatementRestResourceInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceInteraction, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
        ])
        return js


class CapabilityStatementRestResourceOperation(backboneelement.BackboneElement):
    """ 
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
    o
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
    o
    f
    a
    n
    o
    p
    e
    r
    a
    t
    i
    o
    n
    o
    r
    a
    n
    a
    m
    e
    d
    q
    u
    e
    r
    y
    t
    o
    g
    e
    t
    h
    e
    r
    w
    i
    t
    h
    i
    t
    s
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
    a
    n
    d
    t
    h
    e
    i
    r
    m
    e
    a
    n
    i
    n
    g
    a
    n
    d
    t
    y
    p
    e
    .
    C
    o
    n
    s
    u
    l
    t
    t
    h
    e
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
    o
    f
    t
    h
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
    f
    o
    r
    d
    e
    t
    a
    i
    l
    s
    a
    b
    o
    u
    t
    h
    o
    w
    t
    o
    i
    n
    v
    o
    k
    e
    t
    h
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
    ,
    a
    n
    d
    t
    h
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
    .
    
    """
    
    resource_type = "CapabilityStatementRestResourceOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ 
        T
        h
        e
        d
        e
        f
        i
        n
        e
        d
        o
        p
        e
        r
        a
        t
        i
        o
        n
        /
        q
        u
        e
        r
        y
        .
        Type `str`. """
        
        self.documentation = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        d
        e
        t
        a
        i
        l
        s
        a
        b
        o
        u
        t
        o
        p
        e
        r
        a
        t
        i
        o
        n
        b
        e
        h
        a
        v
        i
        o
        r
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        b
        y
        w
        h
        i
        c
        h
        t
        h
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
        /
        q
        u
        e
        r
        y
        i
        s
        i
        n
        v
        o
        k
        e
        d
        .
        Type `str`. """
        
        super(CapabilityStatementRestResourceOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceOperation, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, True),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
        ])
        return js


class CapabilityStatementRestResourceSearchParam(backboneelement.BackboneElement):
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
    s
    f
    o
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
    s
    t
    o
    s
    u
    p
    p
    o
    r
    t
    a
    n
    d
    /
    o
    r
    m
    a
    k
    e
    u
    s
    e
    o
    f
    -
    e
    i
    t
    h
    e
    r
    r
    e
    f
    e
    r
    e
    n
    c
    e
    s
    t
    o
    o
    n
    e
    s
    d
    e
    f
    i
    n
    e
    d
    i
    n
    t
    h
    e
    s
    p
    e
    c
    i
    f
    i
    c
    a
    t
    i
    o
    n
    ,
    o
    r
    a
    d
    d
    i
    t
    i
    o
    n
    a
    l
    o
    n
    e
    s
    d
    e
    f
    i
    n
    e
    d
    f
    o
    r
    /
    b
    y
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
    
    """
    
    resource_type = "CapabilityStatementRestResourceSearchParam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definition = None
        """ 
        S
        o
        u
        r
        c
        e
        o
        f
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
        
        self.documentation = None
        """ 
        S
        e
        r
        v
        e
        r
        -
        s
        p
        e
        c
        i
        f
        i
        c
        u
        s
        a
        g
        e
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        f
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
        
        super(CapabilityStatementRestResourceSearchParam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestResourceSearchParam, self).elementProperties()
        js.extend([
            ("definition", "definition", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class CapabilityStatementRestSecurity(backboneelement.BackboneElement):
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
    s
    e
    c
    u
    r
    i
    t
    y
    o
    f
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
    s
    e
    c
    u
    r
    i
    t
    y
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
    f
    r
    o
    m
    a
    n
    i
    n
    t
    e
    r
    f
    a
    c
    e
    p
    e
    r
    s
    p
    e
    c
    t
    i
    v
    e
    -
    w
    h
    a
    t
    a
    c
    l
    i
    e
    n
    t
    n
    e
    e
    d
    s
    t
    o
    k
    n
    o
    w
    .
    
    """
    
    resource_type = "CapabilityStatementRestSecurity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cors = None
        """ 
        A
        d
        d
        s
        C
        O
        R
        S
        H
        e
        a
        d
        e
        r
        s
        (
        h
        t
        t
        p
        :
        /
        /
        e
        n
        a
        b
        l
        e
        -
        c
        o
        r
        s
        .
        o
        r
        g
        /
        )
        .
        Type `bool`. """
        
        self.description = None
        """ 
        G
        e
        n
        e
        r
        a
        l
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
        h
        o
        w
        s
        e
        c
        u
        r
        i
        t
        y
        w
        o
        r
        k
        s
        .
        Type `str`. """
        
        self.service = None
        """ 
        O
        A
        u
        t
        h
        |
        S
        M
        A
        R
        T
        -
        o
        n
        -
        F
        H
        I
        R
        |
        N
        T
        L
        M
        |
        B
        a
        s
        i
        c
        |
        K
        e
        r
        b
        e
        r
        o
        s
        |
        C
        e
        r
        t
        i
        f
        i
        c
        a
        t
        e
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(CapabilityStatementRestSecurity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementRestSecurity, self).elementProperties()
        js.extend([
            ("cors", "cors", bool, False, None, False),
            ("description", "description", str, False, None, False),
            ("service", "service", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class CapabilityStatementSoftware(backboneelement.BackboneElement):
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
    
    resource_type = "CapabilityStatementSoftware"
    
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
        
        self.releaseDate = None
        """ 
        D
        a
        t
        e
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
        w
        a
        s
        r
        e
        l
        e
        a
        s
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        
        super(CapabilityStatementSoftware, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CapabilityStatementSoftware, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("releaseDate", "releaseDate", fhirdate.FHIRDate, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
