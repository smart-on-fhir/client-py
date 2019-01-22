#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TestScript) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class TestScript(domainresource.DomainResource):
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
    a
    s
    e
    t
    o
    f
    t
    e
    s
    t
    s
    .
    
    
    A
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
    s
    e
    t
    o
    f
    t
    e
    s
    t
    s
    a
    g
    a
    i
    n
    s
    t
    a
    F
    H
    I
    R
    s
    e
    r
    v
    e
    r
    o
    r
    c
    l
    i
    e
    n
    t
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
    t
    o
    d
    e
    t
    e
    r
    m
    i
    n
    e
    c
    o
    m
    p
    l
    i
    a
    n
    c
    e
    a
    g
    a
    i
    n
    s
    t
    t
    h
    e
    F
    H
    I
    R
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
    .
    
    """
    
    resource_type = "TestScript"
    
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
        t
        e
        s
        t
        s
        c
        r
        i
        p
        t
        .
        Type `str`. """
        
        self.destination = None
        """ 
        A
        n
        a
        b
        s
        t
        r
        a
        c
        t
        s
        e
        r
        v
        e
        r
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
        d
        e
        s
        t
        i
        n
        a
        t
        i
        o
        n
        o
        r
        r
        e
        c
        e
        i
        v
        e
        r
        i
        n
        a
        m
        e
        s
        s
        a
        g
        e
        e
        x
        c
        h
        a
        n
        g
        e
        .
        List of `TestScriptDestination` items (represented as `dict` in JSON). """
        
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
        
        self.fixture = None
        """ 
        F
        i
        x
        t
        u
        r
        e
        i
        n
        t
        h
        e
        t
        e
        s
        t
        s
        c
        r
        i
        p
        t
        -
        b
        y
        r
        e
        f
        e
        r
        e
        n
        c
        e
        (
        u
        r
        i
        )
        .
        List of `TestScriptFixture` items (represented as `dict` in JSON). """
        
        self.identifier = None
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
        e
        t
        e
        s
        t
        s
        c
        r
        i
        p
        t
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
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
        s
        t
        s
        c
        r
        i
        p
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
        
        self.metadata = None
        """ 
        R
        e
        q
        u
        i
        r
        e
        d
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
        t
        h
        a
        t
        i
        s
        a
        s
        s
        u
        m
        e
        d
        t
        o
        f
        u
        n
        c
        t
        i
        o
        n
        c
        o
        r
        r
        e
        c
        t
        l
        y
        o
        n
        t
        h
        e
        F
        H
        I
        R
        s
        e
        r
        v
        e
        r
        b
        e
        i
        n
        g
        t
        e
        s
        t
        e
        d
        .
        Type `TestScriptMetadata` (represented as `dict` in JSON). """
        
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
        s
        t
        s
        c
        r
        i
        p
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
        
        self.origin = None
        """ 
        A
        n
        a
        b
        s
        t
        r
        a
        c
        t
        s
        e
        r
        v
        e
        r
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
        c
        l
        i
        e
        n
        t
        o
        r
        s
        e
        n
        d
        e
        r
        i
        n
        a
        m
        e
        s
        s
        a
        g
        e
        e
        x
        c
        h
        a
        n
        g
        e
        .
        List of `TestScriptOrigin` items (represented as `dict` in JSON). """
        
        self.profile = None
        """ 
        R
        e
        f
        e
        r
        e
        n
        c
        e
        o
        f
        t
        h
        e
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        p
        r
        o
        f
        i
        l
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        s
        t
        s
        c
        r
        i
        p
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
        
        self.setup = None
        """ 
        A
        s
        e
        r
        i
        e
        s
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
        s
        e
        t
        u
        p
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
        b
        e
        f
        o
        r
        e
        t
        e
        s
        t
        s
        a
        r
        e
        e
        x
        e
        c
        u
        t
        e
        d
        .
        Type `TestScriptSetup` (represented as `dict` in JSON). """
        
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
        
        self.teardown = None
        """ 
        A
        s
        e
        r
        i
        e
        s
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
        c
        l
        e
        a
        n
        u
        p
        s
        t
        e
        p
        s
        .
        Type `TestScriptTeardown` (represented as `dict` in JSON). """
        
        self.test = None
        """ 
        A
        t
        e
        s
        t
        i
        n
        t
        h
        i
        s
        s
        c
        r
        i
        p
        t
        .
        List of `TestScriptTest` items (represented as `dict` in JSON). """
        
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
        s
        t
        s
        c
        r
        i
        p
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
        t
        e
        s
        t
        s
        c
        r
        i
        p
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
        
        self.variable = None
        """ 
        P
        l
        a
        c
        e
        h
        o
        l
        d
        e
        r
        f
        o
        r
        e
        v
        a
        l
        u
        a
        t
        e
        d
        e
        l
        e
        m
        e
        n
        t
        s
        .
        List of `TestScriptVariable` items (represented as `dict` in JSON). """
        
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
        s
        t
        s
        c
        r
        i
        p
        t
        .
        Type `str`. """
        
        super(TestScript, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScript, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("destination", "destination", TestScriptDestination, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fixture", "fixture", TestScriptFixture, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("metadata", "metadata", TestScriptMetadata, False, None, False),
            ("name", "name", str, False, None, True),
            ("origin", "origin", TestScriptOrigin, True, None, False),
            ("profile", "profile", fhirreference.FHIRReference, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("setup", "setup", TestScriptSetup, False, None, False),
            ("status", "status", str, False, None, True),
            ("teardown", "teardown", TestScriptTeardown, False, None, False),
            ("test", "test", TestScriptTest, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("variable", "variable", TestScriptVariable, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class TestScriptDestination(backboneelement.BackboneElement):
    """ 
    A
    n
    a
    b
    s
    t
    r
    a
    c
    t
    s
    e
    r
    v
    e
    r
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
    d
    e
    s
    t
    i
    n
    a
    t
    i
    o
    n
    o
    r
    r
    e
    c
    e
    i
    v
    e
    r
    i
    n
    a
    m
    e
    s
    s
    a
    g
    e
    e
    x
    c
    h
    a
    n
    g
    e
    .
    
    
    A
    n
    a
    b
    s
    t
    r
    a
    c
    t
    s
    e
    r
    v
    e
    r
    u
    s
    e
    d
    i
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
    s
    w
    i
    t
    h
    i
    n
    t
    h
    i
    s
    t
    e
    s
    t
    s
    c
    r
    i
    p
    t
    i
    n
    t
    h
    e
    d
    e
    s
    t
    i
    n
    a
    t
    i
    o
    n
    e
    l
    e
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "TestScriptDestination"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index = None
        """ 
        T
        h
        e
        i
        n
        d
        e
        x
        o
        f
        t
        h
        e
        a
        b
        s
        t
        r
        a
        c
        t
        d
        e
        s
        t
        i
        n
        a
        t
        i
        o
        n
        s
        e
        r
        v
        e
        r
        s
        t
        a
        r
        t
        i
        n
        g
        a
        t
        1
        .
        Type `int`. """
        
        self.profile = None
        """ 
        F
        H
        I
        R
        -
        S
        e
        r
        v
        e
        r
        |
        F
        H
        I
        R
        -
        S
        D
        C
        -
        F
        o
        r
        m
        M
        a
        n
        a
        g
        e
        r
        |
        F
        H
        I
        R
        -
        S
        D
        C
        -
        F
        o
        r
        m
        R
        e
        c
        e
        i
        v
        e
        r
        |
        F
        H
        I
        R
        -
        S
        D
        C
        -
        F
        o
        r
        m
        P
        r
        o
        c
        e
        s
        s
        o
        r
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        super(TestScriptDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptDestination, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js


class TestScriptFixture(backboneelement.BackboneElement):
    """ 
    F
    i
    x
    t
    u
    r
    e
    i
    n
    t
    h
    e
    t
    e
    s
    t
    s
    c
    r
    i
    p
    t
    -
    b
    y
    r
    e
    f
    e
    r
    e
    n
    c
    e
    (
    u
    r
    i
    )
    .
    
    
    F
    i
    x
    t
    u
    r
    e
    i
    n
    t
    h
    e
    t
    e
    s
    t
    s
    c
    r
    i
    p
    t
    -
    b
    y
    r
    e
    f
    e
    r
    e
    n
    c
    e
    (
    u
    r
    i
    )
    .
    A
    l
    l
    f
    i
    x
    t
    u
    r
    e
    s
    a
    r
    e
    r
    e
    q
    u
    i
    r
    e
    d
    f
    o
    r
    t
    h
    e
    t
    e
    s
    t
    s
    c
    r
    i
    p
    t
    t
    o
    e
    x
    e
    c
    u
    t
    e
    .
    
    """
    
    resource_type = "TestScriptFixture"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.autocreate = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        o
        r
        n
        o
        t
        t
        o
        i
        m
        p
        l
        i
        c
        i
        t
        l
        y
        c
        r
        e
        a
        t
        e
        t
        h
        e
        f
        i
        x
        t
        u
        r
        e
        d
        u
        r
        i
        n
        g
        s
        e
        t
        u
        p
        .
        Type `bool`. """
        
        self.autodelete = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        o
        r
        n
        o
        t
        t
        o
        i
        m
        p
        l
        i
        c
        i
        t
        l
        y
        d
        e
        l
        e
        t
        e
        t
        h
        e
        f
        i
        x
        t
        u
        r
        e
        d
        u
        r
        i
        n
        g
        t
        e
        a
        r
        d
        o
        w
        n
        .
        Type `bool`. """
        
        self.resource = None
        """ 
        R
        e
        f
        e
        r
        e
        n
        c
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(TestScriptFixture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptFixture, self).elementProperties()
        js.extend([
            ("autocreate", "autocreate", bool, False, None, True),
            ("autodelete", "autodelete", bool, False, None, True),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class TestScriptMetadata(backboneelement.BackboneElement):
    """ 
    R
    e
    q
    u
    i
    r
    e
    d
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
    t
    h
    a
    t
    i
    s
    a
    s
    s
    u
    m
    e
    d
    t
    o
    f
    u
    n
    c
    t
    i
    o
    n
    c
    o
    r
    r
    e
    c
    t
    l
    y
    o
    n
    t
    h
    e
    F
    H
    I
    R
    s
    e
    r
    v
    e
    r
    b
    e
    i
    n
    g
    t
    e
    s
    t
    e
    d
    .
    
    
    T
    h
    e
    r
    e
    q
    u
    i
    r
    e
    d
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
    m
    u
    s
    t
    e
    x
    i
    s
    t
    a
    n
    d
    a
    r
    e
    a
    s
    s
    u
    m
    e
    d
    t
    o
    f
    u
    n
    c
    t
    i
    o
    n
    c
    o
    r
    r
    e
    c
    t
    l
    y
    o
    n
    t
    h
    e
    F
    H
    I
    R
    s
    e
    r
    v
    e
    r
    b
    e
    i
    n
    g
    t
    e
    s
    t
    e
    d
    .
    
    """
    
    resource_type = "TestScriptMetadata"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capability = None
        """ 
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
        t
        h
        a
        t
        a
        r
        e
        a
        s
        s
        u
        m
        e
        d
        t
        o
        f
        u
        n
        c
        t
        i
        o
        n
        c
        o
        r
        r
        e
        c
        t
        l
        y
        o
        n
        t
        h
        e
        F
        H
        I
        R
        s
        e
        r
        v
        e
        r
        b
        e
        i
        n
        g
        t
        e
        s
        t
        e
        d
        .
        List of `TestScriptMetadataCapability` items (represented as `dict` in JSON). """
        
        self.link = None
        """ 
        L
        i
        n
        k
        s
        t
        o
        t
        h
        e
        F
        H
        I
        R
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
        .
        List of `TestScriptMetadataLink` items (represented as `dict` in JSON). """
        
        super(TestScriptMetadata, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadata, self).elementProperties()
        js.extend([
            ("capability", "capability", TestScriptMetadataCapability, True, None, True),
            ("link", "link", TestScriptMetadataLink, True, None, False),
        ])
        return js


class TestScriptMetadataCapability(backboneelement.BackboneElement):
    """ 
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
    t
    h
    a
    t
    a
    r
    e
    a
    s
    s
    u
    m
    e
    d
    t
    o
    f
    u
    n
    c
    t
    i
    o
    n
    c
    o
    r
    r
    e
    c
    t
    l
    y
    o
    n
    t
    h
    e
    F
    H
    I
    R
    s
    e
    r
    v
    e
    r
    b
    e
    i
    n
    g
    t
    e
    s
    t
    e
    d
    .
    
    
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
    t
    h
    a
    t
    m
    u
    s
    t
    e
    x
    i
    s
    t
    a
    n
    d
    a
    r
    e
    a
    s
    s
    u
    m
    e
    d
    t
    o
    f
    u
    n
    c
    t
    i
    o
    n
    c
    o
    r
    r
    e
    c
    t
    l
    y
    o
    n
    t
    h
    e
    F
    H
    I
    R
    s
    e
    r
    v
    e
    r
    b
    e
    i
    n
    g
    t
    e
    s
    t
    e
    d
    .
    
    """
    
    resource_type = "TestScriptMetadataCapability"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capabilities = None
        """ 
        R
        e
        q
        u
        i
        r
        e
        d
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
        .
        Type `str`. """
        
        self.description = None
        """ 
        T
        h
        e
        e
        x
        p
        e
        c
        t
        e
        d
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
        e
        r
        v
        e
        r
        .
        Type `str`. """
        
        self.destination = None
        """ 
        W
        h
        i
        c
        h
        s
        e
        r
        v
        e
        r
        t
        h
        e
        s
        e
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
        a
        p
        p
        l
        y
        t
        o
        .
        Type `int`. """
        
        self.link = None
        """ 
        L
        i
        n
        k
        s
        t
        o
        t
        h
        e
        F
        H
        I
        R
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
        .
        List of `str` items. """
        
        self.origin = None
        """ 
        W
        h
        i
        c
        h
        o
        r
        i
        g
        i
        n
        s
        e
        r
        v
        e
        r
        t
        h
        e
        s
        e
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
        a
        p
        p
        l
        y
        t
        o
        .
        List of `int` items. """
        
        self.required = None
        """ 
        A
        r
        e
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
        r
        e
        q
        u
        i
        r
        e
        d
        ?
        .
        Type `bool`. """
        
        self.validated = None
        """ 
        A
        r
        e
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
        v
        a
        l
        i
        d
        a
        t
        e
        d
        ?
        .
        Type `bool`. """
        
        super(TestScriptMetadataCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataCapability, self).elementProperties()
        js.extend([
            ("capabilities", "capabilities", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("link", "link", str, True, None, False),
            ("origin", "origin", int, True, None, False),
            ("required", "required", bool, False, None, True),
            ("validated", "validated", bool, False, None, True),
        ])
        return js


class TestScriptMetadataLink(backboneelement.BackboneElement):
    """ 
    L
    i
    n
    k
    s
    t
    o
    t
    h
    e
    F
    H
    I
    R
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
    .
    
    
    A
    l
    i
    n
    k
    t
    o
    t
    h
    e
    F
    H
    I
    R
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
    t
    h
    a
    t
    t
    h
    i
    s
    t
    e
    s
    t
    i
    s
    c
    o
    v
    e
    r
    i
    n
    g
    .
    
    """
    
    resource_type = "TestScriptMetadataLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        S
        h
        o
        r
        t
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
        .
        Type `str`. """
        
        self.url = None
        """ 
        U
        R
        L
        t
        o
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
        .
        Type `str`. """
        
        super(TestScriptMetadataLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptMetadataLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("url", "url", str, False, None, True),
        ])
        return js


class TestScriptOrigin(backboneelement.BackboneElement):
    """ 
    A
    n
    a
    b
    s
    t
    r
    a
    c
    t
    s
    e
    r
    v
    e
    r
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
    c
    l
    i
    e
    n
    t
    o
    r
    s
    e
    n
    d
    e
    r
    i
    n
    a
    m
    e
    s
    s
    a
    g
    e
    e
    x
    c
    h
    a
    n
    g
    e
    .
    
    
    A
    n
    a
    b
    s
    t
    r
    a
    c
    t
    s
    e
    r
    v
    e
    r
    u
    s
    e
    d
    i
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
    s
    w
    i
    t
    h
    i
    n
    t
    h
    i
    s
    t
    e
    s
    t
    s
    c
    r
    i
    p
    t
    i
    n
    t
    h
    e
    o
    r
    i
    g
    i
    n
    e
    l
    e
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "TestScriptOrigin"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.index = None
        """ 
        T
        h
        e
        i
        n
        d
        e
        x
        o
        f
        t
        h
        e
        a
        b
        s
        t
        r
        a
        c
        t
        o
        r
        i
        g
        i
        n
        s
        e
        r
        v
        e
        r
        s
        t
        a
        r
        t
        i
        n
        g
        a
        t
        1
        .
        Type `int`. """
        
        self.profile = None
        """ 
        F
        H
        I
        R
        -
        C
        l
        i
        e
        n
        t
        |
        F
        H
        I
        R
        -
        S
        D
        C
        -
        F
        o
        r
        m
        F
        i
        l
        l
        e
        r
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        super(TestScriptOrigin, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptOrigin, self).elementProperties()
        js.extend([
            ("index", "index", int, False, None, True),
            ("profile", "profile", coding.Coding, False, None, True),
        ])
        return js


class TestScriptSetup(backboneelement.BackboneElement):
    """ 
    A
    s
    e
    r
    i
    e
    s
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
    s
    e
    t
    u
    p
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
    b
    e
    f
    o
    r
    e
    t
    e
    s
    t
    s
    a
    r
    e
    e
    x
    e
    c
    u
    t
    e
    d
    .
    """
    
    resource_type = "TestScriptSetup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        A
        s
        e
        t
        u
        p
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
        s
        s
        e
        r
        t
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        List of `TestScriptSetupAction` items (represented as `dict` in JSON). """
        
        super(TestScriptSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptSetupAction, True, None, True),
        ])
        return js


class TestScriptSetupAction(backboneelement.BackboneElement):
    """ 
    A
    s
    e
    t
    u
    p
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
    s
    s
    e
    r
    t
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    
    A
    c
    t
    i
    o
    n
    w
    o
    u
    l
    d
    c
    o
    n
    t
    a
    i
    n
    e
    i
    t
    h
    e
    r
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
    s
    s
    e
    r
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "TestScriptSetupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ 
        T
        h
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
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation = None
        """ 
        T
        h
        e
        s
        e
        t
        u
        p
        o
        p
        e
        r
        a
        t
        i
        o
        n
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
        ])
        return js


class TestScriptSetupActionAssert(backboneelement.BackboneElement):
    """ 
    T
    h
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
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    
    E
    v
    a
    l
    u
    a
    t
    e
    s
    t
    h
    e
    r
    e
    s
    u
    l
    t
    s
    o
    f
    p
    r
    e
    v
    i
    o
    u
    s
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
    t
    o
    d
    e
    t
    e
    r
    m
    i
    n
    e
    i
    f
    t
    h
    e
    s
    e
    r
    v
    e
    r
    u
    n
    d
    e
    r
    t
    e
    s
    t
    b
    e
    h
    a
    v
    e
    s
    a
    p
    p
    r
    o
    p
    r
    i
    a
    t
    e
    l
    y
    .
    
    """
    
    resource_type = "TestScriptSetupActionAssert"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compareToSourceExpression = None
        """ 
        T
        h
        e
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
        o
        e
        v
        a
        l
        u
        a
        t
        e
        a
        g
        a
        i
        n
        s
        t
        t
        h
        e
        s
        o
        u
        r
        c
        e
        f
        i
        x
        t
        u
        r
        e
        .
        Type `str`. """
        
        self.compareToSourceId = None
        """ 
        I
        d
        o
        f
        t
        h
        e
        s
        o
        u
        r
        c
        e
        f
        i
        x
        t
        u
        r
        e
        t
        o
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
        .
        Type `str`. """
        
        self.compareToSourcePath = None
        """ 
        X
        P
        a
        t
        h
        o
        r
        J
        S
        O
        N
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
        o
        e
        v
        a
        l
        u
        a
        t
        e
        a
        g
        a
        i
        n
        s
        t
        t
        h
        e
        s
        o
        u
        r
        c
        e
        f
        i
        x
        t
        u
        r
        e
        .
        Type `str`. """
        
        self.contentType = None
        """ 
        M
        i
        m
        e
        t
        y
        p
        e
        t
        o
        c
        o
        m
        p
        a
        r
        e
        a
        g
        a
        i
        n
        s
        t
        t
        h
        e
        '
        C
        o
        n
        t
        e
        n
        t
        -
        T
        y
        p
        e
        '
        h
        e
        a
        d
        e
        r
        .
        Type `str`. """
        
        self.description = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        r
        e
        p
        o
        r
        t
        i
        n
        g
        a
        s
        s
        e
        r
        t
        i
        o
        n
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
        .
        Type `str`. """
        
        self.direction = None
        """ 
        r
        e
        s
        p
        o
        n
        s
        e
        |
        r
        e
        q
        u
        e
        s
        t
        .
        Type `str`. """
        
        self.expression = None
        """ 
        T
        h
        e
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
        o
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
        .
        Type `str`. """
        
        self.headerField = None
        """ 
        H
        T
        T
        P
        h
        e
        a
        d
        e
        r
        f
        i
        e
        l
        d
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.label = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        l
        o
        g
        g
        i
        n
        g
        a
        s
        s
        e
        r
        t
        i
        o
        n
        l
        a
        b
        e
        l
        .
        Type `str`. """
        
        self.minimumId = None
        """ 
        F
        i
        x
        t
        u
        r
        e
        I
        d
        o
        f
        m
        i
        n
        i
        m
        u
        m
        c
        o
        n
        t
        e
        n
        t
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
        
        self.navigationLinks = None
        """ 
        P
        e
        r
        f
        o
        r
        m
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        o
        n
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
        l
        i
        n
        k
        s
        ?
        .
        Type `bool`. """
        
        self.operator = None
        """ 
        e
        q
        u
        a
        l
        s
        |
        n
        o
        t
        E
        q
        u
        a
        l
        s
        |
        i
        n
        |
        n
        o
        t
        I
        n
        |
        g
        r
        e
        a
        t
        e
        r
        T
        h
        a
        n
        |
        l
        e
        s
        s
        T
        h
        a
        n
        |
        e
        m
        p
        t
        y
        |
        n
        o
        t
        E
        m
        p
        t
        y
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
        C
        o
        n
        t
        a
        i
        n
        s
        |
        e
        v
        a
        l
        .
        Type `str`. """
        
        self.path = None
        """ 
        X
        P
        a
        t
        h
        o
        r
        J
        S
        O
        N
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
        .
        Type `str`. """
        
        self.requestMethod = None
        """ 
        d
        e
        l
        e
        t
        e
        |
        g
        e
        t
        |
        o
        p
        t
        i
        o
        n
        s
        |
        p
        a
        t
        c
        h
        |
        p
        o
        s
        t
        |
        p
        u
        t
        |
        h
        e
        a
        d
        .
        Type `str`. """
        
        self.requestURL = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        U
        R
        L
        c
        o
        m
        p
        a
        r
        i
        s
        o
        n
        v
        a
        l
        u
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
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.response = None
        """ 
        o
        k
        a
        y
        |
        c
        r
        e
        a
        t
        e
        d
        |
        n
        o
        C
        o
        n
        t
        e
        n
        t
        |
        n
        o
        t
        M
        o
        d
        i
        f
        i
        e
        d
        |
        b
        a
        d
        |
        f
        o
        r
        b
        i
        d
        d
        e
        n
        |
        n
        o
        t
        F
        o
        u
        n
        d
        |
        m
        e
        t
        h
        o
        d
        N
        o
        t
        A
        l
        l
        o
        w
        e
        d
        |
        c
        o
        n
        f
        l
        i
        c
        t
        |
        g
        o
        n
        e
        |
        p
        r
        e
        c
        o
        n
        d
        i
        t
        i
        o
        n
        F
        a
        i
        l
        e
        d
        |
        u
        n
        p
        r
        o
        c
        e
        s
        s
        a
        b
        l
        e
        .
        Type `str`. """
        
        self.responseCode = None
        """ 
        H
        T
        T
        P
        r
        e
        s
        p
        o
        n
        s
        e
        c
        o
        d
        e
        t
        o
        t
        e
        s
        t
        .
        Type `str`. """
        
        self.sourceId = None
        """ 
        F
        i
        x
        t
        u
        r
        e
        I
        d
        o
        f
        s
        o
        u
        r
        c
        e
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
        o
        r
        h
        e
        a
        d
        e
        r
        F
        i
        e
        l
        d
        .
        Type `str`. """
        
        self.validateProfileId = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        I
        d
        o
        f
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        p
        r
        o
        f
        i
        l
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
        .
        Type `str`. """
        
        self.value = None
        """ 
        T
        h
        e
        v
        a
        l
        u
        e
        t
        o
        c
        o
        m
        p
        a
        r
        e
        t
        o
        .
        Type `str`. """
        
        self.warningOnly = None
        """ 
        W
        i
        l
        l
        t
        h
        i
        s
        a
        s
        s
        e
        r
        t
        p
        r
        o
        d
        u
        c
        e
        a
        w
        a
        r
        n
        i
        n
        g
        o
        n
        l
        y
        o
        n
        e
        r
        r
        o
        r
        ?
        .
        Type `bool`. """
        
        super(TestScriptSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionAssert, self).elementProperties()
        js.extend([
            ("compareToSourceExpression", "compareToSourceExpression", str, False, None, False),
            ("compareToSourceId", "compareToSourceId", str, False, None, False),
            ("compareToSourcePath", "compareToSourcePath", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("direction", "direction", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("minimumId", "minimumId", str, False, None, False),
            ("navigationLinks", "navigationLinks", bool, False, None, False),
            ("operator", "operator", str, False, None, False),
            ("path", "path", str, False, None, False),
            ("requestMethod", "requestMethod", str, False, None, False),
            ("requestURL", "requestURL", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("response", "response", str, False, None, False),
            ("responseCode", "responseCode", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("validateProfileId", "validateProfileId", str, False, None, False),
            ("value", "value", str, False, None, False),
            ("warningOnly", "warningOnly", bool, False, None, True),
        ])
        return js


class TestScriptSetupActionOperation(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    s
    e
    t
    u
    p
    o
    p
    e
    r
    a
    t
    i
    o
    n
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    
    T
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
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    """
    
    resource_type = "TestScriptSetupActionOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accept = None
        """ 
        M
        i
        m
        e
        t
        y
        p
        e
        t
        o
        a
        c
        c
        e
        p
        t
        i
        n
        t
        h
        e
        p
        a
        y
        l
        o
        a
        d
        o
        f
        t
        h
        e
        r
        e
        s
        p
        o
        n
        s
        e
        ,
        w
        i
        t
        h
        c
        h
        a
        r
        s
        e
        t
        e
        t
        c
        .
        .
        Type `str`. """
        
        self.contentType = None
        """ 
        M
        i
        m
        e
        t
        y
        p
        e
        o
        f
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        p
        a
        y
        l
        o
        a
        d
        c
        o
        n
        t
        e
        n
        t
        s
        ,
        w
        i
        t
        h
        c
        h
        a
        r
        s
        e
        t
        e
        t
        c
        .
        .
        Type `str`. """
        
        self.description = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        r
        e
        p
        o
        r
        t
        i
        n
        g
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        .
        Type `str`. """
        
        self.destination = None
        """ 
        S
        e
        r
        v
        e
        r
        r
        e
        s
        p
        o
        n
        d
        i
        n
        g
        t
        o
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        .
        Type `int`. """
        
        self.encodeRequestUrl = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        o
        r
        n
        o
        t
        t
        o
        s
        e
        n
        d
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        u
        r
        l
        i
        n
        e
        n
        c
        o
        d
        e
        d
        f
        o
        r
        m
        a
        t
        .
        Type `bool`. """
        
        self.label = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        l
        o
        g
        g
        i
        n
        g
        o
        p
        e
        r
        a
        t
        i
        o
        n
        l
        a
        b
        e
        l
        .
        Type `str`. """
        
        self.method = None
        """ 
        d
        e
        l
        e
        t
        e
        |
        g
        e
        t
        |
        o
        p
        t
        i
        o
        n
        s
        |
        p
        a
        t
        c
        h
        |
        p
        o
        s
        t
        |
        p
        u
        t
        |
        h
        e
        a
        d
        .
        Type `str`. """
        
        self.origin = None
        """ 
        S
        e
        r
        v
        e
        r
        i
        n
        i
        t
        i
        a
        t
        i
        n
        g
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        .
        Type `int`. """
        
        self.params = None
        """ 
        E
        x
        p
        l
        i
        c
        i
        t
        l
        y
        d
        e
        f
        i
        n
        e
        d
        p
        a
        t
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
        .
        Type `str`. """
        
        self.requestHeader = None
        """ 
        E
        a
        c
        h
        o
        p
        e
        r
        a
        t
        i
        o
        n
        c
        a
        n
        h
        a
        v
        e
        o
        n
        e
        o
        r
        m
        o
        r
        e
        h
        e
        a
        d
        e
        r
        e
        l
        e
        m
        e
        n
        t
        s
        .
        List of `TestScriptSetupActionOperationRequestHeader` items (represented as `dict` in JSON). """
        
        self.requestId = None
        """ 
        F
        i
        x
        t
        u
        r
        e
        I
        d
        o
        f
        m
        a
        p
        p
        e
        d
        r
        e
        q
        u
        e
        s
        t
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
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.responseId = None
        """ 
        F
        i
        x
        t
        u
        r
        e
        I
        d
        o
        f
        m
        a
        p
        p
        e
        d
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `str`. """
        
        self.sourceId = None
        """ 
        F
        i
        x
        t
        u
        r
        e
        I
        d
        o
        f
        b
        o
        d
        y
        f
        o
        r
        P
        U
        T
        a
        n
        d
        P
        O
        S
        T
        r
        e
        q
        u
        e
        s
        t
        s
        .
        Type `str`. """
        
        self.targetId = None
        """ 
        I
        d
        o
        f
        f
        i
        x
        t
        u
        r
        e
        u
        s
        e
        d
        f
        o
        r
        e
        x
        t
        r
        a
        c
        t
        i
        n
        g
        t
        h
        e
        [
        i
        d
        ]
        ,
        [
        t
        y
        p
        e
        ]
        ,
        a
        n
        d
        [
        v
        i
        d
        ]
        f
        o
        r
        G
        E
        T
        r
        e
        q
        u
        e
        s
        t
        s
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
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
        c
        o
        d
        e
        t
        y
        p
        e
        t
        h
        a
        t
        w
        i
        l
        l
        b
        e
        e
        x
        e
        c
        u
        t
        e
        d
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.url = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        U
        R
        L
        .
        Type `str`. """
        
        super(TestScriptSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperation, self).elementProperties()
        js.extend([
            ("accept", "accept", str, False, None, False),
            ("contentType", "contentType", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("destination", "destination", int, False, None, False),
            ("encodeRequestUrl", "encodeRequestUrl", bool, False, None, True),
            ("label", "label", str, False, None, False),
            ("method", "method", str, False, None, False),
            ("origin", "origin", int, False, None, False),
            ("params", "params", str, False, None, False),
            ("requestHeader", "requestHeader", TestScriptSetupActionOperationRequestHeader, True, None, False),
            ("requestId", "requestId", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("responseId", "responseId", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
            ("targetId", "targetId", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


class TestScriptSetupActionOperationRequestHeader(backboneelement.BackboneElement):
    """ 
    E
    a
    c
    h
    o
    p
    e
    r
    a
    t
    i
    o
    n
    c
    a
    n
    h
    a
    v
    e
    o
    n
    e
    o
    r
    m
    o
    r
    e
    h
    e
    a
    d
    e
    r
    e
    l
    e
    m
    e
    n
    t
    s
    .
    
    
    H
    e
    a
    d
    e
    r
    e
    l
    e
    m
    e
    n
    t
    s
    w
    o
    u
    l
    d
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
    t
    H
    T
    T
    P
    h
    e
    a
    d
    e
    r
    s
    .
    
    """
    
    resource_type = "TestScriptSetupActionOperationRequestHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.field = None
        """ 
        H
        T
        T
        P
        h
        e
        a
        d
        e
        r
        f
        i
        e
        l
        d
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.value = None
        """ 
        H
        T
        T
        P
        h
        e
        a
        d
        e
        r
        f
        i
        e
        l
        d
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        super(TestScriptSetupActionOperationRequestHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptSetupActionOperationRequestHeader, self).elementProperties()
        js.extend([
            ("field", "field", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class TestScriptTeardown(backboneelement.BackboneElement):
    """ 
    A
    s
    e
    r
    i
    e
    s
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
    c
    l
    e
    a
    n
    u
    p
    s
    t
    e
    p
    s
    .
    
    
    A
    s
    e
    r
    i
    e
    s
    o
    f
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
    r
    e
    q
    u
    i
    r
    e
    d
    t
    o
    c
    l
    e
    a
    n
    u
    p
    a
    f
    t
    e
    r
    a
    l
    l
    t
    h
    e
    t
    e
    s
    t
    s
    a
    r
    e
    e
    x
    e
    c
    u
    t
    e
    d
    (
    s
    u
    c
    c
    e
    s
    s
    f
    u
    l
    l
    y
    o
    r
    o
    t
    h
    e
    r
    w
    i
    s
    e
    )
    .
    
    """
    
    resource_type = "TestScriptTeardown"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        O
        n
        e
        o
        r
        m
        o
        r
        e
        t
        e
        a
        r
        d
        o
        w
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
        s
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        List of `TestScriptTeardownAction` items (represented as `dict` in JSON). """
        
        super(TestScriptTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTeardownAction, True, None, True),
        ])
        return js


class TestScriptTeardownAction(backboneelement.BackboneElement):
    """ 
    O
    n
    e
    o
    r
    m
    o
    r
    e
    t
    e
    a
    r
    d
    o
    w
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
    s
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    
    T
    h
    e
    t
    e
    a
    r
    d
    o
    w
    n
    a
    c
    t
    i
    o
    n
    w
    i
    l
    l
    o
    n
    l
    y
    c
    o
    n
    t
    a
    i
    n
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
    .
    
    """
    
    resource_type = "TestScriptTeardownAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ 
        T
        h
        e
        t
        e
        a
        r
        d
        o
        w
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
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestScriptSetupActionOperation, False, None, True),
        ])
        return js


class TestScriptTest(backboneelement.BackboneElement):
    """ 
    A
    t
    e
    s
    t
    i
    n
    t
    h
    i
    s
    s
    c
    r
    i
    p
    t
    .
    """
    
    resource_type = "TestScriptTest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        A
        t
        e
        s
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
        o
        r
        a
        s
        s
        e
        r
        t
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        List of `TestScriptTestAction` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        r
        e
        p
        o
        r
        t
        i
        n
        g
        s
        h
        o
        r
        t
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
        s
        t
        .
        Type `str`. """
        
        self.name = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        l
        o
        g
        g
        i
        n
        g
        n
        a
        m
        e
        o
        f
        t
        h
        i
        s
        t
        e
        s
        t
        .
        Type `str`. """
        
        super(TestScriptTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTest, self).elementProperties()
        js.extend([
            ("action", "action", TestScriptTestAction, True, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


class TestScriptTestAction(backboneelement.BackboneElement):
    """ 
    A
    t
    e
    s
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
    o
    r
    a
    s
    s
    e
    r
    t
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    
    A
    c
    t
    i
    o
    n
    w
    o
    u
    l
    d
    c
    o
    n
    t
    a
    i
    n
    e
    i
    t
    h
    e
    r
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
    s
    s
    e
    r
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "TestScriptTestAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ 
        T
        h
        e
        s
        e
        t
        u
        p
        a
        s
        s
        e
        r
        t
        i
        o
        n
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        Type `TestScriptSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation = None
        """ 
        T
        h
        e
        s
        e
        t
        u
        p
        o
        p
        e
        r
        a
        t
        i
        o
        n
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        Type `TestScriptSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestScriptTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestScriptSetupActionAssert, False, None, False),
            ("operation", "operation", TestScriptSetupActionOperation, False, None, False),
        ])
        return js


class TestScriptVariable(backboneelement.BackboneElement):
    """ 
    P
    l
    a
    c
    e
    h
    o
    l
    d
    e
    r
    f
    o
    r
    e
    v
    a
    l
    u
    a
    t
    e
    d
    e
    l
    e
    m
    e
    n
    t
    s
    .
    
    
    V
    a
    r
    i
    a
    b
    l
    e
    i
    s
    s
    e
    t
    b
    a
    s
    e
    d
    e
    i
    t
    h
    e
    r
    o
    n
    e
    l
    e
    m
    e
    n
    t
    v
    a
    l
    u
    e
    i
    n
    r
    e
    s
    p
    o
    n
    s
    e
    b
    o
    d
    y
    o
    r
    o
    n
    h
    e
    a
    d
    e
    r
    f
    i
    e
    l
    d
    v
    a
    l
    u
    e
    i
    n
    t
    h
    e
    r
    e
    s
    p
    o
    n
    s
    e
    h
    e
    a
    d
    e
    r
    s
    .
    
    """
    
    resource_type = "TestScriptVariable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.defaultValue = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        ,
        h
        a
        r
        d
        -
        c
        o
        d
        e
        d
        ,
        o
        r
        u
        s
        e
        r
        -
        d
        e
        f
        i
        n
        e
        d
        v
        a
        l
        u
        e
        f
        o
        r
        t
        h
        i
        s
        v
        a
        r
        i
        a
        b
        l
        e
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
        v
        a
        r
        i
        a
        b
        l
        e
        .
        Type `str`. """
        
        self.expression = None
        """ 
        T
        h
        e
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
        a
        g
        a
        i
        n
        s
        t
        t
        h
        e
        f
        i
        x
        t
        u
        r
        e
        b
        o
        d
        y
        .
        Type `str`. """
        
        self.headerField = None
        """ 
        H
        T
        T
        P
        h
        e
        a
        d
        e
        r
        f
        i
        e
        l
        d
        n
        a
        m
        e
        f
        o
        r
        s
        o
        u
        r
        c
        e
        .
        Type `str`. """
        
        self.hint = None
        """ 
        H
        i
        n
        t
        h
        e
        l
        p
        t
        e
        x
        t
        f
        o
        r
        d
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        t
        o
        e
        n
        t
        e
        r
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
        i
        s
        v
        a
        r
        i
        a
        b
        l
        e
        .
        Type `str`. """
        
        self.path = None
        """ 
        X
        P
        a
        t
        h
        o
        r
        J
        S
        O
        N
        P
        a
        t
        h
        a
        g
        a
        i
        n
        s
        t
        t
        h
        e
        f
        i
        x
        t
        u
        r
        e
        b
        o
        d
        y
        .
        Type `str`. """
        
        self.sourceId = None
        """ 
        F
        i
        x
        t
        u
        r
        e
        I
        d
        o
        f
        s
        o
        u
        r
        c
        e
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
        o
        r
        h
        e
        a
        d
        e
        r
        F
        i
        e
        l
        d
        w
        i
        t
        h
        i
        n
        t
        h
        i
        s
        v
        a
        r
        i
        a
        b
        l
        e
        .
        Type `str`. """
        
        super(TestScriptVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestScriptVariable, self).elementProperties()
        js.extend([
            ("defaultValue", "defaultValue", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("headerField", "headerField", str, False, None, False),
            ("hint", "hint", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("path", "path", str, False, None, False),
            ("sourceId", "sourceId", str, False, None, False),
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
