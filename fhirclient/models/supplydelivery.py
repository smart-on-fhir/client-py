#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class SupplyDelivery(domainresource.DomainResource):
    """ 
    D
    e
    l
    i
    v
    e
    r
    y
    o
    f
    b
    u
    l
    k
    S
    u
    p
    p
    l
    i
    e
    s
    .
    
    
    R
    e
    c
    o
    r
    d
    o
    f
    d
    e
    l
    i
    v
    e
    r
    y
    o
    f
    w
    h
    a
    t
    i
    s
    s
    u
    p
    p
    l
    i
    e
    d
    .
    
    """
    
    resource_type = "SupplyDelivery"
    
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
        
        self.destination = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        S
        u
        p
        p
        l
        y
        w
        a
        s
        s
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
        e
        v
        e
        n
        t
        o
        c
        c
        u
        r
        r
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
        e
        v
        e
        n
        t
        o
        c
        c
        u
        r
        r
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
        e
        v
        e
        n
        t
        o
        c
        c
        u
        r
        r
        e
        d
        .
        Type `Timing` (represented as `dict` in JSON). """
        
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
        
        self.patient = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        f
        o
        r
        w
        h
        o
        m
        t
        h
        e
        i
        t
        e
        m
        i
        s
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
        
        self.receiver = None
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
        S
        u
        p
        p
        l
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        i
        n
        -
        p
        r
        o
        g
        r
        e
        s
        s
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
        a
        b
        a
        n
        d
        o
        n
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
        
        self.suppliedItem = None
        """ 
        T
        h
        e
        i
        t
        e
        m
        t
        h
        a
        t
        i
        s
        d
        e
        l
        i
        v
        e
        r
        e
        d
        o
        r
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `SupplyDeliverySuppliedItem` (represented as `dict` in JSON). """
        
        self.supplier = None
        """ 
        D
        i
        s
        p
        e
        n
        s
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        a
        t
        e
        g
        o
        r
        y
        o
        f
        d
        i
        s
        p
        e
        n
        s
        e
        e
        v
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SupplyDelivery, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyDelivery, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("suppliedItem", "suppliedItem", SupplyDeliverySuppliedItem, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SupplyDeliverySuppliedItem(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    i
    t
    e
    m
    t
    h
    a
    t
    i
    s
    d
    e
    l
    i
    v
    e
    r
    e
    d
    o
    r
    s
    u
    p
    p
    l
    i
    e
    d
    .
    
    
    T
    h
    e
    i
    t
    e
    m
    t
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
    d
    e
    l
    i
    v
    e
    r
    e
    d
    o
    r
    h
    a
    s
    b
    e
    e
    n
    s
    u
    p
    p
    l
    i
    e
    d
    .
    
    """
    
    resource_type = "SupplyDeliverySuppliedItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.quantity = None
        """ 
        A
        m
        o
        u
        n
        t
        d
        i
        s
        p
        e
        n
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SupplyDeliverySuppliedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyDeliverySuppliedItem, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
