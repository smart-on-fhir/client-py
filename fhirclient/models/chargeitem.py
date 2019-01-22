#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ChargeItem) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ChargeItem(domainresource.DomainResource):
    """ 
    I
    t
    e
    m
    c
    o
    n
    t
    a
    i
    n
    i
    n
    g
    c
    h
    a
    r
    g
    e
    c
    o
    d
    e
    (
    s
    )
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
    p
    r
    o
    v
    i
    s
    i
    o
    n
    o
    f
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
    p
    r
    o
    v
    i
    d
    e
    r
    p
    r
    o
    d
    u
    c
    t
    s
    .
    
    
    T
    h
    e
    r
    e
    s
    o
    u
    r
    c
    e
    C
    h
    a
    r
    g
    e
    I
    t
    e
    m
    d
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
    p
    r
    o
    v
    i
    s
    i
    o
    n
    o
    f
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
    p
    r
    o
    v
    i
    d
    e
    r
    p
    r
    o
    d
    u
    c
    t
    s
    f
    o
    r
    a
    c
    e
    r
    t
    a
    i
    n
    p
    a
    t
    i
    e
    n
    t
    ,
    t
    h
    e
    r
    e
    f
    o
    r
    e
    r
    e
    f
    e
    r
    r
    i
    n
    g
    n
    o
    t
    o
    n
    l
    y
    t
    o
    t
    h
    e
    p
    r
    o
    d
    u
    c
    t
    ,
    b
    u
    t
    c
    o
    n
    t
    a
    i
    n
    i
    n
    g
    i
    n
    a
    d
    d
    i
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
    o
    f
    t
    h
    e
    p
    r
    o
    v
    i
    s
    i
    o
    n
    ,
    l
    i
    k
    e
    d
    a
    t
    e
    ,
    t
    i
    m
    e
    ,
    a
    m
    o
    u
    n
    t
    s
    a
    n
    d
    p
    a
    r
    t
    i
    c
    i
    p
    a
    t
    i
    n
    g
    o
    r
    g
    a
    n
    i
    z
    a
    t
    i
    o
    n
    s
    a
    n
    d
    p
    e
    r
    s
    o
    n
    s
    .
    M
    a
    i
    n
    U
    s
    a
    g
    e
    o
    f
    t
    h
    e
    C
    h
    a
    r
    g
    e
    I
    t
    e
    m
    i
    s
    t
    o
    e
    n
    a
    b
    l
    e
    t
    h
    e
    b
    i
    l
    l
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
    a
    n
    d
    i
    n
    t
    e
    r
    n
    a
    l
    c
    o
    s
    t
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
    .
    
    """
    
    resource_type = "ChargeItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.account = None
        """ 
        A
        c
        c
        o
        u
        n
        t
        t
        o
        p
        l
        a
        c
        e
        t
        h
        i
        s
        c
        h
        a
        r
        g
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodysite = None
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
        
        self.code = None
        """ 
        A
        c
        o
        d
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
        s
        t
        h
        e
        c
        h
        a
        r
        g
        e
        ,
        l
        i
        k
        e
        a
        b
        i
        l
        l
        i
        n
        g
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
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
        /
        E
        p
        i
        s
        o
        d
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
        e
        v
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.costCenter = None
        """ 
        O
        r
        g
        a
        n
        i
        z
        a
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
        o
        w
        n
        e
        r
        s
        h
        i
        p
        o
        f
        t
        h
        e
        (
        p
        o
        t
        e
        n
        t
        i
        a
        l
        ,
        f
        u
        t
        u
        r
        e
        )
        r
        e
        v
        e
        n
        u
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definitionCanonical = None
        """ 
        R
        e
        s
        o
        u
        r
        c
        e
        d
        e
        f
        i
        n
        i
        n
        g
        t
        h
        e
        c
        o
        d
        e
        o
        f
        t
        h
        i
        s
        C
        h
        a
        r
        g
        e
        I
        t
        e
        m
        .
        List of `str` items. """
        
        self.definitionUri = None
        """ 
        D
        e
        f
        i
        n
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
        a
        b
        o
        u
        t
        t
        h
        e
        c
        o
        d
        e
        o
        f
        t
        h
        i
        s
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
        .
        List of `str` items. """
        
        self.enteredDate = None
        """ 
        D
        a
        t
        e
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
        w
        a
        s
        e
        n
        t
        e
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.enterer = None
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
        w
        h
        o
        w
        a
        s
        e
        n
        t
        e
        r
        i
        n
        g
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.factorOverride = None
        """ 
        F
        a
        c
        t
        o
        r
        o
        v
        e
        r
        r
        i
        d
        i
        n
        g
        t
        h
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
        r
        u
        l
        e
        s
        .
        Type `float`. """
        
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
        i
        t
        e
        m
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
        h
        a
        r
        g
        e
        I
        t
        e
        m
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        c
        h
        a
        r
        g
        e
        d
        s
        e
        r
        v
        i
        c
        e
        w
        a
        s
        a
        p
        p
        l
        i
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        c
        h
        a
        r
        g
        e
        d
        s
        e
        r
        v
        i
        c
        e
        w
        a
        s
        a
        p
        p
        l
        i
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        c
        h
        a
        r
        g
        e
        d
        s
        e
        r
        v
        i
        c
        e
        w
        a
        s
        a
        p
        p
        l
        i
        e
        d
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.overrideReason = None
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
        o
        v
        e
        r
        r
        i
        d
        i
        n
        g
        t
        h
        e
        l
        i
        s
        t
        p
        r
        i
        c
        e
        /
        f
        a
        c
        t
        o
        r
        .
        Type `str`. """
        
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
        C
        h
        a
        r
        g
        e
        I
        t
        e
        m
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        c
        h
        a
        r
        g
        e
        d
        s
        e
        r
        v
        i
        c
        e
        .
        List of `ChargeItemPerformer` items (represented as `dict` in JSON). """
        
        self.performingOrganization = None
        """ 
        O
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        p
        r
        o
        v
        i
        d
        i
        n
        g
        t
        h
        e
        c
        h
        a
        r
        g
        e
        d
        s
        e
        r
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priceOverride = None
        """ 
        P
        r
        i
        c
        e
        o
        v
        e
        r
        r
        i
        d
        i
        n
        g
        t
        h
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
        r
        u
        l
        e
        s
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.productCodeableConcept = None
        """ 
        P
        r
        o
        d
        u
        c
        t
        c
        h
        a
        r
        g
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productReference = None
        """ 
        P
        r
        o
        d
        u
        c
        t
        c
        h
        a
        r
        g
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
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
        w
        h
        i
        c
        h
        t
        h
        e
        c
        h
        a
        r
        g
        e
        i
        t
        e
        m
        h
        a
        s
        b
        e
        e
        n
        s
        e
        r
        v
        i
        c
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.reason = None
        """ 
        W
        h
        y
        w
        a
        s
        t
        h
        e
        c
        h
        a
        r
        g
        e
        d
        s
        e
        r
        v
        i
        c
        e
        r
        e
        n
        d
        e
        r
        e
        d
        ?
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requestingOrganization = None
        """ 
        O
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
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
        t
        h
        e
        c
        h
        a
        r
        g
        e
        d
        s
        e
        r
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.service = None
        """ 
        W
        h
        i
        c
        h
        r
        e
        n
        d
        e
        r
        e
        d
        s
        e
        r
        v
        i
        c
        e
        i
        s
        b
        e
        i
        n
        g
        c
        h
        a
        r
        g
        e
        d
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        p
        l
        a
        n
        n
        e
        d
        |
        b
        i
        l
        l
        a
        b
        l
        e
        |
        n
        o
        t
        -
        b
        i
        l
        l
        a
        b
        l
        e
        |
        a
        b
        o
        r
        t
        e
        d
        |
        b
        i
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
        s
        e
        r
        v
        i
        c
        e
        w
        a
        s
        d
        o
        n
        e
        f
        o
        r
        /
        t
        o
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ 
        F
        u
        r
        t
        h
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
        i
        s
        c
        h
        a
        r
        g
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ChargeItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItem, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, True, None, False),
            ("bodysite", "bodysite", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("costCenter", "costCenter", fhirreference.FHIRReference, False, None, False),
            ("definitionCanonical", "definitionCanonical", str, True, None, False),
            ("definitionUri", "definitionUri", str, True, None, False),
            ("enteredDate", "enteredDate", fhirdate.FHIRDate, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("factorOverride", "factorOverride", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("overrideReason", "overrideReason", str, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", ChargeItemPerformer, True, None, False),
            ("performingOrganization", "performingOrganization", fhirreference.FHIRReference, False, None, False),
            ("priceOverride", "priceOverride", money.Money, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("requestingOrganization", "requestingOrganization", fhirreference.FHIRReference, False, None, False),
            ("service", "service", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class ChargeItemPerformer(backboneelement.BackboneElement):
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
    c
    h
    a
    r
    g
    e
    d
    s
    e
    r
    v
    i
    c
    e
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
    o
    r
    p
    a
    r
    t
    i
    c
    i
    p
    a
    t
    e
    d
    i
    n
    t
    h
    e
    c
    h
    a
    r
    g
    e
    d
    s
    e
    r
    v
    i
    c
    e
    .
    
    """
    
    resource_type = "ChargeItemPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
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
        w
        h
        o
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
        i
        n
        g
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function = None
        """ 
        W
        h
        a
        t
        t
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
        w
        a
        s
        d
        o
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ChargeItemPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemPerformer, self).elementProperties()
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
