#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ImagingStudy(domainresource.DomainResource):
    """ 
    A
    s
    e
    t
    o
    f
    i
    m
    a
    g
    e
    s
    p
    r
    o
    d
    u
    c
    e
    d
    i
    n
    s
    i
    n
    g
    l
    e
    s
    t
    u
    d
    y
    (
    o
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
    r
    i
    e
    s
    o
    f
    r
    e
    f
    e
    r
    e
    n
    c
    e
    s
    i
    m
    a
    g
    e
    s
    )
    .
    
    
    R
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
    p
    r
    o
    d
    u
    c
    e
    d
    i
    n
    a
    D
    I
    C
    O
    M
    i
    m
    a
    g
    i
    n
    g
    s
    t
    u
    d
    y
    .
    A
    s
    t
    u
    d
    y
    c
    o
    m
    p
    r
    i
    s
    e
    s
    a
    s
    e
    t
    o
    f
    s
    e
    r
    i
    e
    s
    ,
    e
    a
    c
    h
    o
    f
    w
    h
    i
    c
    h
    i
    n
    c
    l
    u
    d
    e
    s
    a
    s
    e
    t
    o
    f
    S
    e
    r
    v
    i
    c
    e
    -
    O
    b
    j
    e
    c
    t
    P
    a
    i
    r
    I
    n
    s
    t
    a
    n
    c
    e
    s
    (
    S
    O
    P
    I
    n
    s
    t
    a
    n
    c
    e
    s
    -
    i
    m
    a
    g
    e
    s
    o
    r
    o
    t
    h
    e
    r
    d
    a
    t
    a
    )
    a
    c
    q
    u
    i
    r
    e
    d
    o
    r
    p
    r
    o
    d
    u
    c
    e
    d
    i
    n
    a
    c
    o
    m
    m
    o
    n
    c
    o
    n
    t
    e
    x
    t
    .
    A
    s
    e
    r
    i
    e
    s
    i
    s
    o
    f
    o
    n
    l
    y
    o
    n
    e
    m
    o
    d
    a
    l
    i
    t
    y
    (
    e
    .
    g
    .
    X
    -
    r
    a
    y
    ,
    C
    T
    ,
    M
    R
    ,
    u
    l
    t
    r
    a
    s
    o
    u
    n
    d
    )
    ,
    b
    u
    t
    a
    s
    t
    u
    d
    y
    m
    a
    y
    h
    a
    v
    e
    m
    u
    l
    t
    i
    p
    l
    e
    s
    e
    r
    i
    e
    s
    o
    f
    d
    i
    f
    f
    e
    r
    e
    n
    t
    m
    o
    d
    a
    l
    i
    t
    i
    e
    s
    .
    
    """
    
    resource_type = "ImagingStudy"
    
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        I
        n
        s
        t
        i
        t
        u
        t
        i
        o
        n
        -
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
        w
        i
        t
        h
        w
        h
        i
        c
        h
        t
        h
        i
        s
        i
        m
        a
        g
        i
        n
        g
        s
        t
        u
        d
        y
        i
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ 
        S
        t
        u
        d
        y
        a
        c
        c
        e
        s
        s
        e
        n
        d
        p
        o
        i
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        I
        d
        e
        n
        t
        i
        f
        i
        e
        r
        s
        f
        o
        r
        t
        h
        e
        w
        h
        o
        l
        e
        s
        t
        u
        d
        y
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpreter = None
        """ 
        W
        h
        o
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
        i
        m
        a
        g
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.location = None
        """ 
        W
        h
        e
        r
        e
        I
        m
        a
        g
        i
        n
        g
        S
        t
        u
        d
        y
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
        
        self.modality = None
        """ 
        A
        l
        l
        s
        e
        r
        i
        e
        s
        m
        o
        d
        a
        l
        i
        t
        y
        i
        f
        a
        c
        t
        u
        a
        l
        a
        c
        q
        u
        i
        s
        i
        t
        i
        o
        n
        m
        o
        d
        a
        l
        i
        t
        i
        e
        s
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.note = None
        """ 
        U
        s
        e
        r
        -
        d
        e
        f
        i
        n
        e
        d
        c
        o
        m
        m
        e
        n
        t
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.numberOfInstances = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        S
        t
        u
        d
        y
        R
        e
        l
        a
        t
        e
        d
        I
        n
        s
        t
        a
        n
        c
        e
        s
        .
        Type `int`. """
        
        self.numberOfSeries = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        S
        t
        u
        d
        y
        R
        e
        l
        a
        t
        e
        d
        S
        e
        r
        i
        e
        s
        .
        Type `int`. """
        
        self.procedureCode = None
        """ 
        T
        h
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
        p
        r
        o
        c
        e
        d
        u
        r
        e
        c
        o
        d
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.procedureReference = None
        """ 
        T
        h
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
        P
        r
        o
        c
        e
        d
        u
        r
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        t
        h
        e
        s
        t
        u
        d
        y
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        w
        a
        s
        s
        t
        u
        d
        y
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.referrer = None
        """ 
        R
        e
        f
        e
        r
        r
        i
        n
        g
        p
        h
        y
        s
        i
        c
        i
        a
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.series = None
        """ 
        E
        a
        c
        h
        s
        t
        u
        d
        y
        h
        a
        s
        o
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
        r
        i
        e
        s
        o
        f
        i
        n
        s
        t
        a
        n
        c
        e
        s
        .
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """
        
        self.started = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        s
        t
        u
        d
        y
        w
        a
        s
        s
        t
        a
        r
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        a
        v
        a
        i
        l
        a
        b
        l
        e
        |
        c
        a
        n
        c
        e
        l
        l
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
        
        self.subject = None
        """ 
        W
        h
        o
        o
        r
        w
        h
        a
        t
        i
        s
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
        o
        f
        t
        h
        e
        s
        t
        u
        d
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ImagingStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpreter", "interpreter", fhirreference.FHIRReference, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("modality", "modality", coding.Coding, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("numberOfSeries", "numberOfSeries", int, False, None, False),
            ("procedureCode", "procedureCode", codeableconcept.CodeableConcept, True, None, False),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("referrer", "referrer", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingStudySeries, True, None, False),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import backboneelement

class ImagingStudySeries(backboneelement.BackboneElement):
    """ 
    E
    a
    c
    h
    s
    t
    u
    d
    y
    h
    a
    s
    o
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
    r
    i
    e
    s
    o
    f
    i
    n
    s
    t
    a
    n
    c
    e
    s
    .
    
    
    E
    a
    c
    h
    s
    t
    u
    d
    y
    h
    a
    s
    o
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
    r
    i
    e
    s
    o
    f
    i
    m
    a
    g
    e
    s
    o
    r
    o
    t
    h
    e
    r
    c
    o
    n
    t
    e
    n
    t
    .
    
    """
    
    resource_type = "ImagingStudySeries"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
        """ 
        B
        o
        d
        y
        p
        a
        r
        t
        e
        x
        a
        m
        i
        n
        e
        d
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        A
        s
        h
        o
        r
        t
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
        s
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
        s
        e
        r
        i
        e
        s
        .
        Type `str`. """
        
        self.endpoint = None
        """ 
        S
        e
        r
        i
        e
        s
        a
        c
        c
        e
        s
        s
        e
        n
        d
        p
        o
        i
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ 
        A
        s
        i
        n
        g
        l
        e
        S
        O
        P
        i
        n
        s
        t
        a
        n
        c
        e
        f
        r
        o
        m
        t
        h
        e
        s
        e
        r
        i
        e
        s
        .
        List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.laterality = None
        """ 
        B
        o
        d
        y
        p
        a
        r
        t
        l
        a
        t
        e
        r
        a
        l
        i
        t
        y
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.modality = None
        """ 
        T
        h
        e
        m
        o
        d
        a
        l
        i
        t
        y
        o
        f
        t
        h
        e
        i
        n
        s
        t
        a
        n
        c
        e
        s
        i
        n
        t
        h
        e
        s
        e
        r
        i
        e
        s
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.number = None
        """ 
        N
        u
        m
        e
        r
        i
        c
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
        o
        f
        t
        h
        i
        s
        s
        e
        r
        i
        e
        s
        .
        Type `int`. """
        
        self.numberOfInstances = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        S
        e
        r
        i
        e
        s
        R
        e
        l
        a
        t
        e
        d
        I
        n
        s
        t
        a
        n
        c
        e
        s
        .
        Type `int`. """
        
        self.performer = None
        """ 
        W
        h
        o
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
        h
        e
        s
        e
        r
        i
        e
        s
        .
        List of `ImagingStudySeriesPerformer` items (represented as `dict` in JSON). """
        
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
        i
        m
        a
        g
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.started = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        s
        e
        r
        i
        e
        s
        s
        t
        a
        r
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.uid = None
        """ 
        D
        I
        C
        O
        M
        S
        e
        r
        i
        e
        s
        I
        n
        s
        t
        a
        n
        c
        e
        U
        I
        D
        f
        o
        r
        t
        h
        e
        s
        e
        r
        i
        e
        s
        .
        Type `str`. """
        
        super(ImagingStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False),
            ("laterality", "laterality", coding.Coding, False, None, False),
            ("modality", "modality", coding.Coding, False, None, True),
            ("number", "number", int, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("performer", "performer", ImagingStudySeriesPerformer, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ 
    A
    s
    i
    n
    g
    l
    e
    S
    O
    P
    i
    n
    s
    t
    a
    n
    c
    e
    f
    r
    o
    m
    t
    h
    e
    s
    e
    r
    i
    e
    s
    .
    
    
    A
    s
    i
    n
    g
    l
    e
    S
    O
    P
    i
    n
    s
    t
    a
    n
    c
    e
    w
    i
    t
    h
    i
    n
    t
    h
    e
    s
    e
    r
    i
    e
    s
    ,
    e
    .
    g
    .
    a
    n
    i
    m
    a
    g
    e
    ,
    o
    r
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
    s
    t
    a
    t
    e
    .
    
    """
    
    resource_type = "ImagingStudySeriesInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.number = None
        """ 
        T
        h
        e
        n
        u
        m
        b
        e
        r
        o
        f
        t
        h
        i
        s
        i
        n
        s
        t
        a
        n
        c
        e
        i
        n
        t
        h
        e
        s
        e
        r
        i
        e
        s
        .
        Type `int`. """
        
        self.sopClass = None
        """ 
        D
        I
        C
        O
        M
        c
        l
        a
        s
        s
        t
        y
        p
        e
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.title = None
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
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.uid = None
        """ 
        D
        I
        C
        O
        M
        S
        O
        P
        I
        n
        s
        t
        a
        n
        c
        e
        U
        I
        D
        .
        Type `str`. """
        
        super(ImagingStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("sopClass", "sopClass", coding.Coding, False, None, True),
            ("title", "title", str, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """ 
    W
    h
    o
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
    h
    e
    s
    e
    r
    i
    e
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
    w
    h
    o
    o
    r
    w
    h
    a
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
    h
    e
    s
    e
    r
    i
    e
    s
    a
    n
    d
    h
    o
    w
    t
    h
    e
    y
    w
    e
    r
    e
    i
    n
    v
    o
    l
    v
    e
    d
    .
    
    """
    
    resource_type = "ImagingStudySeriesPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ 
        W
        h
        o
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
        h
        e
        s
        e
        r
        i
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function = None
        """ 
        T
        y
        p
        e
        o
        f
        p
        e
        r
        f
        o
        r
        m
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImagingStudySeriesPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
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
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
