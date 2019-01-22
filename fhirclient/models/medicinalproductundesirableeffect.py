#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProductUndesirableEffect(domainresource.DomainResource):
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
    U
    n
    d
    e
    s
    i
    r
    a
    b
    l
    e
    E
    f
    f
    e
    c
    t
    .
    
    
    D
    e
    s
    c
    r
    i
    b
    e
    t
    h
    e
    u
    n
    d
    e
    s
    i
    r
    a
    b
    l
    e
    e
    f
    f
    e
    c
    t
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
    .
    
    """
    
    resource_type = "MedicinalProductUndesirableEffect"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
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
        e
        f
        f
        e
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.frequencyOfOccurrence = None
        """ 
        T
        h
        e
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
        o
        c
        c
        u
        r
        r
        e
        n
        c
        e
        o
        f
        t
        h
        e
        e
        f
        f
        e
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.population = None
        """ 
        T
        h
        e
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
        g
        r
        o
        u
        p
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
        List of `Population` items (represented as `dict` in JSON). """
        
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
        n
        i
        n
        d
        i
        c
        a
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.symptomConditionEffect = None
        """ 
        T
        h
        e
        s
        y
        m
        p
        t
        o
        m
        ,
        c
        o
        n
        d
        i
        t
        i
        o
        n
        o
        r
        u
        n
        d
        e
        s
        i
        r
        a
        b
        l
        e
        e
        f
        f
        e
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductUndesirableEffect, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductUndesirableEffect, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("frequencyOfOccurrence", "frequencyOfOccurrence", codeableconcept.CodeableConcept, False, None, False),
            ("population", "population", population.Population, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("symptomConditionEffect", "symptomConditionEffect", codeableconcept.CodeableConcept, False, None, False),
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
    from . import population
except ImportError:
    population = sys.modules[__package__ + '.population']
