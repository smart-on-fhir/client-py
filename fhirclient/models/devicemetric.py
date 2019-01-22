#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DeviceMetric(domainresource.DomainResource):
    """ 
    M
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
    ,
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
    r
    s
    e
    t
    t
    i
    n
    g
    c
    a
    p
    a
    b
    i
    l
    i
    t
    y
    o
    f
    a
    m
    e
    d
    i
    c
    a
    l
    d
    e
    v
    i
    c
    e
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
    ,
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
    r
    s
    e
    t
    t
    i
    n
    g
    c
    a
    p
    a
    b
    i
    l
    i
    t
    y
    o
    f
    a
    m
    e
    d
    i
    c
    a
    l
    d
    e
    v
    i
    c
    e
    .
    
    """
    
    resource_type = "DeviceMetric"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.calibration = None
        """ 
        D
        e
        s
        c
        r
        i
        b
        e
        s
        t
        h
        e
        c
        a
        l
        i
        b
        r
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
        h
        a
        v
        e
        b
        e
        e
        n
        p
        e
        r
        f
        o
        r
        m
        e
        d
        o
        r
        t
        h
        a
        t
        a
        r
        e
        r
        e
        q
        u
        i
        r
        e
        d
        t
        o
        b
        e
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
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
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
        |
        s
        e
        t
        t
        i
        n
        g
        |
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
        |
        u
        n
        s
        p
        e
        c
        i
        f
        i
        e
        d
        .
        Type `str`. """
        
        self.color = None
        """ 
        b
        l
        a
        c
        k
        |
        r
        e
        d
        |
        g
        r
        e
        e
        n
        |
        y
        e
        l
        l
        o
        w
        |
        b
        l
        u
        e
        |
        m
        a
        g
        e
        n
        t
        a
        |
        c
        y
        a
        n
        |
        w
        h
        i
        t
        e
        .
        Type `str`. """
        
        self.identifier = None
        """ 
        I
        n
        s
        t
        a
        n
        c
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
        
        self.measurementPeriod = None
        """ 
        D
        e
        s
        c
        r
        i
        b
        e
        s
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
        m
        e
        n
        t
        r
        e
        p
        e
        t
        i
        t
        i
        o
        n
        t
        i
        m
        e
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.operationalStatus = None
        """ 
        o
        n
        |
        o
        f
        f
        |
        s
        t
        a
        n
        d
        b
        y
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
        
        self.parent = None
        """ 
        D
        e
        s
        c
        r
        i
        b
        e
        s
        t
        h
        e
        l
        i
        n
        k
        t
        o
        t
        h
        e
        p
        a
        r
        e
        n
        t
        D
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        D
        e
        s
        c
        r
        i
        b
        e
        s
        t
        h
        e
        l
        i
        n
        k
        t
        o
        t
        h
        e
        s
        o
        u
        r
        c
        e
        D
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        I
        d
        e
        n
        t
        i
        t
        y
        o
        f
        m
        e
        t
        r
        i
        c
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
        H
        e
        a
        r
        t
        R
        a
        t
        e
        o
        r
        P
        E
        E
        P
        S
        e
        t
        t
        i
        n
        g
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ 
        U
        n
        i
        t
        o
        f
        M
        e
        a
        s
        u
        r
        e
        f
        o
        r
        t
        h
        e
        M
        e
        t
        r
        i
        c
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False),
            ("category", "category", str, False, None, True),
            ("color", "color", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("measurementPeriod", "measurementPeriod", timing.Timing, False, None, False),
            ("operationalStatus", "operationalStatus", str, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ 
    D
    e
    s
    c
    r
    i
    b
    e
    s
    t
    h
    e
    c
    a
    l
    i
    b
    r
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
    h
    a
    v
    e
    b
    e
    e
    n
    p
    e
    r
    f
    o
    r
    m
    e
    d
    o
    r
    t
    h
    a
    t
    a
    r
    e
    r
    e
    q
    u
    i
    r
    e
    d
    t
    o
    b
    e
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
    """
    
    resource_type = "DeviceMetricCalibration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.state = None
        """ 
        n
        o
        t
        -
        c
        a
        l
        i
        b
        r
        a
        t
        e
        d
        |
        c
        a
        l
        i
        b
        r
        a
        t
        i
        o
        n
        -
        r
        e
        q
        u
        i
        r
        e
        d
        |
        c
        a
        l
        i
        b
        r
        a
        t
        e
        d
        |
        u
        n
        s
        p
        e
        c
        i
        f
        i
        e
        d
        .
        Type `str`. """
        
        self.time = None
        """ 
        D
        e
        s
        c
        r
        i
        b
        e
        s
        t
        h
        e
        t
        i
        m
        e
        l
        a
        s
        t
        c
        a
        l
        i
        b
        r
        a
        t
        i
        o
        n
        h
        a
        s
        b
        e
        e
        n
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
        
        self.type = None
        """ 
        u
        n
        s
        p
        e
        c
        i
        f
        i
        e
        d
        |
        o
        f
        f
        s
        e
        t
        |
        g
        a
        i
        n
        |
        t
        w
        o
        -
        p
        o
        i
        n
        t
        .
        Type `str`. """
        
        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("state", "state", str, False, None, False),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
            ("type", "type", str, False, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
