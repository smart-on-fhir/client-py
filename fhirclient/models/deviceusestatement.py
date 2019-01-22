#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ 
    R
    e
    c
    o
    r
    d
    o
    f
    u
    s
    e
    o
    f
    a
    d
    e
    v
    i
    c
    e
    .
    
    
    A
    r
    e
    c
    o
    r
    d
    o
    f
    a
    d
    e
    v
    i
    c
    e
    b
    e
    i
    n
    g
    u
    s
    e
    d
    b
    y
    a
    p
    a
    t
    i
    e
    n
    t
    w
    h
    e
    r
    e
    t
    h
    e
    r
    e
    c
    o
    r
    d
    i
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
    o
    f
    a
    r
    e
    p
    o
    r
    t
    f
    r
    o
    m
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
    o
    r
    a
    n
    o
    t
    h
    e
    r
    c
    l
    i
    n
    i
    c
    i
    a
    n
    .
    
    """
    
    resource_type = "DeviceUseStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ 
        F
        u
        l
        f
        i
        l
        l
        s
        p
        l
        a
        n
        ,
        p
        r
        o
        p
        o
        s
        a
        l
        o
        r
        o
        r
        d
        e
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ 
        T
        a
        r
        g
        e
        t
        b
        o
        d
        y
        s
        i
        t
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.derivedFrom = None
        """ 
        S
        u
        p
        p
        o
        r
        t
        i
        n
        g
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.device = None
        """ 
        R
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
        d
        e
        v
        i
        c
        e
        u
        s
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        E
        x
        t
        e
        r
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
        i
        s
        r
        e
        c
        o
        r
        d
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ 
        A
        d
        d
        i
        t
        i
        o
        n
        d
        e
        t
        a
        i
        l
        s
        (
        c
        o
        m
        m
        e
        n
        t
        s
        ,
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
        )
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        d
        e
        v
        i
        c
        e
        w
        a
        s
        u
        s
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        w
        a
        s
        D
        e
        v
        i
        c
        e
        U
        s
        e
        S
        t
        a
        t
        e
        m
        e
        n
        t
        p
        e
        r
        f
        o
        r
        m
        e
        d
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recordedOn = None
        """ 
        W
        h
        e
        n
        s
        t
        a
        t
        e
        m
        e
        n
        t
        w
        a
        s
        r
        e
        c
        o
        r
        d
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.source = None
        """ 
        W
        h
        o
        m
        a
        d
        e
        t
        h
        e
        s
        t
        a
        t
        e
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
        |
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
        +
        .
        Type `str`. """
        
        self.subject = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        u
        s
        i
        n
        g
        d
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ 
        H
        o
        w
        o
        f
        t
        e
        n
        t
        h
        e
        d
        e
        v
        i
        c
        e
        w
        a
        s
        u
        s
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ 
        H
        o
        w
        o
        f
        t
        e
        n
        t
        h
        e
        d
        e
        v
        i
        c
        e
        w
        a
        s
        u
        s
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ 
        H
        o
        w
        o
        f
        t
        e
        n
        t
        h
        e
        d
        e
        v
        i
        c
        e
        w
        a
        s
        u
        s
        e
        d
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("derivedFrom", "derivedFrom", fhirreference.FHIRReference, True, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
