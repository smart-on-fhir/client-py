#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ 
    G
    u
    i
    d
    a
    n
    c
    e
    o
    r
    a
    d
    v
    i
    c
    e
    r
    e
    l
    a
    t
    i
    n
    g
    t
    o
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
    .
    
    
    A
    p
    a
    t
    i
    e
    n
    t
    '
    s
    p
    o
    i
    n
    t
    -
    i
    n
    -
    t
    i
    m
    e
    s
    e
    t
    o
    f
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
    (
    i
    .
    e
    .
    f
    o
    r
    e
    c
    a
    s
    t
    i
    n
    g
    )
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
    a
    p
    u
    b
    l
    i
    s
    h
    e
    d
    s
    c
    h
    e
    d
    u
    l
    e
    w
    i
    t
    h
    o
    p
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
    o
    r
    t
    i
    n
    g
    j
    u
    s
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
    .
    
    """
    
    resource_type = "ImmunizationRecommendation"
    
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
        r
        o
        t
        o
        c
        o
        l
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        D
        a
        t
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
        (
        s
        )
        c
        r
        e
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        
        self.patient = None
        """ 
        W
        h
        o
        t
        h
        i
        s
        p
        r
        o
        f
        i
        l
        e
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recommendation = None
        """ 
        V
        a
        c
        c
        i
        n
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
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ 
    V
    a
    c
    c
    i
    n
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
    
    resource_type = "ImmunizationRecommendationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contraindicatedVaccineCode = None
        """ 
        V
        a
        c
        c
        i
        n
        e
        w
        h
        i
        c
        h
        i
        s
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
        t
        o
        f
        u
        l
        f
        i
        l
        l
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateCriterion = None
        """ 
        D
        a
        t
        e
        s
        g
        o
        v
        e
        r
        n
        i
        n
        g
        p
        r
        o
        p
        o
        s
        e
        d
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
        .
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        P
        r
        o
        t
        o
        c
        o
        l
        d
        e
        t
        a
        i
        l
        s
        .
        Type `str`. """
        
        self.doseNumberPositiveInt = None
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
        d
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
        d
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
        
        self.forecastReason = None
        """ 
        V
        a
        c
        c
        i
        n
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
        s
        t
        a
        t
        u
        s
        r
        e
        a
        s
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.forecastStatus = None
        """ 
        V
        a
        c
        c
        i
        n
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
        t
        a
        t
        u
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        a
        t
        i
        o
        n
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
        
        self.supportingImmunization = None
        """ 
        P
        a
        s
        t
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
        s
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.supportingPatientInformation = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        o
        b
        s
        e
        r
        v
        a
        t
        i
        o
        n
        s
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.targetDisease = None
        """ 
        D
        i
        s
        e
        a
        s
        e
        t
        o
        b
        e
        i
        m
        m
        u
        n
        i
        z
        e
        d
        a
        g
        a
        i
        n
        s
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        """ 
        V
        a
        c
        c
        i
        n
        e
        o
        r
        v
        a
        c
        c
        i
        n
        e
        g
        r
        o
        u
        p
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
        a
        p
        p
        l
        i
        e
        s
        t
        o
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("contraindicatedVaccineCode", "contraindicatedVaccineCode", codeableconcept.CodeableConcept, True, None, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("description", "description", str, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", False),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", False),
            ("forecastReason", "forecastReason", codeableconcept.CodeableConcept, True, None, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False, None, True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True, None, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, False, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ 
    D
    a
    t
    e
    s
    g
    o
    v
    e
    r
    n
    i
    n
    g
    p
    r
    o
    p
    o
    s
    e
    d
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
    .
    
    
    V
    a
    c
    c
    i
    n
    e
    d
    a
    t
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
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    ,
    e
    a
    r
    l
    i
    e
    s
    t
    d
    a
    t
    e
    t
    o
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
    ,
    l
    a
    t
    e
    s
    t
    d
    a
    t
    e
    t
    o
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
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "ImmunizationRecommendationRecommendationDateCriterion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
        d
        a
        t
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
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
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", fhirdate.FHIRDate, False, None, True),
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
