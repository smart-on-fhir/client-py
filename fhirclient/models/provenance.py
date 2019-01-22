#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Provenance) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Provenance(domainresource.DomainResource):
    """ 
    W
    h
    o
    ,
    W
    h
    a
    t
    ,
    W
    h
    e
    n
    f
    o
    r
    a
    s
    e
    t
    o
    f
    r
    e
    s
    o
    u
    r
    c
    e
    s
    .
    
    
    P
    r
    o
    v
    e
    n
    a
    n
    c
    e
    o
    f
    a
    r
    e
    s
    o
    u
    r
    c
    e
    i
    s
    a
    r
    e
    c
    o
    r
    d
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
    s
    e
    n
    t
    i
    t
    i
    e
    s
    a
    n
    d
    p
    r
    o
    c
    e
    s
    s
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
    p
    r
    o
    d
    u
    c
    i
    n
    g
    a
    n
    d
    d
    e
    l
    i
    v
    e
    r
    i
    n
    g
    o
    r
    o
    t
    h
    e
    r
    w
    i
    s
    e
    i
    n
    f
    l
    u
    e
    n
    c
    i
    n
    g
    t
    h
    a
    t
    r
    e
    s
    o
    u
    r
    c
    e
    .
    P
    r
    o
    v
    e
    n
    a
    n
    c
    e
    p
    r
    o
    v
    i
    d
    e
    s
    a
    c
    r
    i
    t
    i
    c
    a
    l
    f
    o
    u
    n
    d
    a
    t
    i
    o
    n
    f
    o
    r
    a
    s
    s
    e
    s
    s
    i
    n
    g
    a
    u
    t
    h
    e
    n
    t
    i
    c
    i
    t
    y
    ,
    e
    n
    a
    b
    l
    i
    n
    g
    t
    r
    u
    s
    t
    ,
    a
    n
    d
    a
    l
    l
    o
    w
    i
    n
    g
    r
    e
    p
    r
    o
    d
    u
    c
    i
    b
    i
    l
    i
    t
    y
    .
    P
    r
    o
    v
    e
    n
    a
    n
    c
    e
    a
    s
    s
    e
    r
    t
    i
    o
    n
    s
    a
    r
    e
    a
    f
    o
    r
    m
    o
    f
    c
    o
    n
    t
    e
    x
    t
    u
    a
    l
    m
    e
    t
    a
    d
    a
    t
    a
    a
    n
    d
    c
    a
    n
    t
    h
    e
    m
    s
    e
    l
    v
    e
    s
    b
    e
    c
    o
    m
    e
    i
    m
    p
    o
    r
    t
    a
    n
    t
    r
    e
    c
    o
    r
    d
    s
    w
    i
    t
    h
    t
    h
    e
    i
    r
    o
    w
    n
    p
    r
    o
    v
    e
    n
    a
    n
    c
    e
    .
    P
    r
    o
    v
    e
    n
    a
    n
    c
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
    i
    n
    d
    i
    c
    a
    t
    e
    s
    c
    l
    i
    n
    i
    c
    a
    l
    s
    i
    g
    n
    i
    f
    i
    c
    a
    n
    c
    e
    i
    n
    t
    e
    r
    m
    s
    o
    f
    c
    o
    n
    f
    i
    d
    e
    n
    c
    e
    i
    n
    a
    u
    t
    h
    e
    n
    t
    i
    c
    i
    t
    y
    ,
    r
    e
    l
    i
    a
    b
    i
    l
    i
    t
    y
    ,
    a
    n
    d
    t
    r
    u
    s
    t
    w
    o
    r
    t
    h
    i
    n
    e
    s
    s
    ,
    i
    n
    t
    e
    g
    r
    i
    t
    y
    ,
    a
    n
    d
    s
    t
    a
    g
    e
    i
    n
    l
    i
    f
    e
    c
    y
    c
    l
    e
    (
    e
    .
    g
    .
    D
    o
    c
    u
    m
    e
    n
    t
    C
    o
    m
    p
    l
    e
    t
    i
    o
    n
    -
    h
    a
    s
    t
    h
    e
    a
    r
    t
    i
    f
    a
    c
    t
    b
    e
    e
    n
    l
    e
    g
    a
    l
    l
    y
    a
    u
    t
    h
    e
    n
    t
    i
    c
    a
    t
    e
    d
    )
    ,
    a
    l
    l
    o
    f
    w
    h
    i
    c
    h
    m
    a
    y
    i
    m
    p
    a
    c
    t
    s
    e
    c
    u
    r
    i
    t
    y
    ,
    p
    r
    i
    v
    a
    c
    y
    ,
    a
    n
    d
    t
    r
    u
    s
    t
    p
    o
    l
    i
    c
    i
    e
    s
    .
    
    """
    
    resource_type = "Provenance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activity = None
        """ 
        A
        c
        t
        i
        v
        i
        t
        y
        t
        h
        a
        t
        o
        c
        c
        u
        r
        r
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.agent = None
        """ 
        A
        c
        t
        o
        r
        i
        n
        v
        o
        l
        v
        e
        d
        .
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        self.entity = None
        """ 
        A
        n
        e
        n
        t
        i
        t
        y
        u
        s
        e
        d
        i
        n
        t
        h
        i
        s
        a
        c
        t
        i
        v
        i
        t
        y
        .
        List of `ProvenanceEntity` items (represented as `dict` in JSON). """
        
        self.location = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        o
        c
        c
        u
        r
        r
        e
        d
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.occurredDateTime = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        o
        c
        c
        u
        r
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurredPeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        o
        c
        c
        u
        r
        r
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.policy = None
        """ 
        P
        o
        l
        i
        c
        y
        o
        r
        p
        l
        a
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        w
        a
        s
        d
        e
        f
        i
        n
        e
        d
        b
        y
        .
        List of `str` items. """
        
        self.reason = None
        """ 
        R
        e
        a
        s
        o
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        i
        s
        o
        c
        c
        u
        r
        r
        i
        n
        g
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recorded = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        /
        u
        p
        d
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.signature = None
        """ 
        S
        i
        g
        n
        a
        t
        u
        r
        e
        o
        n
        t
        a
        r
        g
        e
        t
        .
        List of `Signature` items (represented as `dict` in JSON). """
        
        self.target = None
        """ 
        T
        a
        r
        g
        e
        t
        R
        e
        f
        e
        r
        e
        n
        c
        e
        (
        s
        )
        (
        u
        s
        u
        a
        l
        l
        y
        v
        e
        r
        s
        i
        o
        n
        s
        p
        e
        c
        i
        f
        i
        c
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Provenance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Provenance, self).elementProperties()
        js.extend([
            ("activity", "activity", codeableconcept.CodeableConcept, False, None, False),
            ("agent", "agent", ProvenanceAgent, True, None, True),
            ("entity", "entity", ProvenanceEntity, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("occurredDateTime", "occurredDateTime", fhirdate.FHIRDate, False, "occurred", False),
            ("occurredPeriod", "occurredPeriod", period.Period, False, "occurred", False),
            ("policy", "policy", str, True, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, True),
            ("signature", "signature", signature.Signature, True, None, False),
            ("target", "target", fhirreference.FHIRReference, True, None, True),
        ])
        return js


from . import backboneelement

class ProvenanceAgent(backboneelement.BackboneElement):
    """ 
    A
    c
    t
    o
    r
    i
    n
    v
    o
    l
    v
    e
    d
    .
    
    
    A
    n
    a
    c
    t
    o
    r
    t
    a
    k
    i
    n
    g
    a
    r
    o
    l
    e
    i
    n
    a
    n
    a
    c
    t
    i
    v
    i
    t
    y
    f
    o
    r
    w
    h
    i
    c
    h
    i
    t
    c
    a
    n
    b
    e
    a
    s
    s
    i
    g
    n
    e
    d
    s
    o
    m
    e
    d
    e
    g
    r
    e
    e
    o
    f
    r
    e
    s
    p
    o
    n
    s
    i
    b
    i
    l
    i
    t
    y
    f
    o
    r
    t
    h
    e
    a
    c
    t
    i
    v
    i
    t
    y
    t
    a
    k
    i
    n
    g
    p
    l
    a
    c
    e
    .
    
    """
    
    resource_type = "ProvenanceAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.onBehalfOf = None
        """ 
        W
        h
        o
        t
        h
        e
        a
        g
        e
        n
        t
        i
        s
        r
        e
        p
        r
        e
        s
        e
        n
        t
        i
        n
        g
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        W
        h
        a
        t
        t
        h
        e
        a
        g
        e
        n
        t
        s
        r
        o
        l
        e
        w
        a
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        H
        o
        w
        t
        h
        e
        a
        g
        e
        n
        t
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.who = None
        """ 
        W
        h
        o
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProvenanceAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ProvenanceEntity(backboneelement.BackboneElement):
    """ 
    A
    n
    e
    n
    t
    i
    t
    y
    u
    s
    e
    d
    i
    n
    t
    h
    i
    s
    a
    c
    t
    i
    v
    i
    t
    y
    .
    """
    
    resource_type = "ProvenanceEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.agent = None
        """ 
        E
        n
        t
        i
        t
        y
        i
        s
        a
        t
        t
        r
        i
        b
        u
        t
        e
        d
        t
        o
        t
        h
        i
        s
        a
        g
        e
        n
        t
        .
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        d
        e
        r
        i
        v
        a
        t
        i
        o
        n
        |
        r
        e
        v
        i
        s
        i
        o
        n
        |
        q
        u
        o
        t
        a
        t
        i
        o
        n
        |
        s
        o
        u
        r
        c
        e
        |
        r
        e
        m
        o
        v
        a
        l
        .
        Type `str`. """
        
        self.what = None
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
        e
        n
        t
        i
        t
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProvenanceEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("agent", "agent", ProvenanceAgent, True, None, False),
            ("role", "role", str, False, None, True),
            ("what", "what", fhirreference.FHIRReference, False, None, True),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
