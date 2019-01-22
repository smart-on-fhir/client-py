#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ClinicalImpression(domainresource.DomainResource):
    """ 
    A
    c
    l
    i
    n
    i
    c
    a
    l
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
    w
    h
    e
    n
    p
    l
    a
    n
    n
    i
    n
    g
    t
    r
    e
    a
    t
    m
    e
    n
    t
    s
    a
    n
    d
    m
    a
    n
    a
    g
    e
    m
    e
    n
    t
    s
    t
    r
    a
    t
    e
    g
    i
    e
    s
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
    .
    
    
    A
    r
    e
    c
    o
    r
    d
    o
    f
    a
    c
    l
    i
    n
    i
    c
    a
    l
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
    p
    r
    o
    b
    l
    e
    m
    (
    s
    )
    m
    a
    y
    a
    f
    f
    e
    c
    t
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
    a
    n
    d
    b
    e
    f
    o
    r
    e
    p
    l
    a
    n
    n
    i
    n
    g
    t
    h
    e
    t
    r
    e
    a
    t
    m
    e
    n
    t
    s
    o
    r
    m
    a
    n
    a
    g
    e
    m
    e
    n
    t
    s
    t
    r
    a
    t
    e
    g
    i
    e
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
    s
    t
    t
    o
    m
    a
    n
    a
    g
    e
    a
    p
    a
    t
    i
    e
    n
    t
    '
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
    s
    a
    r
    e
    o
    f
    t
    e
    n
    1
    :
    1
    w
    i
    t
    h
    a
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
    s
    u
    l
    t
    a
    t
    i
    o
    n
    /
    e
    n
    c
    o
    u
    n
    t
    e
    r
    ,
    b
    u
    t
    t
    h
    i
    s
    v
    a
    r
    i
    e
    s
    g
    r
    e
    a
    t
    l
    y
    d
    e
    p
    e
    n
    d
    i
    n
    g
    o
    n
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
    w
    o
    r
    k
    f
    l
    o
    w
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
    c
    a
    l
    l
    e
    d
    "
    C
    l
    i
    n
    i
    c
    a
    l
    I
    m
    p
    r
    e
    s
    s
    i
    o
    n
    "
    r
    a
    t
    h
    e
    r
    t
    h
    a
    n
    "
    C
    l
    i
    n
    i
    c
    a
    l
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
    "
    t
    o
    a
    v
    o
    i
    d
    c
    o
    n
    f
    u
    s
    i
    o
    n
    w
    i
    t
    h
    t
    h
    e
    r
    e
    c
    o
    r
    d
    i
    n
    g
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
    t
    o
    o
    l
    s
    s
    u
    c
    h
    a
    s
    A
    p
    g
    a
    r
    s
    c
    o
    r
    e
    .
    
    """
    
    resource_type = "ClinicalImpression"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessor = None
        """ 
        T
        h
        e
        c
        l
        i
        n
        i
        c
        i
        a
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
        
        self.code = None
        """ 
        K
        i
        n
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        W
        h
        e
        n
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
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ 
        W
        h
        y
        /
        h
        o
        w
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
        
        self.effectiveDateTime = None
        """ 
        T
        i
        m
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
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ 
        T
        i
        m
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
        Type `Period` (represented as `dict` in JSON). """
        
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
        
        self.finding = None
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
        r
        l
        i
        k
        e
        l
        y
        f
        i
        n
        d
        i
        n
        g
        s
        a
        n
        d
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
        List of `ClinicalImpressionFinding` items (represented as `dict` in JSON). """
        
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.investigation = None
        """ 
        O
        n
        e
        o
        r
        m
        o
        r
        e
        s
        e
        t
        s
        o
        f
        i
        n
        v
        e
        s
        t
        i
        g
        a
        t
        i
        o
        n
        s
        (
        s
        i
        g
        n
        s
        ,
        s
        y
        m
        p
        t
        o
        m
        s
        ,
        e
        t
        c
        .
        )
        .
        List of `ClinicalImpressionInvestigation` items (represented as `dict` in JSON). """
        
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
        m
        a
        d
        e
        a
        b
        o
        u
        t
        t
        h
        e
        C
        l
        i
        n
        i
        c
        a
        l
        I
        m
        p
        r
        e
        s
        s
        i
        o
        n
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.previous = None
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
        l
        a
        s
        t
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
        
        self.problem = None
        """ 
        R
        e
        l
        e
        v
        a
        n
        t
        i
        m
        p
        r
        e
        s
        s
        i
        o
        n
        s
        o
        f
        p
        a
        t
        i
        e
        n
        t
        s
        t
        a
        t
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.prognosisCodeableConcept = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        o
        f
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.prognosisReference = None
        """ 
        R
        i
        s
        k
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
        e
        x
        p
        r
        e
        s
        s
        i
        n
        g
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.protocol = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        P
        r
        o
        t
        o
        c
        o
        l
        f
        o
        l
        l
        o
        w
        e
        d
        .
        List of `str` items. """
        
        self.status = None
        """ 
        d
        r
        a
        f
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
        Type `str`. """
        
        self.statusReason = None
        """ 
        R
        e
        a
        s
        o
        n
        f
        o
        r
        c
        u
        r
        r
        e
        n
        t
        s
        t
        a
        t
        u
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        o
        r
        g
        r
        o
        u
        p
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
        
        self.summary = None
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
        Type `str`. """
        
        self.supportingInfo = None
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
        s
        u
        p
        p
        o
        r
        t
        i
        n
        g
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
        i
        m
        p
        r
        e
        s
        s
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClinicalImpression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpression, self).elementProperties()
        js.extend([
            ("assessor", "assessor", fhirreference.FHIRReference, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("finding", "finding", ClinicalImpressionFinding, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("investigation", "investigation", ClinicalImpressionInvestigation, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("previous", "previous", fhirreference.FHIRReference, False, None, False),
            ("problem", "problem", fhirreference.FHIRReference, True, None, False),
            ("prognosisCodeableConcept", "prognosisCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("prognosisReference", "prognosisReference", fhirreference.FHIRReference, True, None, False),
            ("protocol", "protocol", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("summary", "summary", str, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class ClinicalImpressionFinding(backboneelement.BackboneElement):
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
    r
    l
    i
    k
    e
    l
    y
    f
    i
    n
    d
    i
    n
    g
    s
    a
    n
    d
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
    
    
    S
    p
    e
    c
    i
    f
    i
    c
    f
    i
    n
    d
    i
    n
    g
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
    t
    h
    a
    t
    w
    e
    r
    e
    c
    o
    n
    s
    i
    d
    e
    r
    e
    d
    l
    i
    k
    e
    l
    y
    o
    r
    r
    e
    l
    e
    v
    a
    n
    t
    t
    o
    o
    n
    g
    o
    i
    n
    g
    t
    r
    e
    a
    t
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "ClinicalImpressionFinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basis = None
        """ 
        W
        h
        i
        c
        h
        i
        n
        v
        e
        s
        t
        i
        g
        a
        t
        i
        o
        n
        s
        s
        u
        p
        p
        o
        r
        t
        f
        i
        n
        d
        i
        n
        g
        .
        Type `str`. """
        
        self.itemCodeableConcept = None
        """ 
        W
        h
        a
        t
        w
        a
        s
        f
        o
        u
        n
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ 
        W
        h
        a
        t
        w
        a
        s
        f
        o
        u
        n
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionFinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionFinding, self).elementProperties()
        js.extend([
            ("basis", "basis", str, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, None, False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class ClinicalImpressionInvestigation(backboneelement.BackboneElement):
    """ 
    O
    n
    e
    o
    r
    m
    o
    r
    e
    s
    e
    t
    s
    o
    f
    i
    n
    v
    e
    s
    t
    i
    g
    a
    t
    i
    o
    n
    s
    (
    s
    i
    g
    n
    s
    ,
    s
    y
    m
    p
    t
    o
    m
    s
    ,
    e
    t
    c
    .
    )
    .
    
    
    O
    n
    e
    o
    r
    m
    o
    r
    e
    s
    e
    t
    s
    o
    f
    i
    n
    v
    e
    s
    t
    i
    g
    a
    t
    i
    o
    n
    s
    (
    s
    i
    g
    n
    s
    ,
    s
    y
    m
    p
    t
    o
    m
    s
    ,
    e
    t
    c
    .
    )
    .
    T
    h
    e
    a
    c
    t
    u
    a
    l
    g
    r
    o
    u
    p
    i
    n
    g
    o
    f
    i
    n
    v
    e
    s
    t
    i
    g
    a
    t
    i
    o
    n
    s
    v
    a
    r
    i
    e
    s
    g
    r
    e
    a
    t
    l
    y
    d
    e
    p
    e
    n
    d
    i
    n
    g
    o
    n
    t
    h
    e
    t
    y
    p
    e
    a
    n
    d
    c
    o
    n
    t
    e
    x
    t
    o
    f
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
    T
    h
    e
    s
    e
    i
    n
    v
    e
    s
    t
    i
    g
    a
    t
    i
    o
    n
    s
    m
    a
    y
    i
    n
    c
    l
    u
    d
    e
    d
    a
    t
    a
    g
    e
    n
    e
    r
    a
    t
    e
    d
    d
    u
    r
    i
    n
    g
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
    p
    r
    o
    c
    e
    s
    s
    ,
    o
    r
    d
    a
    t
    a
    p
    r
    e
    v
    i
    o
    u
    s
    l
    y
    g
    e
    n
    e
    r
    a
    t
    e
    d
    a
    n
    d
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
    a
    t
    i
    s
    p
    e
    r
    t
    i
    n
    e
    n
    t
    t
    o
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
    s
    .
    
    """
    
    resource_type = "ClinicalImpressionInvestigation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        A
        n
        a
        m
        e
        /
        c
        o
        d
        e
        f
        o
        r
        t
        h
        e
        s
        e
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        """ 
        R
        e
        c
        o
        r
        d
        o
        f
        a
        s
        p
        e
        c
        i
        f
        i
        c
        i
        n
        v
        e
        s
        t
        i
        g
        a
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClinicalImpressionInvestigation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionInvestigation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("item", "item", fhirreference.FHIRReference, True, None, False),
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
