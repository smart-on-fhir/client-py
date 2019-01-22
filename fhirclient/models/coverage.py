#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Coverage) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Coverage(domainresource.DomainResource):
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
    o
    r
    m
    e
    d
    i
    c
    a
    l
    p
    l
    a
    n
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
    a
    g
    r
    e
    e
    m
    e
    n
    t
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
    w
    h
    i
    c
    h
    m
    a
    y
    b
    e
    u
    s
    e
    d
    t
    o
    r
    e
    i
    m
    b
    u
    r
    s
    e
    o
    r
    p
    a
    y
    f
    o
    r
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
    I
    n
    c
    l
    u
    d
    e
    s
    b
    o
    t
    h
    i
    n
    s
    u
    r
    a
    n
    c
    e
    a
    n
    d
    s
    e
    l
    f
    -
    p
    a
    y
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "Coverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.beneficiary = None
        """ 
        P
        l
        a
        n
        b
        e
        n
        e
        f
        i
        c
        i
        a
        r
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.class_fhir = None
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
        o
        v
        e
        r
        a
        g
        e
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
        s
        .
        List of `CoverageClass` items (represented as `dict` in JSON). """
        
        self.contract = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        d
        e
        t
        a
        i
        l
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.costToBeneficiary = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        p
        a
        y
        m
        e
        n
        t
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
        s
        /
        p
        r
        o
        d
        u
        c
        t
        s
        .
        List of `CoverageCostToBeneficiary` items (represented as `dict` in JSON). """
        
        self.dependent = None
        """ 
        D
        e
        p
        e
        n
        d
        e
        n
        t
        n
        u
        m
        b
        e
        r
        .
        Type `str`. """
        
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
        c
        o
        v
        e
        r
        a
        g
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.network = None
        """ 
        I
        n
        s
        u
        r
        e
        r
        n
        e
        t
        w
        o
        r
        k
        .
        Type `str`. """
        
        self.order = None
        """ 
        R
        e
        l
        a
        t
        i
        v
        e
        o
        r
        d
        e
        r
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
        .
        Type `int`. """
        
        self.payor = None
        """ 
        I
        s
        s
        u
        e
        r
        o
        f
        t
        h
        e
        p
        o
        l
        i
        c
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        C
        o
        v
        e
        r
        a
        g
        e
        s
        t
        a
        r
        t
        a
        n
        d
        e
        n
        d
        d
        a
        t
        e
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.policyHolder = None
        """ 
        O
        w
        n
        e
        r
        o
        f
        t
        h
        e
        p
        o
        l
        i
        c
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        B
        e
        n
        e
        f
        i
        c
        i
        a
        r
        y
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        t
        o
        t
        h
        e
        s
        u
        b
        s
        c
        r
        i
        b
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        
        self.subrogation = None
        """ 
        R
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
        t
        o
        i
        n
        s
        u
        r
        e
        r
        .
        Type `bool`. """
        
        self.subscriber = None
        """ 
        S
        u
        b
        s
        c
        r
        i
        b
        e
        r
        t
        o
        t
        h
        e
        p
        o
        l
        i
        c
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subscriberId = None
        """ 
        I
        D
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
        e
        s
        u
        b
        s
        c
        r
        i
        b
        e
        r
        .
        Type `str`. """
        
        self.type = None
        """ 
        C
        o
        v
        e
        r
        a
        g
        e
        c
        a
        t
        e
        g
        o
        r
        y
        s
        u
        c
        h
        a
        s
        m
        e
        d
        i
        c
        a
        l
        o
        r
        a
        c
        c
        i
        d
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiary", "beneficiary", fhirreference.FHIRReference, False, None, True),
            ("class_fhir", "class", CoverageClass, True, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("costToBeneficiary", "costToBeneficiary", CoverageCostToBeneficiary, True, None, False),
            ("dependent", "dependent", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("network", "network", str, False, None, False),
            ("order", "order", int, False, None, False),
            ("payor", "payor", fhirreference.FHIRReference, True, None, True),
            ("period", "period", period.Period, False, None, False),
            ("policyHolder", "policyHolder", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("subrogation", "subrogation", bool, False, None, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False),
            ("subscriberId", "subscriberId", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class CoverageClass(backboneelement.BackboneElement):
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
    o
    v
    e
    r
    a
    g
    e
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
    s
    .
    
    
    A
    s
    u
    i
    t
    e
    o
    f
    u
    n
    d
    e
    r
    w
    r
    i
    t
    e
    r
    s
    p
    e
    c
    i
    f
    i
    c
    c
    l
    a
    s
    s
    i
    f
    i
    e
    r
    s
    .
    
    """
    
    resource_type = "CoverageClass"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ 
        H
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
        d
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
        t
        y
        p
        e
        a
        n
        d
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        c
        l
        a
        s
        s
        s
        u
        c
        h
        a
        s
        '
        g
        r
        o
        u
        p
        '
        o
        r
        '
        p
        l
        a
        n
        '
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        V
        a
        l
        u
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
        t
        h
        e
        t
        y
        p
        e
        .
        Type `str`. """
        
        super(CoverageClass, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """ 
    P
    a
    t
    i
    e
    n
    t
    p
    a
    y
    m
    e
    n
    t
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
    s
    /
    p
    r
    o
    d
    u
    c
    t
    s
    .
    
    
    A
    s
    u
    i
    t
    e
    o
    f
    c
    o
    d
    e
    s
    i
    n
    d
    i
    c
    a
    t
    i
    n
    g
    t
    h
    e
    c
    o
    s
    t
    c
    a
    t
    e
    g
    o
    r
    y
    a
    n
    d
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
    a
    m
    o
    u
    n
    t
    w
    h
    i
    c
    h
    h
    a
    v
    e
    b
    e
    e
    n
    d
    e
    t
    a
    i
    l
    e
    d
    i
    n
    t
    h
    e
    p
    o
    l
    i
    c
    y
    a
    n
    d
    m
    a
    y
    h
    a
    v
    e
    b
    e
    e
    n
    i
    n
    c
    l
    u
    d
    e
    d
    o
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
    d
    .
    
    """
    
    resource_type = "CoverageCostToBeneficiary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exception = None
        """ 
        E
        x
        c
        e
        p
        t
        i
        o
        n
        s
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
        p
        a
        y
        m
        e
        n
        t
        s
        .
        List of `CoverageCostToBeneficiaryException` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        o
        s
        t
        c
        a
        t
        e
        g
        o
        r
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ 
        T
        h
        e
        a
        m
        o
        u
        n
        t
        o
        r
        p
        e
        r
        c
        e
        n
        t
        a
        g
        e
        d
        u
        e
        f
        r
        o
        m
        t
        h
        e
        b
        e
        n
        e
        f
        i
        c
        i
        a
        r
        y
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ 
        T
        h
        e
        a
        m
        o
        u
        n
        t
        o
        r
        p
        e
        r
        c
        e
        n
        t
        a
        g
        e
        d
        u
        e
        f
        r
        o
        m
        t
        h
        e
        b
        e
        n
        e
        f
        i
        c
        i
        a
        r
        y
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(CoverageCostToBeneficiary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend([
            ("exception", "exception", CoverageCostToBeneficiaryException, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
        ])
        return js


class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """ 
    E
    x
    c
    e
    p
    t
    i
    o
    n
    s
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
    p
    a
    y
    m
    e
    n
    t
    s
    .
    
    
    A
    s
    u
    i
    t
    e
    o
    f
    c
    o
    d
    e
    s
    i
    n
    d
    i
    c
    a
    t
    i
    n
    g
    e
    x
    c
    e
    p
    t
    i
    o
    n
    s
    o
    r
    r
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
    o
    p
    a
    t
    i
    e
    n
    t
    c
    o
    s
    t
    s
    a
    n
    d
    t
    h
    e
    i
    r
    e
    f
    f
    e
    c
    t
    i
    v
    e
    p
    e
    r
    i
    o
    d
    s
    .
    
    """
    
    resource_type = "CoverageCostToBeneficiaryException"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ 
        T
        h
        e
        e
        f
        f
        e
        c
        t
        i
        v
        e
        p
        e
        r
        i
        o
        d
        o
        f
        t
        h
        e
        e
        x
        c
        e
        p
        t
        i
        o
        n
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        E
        x
        c
        e
        p
        t
        i
        o
        n
        c
        a
        t
        e
        g
        o
        r
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CoverageCostToBeneficiaryException, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
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
