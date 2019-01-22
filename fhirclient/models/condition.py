#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Condition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Condition(domainresource.DomainResource):
    """ 
    D
    e
    t
    a
    i
    l
    e
    d
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
    a
    b
    o
    u
    t
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
    ,
    p
    r
    o
    b
    l
    e
    m
    s
    o
    r
    d
    i
    a
    g
    n
    o
    s
    e
    s
    .
    
    
    A
    c
    l
    i
    n
    i
    c
    a
    l
    c
    o
    n
    d
    i
    t
    i
    o
    n
    ,
    p
    r
    o
    b
    l
    e
    m
    ,
    d
    i
    a
    g
    n
    o
    s
    i
    s
    ,
    o
    r
    o
    t
    h
    e
    r
    e
    v
    e
    n
    t
    ,
    s
    i
    t
    u
    a
    t
    i
    o
    n
    ,
    i
    s
    s
    u
    e
    ,
    o
    r
    c
    l
    i
    n
    i
    c
    a
    l
    c
    o
    n
    c
    e
    p
    t
    t
    h
    a
    t
    h
    a
    s
    r
    i
    s
    e
    n
    t
    o
    a
    l
    e
    v
    e
    l
    o
    f
    c
    o
    n
    c
    e
    r
    n
    .
    
    """
    
    resource_type = "Condition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abatementAge = None
        """ 
        W
        h
        e
        n
        i
        n
        r
        e
        s
        o
        l
        u
        t
        i
        o
        n
        /
        r
        e
        m
        i
        s
        s
        i
        o
        n
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.abatementDateTime = None
        """ 
        W
        h
        e
        n
        i
        n
        r
        e
        s
        o
        l
        u
        t
        i
        o
        n
        /
        r
        e
        m
        i
        s
        s
        i
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.abatementPeriod = None
        """ 
        W
        h
        e
        n
        i
        n
        r
        e
        s
        o
        l
        u
        t
        i
        o
        n
        /
        r
        e
        m
        i
        s
        s
        i
        o
        n
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.abatementRange = None
        """ 
        W
        h
        e
        n
        i
        n
        r
        e
        s
        o
        l
        u
        t
        i
        o
        n
        /
        r
        e
        m
        i
        s
        s
        i
        o
        n
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.abatementString = None
        """ 
        W
        h
        e
        n
        i
        n
        r
        e
        s
        o
        l
        u
        t
        i
        o
        n
        /
        r
        e
        m
        i
        s
        s
        i
        o
        n
        .
        Type `str`. """
        
        self.asserter = None
        """ 
        P
        e
        r
        s
        o
        n
        w
        h
        o
        a
        s
        s
        e
        r
        t
        s
        t
        h
        i
        s
        c
        o
        n
        d
        i
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ 
        A
        n
        a
        t
        o
        m
        i
        c
        a
        l
        l
        o
        c
        a
        t
        i
        o
        n
        ,
        i
        f
        r
        e
        l
        e
        v
        a
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        p
        r
        o
        b
        l
        e
        m
        -
        l
        i
        s
        t
        -
        i
        t
        e
        m
        |
        e
        n
        c
        o
        u
        n
        t
        e
        r
        -
        d
        i
        a
        g
        n
        o
        s
        i
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.clinicalStatus = None
        """ 
        a
        c
        t
        i
        v
        e
        |
        r
        e
        c
        u
        r
        r
        e
        n
        c
        e
        |
        r
        e
        l
        a
        p
        s
        e
        |
        i
        n
        a
        c
        t
        i
        v
        e
        |
        r
        e
        m
        i
        s
        s
        i
        o
        n
        |
        r
        e
        s
        o
        l
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        c
        o
        n
        d
        i
        t
        i
        o
        n
        ,
        p
        r
        o
        b
        l
        e
        m
        o
        r
        d
        i
        a
        g
        n
        o
        s
        i
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        E
        n
        c
        o
        u
        n
        t
        e
        r
        c
        r
        e
        a
        t
        e
        d
        a
        s
        p
        a
        r
        t
        o
        f
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.evidence = None
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
        e
        v
        i
        d
        e
        n
        c
        e
        .
        List of `ConditionEvidence` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        E
        x
        t
        e
        r
        n
        a
        l
        I
        d
        s
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
        d
        i
        t
        i
        o
        n
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
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
        a
        b
        o
        u
        t
        t
        h
        e
        C
        o
        n
        d
        i
        t
        i
        o
        n
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        d
        o
        r
        a
        c
        t
        u
        a
        l
        d
        a
        t
        e
        ,
        d
        a
        t
        e
        -
        t
        i
        m
        e
        ,
        o
        r
        a
        g
        e
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetDateTime = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        d
        o
        r
        a
        c
        t
        u
        a
        l
        d
        a
        t
        e
        ,
        d
        a
        t
        e
        -
        t
        i
        m
        e
        ,
        o
        r
        a
        g
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onsetPeriod = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        d
        o
        r
        a
        c
        t
        u
        a
        l
        d
        a
        t
        e
        ,
        d
        a
        t
        e
        -
        t
        i
        m
        e
        ,
        o
        r
        a
        g
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        d
        o
        r
        a
        c
        t
        u
        a
        l
        d
        a
        t
        e
        ,
        d
        a
        t
        e
        -
        t
        i
        m
        e
        ,
        o
        r
        a
        g
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        d
        o
        r
        a
        c
        t
        u
        a
        l
        d
        a
        t
        e
        ,
        d
        a
        t
        e
        -
        t
        i
        m
        e
        ,
        o
        r
        a
        g
        e
        .
        Type `str`. """
        
        self.recordedDate = None
        """ 
        D
        a
        t
        e
        r
        e
        c
        o
        r
        d
        w
        a
        s
        f
        i
        r
        s
        t
        r
        e
        c
        o
        r
        d
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recorder = None
        """ 
        W
        h
        o
        r
        e
        c
        o
        r
        d
        e
        d
        t
        h
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.severity = None
        """ 
        S
        u
        b
        j
        e
        c
        t
        i
        v
        e
        s
        e
        v
        e
        r
        i
        t
        y
        o
        f
        c
        o
        n
        d
        i
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stage = None
        """ 
        S
        t
        a
        g
        e
        /
        g
        r
        a
        d
        e
        ,
        u
        s
        u
        a
        l
        l
        y
        a
        s
        s
        e
        s
        s
        e
        d
        f
        o
        r
        m
        a
        l
        l
        y
        .
        List of `ConditionStage` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        W
        h
        o
        h
        a
        s
        t
        h
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
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.verificationStatus = None
        """ 
        u
        n
        c
        o
        n
        f
        i
        r
        m
        e
        d
        |
        p
        r
        o
        v
        i
        s
        i
        o
        n
        a
        l
        |
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
        |
        c
        o
        n
        f
        i
        r
        m
        e
        d
        |
        r
        e
        f
        u
        t
        e
        d
        |
        e
        n
        t
        e
        r
        e
        d
        -
        i
        n
        -
        e
        r
        r
        o
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Condition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementAge", "abatementAge", age.Age, False, "abatement", False),
            ("abatementDateTime", "abatementDateTime", fhirdate.FHIRDate, False, "abatement", False),
            ("abatementPeriod", "abatementPeriod", period.Period, False, "abatement", False),
            ("abatementRange", "abatementRange", range.Range, False, "abatement", False),
            ("abatementString", "abatementString", str, False, "abatement", False),
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evidence", "evidence", ConditionEvidence, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("stage", "stage", ConditionStage, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class ConditionEvidence(backboneelement.BackboneElement):
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
    e
    v
    i
    d
    e
    n
    c
    e
    .
    
    
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
    e
    v
    i
    d
    e
    n
    c
    e
    /
    m
    a
    n
    i
    f
    e
    s
    t
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
    a
    r
    e
    t
    h
    e
    b
    a
    s
    i
    s
    o
    f
    t
    h
    e
    C
    o
    n
    d
    i
    t
    i
    o
    n
    '
    s
    v
    e
    r
    i
    f
    i
    c
    a
    t
    i
    o
    n
    s
    t
    a
    t
    u
    s
    ,
    s
    u
    c
    h
    a
    s
    e
    v
    i
    d
    e
    n
    c
    e
    t
    h
    a
    t
    c
    o
    n
    f
    i
    r
    m
    e
    d
    o
    r
    r
    e
    f
    u
    t
    e
    d
    t
    h
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
    .
    
    """
    
    resource_type = "ConditionEvidence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        M
        a
        n
        i
        f
        e
        s
        t
        a
        t
        i
        o
        n
        /
        s
        y
        m
        p
        t
        o
        m
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.detail = None
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
        f
        o
        u
        n
        d
        e
        l
        s
        e
        w
        h
        e
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ConditionEvidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ConditionStage(backboneelement.BackboneElement):
    """ 
    S
    t
    a
    g
    e
    /
    g
    r
    a
    d
    e
    ,
    u
    s
    u
    a
    l
    l
    y
    a
    s
    s
    e
    s
    s
    e
    d
    f
    o
    r
    m
    a
    l
    l
    y
    .
    
    
    C
    l
    i
    n
    i
    c
    a
    l
    s
    t
    a
    g
    e
    o
    r
    g
    r
    a
    d
    e
    o
    f
    a
    c
    o
    n
    d
    i
    t
    i
    o
    n
    .
    M
    a
    y
    i
    n
    c
    l
    u
    d
    e
    f
    o
    r
    m
    a
    l
    s
    e
    v
    e
    r
    i
    t
    y
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
    s
    .
    
    """
    
    resource_type = "ConditionStage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment = None
        """ 
        F
        o
        r
        m
        a
        l
        r
        e
        c
        o
        r
        d
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.summary = None
        """ 
        S
        i
        m
        p
        l
        e
        s
        u
        m
        m
        a
        r
        y
        (
        d
        i
        s
        e
        a
        s
        e
        s
        p
        e
        c
        i
        f
        i
        c
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        K
        i
        n
        d
        o
        f
        s
        t
        a
        g
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionStage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", fhirreference.FHIRReference, True, None, False),
            ("summary", "summary", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
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
