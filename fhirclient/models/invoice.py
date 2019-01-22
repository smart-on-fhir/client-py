#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Invoice) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Invoice(domainresource.DomainResource):
    """ 
    I
    n
    v
    o
    i
    c
    e
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
    s
    f
    r
    o
    m
    a
    n
    A
    c
    c
    o
    u
    n
    t
    .
    
    
    I
    n
    v
    o
    i
    c
    e
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
    o
    l
    l
    e
    c
    t
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
    s
    f
    r
    o
    m
    a
    n
    A
    c
    c
    o
    u
    n
    t
    w
    i
    t
    h
    c
    a
    l
    c
    u
    l
    a
    t
    e
    d
    i
    n
    d
    i
    v
    i
    d
    u
    a
    l
    a
    n
    d
    t
    o
    t
    a
    l
    p
    r
    i
    c
    e
    f
    o
    r
    B
    i
    l
    l
    i
    n
    g
    p
    u
    r
    p
    o
    s
    e
    .
    
    """
    
    resource_type = "Invoice"
    
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
        b
        a
        l
        a
        n
        c
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.cancelledReason = None
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
        c
        a
        n
        c
        e
        l
        l
        a
        t
        i
        o
        n
        o
        f
        t
        h
        i
        s
        I
        n
        v
        o
        i
        c
        e
        .
        Type `str`. """
        
        self.date = None
        """ 
        I
        n
        v
        o
        i
        c
        e
        d
        a
        t
        e
        /
        p
        o
        s
        t
        i
        n
        g
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        
        self.issuer = None
        """ 
        I
        s
        s
        u
        i
        n
        g
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
        o
        f
        I
        n
        v
        o
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lineItem = None
        """ 
        L
        i
        n
        e
        i
        t
        e
        m
        s
        o
        f
        t
        h
        i
        s
        I
        n
        v
        o
        i
        c
        e
        .
        List of `InvoiceLineItem` items (represented as `dict` in JSON). """
        
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
        i
        n
        v
        o
        i
        c
        e
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ 
        P
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        i
        n
        c
        r
        e
        a
        t
        i
        o
        n
        o
        f
        t
        h
        i
        s
        I
        n
        v
        o
        i
        c
        e
        .
        List of `InvoiceParticipant` items (represented as `dict` in JSON). """
        
        self.paymentTerms = None
        """ 
        P
        a
        y
        m
        e
        n
        t
        d
        e
        t
        a
        i
        l
        s
        .
        Type `str`. """
        
        self.recipient = None
        """ 
        R
        e
        c
        i
        p
        i
        e
        n
        t
        o
        f
        t
        h
        i
        s
        i
        n
        v
        o
        i
        c
        e
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
        i
        s
        s
        u
        e
        d
        |
        b
        a
        l
        a
        n
        c
        e
        d
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
        .
        Type `str`. """
        
        self.subject = None
        """ 
        R
        e
        c
        i
        p
        i
        e
        n
        t
        (
        s
        )
        o
        f
        g
        o
        o
        d
        s
        a
        n
        d
        s
        e
        r
        v
        i
        c
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.totalGross = None
        """ 
        G
        r
        o
        s
        s
        t
        o
        t
        a
        l
        o
        f
        t
        h
        i
        s
        I
        n
        v
        o
        i
        c
        e
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalNet = None
        """ 
        N
        e
        t
        t
        o
        t
        a
        l
        o
        f
        t
        h
        i
        s
        I
        n
        v
        o
        i
        c
        e
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalPriceComponent = None
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
        s
        o
        f
        I
        n
        v
        o
        i
        c
        e
        t
        o
        t
        a
        l
        .
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        I
        n
        v
        o
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Invoice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Invoice, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, False, None, False),
            ("cancelledReason", "cancelledReason", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("lineItem", "lineItem", InvoiceLineItem, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("participant", "participant", InvoiceParticipant, True, None, False),
            ("paymentTerms", "paymentTerms", str, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("totalGross", "totalGross", money.Money, False, None, False),
            ("totalNet", "totalNet", money.Money, False, None, False),
            ("totalPriceComponent", "totalPriceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class InvoiceLineItem(backboneelement.BackboneElement):
    """ 
    L
    i
    n
    e
    i
    t
    e
    m
    s
    o
    f
    t
    h
    i
    s
    I
    n
    v
    o
    i
    c
    e
    .
    
    
    E
    a
    c
    h
    l
    i
    n
    e
    i
    t
    e
    m
    r
    e
    p
    r
    e
    s
    e
    n
    t
    s
    o
    n
    e
    c
    h
    a
    r
    g
    e
    f
    o
    r
    g
    o
    o
    d
    s
    a
    n
    d
    s
    e
    r
    v
    i
    c
    e
    s
    r
    e
    n
    d
    e
    r
    e
    d
    .
    D
    e
    t
    a
    i
    l
    s
    s
    u
    c
    h
    a
    s
    d
    a
    t
    e
    ,
    c
    o
    d
    e
    a
    n
    d
    a
    m
    o
    u
    n
    t
    a
    r
    e
    f
    o
    u
    n
    d
    i
    n
    t
    h
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
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    """
    
    resource_type = "InvoiceLineItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chargeItemCodeableConcept = None
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
        i
        s
        l
        i
        n
        e
        i
        t
        e
        m
        o
        r
        a
        n
        i
        n
        l
        i
        n
        e
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
        
        self.chargeItemReference = None
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
        i
        s
        l
        i
        n
        e
        i
        t
        e
        m
        o
        r
        a
        n
        i
        n
        l
        i
        n
        e
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priceComponent = None
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
        s
        o
        f
        t
        o
        t
        a
        l
        l
        i
        n
        e
        i
        t
        e
        m
        p
        r
        i
        c
        e
        .
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        S
        e
        q
        u
        e
        n
        c
        e
        n
        u
        m
        b
        e
        r
        o
        f
        l
        i
        n
        e
        i
        t
        e
        m
        .
        Type `int`. """
        
        super(InvoiceLineItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend([
            ("chargeItemCodeableConcept", "chargeItemCodeableConcept", codeableconcept.CodeableConcept, False, "chargeItem", True),
            ("chargeItemReference", "chargeItemReference", fhirreference.FHIRReference, False, "chargeItem", True),
            ("priceComponent", "priceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("sequence", "sequence", int, False, None, False),
        ])
        return js


class InvoiceLineItemPriceComponent(backboneelement.BackboneElement):
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
    s
    o
    f
    t
    o
    t
    a
    l
    l
    i
    n
    e
    i
    t
    e
    m
    p
    r
    i
    c
    e
    .
    
    
    T
    h
    e
    p
    r
    i
    c
    e
    f
    o
    r
    a
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
    m
    a
    y
    b
    e
    c
    a
    l
    c
    u
    l
    a
    t
    e
    d
    a
    s
    a
    b
    a
    s
    e
    p
    r
    i
    c
    e
    w
    i
    t
    h
    s
    u
    r
    c
    h
    a
    r
    g
    e
    s
    /
    d
    e
    d
    u
    c
    t
    i
    o
    n
    s
    t
    h
    a
    t
    a
    p
    p
    l
    y
    i
    n
    c
    e
    r
    t
    a
    i
    n
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
    .
    A
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
    D
    e
    f
    i
    n
    i
    t
    i
    o
    n
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
    d
    e
    f
    i
    n
    e
    s
    t
    h
    e
    p
    r
    i
    c
    e
    s
    ,
    f
    a
    c
    t
    o
    r
    s
    a
    n
    d
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
    t
    h
    a
    t
    a
    p
    p
    l
    y
    t
    o
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
    i
    s
    c
    u
    r
    r
    e
    n
    t
    l
    y
    u
    n
    d
    e
    r
    d
    e
    v
    e
    l
    o
    p
    m
    e
    n
    t
    .
    T
    h
    e
    p
    r
    i
    c
    e
    C
    o
    m
    p
    o
    n
    e
    n
    t
    e
    l
    e
    m
    e
    n
    t
    c
    a
    n
    b
    e
    u
    s
    e
    d
    t
    o
    o
    f
    f
    e
    r
    t
    r
    a
    n
    s
    p
    a
    r
    e
    n
    c
    y
    t
    o
    t
    h
    e
    r
    e
    c
    i
    p
    i
    e
    n
    t
    o
    f
    t
    h
    e
    I
    n
    v
    o
    i
    c
    e
    a
    s
    t
    o
    h
    o
    w
    t
    h
    e
    p
    r
    i
    c
    e
    s
    h
    a
    v
    e
    b
    e
    e
    n
    c
    a
    l
    c
    u
    l
    a
    t
    e
    d
    .
    
    """
    
    resource_type = "InvoiceLineItemPriceComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        M
        o
        n
        e
        t
        a
        r
        y
        a
        m
        o
        u
        n
        t
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
        c
        o
        m
        p
        o
        n
        e
        n
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        C
        o
        d
        e
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
        s
        p
        e
        c
        i
        f
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        """ 
        F
        a
        c
        t
        o
        r
        u
        s
        e
        d
        f
        o
        r
        c
        a
        l
        c
        u
        l
        a
        t
        i
        n
        g
        t
        h
        i
        s
        c
        o
        m
        p
        o
        n
        e
        n
        t
        .
        Type `float`. """
        
        self.type = None
        """ 
        b
        a
        s
        e
        |
        s
        u
        r
        c
        h
        a
        r
        g
        e
        |
        d
        e
        d
        u
        c
        t
        i
        o
        n
        |
        d
        i
        s
        c
        o
        u
        n
        t
        |
        t
        a
        x
        |
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
        l
        .
        Type `str`. """
        
        super(InvoiceLineItemPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class InvoiceParticipant(backboneelement.BackboneElement):
    """ 
    P
    a
    r
    t
    i
    c
    i
    p
    a
    n
    t
    i
    n
    c
    r
    e
    a
    t
    i
    o
    n
    o
    f
    t
    h
    i
    s
    I
    n
    v
    o
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
    
    resource_type = "InvoiceParticipant"
    
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
        i
        n
        v
        o
        l
        v
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        T
        y
        p
        e
        o
        f
        i
        n
        v
        o
        l
        v
        e
        m
        e
        n
        t
        i
        n
        c
        r
        e
        a
        t
        i
        o
        n
        o
        f
        t
        h
        i
        s
        I
        n
        v
        o
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InvoiceParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
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
