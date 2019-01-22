#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Timing) on 2019-01-22.
#  2019, SMART Health IT.


from . import backboneelement

class Timing(backboneelement.BackboneElement):
    """ 
    A
    t
    i
    m
    i
    n
    g
    s
    c
    h
    e
    d
    u
    l
    e
    t
    h
    a
    t
    s
    p
    e
    c
    i
    f
    i
    e
    s
    a
    n
    e
    v
    e
    n
    t
    t
    h
    a
    t
    m
    a
    y
    o
    c
    c
    u
    r
    m
    u
    l
    t
    i
    p
    l
    e
    t
    i
    m
    e
    s
    .
    
    
    S
    p
    e
    c
    i
    f
    i
    e
    s
    a
    n
    e
    v
    e
    n
    t
    t
    h
    a
    t
    m
    a
    y
    o
    c
    c
    u
    r
    m
    u
    l
    t
    i
    p
    l
    e
    t
    i
    m
    e
    s
    .
    T
    i
    m
    i
    n
    g
    s
    c
    h
    e
    d
    u
    l
    e
    s
    a
    r
    e
    u
    s
    e
    d
    t
    o
    r
    e
    c
    o
    r
    d
    w
    h
    e
    n
    t
    h
    i
    n
    g
    s
    a
    r
    e
    p
    l
    a
    n
    n
    e
    d
    ,
    e
    x
    p
    e
    c
    t
    e
    d
    o
    r
    r
    e
    q
    u
    e
    s
    t
    e
    d
    t
    o
    o
    c
    c
    u
    r
    .
    T
    h
    e
    m
    o
    s
    t
    c
    o
    m
    m
    o
    n
    u
    s
    a
    g
    e
    i
    s
    i
    n
    d
    o
    s
    a
    g
    e
    i
    n
    s
    t
    r
    u
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
    T
    h
    e
    y
    a
    r
    e
    a
    l
    s
    o
    u
    s
    e
    d
    w
    h
    e
    n
    p
    l
    a
    n
    n
    i
    n
    g
    c
    a
    r
    e
    o
    f
    v
    a
    r
    i
    o
    u
    s
    k
    i
    n
    d
    s
    ,
    a
    n
    d
    m
    a
    y
    b
    e
    u
    s
    e
    d
    f
    o
    r
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
    s
    c
    h
    e
    d
    u
    l
    e
    t
    o
    w
    h
    i
    c
    h
    p
    a
    s
    t
    r
    e
    g
    u
    l
    a
    r
    a
    c
    t
    i
    v
    i
    t
    i
    e
    s
    w
    e
    r
    e
    c
    a
    r
    r
    i
    e
    d
    o
    u
    t
    .
    
    """
    
    resource_type = "Timing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        B
        I
        D
        |
        T
        I
        D
        |
        Q
        I
        D
        |
        A
        M
        |
        P
        M
        |
        Q
        D
        |
        Q
        O
        D
        |
        +
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.event = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        e
        v
        e
        n
        t
        o
        c
        c
        u
        r
        s
        .
        List of `FHIRDate` items (represented as `str` in JSON). """
        
        self.repeat = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        e
        v
        e
        n
        t
        i
        s
        t
        o
        o
        c
        c
        u
        r
        .
        Type `TimingRepeat` (represented as `dict` in JSON). """
        
        super(Timing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("event", "event", fhirdate.FHIRDate, True, None, False),
            ("repeat", "repeat", TimingRepeat, False, None, False),
        ])
        return js


from . import element

class TimingRepeat(element.Element):
    """ 
    W
    h
    e
    n
    t
    h
    e
    e
    v
    e
    n
    t
    i
    s
    t
    o
    o
    c
    c
    u
    r
    .
    
    
    A
    s
    e
    t
    o
    f
    r
    u
    l
    e
    s
    t
    h
    a
    t
    d
    e
    s
    c
    r
    i
    b
    e
    w
    h
    e
    n
    t
    h
    e
    e
    v
    e
    n
    t
    i
    s
    s
    c
    h
    e
    d
    u
    l
    e
    d
    .
    
    """
    
    resource_type = "TimingRepeat"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.boundsDuration = None
        """ 
        L
        e
        n
        g
        t
        h
        /
        R
        a
        n
        g
        e
        o
        f
        l
        e
        n
        g
        t
        h
        s
        ,
        o
        r
        (
        S
        t
        a
        r
        t
        a
        n
        d
        /
        o
        r
        e
        n
        d
        )
        l
        i
        m
        i
        t
        s
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.boundsPeriod = None
        """ 
        L
        e
        n
        g
        t
        h
        /
        R
        a
        n
        g
        e
        o
        f
        l
        e
        n
        g
        t
        h
        s
        ,
        o
        r
        (
        S
        t
        a
        r
        t
        a
        n
        d
        /
        o
        r
        e
        n
        d
        )
        l
        i
        m
        i
        t
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.boundsRange = None
        """ 
        L
        e
        n
        g
        t
        h
        /
        R
        a
        n
        g
        e
        o
        f
        l
        e
        n
        g
        t
        h
        s
        ,
        o
        r
        (
        S
        t
        a
        r
        t
        a
        n
        d
        /
        o
        r
        e
        n
        d
        )
        l
        i
        m
        i
        t
        s
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.count = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        t
        i
        m
        e
        s
        t
        o
        r
        e
        p
        e
        a
        t
        .
        Type `int`. """
        
        self.countMax = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        n
        u
        m
        b
        e
        r
        o
        f
        t
        i
        m
        e
        s
        t
        o
        r
        e
        p
        e
        a
        t
        .
        Type `int`. """
        
        self.dayOfWeek = None
        """ 
        m
        o
        n
        |
        t
        u
        e
        |
        w
        e
        d
        |
        t
        h
        u
        |
        f
        r
        i
        |
        s
        a
        t
        |
        s
        u
        n
        .
        List of `str` items. """
        
        self.duration = None
        """ 
        H
        o
        w
        l
        o
        n
        g
        w
        h
        e
        n
        i
        t
        h
        a
        p
        p
        e
        n
        s
        .
        Type `float`. """
        
        self.durationMax = None
        """ 
        H
        o
        w
        l
        o
        n
        g
        w
        h
        e
        n
        i
        t
        h
        a
        p
        p
        e
        n
        s
        (
        M
        a
        x
        )
        .
        Type `float`. """
        
        self.durationUnit = None
        """ 
        s
        |
        m
        i
        n
        |
        h
        |
        d
        |
        w
        k
        |
        m
        o
        |
        a
        -
        u
        n
        i
        t
        o
        f
        t
        i
        m
        e
        (
        U
        C
        U
        M
        )
        .
        Type `str`. """
        
        self.frequency = None
        """ 
        E
        v
        e
        n
        t
        o
        c
        c
        u
        r
        s
        f
        r
        e
        q
        u
        e
        n
        c
        y
        t
        i
        m
        e
        s
        p
        e
        r
        p
        e
        r
        i
        o
        d
        .
        Type `int`. """
        
        self.frequencyMax = None
        """ 
        E
        v
        e
        n
        t
        o
        c
        c
        u
        r
        s
        u
        p
        t
        o
        f
        r
        e
        q
        u
        e
        n
        c
        y
        M
        a
        x
        t
        i
        m
        e
        s
        p
        e
        r
        p
        e
        r
        i
        o
        d
        .
        Type `int`. """
        
        self.offset = None
        """ 
        M
        i
        n
        u
        t
        e
        s
        f
        r
        o
        m
        e
        v
        e
        n
        t
        (
        b
        e
        f
        o
        r
        e
        o
        r
        a
        f
        t
        e
        r
        )
        .
        Type `int`. """
        
        self.period = None
        """ 
        E
        v
        e
        n
        t
        o
        c
        c
        u
        r
        s
        f
        r
        e
        q
        u
        e
        n
        c
        y
        t
        i
        m
        e
        s
        p
        e
        r
        p
        e
        r
        i
        o
        d
        .
        Type `float`. """
        
        self.periodMax = None
        """ 
        U
        p
        p
        e
        r
        l
        i
        m
        i
        t
        o
        f
        p
        e
        r
        i
        o
        d
        (
        3
        -
        4
        h
        o
        u
        r
        s
        )
        .
        Type `float`. """
        
        self.periodUnit = None
        """ 
        s
        |
        m
        i
        n
        |
        h
        |
        d
        |
        w
        k
        |
        m
        o
        |
        a
        -
        u
        n
        i
        t
        o
        f
        t
        i
        m
        e
        (
        U
        C
        U
        M
        )
        .
        Type `str`. """
        
        self.timeOfDay = None
        """ 
        T
        i
        m
        e
        o
        f
        d
        a
        y
        f
        o
        r
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRDate` items (represented as `str` in JSON). """
        
        self.when = None
        """ 
        C
        o
        d
        e
        f
        o
        r
        t
        i
        m
        e
        p
        e
        r
        i
        o
        d
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
        .
        List of `str` items. """
        
        super(TimingRepeat, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("boundsDuration", "boundsDuration", duration.Duration, False, "bounds", False),
            ("boundsPeriod", "boundsPeriod", period.Period, False, "bounds", False),
            ("boundsRange", "boundsRange", range.Range, False, "bounds", False),
            ("count", "count", int, False, None, False),
            ("countMax", "countMax", int, False, None, False),
            ("dayOfWeek", "dayOfWeek", str, True, None, False),
            ("duration", "duration", float, False, None, False),
            ("durationMax", "durationMax", float, False, None, False),
            ("durationUnit", "durationUnit", str, False, None, False),
            ("frequency", "frequency", int, False, None, False),
            ("frequencyMax", "frequencyMax", int, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("period", "period", float, False, None, False),
            ("periodMax", "periodMax", float, False, None, False),
            ("periodUnit", "periodUnit", str, False, None, False),
            ("timeOfDay", "timeOfDay", fhirdate.FHIRDate, True, None, False),
            ("when", "when", str, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
