#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Substance) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Substance(domainresource.DomainResource):
    """ 
    A
    h
    o
    m
    o
    g
    e
    n
    e
    o
    u
    s
    m
    a
    t
    e
    r
    i
    a
    l
    w
    i
    t
    h
    a
    d
    e
    f
    i
    n
    i
    t
    e
    c
    o
    m
    p
    o
    s
    i
    t
    i
    o
    n
    .
    """
    
    resource_type = "Substance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ 
        W
        h
        a
        t
        c
        l
        a
        s
        s
        /
        t
        y
        p
        e
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
        t
        h
        i
        s
        i
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        W
        h
        a
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
        t
        h
        i
        s
        i
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        e
        x
        t
        u
        a
        l
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
        c
        o
        m
        m
        e
        n
        t
        s
        .
        Type `str`. """
        
        self.identifier = None
        """ 
        U
        n
        i
        q
        u
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
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ 
        C
        o
        m
        p
        o
        s
        i
        t
        i
        o
        n
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
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ 
        I
        f
        t
        h
        i
        s
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
        s
        p
        e
        c
        i
        f
        i
        c
        p
        a
        c
        k
        a
        g
        e
        /
        c
        o
        n
        t
        a
        i
        n
        e
        r
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
        .
        List of `SubstanceInstance` items (represented as `dict` in JSON). """
        
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
        
        super(Substance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False),
            ("instance", "instance", SubstanceInstance, True, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceIngredient(backboneelement.BackboneElement):
    """ 
    C
    o
    m
    p
    o
    s
    i
    t
    i
    o
    n
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
    
    
    A
    s
    u
    b
    s
    t
    a
    n
    c
    e
    c
    a
    n
    b
    e
    c
    o
    m
    p
    o
    s
    e
    d
    o
    f
    o
    t
    h
    e
    r
    s
    u
    b
    s
    t
    a
    n
    c
    e
    s
    .
    
    """
    
    resource_type = "SubstanceIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None
        """ 
        O
        p
        t
        i
        o
        n
        a
        l
        a
        m
        o
        u
        n
        t
        (
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
        )
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.substanceCodeableConcept = None
        """ 
        A
        c
        o
        m
        p
        o
        n
        e
        n
        t
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.substanceReference = None
        """ 
        A
        c
        o
        m
        p
        o
        n
        e
        n
        t
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(SubstanceIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, False, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", True),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", True),
        ])
        return js


class SubstanceInstance(backboneelement.BackboneElement):
    """ 
    I
    f
    t
    h
    i
    s
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
    s
    p
    e
    c
    i
    f
    i
    c
    p
    a
    c
    k
    a
    g
    e
    /
    c
    o
    n
    t
    a
    i
    n
    e
    r
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
    .
    
    
    S
    u
    b
    s
    t
    a
    n
    c
    e
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
    d
    e
    s
    c
    r
    i
    b
    e
    a
    k
    i
    n
    d
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
    ,
    o
    r
    a
    s
    p
    e
    c
    i
    f
    i
    c
    p
    a
    c
    k
    a
    g
    e
    /
    c
    o
    n
    t
    a
    i
    n
    e
    r
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
    :
    a
    n
    i
    n
    s
    t
    a
    n
    c
    e
    .
    
    """
    
    resource_type = "SubstanceInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expiry = None
        """ 
        W
        h
        e
        n
        n
        o
        l
        o
        n
        g
        e
        r
        v
        a
        l
        i
        d
        t
        o
        u
        s
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        o
        f
        t
        h
        e
        p
        a
        c
        k
        a
        g
        e
        /
        c
        o
        n
        t
        a
        i
        n
        e
        r
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
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
        p
        a
        c
        k
        a
        g
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SubstanceInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("expiry", "expiry", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
