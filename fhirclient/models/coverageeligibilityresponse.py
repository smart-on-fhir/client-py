#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CoverageEligibilityResponse(domainresource.DomainResource):
    """ 
    C
    o
    v
    e
    r
    a
    g
    e
    E
    l
    i
    g
    i
    b
    i
    l
    i
    t
    y
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
    e
    l
    i
    g
    i
    b
    i
    l
    i
    t
    y
    a
    n
    d
    p
    l
    a
    n
    d
    e
    t
    a
    i
    l
    s
    f
    r
    o
    m
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
    o
    f
    a
    n
    C
    o
    v
    e
    r
    a
    g
    e
    E
    l
    i
    g
    i
    b
    i
    l
    i
    t
    y
    R
    e
    q
    u
    e
    s
    t
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
    
    resource_type = "CoverageEligibilityResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
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
        M
        e
        s
        s
        a
        g
        e
        .
        Type `str`. """
        
        self.error = None
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
        e
        r
        r
        o
        r
        s
        .
        List of `CoverageEligibilityResponseError` items (represented as `dict` in JSON). """
        
        self.form = None
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
        c
        o
        v
        e
        r
        a
        g
        e
        e
        l
        i
        g
        i
        b
        l
        i
        t
        y
        r
        e
        q
        u
        e
        s
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        i
        n
        s
        u
        r
        a
        n
        c
        e
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
        List of `CoverageEligibilityResponseInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ 
        C
        o
        v
        e
        r
        a
        g
        e
        i
        s
        s
        u
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.patient = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
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
        p
        r
        o
        d
        u
        c
        t
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
        
        self.preAuthRef = None
        """ 
        P
        r
        e
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
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
        Type `str`. """
        
        self.purpose = None
        """ 
        a
        u
        t
        h
        -
        r
        e
        q
        u
        i
        r
        e
        m
        e
        n
        t
        s
        |
        b
        e
        n
        e
        f
        i
        t
        s
        |
        d
        i
        s
        c
        o
        v
        e
        r
        y
        |
        v
        a
        l
        i
        d
        a
        t
        i
        o
        n
        .
        List of `str` items. """
        
        self.request = None
        """ 
        E
        l
        i
        g
        i
        b
        i
        l
        i
        t
        y
        r
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
        
        self.requestor = None
        """ 
        P
        a
        r
        t
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
        
        self.servicedDate = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        d
        d
        a
        t
        e
        o
        r
        d
        a
        t
        e
        s
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
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ 
        E
        s
        t
        i
        m
        a
        t
        e
        d
        d
        a
        t
        e
        o
        r
        d
        a
        t
        e
        s
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
        
        super(CoverageEligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", CoverageEligibilityResponseError, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("outcome", "outcome", str, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, True),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class CoverageEligibilityResponseError(backboneelement.BackboneElement):
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
    e
    r
    r
    o
    r
    s
    .
    
    
    E
    r
    r
    o
    r
    s
    e
    n
    c
    o
    u
    n
    t
    e
    r
    e
    d
    d
    u
    r
    i
    n
    g
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
    
    """
    
    resource_type = "CoverageEligibilityResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        E
        r
        r
        o
        r
        c
        o
        d
        e
        d
        e
        t
        a
        i
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
        i
        n
        g
        i
        s
        s
        u
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """ 
    P
    a
    t
    i
    e
    n
    t
    i
    n
    s
    u
    r
    a
    n
    c
    e
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
    
    
    F
    i
    n
    a
    n
    c
    i
    a
    l
    i
    n
    s
    t
    r
    u
    m
    e
    n
    t
    s
    f
    o
    r
    r
    e
    i
    m
    b
    u
    r
    s
    e
    m
    e
    n
    t
    f
    o
    r
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
    p
    r
    o
    d
    u
    c
    t
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
    
    """
    
    resource_type = "CoverageEligibilityResponseInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitPeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        b
        e
        n
        e
        f
        i
        t
        s
        a
        r
        e
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ 
        I
        n
        s
        u
        r
        a
        n
        c
        e
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.inforce = None
        """ 
        C
        o
        v
        e
        r
        a
        g
        e
        i
        n
        f
        o
        r
        c
        e
        i
        n
        d
        i
        c
        a
        t
        o
        r
        .
        Type `bool`. """
        
        self.item = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        a
        n
        d
        a
        u
        t
        h
        o
        r
        i
        z
        a
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
        List of `CoverageEligibilityResponseInsuranceItem` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("benefitPeriod", "benefitPeriod", period.Period, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("inforce", "inforce", bool, False, None, False),
            ("item", "item", CoverageEligibilityResponseInsuranceItem, True, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """ 
    B
    e
    n
    e
    f
    i
    t
    s
    a
    n
    d
    a
    u
    t
    h
    o
    r
    i
    z
    a
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
    
    
    B
    e
    n
    e
    f
    i
    t
    s
    a
    n
    d
    o
    p
    t
    i
    o
    n
    a
    l
    l
    y
    c
    u
    r
    r
    e
    n
    t
    b
    a
    l
    a
    n
    c
    e
    s
    ,
    a
    n
    d
    a
    u
    t
    h
    o
    r
    i
    z
    a
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
    b
    y
    c
    a
    t
    e
    g
    o
    r
    y
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
    
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorizationRequired = None
        """ 
        A
        u
        t
        h
        o
        r
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
        i
        r
        e
        d
        f
        l
        a
        g
        .
        Type `bool`. """
        
        self.authorizationSupporting = None
        """ 
        T
        y
        p
        e
        o
        f
        r
        e
        q
        u
        i
        r
        e
        d
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
        m
        a
        t
        e
        r
        i
        a
        l
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.authorizationUrl = None
        """ 
        P
        r
        e
        a
        u
        t
        h
        o
        r
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
        i
        r
        e
        m
        e
        n
        t
        s
        e
        n
        d
        p
        o
        i
        n
        t
        .
        Type `str`. """
        
        self.benefit = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        S
        u
        m
        m
        a
        r
        y
        .
        List of `CoverageEligibilityResponseInsuranceItemBenefit` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        c
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        D
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
        b
        e
        n
        e
        f
        i
        t
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
        c
        o
        v
        e
        r
        e
        d
        .
        Type `str`. """
        
        self.excluded = None
        """ 
        E
        x
        c
        l
        u
        d
        e
        d
        f
        r
        o
        m
        t
        h
        e
        p
        l
        a
        n
        .
        Type `bool`. """
        
        self.modifier = None
        """ 
        P
        r
        o
        d
        u
        c
        t
        o
        r
        s
        e
        r
        v
        i
        c
        e
        b
        i
        l
        l
        i
        n
        g
        m
        o
        d
        i
        f
        i
        e
        r
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        S
        h
        o
        r
        t
        n
        a
        m
        e
        f
        o
        r
        t
        h
        e
        b
        e
        n
        e
        f
        i
        t
        .
        Type `str`. """
        
        self.network = None
        """ 
        I
        n
        o
        r
        o
        u
        t
        o
        f
        n
        e
        t
        w
        o
        r
        k
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productOrService = None
        """ 
        B
        i
        l
        l
        i
        n
        g
        ,
        s
        e
        r
        v
        i
        c
        e
        ,
        p
        r
        o
        d
        u
        c
        t
        ,
        o
        r
        d
        r
        u
        g
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
        """ 
        P
        e
        r
        f
        o
        r
        m
        i
        n
        g
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
        
        self.term = None
        """ 
        A
        n
        n
        u
        a
        l
        o
        r
        l
        i
        f
        e
        t
        i
        m
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
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
        f
        a
        m
        i
        l
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityResponseInsuranceItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend([
            ("authorizationRequired", "authorizationRequired", bool, False, None, False),
            ("authorizationSupporting", "authorizationSupporting", codeableconcept.CodeableConcept, True, None, False),
            ("authorizationUrl", "authorizationUrl", str, False, None, False),
            ("benefit", "benefit", CoverageEligibilityResponseInsuranceItemBenefit, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """ 
    B
    e
    n
    e
    f
    i
    t
    S
    u
    m
    m
    a
    r
    y
    .
    
    
    B
    e
    n
    e
    f
    i
    t
    s
    u
    s
    e
    d
    t
    o
    d
    a
    t
    e
    .
    
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItemBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedMoney = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        a
        l
        l
        o
        w
        e
        d
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.allowedString = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        a
        l
        l
        o
        w
        e
        d
        .
        Type `str`. """
        
        self.allowedUnsignedInt = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        a
        l
        l
        o
        w
        e
        d
        .
        Type `int`. """
        
        self.type = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        c
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.usedMoney = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        u
        s
        e
        d
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.usedString = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        u
        s
        e
        d
        .
        Type `str`. """
        
        self.usedUnsignedInt = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        u
        s
        e
        d
        .
        Type `int`. """
        
        super(CoverageEligibilityResponseInsuranceItemBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItemBenefit, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("usedString", "usedString", str, False, "used", False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
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
