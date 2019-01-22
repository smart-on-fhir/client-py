#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EvidenceVariable) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class EvidenceVariable(domainresource.DomainResource):
    """ 
    A
    p
    o
    p
    u
    l
    a
    t
    i
    o
    n
    ,
    i
    n
    t
    e
    r
    v
    e
    n
    t
    i
    o
    n
    ,
    o
    r
    e
    x
    p
    o
    s
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
    
    
    T
    h
    e
    E
    v
    i
    d
    e
    n
    c
    e
    V
    a
    r
    i
    a
    b
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
    "
    P
    I
    C
    O
    "
    e
    l
    e
    m
    e
    n
    t
    t
    h
    a
    t
    k
    n
    o
    w
    l
    e
    d
    g
    e
    (
    e
    v
    i
    d
    e
    n
    c
    e
    ,
    a
    s
    s
    e
    r
    t
    i
    o
    n
    ,
    r
    e
    c
    o
    m
    m
    e
    n
    d
    a
    t
    i
    o
    n
    )
    i
    s
    a
    b
    o
    u
    t
    .
    
    """
    
    resource_type = "EvidenceVariable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        e
        v
        i
        d
        e
        n
        c
        e
        v
        a
        r
        i
        a
        b
        l
        e
        w
        a
        s
        a
        p
        p
        r
        o
        v
        e
        d
        b
        y
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
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        """ 
        W
        h
        o
        a
        u
        t
        h
        o
        r
        e
        d
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
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ 
        W
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
        t
        h
        e
        m
        e
        m
        b
        e
        r
        s
        o
        f
        t
        h
        e
        e
        v
        i
        d
        e
        n
        c
        e
        e
        l
        e
        m
        e
        n
        t
        .
        List of `EvidenceVariableCharacteristic` items (represented as `dict` in JSON). """
        
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
        e
        v
        i
        d
        e
        n
        c
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
        
        self.editor = None
        """ 
        W
        h
        o
        e
        d
        i
        t
        e
        d
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
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        e
        v
        i
        d
        e
        n
        c
        e
        v
        a
        r
        i
        a
        b
        l
        e
        i
        s
        e
        x
        p
        e
        c
        t
        e
        d
        t
        o
        b
        e
        u
        s
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        """ 
        W
        h
        o
        e
        n
        d
        o
        r
        s
        e
        d
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
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
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
        e
        v
        i
        d
        e
        n
        c
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
        e
        v
        i
        d
        e
        n
        c
        e
        v
        a
        r
        i
        a
        b
        l
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
        
        self.lastReviewDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        e
        v
        i
        d
        e
        n
        c
        e
        v
        a
        r
        i
        a
        b
        l
        e
        w
        a
        s
        l
        a
        s
        t
        r
        e
        v
        i
        e
        w
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        e
        v
        i
        d
        e
        n
        c
        e
        v
        a
        r
        i
        a
        b
        l
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
        
        self.note = None
        """ 
        U
        s
        e
        d
        f
        o
        r
        f
        o
        o
        t
        n
        o
        t
        e
        s
        o
        r
        e
        x
        p
        l
        a
        n
        a
        t
        o
        r
        y
        n
        o
        t
        e
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
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
        
        self.relatedArtifact = None
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
        ,
        c
        i
        t
        a
        t
        i
        o
        n
        s
        ,
        e
        t
        c
        .
        .
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        """ 
        W
        h
        o
        r
        e
        v
        i
        e
        w
        e
        d
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
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.shortTitle = None
        """ 
        T
        i
        t
        l
        e
        f
        o
        r
        u
        s
        e
        i
        n
        i
        n
        f
        o
        r
        m
        a
        l
        c
        o
        n
        t
        e
        x
        t
        s
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
        
        self.subtitle = None
        """ 
        S
        u
        b
        o
        r
        d
        i
        n
        a
        t
        e
        t
        i
        t
        l
        e
        o
        f
        t
        h
        e
        E
        v
        i
        d
        e
        n
        c
        e
        V
        a
        r
        i
        a
        b
        l
        e
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
        e
        v
        i
        d
        e
        n
        c
        e
        v
        a
        r
        i
        a
        b
        l
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
        
        self.topic = None
        """ 
        T
        h
        e
        c
        a
        t
        e
        g
        o
        r
        y
        o
        f
        t
        h
        e
        E
        v
        i
        d
        e
        n
        c
        e
        V
        a
        r
        i
        a
        b
        l
        e
        ,
        s
        u
        c
        h
        a
        s
        E
        d
        u
        c
        a
        t
        i
        o
        n
        ,
        T
        r
        e
        a
        t
        m
        e
        n
        t
        ,
        A
        s
        s
        e
        s
        s
        m
        e
        n
        t
        ,
        e
        t
        c
        .
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        d
        i
        c
        h
        o
        t
        o
        m
        o
        u
        s
        |
        c
        o
        n
        t
        i
        n
        u
        o
        u
        s
        |
        d
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
        e
        v
        i
        d
        e
        n
        c
        e
        v
        a
        r
        i
        a
        b
        l
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
        e
        v
        i
        d
        e
        n
        c
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
        
        super(EvidenceVariable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EvidenceVariable, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("characteristic", "characteristic", EvidenceVariableCharacteristic, True, None, True),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class EvidenceVariableCharacteristic(backboneelement.BackboneElement):
    """ 
    W
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
    t
    h
    e
    m
    e
    m
    b
    e
    r
    s
    o
    f
    t
    h
    e
    e
    v
    i
    d
    e
    n
    c
    e
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
    h
    a
    r
    a
    c
    t
    e
    r
    i
    s
    t
    i
    c
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
    t
    h
    e
    m
    e
    m
    b
    e
    r
    s
    o
    f
    t
    h
    e
    e
    v
    i
    d
    e
    n
    c
    e
    e
    l
    e
    m
    e
    n
    t
    .
    M
    u
    l
    t
    i
    p
    l
    e
    c
    h
    a
    r
    a
    c
    t
    e
    r
    i
    s
    t
    i
    c
    s
    a
    r
    e
    a
    p
    p
    l
    i
    e
    d
    w
    i
    t
    h
    "
    a
    n
    d
    "
    s
    e
    m
    a
    n
    t
    i
    c
    s
    .
    
    """
    
    resource_type = "EvidenceVariableCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.definitionCanonical = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        o
        r
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
        d
        e
        f
        i
        n
        e
        s
        m
        e
        m
        b
        e
        r
        s
        ?
        .
        Type `str`. """
        
        self.definitionCodeableConcept = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        o
        r
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
        d
        e
        f
        i
        n
        e
        s
        m
        e
        m
        b
        e
        r
        s
        ?
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.definitionDataRequirement = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        o
        r
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
        d
        e
        f
        i
        n
        e
        s
        m
        e
        m
        b
        e
        r
        s
        ?
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.definitionExpression = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        o
        r
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
        d
        e
        f
        i
        n
        e
        s
        m
        e
        m
        b
        e
        r
        s
        ?
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.definitionReference = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        o
        r
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
        d
        e
        f
        i
        n
        e
        s
        m
        e
        m
        b
        e
        r
        s
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definitionTriggerDefinition = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        o
        r
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
        d
        e
        f
        i
        n
        e
        s
        m
        e
        m
        b
        e
        r
        s
        ?
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
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
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        .
        Type `str`. """
        
        self.exclude = None
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
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        i
        n
        c
        l
        u
        d
        e
        s
        o
        r
        e
        x
        c
        l
        u
        d
        e
        s
        m
        e
        m
        b
        e
        r
        s
        .
        Type `bool`. """
        
        self.groupMeasure = None
        """ 
        m
        e
        a
        n
        |
        m
        e
        d
        i
        a
        n
        |
        m
        e
        a
        n
        -
        o
        f
        -
        m
        e
        a
        n
        |
        m
        e
        a
        n
        -
        o
        f
        -
        m
        e
        d
        i
        a
        n
        |
        m
        e
        d
        i
        a
        n
        -
        o
        f
        -
        m
        e
        a
        n
        |
        m
        e
        d
        i
        a
        n
        -
        o
        f
        -
        m
        e
        d
        i
        a
        n
        .
        Type `str`. """
        
        self.participantEffectiveDateTime = None
        """ 
        W
        h
        a
        t
        t
        i
        m
        e
        p
        e
        r
        i
        o
        d
        d
        o
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        s
        c
        o
        v
        e
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.participantEffectiveDuration = None
        """ 
        W
        h
        a
        t
        t
        i
        m
        e
        p
        e
        r
        i
        o
        d
        d
        o
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        s
        c
        o
        v
        e
        r
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.participantEffectivePeriod = None
        """ 
        W
        h
        a
        t
        t
        i
        m
        e
        p
        e
        r
        i
        o
        d
        d
        o
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        s
        c
        o
        v
        e
        r
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.participantEffectiveTiming = None
        """ 
        W
        h
        a
        t
        t
        i
        m
        e
        p
        e
        r
        i
        o
        d
        d
        o
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        s
        c
        o
        v
        e
        r
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.timeFromStart = None
        """ 
        O
        b
        s
        e
        r
        v
        a
        t
        i
        o
        n
        t
        i
        m
        e
        f
        r
        o
        m
        s
        t
        u
        d
        y
        s
        t
        a
        r
        t
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.usageContext = None
        """ 
        W
        h
        a
        t
        c
        o
        d
        e
        /
        v
        a
        l
        u
        e
        p
        a
        i
        r
        s
        d
        e
        f
        i
        n
        e
        m
        e
        m
        b
        e
        r
        s
        ?
        .
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        super(EvidenceVariableCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EvidenceVariableCharacteristic, self).elementProperties()
        js.extend([
            ("definitionCanonical", "definitionCanonical", str, False, "definition", True),
            ("definitionCodeableConcept", "definitionCodeableConcept", codeableconcept.CodeableConcept, False, "definition", True),
            ("definitionDataRequirement", "definitionDataRequirement", datarequirement.DataRequirement, False, "definition", True),
            ("definitionExpression", "definitionExpression", expression.Expression, False, "definition", True),
            ("definitionReference", "definitionReference", fhirreference.FHIRReference, False, "definition", True),
            ("definitionTriggerDefinition", "definitionTriggerDefinition", triggerdefinition.TriggerDefinition, False, "definition", True),
            ("description", "description", str, False, None, False),
            ("exclude", "exclude", bool, False, None, False),
            ("groupMeasure", "groupMeasure", str, False, None, False),
            ("participantEffectiveDateTime", "participantEffectiveDateTime", fhirdate.FHIRDate, False, "participantEffective", False),
            ("participantEffectiveDuration", "participantEffectiveDuration", duration.Duration, False, "participantEffective", False),
            ("participantEffectivePeriod", "participantEffectivePeriod", period.Period, False, "participantEffective", False),
            ("participantEffectiveTiming", "participantEffectiveTiming", timing.Timing, False, "participantEffective", False),
            ("timeFromStart", "timeFromStart", duration.Duration, False, None, False),
            ("usageContext", "usageContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
