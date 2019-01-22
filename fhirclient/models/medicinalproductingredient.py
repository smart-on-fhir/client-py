#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProductIngredient(domainresource.DomainResource):
    """ 
    A
    n
    i
    n
    g
    r
    e
    d
    i
    e
    n
    t
    o
    f
    a
    m
    a
    n
    u
    f
    a
    c
    t
    u
    r
    e
    d
    i
    t
    e
    m
    o
    r
    p
    h
    a
    r
    m
    a
    c
    e
    u
    t
    i
    c
    a
    l
    p
    r
    o
    d
    u
    c
    t
    .
    """
    
    resource_type = "MedicinalProductIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergenicIndicator = None
        """ 
        I
        f
        t
        h
        e
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        i
        s
        a
        k
        n
        o
        w
        n
        o
        r
        s
        u
        s
        p
        e
        c
        t
        e
        d
        a
        l
        l
        e
        r
        g
        e
        n
        .
        Type `bool`. """
        
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
        f
        o
        r
        t
        h
        e
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ 
        M
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        r
        o
        f
        t
        h
        i
        s
        I
        n
        g
        r
        e
        d
        i
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        I
        n
        g
        r
        e
        d
        i
        e
        n
        t
        r
        o
        l
        e
        e
        .
        g
        .
        A
        c
        t
        i
        v
        e
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        ,
        e
        x
        c
        i
        p
        i
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specifiedSubstance = None
        """ 
        A
        s
        p
        e
        c
        i
        f
        i
        e
        d
        s
        u
        b
        s
        t
        a
        n
        c
        e
        t
        h
        a
        t
        c
        o
        m
        p
        r
        i
        s
        e
        s
        t
        h
        i
        s
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        .
        List of `MedicinalProductIngredientSpecifiedSubstance` items (represented as `dict` in JSON). """
        
        self.substance = None
        """ 
        T
        h
        e
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `MedicinalProductIngredientSubstance` (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredient, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
            ("specifiedSubstance", "specifiedSubstance", MedicinalProductIngredientSpecifiedSubstance, True, None, False),
            ("substance", "substance", MedicinalProductIngredientSubstance, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductIngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """ 
    A
    s
    p
    e
    c
    i
    f
    i
    e
    d
    s
    u
    b
    s
    t
    a
    n
    c
    e
    t
    h
    a
    t
    c
    o
    m
    p
    r
    i
    s
    e
    s
    t
    h
    i
    s
    i
    n
    g
    r
    e
    d
    i
    e
    n
    t
    .
    """
    
    resource_type = "MedicinalProductIngredientSpecifiedSubstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
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
        e
        d
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.confidentiality = None
        """ 
        C
        o
        n
        f
        i
        d
        e
        n
        t
        i
        a
        l
        i
        t
        y
        l
        e
        v
        e
        l
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
        s
        u
        b
        s
        t
        a
        n
        c
        e
        a
        s
        t
        h
        e
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.group = None
        """ 
        T
        h
        e
        g
        r
        o
        u
        p
        o
        f
        s
        p
        e
        c
        i
        f
        i
        e
        d
        s
        u
        b
        s
        t
        a
        n
        c
        e
        ,
        e
        .
        g
        .
        g
        r
        o
        u
        p
        1
        t
        o
        4
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.strength = None
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
        u
        b
        s
        t
        a
        n
        c
        e
        o
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
        s
        u
        b
        s
        t
        a
        n
        c
        e
        p
        r
        e
        s
        e
        n
        t
        i
        n
        t
        h
        e
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        d
        i
        t
        e
        m
        o
        r
        p
        h
        a
        r
        m
        a
        c
        e
        u
        t
        i
        c
        a
        l
        p
        r
        o
        d
        u
        c
        t
        .
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSpecifiedSubstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("confidentiality", "confidentiality", codeableconcept.CodeableConcept, False, None, False),
            ("group", "group", codeableconcept.CodeableConcept, False, None, True),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
        ])
        return js


class MedicinalProductIngredientSpecifiedSubstanceStrength(backboneelement.BackboneElement):
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
    u
    b
    s
    t
    a
    n
    c
    e
    o
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
    s
    u
    b
    s
    t
    a
    n
    c
    e
    p
    r
    e
    s
    e
    n
    t
    i
    n
    t
    h
    e
    m
    a
    n
    u
    f
    a
    c
    t
    u
    r
    e
    d
    i
    t
    e
    m
    o
    r
    p
    h
    a
    r
    m
    a
    c
    e
    u
    t
    i
    c
    a
    l
    p
    r
    o
    d
    u
    c
    t
    .
    """
    
    resource_type = "MedicinalProductIngredientSpecifiedSubstanceStrength"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.concentration = None
        """ 
        T
        h
        e
        s
        t
        r
        e
        n
        g
        t
        h
        p
        e
        r
        u
        n
        i
        t
        a
        r
        y
        v
        o
        l
        u
        m
        e
        (
        o
        r
        m
        a
        s
        s
        )
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.concentrationLowLimit = None
        """ 
        A
        l
        o
        w
        e
        r
        l
        i
        m
        i
        t
        f
        o
        r
        t
        h
        e
        s
        t
        r
        e
        n
        g
        t
        h
        p
        e
        r
        u
        n
        i
        t
        a
        r
        y
        v
        o
        l
        u
        m
        e
        (
        o
        r
        m
        a
        s
        s
        )
        ,
        f
        o
        r
        w
        h
        e
        n
        t
        h
        e
        r
        e
        i
        s
        a
        r
        a
        n
        g
        e
        .
        T
        h
        e
        c
        o
        n
        c
        e
        n
        t
        r
        a
        t
        i
        o
        n
        a
        t
        t
        r
        i
        b
        u
        t
        e
        t
        h
        e
        n
        b
        e
        c
        o
        m
        e
        s
        t
        h
        e
        u
        p
        p
        e
        r
        l
        i
        m
        i
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.country = None
        """ 
        T
        h
        e
        c
        o
        u
        n
        t
        r
        y
        o
        r
        c
        o
        u
        n
        t
        r
        i
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
        t
        h
        e
        s
        t
        r
        e
        n
        g
        t
        h
        r
        a
        n
        g
        e
        a
        p
        p
        l
        i
        e
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.measurementPoint = None
        """ 
        F
        o
        r
        w
        h
        e
        n
        s
        t
        r
        e
        n
        g
        t
        h
        i
        s
        m
        e
        a
        s
        u
        r
        e
        d
        a
        t
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
        o
        i
        n
        t
        o
        r
        d
        i
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.presentation = None
        """ 
        T
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
        o
        f
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        n
        t
        h
        e
        u
        n
        i
        t
        o
        f
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        ,
        o
        r
        i
        n
        t
        h
        e
        v
        o
        l
        u
        m
        e
        (
        o
        r
        m
        a
        s
        s
        )
        o
        f
        t
        h
        e
        s
        i
        n
        g
        l
        e
        p
        h
        a
        r
        m
        a
        c
        e
        u
        t
        i
        c
        a
        l
        p
        r
        o
        d
        u
        c
        t
        o
        r
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        d
        i
        t
        e
        m
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.presentationLowLimit = None
        """ 
        A
        l
        o
        w
        e
        r
        l
        i
        m
        i
        t
        f
        o
        r
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
        o
        f
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        n
        t
        h
        e
        u
        n
        i
        t
        o
        f
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        .
        F
        o
        r
        u
        s
        e
        w
        h
        e
        n
        t
        h
        e
        r
        e
        i
        s
        a
        r
        a
        n
        g
        e
        o
        f
        s
        t
        r
        e
        n
        g
        t
        h
        s
        ,
        t
        h
        i
        s
        i
        s
        t
        h
        e
        l
        o
        w
        e
        r
        l
        i
        m
        i
        t
        ,
        w
        i
        t
        h
        t
        h
        e
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        a
        t
        t
        r
        i
        b
        u
        t
        e
        b
        e
        c
        o
        m
        i
        n
        g
        t
        h
        e
        u
        p
        p
        e
        r
        l
        i
        m
        i
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.referenceStrength = None
        """ 
        S
        t
        r
        e
        n
        g
        t
        h
        e
        x
        p
        r
        e
        s
        s
        e
        d
        i
        n
        t
        e
        r
        m
        s
        o
        f
        a
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
        u
        b
        s
        t
        a
        n
        c
        e
        .
        List of `MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength` items (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).elementProperties()
        js.extend([
            ("concentration", "concentration", ratio.Ratio, False, None, False),
            ("concentrationLowLimit", "concentrationLowLimit", ratio.Ratio, False, None, False),
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("presentation", "presentation", ratio.Ratio, False, None, True),
            ("presentationLowLimit", "presentationLowLimit", ratio.Ratio, False, None, False),
            ("referenceStrength", "referenceStrength", MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, True, None, False),
        ])
        return js


class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    e
    n
    g
    t
    h
    e
    x
    p
    r
    e
    s
    s
    e
    d
    i
    n
    t
    e
    r
    m
    s
    o
    f
    a
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
    u
    b
    s
    t
    a
    n
    c
    e
    .
    """
    
    resource_type = "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ 
        T
        h
        e
        c
        o
        u
        n
        t
        r
        y
        o
        r
        c
        o
        u
        n
        t
        r
        i
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
        t
        h
        e
        s
        t
        r
        e
        n
        g
        t
        h
        r
        a
        n
        g
        e
        a
        p
        p
        l
        i
        e
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.measurementPoint = None
        """ 
        F
        o
        r
        w
        h
        e
        n
        s
        t
        r
        e
        n
        g
        t
        h
        i
        s
        m
        e
        a
        s
        u
        r
        e
        d
        a
        t
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
        o
        i
        n
        t
        o
        r
        d
        i
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.strength = None
        """ 
        S
        t
        r
        e
        n
        g
        t
        h
        e
        x
        p
        r
        e
        s
        s
        e
        d
        i
        n
        t
        e
        r
        m
        s
        o
        f
        a
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
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.strengthLowLimit = None
        """ 
        S
        t
        r
        e
        n
        g
        t
        h
        e
        x
        p
        r
        e
        s
        s
        e
        d
        i
        n
        t
        e
        r
        m
        s
        o
        f
        a
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
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.substance = None
        """ 
        R
        e
        l
        e
        v
        a
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
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("strength", "strength", ratio.Ratio, False, None, True),
            ("strengthLowLimit", "strengthLowLimit", ratio.Ratio, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicinalProductIngredientSubstance(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    i
    n
    g
    r
    e
    d
    i
    e
    n
    t
    s
    u
    b
    s
    t
    a
    n
    c
    e
    .
    """
    
    resource_type = "MedicinalProductIngredientSubstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        T
        h
        e
        i
        n
        g
        r
        e
        d
        i
        e
        n
        t
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.strength = None
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
        u
        b
        s
        t
        a
        n
        c
        e
        o
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
        s
        u
        b
        s
        t
        a
        n
        c
        e
        p
        r
        e
        s
        e
        n
        t
        i
        n
        t
        h
        e
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        d
        i
        t
        e
        m
        o
        r
        p
        h
        a
        r
        m
        a
        c
        e
        u
        t
        i
        c
        a
        l
        p
        r
        o
        d
        u
        c
        t
        .
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """
        
        super(MedicinalProductIngredientSubstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
