#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MeasureReport) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MeasureReport(domainresource.DomainResource):
    """ 
    R
    e
    s
    u
    l
    t
    s
    o
    f
    a
    m
    e
    a
    s
    u
    r
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
    .
    
    
    T
    h
    e
    M
    e
    a
    s
    u
    r
    e
    R
    e
    p
    o
    r
    t
    r
    e
    s
    o
    u
    r
    c
    e
    c
    o
    n
    t
    a
    i
    n
    s
    t
    h
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
    e
    c
    a
    l
    c
    u
    l
    a
    t
    i
    o
    n
    o
    f
    a
    m
    e
    a
    s
    u
    r
    e
    ;
    a
    n
    d
    o
    p
    t
    i
    o
    n
    a
    l
    l
    y
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
    t
    o
    t
    h
    e
    r
    e
    s
    o
    u
    r
    c
    e
    s
    i
    n
    v
    o
    l
    v
    e
    d
    i
    n
    t
    h
    a
    t
    c
    a
    l
    c
    u
    l
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "MeasureReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        r
        e
        p
        o
        r
        t
        w
        a
        s
        g
        e
        n
        e
        r
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.evaluatedResource = None
        """ 
        W
        h
        a
        t
        d
        a
        t
        a
        w
        a
        s
        u
        s
        e
        d
        t
        o
        c
        a
        l
        c
        u
        l
        a
        t
        e
        t
        h
        e
        m
        e
        a
        s
        u
        r
        e
        s
        c
        o
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.group = None
        """ 
        M
        e
        a
        s
        u
        r
        e
        r
        e
        s
        u
        l
        t
        s
        f
        o
        r
        e
        a
        c
        h
        g
        r
        o
        u
        p
        .
        List of `MeasureReportGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        A
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
        M
        e
        a
        s
        u
        r
        e
        R
        e
        p
        o
        r
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.improvementNotation = None
        """ 
        i
        n
        c
        r
        e
        a
        s
        e
        |
        d
        e
        c
        r
        e
        a
        s
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.measure = None
        """ 
        W
        h
        a
        t
        m
        e
        a
        s
        u
        r
        e
        w
        a
        s
        c
        a
        l
        c
        u
        l
        a
        t
        e
        d
        .
        Type `str`. """
        
        self.period = None
        """ 
        W
        h
        a
        t
        p
        e
        r
        i
        o
        d
        t
        h
        e
        r
        e
        p
        o
        r
        t
        c
        o
        v
        e
        r
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.reporter = None
        """ 
        W
        h
        o
        i
        s
        r
        e
        p
        o
        r
        t
        i
        n
        g
        t
        h
        e
        d
        a
        t
        a
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        |
        p
        e
        n
        d
        i
        n
        g
        |
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        self.subject = None
        """ 
        W
        h
        a
        t
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        (
        s
        )
        t
        h
        e
        r
        e
        p
        o
        r
        t
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        |
        s
        u
        b
        j
        e
        c
        t
        -
        l
        i
        s
        t
        |
        s
        u
        m
        m
        a
        r
        y
        |
        d
        a
        t
        a
        -
        c
        o
        l
        l
        e
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(MeasureReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReport, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("evaluatedResource", "evaluatedResource", fhirreference.FHIRReference, True, None, False),
            ("group", "group", MeasureReportGroup, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("improvementNotation", "improvementNotation", codeableconcept.CodeableConcept, False, None, False),
            ("measure", "measure", str, False, None, True),
            ("period", "period", period.Period, False, None, True),
            ("reporter", "reporter", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import backboneelement

class MeasureReportGroup(backboneelement.BackboneElement):
    """ 
    M
    e
    a
    s
    u
    r
    e
    r
    e
    s
    u
    l
    t
    s
    f
    o
    r
    e
    a
    c
    h
    g
    r
    o
    u
    p
    .
    
    
    T
    h
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
    e
    c
    a
    l
    c
    u
    l
    a
    t
    i
    o
    n
    ,
    o
    n
    e
    f
    o
    r
    e
    a
    c
    h
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
    i
    n
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    """
    
    resource_type = "MeasureReportGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        M
        e
        a
        n
        i
        n
        g
        o
        f
        t
        h
        e
        g
        r
        o
        u
        p
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.measureScore = None
        """ 
        W
        h
        a
        t
        s
        c
        o
        r
        e
        t
        h
        i
        s
        g
        r
        o
        u
        p
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
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
        s
        i
        n
        t
        h
        e
        g
        r
        o
        u
        p
        .
        List of `MeasureReportGroupPopulation` items (represented as `dict` in JSON). """
        
        self.stratifier = None
        """ 
        S
        t
        r
        a
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
        r
        e
        s
        u
        l
        t
        s
        .
        List of `MeasureReportGroupStratifier` items (represented as `dict` in JSON). """
        
        super(MeasureReportGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroup, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("population", "population", MeasureReportGroupPopulation, True, None, False),
            ("stratifier", "stratifier", MeasureReportGroupStratifier, True, None, False),
        ])
        return js


class MeasureReportGroupPopulation(backboneelement.BackboneElement):
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
    s
    i
    n
    t
    h
    e
    g
    r
    o
    u
    p
    .
    
    
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
    s
    t
    h
    a
    t
    m
    a
    k
    e
    u
    p
    t
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
    ,
    o
    n
    e
    f
    o
    r
    e
    a
    c
    h
    t
    y
    p
    e
    o
    f
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
    a
    p
    p
    r
    o
    p
    r
    i
    a
    t
    e
    f
    o
    r
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    """
    
    resource_type = "MeasureReportGroupPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        i
        n
        i
        t
        i
        a
        l
        -
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
        |
        n
        u
        m
        e
        r
        a
        t
        o
        r
        |
        n
        u
        m
        e
        r
        a
        t
        o
        r
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        -
        e
        x
        c
        e
        p
        t
        i
        o
        n
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        
        self.count = None
        """ 
        S
        i
        z
        e
        o
        f
        t
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
        .
        Type `int`. """
        
        self.subjectResults = None
        """ 
        F
        o
        r
        s
        u
        b
        j
        e
        c
        t
        -
        l
        i
        s
        t
        r
        e
        p
        o
        r
        t
        s
        ,
        t
        h
        e
        s
        u
        b
        j
        e
        c
        t
        r
        e
        s
        u
        l
        t
        s
        i
        n
        t
        h
        i
        s
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MeasureReportGroupStratifier(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    a
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
    r
    e
    s
    u
    l
    t
    s
    .
    
    
    W
    h
    e
    n
    a
    m
    e
    a
    s
    u
    r
    e
    i
    n
    c
    l
    u
    d
    e
    s
    m
    u
    l
    t
    i
    p
    l
    e
    s
    t
    r
    a
    t
    i
    f
    i
    e
    r
    s
    ,
    t
    h
    e
    r
    e
    w
    i
    l
    l
    b
    e
    a
    s
    t
    r
    a
    t
    i
    f
    i
    e
    r
    g
    r
    o
    u
    p
    f
    o
    r
    e
    a
    c
    h
    s
    t
    r
    a
    t
    i
    f
    i
    e
    r
    d
    e
    f
    i
    n
    e
    d
    b
    y
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    """
    
    resource_type = "MeasureReportGroupStratifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        W
        h
        a
        t
        s
        t
        r
        a
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
        g
        r
        o
        u
        p
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.stratum = None
        """ 
        S
        t
        r
        a
        t
        u
        m
        r
        e
        s
        u
        l
        t
        s
        ,
        o
        n
        e
        f
        o
        r
        e
        a
        c
        h
        u
        n
        i
        q
        u
        e
        v
        a
        l
        u
        e
        ,
        o
        r
        s
        e
        t
        o
        f
        v
        a
        l
        u
        e
        s
        ,
        i
        n
        t
        h
        e
        s
        t
        r
        a
        t
        i
        f
        i
        e
        r
        ,
        o
        r
        s
        t
        r
        a
        t
        i
        f
        i
        e
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
        s
        .
        List of `MeasureReportGroupStratifierStratum` items (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifier, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("stratum", "stratum", MeasureReportGroupStratifierStratum, True, None, False),
        ])
        return js


class MeasureReportGroupStratifierStratum(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    a
    t
    u
    m
    r
    e
    s
    u
    l
    t
    s
    ,
    o
    n
    e
    f
    o
    r
    e
    a
    c
    h
    u
    n
    i
    q
    u
    e
    v
    a
    l
    u
    e
    ,
    o
    r
    s
    e
    t
    o
    f
    v
    a
    l
    u
    e
    s
    ,
    i
    n
    t
    h
    e
    s
    t
    r
    a
    t
    i
    f
    i
    e
    r
    ,
    o
    r
    s
    t
    r
    a
    t
    i
    f
    i
    e
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
    s
    .
    
    
    T
    h
    i
    s
    e
    l
    e
    m
    e
    n
    t
    c
    o
    n
    t
    a
    i
    n
    s
    t
    h
    e
    r
    e
    s
    u
    l
    t
    s
    f
    o
    r
    a
    s
    i
    n
    g
    l
    e
    s
    t
    r
    a
    t
    u
    m
    w
    i
    t
    h
    i
    n
    t
    h
    e
    s
    t
    r
    a
    t
    i
    f
    i
    e
    r
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
    w
    h
    e
    n
    s
    t
    r
    a
    t
    i
    f
    y
    i
    n
    g
    o
    n
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
    v
    e
    g
    e
    n
    d
    e
    r
    ,
    t
    h
    e
    r
    e
    w
    i
    l
    l
    b
    e
    f
    o
    u
    r
    s
    t
    r
    a
    t
    a
    ,
    o
    n
    e
    f
    o
    r
    e
    a
    c
    h
    p
    o
    s
    s
    i
    b
    l
    e
    g
    e
    n
    d
    e
    r
    v
    a
    l
    u
    e
    .
    
    """
    
    resource_type = "MeasureReportGroupStratifierStratum"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.component = None
        """ 
        S
        t
        r
        a
        t
        i
        f
        i
        e
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
        v
        a
        l
        u
        e
        s
        .
        List of `MeasureReportGroupStratifierStratumComponent` items (represented as `dict` in JSON). """
        
        self.measureScore = None
        """ 
        W
        h
        a
        t
        s
        c
        o
        r
        e
        t
        h
        i
        s
        s
        t
        r
        a
        t
        u
        m
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.population = None
        """ 
        P
        o
        p
        u
        l
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
        i
        n
        t
        h
        i
        s
        s
        t
        r
        a
        t
        u
        m
        .
        List of `MeasureReportGroupStratifierStratumPopulation` items (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        T
        h
        e
        s
        t
        r
        a
        t
        u
        m
        v
        a
        l
        u
        e
        ,
        e
        .
        g
        .
        m
        a
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifierStratum, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratum, self).elementProperties()
        js.extend([
            ("component", "component", MeasureReportGroupStratifierStratumComponent, True, None, False),
            ("measureScore", "measureScore", quantity.Quantity, False, None, False),
            ("population", "population", MeasureReportGroupStratifierStratumPopulation, True, None, False),
            ("value", "value", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MeasureReportGroupStratifierStratumComponent(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    a
    t
    i
    f
    i
    e
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
    v
    a
    l
    u
    e
    s
    .
    
    
    A
    s
    t
    r
    a
    t
    i
    f
    i
    e
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
    v
    a
    l
    u
    e
    .
    
    """
    
    resource_type = "MeasureReportGroupStratifierStratumComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        W
        h
        a
        t
        s
        t
        r
        a
        t
        i
        f
        i
        e
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
        o
        f
        t
        h
        e
        g
        r
        o
        u
        p
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        T
        h
        e
        s
        t
        r
        a
        t
        u
        m
        c
        o
        m
        p
        o
        n
        e
        n
        t
        v
        a
        l
        u
        e
        ,
        e
        .
        g
        .
        m
        a
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifierStratumComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumComponent, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class MeasureReportGroupStratifierStratumPopulation(backboneelement.BackboneElement):
    """ 
    P
    o
    p
    u
    l
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
    i
    n
    t
    h
    i
    s
    s
    t
    r
    a
    t
    u
    m
    .
    
    
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
    s
    t
    h
    a
    t
    m
    a
    k
    e
    u
    p
    t
    h
    e
    s
    t
    r
    a
    t
    u
    m
    ,
    o
    n
    e
    f
    o
    r
    e
    a
    c
    h
    t
    y
    p
    e
    o
    f
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
    a
    p
    p
    r
    o
    p
    r
    i
    a
    t
    e
    t
    o
    t
    h
    e
    m
    e
    a
    s
    u
    r
    e
    .
    
    """
    
    resource_type = "MeasureReportGroupStratifierStratumPopulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        i
        n
        i
        t
        i
        a
        l
        -
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
        |
        n
        u
        m
        e
        r
        a
        t
        o
        r
        |
        n
        u
        m
        e
        r
        a
        t
        o
        r
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        d
        e
        n
        o
        m
        i
        n
        a
        t
        o
        r
        -
        e
        x
        c
        e
        p
        t
        i
        o
        n
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        -
        e
        x
        c
        l
        u
        s
        i
        o
        n
        |
        m
        e
        a
        s
        u
        r
        e
        -
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
        
        self.count = None
        """ 
        S
        i
        z
        e
        o
        f
        t
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
        .
        Type `int`. """
        
        self.subjectResults = None
        """ 
        F
        o
        r
        s
        u
        b
        j
        e
        c
        t
        -
        l
        i
        s
        t
        r
        e
        p
        o
        r
        t
        s
        ,
        t
        h
        e
        s
        u
        b
        j
        e
        c
        t
        r
        e
        s
        u
        l
        t
        s
        i
        n
        t
        h
        i
        s
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MeasureReportGroupStratifierStratumPopulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MeasureReportGroupStratifierStratumPopulation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("count", "count", int, False, None, False),
            ("subjectResults", "subjectResults", fhirreference.FHIRReference, False, None, False),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
