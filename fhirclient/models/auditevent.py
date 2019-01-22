#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class AuditEvent(domainresource.DomainResource):
    """ 
    E
    v
    e
    n
    t
    r
    e
    c
    o
    r
    d
    k
    e
    p
    t
    f
    o
    r
    s
    e
    c
    u
    r
    i
    t
    y
    p
    u
    r
    p
    o
    s
    e
    s
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
    n
    e
    v
    e
    n
    t
    m
    a
    d
    e
    f
    o
    r
    p
    u
    r
    p
    o
    s
    e
    s
    o
    f
    m
    a
    i
    n
    t
    a
    i
    n
    i
    n
    g
    a
    s
    e
    c
    u
    r
    i
    t
    y
    l
    o
    g
    .
    T
    y
    p
    i
    c
    a
    l
    u
    s
    e
    s
    i
    n
    c
    l
    u
    d
    e
    d
    e
    t
    e
    c
    t
    i
    o
    n
    o
    f
    i
    n
    t
    r
    u
    s
    i
    o
    n
    a
    t
    t
    e
    m
    p
    t
    s
    a
    n
    d
    m
    o
    n
    i
    t
    o
    r
    i
    n
    g
    f
    o
    r
    i
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
    u
    s
    a
    g
    e
    .
    
    """
    
    resource_type = "AuditEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        T
        y
        p
        e
        o
        f
        a
        c
        t
        i
        o
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
        d
        u
        r
        i
        n
        g
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
        i
        n
        t
        h
        e
        e
        v
        e
        n
        t
        .
        List of `AuditEventAgent` items (represented as `dict` in JSON). """
        
        self.entity = None
        """ 
        D
        a
        t
        a
        o
        r
        o
        b
        j
        e
        c
        t
        s
        u
        s
        e
        d
        .
        List of `AuditEventEntity` items (represented as `dict` in JSON). """
        
        self.outcome = None
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
        s
        u
        c
        c
        e
        e
        d
        e
        d
        o
        r
        f
        a
        i
        l
        e
        d
        .
        Type `str`. """
        
        self.outcomeDesc = None
        """ 
        D
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
        t
        h
        e
        e
        v
        e
        n
        t
        o
        u
        t
        c
        o
        m
        e
        .
        Type `str`. """
        
        self.period = None
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
        
        self.purposeOfEvent = None
        """ 
        T
        h
        e
        p
        u
        r
        p
        o
        s
        e
        O
        f
        U
        s
        e
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recorded = None
        """ 
        T
        i
        m
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
        A
        u
        d
        i
        t
        E
        v
        e
        n
        t
        R
        e
        p
        o
        r
        t
        e
        r
        .
        Type `AuditEventSource` (represented as `dict` in JSON). """
        
        self.subtype = None
        """ 
        M
        o
        r
        e
        s
        p
        e
        c
        i
        f
        i
        c
        t
        y
        p
        e
        /
        i
        d
        f
        o
        r
        t
        h
        e
        e
        v
        e
        n
        t
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        /
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
        o
        f
        e
        v
        e
        n
        t
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        super(AuditEvent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, False),
            ("agent", "agent", AuditEventAgent, True, None, True),
            ("entity", "entity", AuditEventEntity, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", codeableconcept.CodeableConcept, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, True),
            ("source", "source", AuditEventSource, False, None, True),
            ("subtype", "subtype", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


from . import backboneelement

class AuditEventAgent(backboneelement.BackboneElement):
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
    i
    n
    t
    h
    e
    e
    v
    e
    n
    t
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
    n
    a
    c
    t
    i
    v
    e
    r
    o
    l
    e
    i
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
    r
    a
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
    i
    s
    l
    o
    g
    g
    e
    d
    .
    
    """
    
    resource_type = "AuditEventAgent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altId = None
        """ 
        A
        l
        t
        e
        r
        n
        a
        t
        i
        v
        e
        U
        s
        e
        r
        i
        d
        e
        n
        t
        i
        t
        y
        .
        Type `str`. """
        
        self.location = None
        """ 
        W
        h
        e
        r
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.media = None
        """ 
        T
        y
        p
        e
        o
        f
        m
        e
        d
        i
        a
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        H
        u
        m
        a
        n
        f
        r
        i
        e
        n
        d
        l
        y
        n
        a
        m
        e
        f
        o
        r
        t
        h
        e
        a
        g
        e
        n
        t
        .
        Type `str`. """
        
        self.network = None
        """ 
        L
        o
        g
        i
        c
        a
        l
        n
        e
        t
        w
        o
        r
        k
        l
        o
        c
        a
        t
        i
        o
        n
        f
        o
        r
        a
        p
        p
        l
        i
        c
        a
        t
        i
        o
        n
        a
        c
        t
        i
        v
        i
        t
        y
        .
        Type `AuditEventAgentNetwork` (represented as `dict` in JSON). """
        
        self.policy = None
        """ 
        P
        o
        l
        i
        c
        y
        t
        h
        a
        t
        a
        u
        t
        h
        o
        r
        i
        z
        e
        d
        e
        v
        e
        n
        t
        .
        List of `str` items. """
        
        self.purposeOfUse = None
        """ 
        R
        e
        a
        s
        o
        n
        g
        i
        v
        e
        n
        f
        o
        r
        t
        h
        i
        s
        u
        s
        e
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requestor = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        u
        s
        e
        r
        i
        s
        i
        n
        i
        t
        i
        a
        t
        o
        r
        .
        Type `bool`. """
        
        self.role = None
        """ 
        A
        g
        e
        n
        t
        r
        o
        l
        e
        i
        n
        t
        h
        e
        e
        v
        e
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        H
        o
        w
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
        I
        d
        e
        n
        t
        i
        f
        i
        e
        r
        o
        f
        w
        h
        o
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(AuditEventAgent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventAgent, self).elementProperties()
        js.extend([
            ("altId", "altId", str, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("media", "media", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", AuditEventAgentNetwork, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("purposeOfUse", "purposeOfUse", codeableconcept.CodeableConcept, True, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class AuditEventAgentNetwork(backboneelement.BackboneElement):
    """ 
    L
    o
    g
    i
    c
    a
    l
    n
    e
    t
    w
    o
    r
    k
    l
    o
    c
    a
    t
    i
    o
    n
    f
    o
    r
    a
    p
    p
    l
    i
    c
    a
    t
    i
    o
    n
    a
    c
    t
    i
    v
    i
    t
    y
    .
    
    
    L
    o
    g
    i
    c
    a
    l
    n
    e
    t
    w
    o
    r
    k
    l
    o
    c
    a
    t
    i
    o
    n
    f
    o
    r
    a
    p
    p
    l
    i
    c
    a
    t
    i
    o
    n
    a
    c
    t
    i
    v
    i
    t
    y
    ,
    i
    f
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
    h
    a
    s
    a
    n
    e
    t
    w
    o
    r
    k
    l
    o
    c
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "AuditEventAgentNetwork"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ 
        I
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
        n
        e
        t
        w
        o
        r
        k
        a
        c
        c
        e
        s
        s
        p
        o
        i
        n
        t
        o
        f
        t
        h
        e
        u
        s
        e
        r
        d
        e
        v
        i
        c
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        n
        e
        t
        w
        o
        r
        k
        a
        c
        c
        e
        s
        s
        p
        o
        i
        n
        t
        .
        Type `str`. """
        
        super(AuditEventAgentNetwork, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventAgentNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class AuditEventEntity(backboneelement.BackboneElement):
    """ 
    D
    a
    t
    a
    o
    r
    o
    b
    j
    e
    c
    t
    s
    u
    s
    e
    d
    .
    
    
    S
    p
    e
    c
    i
    f
    i
    c
    i
    n
    s
    t
    a
    n
    c
    e
    s
    o
    f
    d
    a
    t
    a
    o
    r
    o
    b
    j
    e
    c
    t
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
    a
    c
    c
    e
    s
    s
    e
    d
    .
    
    """
    
    resource_type = "AuditEventEntity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        D
        e
        s
        c
        r
        i
        p
        t
        i
        v
        e
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.detail = None
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
        I
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
        a
        b
        o
        u
        t
        t
        h
        e
        e
        n
        t
        i
        t
        y
        .
        List of `AuditEventEntityDetail` items (represented as `dict` in JSON). """
        
        self.lifecycle = None
        """ 
        L
        i
        f
        e
        -
        c
        y
        c
        l
        e
        s
        t
        a
        g
        e
        f
        o
        r
        t
        h
        e
        e
        n
        t
        i
        t
        y
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        D
        e
        s
        c
        r
        i
        p
        t
        o
        r
        f
        o
        r
        e
        n
        t
        i
        t
        y
        .
        Type `str`. """
        
        self.query = None
        """ 
        Q
        u
        e
        r
        y
        p
        a
        r
        a
        m
        e
        t
        e
        r
        s
        .
        Type `str`. """
        
        self.role = None
        """ 
        W
        h
        a
        t
        r
        o
        l
        e
        t
        h
        e
        e
        n
        t
        i
        t
        y
        p
        l
        a
        y
        e
        d
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ 
        S
        e
        c
        u
        r
        i
        t
        y
        l
        a
        b
        e
        l
        s
        o
        n
        t
        h
        e
        e
        n
        t
        i
        t
        y
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        e
        n
        t
        i
        t
        y
        i
        n
        v
        o
        l
        v
        e
        d
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.what = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        i
        n
        s
        t
        a
        n
        c
        e
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(AuditEventEntity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventEntity, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("detail", "detail", AuditEventEntityDetail, True, None, False),
            ("lifecycle", "lifecycle", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("query", "query", str, False, None, False),
            ("role", "role", coding.Coding, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, False),
            ("what", "what", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class AuditEventEntityDetail(backboneelement.BackboneElement):
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
    I
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
    a
    b
    o
    u
    t
    t
    h
    e
    e
    n
    t
    i
    t
    y
    .
    
    
    T
    a
    g
    g
    e
    d
    v
    a
    l
    u
    e
    p
    a
    i
    r
    s
    f
    o
    r
    c
    o
    n
    v
    e
    y
    i
    n
    g
    a
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
    a
    b
    o
    u
    t
    t
    h
    e
    e
    n
    t
    i
    t
    y
    .
    
    """
    
    resource_type = "AuditEventEntityDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        p
        r
        o
        p
        e
        r
        t
        y
        .
        Type `str`. """
        
        self.valueBase64Binary = None
        """ 
        P
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        self.valueString = None
        """ 
        P
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        super(AuditEventEntityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventEntityDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js


class AuditEventSource(backboneelement.BackboneElement):
    """ 
    A
    u
    d
    i
    t
    E
    v
    e
    n
    t
    R
    e
    p
    o
    r
    t
    e
    r
    .
    
    
    T
    h
    e
    s
    y
    s
    t
    e
    m
    t
    h
    a
    t
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
    e
    v
    e
    n
    t
    .
    
    """
    
    resource_type = "AuditEventSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.observer = None
        """ 
        T
        h
        e
        i
        d
        e
        n
        t
        i
        t
        y
        o
        f
        s
        o
        u
        r
        c
        e
        d
        e
        t
        e
        c
        t
        i
        n
        g
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
        
        self.site = None
        """ 
        L
        o
        g
        i
        c
        a
        l
        s
        o
        u
        r
        c
        e
        l
        o
        c
        a
        t
        i
        o
        n
        w
        i
        t
        h
        i
        n
        t
        h
        e
        e
        n
        t
        e
        r
        p
        r
        i
        s
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        s
        o
        u
        r
        c
        e
        w
        h
        e
        r
        e
        e
        v
        e
        n
        t
        o
        r
        i
        g
        i
        n
        a
        t
        e
        d
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("observer", "observer", fhirreference.FHIRReference, False, None, True),
            ("site", "site", str, False, None, False),
            ("type", "type", coding.Coding, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
