#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Observation) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Observation(domainresource.DomainResource):
    """ 
    M
    e
    a
    s
    u
    r
    e
    m
    e
    n
    t
    s
    a
    n
    d
    s
    i
    m
    p
    l
    e
    a
    s
    s
    e
    r
    t
    i
    o
    n
    s
    .
    
    
    M
    e
    a
    s
    u
    r
    e
    m
    e
    n
    t
    s
    a
    n
    d
    s
    i
    m
    p
    l
    e
    a
    s
    s
    e
    r
    t
    i
    o
    n
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
    a
    p
    a
    t
    i
    e
    n
    t
    ,
    d
    e
    v
    i
    c
    e
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
    .
    
    """
    
    resource_type = "Observation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ 
        F
        u
        l
        f
        i
        l
        l
        s
        p
        l
        a
        n
        ,
        p
        r
        o
        p
        o
        s
        a
        l
        o
        r
        o
        r
        d
        e
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ 
        O
        b
        s
        e
        r
        v
        e
        d
        b
        o
        d
        y
        p
        a
        r
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        C
        l
        a
        s
        s
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
        y
        p
        e
        o
        f
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
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
        (
        c
        o
        d
        e
        /
        t
        y
        p
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.component = None
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
        r
        e
        s
        u
        l
        t
        s
        .
        List of `ObservationComponent` items (represented as `dict` in JSON). """
        
        self.dataAbsentReason = None
        """ 
        W
        h
        y
        t
        h
        e
        r
        e
        s
        u
        l
        t
        i
        s
        m
        i
        s
        s
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.derivedFrom = None
        """ 
        R
        e
        l
        a
        t
        e
        d
        m
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        s
        t
        h
        e
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
        i
        s
        m
        a
        d
        e
        f
        r
        o
        m
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.device = None
        """ 
        (
        M
        e
        a
        s
        u
        r
        e
        m
        e
        n
        t
        )
        D
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectiveInstant = None
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
        Type `Period` (represented as `dict` in JSON). """
        
        self.effectiveTiming = None
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
        Type `Timing` (represented as `dict` in JSON). """
        
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
        d
        u
        r
        i
        n
        g
        w
        h
        i
        c
        h
        t
        h
        i
        s
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
        i
        s
        m
        a
        d
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focus = None
        """ 
        W
        h
        a
        t
        t
        h
        e
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
        i
        s
        a
        b
        o
        u
        t
        ,
        w
        h
        e
        n
        i
        t
        i
        s
        n
        o
        t
        a
        b
        o
        u
        t
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
        r
        e
        c
        o
        r
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.hasMember = None
        """ 
        R
        e
        l
        a
        t
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
        t
        h
        a
        t
        b
        e
        l
        o
        n
        g
        s
        t
        o
        t
        h
        e
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
        g
        r
        o
        u
        p
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        f
        o
        r
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
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpretation = None
        """ 
        H
        i
        g
        h
        ,
        l
        o
        w
        ,
        n
        o
        r
        m
        a
        l
        ,
        e
        t
        c
        .
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.issued = None
        """ 
        D
        a
        t
        e
        /
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
        a
        v
        a
        i
        l
        a
        b
        l
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.method = None
        """ 
        H
        o
        w
        i
        t
        w
        a
        s
        d
        o
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        a
        b
        o
        u
        t
        t
        h
        e
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
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ 
        P
        a
        r
        t
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
        d
        e
        v
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        W
        h
        o
        i
        s
        r
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
        f
        o
        r
        t
        h
        e
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.referenceRange = None
        """ 
        P
        r
        o
        v
        i
        d
        e
        s
        g
        u
        i
        d
        e
        f
        o
        r
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
        .
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        
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
        u
        s
        e
        d
        f
        o
        r
        t
        h
        i
        s
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        a
        n
        d
        /
        o
        r
        w
        h
        a
        t
        t
        h
        e
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
        i
        s
        a
        b
        o
        u
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `bool`. """
        
        self.valueCodeableConcept = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `int`. """
        
        self.valuePeriod = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `str`. """
        
        self.valueTime = None
        """ 
        A
        c
        t
        u
        a
        l
        r
        e
        s
        u
        l
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Observation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Observation, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("component", "component", ObservationComponent, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectiveInstant", "effectiveInstant", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("effectiveTiming", "effectiveTiming", timing.Timing, False, "effective", False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("hasMember", "hasMember", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
        ])
        return js


from . import backboneelement

class ObservationComponent(backboneelement.BackboneElement):
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
    r
    e
    s
    u
    l
    t
    s
    .
    
    
    S
    o
    m
    e
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
    s
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
    T
    h
    e
    s
    e
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
    a
    r
    e
    e
    x
    p
    r
    e
    s
    s
    e
    d
    a
    s
    s
    e
    p
    a
    r
    a
    t
    e
    c
    o
    d
    e
    v
    a
    l
    u
    e
    p
    a
    i
    r
    s
    t
    h
    a
    t
    s
    h
    a
    r
    e
    t
    h
    e
    s
    a
    m
    e
    a
    t
    t
    r
    i
    b
    u
    t
    e
    s
    .
    E
    x
    a
    m
    p
    l
    e
    s
    i
    n
    c
    l
    u
    d
    e
    s
    y
    s
    t
    o
    l
    i
    c
    a
    n
    d
    d
    i
    a
    s
    t
    o
    l
    i
    c
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
    f
    o
    r
    b
    l
    o
    o
    d
    p
    r
    e
    s
    s
    u
    r
    e
    m
    e
    a
    s
    u
    r
    e
    m
    e
    n
    t
    a
    n
    d
    m
    u
    l
    t
    i
    p
    l
    e
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
    f
    o
    r
    g
    e
    n
    e
    t
    i
    c
    s
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
    s
    .
    
    """
    
    resource_type = "ObservationComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
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
        (
        c
        o
        d
        e
        /
        t
        y
        p
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dataAbsentReason = None
        """ 
        W
        h
        y
        t
        h
        e
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        i
        s
        m
        i
        s
        s
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.interpretation = None
        """ 
        H
        i
        g
        h
        ,
        l
        o
        w
        ,
        n
        o
        r
        m
        a
        l
        ,
        e
        t
        c
        .
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.referenceRange = None
        """ 
        P
        r
        o
        v
        i
        d
        e
        s
        g
        u
        i
        d
        e
        f
        o
        r
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
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        List of `ObservationReferenceRange` items (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `bool`. """
        
        self.valueCodeableConcept = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueDateTime = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `int`. """
        
        self.valuePeriod = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `str`. """
        
        self.valueTime = None
        """ 
        A
        c
        t
        u
        a
        l
        c
        o
        m
        p
        o
        n
        e
        n
        t
        r
        e
        s
        u
        l
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ObservationComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("interpretation", "interpretation", codeableconcept.CodeableConcept, True, None, False),
            ("referenceRange", "referenceRange", ObservationReferenceRange, True, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
        ])
        return js


class ObservationReferenceRange(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    v
    i
    d
    e
    s
    g
    u
    i
    d
    e
    f
    o
    r
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
    .
    
    
    G
    u
    i
    d
    a
    n
    c
    e
    o
    n
    h
    o
    w
    t
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
    t
    h
    e
    v
    a
    l
    u
    e
    b
    y
    c
    o
    m
    p
    a
    r
    i
    s
    o
    n
    t
    o
    a
    n
    o
    r
    m
    a
    l
    o
    r
    r
    e
    c
    o
    m
    m
    e
    n
    d
    e
    d
    r
    a
    n
    g
    e
    .
    M
    u
    l
    t
    i
    p
    l
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
    r
    a
    n
    g
    e
    s
    a
    r
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
    a
    s
    a
    n
    "
    O
    R
    "
    .
    I
    n
    o
    t
    h
    e
    r
    w
    o
    r
    d
    s
    ,
    t
    o
    r
    e
    p
    r
    e
    s
    e
    n
    t
    t
    w
    o
    d
    i
    s
    t
    i
    n
    c
    t
    t
    a
    r
    g
    e
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
    s
    ,
    t
    w
    o
    `
    r
    e
    f
    e
    r
    e
    n
    c
    e
    R
    a
    n
    g
    e
    `
    e
    l
    e
    m
    e
    n
    t
    s
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
    .
    
    """
    
    resource_type = "ObservationReferenceRange"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.age = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
        e
        a
        g
        e
        r
        a
        n
        g
        e
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
        Type `Range` (represented as `dict` in JSON). """
        
        self.appliesTo = None
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
        r
        a
        n
        g
        e
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.high = None
        """ 
        H
        i
        g
        h
        R
        a
        n
        g
        e
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
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.low = None
        """ 
        L
        o
        w
        R
        a
        n
        g
        e
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
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        T
        e
        x
        t
        b
        a
        s
        e
        d
        r
        e
        f
        e
        r
        e
        n
        c
        e
        r
        a
        n
        g
        e
        i
        n
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
        .
        Type `str`. """
        
        self.type = None
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
        r
        a
        n
        g
        e
        q
        u
        a
        l
        i
        f
        i
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ObservationReferenceRange, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationReferenceRange, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("high", "high", quantity.Quantity, False, None, False),
            ("low", "low", quantity.Quantity, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
