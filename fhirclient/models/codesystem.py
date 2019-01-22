#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CodeSystem) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CodeSystem(domainresource.DomainResource):
    """ 
    D
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
    e
    x
    i
    s
    t
    e
    n
    c
    e
    o
    f
    a
    n
    d
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
    o
    r
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
    l
    e
    m
    e
    n
    t
    .
    
    
    T
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
    d
    e
    c
    l
    a
    r
    e
    t
    h
    e
    e
    x
    i
    s
    t
    e
    n
    c
    e
    o
    f
    a
    n
    d
    d
    e
    s
    c
    r
    i
    b
    e
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
    o
    r
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
    l
    e
    m
    e
    n
    t
    a
    n
    d
    i
    t
    s
    k
    e
    y
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    ,
    a
    n
    d
    o
    p
    t
    i
    o
    n
    a
    l
    l
    y
    d
    e
    f
    i
    n
    e
    a
    p
    a
    r
    t
    o
    r
    a
    l
    l
    o
    f
    i
    t
    s
    c
    o
    n
    t
    e
    n
    t
    .
    
    """
    
    resource_type = "CodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.caseSensitive = None
        """ 
        I
        f
        c
        o
        d
        e
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
        i
        s
        c
        a
        s
        e
        s
        e
        n
        s
        i
        t
        i
        v
        e
        .
        Type `bool`. """
        
        self.compositional = None
        """ 
        I
        f
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
        d
        e
        f
        i
        n
        e
        s
        a
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
        .
        Type `bool`. """
        
        self.concept = None
        """ 
        C
        o
        n
        c
        e
        p
        t
        s
        i
        n
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
        .
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        
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
        
        self.content = None
        """ 
        n
        o
        t
        -
        p
        r
        e
        s
        e
        n
        t
        |
        e
        x
        a
        m
        p
        l
        e
        |
        f
        r
        a
        g
        m
        e
        n
        t
        |
        c
        o
        m
        p
        l
        e
        t
        e
        |
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
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
        
        self.count = None
        """ 
        T
        o
        t
        a
        l
        c
        o
        n
        c
        e
        p
        t
        s
        i
        n
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
        .
        Type `int`. """
        
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
        d
        e
        s
        y
        s
        t
        e
        m
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
        
        self.filter = None
        """ 
        F
        i
        l
        t
        e
        r
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
        i
        n
        a
        v
        a
        l
        u
        e
        s
        e
        t
        .
        List of `CodeSystemFilter` items (represented as `dict` in JSON). """
        
        self.hierarchyMeaning = None
        """ 
        g
        r
        o
        u
        p
        e
        d
        -
        b
        y
        |
        i
        s
        -
        a
        |
        p
        a
        r
        t
        -
        o
        f
        |
        c
        l
        a
        s
        s
        i
        f
        i
        e
        d
        -
        w
        i
        t
        h
        .
        Type `str`. """
        
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
        (
        b
        u
        s
        i
        n
        e
        s
        s
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
        )
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
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
        o
        d
        e
        s
        y
        s
        t
        e
        m
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
        d
        e
        s
        y
        s
        t
        e
        m
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
        
        self.property = None
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
        s
        u
        p
        p
        l
        i
        e
        d
        a
        b
        o
        u
        t
        e
        a
        c
        h
        c
        o
        n
        c
        e
        p
        t
        .
        List of `CodeSystemProperty` items (represented as `dict` in JSON). """
        
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
        d
        e
        s
        y
        s
        t
        e
        m
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
        
        self.supplements = None
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
        t
        h
        i
        s
        a
        d
        d
        s
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        s
        a
        n
        d
        p
        r
        o
        p
        e
        r
        t
        i
        e
        s
        t
        o
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
        o
        d
        e
        s
        y
        s
        t
        e
        m
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
        (
        C
        o
        d
        i
        n
        g
        .
        s
        y
        s
        t
        e
        m
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
        
        self.valueSet = None
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
        v
        a
        l
        u
        e
        s
        e
        t
        w
        i
        t
        h
        e
        n
        t
        i
        r
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
        .
        Type `str`. """
        
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
        d
        e
        s
        y
        s
        t
        e
        m
        (
        C
        o
        d
        i
        n
        g
        .
        v
        e
        r
        s
        i
        o
        n
        )
        .
        Type `str`. """
        
        self.versionNeeded = None
        """ 
        I
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
        s
        a
        r
        e
        n
        o
        t
        s
        t
        a
        b
        l
        e
        .
        Type `bool`. """
        
        super(CodeSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystem, self).elementProperties()
        js.extend([
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("compositional", "compositional", bool, False, None, False),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("content", "content", str, False, None, True),
            ("copyright", "copyright", str, False, None, False),
            ("count", "count", int, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("filter", "filter", CodeSystemFilter, True, None, False),
            ("hierarchyMeaning", "hierarchyMeaning", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("property", "property", CodeSystemProperty, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("supplements", "supplements", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("version", "version", str, False, None, False),
            ("versionNeeded", "versionNeeded", bool, False, None, False),
        ])
        return js


from . import backboneelement

class CodeSystemConcept(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    c
    e
    p
    t
    s
    i
    n
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
    .
    
    
    C
    o
    n
    c
    e
    p
    t
    s
    t
    h
    a
    t
    a
    r
    e
    i
    n
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
    .
    T
    h
    e
    c
    o
    n
    c
    e
    p
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
    s
    a
    r
    e
    i
    n
    h
    e
    r
    e
    n
    t
    l
    y
    h
    i
    e
    r
    a
    r
    c
    h
    i
    c
    a
    l
    ,
    b
    u
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
    s
    m
    u
    s
    t
    b
    e
    c
    o
    n
    s
    u
    l
    t
    e
    d
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
    w
    h
    a
    t
    t
    h
    e
    m
    e
    a
    n
    i
    n
    g
    s
    o
    f
    t
    h
    e
    h
    i
    e
    r
    a
    r
    c
    h
    i
    c
    a
    l
    r
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    s
    a
    r
    e
    .
    
    """
    
    resource_type = "CodeSystemConcept"
    
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
        t
        h
        a
        t
        i
        d
        e
        n
        t
        i
        f
        i
        e
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `str`. """
        
        self.concept = None
        """ 
        C
        h
        i
        l
        d
        C
        o
        n
        c
        e
        p
        t
        s
        (
        i
        s
        -
        a
        /
        c
        o
        n
        t
        a
        i
        n
        s
        /
        c
        a
        t
        e
        g
        o
        r
        i
        z
        e
        s
        )
        .
        List of `CodeSystemConcept` items (represented as `dict` in JSON). """
        
        self.definition = None
        """ 
        F
        o
        r
        m
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
        .
        Type `str`. """
        
        self.designation = None
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
        r
        e
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        s
        f
        o
        r
        t
        h
        e
        c
        o
        n
        c
        e
        p
        t
        .
        List of `CodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ 
        T
        e
        x
        t
        t
        o
        d
        i
        s
        p
        l
        a
        y
        t
        o
        t
        h
        e
        u
        s
        e
        r
        .
        Type `str`. """
        
        self.property = None
        """ 
        P
        r
        o
        p
        e
        r
        t
        y
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
        e
        c
        o
        n
        c
        e
        p
        t
        .
        List of `CodeSystemConceptProperty` items (represented as `dict` in JSON). """
        
        super(CodeSystemConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("concept", "concept", CodeSystemConcept, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("designation", "designation", CodeSystemConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
            ("property", "property", CodeSystemConceptProperty, True, None, False),
        ])
        return js


class CodeSystemConceptDesignation(backboneelement.BackboneElement):
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
    r
    e
    p
    r
    e
    s
    e
    n
    t
    a
    t
    i
    o
    n
    s
    f
    o
    r
    t
    h
    e
    c
    o
    n
    c
    e
    p
    t
    .
    
    
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
    r
    e
    p
    r
    e
    s
    e
    n
    t
    a
    t
    i
    o
    n
    s
    f
    o
    r
    t
    h
    e
    c
    o
    n
    c
    e
    p
    t
    -
    o
    t
    h
    e
    r
    l
    a
    n
    g
    u
    a
    g
    e
    s
    ,
    a
    l
    i
    a
    s
    e
    s
    ,
    s
    p
    e
    c
    i
    a
    l
    i
    z
    e
    d
    p
    u
    r
    p
    o
    s
    e
    s
    ,
    u
    s
    e
    d
    f
    o
    r
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
    p
    u
    r
    p
    o
    s
    e
    s
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "CodeSystemConceptDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ 
        H
        u
        m
        a
        n
        l
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
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.use = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        h
        o
        w
        t
        h
        i
        s
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
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
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        T
        h
        e
        t
        e
        x
        t
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
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(CodeSystemConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class CodeSystemConceptProperty(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    p
    e
    r
    t
    y
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
    e
    c
    o
    n
    c
    e
    p
    t
    .
    
    
    A
    p
    r
    o
    p
    e
    r
    t
    y
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
    c
    o
    n
    c
    e
    p
    t
    .
    
    """
    
    resource_type = "CodeSystemConceptProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
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
        t
        o
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
        p
        r
        o
        p
        e
        r
        t
        y
        .
        c
        o
        d
        e
        .
        Type `str`. """
        
        self.valueBoolean = None
        """ 
        V
        a
        l
        u
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `bool`. """
        
        self.valueCode = None
        """ 
        V
        a
        l
        u
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `str`. """
        
        self.valueCoding = None
        """ 
        V
        a
        l
        u
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        """ 
        V
        a
        l
        u
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ 
        V
        a
        l
        u
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `float`. """
        
        self.valueInteger = None
        """ 
        V
        a
        l
        u
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `int`. """
        
        self.valueString = None
        """ 
        V
        a
        l
        u
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
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        Type `str`. """
        
        super(CodeSystemConceptProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemConceptProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js


class CodeSystemFilter(backboneelement.BackboneElement):
    """ 
    F
    i
    l
    t
    e
    r
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
    i
    n
    a
    v
    a
    l
    u
    e
    s
    e
    t
    .
    
    
    A
    f
    i
    l
    t
    e
    r
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
    i
    n
    a
    v
    a
    l
    u
    e
    s
    e
    t
    c
    o
    m
    p
    o
    s
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
    w
    h
    e
    n
    s
    e
    l
    e
    c
    t
    i
    n
    g
    c
    o
    n
    c
    e
    p
    t
    s
    u
    s
    i
    n
    g
    a
    f
    i
    l
    t
    e
    r
    .
    
    """
    
    resource_type = "CodeSystemFilter"
    
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
        t
        h
        a
        t
        i
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
        h
        e
        f
        i
        l
        t
        e
        r
        .
        Type `str`. """
        
        self.description = None
        """ 
        H
        o
        w
        o
        r
        w
        h
        y
        t
        h
        e
        f
        i
        l
        t
        e
        r
        i
        s
        u
        s
        e
        d
        .
        Type `str`. """
        
        self.operator = None
        """ 
        O
        p
        e
        r
        a
        t
        o
        r
        s
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
        w
        i
        t
        h
        f
        i
        l
        t
        e
        r
        .
        List of `str` items. """
        
        self.value = None
        """ 
        W
        h
        a
        t
        t
        o
        u
        s
        e
        f
        o
        r
        t
        h
        e
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        super(CodeSystemFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemFilter, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("operator", "operator", str, True, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class CodeSystemProperty(backboneelement.BackboneElement):
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
    s
    u
    p
    p
    l
    i
    e
    d
    a
    b
    o
    u
    t
    e
    a
    c
    h
    c
    o
    n
    c
    e
    p
    t
    .
    
    
    A
    p
    r
    o
    p
    e
    r
    t
    y
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
    d
    d
    i
    t
    i
    o
    n
    a
    l
    s
    l
    o
    t
    t
    h
    r
    o
    u
    g
    h
    w
    h
    i
    c
    h
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
    c
    a
    n
    b
    e
    p
    r
    o
    v
    i
    d
    e
    d
    a
    b
    o
    u
    t
    a
    c
    o
    n
    c
    e
    p
    t
    .
    
    """
    
    resource_type = "CodeSystemProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
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
        o
        n
        t
        h
        e
        c
        o
        n
        c
        e
        p
        t
        s
        ,
        a
        n
        d
        w
        h
        e
        n
        r
        e
        f
        e
        r
        r
        e
        d
        t
        o
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
        .
        Type `str`. """
        
        self.description = None
        """ 
        W
        h
        y
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
        i
        s
        d
        e
        f
        i
        n
        e
        d
        ,
        a
        n
        d
        /
        o
        r
        w
        h
        a
        t
        i
        t
        c
        o
        n
        v
        e
        y
        s
        .
        Type `str`. """
        
        self.type = None
        """ 
        c
        o
        d
        e
        |
        C
        o
        d
        i
        n
        g
        |
        s
        t
        r
        i
        n
        g
        |
        i
        n
        t
        e
        g
        e
        r
        |
        b
        o
        o
        l
        e
        a
        n
        |
        d
        a
        t
        e
        T
        i
        m
        e
        |
        d
        e
        c
        i
        m
        a
        l
        .
        Type `str`. """
        
        self.uri = None
        """ 
        F
        o
        r
        m
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
        p
        r
        o
        p
        e
        r
        t
        y
        .
        Type `str`. """
        
        super(CodeSystemProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeSystemProperty, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, False),
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
