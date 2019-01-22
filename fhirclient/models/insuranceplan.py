#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/InsurancePlan) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class InsurancePlan(domainresource.DomainResource):
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
    a
    H
    e
    a
    l
    t
    h
    I
    n
    s
    u
    r
    a
    n
    c
    e
    p
    r
    o
    d
    u
    c
    t
    /
    p
    l
    a
    n
    p
    r
    o
    v
    i
    d
    e
    d
    b
    y
    a
    n
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
    """
    
    resource_type = "InsurancePlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administeredBy = None
        """ 
        P
        r
        o
        d
        u
        c
        t
        a
        d
        m
        i
        n
        i
        s
        t
        r
        a
        t
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.alias = None
        """ 
        A
        l
        t
        e
        r
        n
        a
        t
        e
        n
        a
        m
        e
        s
        .
        List of `str` items. """
        
        self.contact = None
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
        p
        r
        o
        d
        u
        c
        t
        .
        List of `InsurancePlanContact` items (represented as `dict` in JSON). """
        
        self.coverage = None
        """ 
        C
        o
        v
        e
        r
        a
        g
        e
        d
        e
        t
        a
        i
        l
        s
        .
        List of `InsurancePlanCoverage` items (represented as `dict` in JSON). """
        
        self.coverageArea = None
        """ 
        W
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
        a
        p
        p
        l
        i
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ 
        T
        e
        c
        h
        n
        i
        c
        a
        l
        e
        n
        d
        p
        o
        i
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        P
        r
        o
        d
        u
        c
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        O
        f
        f
        i
        c
        i
        a
        l
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.network = None
        """ 
        W
        h
        a
        t
        n
        e
        t
        w
        o
        r
        k
        s
        a
        r
        e
        I
        n
        c
        l
        u
        d
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.ownedBy = None
        """ 
        P
        l
        a
        n
        i
        s
        s
        u
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
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
        d
        u
        c
        t
        i
        s
        a
        v
        a
        i
        l
        a
        b
        l
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.plan = None
        """ 
        P
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
        .
        List of `InsurancePlanPlan` items (represented as `dict` in JSON). """
        
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
        r
        e
        t
        i
        r
        e
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
        
        self.type = None
        """ 
        K
        i
        n
        d
        o
        f
        p
        r
        o
        d
        u
        c
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(InsurancePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlan, self).elementProperties()
        js.extend([
            ("administeredBy", "administeredBy", fhirreference.FHIRReference, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", InsurancePlanContact, True, None, False),
            ("coverage", "coverage", InsurancePlanCoverage, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("ownedBy", "ownedBy", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("plan", "plan", InsurancePlanPlan, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class InsurancePlanContact(backboneelement.BackboneElement):
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
    p
    r
    o
    d
    u
    c
    t
    .
    
    
    T
    h
    e
    c
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
    h
    e
    a
    l
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
    p
    r
    o
    d
    u
    c
    t
    f
    o
    r
    a
    c
    e
    r
    t
    a
    i
    n
    p
    u
    r
    p
    o
    s
    e
    .
    
    """
    
    resource_type = "InsurancePlanContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ 
        V
        i
        s
        i
        t
        i
        n
        g
        o
        r
        p
        o
        s
        t
        a
        l
        a
        d
        d
        r
        e
        s
        s
        e
        s
        f
        o
        r
        t
        h
        e
        c
        o
        n
        t
        a
        c
        t
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        A
        n
        a
        m
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
        c
        o
        n
        t
        a
        c
        t
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.purpose = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        c
        o
        n
        t
        a
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ 
        C
        o
        n
        t
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
        (
        t
        e
        l
        e
        p
        h
        o
        n
        e
        ,
        e
        m
        a
        i
        l
        ,
        e
        t
        c
        .
        )
        f
        o
        r
        a
        c
        o
        n
        t
        a
        c
        t
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(InsurancePlanContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class InsurancePlanCoverage(backboneelement.BackboneElement):
    """ 
    C
    o
    v
    e
    r
    a
    g
    e
    d
    e
    t
    a
    i
    l
    s
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    a
    b
    o
    u
    t
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
    o
    f
    f
    e
    r
    e
    d
    b
    y
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
    p
    r
    o
    d
    u
    c
    t
    .
    
    """
    
    resource_type = "InsurancePlanCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit = None
        """ 
        L
        i
        s
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
        .
        List of `InsurancePlanCoverageBenefit` items (represented as `dict` in JSON). """
        
        self.network = None
        """ 
        W
        h
        a
        t
        n
        e
        t
        w
        o
        r
        k
        s
        p
        r
        o
        v
        i
        d
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        c
        o
        v
        e
        r
        a
        g
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanCoverage, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanCoverageBenefit, True, None, True),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanCoverageBenefit(backboneelement.BackboneElement):
    """ 
    L
    i
    s
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
    .
    
    
    S
    p
    e
    c
    i
    f
    i
    c
    b
    e
    n
    e
    f
    i
    t
    s
    u
    n
    d
    e
    r
    t
    h
    i
    s
    t
    y
    p
    e
    o
    f
    c
    o
    v
    e
    r
    a
    g
    e
    .
    
    """
    
    resource_type = "InsurancePlanCoverageBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.limit = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        l
        i
        m
        i
        t
        s
        .
        List of `InsurancePlanCoverageBenefitLimit` items (represented as `dict` in JSON). """
        
        self.requirement = None
        """ 
        R
        e
        f
        e
        r
        r
        a
        l
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
        b
        e
        n
        e
        f
        i
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanCoverageBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefit, self).elementProperties()
        js.extend([
            ("limit", "limit", InsurancePlanCoverageBenefitLimit, True, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanCoverageBenefitLimit(backboneelement.BackboneElement):
    """ 
    B
    e
    n
    e
    f
    i
    t
    l
    i
    m
    i
    t
    s
    .
    
    
    T
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
    l
    i
    m
    i
    t
    s
    o
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
    .
    
    """
    
    resource_type = "InsurancePlanCoverageBenefitLimit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        l
        i
        m
        i
        t
        d
        e
        t
        a
        i
        l
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        v
        a
        l
        u
        e
        a
        l
        l
        o
        w
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(InsurancePlanCoverageBenefitLimit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefitLimit, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", quantity.Quantity, False, None, False),
        ])
        return js


class InsurancePlanPlan(backboneelement.BackboneElement):
    """ 
    P
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
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    a
    b
    o
    u
    t
    a
    n
    i
    n
    s
    u
    r
    a
    n
    c
    e
    p
    l
    a
    n
    .
    
    """
    
    resource_type = "InsurancePlanPlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverageArea = None
        """ 
        W
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
        a
        p
        p
        l
        i
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.generalCost = None
        """ 
        O
        v
        e
        r
        a
        l
        l
        c
        o
        s
        t
        s
        .
        List of `InsurancePlanPlanGeneralCost` items (represented as `dict` in JSON). """
        
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
        P
        r
        o
        d
        u
        c
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.network = None
        """ 
        W
        h
        a
        t
        n
        e
        t
        w
        o
        r
        k
        s
        p
        r
        o
        v
        i
        d
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.specificCost = None
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
        o
        s
        t
        s
        .
        List of `InsurancePlanPlanSpecificCost` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        p
        l
        a
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlan, self).elementProperties()
        js.extend([
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("generalCost", "generalCost", InsurancePlanPlanGeneralCost, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("specificCost", "specificCost", InsurancePlanPlanSpecificCost, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class InsurancePlanPlanGeneralCost(backboneelement.BackboneElement):
    """ 
    O
    v
    e
    r
    a
    l
    l
    c
    o
    s
    t
    s
    .
    
    
    O
    v
    e
    r
    a
    l
    l
    c
    o
    s
    t
    s
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
    p
    l
    a
    n
    .
    
    """
    
    resource_type = "InsurancePlanPlanGeneralCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
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
        s
        t
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
        Type `str`. """
        
        self.cost = None
        """ 
        C
        o
        s
        t
        v
        a
        l
        u
        e
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.groupSize = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        e
        n
        r
        o
        l
        l
        e
        e
        s
        .
        Type `int`. """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        c
        o
        s
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanGeneralCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanGeneralCost, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("cost", "cost", money.Money, False, None, False),
            ("groupSize", "groupSize", int, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class InsurancePlanPlanSpecificCost(backboneelement.BackboneElement):
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
    o
    s
    t
    s
    .
    
    
    C
    o
    s
    t
    s
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
    c
    o
    v
    e
    r
    a
    g
    e
    p
    r
    o
    v
    i
    d
    e
    d
    b
    y
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
    .
    
    """
    
    resource_type = "InsurancePlanPlanSpecificCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit = None
        """ 
        B
        e
        n
        e
        f
        i
        t
        s
        l
        i
        s
        t
        .
        List of `InsurancePlanPlanSpecificCostBenefit` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        G
        e
        n
        e
        r
        a
        l
        c
        a
        t
        e
        g
        o
        r
        y
        o
        f
        b
        e
        n
        e
        f
        i
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanSpecificCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCost, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanPlanSpecificCostBenefit, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanPlanSpecificCostBenefit(backboneelement.BackboneElement):
    """ 
    B
    e
    n
    e
    f
    i
    t
    s
    l
    i
    s
    t
    .
    
    
    L
    i
    s
    t
    o
    f
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
    b
    e
    n
    e
    f
    i
    t
    s
    u
    n
    d
    e
    r
    t
    h
    i
    s
    c
    a
    t
    e
    g
    o
    r
    y
    o
    f
    b
    e
    n
    e
    f
    i
    t
    .
    
    """
    
    resource_type = "InsurancePlanPlanSpecificCostBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cost = None
        """ 
        L
        i
        s
        t
        o
        f
        t
        h
        e
        c
        o
        s
        t
        s
        .
        List of `InsurancePlanPlanSpecificCostBenefitCost` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        s
        p
        e
        c
        i
        f
        i
        c
        b
        e
        n
        e
        f
        i
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanSpecificCostBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefit, self).elementProperties()
        js.extend([
            ("cost", "cost", InsurancePlanPlanSpecificCostBenefitCost, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class InsurancePlanPlanSpecificCostBenefitCost(backboneelement.BackboneElement):
    """ 
    L
    i
    s
    t
    o
    f
    t
    h
    e
    c
    o
    s
    t
    s
    .
    
    
    L
    i
    s
    t
    o
    f
    t
    h
    e
    c
    o
    s
    t
    s
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
    a
    s
    p
    e
    c
    i
    f
    i
    c
    b
    e
    n
    e
    f
    i
    t
    .
    
    """
    
    resource_type = "InsurancePlanPlanSpecificCostBenefitCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
        """ 
        i
        n
        -
        n
        e
        t
        w
        o
        r
        k
        |
        o
        u
        t
        -
        o
        f
        -
        n
        e
        t
        w
        o
        r
        k
        |
        o
        t
        h
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.qualifiers = None
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
        b
        o
        u
        t
        t
        h
        e
        c
        o
        s
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        c
        o
        s
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        T
        h
        e
        a
        c
        t
        u
        a
        l
        c
        o
        s
        t
        v
        a
        l
        u
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(InsurancePlanPlanSpecificCostBenefitCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefitCost, self).elementProperties()
        js.extend([
            ("applicability", "applicability", codeableconcept.CodeableConcept, False, None, False),
            ("qualifiers", "qualifiers", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
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
