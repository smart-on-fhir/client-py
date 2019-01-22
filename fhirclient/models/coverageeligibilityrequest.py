#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CoverageEligibilityRequest(domainresource.DomainResource):
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
    
    
    T
    h
    e
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
    p
    r
    o
    v
    i
    d
    e
    s
    p
    a
    t
    i
    e
    n
    t
    a
    n
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
    t
    o
    a
    n
    i
    n
    s
    u
    r
    e
    r
    f
    o
    r
    t
    h
    e
    m
    t
    o
    r
    e
    s
    p
    o
    n
    d
    ,
    i
    n
    t
    h
    e
    f
    o
    r
    m
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
    s
    p
    o
    n
    s
    e
    ,
    w
    i
    t
    h
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
    r
    e
    g
    a
    r
    d
    i
    n
    g
    w
    h
    e
    t
    h
    e
    r
    t
    h
    e
    s
    t
    a
    t
    e
    d
    c
    o
    v
    e
    r
    a
    g
    e
    i
    s
    v
    a
    l
    i
    d
    a
    n
    d
    i
    n
    -
    f
    o
    r
    c
    e
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
    t
    o
    p
    r
    o
    v
    i
    d
    e
    t
    h
    e
    i
    n
    s
    u
    r
    a
    n
    c
    e
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
    o
    l
    i
    c
    y
    .
    
    """
    
    resource_type = "CoverageEligibilityRequest"
    
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
        
        self.enterer = None
        """ 
        A
        u
        t
        h
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.facility = None
        """ 
        S
        e
        r
        v
        i
        c
        i
        n
        g
        f
        a
        c
        i
        l
        i
        t
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
        List of `CoverageEligibilityRequestInsurance` items (represented as `dict` in JSON). """
        
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
        
        self.item = None
        """ 
        I
        t
        e
        m
        t
        o
        b
        e
        e
        v
        a
        l
        u
        a
        t
        e
        d
        f
        o
        r
        e
        l
        i
        g
        i
        b
        i
        i
        t
        y
        .
        List of `CoverageEligibilityRequestItem` items (represented as `dict` in JSON). """
        
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
        
        self.priority = None
        """ 
        D
        e
        s
        i
        r
        e
        d
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
        p
        r
        i
        o
        r
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
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
        
        self.supportingInfo = None
        """ 
        S
        u
        p
        p
        o
        r
        t
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
        .
        List of `CoverageEligibilityRequestSupportingInfo` items (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", CoverageEligibilityRequestInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("item", "item", CoverageEligibilityRequestItem, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("status", "status", str, False, None, True),
            ("supportingInfo", "supportingInfo", CoverageEligibilityRequestSupportingInfo, True, None, False),
        ])
        return js


from . import backboneelement

class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
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
    
    resource_type = "CoverageEligibilityRequestInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
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
        p
        r
        o
        v
        i
        d
        e
        r
        c
        o
        n
        t
        r
        a
        c
        t
        n
        u
        m
        b
        e
        r
        .
        Type `str`. """
        
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
        
        self.focal = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
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
        Type `bool`. """
        
        super(CoverageEligibilityRequestInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """ 
    I
    t
    e
    m
    t
    o
    b
    e
    e
    v
    a
    l
    u
    a
    t
    e
    d
    f
    o
    r
    e
    l
    i
    g
    i
    b
    i
    i
    t
    y
    .
    
    
    S
    e
    r
    v
    i
    c
    e
    c
    a
    t
    e
    g
    o
    r
    i
    e
    s
    o
    r
    b
    i
    l
    l
    a
    b
    l
    e
    s
    e
    r
    v
    i
    c
    e
    s
    f
    o
    r
    w
    h
    i
    c
    h
    b
    e
    n
    e
    f
    i
    t
    d
    e
    t
    a
    i
    l
    s
    a
    n
    d
    /
    o
    r
    a
    n
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
    p
    r
    i
    o
    r
    t
    o
    s
    e
    r
    v
    i
    c
    e
    d
    e
    l
    i
    v
    e
    r
    y
    m
    a
    y
    b
    e
    r
    e
    q
    u
    i
    r
    e
    d
    b
    y
    t
    h
    e
    p
    a
    y
    o
    r
    .
    
    """
    
    resource_type = "CoverageEligibilityRequestItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.detail = None
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
        d
        e
        t
        a
        i
        l
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.diagnosis = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
        e
        d
        i
        a
        g
        n
        o
        s
        i
        s
        .
        List of `CoverageEligibilityRequestItemDiagnosis` items (represented as `dict` in JSON). """
        
        self.facility = None
        """ 
        S
        e
        r
        v
        i
        c
        i
        n
        g
        f
        a
        c
        i
        l
        i
        t
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.quantity = None
        """ 
        C
        o
        u
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
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.supportingInfoSequence = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
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
        o
        r
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
        List of `int` items. """
        
        self.unitPrice = None
        """ 
        F
        e
        e
        ,
        c
        h
        a
        r
        g
        e
        o
        r
        c
        o
        s
        t
        p
        e
        r
        i
        t
        e
        m
        .
        Type `Money` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequestItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("diagnosis", "diagnosis", CoverageEligibilityRequestItemDiagnosis, True, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("supportingInfoSequence", "supportingInfoSequence", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """ 
    A
    p
    p
    l
    i
    c
    a
    b
    l
    e
    d
    i
    a
    g
    n
    o
    s
    i
    s
    .
    
    
    P
    a
    t
    i
    e
    n
    t
    d
    i
    a
    g
    n
    o
    s
    i
    s
    f
    o
    r
    w
    h
    i
    c
    h
    c
    a
    r
    e
    i
    s
    s
    o
    u
    g
    h
    t
    .
    
    """
    
    resource_type = "CoverageEligibilityRequestItemDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        """ 
        N
        a
        t
        u
        r
        e
        o
        f
        i
        l
        l
        n
        e
        s
        s
        o
        r
        p
        r
        o
        b
        l
        e
        m
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnosisReference = None
        """ 
        N
        a
        t
        u
        r
        e
        o
        f
        i
        l
        l
        n
        e
        s
        s
        o
        r
        p
        r
        o
        b
        l
        e
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CoverageEligibilityRequestItemDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", False),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", False),
        ])
        return js


class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """ 
    S
    u
    p
    p
    o
    r
    t
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
    .
    
    
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
    c
    o
    d
    e
    s
    r
    e
    g
    a
    r
    d
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
    ,
    s
    p
    e
    c
    i
    a
    l
    c
    o
    n
    s
    i
    d
    e
    r
    a
    t
    i
    o
    n
    s
    ,
    t
    h
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
    ,
    s
    i
    t
    u
    a
    t
    i
    o
    n
    ,
    p
    r
    i
    o
    r
    o
    r
    c
    o
    n
    c
    u
    r
    r
    e
    n
    t
    i
    s
    s
    u
    e
    s
    .
    
    """
    
    resource_type = "CoverageEligibilityRequestSupportingInfo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appliesToAll = None
        """ 
        A
        p
        p
        l
        i
        e
        s
        t
        o
        a
        l
        l
        i
        t
        e
        m
        s
        .
        Type `bool`. """
        
        self.information = None
        """ 
        D
        a
        t
        a
        t
        o
        b
        e
        p
        r
        o
        v
        i
        d
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        I
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
        i
        n
        s
        t
        a
        n
        c
        e
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
        Type `int`. """
        
        super(CoverageEligibilityRequestSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend([
            ("appliesToAll", "appliesToAll", bool, False, None, False),
            ("information", "information", fhirreference.FHIRReference, False, None, True),
            ("sequence", "sequence", int, False, None, True),
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
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
