#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TriggerDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class TriggerDefinition(element.Element):
    """ 
    D
    e
    f
    i
    n
    e
    s
    a
    n
    e
    x
    p
    e
    c
    t
    e
    d
    t
    r
    i
    g
    g
    e
    r
    f
    o
    r
    a
    m
    o
    d
    u
    l
    e
    .
    
    
    A
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
    a
    t
    r
    i
    g
    g
    e
    r
    i
    n
    g
    e
    v
    e
    n
    t
    .
    T
    r
    i
    g
    g
    e
    r
    i
    n
    g
    e
    v
    e
    n
    t
    s
    c
    a
    n
    b
    e
    n
    a
    m
    e
    d
    e
    v
    e
    n
    t
    s
    ,
    d
    a
    t
    a
    e
    v
    e
    n
    t
    s
    ,
    o
    r
    p
    e
    r
    i
    o
    d
    i
    c
    ,
    a
    s
    d
    e
    t
    e
    r
    m
    i
    n
    e
    d
    b
    y
    t
    h
    e
    t
    y
    p
    e
    e
    l
    e
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "TriggerDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        e
        e
        v
        e
        n
        t
        t
        r
        i
        g
        g
        e
        r
        s
        (
        b
        o
        o
        l
        e
        a
        n
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        )
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.data = None
        """ 
        T
        r
        i
        g
        g
        e
        r
        i
        n
        g
        d
        a
        t
        a
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        (
        m
        u
        l
        t
        i
        p
        l
        e
        =
        '
        a
        n
        d
        '
        )
        .
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        r
        U
        R
        I
        t
        h
        a
        t
        i
        d
        e
        n
        t
        i
        f
        i
        e
        s
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `str`. """
        
        self.timingDate = None
        """ 
        T
        i
        m
        i
        n
        g
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDateTime = None
        """ 
        T
        i
        m
        i
        n
        g
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingReference = None
        """ 
        T
        i
        m
        i
        n
        g
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ 
        T
        i
        m
        i
        n
        g
        o
        f
        t
        h
        e
        e
        v
        e
        n
        t
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        n
        a
        m
        e
        d
        -
        e
        v
        e
        n
        t
        |
        p
        e
        r
        i
        o
        d
        i
        c
        |
        d
        a
        t
        a
        -
        c
        h
        a
        n
        g
        e
        d
        |
        d
        a
        t
        a
        -
        a
        d
        d
        e
        d
        |
        d
        a
        t
        a
        -
        m
        o
        d
        i
        f
        i
        e
        d
        |
        d
        a
        t
        a
        -
        r
        e
        m
        o
        v
        e
        d
        |
        d
        a
        t
        a
        -
        a
        c
        c
        e
        s
        s
        e
        d
        |
        d
        a
        t
        a
        -
        a
        c
        c
        e
        s
        s
        -
        e
        n
        d
        e
        d
        .
        Type `str`. """
        
        super(TriggerDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TriggerDefinition, self).elementProperties()
        js.extend([
            ("condition", "condition", expression.Expression, False, None, False),
            ("data", "data", datarequirement.DataRequirement, True, None, False),
            ("name", "name", str, False, None, False),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingReference", "timingReference", fhirreference.FHIRReference, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
