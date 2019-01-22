#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RiskAssessment) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class RiskAssessment(domainresource.DomainResource):
    """ 
    P
    o
    t
    e
    n
    t
    i
    a
    l
    o
    u
    t
    c
    o
    m
    e
    s
    f
    o
    r
    a
    s
    u
    b
    j
    e
    c
    t
    w
    i
    t
    h
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
    .
    
    
    A
    n
    a
    s
    s
    e
    s
    s
    m
    e
    n
    t
    o
    f
    t
    h
    e
    l
    i
    k
    e
    l
    y
    o
    u
    t
    c
    o
    m
    e
    (
    s
    )
    f
    o
    r
    a
    p
    a
    t
    i
    e
    n
    t
    o
    r
    o
    t
    h
    e
    r
    s
    u
    b
    j
    e
    c
    t
    a
    s
    w
    e
    l
    l
    a
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
    e
    a
    c
    h
    o
    u
    t
    c
    o
    m
    e
    .
    
    """
    
    resource_type = "RiskAssessment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        f
        u
        l
        f
        i
        l
        l
        e
        d
        b
        y
        t
        h
        i
        s
        a
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.basis = None
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
        u
        s
        e
        d
        i
        n
        a
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
        a
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.condition = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
        a
        s
        s
        e
        s
        s
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        W
        h
        e
        r
        e
        w
        a
        s
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        p
        e
        r
        f
        o
        r
        m
        e
        d
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        U
        n
        i
        q
        u
        e
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
        a
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
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.method = None
        """ 
        E
        v
        a
        l
        u
        a
        t
        i
        o
        n
        m
        e
        c
        h
        a
        n
        i
        s
        m
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.mitigation = None
        """ 
        H
        o
        w
        t
        o
        r
        e
        d
        u
        c
        e
        r
        i
        s
        k
        .
        Type `str`. """
        
        self.note = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        s
        o
        n
        t
        h
        e
        r
        i
        s
        k
        a
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
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
        w
        a
        s
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        m
        a
        d
        e
        ?
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ 
        W
        h
        e
        n
        w
        a
        s
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        m
        a
        d
        e
        ?
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.parent = None
        """ 
        P
        a
        r
        t
        o
        f
        t
        h
        i
        s
        o
        c
        c
        u
        r
        r
        e
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        W
        h
        o
        d
        i
        d
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prediction = None
        """ 
        O
        u
        t
        c
        o
        m
        e
        p
        r
        e
        d
        i
        c
        t
        e
        d
        .
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        t
        h
        e
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        w
        a
        s
        n
        e
        c
        e
        s
        s
        a
        r
        y
        ?
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        t
        h
        e
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        w
        a
        s
        n
        e
        c
        e
        s
        s
        a
        r
        y
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        r
        e
        g
        i
        s
        t
        e
        r
        e
        d
        |
        p
        r
        e
        l
        i
        m
        i
        n
        a
        r
        y
        |
        f
        i
        n
        a
        l
        |
        a
        m
        e
        n
        d
        e
        d
        +
        .
        Type `str`. """
        
        self.subject = None
        """ 
        W
        h
        o
        /
        w
        h
        a
        t
        d
        o
        e
        s
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        a
        p
        p
        l
        y
        t
        o
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(RiskAssessment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, False, None, False),
            ("basis", "basis", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("condition", "condition", fhirreference.FHIRReference, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("mitigation", "mitigation", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("prediction", "prediction", RiskAssessmentPrediction, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import backboneelement

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ 
    O
    u
    t
    c
    o
    m
    e
    p
    r
    e
    d
    i
    c
    t
    e
    d
    .
    
    
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
    e
    x
    p
    e
    c
    t
    e
    d
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
    s
    u
    b
    j
    e
    c
    t
    .
    
    """
    
    resource_type = "RiskAssessmentPrediction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcome = None
        """ 
        P
        o
        s
        s
        i
        b
        l
        e
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
        s
        u
        b
        j
        e
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.probabilityDecimal = None
        """ 
        L
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
        s
        p
        e
        c
        i
        f
        i
        e
        d
        o
        u
        t
        c
        o
        m
        e
        .
        Type `float`. """
        
        self.probabilityRange = None
        """ 
        L
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
        s
        p
        e
        c
        i
        f
        i
        e
        d
        o
        u
        t
        c
        o
        m
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.qualitativeRisk = None
        """ 
        L
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
        s
        p
        e
        c
        i
        f
        i
        e
        d
        o
        u
        t
        c
        o
        m
        e
        a
        s
        a
        q
        u
        a
        l
        i
        t
        a
        t
        i
        v
        e
        v
        a
        l
        u
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rationale = None
        """ 
        E
        x
        p
        l
        a
        n
        a
        t
        i
        o
        n
        o
        f
        p
        r
        e
        d
        i
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.relativeRisk = None
        """ 
        R
        e
        l
        a
        t
        i
        v
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
        .
        Type `float`. """
        
        self.whenPeriod = None
        """ 
        T
        i
        m
        e
        f
        r
        a
        m
        e
        o
        r
        a
        g
        e
        r
        a
        n
        g
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.whenRange = None
        """ 
        T
        i
        m
        e
        f
        r
        a
        m
        e
        o
        r
        a
        g
        e
        r
        a
        n
        g
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        super(RiskAssessmentPrediction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend([
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("probabilityDecimal", "probabilityDecimal", float, False, "probability", False),
            ("probabilityRange", "probabilityRange", range.Range, False, "probability", False),
            ("qualitativeRisk", "qualitativeRisk", codeableconcept.CodeableConcept, False, None, False),
            ("rationale", "rationale", str, False, None, False),
            ("relativeRisk", "relativeRisk", float, False, None, False),
            ("whenPeriod", "whenPeriod", period.Period, False, "when", False),
            ("whenRange", "whenRange", range.Range, False, "when", False),
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
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
