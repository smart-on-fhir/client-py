#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AdverseEvent) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class AdverseEvent(domainresource.DomainResource):
    """ 
    M
    e
    d
    i
    c
    a
    l
    c
    a
    r
    e
    ,
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
    y
    o
    r
    o
    t
    h
    e
    r
    h
    e
    a
    l
    t
    h
    c
    a
    r
    e
    e
    v
    e
    n
    t
    c
    a
    u
    s
    i
    n
    g
    p
    h
    y
    s
    i
    c
    a
    l
    i
    n
    j
    u
    r
    y
    .
    
    
    A
    c
    t
    u
    a
    l
    o
    r
    p
    o
    t
    e
    n
    t
    i
    a
    l
    /
    a
    v
    o
    i
    d
    e
    d
    e
    v
    e
    n
    t
    c
    a
    u
    s
    i
    n
    g
    u
    n
    i
    n
    t
    e
    n
    d
    e
    d
    p
    h
    y
    s
    i
    c
    a
    l
    i
    n
    j
    u
    r
    y
    r
    e
    s
    u
    l
    t
    i
    n
    g
    f
    r
    o
    m
    o
    r
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
    d
    t
    o
    b
    y
    m
    e
    d
    i
    c
    a
    l
    c
    a
    r
    e
    ,
    a
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
    y
    o
    r
    o
    t
    h
    e
    r
    h
    e
    a
    l
    t
    h
    c
    a
    r
    e
    s
    e
    t
    t
    i
    n
    g
    f
    a
    c
    t
    o
    r
    s
    t
    h
    a
    t
    r
    e
    q
    u
    i
    r
    e
    s
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
    m
    o
    n
    i
    t
    o
    r
    i
    n
    g
    ,
    t
    r
    e
    a
    t
    m
    e
    n
    t
    ,
    o
    r
    h
    o
    s
    p
    i
    t
    a
    l
    i
    z
    a
    t
    i
    o
    n
    ,
    o
    r
    t
    h
    a
    t
    r
    e
    s
    u
    l
    t
    s
    i
    n
    d
    e
    a
    t
    h
    .
    
    """
    
    resource_type = "AdverseEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actuality = None
        """ 
        a
        c
        t
        u
        a
        l
        |
        p
        o
        t
        e
        n
        t
        i
        a
        l
        .
        Type `str`. """
        
        self.category = None
        """ 
        p
        r
        o
        d
        u
        c
        t
        -
        p
        r
        o
        b
        l
        e
        m
        |
        p
        r
        o
        d
        u
        c
        t
        -
        q
        u
        a
        l
        i
        t
        y
        |
        p
        r
        o
        d
        u
        c
        t
        -
        u
        s
        e
        -
        e
        r
        r
        o
        r
        |
        w
        r
        o
        n
        g
        -
        d
        o
        s
        e
        |
        i
        n
        c
        o
        r
        r
        e
        c
        t
        -
        p
        r
        e
        s
        c
        r
        i
        b
        i
        n
        g
        -
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
        |
        w
        r
        o
        n
        g
        -
        t
        e
        c
        h
        n
        i
        q
        u
        e
        |
        w
        r
        o
        n
        g
        -
        r
        o
        u
        t
        e
        -
        o
        f
        -
        a
        d
        m
        i
        n
        i
        s
        t
        r
        a
        t
        i
        o
        n
        |
        w
        r
        o
        n
        g
        -
        r
        a
        t
        e
        |
        w
        r
        o
        n
        g
        -
        d
        u
        r
        a
        t
        i
        o
        n
        |
        w
        r
        o
        n
        g
        -
        t
        i
        m
        e
        |
        e
        x
        p
        i
        r
        e
        d
        -
        d
        r
        u
        g
        |
        m
        e
        d
        i
        c
        a
        l
        -
        d
        e
        v
        i
        c
        e
        -
        u
        s
        e
        -
        e
        r
        r
        o
        r
        |
        p
        r
        o
        b
        l
        e
        m
        -
        d
        i
        f
        f
        e
        r
        e
        n
        t
        -
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        r
        |
        u
        n
        s
        a
        f
        e
        -
        p
        h
        y
        s
        i
        c
        a
        l
        -
        e
        n
        v
        i
        r
        o
        n
        m
        e
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.contributor = None
        """ 
        W
        h
        o
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
        i
        n
        t
        h
        e
        a
        d
        v
        e
        r
        s
        e
        e
        v
        e
        n
        t
        o
        r
        t
        h
        e
        p
        o
        t
        e
        n
        t
        i
        a
        l
        a
        d
        v
        e
        r
        s
        e
        e
        v
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.date = None
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
        e
        n
        t
        o
        c
        c
        u
        r
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detected = None
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
        e
        n
        t
        w
        a
        s
        d
        e
        t
        e
        c
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        
        self.event = None
        """ 
        T
        y
        p
        e
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        i
        t
        s
        e
        l
        f
        i
        n
        r
        e
        l
        a
        t
        i
        o
        n
        t
        o
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
        
        self.identifier = None
        """ 
        B
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
        f
        o
        r
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.location = None
        """ 
        L
        o
        c
        a
        t
        i
        o
        n
        w
        h
        e
        r
        e
        a
        d
        v
        e
        r
        s
        e
        e
        v
        e
        n
        t
        o
        c
        c
        u
        r
        r
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ 
        r
        e
        s
        o
        l
        v
        e
        d
        |
        r
        e
        c
        o
        v
        e
        r
        i
        n
        g
        |
        o
        n
        g
        o
        i
        n
        g
        |
        r
        e
        s
        o
        l
        v
        e
        d
        W
        i
        t
        h
        S
        e
        q
        u
        e
        l
        a
        e
        |
        f
        a
        t
        a
        l
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recordedDate = None
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
        e
        n
        t
        w
        a
        s
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
        a
        d
        v
        e
        r
        s
        e
        e
        v
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referenceDocument = None
        """ 
        A
        d
        v
        e
        r
        s
        e
        E
        v
        e
        n
        t
        .
        r
        e
        f
        e
        r
        e
        n
        c
        e
        D
        o
        c
        u
        m
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.resultingCondition = None
        """ 
        E
        f
        f
        e
        c
        t
        o
        n
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
        d
        u
        e
        t
        o
        t
        h
        i
        s
        e
        v
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.seriousness = None
        """ 
        S
        e
        r
        i
        o
        u
        s
        n
        e
        s
        s
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.severity = None
        """ 
        m
        i
        l
        d
        |
        m
        o
        d
        e
        r
        a
        t
        e
        |
        s
        e
        v
        e
        r
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.study = None
        """ 
        A
        d
        v
        e
        r
        s
        e
        E
        v
        e
        n
        t
        .
        s
        t
        u
        d
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        S
        u
        b
        j
        e
        c
        t
        i
        m
        p
        a
        c
        t
        e
        d
        b
        y
        e
        v
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subjectMedicalHistory = None
        """ 
        A
        d
        v
        e
        r
        s
        e
        E
        v
        e
        n
        t
        .
        s
        u
        b
        j
        e
        c
        t
        M
        e
        d
        i
        c
        a
        l
        H
        i
        s
        t
        o
        r
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.suspectEntity = None
        """ 
        T
        h
        e
        s
        u
        s
        p
        e
        c
        t
        e
        d
        a
        g
        e
        n
        t
        c
        a
        u
        s
        i
        n
        g
        t
        h
        e
        a
        d
        v
        e
        r
        s
        e
        e
        v
        e
        n
        t
        .
        List of `AdverseEventSuspectEntity` items (represented as `dict` in JSON). """
        
        super(AdverseEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEvent, self).elementProperties()
        js.extend([
            ("actuality", "actuality", str, False, None, True),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("detected", "detected", fhirdate.FHIRDate, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("event", "event", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("referenceDocument", "referenceDocument", fhirreference.FHIRReference, True, None, False),
            ("resultingCondition", "resultingCondition", fhirreference.FHIRReference, True, None, False),
            ("seriousness", "seriousness", codeableconcept.CodeableConcept, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("study", "study", fhirreference.FHIRReference, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("subjectMedicalHistory", "subjectMedicalHistory", fhirreference.FHIRReference, True, None, False),
            ("suspectEntity", "suspectEntity", AdverseEventSuspectEntity, True, None, False),
        ])
        return js


from . import backboneelement

class AdverseEventSuspectEntity(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    s
    u
    s
    p
    e
    c
    t
    e
    d
    a
    g
    e
    n
    t
    c
    a
    u
    s
    i
    n
    g
    t
    h
    e
    a
    d
    v
    e
    r
    s
    e
    e
    v
    e
    n
    t
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
    n
    t
    i
    t
    y
    t
    h
    a
    t
    i
    s
    s
    u
    s
    p
    e
    c
    t
    e
    d
    t
    o
    h
    a
    v
    e
    c
    a
    u
    s
    e
    d
    t
    h
    e
    a
    d
    v
    e
    r
    s
    e
    e
    v
    e
    n
    t
    .
    
    """
    
    resource_type = "AdverseEventSuspectEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.causality = None
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
        o
        n
        t
        h
        e
        p
        o
        s
        s
        i
        b
        l
        e
        c
        a
        u
        s
        e
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        .
        List of `AdverseEventSuspectEntityCausality` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ 
        R
        e
        f
        e
        r
        s
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
        e
        n
        t
        i
        t
        y
        t
        h
        a
        t
        c
        a
        u
        s
        e
        d
        t
        h
        e
        a
        d
        v
        e
        r
        s
        e
        e
        v
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(AdverseEventSuspectEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEventSuspectEntity, self).elementProperties()
        js.extend([
            ("causality", "causality", AdverseEventSuspectEntityCausality, True, None, False),
            ("instance", "instance", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class AdverseEventSuspectEntityCausality(backboneelement.BackboneElement):
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
    o
    n
    t
    h
    e
    p
    o
    s
    s
    i
    b
    l
    e
    c
    a
    u
    s
    e
    o
    f
    t
    h
    e
    e
    v
    e
    n
    t
    .
    """
    
    resource_type = "AdverseEventSuspectEntityCausality"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment = None
        """ 
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
        o
        f
        i
        f
        t
        h
        e
        e
        n
        t
        i
        t
        y
        c
        a
        u
        s
        e
        d
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.author = None
        """ 
        A
        d
        v
        e
        r
        s
        e
        E
        v
        e
        n
        t
        .
        s
        u
        s
        p
        e
        c
        t
        E
        n
        t
        i
        t
        y
        .
        c
        a
        u
        s
        a
        l
        i
        t
        y
        A
        u
        t
        h
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.method = None
        """ 
        P
        r
        o
        b
        a
        b
        i
        l
        i
        t
        y
        S
        c
        a
        l
        e
        |
        B
        a
        y
        e
        s
        i
        a
        n
        |
        C
        h
        e
        c
        k
        l
        i
        s
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productRelatedness = None
        """ 
        A
        d
        v
        e
        r
        s
        e
        E
        v
        e
        n
        t
        .
        s
        u
        s
        p
        e
        c
        t
        E
        n
        t
        i
        t
        y
        .
        c
        a
        u
        s
        a
        l
        i
        t
        y
        P
        r
        o
        d
        u
        c
        t
        R
        e
        l
        a
        t
        e
        d
        n
        e
        s
        s
        .
        Type `str`. """
        
        super(AdverseEventSuspectEntityCausality, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AdverseEventSuspectEntityCausality, self).elementProperties()
        js.extend([
            ("assessment", "assessment", codeableconcept.CodeableConcept, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("productRelatedness", "productRelatedness", str, False, None, False),
        ])
        return js


import sys
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
