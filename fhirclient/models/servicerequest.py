#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ServiceRequest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ServiceRequest(domainresource.DomainResource):
    """ 
    A
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
    s
    e
    r
    v
    i
    c
    e
    t
    o
    b
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
    s
    e
    r
    v
    i
    c
    e
    s
    u
    c
    h
    a
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
    s
    ,
    o
    r
    o
    p
    e
    r
    a
    t
    i
    o
    n
    s
    t
    o
    b
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
    .
    
    """
    
    resource_type = "ServiceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asNeededBoolean = None
        """ 
        P
        r
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
        s
        f
        o
        r
        s
        e
        r
        v
        i
        c
        e
        .
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ 
        P
        r
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
        s
        f
        o
        r
        s
        e
        r
        v
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ 
        D
        a
        t
        e
        r
        e
        q
        u
        e
        s
        t
        s
        i
        g
        n
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
        
        self.bodySite = None
        """ 
        L
        o
        c
        a
        t
        i
        o
        n
        o
        n
        B
        o
        d
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        s
        e
        r
        v
        i
        c
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        W
        h
        a
        t
        i
        s
        b
        e
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
        e
        d
        /
        o
        r
        d
        e
        r
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doNotPerform = None
        """ 
        T
        r
        u
        e
        i
        f
        s
        e
        r
        v
        i
        c
        e
        /
        p
        r
        o
        c
        e
        d
        u
        r
        e
        s
        h
        o
        u
        l
        d
        n
        o
        t
        b
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
        .
        Type `bool`. """
        
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
        i
        n
        w
        h
        i
        c
        h
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        w
        a
        s
        c
        r
        e
        a
        t
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        a
        s
        s
        i
        g
        n
        e
        d
        t
        o
        t
        h
        i
        s
        o
        r
        d
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
        d
        e
        r
        +
        .
        Type `str`. """
        
        self.locationCode = None
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
        l
        o
        c
        a
        t
        i
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.locationReference = None
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
        l
        o
        c
        a
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
        s
        e
        r
        v
        i
        c
        e
        s
        h
        o
        u
        l
        d
        o
        c
        c
        u
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ 
        W
        h
        e
        n
        s
        e
        r
        v
        i
        c
        e
        s
        h
        o
        u
        l
        d
        o
        c
        c
        u
        r
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ 
        W
        h
        e
        n
        s
        e
        r
        v
        i
        c
        e
        s
        h
        o
        u
        l
        d
        o
        c
        c
        u
        r
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.orderDetail = None
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
        o
        r
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.patientInstruction = None
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
        c
        o
        n
        s
        u
        m
        e
        r
        -
        o
        r
        i
        e
        n
        t
        e
        d
        i
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
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
        p
        e
        r
        f
        o
        r
        m
        e
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performerType = None
        """ 
        P
        e
        r
        f
        o
        r
        m
        e
        r
        r
        o
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priority = None
        """ 
        r
        o
        u
        t
        i
        n
        e
        |
        u
        r
        g
        e
        n
        t
        |
        a
        s
        a
        p
        |
        s
        t
        a
        t
        .
        Type `str`. """
        
        self.quantityQuantity = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        a
        m
        o
        u
        n
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.quantityRange = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        a
        m
        o
        u
        n
        t
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.quantityRatio = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        a
        m
        o
        u
        n
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.reasonCode = None
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
        /
        J
        u
        s
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
        f
        o
        r
        p
        r
        o
        c
        e
        d
        u
        r
        e
        o
        r
        s
        e
        r
        v
        i
        c
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
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
        /
        J
        u
        s
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
        f
        o
        r
        s
        e
        r
        v
        i
        c
        e
        o
        r
        s
        e
        r
        v
        i
        c
        e
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
        
        self.replaces = None
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
        s
        e
        r
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requisition = None
        """ 
        C
        o
        m
        p
        o
        s
        i
        t
        e
        R
        e
        q
        u
        e
        s
        t
        I
        D
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ 
        P
        r
        o
        c
        e
        d
        u
        r
        e
        S
        a
        m
        p
        l
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        I
        n
        d
        i
        v
        i
        d
        u
        a
        l
        o
        r
        E
        n
        t
        i
        t
        y
        t
        h
        e
        s
        e
        r
        v
        i
        c
        e
        i
        s
        o
        r
        d
        e
        r
        e
        d
        f
        o
        r
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
        
        super(ServiceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("locationCode", "locationCode", codeableconcept.CodeableConcept, True, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("orderDetail", "orderDetail", codeableconcept.CodeableConcept, True, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, False, "quantity", False),
            ("quantityRange", "quantityRange", range.Range, False, "quantity", False),
            ("quantityRatio", "quantityRatio", ratio.Ratio, False, "quantity", False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
