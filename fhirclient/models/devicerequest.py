#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceRequest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DeviceRequest(domainresource.DomainResource):
    """ 
    M
    e
    d
    i
    c
    a
    l
    d
    e
    v
    i
    c
    e
    r
    e
    q
    u
    e
    s
    t
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
    s
    a
    r
    e
    q
    u
    e
    s
    t
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
    t
    o
    e
    m
    p
    l
    o
    y
    a
    m
    e
    d
    i
    c
    a
    l
    d
    e
    v
    i
    c
    e
    .
    T
    h
    e
    d
    e
    v
    i
    c
    e
    m
    a
    y
    b
    e
    a
    n
    i
    m
    p
    l
    a
    n
    t
    a
    b
    l
    e
    d
    e
    v
    i
    c
    e
    ,
    o
    r
    a
    n
    e
    x
    t
    e
    r
    n
    a
    l
    a
    s
    s
    i
    s
    t
    i
    v
    e
    d
    e
    v
    i
    c
    e
    ,
    s
    u
    c
    h
    a
    s
    a
    w
    a
    l
    k
    e
    r
    .
    
    """
    
    resource_type = "DeviceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ 
        W
        h
        e
        n
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
        
        self.basedOn = None
        """ 
        W
        h
        a
        t
        r
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
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.codeCodeableConcept = None
        """ 
        D
        e
        v
        i
        c
        e
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.codeReference = None
        """ 
        D
        e
        v
        i
        c
        e
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        m
        o
        t
        i
        v
        a
        t
        i
        n
        g
        r
        e
        q
        u
        e
        s
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
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
        o
        f
        c
        o
        m
        p
        o
        s
        i
        t
        e
        r
        e
        q
        u
        e
        s
        t
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
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
        R
        e
        q
        u
        e
        s
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
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        F
        H
        I
        R
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        List of `str` items. """
        
        self.instantiatesUri = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        e
        x
        t
        e
        r
        n
        a
        l
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        List of `str` items. """
        
        self.insurance = None
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
        i
        n
        s
        u
        r
        a
        n
        c
        e
        c
        o
        v
        e
        r
        a
        g
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent = None
        """ 
        p
        r
        o
        p
        o
        s
        a
        l
        |
        p
        l
        a
        n
        |
        o
        r
        i
        g
        i
        n
        a
        l
        -
        o
        r
        d
        e
        r
        |
        e
        n
        c
        o
        d
        e
        d
        |
        r
        e
        f
        l
        e
        x
        -
        o
        r
        d
        e
        r
        .
        Type `str`. """
        
        self.note = None
        """ 
        N
        o
        t
        e
        s
        o
        r
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
        
        self.occurrenceDateTime = None
        """ 
        D
        e
        s
        i
        r
        e
        d
        t
        i
        m
        e
        o
        r
        s
        c
        h
        e
        d
        u
        l
        e
        f
        o
        r
        u
        s
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ 
        D
        e
        s
        i
        r
        e
        d
        t
        i
        m
        e
        o
        r
        s
        c
        h
        e
        d
        u
        l
        e
        f
        o
        r
        u
        s
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ 
        D
        e
        s
        i
        r
        e
        d
        t
        i
        m
        e
        o
        r
        s
        c
        h
        e
        d
        u
        l
        e
        f
        o
        r
        u
        s
        e
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.parameter = None
        """ 
        D
        e
        v
        i
        c
        e
        d
        e
        t
        a
        i
        l
        s
        .
        List of `DeviceRequestParameter` items (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        e
        d
        F
        i
        l
        l
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ 
        F
        i
        l
        l
        e
        r
        r
        o
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priorRequest = None
        """ 
        W
        h
        a
        t
        r
        e
        q
        u
        e
        s
        t
        r
        e
        p
        l
        a
        c
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.priority = None
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
        h
        o
        w
        q
        u
        i
        c
        k
        l
        y
        t
        h
        e
        {
        {
        t
        i
        t
        l
        e
        }
        }
        s
        h
        o
        u
        l
        d
        b
        e
        a
        d
        d
        r
        e
        s
        s
        e
        d
        w
        i
        t
        h
        r
        e
        s
        p
        e
        c
        t
        t
        o
        o
        t
        h
        e
        r
        r
        e
        q
        u
        e
        s
        t
        s
        .
        Type `str`. """
        
        self.reasonCode = None
        """ 
        C
        o
        d
        e
        d
        R
        e
        a
        s
        o
        n
        f
        o
        r
        r
        e
        q
        u
        e
        s
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        L
        i
        n
        k
        e
        d
        R
        e
        a
        s
        o
        n
        f
        o
        r
        r
        e
        q
        u
        e
        s
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        p
        r
        o
        v
        e
        n
        a
        n
        c
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        """ 
        W
        h
        o
        /
        w
        h
        a
        t
        i
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
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        s
        u
        s
        p
        e
        n
        d
        e
        d
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
        .
        Type `str`. """
        
        self.subject = None
        """ 
        F
        o
        c
        u
        s
        o
        f
        r
        e
        q
        u
        e
        s
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInfo = None
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
        c
        l
        i
        n
        i
        c
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("codeCodeableConcept", "codeCodeableConcept", codeableconcept.CodeableConcept, False, "code", True),
            ("codeReference", "codeReference", fhirreference.FHIRReference, False, "code", True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("parameter", "parameter", DeviceRequestParameter, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priorRequest", "priorRequest", fhirreference.FHIRReference, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceRequestParameter(backboneelement.BackboneElement):
    """ 
    D
    e
    v
    i
    c
    e
    d
    e
    t
    a
    i
    l
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
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    f
    o
    r
    t
    h
    e
    o
    r
    d
    e
    r
    e
    d
    i
    t
    e
    m
    .
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    ,
    t
    h
    e
    p
    r
    i
    s
    m
    v
    a
    l
    u
    e
    f
    o
    r
    l
    e
    n
    s
    e
    s
    .
    
    """
    
    resource_type = "DeviceRequestParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        D
        e
        v
        i
        c
        e
        d
        e
        t
        a
        i
        l
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        d
        e
        t
        a
        i
        l
        .
        Type `bool`. """
        
        self.valueCodeableConcept = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        d
        e
        t
        a
        i
        l
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        d
        e
        t
        a
        i
        l
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        d
        e
        t
        a
        i
        l
        .
        Type `Range` (represented as `dict` in JSON). """
        
        super(DeviceRequestParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
