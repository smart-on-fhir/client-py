#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Population) on 2019-01-22.
#  2019, SMART Health IT.


from . import backboneelement

class Population(backboneelement.BackboneElement):
    """ 
    A
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
    s
    e
    t
    o
    f
    p
    e
    o
    p
    l
    e
    t
    h
    a
    t
    a
    p
    p
    l
    y
    t
    o
    s
    o
    m
    e
    c
    l
    i
    n
    i
    c
    a
    l
    l
    y
    r
    e
    l
    a
    t
    e
    d
    c
    o
    n
    t
    e
    x
    t
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
    p
    e
    o
    p
    l
    e
    c
    o
    n
    t
    r
    a
    i
    n
    d
    i
    c
    a
    t
    e
    d
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
    
    
    A
    p
    o
    p
    u
    l
    a
    t
    i
    o
    o
    f
    p
    e
    o
    p
    l
    e
    w
    i
    t
    h
    s
    o
    m
    e
    s
    e
    t
    o
    f
    g
    r
    o
    u
    p
    i
    n
    g
    c
    r
    i
    t
    e
    r
    i
    a
    .
    
    """
    
    resource_type = "Population"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageCodeableConcept = None
        """ 
        T
        h
        e
        a
        g
        e
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
        p
        o
        p
        u
        l
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.ageRange = None
        """ 
        T
        h
        e
        a
        g
        e
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
        p
        o
        p
        u
        l
        a
        t
        i
        o
        n
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.gender = None
        """ 
        T
        h
        e
        g
        e
        n
        d
        e
        r
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
        p
        o
        p
        u
        l
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.physiologicalCondition = None
        """ 
        T
        h
        e
        e
        x
        i
        s
        t
        i
        n
        g
        p
        h
        y
        s
        i
        o
        l
        o
        g
        i
        c
        a
        l
        c
        o
        n
        d
        i
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
        s
        p
        e
        c
        i
        f
        i
        c
        p
        o
        p
        u
        l
        a
        t
        i
        o
        n
        t
        o
        w
        h
        i
        c
        h
        t
        h
        i
        s
        a
        p
        p
        l
        i
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.race = None
        """ 
        R
        a
        c
        e
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
        p
        o
        p
        u
        l
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Population, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Population, self).elementProperties()
        js.extend([
            ("ageCodeableConcept", "ageCodeableConcept", codeableconcept.CodeableConcept, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("gender", "gender", codeableconcept.CodeableConcept, False, None, False),
            ("physiologicalCondition", "physiologicalCondition", codeableconcept.CodeableConcept, False, None, False),
            ("race", "race", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
