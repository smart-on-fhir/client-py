#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DiagnosticReport(domainresource.DomainResource):
    """ 
    A
    D
    i
    a
    g
    n
    o
    s
    t
    i
    c
    r
    e
    p
    o
    r
    t
    -
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
    q
    u
    e
    s
    t
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
    ,
    a
    t
    o
    m
    i
    c
    r
    e
    s
    u
    l
    t
    s
    ,
    i
    m
    a
    g
    e
    s
    ,
    i
    n
    t
    e
    r
    p
    r
    e
    t
    a
    t
    i
    o
    n
    ,
    a
    s
    w
    e
    l
    l
    a
    s
    f
    o
    r
    m
    a
    t
    t
    e
    d
    r
    e
    p
    o
    r
    t
    s
    .
    
    
    T
    h
    e
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
    i
    n
    t
    e
    r
    p
    r
    e
    t
    a
    t
    i
    o
    n
    o
    f
    d
    i
    a
    g
    n
    o
    s
    t
    i
    c
    t
    e
    s
    t
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
    o
    n
    p
    a
    t
    i
    e
    n
    t
    s
    ,
    g
    r
    o
    u
    p
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
    ,
    d
    e
    v
    i
    c
    e
    s
    ,
    a
    n
    d
    l
    o
    c
    a
    t
    i
    o
    n
    s
    ,
    a
    n
    d
    /
    o
    r
    s
    p
    e
    c
    i
    m
    e
    n
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
    t
    h
    e
    s
    e
    .
    T
    h
    e
    r
    e
    p
    o
    r
    t
    i
    n
    c
    l
    u
    d
    e
    s
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
    t
    e
    x
    t
    s
    u
    c
    h
    a
    s
    r
    e
    q
    u
    e
    s
    t
    i
    n
    g
    a
    n
    d
    p
    r
    o
    v
    i
    d
    e
    r
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
    ,
    a
    n
    d
    s
    o
    m
    e
    m
    i
    x
    o
    f
    a
    t
    o
    m
    i
    c
    r
    e
    s
    u
    l
    t
    s
    ,
    i
    m
    a
    g
    e
    s
    ,
    t
    e
    x
    t
    u
    a
    l
    a
    n
    d
    c
    o
    d
    e
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
    a
    t
    i
    o
    n
    s
    ,
    a
    n
    d
    f
    o
    r
    m
    a
    t
    t
    e
    d
    r
    e
    p
    r
    e
    s
    e
    n
    t
    a
    t
    i
    o
    n
    o
    f
    d
    i
    a
    g
    n
    o
    s
    t
    i
    c
    r
    e
    p
    o
    r
    t
    s
    .
    
    """
    
    resource_type = "DiagnosticReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ 
        W
        h
        a
        t
        w
        a
        s
        r
        e
        q
        u
        e
        s
        t
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        c
        a
        t
        e
        g
        o
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        N
        a
        m
        e
        /
        C
        o
        d
        e
        f
        o
        r
        t
        h
        i
        s
        d
        i
        a
        g
        n
        o
        s
        t
        i
        c
        r
        e
        p
        o
        r
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.conclusion = None
        """ 
        C
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
        l
        u
        s
        i
        o
        n
        (
        i
        n
        t
        e
        r
        p
        r
        e
        t
        a
        t
        i
        o
        n
        )
        o
        f
        t
        e
        s
        t
        r
        e
        s
        u
        l
        t
        s
        .
        Type `str`. """
        
        self.conclusionCode = None
        """ 
        C
        o
        d
        e
        s
        f
        o
        r
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
        c
        o
        n
        c
        l
        u
        s
        i
        o
        n
        o
        f
        t
        e
        s
        t
        r
        e
        s
        u
        l
        t
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        l
        y
        r
        e
        l
        e
        v
        a
        n
        t
        t
        i
        m
        e
        /
        t
        i
        m
        e
        -
        p
        e
        r
        i
        o
        d
        f
        o
        r
        r
        e
        p
        o
        r
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        l
        y
        r
        e
        l
        e
        v
        a
        n
        t
        t
        i
        m
        e
        /
        t
        i
        m
        e
        -
        p
        e
        r
        i
        o
        d
        f
        o
        r
        r
        e
        p
        o
        r
        t
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        H
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
        w
        h
        e
        n
        t
        e
        s
        t
        o
        r
        d
        e
        r
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        r
        e
        p
        o
        r
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
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
        f
        u
        l
        l
        d
        e
        t
        a
        i
        l
        s
        o
        f
        i
        m
        a
        g
        i
        n
        g
        a
        s
        s
        o
        c
        i
        a
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
        d
        i
        a
        g
        n
        o
        s
        t
        i
        c
        r
        e
        p
        o
        r
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.issued = None
        """ 
        D
        a
        t
        e
        T
        i
        m
        e
        t
        h
        i
        s
        v
        e
        r
        s
        i
        o
        n
        w
        a
        s
        m
        a
        d
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.media = None
        """ 
        K
        e
        y
        i
        m
        a
        g
        e
        s
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        t
        h
        i
        s
        r
        e
        p
        o
        r
        t
        .
        List of `DiagnosticReportMedia` items (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        R
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        D
        i
        a
        g
        n
        o
        s
        t
        i
        c
        S
        e
        r
        v
        i
        c
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.presentedForm = None
        """ 
        E
        n
        t
        i
        r
        e
        r
        e
        p
        o
        r
        t
        a
        s
        i
        s
        s
        u
        e
        d
        .
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.result = None
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
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.resultsInterpreter = None
        """ 
        P
        r
        i
        m
        a
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
        t
        e
        r
        p
        r
        e
        t
        e
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        s
        t
        h
        i
        s
        r
        e
        p
        o
        r
        t
        i
        s
        b
        a
        s
        e
        d
        o
        n
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
        a
        r
        t
        i
        a
        l
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
        +
        .
        Type `str`. """
        
        self.subject = None
        """ 
        T
        h
        e
        s
        u
        b
        j
        e
        c
        t
        o
        f
        t
        h
        e
        r
        e
        p
        o
        r
        t
        -
        u
        s
        u
        a
        l
        l
        y
        ,
        b
        u
        t
        n
        o
        t
        a
        l
        w
        a
        y
        s
        ,
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DiagnosticReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("conclusion", "conclusion", str, False, None, False),
            ("conclusionCode", "conclusionCode", codeableconcept.CodeableConcept, True, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("media", "media", DiagnosticReportMedia, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("presentedForm", "presentedForm", attachment.Attachment, True, None, False),
            ("result", "result", fhirreference.FHIRReference, True, None, False),
            ("resultsInterpreter", "resultsInterpreter", fhirreference.FHIRReference, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class DiagnosticReportMedia(backboneelement.BackboneElement):
    """ 
    K
    e
    y
    i
    m
    a
    g
    e
    s
    a
    s
    s
    o
    c
    i
    a
    t
    e
    d
    w
    i
    t
    h
    t
    h
    i
    s
    r
    e
    p
    o
    r
    t
    .
    
    
    A
    l
    i
    s
    t
    o
    f
    k
    e
    y
    i
    m
    a
    g
    e
    s
    a
    s
    s
    o
    c
    i
    a
    t
    e
    d
    w
    i
    t
    h
    t
    h
    i
    s
    r
    e
    p
    o
    r
    t
    .
    T
    h
    e
    i
    m
    a
    g
    e
    s
    a
    r
    e
    g
    e
    n
    e
    r
    a
    l
    l
    y
    c
    r
    e
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
    d
    i
    a
    g
    n
    o
    s
    t
    i
    c
    p
    r
    o
    c
    e
    s
    s
    ,
    a
    n
    d
    m
    a
    y
    b
    e
    d
    i
    r
    e
    c
    t
    l
    y
    o
    f
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
    ,
    o
    r
    o
    f
    t
    r
    e
    a
    t
    e
    d
    s
    p
    e
    c
    i
    m
    e
    n
    s
    (
    i
    .
    e
    .
    s
    l
    i
    d
    e
    s
    o
    f
    i
    n
    t
    e
    r
    e
    s
    t
    )
    .
    
    """
    
    resource_type = "DiagnosticReportMedia"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        a
        b
        o
        u
        t
        t
        h
        e
        i
        m
        a
        g
        e
        (
        e
        .
        g
        .
        e
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
        )
        .
        Type `str`. """
        
        self.link = None
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
        t
        h
        e
        i
        m
        a
        g
        e
        s
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DiagnosticReportMedia, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReportMedia, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("link", "link", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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
