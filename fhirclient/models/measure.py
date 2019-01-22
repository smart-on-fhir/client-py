#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Measure) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Measure(domainresource.DomainResource):
    """ 
    A
    q
    u
    a
    l
    i
    t
    y
    m
    e
    a
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
    M
    e
    a
    s
    u
    r
    e
    r
    e
    s
    o
    u
    r
    c
    e
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
    q
    u
    a
    l
    i
    t
    y
    m
    e
    a
    s
    u
    r
    e
    .
    
    """
    
    resource_type = "Measure"
    
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
        m
        e
        a
        s
        u
        r
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
        
        self.clinicalRecommendationStatement = None
        """ 
        S
        u
        m
        m
        a
        r
        y
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
        g
        u
        i
        d
        e
        l
        i
        n
        e
        s
        .
        Type `str`. """
        
        self.compositeScoring = None
        """ 
        o
        p
        p
        o
        r
        t
        u
        n
        i
        t
        y
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
        t
        h
        i
        n
        g
        |
        l
        i
        n
        e
        a
        r
        |
        w
        e
        i
        g
        h
        t
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        D
        e
        f
        i
        n
        e
        d
        t
        e
        r
        m
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
        m
        e
        a
        s
        u
        r
        e
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
        .
        List of `str` items. """
        
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
        m
        e
        a
        s
        u
        r
        e
        .
        Type `str`. """
        
        self.disclaimer = None
        """ 
        D
        i
        s
        c
        l
        a
        i
        m
        e
        r
        f
        o
        r
        u
        s
        e
        o
        f
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        o
        r
        i
        t
        s
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
        c
        o
        n
        t
        e
        n
        t
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
        m
        e
        a
        s
        u
        r
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
        P
        o
        p
        u
        l
        a
        t
        i
        o
        n
        c
        r
        i
        t
        e
        r
        i
        a
        g
        r
        o
        u
        p
        .
        List of `MeasureGroup` items (represented as `dict` in JSON). """
        
        self.guidance = None
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
        g
        u
        i
        d
        a
        n
        c
        e
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
        e
        r
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
        m
        e
        a
        s
        u
        r
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.improvementNotation = None
        """ 
        i
        n
        c
        r
        e
        a
        s
        e
        |
        d
        e
        c
        r
        e
        a
        s
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        m
        e
        a
        s
        u
        r
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
        m
        e
        a
        s
        u
        r
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
        m
        e
        a
        s
        u
        r
        e
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
        m
        e
        a
        s
        u
        r
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
        m
        e
        a
        s
        u
        r
        e
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
        
        self.rateAggregation = None
        """ 
        H
        o
        w
        i
        s
        r
        a
        t
        e
        a
        g
        g
        r
        e
        g
        a
        t
        i
        o
        n
        p
        e
        r
        f
        o
        r
        m
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
        e
        a
        s
        u
        r
        e
        .
        Type `str`. """
        
        self.rationale = None
        """ 
        D
        e
        t
        a
        i
        l
        e
        d
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
        w
        h
        y
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        e
        x
        i
        s
        t
        s
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
        
        self.riskAdjustment = None
        """ 
        H
        o
        w
        r
        i
        s
        k
        a
        d
        j
        u
        s
        t
        m
        e
        n
        t
        i
        s
        a
        p
        p
        l
        i
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
        e
        a
        s
        u
        r
        e
        .
        Type `str`. """
        
        self.scoring = None
        """ 
        p
        r
        o
        p
        o
        r
        t
        i
        o
        n
        |
        r
        a
        t
        i
        o
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
        -
        v
        a
        r
        i
        a
        b
        l
        e
        |
        c
        o
        h
        o
        r
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        E
        .
        g
        .
        P
        a
        t
        i
        e
        n
        t
        ,
        P
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
        ,
        R
        e
        l
        a
        t
        e
        d
        P
        e
        r
        s
        o
        n
        ,
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
        ,
        L
        o
        c
        a
        t
        i
        o
        n
        ,
        D
        e
        v
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ 
        E
        .
        g
        .
        P
        a
        t
        i
        e
        n
        t
        ,
        P
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
        ,
        R
        e
        l
        a
        t
        e
        d
        P
        e
        r
        s
        o
        n
        ,
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
        ,
        L
        o
        c
        a
        t
        i
        o
        n
        ,
        D
        e
        v
        i
        c
        e
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
        m
        e
        a
        s
        u
        r
        e
        .
        Type `str`. """
        
        self.supplementalData = None
        """ 
        W
        h
        a
        t
        o
        t
        h
        e
        r
        d
        a
        t
        a
        s
        h
        o
        u
        l
        d
        b
        e
        r
        e
        p
        o
        r
        t
        e
        d
        w
        i
        t
        h
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        .
        List of `MeasureSupplementalData` items (represented as `dict` in JSON). """
        
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
        m
        e
        a
        s
        u
        r
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
        m
        e
        a
        s
        u
        r
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
        p
        r
        o
        c
        e
        s
        s
        |
        o
        u
        t
        c
        o
        m
        e
        |
        s
        t
        r
        u
        c
        t
        u
        r
        e
        |
        p
        a
        t
        i
        e
        n
        t
        -
        r
        e
        p
        o
        r
        t
        e
        d
        -
        o
        u
        t
        c
        o
        m
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        m
        e
        a
        s
        u
        r
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
        m
        e
        a
        s
        u
        r
        e
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
        m
        e
        a
        s
        u
        r
        e
        .
        Type `str`. """
        
        super(Measure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Measure, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("clinicalRecommendationStatement", "clinicalRecommendationStatement", str, False, None, False),
            ("compositeScoring", "compositeScoring", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("disclaimer", "disclaimer", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", MeasureGroup, True, None, False),
            ("guidance", "guidance", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("rateAggregation", "rateAggregation", str, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("riskAdjustment", "riskAdjustment", str, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supplementalData", "supplementalData", MeasureSupplementalData, True, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class MeasureGroup(backboneelement.BackboneElement):
    """ 
    P
    o
    p
    u
    l
    a
    t
    i
    o
    n
    c
    r
    i
    t
    e
    r
    i
    a
    g
    r
    o
    u
    p
    .
    
    
    A
    g
    r
    o
    u
    p
    o
    f
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
    c
    r
    i
    t
    e
    r
    i
    a
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    """
    
    resource_type = "MeasureGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        M
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
        g
        r
        o
        u
        p
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        S
        u
        m
        m
        a
        r
        y
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
        
        self.population = None
        """ 
        P
        o
        p
        u
        l
        a
        t
        i
        o
        n
        c
        r
        i
        t
        e
        r
        i
        a
        .
        List of `MeasureGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ 
        S
        t
        r
        a
        t
        i
        f
        i
        e
        r
        c
        r
        i
        t
        e
        r
        i
        a
        f
        o
        r
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        .
        List of `MeasureGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("population", "population", MeasureGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureGroupStratifier, True, None, False),
        ])
        return js


class MeasureGroupPopulation(backboneelement.BackboneElement):
    """ 
    P
    o
    p
    u
    l
    a
    t
    i
    o
    n
    c
    r
    i
    t
    e
    r
    i
    a
    .
    
    
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
    c
    r
    i
    t
    e
    r
    i
    a
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    """
    
    resource_type = "MeasureGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        i
        n
        i
        t
        i
        a
        l
        -
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
        |
        n
        u
        m
        e
        r
        a
        t
        o
        r
        |
        n
        u
        m
        e
        r
        a
        t
        o
        r
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        -
        e
        x
        c
        e
        p
        t
        i
        o
        n
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        m
        e
        a
        s
        u
        r
        e
        -
        o
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criteria = None
        """ 
        T
        h
        e
        c
        r
        i
        t
        e
        r
        i
        a
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
        i
        s
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
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        h
        e
        h
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
        i
        s
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
        c
        r
        i
        t
        e
        r
        i
        a
        .
        Type `str`. """
        
        super(MeasureGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", expression.Expression, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js


class MeasureGroupStratifier(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    a
    t
    i
    f
    i
    e
    r
    c
    r
    i
    t
    e
    r
    i
    a
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    
    T
    h
    e
    s
    t
    r
    a
    t
    i
    f
    i
    e
    r
    c
    r
    i
    t
    e
    r
    i
    a
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    r
    e
    p
    o
    r
    t
    ,
    s
    p
    e
    c
    i
    f
    i
    e
    d
    a
    s
    e
    i
    t
    h
    e
    r
    t
    h
    e
    n
    a
    m
    e
    o
    f
    a
    v
    a
    l
    i
    d
    C
    Q
    L
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
    d
    w
    i
    t
    h
    i
    n
    a
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
    l
    i
    b
    r
    a
    r
    y
    o
    r
    a
    v
    a
    l
    i
    d
    F
    H
    I
    R
    R
    e
    s
    o
    u
    r
    c
    e
    P
    a
    t
    h
    .
    
    """
    
    resource_type = "MeasureGroupStratifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        M
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
        s
        t
        r
        a
        t
        i
        f
        i
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.component = None
        """ 
        S
        t
        r
        a
        t
        i
        f
        i
        e
        r
        c
        r
        i
        t
        e
        r
        i
        a
        c
        o
        m
        p
        o
        n
        e
        n
        t
        f
        o
        r
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        .
        List of `MeasureGroupStratifierComponent` items (represented as `dict` in JSON). """
        
        self.criteria = None
        """ 
        H
        o
        w
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        s
        h
        o
        u
        l
        d
        b
        e
        s
        t
        r
        a
        t
        i
        f
        i
        e
        d
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        h
        e
        h
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
        i
        s
        s
        t
        r
        a
        t
        i
        f
        i
        e
        r
        .
        Type `str`. """
        
        super(MeasureGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("component", "component", MeasureGroupStratifierComponent, True, None, False),
            ("criteria", "criteria", expression.Expression, False, None, False),
            ("description", "description", str, False, None, False),
        ])
        return js


class MeasureGroupStratifierComponent(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    a
    t
    i
    f
    i
    e
    r
    c
    r
    i
    t
    e
    r
    i
    a
    c
    o
    m
    p
    o
    n
    e
    n
    t
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    
    A
    c
    o
    m
    p
    o
    n
    e
    n
    t
    o
    f
    t
    h
    e
    s
    t
    r
    a
    t
    i
    f
    i
    e
    r
    c
    r
    i
    t
    e
    r
    i
    a
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    r
    e
    p
    o
    r
    t
    ,
    s
    p
    e
    c
    i
    f
    i
    e
    d
    a
    s
    e
    i
    t
    h
    e
    r
    t
    h
    e
    n
    a
    m
    e
    o
    f
    a
    v
    a
    l
    i
    d
    C
    Q
    L
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
    d
    w
    i
    t
    h
    i
    n
    a
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
    l
    i
    b
    r
    a
    r
    y
    o
    r
    a
    v
    a
    l
    i
    d
    F
    H
    I
    R
    R
    e
    s
    o
    u
    r
    c
    e
    P
    a
    t
    h
    .
    
    """
    
    resource_type = "MeasureGroupStratifierComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        M
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
        s
        t
        r
        a
        t
        i
        f
        i
        e
        r
        c
        o
        m
        p
        o
        n
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criteria = None
        """ 
        C
        o
        m
        p
        o
        n
        e
        n
        t
        o
        f
        h
        o
        w
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        s
        h
        o
        u
        l
        d
        b
        e
        s
        t
        r
        a
        t
        i
        f
        i
        e
        d
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        h
        e
        h
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
        i
        s
        s
        t
        r
        a
        t
        i
        f
        i
        e
        r
        c
        o
        m
        p
        o
        n
        e
        n
        t
        .
        Type `str`. """
        
        super(MeasureGroupStratifierComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureGroupStratifierComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", expression.Expression, False, None, True),
            ("description", "description", str, False, None, False),
        ])
        return js


class MeasureSupplementalData(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    o
    t
    h
    e
    r
    d
    a
    t
    a
    s
    h
    o
    u
    l
    d
    b
    e
    r
    e
    p
    o
    r
    t
    e
    d
    w
    i
    t
    h
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    
    T
    h
    e
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
    l
    d
    a
    t
    a
    c
    r
    i
    t
    e
    r
    i
    a
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    r
    e
    p
    o
    r
    t
    ,
    s
    p
    e
    c
    i
    f
    i
    e
    d
    a
    s
    e
    i
    t
    h
    e
    r
    t
    h
    e
    n
    a
    m
    e
    o
    f
    a
    v
    a
    l
    i
    d
    C
    Q
    L
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
    w
    i
    t
    h
    i
    n
    a
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
    l
    i
    b
    r
    a
    r
    y
    ,
    o
    r
    a
    v
    a
    l
    i
    d
    F
    H
    I
    R
    R
    e
    s
    o
    u
    r
    c
    e
    P
    a
    t
    h
    .
    
    """
    
    resource_type = "MeasureSupplementalData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        M
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
        l
        d
        a
        t
        a
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criteria = None
        """ 
        E
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
        s
        c
        r
        i
        b
        i
        n
        g
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
        a
        t
        a
        t
        o
        b
        e
        r
        e
        p
        o
        r
        t
        e
        d
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        h
        e
        h
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
        i
        s
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
        l
        d
        a
        t
        a
        .
        Type `str`. """
        
        self.usage = None
        """ 
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
        l
        -
        d
        a
        t
        a
        |
        r
        i
        s
        k
        -
        a
        d
        j
        u
        s
        t
        m
        e
        n
        t
        -
        f
        a
        c
        t
        o
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(MeasureSupplementalData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureSupplementalData, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criteria", "criteria", expression.Expression, False, None, True),
            ("description", "description", str, False, None, False),
            ("usage", "usage", codeableconcept.CodeableConcept, True, None, False),
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
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
