#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/NutritionOrder) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class NutritionOrder(domainresource.DomainResource):
    """ 
    D
    i
    e
    t
    ,
    f
    o
    r
    m
    u
    l
    a
    o
    r
    n
    u
    t
    r
    i
    t
    i
    o
    n
    a
    l
    s
    u
    p
    p
    l
    e
    m
    e
    n
    t
    r
    e
    q
    u
    e
    s
    t
    .
    
    
    A
    r
    e
    q
    u
    e
    s
    t
    t
    o
    s
    u
    p
    p
    l
    y
    a
    d
    i
    e
    t
    ,
    f
    o
    r
    m
    u
    l
    a
    f
    e
    e
    d
    i
    n
    g
    (
    e
    n
    t
    e
    r
    a
    l
    )
    o
    r
    o
    r
    a
    l
    n
    u
    t
    r
    i
    t
    i
    o
    n
    a
    l
    s
    u
    p
    p
    l
    e
    m
    e
    n
    t
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
    /
    r
    e
    s
    i
    d
    e
    n
    t
    .
    
    """
    
    resource_type = "NutritionOrder"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergyIntolerance = None
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
        p
        a
        t
        i
        e
        n
        t
        '
        s
        f
        o
        o
        d
        a
        n
        d
        n
        u
        t
        r
        i
        t
        i
        o
        n
        -
        r
        e
        l
        a
        t
        e
        d
        a
        l
        l
        e
        r
        g
        i
        e
        s
        a
        n
        d
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ 
        D
        a
        t
        e
        a
        n
        d
        t
        i
        m
        e
        t
        h
        e
        n
        u
        t
        r
        i
        t
        i
        o
        n
        o
        r
        d
        e
        r
        w
        a
        s
        r
        e
        q
        u
        e
        s
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ 
        T
        h
        e
        e
        n
        c
        o
        u
        n
        t
        e
        r
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
        n
        u
        t
        r
        i
        t
        i
        o
        n
        o
        r
        d
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.enteralFormula = None
        """ 
        E
        n
        t
        e
        r
        a
        l
        f
        o
        r
        m
        u
        l
        a
        c
        o
        m
        p
        o
        n
        e
        n
        t
        s
        .
        Type `NutritionOrderEnteralFormula` (represented as `dict` in JSON). """
        
        self.excludeFoodModifier = None
        """ 
        O
        r
        d
        e
        r
        -
        s
        p
        e
        c
        i
        f
        i
        c
        m
        o
        d
        i
        f
        i
        e
        r
        a
        b
        o
        u
        t
        t
        h
        e
        t
        y
        p
        e
        o
        f
        f
        o
        o
        d
        t
        h
        a
        t
        s
        h
        o
        u
        l
        d
        n
        o
        t
        b
        e
        g
        i
        v
        e
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.foodPreferenceModifier = None
        """ 
        O
        r
        d
        e
        r
        -
        s
        p
        e
        c
        i
        f
        i
        c
        m
        o
        d
        i
        f
        i
        e
        r
        a
        b
        o
        u
        t
        t
        h
        e
        t
        y
        p
        e
        o
        f
        f
        o
        o
        d
        t
        h
        a
        t
        s
        h
        o
        u
        l
        d
        b
        e
        g
        i
        v
        e
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
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
        s
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
        i
        s
        o
        r
        d
        e
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiates = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        List of `str` items. """
        
        self.instantiatesCanonical = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        F
        H
        I
        R
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        List of `str` items. """
        
        self.instantiatesUri = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        e
        x
        t
        e
        r
        n
        a
        l
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
        d
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        List of `str` items. """
        
        self.intent = None
        """ 
        p
        r
        o
        p
        o
        s
        a
        l
        |
        p
        l
        a
        n
        |
        o
        r
        d
        e
        r
        .
        Type `str`. """
        
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
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.oralDiet = None
        """ 
        O
        r
        a
        l
        d
        i
        e
        t
        c
        o
        m
        p
        o
        n
        e
        n
        t
        s
        .
        Type `NutritionOrderOralDiet` (represented as `dict` in JSON). """
        
        self.orderer = None
        """ 
        W
        h
        o
        o
        r
        d
        e
        r
        e
        d
        t
        h
        e
        d
        i
        e
        t
        ,
        f
        o
        r
        m
        u
        l
        a
        o
        r
        n
        u
        t
        r
        i
        t
        i
        o
        n
        a
        l
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        T
        h
        e
        p
        e
        r
        s
        o
        n
        w
        h
        o
        r
        e
        q
        u
        i
        r
        e
        s
        t
        h
        e
        d
        i
        e
        t
        ,
        f
        o
        r
        m
        u
        l
        a
        o
        r
        n
        u
        t
        r
        i
        t
        i
        o
        n
        a
        l
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        p
        r
        o
        p
        o
        s
        e
        d
        |
        d
        r
        a
        f
        t
        |
        p
        l
        a
        n
        n
        e
        d
        |
        r
        e
        q
        u
        e
        s
        t
        e
        d
        |
        a
        c
        t
        i
        v
        e
        |
        o
        n
        -
        h
        o
        l
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
        
        self.supplement = None
        """ 
        S
        u
        p
        p
        l
        e
        m
        e
        n
        t
        c
        o
        m
        p
        o
        n
        e
        n
        t
        s
        .
        List of `NutritionOrderSupplement` items (represented as `dict` in JSON). """
        
        super(NutritionOrder, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrder, self).elementProperties()
        js.extend([
            ("allergyIntolerance", "allergyIntolerance", fhirreference.FHIRReference, True, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("enteralFormula", "enteralFormula", NutritionOrderEnteralFormula, False, None, False),
            ("excludeFoodModifier", "excludeFoodModifier", codeableconcept.CodeableConcept, True, None, False),
            ("foodPreferenceModifier", "foodPreferenceModifier", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("oralDiet", "oralDiet", NutritionOrderOralDiet, False, None, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
            ("supplement", "supplement", NutritionOrderSupplement, True, None, False),
        ])
        return js


from . import backboneelement

class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    """ 
    E
    n
    t
    e
    r
    a
    l
    f
    o
    r
    m
    u
    l
    a
    c
    o
    m
    p
    o
    n
    e
    n
    t
    s
    .
    
    
    F
    e
    e
    d
    i
    n
    g
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
    r
    o
    u
    g
    h
    t
    h
    e
    g
    a
    s
    t
    r
    o
    i
    n
    t
    e
    s
    t
    i
    n
    a
    l
    t
    r
    a
    c
    t
    v
    i
    a
    a
    t
    u
    b
    e
    ,
    c
    a
    t
    h
    e
    t
    e
    r
    ,
    o
    r
    s
    t
    o
    m
    a
    t
    h
    a
    t
    d
    e
    l
    i
    v
    e
    r
    s
    n
    u
    t
    r
    i
    t
    i
    o
    n
    d
    i
    s
    t
    a
    l
    t
    o
    t
    h
    e
    o
    r
    a
    l
    c
    a
    v
    i
    t
    y
    .
    
    """
    
    resource_type = "NutritionOrderEnteralFormula"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveProductName = None
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
        b
        r
        a
        n
        d
        n
        a
        m
        e
        o
        f
        t
        h
        e
        m
        o
        d
        u
        l
        a
        r
        a
        d
        d
        i
        t
        i
        v
        e
        .
        Type `str`. """
        
        self.additiveType = None
        """ 
        T
        y
        p
        e
        o
        f
        m
        o
        d
        u
        l
        a
        r
        c
        o
        m
        p
        o
        n
        e
        n
        t
        t
        o
        a
        d
        d
        t
        o
        t
        h
        e
        f
        e
        e
        d
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.administration = None
        """ 
        F
        o
        r
        m
        u
        l
        a
        f
        e
        e
        d
        i
        n
        g
        i
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        a
        s
        s
        t
        r
        u
        c
        t
        u
        r
        e
        d
        d
        a
        t
        a
        .
        List of `NutritionOrderEnteralFormulaAdministration` items (represented as `dict` in JSON). """
        
        self.administrationInstruction = None
        """ 
        F
        o
        r
        m
        u
        l
        a
        f
        e
        e
        d
        i
        n
        g
        i
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        s
        e
        x
        p
        r
        e
        s
        s
        e
        d
        a
        s
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.baseFormulaProductName = None
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
        b
        r
        a
        n
        d
        n
        a
        m
        e
        o
        f
        t
        h
        e
        e
        n
        t
        e
        r
        a
        l
        o
        r
        i
        n
        f
        a
        n
        t
        f
        o
        r
        m
        u
        l
        a
        .
        Type `str`. """
        
        self.baseFormulaType = None
        """ 
        T
        y
        p
        e
        o
        f
        e
        n
        t
        e
        r
        a
        l
        o
        r
        i
        n
        f
        a
        n
        t
        f
        o
        r
        m
        u
        l
        a
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.caloricDensity = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
        e
        n
        e
        r
        g
        y
        p
        e
        r
        s
        p
        e
        c
        i
        f
        i
        e
        d
        v
        o
        l
        u
        m
        e
        t
        h
        a
        t
        i
        s
        r
        e
        q
        u
        i
        r
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxVolumeToDeliver = None
        """ 
        U
        p
        p
        e
        r
        l
        i
        m
        i
        t
        o
        n
        f
        o
        r
        m
        u
        l
        a
        v
        o
        l
        u
        m
        e
        p
        e
        r
        u
        n
        i
        t
        o
        f
        t
        i
        m
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.routeofAdministration = None
        """ 
        H
        o
        w
        t
        h
        e
        f
        o
        r
        m
        u
        l
        a
        s
        h
        o
        u
        l
        d
        e
        n
        t
        e
        r
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
        '
        s
        g
        a
        s
        t
        r
        o
        i
        n
        t
        e
        s
        t
        i
        n
        a
        l
        t
        r
        a
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderEnteralFormula, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderEnteralFormula, self).elementProperties()
        js.extend([
            ("additiveProductName", "additiveProductName", str, False, None, False),
            ("additiveType", "additiveType", codeableconcept.CodeableConcept, False, None, False),
            ("administration", "administration", NutritionOrderEnteralFormulaAdministration, True, None, False),
            ("administrationInstruction", "administrationInstruction", str, False, None, False),
            ("baseFormulaProductName", "baseFormulaProductName", str, False, None, False),
            ("baseFormulaType", "baseFormulaType", codeableconcept.CodeableConcept, False, None, False),
            ("caloricDensity", "caloricDensity", quantity.Quantity, False, None, False),
            ("maxVolumeToDeliver", "maxVolumeToDeliver", quantity.Quantity, False, None, False),
            ("routeofAdministration", "routeofAdministration", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    """ 
    F
    o
    r
    m
    u
    l
    a
    f
    e
    e
    d
    i
    n
    g
    i
    n
    s
    t
    r
    u
    c
    t
    i
    o
    n
    a
    s
    s
    t
    r
    u
    c
    t
    u
    r
    e
    d
    d
    a
    t
    a
    .
    
    
    F
    o
    r
    m
    u
    l
    a
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
    i
    o
    n
    i
    n
    s
    t
    r
    u
    c
    t
    i
    o
    n
    s
    a
    s
    s
    t
    r
    u
    c
    t
    u
    r
    e
    d
    d
    a
    t
    a
    .
    T
    h
    i
    s
    r
    e
    p
    e
    a
    t
    i
    n
    g
    s
    t
    r
    u
    c
    t
    u
    r
    e
    a
    l
    l
    o
    w
    s
    f
    o
    r
    c
    h
    a
    n
    g
    i
    n
    g
    t
    h
    e
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
    i
    o
    n
    r
    a
    t
    e
    o
    r
    v
    o
    l
    u
    m
    e
    o
    v
    e
    r
    t
    i
    m
    e
    f
    o
    r
    b
    o
    t
    h
    b
    o
    l
    u
    s
    a
    n
    d
    c
    o
    n
    t
    i
    n
    u
    o
    u
    s
    f
    e
    e
    d
    i
    n
    g
    .
    A
    n
    e
    x
    a
    m
    p
    l
    e
    o
    f
    t
    h
    i
    s
    w
    o
    u
    l
    d
    b
    e
    a
    n
    i
    n
    s
    t
    r
    u
    c
    t
    i
    o
    n
    t
    o
    i
    n
    c
    r
    e
    a
    s
    e
    t
    h
    e
    r
    a
    t
    e
    o
    f
    c
    o
    n
    t
    i
    n
    u
    o
    u
    s
    f
    e
    e
    d
    i
    n
    g
    e
    v
    e
    r
    y
    2
    h
    o
    u
    r
    s
    .
    
    """
    
    resource_type = "NutritionOrderEnteralFormulaAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None
        """ 
        T
        h
        e
        v
        o
        l
        u
        m
        e
        o
        f
        f
        o
        r
        m
        u
        l
        a
        t
        o
        p
        r
        o
        v
        i
        d
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ 
        S
        p
        e
        e
        d
        w
        i
        t
        h
        w
        h
        i
        c
        h
        t
        h
        e
        f
        o
        r
        m
        u
        l
        a
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
        p
        e
        r
        p
        e
        r
        i
        o
        d
        o
        f
        t
        i
        m
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ 
        S
        p
        e
        e
        d
        w
        i
        t
        h
        w
        h
        i
        c
        h
        t
        h
        e
        f
        o
        r
        m
        u
        l
        a
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
        p
        e
        r
        p
        e
        r
        i
        o
        d
        o
        f
        t
        i
        m
        e
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ 
        S
        c
        h
        e
        d
        u
        l
        e
        d
        f
        r
        e
        q
        u
        e
        n
        c
        y
        o
        f
        e
        n
        t
        e
        r
        a
        l
        f
        e
        e
        d
        i
        n
        g
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        super(NutritionOrderEnteralFormulaAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderEnteralFormulaAdministration, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("schedule", "schedule", timing.Timing, False, None, False),
        ])
        return js


class NutritionOrderOralDiet(backboneelement.BackboneElement):
    """ 
    O
    r
    a
    l
    d
    i
    e
    t
    c
    o
    m
    p
    o
    n
    e
    n
    t
    s
    .
    
    
    D
    i
    e
    t
    g
    i
    v
    e
    n
    o
    r
    a
    l
    l
    y
    i
    n
    c
    o
    n
    t
    r
    a
    s
    t
    t
    o
    e
    n
    t
    e
    r
    a
    l
    (
    t
    u
    b
    e
    )
    f
    e
    e
    d
    i
    n
    g
    .
    
    """
    
    resource_type = "NutritionOrderOralDiet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fluidConsistencyType = None
        """ 
        T
        h
        e
        r
        e
        q
        u
        i
        r
        e
        d
        c
        o
        n
        s
        i
        s
        t
        e
        n
        c
        y
        o
        f
        f
        l
        u
        i
        d
        s
        a
        n
        d
        l
        i
        q
        u
        i
        d
        s
        p
        r
        o
        v
        i
        d
        e
        d
        t
        o
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.instruction = None
        """ 
        I
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        s
        o
        r
        a
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
        o
        r
        a
        l
        d
        i
        e
        t
        .
        Type `str`. """
        
        self.nutrient = None
        """ 
        R
        e
        q
        u
        i
        r
        e
        d
        n
        u
        t
        r
        i
        e
        n
        t
        m
        o
        d
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
        List of `NutritionOrderOralDietNutrient` items (represented as `dict` in JSON). """
        
        self.schedule = None
        """ 
        S
        c
        h
        e
        d
        u
        l
        e
        d
        f
        r
        e
        q
        u
        e
        n
        c
        y
        o
        f
        d
        i
        e
        t
        .
        List of `Timing` items (represented as `dict` in JSON). """
        
        self.texture = None
        """ 
        R
        e
        q
        u
        i
        r
        e
        d
        t
        e
        x
        t
        u
        r
        e
        m
        o
        d
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
        List of `NutritionOrderOralDietTexture` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        o
        r
        a
        l
        d
        i
        e
        t
        o
        r
        d
        i
        e
        t
        r
        e
        s
        t
        r
        i
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
        d
        e
        s
        c
        r
        i
        b
        e
        w
        h
        a
        t
        c
        a
        n
        b
        e
        c
        o
        n
        s
        u
        m
        e
        d
        o
        r
        a
        l
        l
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(NutritionOrderOralDiet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDiet, self).elementProperties()
        js.extend([
            ("fluidConsistencyType", "fluidConsistencyType", codeableconcept.CodeableConcept, True, None, False),
            ("instruction", "instruction", str, False, None, False),
            ("nutrient", "nutrient", NutritionOrderOralDietNutrient, True, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("texture", "texture", NutritionOrderOralDietTexture, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    """ 
    R
    e
    q
    u
    i
    r
    e
    d
    n
    u
    t
    r
    i
    e
    n
    t
    m
    o
    d
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
    
    
    C
    l
    a
    s
    s
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
    q
    u
    a
    n
    t
    i
    t
    y
    a
    n
    d
    t
    y
    p
    e
    o
    f
    n
    u
    t
    r
    i
    e
    n
    t
    m
    o
    d
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
    (
    f
    o
    r
    e
    x
    a
    m
    p
    l
    e
    c
    a
    r
    b
    o
    h
    y
    d
    r
    a
    t
    e
    ,
    f
    i
    b
    e
    r
    o
    r
    s
    o
    d
    i
    u
    m
    )
    r
    e
    q
    u
    i
    r
    e
    d
    f
    o
    r
    t
    h
    e
    o
    r
    a
    l
    d
    i
    e
    t
    .
    
    """
    
    resource_type = "NutritionOrderOralDietNutrient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        y
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
        e
        d
        n
        u
        t
        r
        i
        e
        n
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ 
        T
        y
        p
        e
        o
        f
        n
        u
        t
        r
        i
        e
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
        m
        o
        d
        i
        f
        i
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderOralDietNutrient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDietNutrient, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    """ 
    R
    e
    q
    u
    i
    r
    e
    d
    t
    e
    x
    t
    u
    r
    e
    m
    o
    d
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
    
    
    C
    l
    a
    s
    s
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
    a
    n
    y
    t
    e
    x
    t
    u
    r
    e
    m
    o
    d
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
    r
    e
    q
    u
    i
    r
    e
    d
    f
    o
    r
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
    t
    o
    s
    a
    f
    e
    l
    y
    c
    o
    n
    s
    u
    m
    e
    v
    a
    r
    i
    o
    u
    s
    t
    y
    p
    e
    s
    o
    f
    s
    o
    l
    i
    d
    f
    o
    o
    d
    s
    .
    
    """
    
    resource_type = "NutritionOrderOralDietTexture"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.foodType = None
        """ 
        C
        o
        n
        c
        e
        p
        t
        s
        t
        h
        a
        t
        a
        r
        e
        u
        s
        e
        d
        t
        o
        i
        d
        e
        n
        t
        i
        f
        y
        a
        n
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
        i
        s
        i
        n
        g
        e
        s
        t
        e
        d
        f
        o
        r
        n
        u
        t
        r
        i
        t
        i
        o
        n
        a
        l
        p
        u
        r
        p
        o
        s
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ 
        C
        o
        d
        e
        t
        o
        i
        n
        d
        i
        c
        a
        t
        e
        h
        o
        w
        t
        o
        a
        l
        t
        e
        r
        t
        h
        e
        t
        e
        x
        t
        u
        r
        e
        o
        f
        t
        h
        e
        f
        o
        o
        d
        s
        ,
        e
        .
        g
        .
        p
        u
        r
        e
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderOralDietTexture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDietTexture, self).elementProperties()
        js.extend([
            ("foodType", "foodType", codeableconcept.CodeableConcept, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class NutritionOrderSupplement(backboneelement.BackboneElement):
    """ 
    S
    u
    p
    p
    l
    e
    m
    e
    n
    t
    c
    o
    m
    p
    o
    n
    e
    n
    t
    s
    .
    
    
    O
    r
    a
    l
    n
    u
    t
    r
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
    d
    u
    c
    t
    s
    g
    i
    v
    e
    n
    i
    n
    o
    r
    d
    e
    r
    t
    o
    a
    d
    d
    f
    u
    r
    t
    h
    e
    r
    n
    u
    t
    r
    i
    t
    i
    o
    n
    a
    l
    v
    a
    l
    u
    e
    t
    o
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
    '
    s
    d
    i
    e
    t
    .
    
    """
    
    resource_type = "NutritionOrderSupplement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instruction = None
        """ 
        I
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        s
        o
        r
        a
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
        o
        r
        a
        l
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.productName = None
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
        b
        r
        a
        n
        d
        n
        a
        m
        e
        o
        f
        t
        h
        e
        n
        u
        t
        r
        i
        t
        i
        o
        n
        a
        l
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.quantity = None
        """ 
        A
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
        n
        u
        t
        r
        i
        t
        i
        o
        n
        a
        l
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ 
        S
        c
        h
        e
        d
        u
        l
        e
        d
        f
        r
        e
        q
        u
        e
        n
        c
        y
        o
        f
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        .
        List of `Timing` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        s
        u
        p
        p
        l
        e
        m
        e
        n
        t
        p
        r
        o
        d
        u
        c
        t
        r
        e
        q
        u
        e
        s
        t
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderSupplement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderSupplement, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("productName", "productName", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
