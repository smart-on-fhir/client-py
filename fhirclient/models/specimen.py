#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Specimen) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Specimen(domainresource.DomainResource):
    """ 
    S
    a
    m
    p
    l
    e
    f
    o
    r
    a
    n
    a
    l
    y
    s
    i
    s
    .
    
    
    A
    s
    a
    m
    p
    l
    e
    t
    o
    b
    e
    u
    s
    e
    d
    f
    o
    r
    a
    n
    a
    l
    y
    s
    i
    s
    .
    
    """
    
    resource_type = "Specimen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accessionIdentifier = None
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
        a
        s
        s
        i
        g
        n
        e
        d
        b
        y
        t
        h
        e
        l
        a
        b
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.collection = None
        """ 
        C
        o
        l
        l
        e
        c
        t
        i
        o
        n
        d
        e
        t
        a
        i
        l
        s
        .
        Type `SpecimenCollection` (represented as `dict` in JSON). """
        
        self.condition = None
        """ 
        S
        t
        a
        t
        e
        o
        f
        t
        h
        e
        s
        p
        e
        c
        i
        m
        e
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.container = None
        """ 
        D
        i
        r
        e
        c
        t
        c
        o
        n
        t
        a
        i
        n
        e
        r
        o
        f
        s
        p
        e
        c
        i
        m
        e
        n
        (
        t
        u
        b
        e
        /
        s
        l
        i
        d
        e
        ,
        e
        t
        c
        .
        )
        .
        List of `SpecimenContainer` items (represented as `dict` in JSON). """
        
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
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.parent = None
        """ 
        S
        p
        e
        c
        i
        m
        e
        n
        f
        r
        o
        m
        w
        h
        i
        c
        h
        t
        h
        i
        s
        s
        p
        e
        c
        i
        m
        e
        n
        o
        r
        i
        g
        i
        n
        a
        t
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.processing = None
        """ 
        P
        r
        o
        c
        e
        s
        s
        i
        n
        g
        a
        n
        d
        p
        r
        o
        c
        e
        s
        s
        i
        n
        g
        s
        t
        e
        p
        d
        e
        t
        a
        i
        l
        s
        .
        List of `SpecimenProcessing` items (represented as `dict` in JSON). """
        
        self.receivedTime = None
        """ 
        T
        h
        e
        t
        i
        m
        e
        w
        h
        e
        n
        s
        p
        e
        c
        i
        m
        e
        n
        w
        a
        s
        r
        e
        c
        e
        i
        v
        e
        d
        f
        o
        r
        p
        r
        o
        c
        e
        s
        s
        i
        n
        g
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.request = None
        """ 
        W
        h
        y
        t
        h
        e
        s
        p
        e
        c
        i
        m
        e
        n
        w
        a
        s
        c
        o
        l
        l
        e
        c
        t
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
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
        u
        n
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
        u
        n
        s
        a
        t
        i
        s
        f
        a
        c
        t
        o
        r
        y
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
        
        self.subject = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        s
        p
        e
        c
        i
        m
        e
        n
        c
        a
        m
        e
        f
        r
        o
        m
        .
        T
        h
        i
        s
        m
        a
        y
        b
        e
        f
        r
        o
        m
        p
        a
        t
        i
        e
        n
        t
        (
        s
        )
        ,
        f
        r
        o
        m
        a
        l
        o
        c
        a
        t
        i
        o
        n
        (
        e
        .
        g
        .
        ,
        t
        h
        e
        s
        o
        u
        r
        c
        e
        o
        f
        a
        n
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
        a
        l
        s
        a
        m
        p
        l
        e
        )
        ,
        o
        r
        a
        s
        a
        m
        p
        l
        i
        n
        g
        o
        f
        a
        s
        u
        b
        s
        t
        a
        n
        c
        e
        o
        r
        a
        d
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        K
        i
        n
        d
        o
        f
        m
        a
        t
        e
        r
        i
        a
        l
        t
        h
        a
        t
        f
        o
        r
        m
        s
        t
        h
        e
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Specimen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend([
            ("accessionIdentifier", "accessionIdentifier", identifier.Identifier, False, None, False),
            ("collection", "collection", SpecimenCollection, False, None, False),
            ("condition", "condition", codeableconcept.CodeableConcept, True, None, False),
            ("container", "container", SpecimenContainer, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("processing", "processing", SpecimenProcessing, True, None, False),
            ("receivedTime", "receivedTime", fhirdate.FHIRDate, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SpecimenCollection(backboneelement.BackboneElement):
    """ 
    C
    o
    l
    l
    e
    c
    t
    i
    o
    n
    d
    e
    t
    a
    i
    l
    s
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    c
    o
    n
    c
    e
    r
    n
    i
    n
    g
    t
    h
    e
    s
    p
    e
    c
    i
    m
    e
    n
    c
    o
    l
    l
    e
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "SpecimenCollection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        c
        o
        l
        l
        e
        c
        t
        i
        o
        n
        s
        i
        t
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.collectedDateTime = None
        """ 
        C
        o
        l
        l
        e
        c
        t
        i
        o
        n
        t
        i
        m
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.collectedPeriod = None
        """ 
        C
        o
        l
        l
        e
        c
        t
        i
        o
        n
        t
        i
        m
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.collector = None
        """ 
        W
        h
        o
        c
        o
        l
        l
        e
        c
        t
        e
        d
        t
        h
        e
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.duration = None
        """ 
        H
        o
        w
        l
        o
        n
        g
        i
        t
        t
        o
        o
        k
        t
        o
        c
        o
        l
        l
        e
        c
        t
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.fastingStatusCodeableConcept = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        o
        r
        h
        o
        w
        l
        o
        n
        g
        p
        a
        t
        i
        e
        n
        t
        a
        b
        s
        t
        a
        i
        n
        e
        d
        f
        r
        o
        m
        f
        o
        o
        d
        a
        n
        d
        /
        o
        r
        d
        r
        i
        n
        k
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fastingStatusDuration = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        o
        r
        h
        o
        w
        l
        o
        n
        g
        p
        a
        t
        i
        e
        n
        t
        a
        b
        s
        t
        a
        i
        n
        e
        d
        f
        r
        o
        m
        f
        o
        o
        d
        a
        n
        d
        /
        o
        r
        d
        r
        i
        n
        k
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.method = None
        """ 
        T
        e
        c
        h
        n
        i
        q
        u
        e
        u
        s
        e
        d
        t
        o
        p
        e
        r
        f
        o
        r
        m
        c
        o
        l
        l
        e
        c
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        T
        h
        e
        q
        u
        a
        n
        t
        i
        t
        y
        o
        f
        s
        p
        e
        c
        i
        m
        e
        n
        c
        o
        l
        l
        e
        c
        t
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SpecimenCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("collectedDateTime", "collectedDateTime", fhirdate.FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("duration", "duration", duration.Duration, False, None, False),
            ("fastingStatusCodeableConcept", "fastingStatusCodeableConcept", codeableconcept.CodeableConcept, False, "fastingStatus", False),
            ("fastingStatusDuration", "fastingStatusDuration", duration.Duration, False, "fastingStatus", False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js


class SpecimenContainer(backboneelement.BackboneElement):
    """ 
    D
    i
    r
    e
    c
    t
    c
    o
    n
    t
    a
    i
    n
    e
    r
    o
    f
    s
    p
    e
    c
    i
    m
    e
    n
    (
    t
    u
    b
    e
    /
    s
    l
    i
    d
    e
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
    c
    o
    n
    t
    a
    i
    n
    e
    r
    h
    o
    l
    d
    i
    n
    g
    t
    h
    e
    s
    p
    e
    c
    i
    m
    e
    n
    .
    T
    h
    e
    r
    e
    c
    u
    r
    s
    i
    v
    e
    n
    a
    t
    u
    r
    e
    o
    f
    c
    o
    n
    t
    a
    i
    n
    e
    r
    s
    ;
    i
    .
    e
    .
    b
    l
    o
    o
    d
    i
    n
    t
    u
    b
    e
    i
    n
    t
    r
    a
    y
    i
    n
    r
    a
    c
    k
    i
    s
    n
    o
    t
    a
    d
    d
    r
    e
    s
    s
    e
    d
    h
    e
    r
    e
    .
    
    """
    
    resource_type = "SpecimenContainer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept = None
        """ 
        A
        d
        d
        i
        t
        i
        v
        e
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
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.additiveReference = None
        """ 
        A
        d
        d
        i
        t
        i
        v
        e
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
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.capacity = None
        """ 
        C
        o
        n
        t
        a
        i
        n
        e
        r
        v
        o
        l
        u
        m
        e
        o
        r
        s
        i
        z
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        e
        x
        t
        u
        a
        l
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
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `str`. """
        
        self.identifier = None
        """ 
        I
        d
        f
        o
        r
        t
        h
        e
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.specimenQuantity = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        y
        o
        f
        s
        p
        e
        c
        i
        m
        e
        n
        w
        i
        t
        h
        i
        n
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        K
        i
        n
        d
        o
        f
        c
        o
        n
        t
        a
        i
        n
        e
        r
        d
        i
        r
        e
        c
        t
        l
        y
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
        s
        p
        e
        c
        i
        m
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SpecimenContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", False),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("specimenQuantity", "specimenQuantity", quantity.Quantity, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SpecimenProcessing(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    c
    e
    s
    s
    i
    n
    g
    a
    n
    d
    p
    r
    o
    c
    e
    s
    s
    i
    n
    g
    s
    t
    e
    p
    d
    e
    t
    a
    i
    l
    s
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    c
    o
    n
    c
    e
    r
    n
    i
    n
    g
    p
    r
    o
    c
    e
    s
    s
    i
    n
    g
    a
    n
    d
    p
    r
    o
    c
    e
    s
    s
    i
    n
    g
    s
    t
    e
    p
    s
    f
    o
    r
    t
    h
    e
    s
    p
    e
    c
    i
    m
    e
    n
    .
    
    """
    
    resource_type = "SpecimenProcessing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        """ 
        M
        a
        t
        e
        r
        i
        a
        l
        u
        s
        e
        d
        i
        n
        t
        h
        e
        p
        r
        o
        c
        e
        s
        s
        i
        n
        g
        s
        t
        e
        p
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        e
        x
        t
        u
        a
        l
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
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `str`. """
        
        self.procedure = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
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
        t
        e
        p
        a
        p
        p
        l
        i
        e
        d
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
        m
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timeDateTime = None
        """ 
        D
        a
        t
        e
        a
        n
        d
        t
        i
        m
        e
        o
        f
        s
        p
        e
        c
        i
        m
        e
        n
        p
        r
        o
        c
        e
        s
        s
        i
        n
        g
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timePeriod = None
        """ 
        D
        a
        t
        e
        a
        n
        d
        t
        i
        m
        e
        o
        f
        s
        p
        e
        c
        i
        m
        e
        n
        p
        r
        o
        c
        e
        s
        s
        i
        n
        g
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(SpecimenProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, True, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
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
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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
