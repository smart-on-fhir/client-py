#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ 
    P
    a
    y
    m
    e
    n
    t
    N
    o
    t
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
    s
    t
    a
    t
    u
    s
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
    ,
    a
    n
    d
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
    a
    n
    d
    r
    e
    s
    p
    o
    n
    s
    e
    r
    e
    s
    o
    u
    r
    c
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
    s
    .
    
    """
    
    resource_type = "PaymentNotice"
    
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
        Type `Money` (represented as `dict` in JSON). """
        
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
        n
        o
        c
        t
        i
        c
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.payee = None
        """ 
        P
        a
        r
        t
        y
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payment = None
        """ 
        P
        a
        y
        m
        e
        n
        t
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
        
        self.paymentDate = None
        """ 
        P
        a
        y
        m
        e
        n
        t
        o
        r
        c
        l
        e
        a
        r
        i
        n
        g
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.paymentStatus = None
        """ 
        I
        s
        s
        u
        e
        d
        o
        r
        c
        l
        e
        a
        r
        e
        d
        S
        t
        a
        t
        u
        s
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
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
        
        self.recipient = None
        """ 
        P
        a
        r
        t
        y
        b
        e
        i
        n
        g
        n
        o
        t
        i
        f
        i
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.request = None
        """ 
        R
        e
        q
        u
        e
        s
        t
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
        
        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("payment", "payment", fhirreference.FHIRReference, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("paymentStatus", "paymentStatus", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
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
