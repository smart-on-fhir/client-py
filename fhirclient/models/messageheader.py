#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MessageHeader(domainresource.DomainResource):
    """ 
    A
    r
    e
    s
    o
    u
    r
    c
    e
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
    a
    m
    e
    s
    s
    a
    g
    e
    t
    h
    a
    t
    i
    s
    e
    x
    c
    h
    a
    n
    g
    e
    d
    b
    e
    t
    w
    e
    e
    n
    s
    y
    s
    t
    e
    m
    s
    .
    
    
    T
    h
    e
    h
    e
    a
    d
    e
    r
    f
    o
    r
    a
    m
    e
    s
    s
    a
    g
    e
    e
    x
    c
    h
    a
    n
    g
    e
    t
    h
    a
    t
    i
    s
    e
    i
    t
    h
    e
    r
    r
    e
    q
    u
    e
    s
    t
    i
    n
    g
    o
    r
    r
    e
    s
    p
    o
    n
    d
    i
    n
    g
    t
    o
    a
    n
    a
    c
    t
    i
    o
    n
    .
    T
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
    (
    s
    )
    t
    h
    a
    t
    a
    r
    e
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
    o
    f
    t
    h
    e
    a
    c
    t
    i
    o
    n
    a
    s
    w
    e
    l
    l
    a
    s
    o
    t
    h
    e
    r
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
    r
    e
    l
    a
    t
    e
    d
    t
    o
    t
    h
    e
    a
    c
    t
    i
    o
    n
    a
    r
    e
    t
    y
    p
    i
    c
    a
    l
    l
    y
    t
    r
    a
    n
    s
    m
    i
    t
    t
    e
    d
    i
    n
    a
    b
    u
    n
    d
    l
    e
    i
    n
    w
    h
    i
    c
    h
    t
    h
    e
    M
    e
    s
    s
    a
    g
    e
    H
    e
    a
    d
    e
    r
    r
    e
    s
    o
    u
    r
    c
    e
    i
    n
    s
    t
    a
    n
    c
    e
    i
    s
    t
    h
    e
    f
    i
    r
    s
    t
    r
    e
    s
    o
    u
    r
    c
    e
    i
    n
    t
    h
    e
    b
    u
    n
    d
    l
    e
    .
    
    """
    
    resource_type = "MessageHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ 
        T
        h
        e
        s
        o
        u
        r
        c
        e
        o
        f
        t
        h
        e
        d
        e
        c
        i
        s
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.definition = None
        """ 
        L
        i
        n
        k
        t
        o
        t
        h
        e
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
        f
        o
        r
        t
        h
        i
        s
        m
        e
        s
        s
        a
        g
        e
        .
        Type `str`. """
        
        self.destination = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        d
        e
        s
        t
        i
        n
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
        c
        a
        t
        i
        o
        n
        (
        s
        )
        .
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """
        
        self.enterer = None
        """ 
        T
        h
        e
        s
        o
        u
        r
        c
        e
        o
        f
        t
        h
        e
        d
        a
        t
        a
        e
        n
        t
        r
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.eventCoding = None
        """ 
        C
        o
        d
        e
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
        t
        h
        i
        s
        m
        e
        s
        s
        a
        g
        e
        r
        e
        p
        r
        e
        s
        e
        n
        t
        s
        o
        r
        l
        i
        n
        k
        t
        o
        e
        v
        e
        n
        t
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
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.eventUri = None
        """ 
        C
        o
        d
        e
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
        t
        h
        i
        s
        m
        e
        s
        s
        a
        g
        e
        r
        e
        p
        r
        e
        s
        e
        n
        t
        s
        o
        r
        l
        i
        n
        k
        t
        o
        e
        v
        e
        n
        t
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
        .
        Type `str`. """
        
        self.focus = None
        """ 
        T
        h
        e
        a
        c
        t
        u
        a
        l
        c
        o
        n
        t
        e
        n
        t
        o
        f
        t
        h
        e
        m
        e
        s
        s
        a
        g
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reason = None
        """ 
        C
        a
        u
        s
        e
        o
        f
        e
        v
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.response = None
        """ 
        I
        f
        t
        h
        i
        s
        i
        s
        a
        r
        e
        p
        l
        y
        t
        o
        p
        r
        i
        o
        r
        m
        e
        s
        s
        a
        g
        e
        .
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ 
        F
        i
        n
        a
        l
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
        e
        v
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sender = None
        """ 
        R
        e
        a
        l
        w
        o
        r
        l
        d
        s
        e
        n
        d
        e
        r
        o
        f
        t
        h
        e
        m
        e
        s
        s
        a
        g
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        s
        o
        u
        r
        c
        e
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
        .
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
        
        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("destination", "destination", MessageHeaderDestination, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("response", "response", MessageHeaderResponse, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("source", "source", MessageHeaderSource, False, None, True),
        ])
        return js


from . import backboneelement

class MessageHeaderDestination(backboneelement.BackboneElement):
    """ 
    M
    e
    s
    s
    a
    g
    e
    d
    e
    s
    t
    i
    n
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
    c
    a
    t
    i
    o
    n
    (
    s
    )
    .
    
    
    T
    h
    e
    d
    e
    s
    t
    i
    n
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
    c
    a
    t
    i
    o
    n
    w
    h
    i
    c
    h
    t
    h
    e
    m
    e
    s
    s
    a
    g
    e
    i
    s
    i
    n
    t
    e
    n
    d
    e
    d
    f
    o
    r
    .
    
    """
    
    resource_type = "MessageHeaderDestination"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        """ 
        A
        c
        t
        u
        a
        l
        d
        e
        s
        t
        i
        n
        a
        t
        i
        o
        n
        a
        d
        d
        r
        e
        s
        s
        o
        r
        i
        d
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        f
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.receiver = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        "
        r
        e
        a
        l
        -
        w
        o
        r
        l
        d
        "
        r
        e
        c
        i
        p
        i
        e
        n
        t
        f
        o
        r
        t
        h
        e
        d
        a
        t
        a
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.target = None
        """ 
        P
        a
        r
        t
        i
        c
        u
        l
        a
        r
        d
        e
        l
        i
        v
        e
        r
        y
        d
        e
        s
        t
        i
        n
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
        d
        e
        s
        t
        i
        n
        a
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MessageHeaderResponse(backboneelement.BackboneElement):
    """ 
    I
    f
    t
    h
    i
    s
    i
    s
    a
    r
    e
    p
    l
    y
    t
    o
    p
    r
    i
    o
    r
    m
    e
    s
    s
    a
    g
    e
    .
    
    
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
    m
    e
    s
    s
    a
    g
    e
    t
    h
    a
    t
    t
    h
    i
    s
    m
    e
    s
    s
    a
    g
    e
    i
    s
    a
    r
    e
    s
    p
    o
    n
    s
    e
    t
    o
    .
    O
    n
    l
    y
    p
    r
    e
    s
    e
    n
    t
    i
    f
    t
    h
    i
    s
    m
    e
    s
    s
    a
    g
    e
    i
    s
    a
    r
    e
    s
    p
    o
    n
    s
    e
    .
    
    """
    
    resource_type = "MessageHeaderResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        o
        k
        |
        t
        r
        a
        n
        s
        i
        e
        n
        t
        -
        e
        r
        r
        o
        r
        |
        f
        a
        t
        a
        l
        -
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        self.details = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        l
        i
        s
        t
        o
        f
        h
        i
        n
        t
        s
        /
        w
        a
        r
        n
        i
        n
        g
        s
        /
        e
        r
        r
        o
        r
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        I
        d
        o
        f
        o
        r
        i
        g
        i
        n
        a
        l
        m
        e
        s
        s
        a
        g
        e
        .
        Type `str`. """
        
        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", str, False, None, True),
        ])
        return js


class MessageHeaderSource(backboneelement.BackboneElement):
    """ 
    M
    e
    s
    s
    a
    g
    e
    s
    o
    u
    r
    c
    e
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
    .
    
    
    T
    h
    e
    s
    o
    u
    r
    c
    e
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
    f
    r
    o
    m
    w
    h
    i
    c
    h
    t
    h
    i
    s
    m
    e
    s
    s
    a
    g
    e
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
    
    """
    
    resource_type = "MessageHeaderSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ 
        H
        u
        m
        a
        n
        c
        o
        n
        t
        a
        c
        t
        f
        o
        r
        p
        r
        o
        b
        l
        e
        m
        s
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ 
        A
        c
        t
        u
        a
        l
        m
        e
        s
        s
        a
        g
        e
        s
        o
        u
        r
        c
        e
        a
        d
        d
        r
        e
        s
        s
        o
        r
        i
        d
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        f
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.software = None
        """ 
        N
        a
        m
        e
        o
        f
        s
        o
        f
        t
        w
        a
        r
        e
        r
        u
        n
        n
        i
        n
        g
        t
        h
        e
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.version = None
        """ 
        V
        e
        r
        s
        i
        o
        n
        o
        f
        s
        o
        f
        t
        w
        a
        r
        e
        r
        u
        n
        n
        i
        n
        g
        .
        Type `str`. """
        
        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("software", "software", str, False, None, False),
            ("version", "version", str, False, None, False),
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
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
