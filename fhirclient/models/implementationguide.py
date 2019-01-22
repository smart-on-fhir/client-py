#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImplementationGuide) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ImplementationGuide(domainresource.DomainResource):
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
    a
    b
    o
    u
    t
    h
    o
    w
    F
    H
    I
    R
    i
    s
    u
    s
    e
    d
    .
    
    
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
    o
    f
    h
    o
    w
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
    t
    e
    r
    o
    p
    e
    r
    a
    b
    i
    l
    i
    t
    y
    o
    r
    s
    t
    a
    n
    d
    a
    r
    d
    s
    p
    r
    o
    b
    l
    e
    m
    i
    s
    s
    o
    l
    v
    e
    d
    -
    t
    y
    p
    i
    c
    a
    l
    l
    y
    t
    h
    r
    o
    u
    g
    h
    t
    h
    e
    u
    s
    e
    o
    f
    F
    H
    I
    R
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
    T
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
    i
    s
    u
    s
    e
    d
    t
    o
    g
    a
    t
    h
    e
    r
    a
    l
    l
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
    n
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
    g
    u
    i
    d
    e
    i
    n
    t
    o
    a
    l
    o
    g
    i
    c
    a
    l
    w
    h
    o
    l
    e
    a
    n
    d
    t
    o
    p
    u
    b
    l
    i
    s
    h
    a
    c
    o
    m
    p
    u
    t
    a
    b
    l
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
    a
    l
    l
    t
    h
    e
    p
    a
    r
    t
    s
    .
    
    """
    
    resource_type = "ImplementationGuide"
    
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
        
        self.definition = None
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
        n
        e
        e
        d
        e
        d
        t
        o
        b
        u
        i
        l
        d
        t
        h
        e
        I
        G
        .
        Type `ImplementationGuideDefinition` (represented as `dict` in JSON). """
        
        self.dependsOn = None
        """ 
        A
        n
        o
        t
        h
        e
        r
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
        t
        h
        i
        s
        d
        e
        p
        e
        n
        d
        s
        o
        n
        .
        List of `ImplementationGuideDependsOn` items (represented as `dict` in JSON). """
        
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
        g
        u
        i
        d
        e
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
        (
        s
        )
        t
        h
        i
        s
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
        G
        u
        i
        d
        e
        t
        a
        r
        g
        e
        t
        s
        .
        List of `str` items. """
        
        self.global_fhir = None
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
        a
        t
        a
        p
        p
        l
        y
        g
        l
        o
        b
        a
        l
        l
        y
        .
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """
        
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
        g
        u
        i
        d
        e
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
        
        self.license = None
        """ 
        S
        P
        D
        X
        l
        i
        c
        e
        n
        s
        e
        c
        o
        d
        e
        f
        o
        r
        t
        h
        i
        s
        I
        G
        (
        o
        r
        n
        o
        t
        -
        o
        p
        e
        n
        -
        s
        o
        u
        r
        c
        e
        )
        .
        Type `str`. """
        
        self.manifest = None
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
        a
        n
        a
        s
        s
        e
        m
        b
        l
        e
        d
        I
        G
        .
        Type `ImplementationGuideManifest` (represented as `dict` in JSON). """
        
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
        g
        u
        i
        d
        e
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
        
        self.packageId = None
        """ 
        N
        P
        M
        P
        a
        c
        k
        a
        g
        e
        n
        a
        m
        e
        f
        o
        r
        I
        G
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
        g
        u
        i
        d
        e
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
        g
        u
        i
        d
        e
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
        g
        u
        i
        d
        e
        .
        Type `str`. """
        
        super(ImplementationGuide, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", ImplementationGuideDefinition, False, None, False),
            ("dependsOn", "dependsOn", ImplementationGuideDependsOn, True, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, True, None, True),
            ("global_fhir", "global", ImplementationGuideGlobal, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("license", "license", str, False, None, False),
            ("manifest", "manifest", ImplementationGuideManifest, False, None, False),
            ("name", "name", str, False, None, True),
            ("packageId", "packageId", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ImplementationGuideDefinition(backboneelement.BackboneElement):
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
    n
    e
    e
    d
    e
    d
    t
    o
    b
    u
    i
    l
    d
    t
    h
    e
    I
    G
    .
    
    
    T
    h
    e
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
    n
    e
    e
    d
    e
    d
    b
    y
    a
    n
    I
    G
    p
    u
    b
    l
    i
    s
    h
    e
    r
    t
    o
    o
    l
    t
    o
    p
    u
    b
    l
    i
    s
    h
    t
    h
    e
    w
    h
    o
    l
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
    g
    u
    i
    d
    e
    .
    
    """
    
    resource_type = "ImplementationGuideDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.grouping = None
        """ 
        G
        r
        o
        u
        p
        i
        n
        g
        u
        s
        e
        d
        t
        o
        p
        r
        e
        s
        e
        n
        t
        r
        e
        l
        a
        t
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
        i
        n
        t
        h
        e
        I
        G
        .
        List of `ImplementationGuideDefinitionGrouping` items (represented as `dict` in JSON). """
        
        self.page = None
        """ 
        P
        a
        g
        e
        /
        S
        e
        c
        t
        i
        o
        n
        i
        n
        t
        h
        e
        G
        u
        i
        d
        e
        .
        Type `ImplementationGuideDefinitionPage` (represented as `dict` in JSON). """
        
        self.parameter = None
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
        I
        G
        i
        s
        b
        u
        i
        l
        t
        b
        y
        t
        o
        o
        l
        s
        .
        List of `ImplementationGuideDefinitionParameter` items (represented as `dict` in JSON). """
        
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
        i
        n
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
        g
        u
        i
        d
        e
        .
        List of `ImplementationGuideDefinitionResource` items (represented as `dict` in JSON). """
        
        self.template = None
        """ 
        A
        t
        e
        m
        p
        l
        a
        t
        e
        f
        o
        r
        b
        u
        i
        l
        d
        i
        n
        g
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
        List of `ImplementationGuideDefinitionTemplate` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinition, self).elementProperties()
        js.extend([
            ("grouping", "grouping", ImplementationGuideDefinitionGrouping, True, None, False),
            ("page", "page", ImplementationGuideDefinitionPage, False, None, False),
            ("parameter", "parameter", ImplementationGuideDefinitionParameter, True, None, False),
            ("resource", "resource", ImplementationGuideDefinitionResource, True, None, True),
            ("template", "template", ImplementationGuideDefinitionTemplate, True, None, False),
        ])
        return js


class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """ 
    G
    r
    o
    u
    p
    i
    n
    g
    u
    s
    e
    d
    t
    o
    p
    r
    e
    s
    e
    n
    t
    r
    e
    l
    a
    t
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
    i
    n
    t
    h
    e
    I
    G
    .
    
    
    A
    l
    o
    g
    i
    c
    a
    l
    g
    r
    o
    u
    p
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
    s
    .
    L
    o
    g
    i
    c
    a
    l
    g
    r
    o
    u
    p
    s
    c
    a
    n
    b
    e
    u
    s
    e
    d
    w
    h
    e
    n
    b
    u
    i
    l
    d
    i
    n
    g
    p
    a
    g
    e
    s
    .
    
    """
    
    resource_type = "ImplementationGuideDefinitionGrouping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        H
        u
        m
        a
        n
        r
        e
        a
        d
        a
        b
        l
        e
        t
        e
        x
        t
        d
        e
        s
        c
        r
        i
        b
        i
        n
        g
        t
        h
        e
        p
        a
        c
        k
        a
        g
        e
        .
        Type `str`. """
        
        self.name = None
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
        v
        e
        n
        a
        m
        e
        f
        o
        r
        t
        h
        e
        p
        a
        c
        k
        a
        g
        e
        .
        Type `str`. """
        
        super(ImplementationGuideDefinitionGrouping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionGrouping, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """ 
    P
    a
    g
    e
    /
    S
    e
    c
    t
    i
    o
    n
    i
    n
    t
    h
    e
    G
    u
    i
    d
    e
    .
    
    
    A
    p
    a
    g
    e
    /
    s
    e
    c
    t
    i
    o
    n
    i
    n
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
    g
    u
    i
    d
    e
    .
    T
    h
    e
    r
    o
    o
    t
    p
    a
    g
    e
    i
    s
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
    g
    u
    i
    d
    e
    h
    o
    m
    e
    p
    a
    g
    e
    .
    
    """
    
    resource_type = "ImplementationGuideDefinitionPage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.generation = None
        """ 
        h
        t
        m
        l
        |
        m
        a
        r
        k
        d
        o
        w
        n
        |
        x
        m
        l
        |
        g
        e
        n
        e
        r
        a
        t
        e
        d
        .
        Type `str`. """
        
        self.nameReference = None
        """ 
        W
        h
        e
        r
        e
        t
        o
        f
        i
        n
        d
        t
        h
        a
        t
        p
        a
        g
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.nameUrl = None
        """ 
        W
        h
        e
        r
        e
        t
        o
        f
        i
        n
        d
        t
        h
        a
        t
        p
        a
        g
        e
        .
        Type `str`. """
        
        self.page = None
        """ 
        N
        e
        s
        t
        e
        d
        P
        a
        g
        e
        s
        /
        S
        e
        c
        t
        i
        o
        n
        s
        .
        List of `ImplementationGuideDefinitionPage` items (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        S
        h
        o
        r
        t
        t
        i
        t
        l
        e
        s
        h
        o
        w
        n
        f
        o
        r
        n
        a
        v
        i
        g
        a
        t
        i
        o
        n
        a
        l
        a
        s
        s
        i
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        super(ImplementationGuideDefinitionPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionPage, self).elementProperties()
        js.extend([
            ("generation", "generation", str, False, None, True),
            ("nameReference", "nameReference", fhirreference.FHIRReference, False, "name", True),
            ("nameUrl", "nameUrl", str, False, "name", True),
            ("page", "page", ImplementationGuideDefinitionPage, True, None, False),
            ("title", "title", str, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
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
    I
    G
    i
    s
    b
    u
    i
    l
    t
    b
    y
    t
    o
    o
    l
    s
    .
    """
    
    resource_type = "ImplementationGuideDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        a
        p
        p
        l
        y
        |
        p
        a
        t
        h
        -
        r
        e
        s
        o
        u
        r
        c
        e
        |
        p
        a
        t
        h
        -
        p
        a
        g
        e
        s
        |
        p
        a
        t
        h
        -
        t
        x
        -
        c
        a
        c
        h
        e
        |
        e
        x
        p
        a
        n
        s
        i
        o
        n
        -
        p
        a
        r
        a
        m
        e
        t
        e
        r
        |
        r
        u
        l
        e
        -
        b
        r
        o
        k
        e
        n
        -
        l
        i
        n
        k
        s
        |
        g
        e
        n
        e
        r
        a
        t
        e
        -
        x
        m
        l
        |
        g
        e
        n
        e
        r
        a
        t
        e
        -
        j
        s
        o
        n
        |
        g
        e
        n
        e
        r
        a
        t
        e
        -
        t
        u
        r
        t
        l
        e
        |
        h
        t
        m
        l
        -
        t
        e
        m
        p
        l
        a
        t
        e
        .
        Type `str`. """
        
        self.value = None
        """ 
        V
        a
        l
        u
        e
        f
        o
        r
        n
        a
        m
        e
        d
        t
        y
        p
        e
        .
        Type `str`. """
        
        super(ImplementationGuideDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionParameter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """ 
    R
    e
    s
    o
    u
    r
    c
    e
    i
    n
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
    g
    u
    i
    d
    e
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
    i
    s
    p
    a
    r
    t
    o
    f
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
    g
    u
    i
    d
    e
    .
    C
    o
    n
    f
    o
    r
    m
    a
    n
    c
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
    (
    v
    a
    l
    u
    e
    s
    e
    t
    ,
    s
    t
    r
    u
    c
    t
    u
    r
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
    ,
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
    s
    e
    t
    c
    .
    )
    a
    r
    e
    o
    b
    v
    i
    o
    u
    s
    c
    a
    n
    d
    i
    d
    a
    t
    e
    s
    f
    o
    r
    i
    n
    c
    l
    u
    s
    i
    o
    n
    ,
    b
    u
    t
    a
    n
    y
    k
    i
    n
    d
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
    c
    a
    n
    b
    e
    i
    n
    c
    l
    u
    d
    e
    d
    a
    s
    a
    n
    e
    x
    a
    m
    p
    l
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
    
    resource_type = "ImplementationGuideDefinitionResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        R
        e
        a
        s
        o
        n
        w
        h
        y
        i
        n
        c
        l
        u
        d
        e
        d
        i
        n
        g
        u
        i
        d
        e
        .
        Type `str`. """
        
        self.exampleBoolean = None
        """ 
        I
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        /
        W
        h
        a
        t
        i
        s
        t
        h
        i
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        o
        f
        ?
        .
        Type `bool`. """
        
        self.exampleCanonical = None
        """ 
        I
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        /
        W
        h
        a
        t
        i
        s
        t
        h
        i
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        o
        f
        ?
        .
        Type `str`. """
        
        self.fhirVersion = None
        """ 
        V
        e
        r
        s
        i
        o
        n
        s
        t
        h
        i
        s
        a
        p
        p
        l
        i
        e
        s
        t
        o
        (
        i
        f
        d
        i
        f
        f
        e
        r
        e
        n
        t
        t
        o
        I
        G
        )
        .
        List of `str` items. """
        
        self.groupingId = None
        """ 
        G
        r
        o
        u
        p
        i
        n
        g
        t
        h
        i
        s
        i
        s
        p
        a
        r
        t
        o
        f
        .
        Type `str`. """
        
        self.name = None
        """ 
        H
        u
        m
        a
        n
        N
        a
        m
        e
        f
        o
        r
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
        Type `str`. """
        
        self.reference = None
        """ 
        L
        o
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
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ImplementationGuideDefinitionResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionResource, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("fhirVersion", "fhirVersion", str, True, None, False),
            ("groupingId", "groupingId", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """ 
    A
    t
    e
    m
    p
    l
    a
    t
    e
    f
    o
    r
    b
    u
    i
    l
    d
    i
    n
    g
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
    """
    
    resource_type = "ImplementationGuideDefinitionTemplate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
        t
        e
        m
        p
        l
        a
        t
        e
        s
        p
        e
        c
        i
        f
        i
        e
        d
        .
        Type `str`. """
        
        self.scope = None
        """ 
        T
        h
        e
        s
        c
        o
        p
        e
        i
        n
        w
        h
        i
        c
        h
        t
        h
        e
        t
        e
        m
        p
        l
        a
        t
        e
        a
        p
        p
        l
        i
        e
        s
        .
        Type `str`. """
        
        self.source = None
        """ 
        T
        h
        e
        s
        o
        u
        r
        c
        e
        l
        o
        c
        a
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
        t
        e
        m
        p
        l
        a
        t
        e
        .
        Type `str`. """
        
        super(ImplementationGuideDefinitionTemplate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDefinitionTemplate, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("scope", "scope", str, False, None, False),
            ("source", "source", str, False, None, True),
        ])
        return js


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """ 
    A
    n
    o
    t
    h
    e
    r
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
    t
    h
    i
    s
    d
    e
    p
    e
    n
    d
    s
    o
    n
    .
    
    
    A
    n
    o
    t
    h
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
    g
    u
    i
    d
    e
    t
    h
    a
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
    a
    t
    i
    o
    n
    d
    e
    p
    e
    n
    d
    s
    o
    n
    .
    T
    y
    p
    i
    c
    a
    l
    l
    y
    ,
    a
    n
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
    g
    u
    i
    d
    e
    u
    s
    e
    s
    v
    a
    l
    u
    e
    s
    e
    t
    s
    ,
    p
    r
    o
    f
    i
    l
    e
    s
    e
    t
    c
    .
    d
    e
    f
    i
    n
    e
    d
    i
    n
    o
    t
    h
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
    g
    u
    i
    d
    e
    s
    .
    
    """
    
    resource_type = "ImplementationGuideDependsOn"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.packageId = None
        """ 
        N
        P
        M
        P
        a
        c
        k
        a
        g
        e
        n
        a
        m
        e
        f
        o
        r
        I
        G
        t
        h
        i
        s
        d
        e
        p
        e
        n
        d
        s
        o
        n
        .
        Type `str`. """
        
        self.uri = None
        """ 
        I
        d
        e
        n
        t
        i
        t
        y
        o
        f
        t
        h
        e
        I
        G
        t
        h
        a
        t
        t
        h
        i
        s
        d
        e
        p
        e
        n
        d
        s
        o
        n
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
        t
        h
        e
        I
        G
        .
        Type `str`. """
        
        super(ImplementationGuideDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideDependsOn, self).elementProperties()
        js.extend([
            ("packageId", "packageId", str, False, None, False),
            ("uri", "uri", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ImplementationGuideGlobal(backboneelement.BackboneElement):
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
    a
    t
    a
    p
    p
    l
    y
    g
    l
    o
    b
    a
    l
    l
    y
    .
    
    
    A
    s
    e
    t
    o
    f
    p
    r
    o
    f
    i
    l
    e
    s
    t
    h
    a
    t
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
    g
    u
    i
    d
    e
    m
    u
    s
    t
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
    
    """
    
    resource_type = "ImplementationGuideGlobal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.profile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        t
        h
        a
        t
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
        m
        u
        s
        t
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
        Type `str`. """
        
        self.type = None
        """ 
        T
        y
        p
        e
        t
        h
        i
        s
        p
        r
        o
        f
        i
        l
        e
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
        Type `str`. """
        
        super(ImplementationGuideGlobal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend([
            ("profile", "profile", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class ImplementationGuideManifest(backboneelement.BackboneElement):
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
    a
    n
    a
    s
    s
    e
    m
    b
    l
    e
    d
    I
    G
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
    a
    n
    a
    s
    s
    e
    m
    b
    l
    e
    d
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
    g
    u
    i
    d
    e
    ,
    c
    r
    e
    a
    t
    e
    d
    b
    y
    t
    h
    e
    p
    u
    b
    l
    i
    c
    a
    t
    i
    o
    n
    t
    o
    o
    l
    i
    n
    g
    .
    
    """
    
    resource_type = "ImplementationGuideManifest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.image = None
        """ 
        I
        m
        a
        g
        e
        w
        i
        t
        h
        i
        n
        t
        h
        e
        I
        G
        .
        List of `str` items. """
        
        self.other = None
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
        l
        i
        n
        k
        a
        b
        l
        e
        f
        i
        l
        e
        i
        n
        I
        G
        .
        List of `str` items. """
        
        self.page = None
        """ 
        H
        T
        M
        L
        p
        a
        g
        e
        w
        i
        t
        h
        i
        n
        t
        h
        e
        p
        a
        r
        e
        n
        t
        I
        G
        .
        List of `ImplementationGuideManifestPage` items (represented as `dict` in JSON). """
        
        self.rendering = None
        """ 
        L
        o
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
        n
        d
        e
        r
        e
        d
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
        g
        u
        i
        d
        e
        .
        Type `str`. """
        
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
        i
        n
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
        g
        u
        i
        d
        e
        .
        List of `ImplementationGuideManifestResource` items (represented as `dict` in JSON). """
        
        super(ImplementationGuideManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifest, self).elementProperties()
        js.extend([
            ("image", "image", str, True, None, False),
            ("other", "other", str, True, None, False),
            ("page", "page", ImplementationGuideManifestPage, True, None, False),
            ("rendering", "rendering", str, False, None, False),
            ("resource", "resource", ImplementationGuideManifestResource, True, None, True),
        ])
        return js


class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """ 
    H
    T
    M
    L
    p
    a
    g
    e
    w
    i
    t
    h
    i
    n
    t
    h
    e
    p
    a
    r
    e
    n
    t
    I
    G
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
    a
    p
    a
    g
    e
    w
    i
    t
    h
    i
    n
    t
    h
    e
    I
    G
    .
    
    """
    
    resource_type = "ImplementationGuideManifestPage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.anchor = None
        """ 
        A
        n
        c
        h
        o
        r
        a
        v
        a
        i
        l
        a
        b
        l
        e
        o
        n
        t
        h
        e
        p
        a
        g
        e
        .
        List of `str` items. """
        
        self.name = None
        """ 
        H
        T
        M
        L
        p
        a
        g
        e
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.title = None
        """ 
        T
        i
        t
        l
        e
        o
        f
        t
        h
        e
        p
        a
        g
        e
        ,
        f
        o
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
        .
        Type `str`. """
        
        super(ImplementationGuideManifestPage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifestPage, self).elementProperties()
        js.extend([
            ("anchor", "anchor", str, True, None, False),
            ("name", "name", str, False, None, True),
            ("title", "title", str, False, None, False),
        ])
        return js


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """ 
    R
    e
    s
    o
    u
    r
    c
    e
    i
    n
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
    g
    u
    i
    d
    e
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
    i
    s
    p
    a
    r
    t
    o
    f
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
    g
    u
    i
    d
    e
    .
    C
    o
    n
    f
    o
    r
    m
    a
    n
    c
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
    (
    v
    a
    l
    u
    e
    s
    e
    t
    ,
    s
    t
    r
    u
    c
    t
    u
    r
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
    ,
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
    s
    e
    t
    c
    .
    )
    a
    r
    e
    o
    b
    v
    i
    o
    u
    s
    c
    a
    n
    d
    i
    d
    a
    t
    e
    s
    f
    o
    r
    i
    n
    c
    l
    u
    s
    i
    o
    n
    ,
    b
    u
    t
    a
    n
    y
    k
    i
    n
    d
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
    c
    a
    n
    b
    e
    i
    n
    c
    l
    u
    d
    e
    d
    a
    s
    a
    n
    e
    x
    a
    m
    p
    l
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
    
    resource_type = "ImplementationGuideManifestResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exampleBoolean = None
        """ 
        I
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        /
        W
        h
        a
        t
        i
        s
        t
        h
        i
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        o
        f
        ?
        .
        Type `bool`. """
        
        self.exampleCanonical = None
        """ 
        I
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        /
        W
        h
        a
        t
        i
        s
        t
        h
        i
        s
        a
        n
        e
        x
        a
        m
        p
        l
        e
        o
        f
        ?
        .
        Type `str`. """
        
        self.reference = None
        """ 
        L
        o
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
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relativePath = None
        """ 
        R
        e
        l
        a
        t
        i
        v
        e
        p
        a
        t
        h
        f
        o
        r
        p
        a
        g
        e
        i
        n
        I
        G
        .
        Type `str`. """
        
        super(ImplementationGuideManifestResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImplementationGuideManifestResource, self).elementProperties()
        js.extend([
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCanonical", "exampleCanonical", str, False, "example", False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("relativePath", "relativePath", str, False, None, False),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
