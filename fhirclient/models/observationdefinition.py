#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ObservationDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ObservationDefinition(domainresource.DomainResource):
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
    n
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
    .
    
    
    S
    e
    t
    o
    f
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
    a
    l
    c
    h
    a
    r
    a
    c
    t
    e
    r
    i
    s
    t
    i
    c
    s
    f
    o
    r
    a
    k
    i
    n
    d
    o
    f
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
    o
    r
    m
    e
    a
    s
    u
    r
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
    e
    d
    o
    r
    c
    o
    n
    s
    u
    m
    e
    d
    b
    y
    a
    n
    o
    r
    d
    e
    r
    a
    b
    l
    e
    h
    e
    a
    l
    t
    h
    c
    a
    r
    e
    s
    e
    r
    v
    i
    c
    e
    .
    
    """
    
    resource_type = "ObservationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abnormalCodedValueSet = None
        """ 
        V
        a
        l
        u
        e
        s
        e
        t
        o
        f
        a
        b
        n
        o
        r
        m
        a
        l
        c
        o
        d
        e
        d
        v
        a
        l
        u
        e
        s
        f
        o
        r
        t
        h
        e
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
        c
        o
        n
        f
        o
        r
        m
        i
        n
        g
        t
        o
        t
        h
        i
        s
        O
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        C
        a
        t
        e
        g
        o
        r
        y
        o
        f
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
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
        (
        c
        o
        d
        e
        /
        t
        y
        p
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criticalCodedValueSet = None
        """ 
        V
        a
        l
        u
        e
        s
        e
        t
        o
        f
        c
        r
        i
        t
        i
        c
        a
        l
        c
        o
        d
        e
        d
        v
        a
        l
        u
        e
        s
        f
        o
        r
        t
        h
        e
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
        c
        o
        n
        f
        o
        r
        m
        i
        n
        g
        t
        o
        t
        h
        i
        s
        O
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        O
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
        i
        n
        s
        t
        a
        n
        c
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.method = None
        """ 
        M
        e
        t
        h
        o
        d
        u
        s
        e
        d
        t
        o
        p
        r
        o
        d
        u
        c
        e
        t
        h
        e
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleResultsAllowed = None
        """ 
        M
        u
        l
        t
        i
        p
        l
        e
        r
        e
        s
        u
        l
        t
        s
        a
        l
        l
        o
        w
        e
        d
        .
        Type `bool`. """
        
        self.normalCodedValueSet = None
        """ 
        V
        a
        l
        u
        e
        s
        e
        t
        o
        f
        n
        o
        r
        m
        a
        l
        c
        o
        d
        e
        d
        v
        a
        l
        u
        e
        s
        f
        o
        r
        t
        h
        e
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
        c
        o
        n
        f
        o
        r
        m
        i
        n
        g
        t
        o
        t
        h
        i
        s
        O
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.permittedDataType = None
        """ 
        Q
        u
        a
        n
        t
        i
        t
        y
        |
        C
        o
        d
        e
        a
        b
        l
        e
        C
        o
        n
        c
        e
        p
        t
        |
        s
        t
        r
        i
        n
        g
        |
        b
        o
        o
        l
        e
        a
        n
        |
        i
        n
        t
        e
        g
        e
        r
        |
        R
        a
        n
        g
        e
        |
        R
        a
        t
        i
        o
        |
        S
        a
        m
        p
        l
        e
        d
        D
        a
        t
        a
        |
        t
        i
        m
        e
        |
        d
        a
        t
        e
        T
        i
        m
        e
        |
        P
        e
        r
        i
        o
        d
        .
        List of `str` items. """
        
        self.preferredReportName = None
        """ 
        P
        r
        e
        f
        e
        r
        r
        e
        d
        r
        e
        p
        o
        r
        t
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.qualifiedInterval = None
        """ 
        Q
        u
        a
        l
        i
        f
        i
        e
        d
        r
        a
        n
        g
        e
        f
        o
        r
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
        a
        n
        d
        o
        r
        d
        i
        n
        a
        l
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
        r
        e
        s
        u
        l
        t
        s
        .
        List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON). """
        
        self.quantitativeDetails = None
        """ 
        C
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        s
        o
        f
        q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
        r
        e
        s
        u
        l
        t
        s
        .
        Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON). """
        
        self.validCodedValueSet = None
        """ 
        V
        a
        l
        u
        e
        s
        e
        t
        o
        f
        v
        a
        l
        i
        d
        c
        o
        d
        e
        d
        v
        a
        l
        u
        e
        s
        f
        o
        r
        t
        h
        e
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
        c
        o
        n
        f
        o
        r
        m
        i
        n
        g
        t
        o
        t
        h
        i
        s
        O
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ObservationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend([
            ("abnormalCodedValueSet", "abnormalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("criticalCodedValueSet", "criticalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("multipleResultsAllowed", "multipleResultsAllowed", bool, False, None, False),
            ("normalCodedValueSet", "normalCodedValueSet", fhirreference.FHIRReference, False, None, False),
            ("permittedDataType", "permittedDataType", str, True, None, False),
            ("preferredReportName", "preferredReportName", str, False, None, False),
            ("qualifiedInterval", "qualifiedInterval", ObservationDefinitionQualifiedInterval, True, None, False),
            ("quantitativeDetails", "quantitativeDetails", ObservationDefinitionQuantitativeDetails, False, None, False),
            ("validCodedValueSet", "validCodedValueSet", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ 
    Q
    u
    a
    l
    i
    f
    i
    e
    d
    r
    a
    n
    g
    e
    f
    o
    r
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
    a
    n
    d
    o
    r
    d
    i
    n
    a
    l
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
    r
    e
    s
    u
    l
    t
    s
    .
    
    
    M
    u
    l
    t
    i
    p
    l
    e
    r
    a
    n
    g
    e
    s
    o
    f
    r
    e
    s
    u
    l
    t
    s
    q
    u
    a
    l
    i
    f
    i
    e
    d
    b
    y
    d
    i
    f
    f
    e
    r
    e
    n
    t
    c
    o
    n
    t
    e
    x
    t
    s
    f
    o
    r
    o
    r
    d
    i
    n
    a
    l
    o
    r
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
    c
    o
    n
    f
    o
    r
    m
    i
    n
    g
    t
    o
    t
    h
    i
    s
    O
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
    .
    
    """
    
    resource_type = "ObservationDefinitionQualifiedInterval"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.age = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
        e
        a
        g
        e
        r
        a
        n
        g
        e
        ,
        i
        f
        r
        e
        l
        e
        v
        a
        n
        t
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.appliesTo = None
        """ 
        T
        a
        r
        g
        e
        t
        t
        e
        d
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
        o
        f
        t
        h
        e
        r
        a
        n
        g
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        r
        e
        f
        e
        r
        e
        n
        c
        e
        |
        c
        r
        i
        t
        i
        c
        a
        l
        |
        a
        b
        s
        o
        l
        u
        t
        e
        .
        Type `str`. """
        
        self.condition = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
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
        r
        e
        f
        e
        r
        e
        n
        c
        e
        r
        a
        n
        g
        e
        .
        Type `str`. """
        
        self.context = None
        """ 
        R
        a
        n
        g
        e
        c
        o
        n
        t
        e
        x
        t
        q
        u
        a
        l
        i
        f
        i
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.gender = None
        """ 
        m
        a
        l
        e
        |
        f
        e
        m
        a
        l
        e
        |
        o
        t
        h
        e
        r
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
        
        self.gestationalAge = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
        e
        g
        e
        s
        t
        a
        t
        i
        o
        n
        a
        l
        a
        g
        e
        r
        a
        n
        g
        e
        ,
        i
        f
        r
        e
        l
        e
        v
        a
        n
        t
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.range = None
        """ 
        T
        h
        e
        i
        n
        t
        e
        r
        v
        a
        l
        i
        t
        s
        e
        l
        f
        ,
        f
        o
        r
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
        o
        r
        o
        r
        d
        i
        n
        a
        l
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
        .
        Type `Range` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQualifiedInterval, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend([
            ("age", "age", range.Range, False, None, False),
            ("appliesTo", "appliesTo", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", codeableconcept.CodeableConcept, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("gestationalAge", "gestationalAge", range.Range, False, None, False),
            ("range", "range", range.Range, False, None, False),
        ])
        return js


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ 
    C
    h
    a
    r
    a
    c
    t
    e
    r
    i
    s
    t
    i
    c
    s
    o
    f
    q
    u
    a
    n
    t
    i
    t
    a
    t
    i
    v
    e
    r
    e
    s
    u
    l
    t
    s
    .
    
    
    C
    h
    a
    r
    a
    c
    t
    e
    r
    i
    s
    t
    i
    c
    s
    f
    o
    r
    q
    u
    a
    n
    t
    i
    t
    a
    t
    i
    v
    e
    r
    e
    s
    u
    l
    t
    s
    o
    f
    t
    h
    i
    s
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
    .
    
    """
    
    resource_type = "ObservationDefinitionQuantitativeDetails"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.conversionFactor = None
        """ 
        S
        I
        t
        o
        C
        u
        s
        t
        o
        m
        a
        r
        y
        u
        n
        i
        t
        c
        o
        n
        v
        e
        r
        s
        i
        o
        n
        f
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.customaryUnit = None
        """ 
        C
        u
        s
        t
        o
        m
        a
        r
        y
        u
        n
        i
        t
        f
        o
        r
        q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
        r
        e
        s
        u
        l
        t
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decimalPrecision = None
        """ 
        D
        e
        c
        i
        m
        a
        l
        p
        r
        e
        c
        i
        s
        i
        o
        n
        o
        f
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
        q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
        r
        e
        s
        u
        l
        t
        s
        .
        Type `int`. """
        
        self.unit = None
        """ 
        S
        I
        u
        n
        i
        t
        f
        o
        r
        q
        u
        a
        n
        t
        i
        t
        a
        t
        i
        v
        e
        r
        e
        s
        u
        l
        t
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ObservationDefinitionQuantitativeDetails, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend([
            ("conversionFactor", "conversionFactor", float, False, None, False),
            ("customaryUnit", "customaryUnit", codeableconcept.CodeableConcept, False, None, False),
            ("decimalPrecision", "decimalPrecision", int, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
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
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
