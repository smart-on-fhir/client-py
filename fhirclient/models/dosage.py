#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Dosage) on 2019-01-22.
#  2019, SMART Health IT.


from . import backboneelement

class Dosage(backboneelement.BackboneElement):
    """ 
    H
    o
    w
    t
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
    i
    s
    /
    w
    a
    s
    t
    a
    k
    e
    n
    o
    r
    s
    h
    o
    u
    l
    d
    b
    e
    t
    a
    k
    e
    n
    .
    
    
    I
    n
    d
    i
    c
    a
    t
    e
    s
    h
    o
    w
    t
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
    i
    s
    /
    w
    a
    s
    t
    a
    k
    e
    n
    o
    r
    s
    h
    o
    u
    l
    d
    b
    e
    t
    a
    k
    e
    n
    b
    y
    t
    h
    e
    p
    a
    t
    i
    e
    n
    t
    .
    
    """
    
    resource_type = "Dosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalInstruction = None
        """ 
        S
        u
        p
        p
        l
        e
        m
        e
        n
        t
        a
        l
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
        o
        r
        w
        a
        r
        n
        i
        n
        g
        s
        t
        o
        t
        h
        e
        p
        a
        t
        i
        e
        n
        t
        -
        e
        .
        g
        .
        "
        w
        i
        t
        h
        m
        e
        a
        l
        s
        "
        ,
        "
        m
        a
        y
        c
        a
        u
        s
        e
        d
        r
        o
        w
        s
        i
        n
        e
        s
        s
        "
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ 
        T
        a
        k
        e
        "
        a
        s
        n
        e
        e
        d
        e
        d
        "
        (
        f
        o
        r
        x
        )
        .
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ 
        T
        a
        k
        e
        "
        a
        s
        n
        e
        e
        d
        e
        d
        "
        (
        f
        o
        r
        x
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseAndRate = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
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
        e
        d
        .
        List of `DosageDoseAndRate` items (represented as `dict` in JSON). """
        
        self.maxDosePerAdministration = None
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
        p
        e
        r
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
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerLifetime = None
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
        p
        e
        r
        l
        i
        f
        e
        t
        i
        m
        e
        o
        f
        t
        h
        e
        p
        a
        t
        i
        e
        n
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
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
        p
        e
        r
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
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ 
        T
        e
        c
        h
        n
        i
        q
        u
        e
        f
        o
        r
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
        i
        n
        g
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patientInstruction = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        o
        r
        c
        o
        n
        s
        u
        m
        e
        r
        o
        r
        i
        e
        n
        t
        e
        d
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
        .
        Type `str`. """
        
        self.route = None
        """ 
        H
        o
        w
        d
        r
        u
        g
        s
        h
        o
        u
        l
        d
        e
        n
        t
        e
        r
        b
        o
        d
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ 
        T
        h
        e
        o
        r
        d
        e
        r
        o
        f
        t
        h
        e
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
        .
        Type `int`. """
        
        self.site = None
        """ 
        B
        o
        d
        y
        s
        i
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
        t
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        F
        r
        e
        e
        t
        e
        x
        t
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
        e
        .
        g
        .
        S
        I
        G
        .
        Type `str`. """
        
        self.timing = None
        """ 
        W
        h
        e
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
        s
        h
        o
        u
        l
        d
        b
        e
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
        e
        d
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        super(Dosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Dosage, self).elementProperties()
        js.extend([
            ("additionalInstruction", "additionalInstruction", codeableconcept.CodeableConcept, True, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("doseAndRate", "doseAndRate", DosageDoseAndRate, True, None, False),
            ("maxDosePerAdministration", "maxDosePerAdministration", quantity.Quantity, False, None, False),
            ("maxDosePerLifetime", "maxDosePerLifetime", quantity.Quantity, False, None, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
        ])
        return js


from . import element

class DosageDoseAndRate(element.Element):
    """ 
    A
    m
    o
    u
    n
    t
    o
    f
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
    e
    d
    .
    
    
    T
    h
    e
    a
    m
    o
    u
    n
    t
    o
    f
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
    e
    d
    .
    
    """
    
    resource_type = "DosageDoseAndRate"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doseQuantity = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
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
        p
        e
        r
        d
        o
        s
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.doseRange = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
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
        p
        e
        r
        d
        o
        s
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
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
        p
        e
        r
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
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
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
        p
        e
        r
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
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
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
        p
        e
        r
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
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        h
        e
        k
        i
        n
        d
        o
        f
        d
        o
        s
        e
        o
        r
        r
        a
        t
        e
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DosageDoseAndRate, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DosageDoseAndRate, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
