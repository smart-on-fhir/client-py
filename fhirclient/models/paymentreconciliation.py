#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ 
    P
    a
    y
    m
    e
    n
    t
    R
    e
    c
    o
    n
    c
    i
    l
    i
    a
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
    .
    
    
    T
    h
    i
    s
    r
    e
    s
    o
    u
    r
    c
    e
    p
    r
    o
    v
    i
    d
    e
    s
    t
    h
    e
    d
    e
    t
    a
    i
    l
    s
    i
    n
    c
    l
    u
    d
    i
    n
    g
    a
    m
    o
    u
    n
    t
    o
    f
    a
    p
    a
    y
    m
    e
    n
    t
    a
    n
    d
    a
    l
    l
    o
    c
    a
    t
    e
    s
    t
    h
    e
    p
    a
    y
    m
    e
    n
    t
    i
    t
    e
    m
    s
    b
    e
    i
    n
    g
    p
    a
    i
    d
    .
    
    """
    
    resource_type = "PaymentReconciliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ 
        C
        r
        e
        a
        t
        i
        o
        n
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ 
        S
        e
        t
        t
        l
        e
        m
        e
        n
        t
        p
        a
        r
        t
        i
        c
        u
        l
        a
        r
        s
        .
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.disposition = None
        """ 
        D
        i
        s
        p
        o
        s
        i
        t
        i
        o
        n
        m
        e
        s
        s
        a
        g
        e
        .
        Type `str`. """
        
        self.formCode = None
        """ 
        P
        r
        i
        n
        t
        e
        d
        f
        o
        r
        m
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        a
        p
        a
        y
        m
        e
        n
        t
        r
        e
        c
        o
        n
        c
        i
        l
        i
        a
        t
        i
        o
        n
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ 
        q
        u
        e
        u
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
        |
        e
        r
        r
        o
        r
        |
        p
        a
        r
        t
        i
        a
        l
        .
        Type `str`. """
        
        self.paymentAmount = None
        """ 
        T
        o
        t
        a
        l
        a
        m
        o
        u
        n
        t
        o
        f
        P
        a
        y
        m
        e
        n
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentDate = None
        """ 
        W
        h
        e
        n
        p
        a
        y
        m
        e
        n
        t
        i
        s
        s
        u
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.paymentIdentifier = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
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
        f
        o
        r
        t
        h
        e
        p
        a
        y
        m
        e
        n
        t
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.paymentIssuer = None
        """ 
        P
        a
        r
        t
        y
        g
        e
        n
        e
        r
        a
        t
        i
        n
        g
        p
        a
        y
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        P
        e
        r
        i
        o
        d
        c
        o
        v
        e
        r
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.processNote = None
        """ 
        N
        o
        t
        e
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
        .
        List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON). """
        
        self.request = None
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
        r
        e
        s
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestor = None
        """ 
        R
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
        p
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
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
        d
        r
        a
        f
        t
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
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("paymentAmount", "paymentAmount", money.Money, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, True),
            ("paymentIdentifier", "paymentIdentifier", identifier.Identifier, False, None, False),
            ("paymentIssuer", "paymentIssuer", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ 
    S
    e
    t
    t
    l
    e
    m
    e
    n
    t
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    s
    .
    
    
    D
    i
    s
    t
    r
    i
    b
    u
    t
    i
    o
    n
    o
    f
    t
    h
    e
    p
    a
    y
    m
    e
    n
    t
    a
    m
    o
    u
    n
    t
    f
    o
    r
    a
    p
    r
    e
    v
    i
    o
    u
    s
    l
    y
    a
    c
    k
    n
    o
    w
    l
    e
    d
    g
    e
    d
    p
    a
    y
    a
    b
    l
    e
    .
    
    """
    
    resource_type = "PaymentReconciliationDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        A
        m
        o
        u
        n
        t
        a
        l
        l
        o
        c
        a
        t
        e
        d
        t
        o
        t
        h
        i
        s
        p
        a
        y
        a
        b
        l
        e
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        D
        a
        t
        e
        o
        f
        c
        o
        m
        m
        i
        t
        m
        e
        n
        t
        t
        o
        p
        a
        y
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
        e
        p
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
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.payee = None
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
        e
        p
        a
        y
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.predecessor = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
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
        e
        p
        r
        i
        o
        r
        p
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
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.request = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        g
        i
        v
        i
        n
        g
        r
        i
        s
        e
        t
        o
        t
        h
        e
        p
        a
        y
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        """ 
        R
        e
        s
        p
        o
        n
        s
        e
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
        t
        o
        a
        p
        a
        y
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ 
        C
        o
        n
        t
        a
        c
        t
        f
        o
        r
        t
        h
        e
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.submitter = None
        """ 
        S
        u
        b
        m
        i
        t
        t
        e
        r
        o
        f
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
        p
        a
        y
        m
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("predecessor", "predecessor", identifier.Identifier, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ 
    N
    o
    t
    e
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
    .
    
    
    A
    n
    o
    t
    e
    t
    h
    a
    t
    d
    e
    s
    c
    r
    i
    b
    e
    s
    o
    r
    e
    x
    p
    l
    a
    i
    n
    s
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
    i
    n
    a
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
    f
    o
    r
    m
    .
    
    """
    
    resource_type = "PaymentReconciliationProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ 
        N
        o
        t
        e
        e
        x
        p
        l
        a
        n
        a
        t
        o
        r
        y
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.type = None
        """ 
        d
        i
        s
        p
        l
        a
        y
        |
        p
        r
        i
        n
        t
        |
        p
        r
        i
        n
        t
        o
        p
        e
        r
        .
        Type `str`. """
        
        super(PaymentReconciliationProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
