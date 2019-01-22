#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Account) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Account(domainresource.DomainResource):
    """ 
    T
    r
    a
    c
    k
    s
    b
    a
    l
    a
    n
    c
    e
    ,
    c
    h
    a
    r
    g
    e
    s
    ,
    f
    o
    r
    p
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
    s
    t
    c
    e
    n
    t
    e
    r
    .
    
    
    A
    f
    i
    n
    a
    n
    c
    i
    a
    l
    t
    o
    o
    l
    f
    o
    r
    t
    r
    a
    c
    k
    i
    n
    g
    v
    a
    l
    u
    e
    a
    c
    c
    r
    u
    e
    d
    f
    o
    r
    a
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
    p
    u
    r
    p
    o
    s
    e
    .
    I
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
    f
    i
    e
    l
    d
    ,
    u
    s
    e
    d
    t
    o
    t
    r
    a
    c
    k
    c
    h
    a
    r
    g
    e
    s
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
    ,
    c
    o
    s
    t
    c
    e
    n
    t
    e
    r
    s
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "Account"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ 
        T
        h
        e
        p
        a
        r
        t
        y
        (
        s
        )
        t
        h
        a
        t
        a
        r
        e
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
        c
        o
        v
        e
        r
        i
        n
        g
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
        o
        f
        t
        h
        i
        s
        a
        c
        c
        o
        u
        n
        t
        ,
        a
        n
        d
        w
        h
        a
        t
        o
        r
        d
        e
        r
        s
        h
        o
        u
        l
        d
        t
        h
        e
        y
        b
        e
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
        a
        c
        c
        o
        u
        n
        t
        .
        List of `AccountCoverage` items (represented as `dict` in JSON). """
        
        self.description = None
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
        o
        f
        p
        u
        r
        p
        o
        s
        e
        /
        u
        s
        e
        .
        Type `str`. """
        
        self.guarantor = None
        """ 
        T
        h
        e
        p
        a
        r
        t
        i
        e
        s
        u
        l
        t
        i
        m
        a
        t
        e
        l
        y
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
        b
        a
        l
        a
        n
        c
        i
        n
        g
        t
        h
        e
        A
        c
        c
        o
        u
        n
        t
        .
        List of `AccountGuarantor` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        A
        c
        c
        o
        u
        n
        t
        n
        u
        m
        b
        e
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        H
        u
        m
        a
        n
        -
        r
        e
        a
        d
        a
        b
        l
        e
        l
        a
        b
        e
        l
        .
        Type `str`. """
        
        self.owner = None
        """ 
        E
        n
        t
        i
        t
        y
        m
        a
        n
        a
        g
        i
        n
        g
        t
        h
        e
        A
        c
        c
        o
        u
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partOf = None
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
        a
        p
        a
        r
        e
        n
        t
        A
        c
        c
        o
        u
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.servicePeriod = None
        """ 
        T
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        w
        i
        n
        d
        o
        w
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
        |
        i
        n
        a
        c
        t
        i
        v
        e
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
        o
        n
        -
        h
        o
        l
        d
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
        T
        h
        e
        e
        n
        t
        i
        t
        y
        t
        h
        a
        t
        c
        a
        u
        s
        e
        d
        t
        h
        e
        e
        x
        p
        e
        n
        s
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        E
        .
        g
        .
        p
        a
        t
        i
        e
        n
        t
        ,
        e
        x
        p
        e
        n
        s
        e
        ,
        d
        e
        p
        r
        e
        c
        i
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Account, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend([
            ("coverage", "coverage", AccountCoverage, True, None, False),
            ("description", "description", str, False, None, False),
            ("guarantor", "guarantor", AccountGuarantor, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("servicePeriod", "servicePeriod", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class AccountCoverage(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    p
    a
    r
    t
    y
    (
    s
    )
    t
    h
    a
    t
    a
    r
    e
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
    c
    o
    v
    e
    r
    i
    n
    g
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
    o
    f
    t
    h
    i
    s
    a
    c
    c
    o
    u
    n
    t
    ,
    a
    n
    d
    w
    h
    a
    t
    o
    r
    d
    e
    r
    s
    h
    o
    u
    l
    d
    t
    h
    e
    y
    b
    e
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
    a
    c
    c
    o
    u
    n
    t
    .
    """
    
    resource_type = "AccountCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None
        """ 
        T
        h
        e
        p
        a
        r
        t
        y
        (
        s
        )
        ,
        s
        u
        c
        h
        a
        s
        i
        n
        s
        u
        r
        a
        n
        c
        e
        s
        ,
        t
        h
        a
        t
        m
        a
        y
        c
        o
        n
        t
        r
        i
        b
        u
        t
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
        o
        f
        t
        h
        i
        s
        a
        c
        c
        o
        u
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        """ 
        T
        h
        e
        p
        r
        i
        o
        r
        i
        t
        y
        o
        f
        t
        h
        e
        c
        o
        v
        e
        r
        a
        g
        e
        i
        n
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        o
        f
        t
        h
        i
        s
        a
        c
        c
        o
        u
        n
        t
        .
        Type `int`. """
        
        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("priority", "priority", int, False, None, False),
        ])
        return js


class AccountGuarantor(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    p
    a
    r
    t
    i
    e
    s
    u
    l
    t
    i
    m
    a
    t
    e
    l
    y
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
    b
    a
    l
    a
    n
    c
    i
    n
    g
    t
    h
    e
    A
    c
    c
    o
    u
    n
    t
    .
    
    
    T
    h
    e
    p
    a
    r
    t
    i
    e
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
    b
    a
    l
    a
    n
    c
    i
    n
    g
    t
    h
    e
    a
    c
    c
    o
    u
    n
    t
    i
    f
    o
    t
    h
    e
    r
    p
    a
    y
    m
    e
    n
    t
    o
    p
    t
    i
    o
    n
    s
    f
    a
    l
    l
    s
    h
    o
    r
    t
    .
    
    """
    
    resource_type = "AccountGuarantor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.onHold = None
        """ 
        C
        r
        e
        d
        i
        t
        o
        r
        o
        t
        h
        e
        r
        h
        o
        l
        d
        a
        p
        p
        l
        i
        e
        d
        .
        Type `bool`. """
        
        self.party = None
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
        e
        n
        t
        i
        t
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        G
        u
        a
        r
        a
        n
        t
        e
        e
        a
        c
        c
        o
        u
        n
        t
        d
        u
        r
        i
        n
        g
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend([
            ("onHold", "onHold", bool, False, None, False),
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
