#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class RiskEvidenceSynthesis(domainresource.DomainResource):
    """ 
    A
    q
    u
    a
    n
    t
    i
    f
    i
    e
    d
    e
    s
    t
    i
    m
    a
    t
    e
    o
    f
    r
    i
    s
    k
    b
    a
    s
    e
    d
    o
    n
    a
    b
    o
    d
    y
    o
    f
    e
    v
    i
    d
    e
    n
    c
    e
    .
    
    
    T
    h
    e
    R
    i
    s
    k
    E
    v
    i
    d
    e
    n
    c
    e
    S
    y
    n
    t
    h
    e
    s
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
    l
    i
    k
    e
    l
    i
    h
    o
    o
    d
    o
    f
    a
    n
    o
    u
    t
    c
    o
    m
    e
    i
    n
    a
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
    p
    l
    u
    s
    e
    x
    p
    o
    s
    u
    r
    e
    s
    t
    a
    t
    e
    w
    h
    e
    r
    e
    t
    h
    e
    r
    i
    s
    k
    e
    s
    t
    i
    m
    a
    t
    e
    i
    s
    d
    e
    r
    i
    v
    e
    d
    f
    r
    o
    m
    a
    c
    o
    m
    b
    i
    n
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
    e
    a
    r
    c
    h
    s
    t
    u
    d
    i
    e
    s
    .
    
    """
    
    resource_type = "RiskEvidenceSynthesis"
    
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
        s
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
        
        self.certainty = None
        """ 
        H
        o
        w
        c
        e
        r
        t
        a
        i
        n
        i
        s
        t
        h
        e
        r
        i
        s
        k
        .
        List of `RiskEvidenceSynthesisCertainty` items (represented as `dict` in JSON). """
        
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
        s
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
        s
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
        
        self.exposure = None
        """ 
        W
        h
        a
        t
        e
        x
        p
        o
        s
        u
        r
        e
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
        s
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
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
        
        self.lastReviewDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
        s
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
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
        
        self.outcome = None
        """ 
        W
        h
        a
        t
        o
        u
        t
        c
        o
        m
        e
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.population = None
        """ 
        W
        h
        a
        t
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
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.riskEstimate = None
        """ 
        W
        h
        a
        t
        w
        a
        s
        t
        h
        e
        e
        s
        t
        i
        m
        a
        t
        e
        d
        r
        i
        s
        k
        .
        Type `RiskEvidenceSynthesisRiskEstimate` (represented as `dict` in JSON). """
        
        self.sampleSize = None
        """ 
        W
        h
        a
        t
        s
        a
        m
        p
        l
        e
        s
        i
        z
        e
        w
        a
        s
        i
        n
        v
        o
        l
        v
        e
        d
        ?
        .
        Type `RiskEvidenceSynthesisSampleSize` (represented as `dict` in JSON). """
        
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
        
        self.studyType = None
        """ 
        T
        y
        p
        e
        o
        f
        s
        t
        u
        d
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.synthesisType = None
        """ 
        T
        y
        p
        e
        o
        f
        s
        y
        n
        t
        h
        e
        s
        i
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
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
        f
        f
        e
        c
        t
        E
        v
        i
        d
        e
        n
        c
        e
        S
        y
        n
        t
        h
        e
        s
        i
        s
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
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
        r
        i
        s
        k
        e
        v
        i
        d
        e
        n
        c
        e
        s
        y
        n
        t
        h
        e
        s
        i
        s
        .
        Type `str`. """
        
        super(RiskEvidenceSynthesis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("certainty", "certainty", RiskEvidenceSynthesisCertainty, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, True),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("riskEstimate", "riskEstimate", RiskEvidenceSynthesisRiskEstimate, False, None, False),
            ("sampleSize", "sampleSize", RiskEvidenceSynthesisSampleSize, False, None, False),
            ("status", "status", str, False, None, True),
            ("studyType", "studyType", codeableconcept.CodeableConcept, False, None, False),
            ("synthesisType", "synthesisType", codeableconcept.CodeableConcept, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class RiskEvidenceSynthesisCertainty(backboneelement.BackboneElement):
    """ 
    H
    o
    w
    c
    e
    r
    t
    a
    i
    n
    i
    s
    t
    h
    e
    r
    i
    s
    k
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
    c
    e
    r
    t
    a
    i
    n
    t
    y
    o
    f
    t
    h
    e
    r
    i
    s
    k
    e
    s
    t
    i
    m
    a
    t
    e
    .
    
    """
    
    resource_type = "RiskEvidenceSynthesisCertainty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.certaintySubcomponent = None
        """ 
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
        t
        h
        a
        t
        c
        o
        n
        t
        r
        i
        b
        u
        t
        e
        s
        t
        o
        t
        h
        e
        o
        v
        e
        r
        a
        l
        l
        c
        e
        r
        t
        a
        i
        n
        t
        y
        .
        List of `RiskEvidenceSynthesisCertaintyCertaintySubcomponent` items (represented as `dict` in JSON). """
        
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
        
        self.rating = None
        """ 
        C
        e
        r
        t
        a
        i
        n
        t
        y
        r
        a
        t
        i
        n
        g
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisCertainty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("certaintySubcomponent", "certaintySubcomponent", RiskEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(backboneelement.BackboneElement):
    """ 
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
    t
    h
    a
    t
    c
    o
    n
    t
    r
    i
    b
    u
    t
    e
    s
    t
    o
    t
    h
    e
    o
    v
    e
    r
    a
    l
    l
    c
    e
    r
    t
    a
    i
    n
    t
    y
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
    o
    f
    t
    h
    e
    o
    v
    e
    r
    a
    l
    l
    c
    e
    r
    t
    a
    i
    n
    t
    y
    .
    
    """
    
    resource_type = "RiskEvidenceSynthesisCertaintyCertaintySubcomponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.rating = None
        """ 
        S
        u
        b
        c
        o
        m
        p
        o
        n
        e
        n
        t
        c
        e
        r
        t
        a
        i
        n
        t
        y
        r
        a
        t
        i
        n
        g
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        s
        u
        b
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
        c
        e
        r
        t
        a
        i
        n
        t
        y
        r
        a
        t
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("note", "note", annotation.Annotation, True, None, False),
            ("rating", "rating", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class RiskEvidenceSynthesisRiskEstimate(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    w
    a
    s
    t
    h
    e
    e
    s
    t
    i
    m
    a
    t
    e
    d
    r
    i
    s
    k
    .
    
    
    T
    h
    e
    e
    s
    t
    i
    m
    a
    t
    e
    d
    r
    i
    s
    k
    o
    f
    t
    h
    e
    o
    u
    t
    c
    o
    m
    e
    .
    
    """
    
    resource_type = "RiskEvidenceSynthesisRiskEstimate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.denominatorCount = None
        """ 
        S
        a
        m
        p
        l
        e
        s
        i
        z
        e
        f
        o
        r
        g
        r
        o
        u
        p
        m
        e
        a
        s
        u
        r
        e
        d
        .
        Type `int`. """
        
        self.description = None
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
        r
        i
        s
        k
        e
        s
        t
        i
        m
        a
        t
        e
        .
        Type `str`. """
        
        self.numeratorCount = None
        """ 
        N
        u
        m
        b
        e
        r
        w
        i
        t
        h
        t
        h
        e
        o
        u
        t
        c
        o
        m
        e
        .
        Type `int`. """
        
        self.precisionEstimate = None
        """ 
        H
        o
        w
        p
        r
        e
        c
        i
        s
        e
        t
        h
        e
        e
        s
        t
        i
        m
        a
        t
        e
        i
        s
        .
        List of `RiskEvidenceSynthesisRiskEstimatePrecisionEstimate` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        r
        i
        s
        k
        e
        s
        t
        i
        m
        a
        t
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unitOfMeasure = None
        """ 
        W
        h
        a
        t
        u
        n
        i
        t
        i
        s
        t
        h
        e
        o
        u
        t
        c
        o
        m
        e
        d
        e
        s
        c
        r
        i
        b
        e
        d
        i
        n
        ?
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        P
        o
        i
        n
        t
        e
        s
        t
        i
        m
        a
        t
        e
        .
        Type `float`. """
        
        super(RiskEvidenceSynthesisRiskEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimate, self).elementProperties()
        js.extend([
            ("denominatorCount", "denominatorCount", int, False, None, False),
            ("description", "description", str, False, None, False),
            ("numeratorCount", "numeratorCount", int, False, None, False),
            ("precisionEstimate", "precisionEstimate", RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(backboneelement.BackboneElement):
    """ 
    H
    o
    w
    p
    r
    e
    c
    i
    s
    e
    t
    h
    e
    e
    s
    t
    i
    m
    a
    t
    e
    i
    s
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
    p
    r
    e
    c
    i
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
    s
    t
    i
    m
    a
    t
    e
    f
    o
    r
    t
    h
    e
    e
    f
    f
    e
    c
    t
    .
    
    """
    
    resource_type = "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.from_fhir = None
        """ 
        L
        o
        w
        e
        r
        b
        o
        u
        n
        d
        .
        Type `float`. """
        
        self.level = None
        """ 
        L
        e
        v
        e
        l
        o
        f
        c
        o
        n
        f
        i
        d
        e
        n
        c
        e
        i
        n
        t
        e
        r
        v
        a
        l
        .
        Type `float`. """
        
        self.to = None
        """ 
        U
        p
        p
        e
        r
        b
        o
        u
        n
        d
        .
        Type `float`. """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        p
        r
        e
        c
        i
        s
        i
        o
        n
        e
        s
        t
        i
        m
        a
        t
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("from_fhir", "from", float, False, None, False),
            ("level", "level", float, False, None, False),
            ("to", "to", float, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class RiskEvidenceSynthesisSampleSize(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    s
    a
    m
    p
    l
    e
    s
    i
    z
    e
    w
    a
    s
    i
    n
    v
    o
    l
    v
    e
    d
    ?
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
    s
    i
    z
    e
    o
    f
    t
    h
    e
    s
    a
    m
    p
    l
    e
    i
    n
    v
    o
    l
    v
    e
    d
    i
    n
    t
    h
    e
    s
    y
    n
    t
    h
    e
    s
    i
    s
    .
    
    """
    
    resource_type = "RiskEvidenceSynthesisSampleSize"
    
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
        p
        t
        i
        o
        n
        o
        f
        s
        a
        m
        p
        l
        e
        s
        i
        z
        e
        .
        Type `str`. """
        
        self.numberOfParticipants = None
        """ 
        H
        o
        w
        m
        a
        n
        y
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
        ?
        .
        Type `int`. """
        
        self.numberOfStudies = None
        """ 
        H
        o
        w
        m
        a
        n
        y
        s
        t
        u
        d
        i
        e
        s
        ?
        .
        Type `int`. """
        
        super(RiskEvidenceSynthesisSampleSize, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
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
