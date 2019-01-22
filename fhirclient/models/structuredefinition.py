#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class StructureDefinition(domainresource.DomainResource):
    """ 
    S
    t
    r
    u
    c
    t
    u
    r
    a
    l
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
    a
    F
    H
    I
    R
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
    d
    e
    s
    c
    r
    i
    b
    e
    t
    h
    e
    u
    n
    d
    e
    r
    l
    y
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
    ,
    d
    a
    t
    a
    t
    y
    p
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
    F
    H
    I
    R
    ,
    a
    n
    d
    a
    l
    s
    o
    f
    o
    r
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
    e
    x
    t
    e
    n
    s
    i
    o
    n
    s
    a
    n
    d
    c
    o
    n
    s
    t
    r
    a
    i
    n
    t
    s
    o
    n
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
    n
    d
    d
    a
    t
    a
    t
    y
    p
    e
    s
    .
    
    """
    
    resource_type = "StructureDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None
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
        t
        r
        u
        c
        t
        u
        r
        e
        i
        s
        a
        b
        s
        t
        r
        a
        c
        t
        .
        Type `bool`. """
        
        self.baseDefinition = None
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
        t
        h
        a
        t
        t
        h
        i
        s
        t
        y
        p
        e
        i
        s
        c
        o
        n
        s
        t
        r
        a
        i
        n
        e
        d
        /
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
        f
        r
        o
        m
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
        
        self.context = None
        """ 
        I
        f
        a
        n
        e
        x
        t
        e
        n
        s
        i
        o
        n
        ,
        w
        h
        e
        r
        e
        i
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
        i
        n
        s
        t
        a
        n
        c
        e
        s
        .
        List of `StructureDefinitionContext` items (represented as `dict` in JSON). """
        
        self.contextInvariant = None
        """ 
        F
        H
        I
        R
        P
        a
        t
        h
        i
        n
        v
        a
        r
        i
        a
        n
        t
        s
        -
        w
        h
        e
        n
        t
        h
        e
        e
        x
        t
        e
        n
        s
        i
        o
        n
        c
        a
        n
        b
        e
        u
        s
        e
        d
        .
        List of `str` items. """
        
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
        
        self.derivation = None
        """ 
        s
        p
        e
        c
        i
        a
        l
        i
        z
        a
        t
        i
        o
        n
        |
        c
        o
        n
        s
        t
        r
        a
        i
        n
        t
        -
        H
        o
        w
        r
        e
        l
        a
        t
        e
        s
        t
        o
        b
        a
        s
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
        .
        Type `str`. """
        
        self.differential = None
        """ 
        D
        i
        f
        f
        e
        r
        e
        n
        t
        i
        a
        l
        v
        i
        e
        w
        o
        f
        t
        h
        e
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
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """
        
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
        i
        s
        S
        t
        r
        u
        c
        t
        u
        r
        e
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
        t
        a
        r
        g
        e
        t
        s
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
        
        self.keyword = None
        """ 
        A
        s
        s
        i
        s
        t
        w
        i
        t
        h
        i
        n
        d
        e
        x
        i
        n
        g
        a
        n
        d
        f
        i
        n
        d
        i
        n
        g
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ 
        p
        r
        i
        m
        i
        t
        i
        v
        e
        -
        t
        y
        p
        e
        |
        c
        o
        m
        p
        l
        e
        x
        -
        t
        y
        p
        e
        |
        r
        e
        s
        o
        u
        r
        c
        e
        |
        l
        o
        g
        i
        c
        a
        l
        .
        Type `str`. """
        
        self.mapping = None
        """ 
        E
        x
        t
        e
        r
        n
        a
        l
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
        m
        a
        p
        p
        e
        d
        t
        o
        .
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """
        
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
        
        self.snapshot = None
        """ 
        S
        n
        a
        p
        s
        h
        o
        t
        v
        i
        e
        w
        o
        f
        t
        h
        e
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
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """
        
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
        
        self.type = None
        """ 
        T
        y
        p
        e
        d
        e
        f
        i
        n
        e
        d
        o
        r
        c
        o
        n
        s
        t
        r
        a
        i
        n
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
        r
        u
        c
        t
        u
        r
        e
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
        .
        Type `str`. """
        
        super(StructureDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, True),
            ("baseDefinition", "baseDefinition", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("context", "context", StructureDefinitionContext, True, None, False),
            ("contextInvariant", "contextInvariant", str, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("derivation", "derivation", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("differential", "differential", StructureDefinitionDifferential, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("keyword", "keyword", coding.Coding, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("mapping", "mapping", StructureDefinitionMapping, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class StructureDefinitionContext(backboneelement.BackboneElement):
    """ 
    I
    f
    a
    n
    e
    x
    t
    e
    n
    s
    i
    o
    n
    ,
    w
    h
    e
    r
    e
    i
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
    i
    n
    s
    t
    a
    n
    c
    e
    s
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
    h
    e
    t
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
    o
    r
    d
    a
    t
    a
    t
    y
    p
    e
    e
    l
    e
    m
    e
    n
    t
    s
    t
    o
    w
    h
    i
    c
    h
    t
    h
    e
    e
    x
    t
    e
    n
    s
    i
    o
    n
    c
    a
    n
    b
    e
    a
    p
    p
    l
    i
    e
    d
    .
    
    """
    
    resource_type = "StructureDefinitionContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        e
        x
        t
        e
        n
        s
        i
        o
        n
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
        i
        n
        s
        t
        a
        n
        c
        e
        s
        .
        Type `str`. """
        
        self.type = None
        """ 
        f
        h
        i
        r
        p
        a
        t
        h
        |
        e
        l
        e
        m
        e
        n
        t
        |
        e
        x
        t
        e
        n
        s
        i
        o
        n
        .
        Type `str`. """
        
        super(StructureDefinitionContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionContext, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ 
    D
    i
    f
    f
    e
    r
    e
    n
    t
    i
    a
    l
    v
    i
    e
    w
    o
    f
    t
    h
    e
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
    
    
    A
    d
    i
    f
    f
    e
    r
    e
    n
    t
    i
    a
    l
    v
    i
    e
    w
    i
    s
    e
    x
    p
    r
    e
    s
    s
    e
    d
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
    t
    h
    e
    b
    a
    s
    e
    S
    t
    r
    u
    c
    t
    u
    r
    e
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
    -
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
    d
    i
    f
    f
    e
    r
    e
    n
    c
    e
    s
    t
    h
    a
    t
    i
    t
    a
    p
    p
    l
    i
    e
    s
    .
    
    """
    
    resource_type = "StructureDefinitionDifferential"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
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
        e
        l
        e
        m
        e
        n
        t
        s
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
        (
        i
        f
        n
        o
        S
        t
        r
        u
        c
        t
        u
        r
        e
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
        )
        .
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionDifferential, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ 
    E
    x
    t
    e
    r
    n
    a
    l
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
    m
    a
    p
    p
    e
    d
    t
    o
    .
    
    
    A
    n
    e
    x
    t
    e
    r
    n
    a
    l
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
    m
    a
    p
    p
    e
    d
    t
    o
    .
    
    """
    
    resource_type = "StructureDefinitionMapping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ 
        V
        e
        r
        s
        i
        o
        n
        s
        ,
        I
        s
        s
        u
        e
        s
        ,
        S
        c
        o
        p
        e
        l
        i
        m
        i
        t
        a
        t
        i
        o
        n
        s
        e
        t
        c
        .
        .
        Type `str`. """
        
        self.identity = None
        """ 
        I
        n
        t
        e
        r
        n
        a
        l
        i
        d
        w
        h
        e
        n
        t
        h
        i
        s
        m
        a
        p
        p
        i
        n
        g
        i
        s
        u
        s
        e
        d
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        s
        w
        h
        a
        t
        t
        h
        i
        s
        m
        a
        p
        p
        i
        n
        g
        r
        e
        f
        e
        r
        s
        t
        o
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
        f
        i
        e
        s
        w
        h
        a
        t
        t
        h
        i
        s
        m
        a
        p
        p
        i
        n
        g
        r
        e
        f
        e
        r
        s
        t
        o
        .
        Type `str`. """
        
        super(StructureDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ 
    S
    n
    a
    p
    s
    h
    o
    t
    v
    i
    e
    w
    o
    f
    t
    h
    e
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
    
    
    A
    s
    n
    a
    p
    s
    h
    o
    t
    v
    i
    e
    w
    i
    s
    e
    x
    p
    r
    e
    s
    s
    e
    d
    i
    n
    a
    s
    t
    a
    n
    d
    a
    l
    o
    n
    e
    f
    o
    r
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
    a
    n
    d
    i
    n
    t
    e
    r
    p
    r
    e
    t
    e
    d
    w
    i
    t
    h
    o
    u
    t
    c
    o
    n
    s
    i
    d
    e
    r
    i
    n
    g
    t
    h
    e
    b
    a
    s
    e
    S
    t
    r
    u
    c
    t
    u
    r
    e
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
    .
    
    """
    
    resource_type = "StructureDefinitionSnapshot"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
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
        e
        l
        e
        m
        e
        n
        t
        s
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
        (
        i
        f
        n
        o
        S
        t
        r
        u
        c
        t
        u
        r
        e
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
        )
        .
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionSnapshot, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
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
    from . import elementdefinition
except ImportError:
    elementdefinition = sys.modules[__package__ + '.elementdefinition']
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
