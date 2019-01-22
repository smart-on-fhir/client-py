#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Claim) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Claim(domainresource.DomainResource):
    """ 
    C
    l
    a
    i
    m
    ,
    P
    r
    e
    -
    d
    e
    t
    e
    r
    m
    i
    n
    a
    t
    i
    o
    n
    o
    r
    P
    r
    e
    -
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
    .
    
    
    A
    p
    r
    o
    v
    i
    d
    e
    r
    i
    s
    s
    u
    e
    d
    l
    i
    s
    t
    o
    f
    p
    r
    o
    f
    e
    s
    s
    i
    o
    n
    a
    l
    s
    e
    r
    v
    i
    c
    e
    s
    a
    n
    d
    p
    r
    o
    d
    u
    c
    t
    s
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
    p
    r
    o
    v
    i
    d
    e
    d
    ,
    o
    r
    a
    r
    e
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
    ,
    t
    o
    a
    p
    a
    t
    i
    e
    n
    t
    w
    h
    i
    c
    h
    i
    s
    s
    e
    n
    t
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
    .
    
    """
    
    resource_type = "Claim"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accident = None
        """ 
        D
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
        e
        v
        e
        n
        t
        .
        Type `ClaimAccident` (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        """ 
        R
        e
        l
        e
        v
        a
        n
        t
        t
        i
        m
        e
        f
        r
        a
        m
        e
        f
        o
        r
        t
        h
        e
        c
        l
        a
        i
        m
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ 
        M
        e
        m
        b
        e
        r
        s
        o
        f
        t
        h
        e
        c
        a
        r
        e
        t
        e
        a
        m
        .
        List of `ClaimCareTeam` items (represented as `dict` in JSON). """
        
        self.created = None
        """ 
        R
        e
        s
        o
        u
        r
        c
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
        
        self.diagnosis = None
        """ 
        P
        e
        r
        t
        i
        n
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
        List of `ClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.enterer = None
        """ 
        A
        u
        t
        h
        o
        r
        o
        f
        t
        h
        e
        c
        l
        a
        i
        m
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
        
        self.fundsReserve = None
        """ 
        F
        o
        r
        w
        h
        o
        m
        t
        o
        r
        e
        s
        e
        r
        v
        e
        f
        u
        n
        d
        s
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
        l
        a
        i
        m
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
        List of `ClaimInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ 
        T
        a
        r
        g
        e
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.item = None
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
        p
        r
        o
        v
        i
        d
        e
        d
        .
        List of `ClaimItem` items (represented as `dict` in JSON). """
        
        self.originalPrescription = None
        """ 
        O
        r
        i
        g
        i
        n
        a
        l
        p
        r
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
        i
        f
        s
        u
        p
        e
        r
        s
        e
        d
        e
        d
        b
        y
        f
        u
        l
        f
        i
        l
        l
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        T
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
        b
        e
        n
        e
        f
        i
        t
        s
        p
        a
        y
        a
        b
        l
        e
        .
        Type `ClaimPayee` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ 
        P
        r
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
        a
        u
        t
        h
        o
        r
        i
        z
        i
        n
        g
        s
        e
        r
        v
        i
        c
        e
        s
        a
        n
        d
        p
        r
        o
        d
        u
        c
        t
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
        u
        g
        e
        n
        c
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        p
        r
        o
        c
        e
        d
        u
        r
        e
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        List of `ClaimProcedure` items (represented as `dict` in JSON). """
        
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
        c
        l
        a
        i
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referral = None
        """ 
        T
        r
        e
        a
        t
        m
        e
        n
        t
        r
        e
        f
        e
        r
        r
        a
        l
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.related = None
        """ 
        P
        r
        i
        o
        r
        o
        r
        c
        o
        r
        o
        l
        l
        a
        r
        y
        c
        l
        a
        i
        m
        s
        .
        List of `ClaimRelated` items (represented as `dict` in JSON). """
        
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
        
        self.subType = None
        """ 
        M
        o
        r
        e
        g
        r
        a
        n
        u
        l
        a
        r
        c
        l
        a
        i
        m
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        List of `ClaimSupportingInfo` items (represented as `dict` in JSON). """
        
        self.total = None
        """ 
        T
        o
        t
        a
        l
        c
        l
        a
        i
        m
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
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
        r
        d
        i
        s
        c
        i
        p
        l
        i
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        """ 
        c
        l
        a
        i
        m
        |
        p
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
        |
        p
        r
        e
        d
        e
        t
        e
        r
        m
        i
        n
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(Claim, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Claim, self).elementProperties()
        js.extend([
            ("accident", "accident", ClaimAccident, False, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("careTeam", "careTeam", ClaimCareTeam, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("diagnosis", "diagnosis", ClaimDiagnosis, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("fundsReserve", "fundsReserve", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ClaimInsurance, True, None, True),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ClaimItem, True, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payee", "payee", ClaimPayee, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, True),
            ("procedure", "procedure", ClaimProcedure, True, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("related", "related", ClaimRelated, True, None, False),
            ("status", "status", str, False, None, True),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("supportingInfo", "supportingInfo", ClaimSupportingInfo, True, None, False),
            ("total", "total", money.Money, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


from . import backboneelement

class ClaimAccident(backboneelement.BackboneElement):
    """ 
    D
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
    e
    v
    e
    n
    t
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    o
    f
    a
    n
    a
    c
    c
    i
    d
    e
    n
    t
    w
    h
    i
    c
    h
    r
    e
    s
    u
    l
    t
    e
    d
    i
    n
    i
    n
    j
    u
    r
    i
    e
    s
    w
    h
    i
    c
    h
    r
    e
    q
    u
    i
    r
    e
    d
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
    l
    i
    s
    t
    e
    d
    i
    n
    t
    h
    e
    c
    l
    a
    i
    m
    .
    
    """
    
    resource_type = "ClaimAccident"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        i
        n
        c
        i
        d
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
        
        self.locationAddress = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
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
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        h
        e
        n
        a
        t
        u
        r
        e
        o
        f
        t
        h
        e
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
        
        super(ClaimAccident, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimAccident, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimCareTeam(backboneelement.BackboneElement):
    """ 
    M
    e
    m
    b
    e
    r
    s
    o
    f
    t
    h
    e
    c
    a
    r
    e
    t
    e
    a
    m
    .
    
    
    T
    h
    e
    m
    e
    m
    b
    e
    r
    s
    o
    f
    t
    h
    e
    t
    e
    a
    m
    w
    h
    o
    p
    r
    o
    v
    i
    d
    e
    d
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
    
    resource_type = "ClaimCareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.provider = None
        """ 
        P
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
        o
        r
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.qualification = None
        """ 
        P
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
        c
        r
        e
        d
        e
        n
        t
        i
        a
        l
        o
        r
        s
        p
        e
        c
        i
        a
        l
        i
        z
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        o
        r
        o
        f
        t
        h
        e
        l
        e
        a
        d
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
        Type `bool`. """
        
        self.role = None
        """ 
        F
        u
        n
        c
        t
        i
        o
        n
        w
        i
        t
        h
        i
        n
        t
        h
        e
        t
        e
        a
        m
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        O
        r
        d
        e
        r
        o
        f
        c
        a
        r
        e
        t
        e
        a
        m
        .
        Type `int`. """
        
        super(ClaimCareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimCareTeam, self).elementProperties()
        js.extend([
            ("provider", "provider", fhirreference.FHIRReference, False, None, True),
            ("qualification", "qualification", codeableconcept.CodeableConcept, False, None, False),
            ("responsible", "responsible", bool, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimDiagnosis(backboneelement.BackboneElement):
    """ 
    P
    e
    r
    t
    i
    n
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
    a
    b
    o
    u
    t
    d
    i
    a
    g
    n
    o
    s
    e
    s
    r
    e
    l
    e
    v
    a
    n
    t
    t
    o
    t
    h
    e
    c
    l
    a
    i
    m
    i
    t
    e
    m
    s
    .
    
    """
    
    resource_type = "ClaimDiagnosis"
    
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
        
        self.onAdmission = None
        """ 
        P
        r
        e
        s
        e
        n
        t
        o
        n
        a
        d
        m
        i
        s
        s
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.packageCode = None
        """ 
        P
        a
        c
        k
        a
        g
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
        
        self.sequence = None
        """ 
        D
        i
        a
        g
        n
        o
        s
        i
        s
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
        
        self.type = None
        """ 
        T
        i
        m
        i
        n
        g
        o
        r
        n
        a
        t
        u
        r
        e
        o
        f
        t
        h
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ClaimDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", True),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", True),
            ("onAdmission", "onAdmission", codeableconcept.CodeableConcept, False, None, False),
            ("packageCode", "packageCode", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ClaimInsurance(backboneelement.BackboneElement):
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
    s
    p
    e
    c
    i
    f
    i
    e
    d
    o
    n
    t
    h
    e
    c
    l
    a
    i
    m
    .
    
    """
    
    resource_type = "ClaimInsurance"
    
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
        
        self.claimResponse = None
        """ 
        A
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        r
        e
        s
        u
        l
        t
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        C
        o
        v
        e
        r
        a
        g
        e
        t
        o
        b
        e
        u
        s
        e
        d
        f
        o
        r
        a
        d
        j
        u
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `bool`. """
        
        self.identifier = None
        """ 
        P
        r
        e
        -
        a
        s
        s
        i
        g
        n
        e
        d
        C
        l
        a
        i
        m
        n
        u
        m
        b
        e
        r
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ 
        P
        r
        i
        o
        r
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
        n
        u
        m
        b
        e
        r
        .
        List of `str` items. """
        
        self.sequence = None
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
        
        super(ClaimInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimItem(backboneelement.BackboneElement):
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
    p
    r
    o
    v
    i
    d
    e
    d
    .
    
    
    A
    c
    l
    a
    i
    m
    l
    i
    n
    e
    .
    E
    i
    t
    h
    e
    r
    a
    s
    i
    m
    p
    l
    e
    p
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
    o
    r
    a
    '
    g
    r
    o
    u
    p
    '
    o
    f
    d
    e
    t
    a
    i
    l
    s
    w
    h
    i
    c
    h
    c
    a
    n
    e
    a
    c
    h
    b
    e
    a
    s
    i
    m
    p
    l
    e
    i
    t
    e
    m
    s
    o
    r
    g
    r
    o
    u
    p
    s
    o
    f
    s
    u
    b
    -
    d
    e
    t
    a
    i
    l
    s
    .
    
    """
    
    resource_type = "ClaimItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySite = None
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.careTeamSequence = None
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
        a
        r
        e
        T
        e
        a
        m
        m
        e
        m
        b
        e
        r
        s
        .
        List of `int` items. """
        
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
        p
        r
        o
        v
        i
        d
        e
        d
        .
        List of `ClaimItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisSequence = None
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
        e
        s
        .
        List of `int` items. """
        
        self.encounter = None
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
        s
        r
        e
        l
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
        b
        i
        l
        l
        e
        d
        i
        t
        e
        m
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.factor = None
        """ 
        P
        r
        i
        c
        e
        s
        c
        a
        l
        i
        n
        g
        f
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.informationSequence = None
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
        a
        n
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
        
        self.locationAddress = None
        """ 
        P
        l
        a
        c
        e
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        w
        h
        e
        r
        e
        p
        r
        o
        d
        u
        c
        t
        w
        a
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
        Type `Address` (represented as `dict` in JSON). """
        
        self.locationCodeableConcept = None
        """ 
        P
        l
        a
        c
        e
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        w
        h
        e
        r
        e
        p
        r
        o
        d
        u
        c
        t
        w
        a
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationReference = None
        """ 
        P
        l
        a
        c
        e
        o
        f
        s
        e
        r
        v
        i
        c
        e
        o
        r
        w
        h
        e
        r
        e
        p
        r
        o
        d
        u
        c
        t
        w
        a
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
        
        self.net = None
        """ 
        T
        o
        t
        a
        l
        i
        t
        e
        m
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.procedureSequence = None
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
        p
        r
        o
        c
        e
        d
        u
        r
        e
        s
        .
        List of `int` items. """
        
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
        
        self.programCode = None
        """ 
        P
        r
        o
        g
        r
        a
        m
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
        o
        r
        s
        e
        r
        v
        i
        c
        e
        i
        s
        p
        r
        o
        v
        i
        d
        e
        d
        u
        n
        d
        e
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        
        self.revenue = None
        """ 
        R
        e
        v
        e
        n
        u
        e
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
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        I
        t
        e
        m
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
        
        self.servicedDate = None
        """ 
        D
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
        o
        r
        p
        r
        o
        d
        u
        c
        t
        d
        e
        l
        i
        v
        e
        r
        y
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ 
        D
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
        o
        r
        p
        r
        o
        d
        u
        c
        t
        d
        e
        l
        i
        v
        e
        r
        y
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
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
        s
        u
        b
        -
        l
        o
        c
        a
        t
        i
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.udi = None
        """ 
        U
        n
        i
        q
        u
        e
        d
        e
        v
        i
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        
        super(ClaimItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("careTeamSequence", "careTeamSequence", int, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimItemDetail, True, None, False),
            ("diagnosisSequence", "diagnosisSequence", int, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("informationSequence", "informationSequence", int, True, None, False),
            ("locationAddress", "locationAddress", address.Address, False, "location", False),
            ("locationCodeableConcept", "locationCodeableConcept", codeableconcept.CodeableConcept, False, "location", False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, False, "location", False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("procedureSequence", "procedureSequence", int, True, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimItemDetail(backboneelement.BackboneElement):
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
    p
    r
    o
    v
    i
    d
    e
    d
    .
    
    
    A
    c
    l
    a
    i
    m
    d
    e
    t
    a
    i
    l
    l
    i
    n
    e
    .
    E
    i
    t
    h
    e
    r
    a
    s
    i
    m
    p
    l
    e
    (
    a
    p
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
    )
    o
    r
    a
    '
    g
    r
    o
    u
    p
    '
    o
    f
    s
    u
    b
    -
    d
    e
    t
    a
    i
    l
    s
    w
    h
    i
    c
    h
    a
    r
    e
    s
    i
    m
    p
    l
    e
    i
    t
    e
    m
    s
    .
    
    """
    
    resource_type = "ClaimItemDetail"
    
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
        
        self.factor = None
        """ 
        P
        r
        i
        c
        e
        s
        c
        a
        l
        i
        n
        g
        f
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.modifier = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        /
        P
        r
        o
        d
        u
        c
        t
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
        
        self.net = None
        """ 
        T
        o
        t
        a
        l
        i
        t
        e
        m
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
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
        
        self.programCode = None
        """ 
        P
        r
        o
        g
        r
        a
        m
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
        o
        r
        s
        e
        r
        v
        i
        c
        e
        i
        s
        p
        r
        o
        v
        i
        d
        e
        d
        u
        n
        d
        e
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        
        self.revenue = None
        """ 
        R
        e
        v
        e
        n
        u
        e
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
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        I
        t
        e
        m
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
        
        self.subDetail = None
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
        p
        r
        o
        v
        i
        d
        e
        d
        .
        List of `ClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.udi = None
        """ 
        U
        n
        i
        q
        u
        e
        d
        e
        v
        i
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        
        super(ClaimItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("subDetail", "subDetail", ClaimItemDetailSubDetail, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimItemDetailSubDetail(backboneelement.BackboneElement):
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
    p
    r
    o
    v
    i
    d
    e
    d
    .
    
    
    A
    c
    l
    a
    i
    m
    d
    e
    t
    a
    i
    l
    l
    i
    n
    e
    .
    E
    i
    t
    h
    e
    r
    a
    s
    i
    m
    p
    l
    e
    (
    a
    p
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
    )
    o
    r
    a
    '
    g
    r
    o
    u
    p
    '
    o
    f
    s
    u
    b
    -
    d
    e
    t
    a
    i
    l
    s
    w
    h
    i
    c
    h
    a
    r
    e
    s
    i
    m
    p
    l
    e
    i
    t
    e
    m
    s
    .
    
    """
    
    resource_type = "ClaimItemDetailSubDetail"
    
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
        
        self.factor = None
        """ 
        P
        r
        i
        c
        e
        s
        c
        a
        l
        i
        n
        g
        f
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.modifier = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        /
        P
        r
        o
        d
        u
        c
        t
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
        
        self.net = None
        """ 
        T
        o
        t
        a
        l
        i
        t
        e
        m
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
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
        
        self.programCode = None
        """ 
        P
        r
        o
        g
        r
        a
        m
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
        o
        r
        s
        e
        r
        v
        i
        c
        e
        i
        s
        p
        r
        o
        v
        i
        d
        e
        d
        u
        n
        d
        e
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        
        self.revenue = None
        """ 
        R
        e
        v
        e
        n
        u
        e
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
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        I
        t
        e
        m
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
        
        self.udi = None
        """ 
        U
        n
        i
        q
        u
        e
        d
        e
        v
        i
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        
        super(ClaimItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, True),
            ("programCode", "programCode", codeableconcept.CodeableConcept, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ClaimPayee(backboneelement.BackboneElement):
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
    b
    e
    n
    e
    f
    i
    t
    s
    p
    a
    y
    a
    b
    l
    e
    .
    
    
    T
    h
    e
    p
    a
    r
    t
    y
    t
    o
    b
    e
    r
    e
    i
    m
    b
    u
    r
    s
    e
    d
    f
    o
    r
    c
    o
    s
    t
    o
    f
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
    a
    c
    c
    o
    r
    d
    i
    n
    g
    t
    o
    t
    h
    e
    t
    e
    r
    m
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
    
    resource_type = "ClaimPayee"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
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
        r
        e
        c
        i
        p
        i
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimPayee, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimPayee, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ClaimProcedure(backboneelement.BackboneElement):
    """ 
    C
    l
    i
    n
    i
    c
    a
    l
    p
    r
    o
    c
    e
    d
    u
    r
    e
    s
    p
    e
    r
    f
    o
    r
    m
    e
    d
    .
    
    
    P
    r
    o
    c
    e
    d
    u
    r
    e
    s
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
    n
    t
    h
    e
    p
    a
    t
    i
    e
    n
    t
    r
    e
    l
    e
    v
    a
    n
    t
    t
    o
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
    i
    t
    e
    m
    s
    w
    i
    t
    h
    t
    h
    e
    c
    l
    a
    i
    m
    .
    
    """
    
    resource_type = "ClaimProcedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
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
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.procedureCodeableConcept = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        c
        l
        i
        n
        i
        c
        a
        l
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.procedureReference = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        c
        l
        i
        n
        i
        c
        a
        l
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        P
        r
        o
        c
        e
        d
        u
        r
        e
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
        P
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.udi = None
        """ 
        U
        n
        i
        q
        u
        e
        d
        e
        v
        i
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(ClaimProcedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimProcedure, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("procedureCodeableConcept", "procedureCodeableConcept", codeableconcept.CodeableConcept, False, "procedure", True),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, "procedure", True),
            ("sequence", "sequence", int, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("udi", "udi", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ClaimRelated(backboneelement.BackboneElement):
    """ 
    P
    r
    i
    o
    r
    o
    r
    c
    o
    r
    o
    l
    l
    a
    r
    y
    c
    l
    a
    i
    m
    s
    .
    
    
    O
    t
    h
    e
    r
    c
    l
    a
    i
    m
    s
    w
    h
    i
    c
    h
    a
    r
    e
    r
    e
    l
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
    c
    l
    a
    i
    m
    s
    u
    c
    h
    a
    s
    p
    r
    i
    o
    r
    s
    u
    b
    m
    i
    s
    s
    i
    o
    n
    s
    o
    r
    c
    l
    a
    i
    m
    s
    f
    o
    r
    r
    e
    l
    a
    t
    e
    d
    s
    e
    r
    v
    i
    c
    e
    s
    o
    r
    f
    o
    r
    t
    h
    e
    s
    a
    m
    e
    e
    v
    e
    n
    t
    .
    
    """
    
    resource_type = "ClaimRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.claim = None
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
        t
        h
        e
        r
        e
        l
        a
        t
        e
        d
        c
        l
        a
        i
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reference = None
        """ 
        F
        i
        l
        e
        o
        r
        c
        a
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
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        H
        o
        w
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
        c
        l
        a
        i
        m
        i
        s
        r
        e
        l
        a
        t
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimRelated, self).elementProperties()
        js.extend([
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", identifier.Identifier, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimSupportingInfo(backboneelement.BackboneElement):
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
    
    resource_type = "ClaimSupportingInfo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ 
        C
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
        i
        e
        d
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
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
        f
        o
        r
        t
        h
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        
        self.timingDate = None
        """ 
        W
        h
        e
        n
        i
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
        
        self.timingPeriod = None
        """ 
        W
        h
        e
        n
        i
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
        
        self.valueAttachment = None
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
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
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
        Type `bool`. """
        
        self.valueQuantity = None
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
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
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
        
        self.valueString = None
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
        Type `str`. """
        
        super(ClaimSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimSupportingInfo, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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
