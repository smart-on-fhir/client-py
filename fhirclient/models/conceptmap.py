#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ConceptMap) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ConceptMap(domainresource.DomainResource):
    """ 
    A
    m
    a
    p
    f
    r
    o
    m
    o
    n
    e
    s
    e
    t
    o
    f
    c
    o
    n
    c
    e
    p
    t
    s
    t
    o
    o
    n
    e
    o
    r
    m
    o
    r
    e
    o
    t
    h
    e
    r
    c
    o
    n
    c
    e
    p
    t
    s
    .
    
    
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
    f
    r
    o
    m
    o
    n
    e
    s
    e
    t
    o
    f
    c
    o
    n
    c
    e
    p
    t
    s
    t
    o
    o
    n
    e
    o
    r
    m
    o
    r
    e
    o
    t
    h
    e
    r
    c
    o
    n
    c
    e
    p
    t
    s
    -
    e
    i
    t
    h
    e
    r
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
    ,
    o
    r
    d
    a
    t
    a
    e
    l
    e
    m
    e
    n
    t
    /
    d
    a
    t
    a
    e
    l
    e
    m
    e
    n
    t
    c
    o
    n
    c
    e
    p
    t
    s
    ,
    o
    r
    c
    l
    a
    s
    s
    e
    s
    i
    n
    c
    l
    a
    s
    s
    m
    o
    d
    e
    l
    s
    .
    
    """
    
    resource_type = "ConceptMap"
    
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
        o
        n
        c
        e
        p
        t
        m
        a
        p
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
        
        self.group = None
        """ 
        S
        a
        m
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
        t
        a
        r
        g
        e
        t
        s
        y
        s
        t
        e
        m
        s
        .
        List of `ConceptMapGroup` items (represented as `dict` in JSON). """
        
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
        n
        c
        e
        p
        t
        m
        a
        p
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
        n
        c
        e
        p
        t
        m
        a
        p
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
        n
        c
        e
        p
        t
        m
        a
        p
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
        
        self.sourceCanonical = None
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
        v
        a
        l
        u
        e
        s
        e
        t
        t
        h
        a
        t
        c
        o
        n
        t
        a
        i
        n
        s
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
        t
        h
        a
        t
        a
        r
        e
        b
        e
        i
        n
        g
        m
        a
        p
        p
        e
        d
        .
        Type `str`. """
        
        self.sourceUri = None
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
        v
        a
        l
        u
        e
        s
        e
        t
        t
        h
        a
        t
        c
        o
        n
        t
        a
        i
        n
        s
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
        t
        h
        a
        t
        a
        r
        e
        b
        e
        i
        n
        g
        m
        a
        p
        p
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
        
        self.targetCanonical = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        s
        e
        t
        w
        h
        i
        c
        h
        p
        r
        o
        v
        i
        d
        e
        s
        c
        o
        n
        t
        e
        x
        t
        f
        o
        r
        t
        h
        e
        m
        a
        p
        p
        i
        n
        g
        s
        .
        Type `str`. """
        
        self.targetUri = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        s
        e
        t
        w
        h
        i
        c
        h
        p
        r
        o
        v
        i
        d
        e
        s
        c
        o
        n
        t
        e
        x
        t
        f
        o
        r
        t
        h
        e
        m
        a
        p
        p
        i
        n
        g
        s
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
        n
        c
        e
        p
        t
        m
        a
        p
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
        n
        c
        e
        p
        t
        m
        a
        p
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
        n
        c
        e
        p
        t
        m
        a
        p
        .
        Type `str`. """
        
        super(ConceptMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", ConceptMapGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("sourceCanonical", "sourceCanonical", str, False, "source", False),
            ("sourceUri", "sourceUri", str, False, "source", False),
            ("status", "status", str, False, None, True),
            ("targetCanonical", "targetCanonical", str, False, "target", False),
            ("targetUri", "targetUri", str, False, "target", False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ConceptMapGroup(backboneelement.BackboneElement):
    """ 
    S
    a
    m
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
    t
    a
    r
    g
    e
    t
    s
    y
    s
    t
    e
    m
    s
    .
    
    
    A
    g
    r
    o
    u
    p
    o
    f
    m
    a
    p
    p
    i
    n
    g
    s
    t
    h
    a
    t
    a
    l
    l
    h
    a
    v
    e
    t
    h
    e
    s
    a
    m
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
    t
    a
    r
    g
    e
    t
    s
    y
    s
    t
    e
    m
    .
    
    """
    
    resource_type = "ConceptMapGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ 
        M
        a
        p
        p
        i
        n
        g
        s
        f
        o
        r
        a
        c
        o
        n
        c
        e
        p
        t
        f
        r
        o
        m
        t
        h
        e
        s
        o
        u
        r
        c
        e
        s
        e
        t
        .
        List of `ConceptMapGroupElement` items (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        S
        o
        u
        r
        c
        e
        s
        y
        s
        t
        e
        m
        w
        h
        e
        r
        e
        c
        o
        n
        c
        e
        p
        t
        s
        t
        o
        b
        e
        m
        a
        p
        p
        e
        d
        a
        r
        e
        d
        e
        f
        i
        n
        e
        d
        .
        Type `str`. """
        
        self.sourceVersion = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
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
        .
        Type `str`. """
        
        self.target = None
        """ 
        T
        a
        r
        g
        e
        t
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
        a
        r
        e
        t
        o
        b
        e
        m
        a
        p
        p
        e
        d
        t
        o
        .
        Type `str`. """
        
        self.targetVersion = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
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
        .
        Type `str`. """
        
        self.unmapped = None
        """ 
        W
        h
        a
        t
        t
        o
        d
        o
        w
        h
        e
        n
        t
        h
        e
        r
        e
        i
        s
        n
        o
        m
        a
        p
        p
        i
        n
        g
        f
        o
        r
        t
        h
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
        c
        e
        p
        t
        .
        Type `ConceptMapGroupUnmapped` (represented as `dict` in JSON). """
        
        super(ConceptMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroup, self).elementProperties()
        js.extend([
            ("element", "element", ConceptMapGroupElement, True, None, True),
            ("source", "source", str, False, None, False),
            ("sourceVersion", "sourceVersion", str, False, None, False),
            ("target", "target", str, False, None, False),
            ("targetVersion", "targetVersion", str, False, None, False),
            ("unmapped", "unmapped", ConceptMapGroupUnmapped, False, None, False),
        ])
        return js


class ConceptMapGroupElement(backboneelement.BackboneElement):
    """ 
    M
    a
    p
    p
    i
    n
    g
    s
    f
    o
    r
    a
    c
    o
    n
    c
    e
    p
    t
    f
    r
    o
    m
    t
    h
    e
    s
    o
    u
    r
    c
    e
    s
    e
    t
    .
    
    
    M
    a
    p
    p
    i
    n
    g
    s
    f
    o
    r
    a
    n
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
    c
    o
    n
    c
    e
    p
    t
    i
    n
    t
    h
    e
    s
    o
    u
    r
    c
    e
    t
    o
    o
    n
    e
    o
    r
    m
    o
    r
    e
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
    t
    a
    r
    g
    e
    t
    .
    
    """
    
    resource_type = "ConceptMapGroupElement"
    
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
        e
        l
        e
        m
        e
        n
        t
        b
        e
        i
        n
        g
        m
        a
        p
        p
        e
        d
        .
        Type `str`. """
        
        self.display = None
        """ 
        D
        i
        s
        p
        l
        a
        y
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
        .
        Type `str`. """
        
        self.target = None
        """ 
        C
        o
        n
        c
        e
        p
        t
        i
        n
        t
        a
        r
        g
        e
        t
        s
        y
        s
        t
        e
        m
        f
        o
        r
        e
        l
        e
        m
        e
        n
        t
        .
        List of `ConceptMapGroupElementTarget` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElement, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("target", "target", ConceptMapGroupElementTarget, True, None, False),
        ])
        return js


class ConceptMapGroupElementTarget(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    c
    e
    p
    t
    i
    n
    t
    a
    r
    g
    e
    t
    s
    y
    s
    t
    e
    m
    f
    o
    r
    e
    l
    e
    m
    e
    n
    t
    .
    
    
    A
    c
    o
    n
    c
    e
    p
    t
    f
    r
    o
    m
    t
    h
    e
    t
    a
    r
    g
    e
    t
    v
    a
    l
    u
    e
    s
    e
    t
    t
    h
    a
    t
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
    m
    a
    p
    s
    t
    o
    .
    
    """
    
    resource_type = "ConceptMapGroupElementTarget"
    
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
        t
        a
        r
        g
        e
        t
        e
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.comment = None
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
        t
        a
        t
        u
        s
        /
        i
        s
        s
        u
        e
        s
        i
        n
        m
        a
        p
        p
        i
        n
        g
        .
        Type `str`. """
        
        self.dependsOn = None
        """ 
        O
        t
        h
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
        i
        s
        m
        a
        p
        p
        i
        n
        g
        (
        f
        r
        o
        m
        c
        o
        n
        t
        e
        x
        t
        )
        .
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        self.display = None
        """ 
        D
        i
        s
        p
        l
        a
        y
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
        .
        Type `str`. """
        
        self.equivalence = None
        """ 
        r
        e
        l
        a
        t
        e
        d
        t
        o
        |
        e
        q
        u
        i
        v
        a
        l
        e
        n
        t
        |
        e
        q
        u
        a
        l
        |
        w
        i
        d
        e
        r
        |
        s
        u
        b
        s
        u
        m
        e
        s
        |
        n
        a
        r
        r
        o
        w
        e
        r
        |
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
        s
        |
        i
        n
        e
        x
        a
        c
        t
        |
        u
        n
        m
        a
        t
        c
        h
        e
        d
        |
        d
        i
        s
        j
        o
        i
        n
        t
        .
        Type `str`. """
        
        self.product = None
        """ 
        O
        t
        h
        e
        r
        c
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
        a
        l
        s
        o
        p
        r
        o
        d
        u
        c
        e
        s
        .
        List of `ConceptMapGroupElementTargetDependsOn` items (represented as `dict` in JSON). """
        
        super(ConceptMapGroupElementTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTarget, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("dependsOn", "dependsOn", ConceptMapGroupElementTargetDependsOn, True, None, False),
            ("display", "display", str, False, None, False),
            ("equivalence", "equivalence", str, False, None, True),
            ("product", "product", ConceptMapGroupElementTargetDependsOn, True, None, False),
        ])
        return js


class ConceptMapGroupElementTargetDependsOn(backboneelement.BackboneElement):
    """ 
    O
    t
    h
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
    i
    s
    m
    a
    p
    p
    i
    n
    g
    (
    f
    r
    o
    m
    c
    o
    n
    t
    e
    x
    t
    )
    .
    
    
    A
    s
    e
    t
    o
    f
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
    d
    e
    p
    e
    n
    d
    e
    n
    c
    i
    e
    s
    f
    o
    r
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
    t
    o
    h
    o
    l
    d
    .
    T
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
    o
    n
    l
    y
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
    i
    f
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
    e
    d
    e
    l
    e
    m
    e
    n
    t
    c
    a
    n
    b
    e
    r
    e
    s
    o
    l
    v
    e
    d
    ,
    a
    n
    d
    i
    t
    h
    a
    s
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
    e
    d
    v
    a
    l
    u
    e
    .
    
    """
    
    resource_type = "ConceptMapGroupElementTargetDependsOn"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.display = None
        """ 
        D
        i
        s
        p
        l
        a
        y
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
        (
        i
        f
        v
        a
        l
        u
        e
        i
        s
        a
        c
        o
        d
        e
        )
        .
        Type `str`. """
        
        self.property = None
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
        p
        r
        o
        p
        e
        r
        t
        y
        m
        a
        p
        p
        i
        n
        g
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
        
        self.system = None
        """ 
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
        (
        i
        f
        n
        e
        c
        e
        s
        s
        a
        r
        y
        )
        .
        Type `str`. """
        
        self.value = None
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
        r
        e
        f
        e
        r
        e
        n
        c
        e
        d
        e
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        super(ConceptMapGroupElementTargetDependsOn, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupElementTargetDependsOn, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("property", "property", str, False, None, True),
            ("system", "system", str, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class ConceptMapGroupUnmapped(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    t
    o
    d
    o
    w
    h
    e
    n
    t
    h
    e
    r
    e
    i
    s
    n
    o
    m
    a
    p
    p
    i
    n
    g
    f
    o
    r
    t
    h
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
    c
    e
    p
    t
    .
    
    
    W
    h
    a
    t
    t
    o
    d
    o
    w
    h
    e
    n
    t
    h
    e
    r
    e
    i
    s
    n
    o
    m
    a
    p
    p
    i
    n
    g
    f
    o
    r
    t
    h
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
    c
    e
    p
    t
    .
    "
    U
    n
    m
    a
    p
    p
    e
    d
    "
    d
    o
    e
    s
    n
    o
    t
    i
    n
    c
    l
    u
    d
    e
    c
    o
    d
    e
    s
    t
    h
    a
    t
    a
    r
    e
    u
    n
    m
    a
    t
    c
    h
    e
    d
    ,
    a
    n
    d
    t
    h
    e
    u
    n
    m
    a
    p
    p
    e
    d
    e
    l
    e
    m
    e
    n
    t
    i
    s
    i
    g
    n
    o
    r
    e
    d
    i
    n
    a
    c
    o
    d
    e
    i
    s
    s
    p
    e
    c
    i
    f
    i
    e
    d
    t
    o
    h
    a
    v
    e
    e
    q
    u
    i
    v
    a
    l
    e
    n
    c
    e
    =
    u
    n
    m
    a
    t
    c
    h
    e
    d
    .
    
    """
    
    resource_type = "ConceptMapGroupUnmapped"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        F
        i
        x
        e
        d
        c
        o
        d
        e
        w
        h
        e
        n
        m
        o
        d
        e
        =
        f
        i
        x
        e
        d
        .
        Type `str`. """
        
        self.display = None
        """ 
        D
        i
        s
        p
        l
        a
        y
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
        .
        Type `str`. """
        
        self.mode = None
        """ 
        p
        r
        o
        v
        i
        d
        e
        d
        |
        f
        i
        x
        e
        d
        |
        o
        t
        h
        e
        r
        -
        m
        a
        p
        .
        Type `str`. """
        
        self.url = None
        """ 
        c
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
        t
        o
        u
        s
        e
        f
        o
        r
        m
        a
        p
        p
        i
        n
        g
        i
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
        c
        o
        n
        c
        e
        p
        t
        i
        s
        u
        n
        m
        a
        p
        p
        e
        d
        .
        Type `str`. """
        
        super(ConceptMapGroupUnmapped, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConceptMapGroupUnmapped, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, False),
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
