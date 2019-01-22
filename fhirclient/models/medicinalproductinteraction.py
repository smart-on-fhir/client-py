#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProductInteraction(domainresource.DomainResource):
    """ 
    M
    e
    d
    i
    c
    i
    n
    a
    l
    P
    r
    o
    d
    u
    c
    t
    I
    n
    t
    e
    r
    a
    c
    t
    i
    o
    n
    .
    
    
    T
    h
    e
    i
    n
    t
    e
    r
    a
    c
    t
    i
    o
    n
    s
    o
    f
    t
    h
    e
    m
    e
    d
    i
    c
    i
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
    w
    i
    t
    h
    o
    t
    h
    e
    r
    m
    e
    d
    i
    c
    i
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
    ,
    o
    r
    o
    t
    h
    e
    r
    f
    o
    r
    m
    s
    o
    f
    i
    n
    t
    e
    r
    a
    c
    t
    i
    o
    n
    s
    .
    
    """
    
    resource_type = "MedicinalProductInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        T
        h
        e
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        d
        e
        s
        c
        r
        i
        b
        e
        d
        .
        Type `str`. """
        
        self.effect = None
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
        o
        f
        t
        h
        e
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        ,
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
        "
        r
        e
        d
        u
        c
        e
        d
        g
        a
        s
        t
        r
        i
        c
        a
        b
        s
        o
        r
        p
        t
        i
        o
        n
        o
        f
        p
        r
        i
        m
        a
        r
        y
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
        "
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.incidence = None
        """ 
        T
        h
        e
        i
        n
        c
        i
        d
        e
        n
        c
        e
        o
        f
        t
        h
        e
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        ,
        e
        .
        g
        .
        t
        h
        e
        o
        r
        e
        t
        i
        c
        a
        l
        ,
        o
        b
        s
        e
        r
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.interactant = None
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
        c
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
        ,
        f
        o
        o
        d
        o
        r
        l
        a
        b
        o
        r
        a
        t
        o
        r
        y
        t
        e
        s
        t
        t
        h
        a
        t
        i
        n
        t
        e
        r
        a
        c
        t
        s
        .
        List of `MedicinalProductInteractionInteractant` items (represented as `dict` in JSON). """
        
        self.management = None
        """ 
        A
        c
        t
        i
        o
        n
        s
        f
        o
        r
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
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        T
        h
        e
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
        w
        h
        i
        c
        h
        t
        h
        i
        s
        i
        s
        a
        d
        e
        s
        c
        r
        i
        b
        e
        d
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
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
        t
        h
        e
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        e
        .
        g
        .
        d
        r
        u
        g
        -
        d
        r
        u
        g
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        ,
        d
        r
        u
        g
        -
        f
        o
        o
        d
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        ,
        d
        r
        u
        g
        -
        l
        a
        b
        t
        e
        s
        t
        i
        n
        t
        e
        r
        a
        c
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("effect", "effect", codeableconcept.CodeableConcept, False, None, False),
            ("incidence", "incidence", codeableconcept.CodeableConcept, False, None, False),
            ("interactant", "interactant", MedicinalProductInteractionInteractant, True, None, False),
            ("management", "management", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductInteractionInteractant(backboneelement.BackboneElement):
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
    c
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
    ,
    f
    o
    o
    d
    o
    r
    l
    a
    b
    o
    r
    a
    t
    o
    r
    y
    t
    e
    s
    t
    t
    h
    a
    t
    i
    n
    t
    e
    r
    a
    c
    t
    s
    .
    """
    
    resource_type = "MedicinalProductInteractionInteractant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.itemCodeableConcept = None
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
        c
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
        ,
        f
        o
        o
        d
        o
        r
        l
        a
        b
        o
        r
        a
        t
        o
        r
        y
        t
        e
        s
        t
        t
        h
        a
        t
        i
        n
        t
        e
        r
        a
        c
        t
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
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
        c
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
        ,
        f
        o
        o
        d
        o
        r
        l
        a
        b
        o
        r
        a
        t
        o
        r
        y
        t
        e
        s
        t
        t
        h
        a
        t
        i
        n
        t
        e
        r
        a
        c
        t
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MedicinalProductInteractionInteractant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
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
