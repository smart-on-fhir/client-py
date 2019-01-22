#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DetectedIssue) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DetectedIssue(domainresource.DomainResource):
    """ 
    C
    l
    i
    n
    i
    c
    a
    l
    i
    s
    s
    u
    e
    w
    i
    t
    h
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
    a
    n
    a
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
    c
    l
    i
    n
    i
    c
    a
    l
    i
    s
    s
    u
    e
    w
    i
    t
    h
    o
    r
    b
    e
    t
    w
    e
    e
    n
    o
    n
    e
    o
    r
    m
    o
    r
    e
    a
    c
    t
    i
    v
    e
    o
    r
    p
    r
    o
    p
    o
    s
    e
    d
    c
    l
    i
    n
    i
    c
    a
    l
    a
    c
    t
    i
    o
    n
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
    ;
    e
    .
    g
    .
    D
    r
    u
    g
    -
    d
    r
    u
    g
    i
    n
    t
    e
    r
    a
    c
    t
    i
    o
    n
    ,
    I
    n
    e
    f
    f
    e
    c
    t
    i
    v
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
    f
    r
    e
    q
    u
    e
    n
    c
    y
    ,
    P
    r
    o
    c
    e
    d
    u
    r
    e
    -
    c
    o
    n
    d
    i
    t
    i
    o
    n
    c
    o
    n
    f
    l
    i
    c
    t
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "DetectedIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ 
        T
        h
        e
        p
        r
        o
        v
        i
        d
        e
        r
        o
        r
        d
        e
        v
        i
        c
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
        d
        t
        h
        e
        i
        s
        s
        u
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        I
        s
        s
        u
        e
        C
        a
        t
        e
        g
        o
        r
        y
        ,
        e
        .
        g
        .
        d
        r
        u
        g
        -
        d
        r
        u
        g
        ,
        d
        u
        p
        l
        i
        c
        a
        t
        e
        t
        h
        e
        r
        a
        p
        y
        ,
        e
        t
        c
        .
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
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
        .
        Type `str`. """
        
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
        List of `DetectedIssueEvidence` items (represented as `dict` in JSON). """
        
        self.identifiedDateTime = None
        """ 
        W
        h
        e
        n
        i
        d
        e
        n
        t
        i
        f
        i
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifiedPeriod = None
        """ 
        W
        h
        e
        n
        i
        d
        e
        n
        t
        i
        f
        i
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
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
        f
        o
        r
        t
        h
        e
        d
        e
        t
        e
        c
        t
        e
        d
        i
        s
        s
        u
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.implicated = None
        """ 
        P
        r
        o
        b
        l
        e
        m
        r
        e
        s
        o
        u
        r
        c
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.mitigation = None
        """ 
        S
        t
        e
        p
        t
        a
        k
        e
        n
        t
        o
        a
        d
        d
        r
        e
        s
        s
        .
        List of `DetectedIssueMitigation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        A
        s
        s
        o
        c
        i
        a
        t
        e
        d
        p
        a
        t
        i
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reference = None
        """ 
        A
        u
        t
        h
        o
        r
        i
        t
        y
        f
        o
        r
        i
        s
        s
        u
        e
        .
        Type `str`. """
        
        self.severity = None
        """ 
        h
        i
        g
        h
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
        l
        o
        w
        .
        Type `str`. """
        
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
        
        super(DetectedIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", str, False, None, False),
            ("evidence", "evidence", DetectedIssueEvidence, True, None, False),
            ("identifiedDateTime", "identifiedDateTime", fhirdate.FHIRDate, False, "identified", False),
            ("identifiedPeriod", "identifiedPeriod", period.Period, False, "identified", False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("implicated", "implicated", fhirreference.FHIRReference, True, None, False),
            ("mitigation", "mitigation", DetectedIssueMitigation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class DetectedIssueEvidence(backboneelement.BackboneElement):
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
    o
    r
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
    p
    r
    o
    v
    i
    d
    e
    t
    h
    e
    b
    a
    s
    i
    s
    f
    o
    r
    i
    d
    e
    n
    t
    i
    f
    y
    i
    n
    g
    t
    h
    e
    d
    e
    t
    e
    c
    t
    e
    d
    i
    s
    s
    u
    e
    s
    u
    c
    h
    a
    s
    a
    G
    u
    i
    d
    a
    n
    c
    e
    R
    e
    s
    p
    o
    n
    s
    e
    o
    r
    M
    e
    a
    s
    u
    r
    e
    R
    e
    p
    o
    r
    t
    .
    
    """
    
    resource_type = "DetectedIssueEvidence"
    
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(DetectedIssueEvidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssueEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ 
    S
    t
    e
    p
    t
    a
    k
    e
    n
    t
    o
    a
    d
    d
    r
    e
    s
    s
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
    a
    n
    a
    c
    t
    i
    o
    n
    t
    h
    a
    t
    h
    a
    s
    b
    e
    e
    n
    t
    a
    k
    e
    n
    o
    r
    i
    s
    c
    o
    m
    m
    i
    t
    t
    e
    d
    t
    o
    r
    e
    d
    u
    c
    e
    o
    r
    e
    l
    i
    m
    i
    n
    a
    t
    e
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
    t
    h
    e
    r
    i
    s
    k
    i
    d
    e
    n
    t
    i
    f
    i
    e
    d
    b
    y
    t
    h
    e
    d
    e
    t
    e
    c
    t
    e
    d
    i
    s
    s
    u
    e
    f
    r
    o
    m
    m
    a
    n
    i
    f
    e
    s
    t
    i
    n
    g
    .
    C
    a
    n
    a
    l
    s
    o
    r
    e
    f
    l
    e
    c
    t
    a
    n
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
    o
    f
    k
    n
    o
    w
    n
    m
    i
    t
    i
    g
    a
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
    m
    a
    y
    r
    e
    d
    u
    c
    e
    /
    e
    l
    i
    m
    i
    n
    a
    t
    e
    t
    h
    e
    n
    e
    e
    d
    f
    o
    r
    a
    n
    y
    a
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "DetectedIssueMitigation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        W
        h
        a
        t
        m
        i
        t
        i
        g
        a
        t
        i
        o
        n
        ?
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.author = None
        """ 
        W
        h
        o
        i
        s
        c
        o
        m
        m
        i
        t
        t
        i
        n
        g
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        D
        a
        t
        e
        c
        o
        m
        m
        i
        t
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(DetectedIssueMitigation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, True),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
