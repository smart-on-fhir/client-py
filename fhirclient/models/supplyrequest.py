#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SupplyRequest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class SupplyRequest(domainresource.DomainResource):
    """ 
    R
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
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    ,
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
    d
    e
    v
    i
    c
    e
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
    a
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    ,
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
    d
    e
    v
    i
    c
    e
    u
    s
    e
    d
    i
    n
    t
    h
    e
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
    .
    
    """
    
    resource_type = "SupplyRequest"
    
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
        m
        a
        d
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.category = None
        """ 
        T
        h
        e
        k
        i
        n
        d
        o
        f
        s
        u
        p
        p
        l
        y
        (
        c
        e
        n
        t
        r
        a
        l
        ,
        n
        o
        n
        -
        s
        t
        o
        c
        k
        ,
        e
        t
        c
        .
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.deliverFrom = None
        """ 
        T
        h
        e
        o
        r
        i
        g
        i
        n
        o
        f
        t
        h
        e
        s
        u
        p
        p
        l
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deliverTo = None
        """ 
        T
        h
        e
        d
        e
        s
        t
        i
        n
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
        s
        u
        p
        p
        l
        y
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
        S
        u
        p
        p
        l
        y
        R
        e
        q
        u
        e
        s
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.itemCodeableConcept = None
        """ 
        M
        e
        d
        i
        c
        a
        t
        i
        o
        n
        ,
        S
        u
        b
        s
        t
        a
        n
        c
        e
        ,
        o
        r
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
        t
        o
        b
        e
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ 
        M
        e
        d
        i
        c
        a
        t
        i
        o
        n
        ,
        S
        u
        b
        s
        t
        a
        n
        c
        e
        ,
        o
        r
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
        t
        o
        b
        e
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
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
        s
        h
        o
        u
        l
        d
        b
        e
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
        r
        e
        q
        u
        e
        s
        t
        s
        h
        o
        u
        l
        d
        b
        e
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
        r
        e
        q
        u
        e
        s
        t
        s
        h
        o
        u
        l
        d
        b
        e
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
        Type `Timing` (represented as `dict` in JSON). """
        
        self.parameter = None
        """ 
        O
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
        d
        e
        t
        a
        i
        l
        s
        .
        List of `SupplyRequestParameter` items (represented as `dict` in JSON). """
        
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
        
        self.quantity = None
        """ 
        T
        h
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
        a
        m
        o
        u
        n
        t
        o
        f
        t
        h
        e
        i
        t
        e
        m
        i
        n
        d
        i
        c
        a
        t
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        T
        h
        e
        r
        e
        a
        s
        o
        n
        w
        h
        y
        t
        h
        e
        s
        u
        p
        p
        l
        y
        i
        t
        e
        m
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
        T
        h
        e
        r
        e
        a
        s
        o
        n
        w
        h
        y
        t
        h
        e
        s
        u
        p
        p
        l
        y
        i
        t
        e
        m
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
        
        self.requester = None
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
        m
        a
        k
        i
        n
        g
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
        +
        .
        Type `str`. """
        
        self.supplier = None
        """ 
        W
        h
        o
        i
        s
        i
        n
        t
        e
        n
        d
        e
        d
        t
        o
        f
        u
        l
        f
        i
        l
        l
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(SupplyRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("deliverFrom", "deliverFrom", fhirreference.FHIRReference, False, None, False),
            ("deliverTo", "deliverTo", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("parameter", "parameter", SupplyRequestParameter, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class SupplyRequestParameter(backboneelement.BackboneElement):
    """ 
    O
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
    s
    i
    z
    e
    o
    f
    t
    h
    e
    i
    n
    d
    i
    c
    a
    t
    e
    d
    i
    t
    e
    m
    .
    
    """
    
    resource_type = "SupplyRequestParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        I
        t
        e
        m
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
        
        super(SupplyRequestParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequestParameter, self).elementProperties()
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
