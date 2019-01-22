#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Medication) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Medication(domainresource.DomainResource):
    """ 
    D
    e
    f
    i
    n
    i
    t
    i
    o
    n
    o
    f
    a
    M
    e
    d
    i
    c
    a
    t
    i
    o
    n
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
    i
    s
    p
    r
    i
    m
    a
    r
    i
    l
    y
    u
    s
    e
    d
    f
    o
    r
    t
    h
    e
    i
    d
    e
    n
    t
    i
    f
    i
    c
    a
    t
    i
    o
    n
    a
    n
    d
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
    o
    f
    a
    m
    e
    d
    i
    c
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
    p
    u
    r
    p
    o
    s
    e
    s
    o
    f
    p
    r
    e
    s
    c
    r
    i
    b
    i
    n
    g
    ,
    d
    i
    s
    p
    e
    n
    s
    i
    n
    g
    ,
    a
    n
    d
    a
    d
    m
    i
    n
    i
    s
    t
    e
    r
    i
    n
    g
    a
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    a
    s
    w
    e
    l
    l
    a
    s
    f
    o
    r
    m
    a
    k
    i
    n
    g
    s
    t
    a
    t
    e
    m
    e
    n
    t
    s
    a
    b
    o
    u
    t
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    u
    s
    e
    .
    
    """
    
    resource_type = "Medication"
    
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
        o
        f
        d
        r
        u
        g
        i
        n
        p
        a
        c
        k
        a
        g
        e
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.batch = None
        """ 
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
        p
        a
        c
        k
        a
        g
        e
        d
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        s
        .
        Type `MedicationBatch` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        C
        o
        d
        e
        s
        t
        h
        a
        t
        i
        d
        e
        n
        t
        i
        f
        y
        t
        h
        i
        s
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.form = None
        """ 
        p
        o
        w
        d
        e
        r
        |
        t
        a
        b
        l
        e
        t
        s
        |
        c
        a
        p
        s
        u
        l
        e
        +
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
        i
        s
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ 
        A
        c
        t
        i
        v
        e
        o
        r
        i
        n
        a
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
        .
        List of `MedicationIngredient` items (represented as `dict` in JSON). """
        
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
        e
        i
        t
        e
        m
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
        .
        Type `str`. """
        
        super(Medication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("amount", "amount", ratio.Ratio, False, None, False),
            ("batch", "batch", MedicationBatch, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", MedicationIngredient, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationBatch(backboneelement.BackboneElement):
    """ 
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
    p
    a
    c
    k
    a
    g
    e
    d
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    s
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
    t
    h
    a
    t
    o
    n
    l
    y
    a
    p
    p
    l
    i
    e
    s
    t
    o
    p
    a
    c
    k
    a
    g
    e
    s
    (
    n
    o
    t
    p
    r
    o
    d
    u
    c
    t
    s
    )
    .
    
    """
    
    resource_type = "MedicationBatch"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expirationDate = None
        """ 
        W
        h
        e
        n
        b
        a
        t
        c
        h
        w
        i
        l
        l
        e
        x
        p
        i
        r
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lotNumber = None
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
        b
        a
        t
        c
        h
        .
        Type `str`. """
        
        super(MedicationBatch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationBatch, self).elementProperties()
        js.extend([
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
        ])
        return js


class MedicationIngredient(backboneelement.BackboneElement):
    """ 
    A
    c
    t
    i
    v
    e
    o
    r
    i
    n
    a
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
    .
    
    
    I
    d
    e
    n
    t
    i
    f
    i
    e
    s
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
    c
    o
    n
    s
    t
    i
    t
    u
    e
    n
    t
    o
    f
    i
    n
    t
    e
    r
    e
    s
    t
    i
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
    .
    
    """
    
    resource_type = "MedicationIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isActive = None
        """ 
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
        
        self.itemCodeableConcept = None
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
        r
        c
        o
        n
        t
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
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
        r
        c
        o
        n
        t
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        p
        r
        e
        s
        e
        n
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        super(MedicationIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("strength", "strength", ratio.Ratio, False, None, False),
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
