#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ImmunizationEvaluation(domainresource.DomainResource):
    """ 
    I
    m
    m
    u
    n
    i
    z
    a
    t
    i
    o
    n
    e
    v
    a
    l
    u
    a
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
    .
    
    
    D
    e
    s
    c
    r
    i
    b
    e
    s
    a
    c
    o
    m
    p
    a
    r
    i
    s
    o
    n
    o
    f
    a
    n
    i
    m
    m
    u
    n
    i
    z
    a
    t
    i
    o
    n
    e
    v
    e
    n
    t
    a
    g
    a
    i
    n
    s
    t
    p
    u
    b
    l
    i
    s
    h
    e
    d
    r
    e
    c
    o
    m
    m
    e
    n
    d
    a
    t
    i
    o
    n
    s
    t
    o
    d
    e
    t
    e
    r
    m
    i
    n
    e
    i
    f
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
    i
    s
    "
    v
    a
    l
    i
    d
    "
    i
    n
    r
    e
    l
    a
    t
    i
    o
    n
    t
    o
    t
    h
    o
    s
    e
    r
    e
    c
    o
    m
    m
    e
    n
    d
    a
    t
    i
    o
    n
    s
    .
    
    """
    
    resource_type = "ImmunizationEvaluation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ 
        W
        h
        o
        i
        s
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
        p
        u
        b
        l
        i
        s
        h
        i
        n
        g
        t
        h
        e
        r
        e
        c
        o
        m
        m
        e
        n
        d
        a
        t
        i
        o
        n
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        D
        a
        t
        e
        e
        v
        a
        l
        u
        a
        t
        i
        o
        n
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
        
        self.description = None
        """ 
        E
        v
        a
        l
        u
        a
        t
        i
        o
        n
        n
        o
        t
        e
        s
        .
        Type `str`. """
        
        self.doseNumberPositiveInt = None
        """ 
        D
        o
        s
        e
        n
        u
        m
        b
        e
        r
        w
        i
        t
        h
        i
        n
        s
        e
        r
        i
        e
        s
        .
        Type `int`. """
        
        self.doseNumberString = None
        """ 
        D
        o
        s
        e
        n
        u
        m
        b
        e
        r
        w
        i
        t
        h
        i
        n
        s
        e
        r
        i
        e
        s
        .
        Type `str`. """
        
        self.doseStatus = None
        """ 
        S
        t
        a
        t
        u
        s
        o
        f
        t
        h
        e
        d
        o
        s
        e
        r
        e
        l
        a
        t
        i
        v
        e
        t
        o
        p
        u
        b
        l
        i
        s
        h
        e
        d
        r
        e
        c
        o
        m
        m
        e
        n
        d
        a
        t
        i
        o
        n
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseStatusReason = None
        """ 
        R
        e
        a
        s
        o
        n
        f
        o
        r
        t
        h
        e
        d
        o
        s
        e
        s
        t
        a
        t
        u
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.immunizationEvent = None
        """ 
        I
        m
        m
        u
        n
        i
        z
        a
        t
        i
        o
        n
        b
        e
        i
        n
        g
        e
        v
        a
        l
        u
        a
        t
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        W
        h
        o
        t
        h
        i
        s
        e
        v
        a
        l
        u
        a
        t
        i
        o
        n
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.series = None
        """ 
        N
        a
        m
        e
        o
        f
        v
        a
        c
        c
        i
        n
        e
        s
        e
        r
        i
        e
        s
        .
        Type `str`. """
        
        self.seriesDosesPositiveInt = None
        """ 
        R
        e
        c
        o
        m
        m
        e
        n
        d
        e
        d
        n
        u
        m
        b
        e
        r
        o
        f
        d
        o
        s
        e
        s
        f
        o
        r
        i
        m
        m
        u
        n
        i
        t
        y
        .
        Type `int`. """
        
        self.seriesDosesString = None
        """ 
        R
        e
        c
        o
        m
        m
        e
        n
        d
        e
        d
        n
        u
        m
        b
        e
        r
        o
        f
        d
        o
        s
        e
        s
        f
        o
        r
        i
        m
        m
        u
        n
        i
        t
        y
        .
        Type `str`. """
        
        self.status = None
        """ 
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
        
        self.targetDisease = None
        """ 
        E
        v
        a
        l
        u
        a
        t
        i
        o
        n
        t
        a
        r
        g
        e
        t
        d
        i
        s
        e
        a
        s
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationEvaluation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationEvaluation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False, None, True),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("immunizationEvent", "immunizationEvent", fhirreference.FHIRReference, False, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("status", "status", str, False, None, True),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, True),
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
