#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PlanDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class PlanDefinition(domainresource.DomainResource):
    """ 
    T
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
    a
    p
    l
    a
    n
    f
    o
    r
    a
    s
    e
    r
    i
    e
    s
    o
    f
    a
    c
    t
    i
    o
    n
    s
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
    y
    s
    p
    e
    c
    i
    f
    i
    c
    p
    a
    t
    i
    e
    n
    t
    o
    r
    c
    o
    n
    t
    e
    x
    t
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
    a
    l
    l
    o
    w
    s
    f
    o
    r
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
    v
    a
    r
    i
    o
    u
    s
    t
    y
    p
    e
    s
    o
    f
    p
    l
    a
    n
    s
    a
    s
    a
    s
    h
    a
    r
    a
    b
    l
    e
    ,
    c
    o
    n
    s
    u
    m
    a
    b
    l
    e
    ,
    a
    n
    d
    e
    x
    e
    c
    u
    t
    a
    b
    l
    e
    a
    r
    t
    i
    f
    a
    c
    t
    .
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
    i
    s
    g
    e
    n
    e
    r
    a
    l
    e
    n
    o
    u
    g
    h
    t
    o
    s
    u
    p
    p
    o
    r
    t
    t
    h
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
    a
    b
    r
    o
    a
    d
    r
    a
    n
    g
    e
    o
    f
    c
    l
    i
    n
    i
    c
    a
    l
    a
    r
    t
    i
    f
    a
    c
    t
    s
    s
    u
    c
    h
    a
    s
    c
    l
    i
    n
    i
    c
    a
    l
    d
    e
    c
    i
    s
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
    r
    u
    l
    e
    s
    ,
    o
    r
    d
    e
    r
    s
    e
    t
    s
    a
    n
    d
    p
    r
    o
    t
    o
    c
    o
    l
    s
    .
    
    """
    
    resource_type = "PlanDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        A
        c
        t
        i
        o
        n
        d
        e
        f
        i
        n
        e
        d
        b
        y
        t
        h
        e
        p
        l
        a
        n
        .
        List of `PlanDefinitionAction` items (represented as `dict` in JSON). """
        
        self.approvalDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        l
        a
        n
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
        p
        l
        a
        n
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
        p
        l
        a
        n
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
        
        self.goal = None
        """ 
        W
        h
        a
        t
        t
        h
        e
        p
        l
        a
        n
        i
        s
        t
        r
        y
        i
        n
        g
        t
        o
        a
        c
        c
        o
        m
        p
        l
        i
        s
        h
        .
        List of `PlanDefinitionGoal` items (represented as `dict` in JSON). """
        
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
        p
        l
        a
        n
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
        p
        l
        a
        n
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
        
        self.lastReviewDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        l
        a
        n
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
        
        self.library = None
        """ 
        L
        o
        g
        i
        c
        u
        s
        e
        d
        b
        y
        t
        h
        e
        p
        l
        a
        n
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
        List of `str` items. """
        
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
        p
        l
        a
        n
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
        p
        l
        a
        n
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
        
        self.subjectCodeableConcept = None
        """ 
        T
        y
        p
        e
        o
        f
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
        t
        h
        e
        p
        l
        a
        n
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
        f
        o
        c
        u
        s
        e
        d
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ 
        T
        y
        p
        e
        o
        f
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
        t
        h
        e
        p
        l
        a
        n
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
        f
        o
        c
        u
        s
        e
        d
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        p
        l
        a
        n
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
        p
        l
        a
        n
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
        
        self.topic = None
        """ 
        E
        .
        g
        .
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        o
        r
        d
        e
        r
        -
        s
        e
        t
        |
        c
        l
        i
        n
        i
        c
        a
        l
        -
        p
        r
        o
        t
        o
        c
        o
        l
        |
        e
        c
        a
        -
        r
        u
        l
        e
        |
        w
        o
        r
        k
        f
        l
        o
        w
        -
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        p
        l
        a
        n
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
        
        self.usage = None
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
        e
        c
        l
        i
        n
        i
        c
        a
        l
        u
        s
        a
        g
        e
        o
        f
        t
        h
        e
        p
        l
        a
        n
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
        p
        l
        a
        n
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
        
        super(PlanDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("goal", "goal", PlanDefinitionGoal, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class PlanDefinitionAction(backboneelement.BackboneElement):
    """ 
    A
    c
    t
    i
    o
    n
    d
    e
    f
    i
    n
    e
    d
    b
    y
    t
    h
    e
    p
    l
    a
    n
    .
    
    
    A
    n
    a
    c
    t
    i
    o
    n
    o
    r
    g
    r
    o
    u
    p
    o
    f
    a
    c
    t
    i
    o
    n
    s
    t
    o
    b
    e
    t
    a
    k
    e
    n
    a
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
    p
    l
    a
    n
    .
    
    """
    
    resource_type = "PlanDefinitionAction"
    
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
        u
        b
        -
        a
        c
        t
        i
        o
        n
        .
        List of `PlanDefinitionAction` items (represented as `dict` in JSON). """
        
        self.cardinalityBehavior = None
        """ 
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
        .
        Type `str`. """
        
        self.code = None
        """ 
        C
        o
        d
        e
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
        o
        f
        t
        h
        e
        a
        c
        t
        i
        o
        n
        o
        r
        s
        u
        b
        -
        a
        c
        t
        i
        o
        n
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.condition = None
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
        h
        e
        a
        c
        t
        i
        o
        n
        i
        s
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
        .
        List of `PlanDefinitionActionCondition` items (represented as `dict` in JSON). """
        
        self.definitionCanonical = None
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
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        t
        o
        b
        e
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        Type `str`. """
        
        self.definitionUri = None
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
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        t
        o
        b
        e
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        Type `str`. """
        
        self.description = None
        """ 
        B
        r
        i
        e
        f
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
        a
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.documentation = None
        """ 
        S
        u
        p
        p
        o
        r
        t
        i
        n
        g
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
        f
        o
        r
        t
        h
        e
        i
        n
        t
        e
        n
        d
        e
        d
        p
        e
        r
        f
        o
        r
        m
        e
        r
        o
        f
        t
        h
        e
        a
        c
        t
        i
        o
        n
        .
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.dynamicValue = None
        """ 
        D
        y
        n
        a
        m
        i
        c
        a
        s
        p
        e
        c
        t
        s
        o
        f
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
        .
        List of `PlanDefinitionActionDynamicValue` items (represented as `dict` in JSON). """
        
        self.goalId = None
        """ 
        W
        h
        a
        t
        g
        o
        a
        l
        s
        t
        h
        i
        s
        a
        c
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
        s
        .
        List of `str` items. """
        
        self.groupingBehavior = None
        """ 
        v
        i
        s
        u
        a
        l
        -
        g
        r
        o
        u
        p
        |
        l
        o
        g
        i
        c
        a
        l
        -
        g
        r
        o
        u
        p
        |
        s
        e
        n
        t
        e
        n
        c
        e
        -
        g
        r
        o
        u
        p
        .
        Type `str`. """
        
        self.input = None
        """ 
        I
        n
        p
        u
        t
        d
        a
        t
        a
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
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.output = None
        """ 
        O
        u
        t
        p
        u
        t
        d
        a
        t
        a
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
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ 
        W
        h
        o
        s
        h
        o
        u
        l
        d
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        e
        i
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        .
        List of `PlanDefinitionActionParticipant` items (represented as `dict` in JSON). """
        
        self.precheckBehavior = None
        """ 
        y
        e
        s
        |
        n
        o
        .
        Type `str`. """
        
        self.prefix = None
        """ 
        U
        s
        e
        r
        -
        v
        i
        s
        i
        b
        l
        e
        p
        r
        e
        f
        i
        x
        f
        o
        r
        t
        h
        e
        a
        c
        t
        i
        o
        n
        (
        e
        .
        g
        .
        1
        .
        o
        r
        A
        .
        )
        .
        Type `str`. """
        
        self.priority = None
        """ 
        r
        o
        u
        t
        i
        n
        e
        |
        u
        r
        g
        e
        n
        t
        |
        a
        s
        a
        p
        |
        s
        t
        a
        t
        .
        Type `str`. """
        
        self.reason = None
        """ 
        W
        h
        y
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        b
        e
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.relatedAction = None
        """ 
        R
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
        t
        o
        a
        n
        o
        t
        h
        e
        r
        a
        c
        t
        i
        o
        n
        .
        List of `PlanDefinitionActionRelatedAction` items (represented as `dict` in JSON). """
        
        self.requiredBehavior = None
        """ 
        m
        u
        s
        t
        |
        c
        o
        u
        l
        d
        |
        m
        u
        s
        t
        -
        u
        n
        l
        e
        s
        s
        -
        d
        o
        c
        u
        m
        e
        n
        t
        e
        d
        .
        Type `str`. """
        
        self.selectionBehavior = None
        """ 
        a
        n
        y
        |
        a
        l
        l
        |
        a
        l
        l
        -
        o
        r
        -
        n
        o
        n
        e
        |
        e
        x
        a
        c
        t
        l
        y
        -
        o
        n
        e
        |
        a
        t
        -
        m
        o
        s
        t
        -
        o
        n
        e
        |
        o
        n
        e
        -
        o
        r
        -
        m
        o
        r
        e
        .
        Type `str`. """
        
        self.subjectCodeableConcept = None
        """ 
        T
        y
        p
        e
        o
        f
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
        t
        h
        e
        a
        c
        t
        i
        o
        n
        i
        s
        f
        o
        c
        u
        s
        e
        d
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ 
        T
        y
        p
        e
        o
        f
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
        t
        h
        e
        a
        c
        t
        i
        o
        n
        i
        s
        f
        o
        c
        u
        s
        e
        d
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.textEquivalent = None
        """ 
        S
        t
        a
        t
        i
        c
        t
        e
        x
        t
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
        o
        f
        t
        h
        e
        a
        c
        t
        i
        o
        n
        ,
        u
        s
        e
        d
        i
        f
        t
        h
        e
        d
        y
        n
        a
        m
        i
        c
        a
        s
        p
        e
        c
        t
        s
        c
        a
        n
        n
        o
        t
        b
        e
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
        b
        y
        t
        h
        e
        r
        e
        c
        e
        i
        v
        i
        n
        g
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.timingAge = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDuration = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingRange = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        U
        s
        e
        r
        -
        v
        i
        s
        i
        b
        l
        e
        t
        i
        t
        l
        e
        .
        Type `str`. """
        
        self.transform = None
        """ 
        T
        r
        a
        n
        s
        f
        o
        r
        m
        t
        o
        a
        p
        p
        l
        y
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
        
        self.trigger = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        b
        e
        t
        r
        i
        g
        g
        e
        r
        e
        d
        .
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        c
        r
        e
        a
        t
        e
        |
        u
        p
        d
        a
        t
        e
        |
        r
        e
        m
        o
        v
        e
        |
        f
        i
        r
        e
        -
        e
        v
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PlanDefinitionAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionAction, self).elementProperties()
        js.extend([
            ("action", "action", PlanDefinitionAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", PlanDefinitionActionCondition, True, None, False),
            ("definitionCanonical", "definitionCanonical", str, False, "definition", False),
            ("definitionUri", "definitionUri", str, False, "definition", False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("dynamicValue", "dynamicValue", PlanDefinitionActionDynamicValue, True, None, False),
            ("goalId", "goalId", str, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("input", "input", datarequirement.DataRequirement, True, None, False),
            ("output", "output", datarequirement.DataRequirement, True, None, False),
            ("participant", "participant", PlanDefinitionActionParticipant, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("relatedAction", "relatedAction", PlanDefinitionActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("transform", "transform", str, False, None, False),
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class PlanDefinitionActionCondition(backboneelement.BackboneElement):
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
    h
    e
    a
    c
    t
    i
    o
    n
    i
    s
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
    .
    
    
    A
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
    t
    h
    a
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
    a
    p
    p
    l
    i
    c
    a
    b
    i
    l
    i
    t
    y
    c
    r
    i
    t
    e
    r
    i
    a
    o
    r
    s
    t
    a
    r
    t
    /
    s
    t
    o
    p
    c
    o
    n
    d
    i
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
    a
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "PlanDefinitionActionCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ 
        B
        o
        o
        l
        e
        a
        n
        -
        v
        a
        l
        u
        e
        d
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
        Type `Expression` (represented as `dict` in JSON). """
        
        self.kind = None
        """ 
        a
        p
        p
        l
        i
        c
        a
        b
        i
        l
        i
        t
        y
        |
        s
        t
        a
        r
        t
        |
        s
        t
        o
        p
        .
        Type `str`. """
        
        super(PlanDefinitionActionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("kind", "kind", str, False, None, True),
        ])
        return js


class PlanDefinitionActionDynamicValue(backboneelement.BackboneElement):
    """ 
    D
    y
    n
    a
    m
    i
    c
    a
    s
    p
    e
    c
    t
    s
    o
    f
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
    .
    
    
    C
    u
    s
    t
    o
    m
    i
    z
    a
    t
    i
    o
    n
    s
    t
    h
    a
    t
    s
    h
    o
    u
    l
    d
    b
    e
    a
    p
    p
    l
    i
    e
    d
    t
    o
    t
    h
    e
    s
    t
    a
    t
    i
    c
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
    d
    r
    e
    s
    o
    u
    r
    c
    e
    .
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    ,
    i
    f
    t
    h
    e
    d
    o
    s
    a
    g
    e
    o
    f
    a
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    m
    u
    s
    t
    b
    e
    c
    o
    m
    p
    u
    t
    e
    d
    b
    a
    s
    e
    d
    o
    n
    t
    h
    e
    p
    a
    t
    i
    e
    n
    t
    '
    s
    w
    e
    i
    g
    h
    t
    ,
    a
    c
    u
    s
    t
    o
    m
    i
    z
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
    t
    o
    s
    p
    e
    c
    i
    f
    y
    a
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
    t
    h
    a
    t
    c
    a
    l
    c
    u
    l
    a
    t
    e
    d
    t
    h
    e
    w
    e
    i
    g
    h
    t
    ,
    a
    n
    d
    t
    h
    e
    p
    a
    t
    h
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
    t
    h
    a
    t
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
    t
    h
    e
    r
    e
    s
    u
    l
    t
    .
    
    """
    
    resource_type = "PlanDefinitionActionDynamicValue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ 
        A
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
        t
        h
        a
        t
        p
        r
        o
        v
        i
        d
        e
        s
        t
        h
        e
        d
        y
        n
        a
        m
        i
        c
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
        u
        s
        t
        o
        m
        i
        z
        a
        t
        i
        o
        n
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.path = None
        """ 
        T
        h
        e
        p
        a
        t
        h
        t
        o
        t
        h
        e
        e
        l
        e
        m
        e
        n
        t
        t
        o
        b
        e
        s
        e
        t
        d
        y
        n
        a
        m
        i
        c
        a
        l
        l
        y
        .
        Type `str`. """
        
        super(PlanDefinitionActionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("path", "path", str, False, None, False),
        ])
        return js


class PlanDefinitionActionParticipant(backboneelement.BackboneElement):
    """ 
    W
    h
    o
    s
    h
    o
    u
    l
    d
    p
    a
    r
    t
    i
    c
    i
    p
    a
    t
    e
    i
    n
    t
    h
    e
    a
    c
    t
    i
    o
    n
    .
    
    
    I
    n
    d
    i
    c
    a
    t
    e
    s
    w
    h
    o
    s
    h
    o
    u
    l
    d
    p
    a
    r
    t
    i
    c
    i
    p
    a
    t
    e
    i
    n
    p
    e
    r
    f
    o
    r
    m
    i
    n
    g
    t
    h
    e
    a
    c
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
    b
    e
    d
    .
    
    """
    
    resource_type = "PlanDefinitionActionParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ 
        E
        .
        g
        .
        N
        u
        r
        s
        e
        ,
        S
        u
        r
        g
        e
        o
        n
        ,
        P
        a
        r
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        p
        a
        t
        i
        e
        n
        t
        |
        p
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
        r
        e
        l
        a
        t
        e
        d
        -
        p
        e
        r
        s
        o
        n
        |
        d
        e
        v
        i
        c
        e
        .
        Type `str`. """
        
        super(PlanDefinitionActionParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class PlanDefinitionActionRelatedAction(backboneelement.BackboneElement):
    """ 
    R
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
    t
    o
    a
    n
    o
    t
    h
    e
    r
    a
    c
    t
    i
    o
    n
    .
    
    
    A
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
    t
    o
    a
    n
    o
    t
    h
    e
    r
    a
    c
    t
    i
    o
    n
    s
    u
    c
    h
    a
    s
    "
    b
    e
    f
    o
    r
    e
    "
    o
    r
    "
    3
    0
    -
    6
    0
    m
    i
    n
    u
    t
    e
    s
    a
    f
    t
    e
    r
    s
    t
    a
    r
    t
    o
    f
    "
    .
    
    """
    
    resource_type = "PlanDefinitionActionRelatedAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionId = None
        """ 
        W
        h
        a
        t
        a
        c
        t
        i
        o
        n
        i
        s
        t
        h
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
        .
        Type `str`. """
        
        self.offsetDuration = None
        """ 
        T
        i
        m
        e
        o
        f
        f
        s
        e
        t
        f
        o
        r
        t
        h
        e
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
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.offsetRange = None
        """ 
        T
        i
        m
        e
        o
        f
        f
        s
        e
        t
        f
        o
        r
        t
        h
        e
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
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        b
        e
        f
        o
        r
        e
        -
        s
        t
        a
        r
        t
        |
        b
        e
        f
        o
        r
        e
        |
        b
        e
        f
        o
        r
        e
        -
        e
        n
        d
        |
        c
        o
        n
        c
        u
        r
        r
        e
        n
        t
        -
        w
        i
        t
        h
        -
        s
        t
        a
        r
        t
        |
        c
        o
        n
        c
        u
        r
        r
        e
        n
        t
        |
        c
        o
        n
        c
        u
        r
        r
        e
        n
        t
        -
        w
        i
        t
        h
        -
        e
        n
        d
        |
        a
        f
        t
        e
        r
        -
        s
        t
        a
        r
        t
        |
        a
        f
        t
        e
        r
        |
        a
        f
        t
        e
        r
        -
        e
        n
        d
        .
        Type `str`. """
        
        super(PlanDefinitionActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


class PlanDefinitionGoal(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    t
    h
    e
    p
    l
    a
    n
    i
    s
    t
    r
    y
    i
    n
    g
    t
    o
    a
    c
    c
    o
    m
    p
    l
    i
    s
    h
    .
    
    
    G
    o
    a
    l
    s
    t
    h
    a
    t
    d
    e
    s
    c
    r
    i
    b
    e
    w
    h
    a
    t
    t
    h
    e
    a
    c
    t
    i
    v
    i
    t
    i
    e
    s
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
    l
    a
    n
    a
    r
    e
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
    a
    c
    h
    i
    e
    v
    e
    .
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    ,
    w
    e
    i
    g
    h
    t
    l
    o
    s
    s
    ,
    r
    e
    s
    t
    o
    r
    i
    n
    g
    a
    n
    a
    c
    t
    i
    v
    i
    t
    y
    o
    f
    d
    a
    i
    l
    y
    l
    i
    v
    i
    n
    g
    ,
    o
    b
    t
    a
    i
    n
    i
    n
    g
    h
    e
    r
    d
    i
    m
    m
    u
    n
    i
    t
    y
    v
    i
    a
    i
    m
    m
    u
    n
    i
    z
    a
    t
    i
    o
    n
    ,
    m
    e
    e
    t
    i
    n
    g
    a
    p
    r
    o
    c
    e
    s
    s
    i
    m
    p
    r
    o
    v
    e
    m
    e
    n
    t
    o
    b
    j
    e
    c
    t
    i
    v
    e
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "PlanDefinitionGoal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addresses = None
        """ 
        W
        h
        a
        t
        d
        o
        e
        s
        t
        h
        e
        g
        o
        a
        l
        a
        d
        d
        r
        e
        s
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        E
        .
        g
        .
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
        d
        i
        e
        t
        a
        r
        y
        ,
        b
        e
        h
        a
        v
        i
        o
        r
        a
        l
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        C
        o
        d
        e
        o
        r
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
        g
        o
        a
        l
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.documentation = None
        """ 
        S
        u
        p
        p
        o
        r
        t
        i
        n
        g
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
        f
        o
        r
        t
        h
        e
        g
        o
        a
        l
        .
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ 
        h
        i
        g
        h
        -
        p
        r
        i
        o
        r
        i
        t
        y
        |
        m
        e
        d
        i
        u
        m
        -
        p
        r
        i
        o
        r
        i
        t
        y
        |
        l
        o
        w
        -
        p
        r
        i
        o
        r
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.start = None
        """ 
        W
        h
        e
        n
        g
        o
        a
        l
        p
        u
        r
        s
        u
        i
        t
        b
        e
        g
        i
        n
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ 
        T
        a
        r
        g
        e
        t
        o
        u
        t
        c
        o
        m
        e
        f
        o
        r
        t
        h
        e
        g
        o
        a
        l
        .
        List of `PlanDefinitionGoalTarget` items (represented as `dict` in JSON). """
        
        super(PlanDefinitionGoal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionGoal, self).elementProperties()
        js.extend([
            ("addresses", "addresses", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", codeableconcept.CodeableConcept, False, None, True),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("start", "start", codeableconcept.CodeableConcept, False, None, False),
            ("target", "target", PlanDefinitionGoalTarget, True, None, False),
        ])
        return js


class PlanDefinitionGoalTarget(backboneelement.BackboneElement):
    """ 
    T
    a
    r
    g
    e
    t
    o
    u
    t
    c
    o
    m
    e
    f
    o
    r
    t
    h
    e
    g
    o
    a
    l
    .
    
    
    I
    n
    d
    i
    c
    a
    t
    e
    s
    w
    h
    a
    t
    s
    h
    o
    u
    l
    d
    b
    e
    d
    o
    n
    e
    a
    n
    d
    w
    i
    t
    h
    i
    n
    w
    h
    a
    t
    t
    i
    m
    e
    f
    r
    a
    m
    e
    .
    
    """
    
    resource_type = "PlanDefinitionGoalTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detailCodeableConcept = None
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
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailQuantity = None
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
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.detailRange = None
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
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.due = None
        """ 
        R
        e
        a
        c
        h
        g
        o
        a
        l
        w
        i
        t
        h
        i
        n
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.measure = None
        """ 
        T
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
        w
        h
        o
        s
        e
        v
        a
        l
        u
        e
        i
        s
        t
        o
        b
        e
        t
        r
        a
        c
        k
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PlanDefinitionGoalTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionGoalTarget, self).elementProperties()
        js.extend([
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False),
            ("detailRange", "detailRange", range.Range, False, "detail", False),
            ("due", "due", duration.Duration, False, None, False),
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
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
