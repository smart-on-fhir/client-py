#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Subscription) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Subscription(domainresource.DomainResource):
    """ 
    S
    e
    r
    v
    e
    r
    p
    u
    s
    h
    s
    u
    b
    s
    c
    r
    i
    p
    t
    i
    o
    n
    c
    r
    i
    t
    e
    r
    i
    a
    .
    
    
    T
    h
    e
    s
    u
    b
    s
    c
    r
    i
    p
    t
    i
    o
    n
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
    u
    s
    e
    d
    t
    o
    d
    e
    f
    i
    n
    e
    a
    p
    u
    s
    h
    -
    b
    a
    s
    e
    d
    s
    u
    b
    s
    c
    r
    i
    p
    t
    i
    o
    n
    f
    r
    o
    m
    a
    s
    e
    r
    v
    e
    r
    t
    o
    a
    n
    o
    t
    h
    e
    r
    s
    y
    s
    t
    e
    m
    .
    O
    n
    c
    e
    a
    s
    u
    b
    s
    c
    r
    i
    p
    t
    i
    o
    n
    i
    s
    r
    e
    g
    i
    s
    t
    e
    r
    e
    d
    w
    i
    t
    h
    t
    h
    e
    s
    e
    r
    v
    e
    r
    ,
    t
    h
    e
    s
    e
    r
    v
    e
    r
    c
    h
    e
    c
    k
    s
    e
    v
    e
    r
    y
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
    i
    s
    c
    r
    e
    a
    t
    e
    d
    o
    r
    u
    p
    d
    a
    t
    e
    d
    ,
    a
    n
    d
    i
    f
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
    m
    a
    t
    c
    h
    e
    s
    t
    h
    e
    g
    i
    v
    e
    n
    c
    r
    i
    t
    e
    r
    i
    a
    ,
    i
    t
    s
    e
    n
    d
    s
    a
    m
    e
    s
    s
    a
    g
    e
    o
    n
    t
    h
    e
    d
    e
    f
    i
    n
    e
    d
    "
    c
    h
    a
    n
    n
    e
    l
    "
    s
    o
    t
    h
    a
    t
    a
    n
    o
    t
    h
    e
    r
    s
    y
    s
    t
    e
    m
    c
    a
    n
    t
    a
    k
    e
    a
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
    a
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "Subscription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.channel = None
        """ 
        T
        h
        e
        c
        h
        a
        n
        n
        e
        l
        o
        n
        w
        h
        i
        c
        h
        t
        o
        r
        e
        p
        o
        r
        t
        m
        a
        t
        c
        h
        e
        s
        t
        o
        t
        h
        e
        c
        r
        i
        t
        e
        r
        i
        a
        .
        Type `SubscriptionChannel` (represented as `dict` in JSON). """
        
        self.contact = None
        """ 
        C
        o
        n
        t
        a
        c
        t
        d
        e
        t
        a
        i
        l
        s
        f
        o
        r
        s
        o
        u
        r
        c
        e
        (
        e
        .
        g
        .
        t
        r
        o
        u
        b
        l
        e
        s
        h
        o
        o
        t
        i
        n
        g
        )
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.criteria = None
        """ 
        R
        u
        l
        e
        f
        o
        r
        s
        e
        r
        v
        e
        r
        p
        u
        s
        h
        .
        Type `str`. """
        
        self.end = None
        """ 
        W
        h
        e
        n
        t
        o
        a
        u
        t
        o
        m
        a
        t
        i
        c
        a
        l
        l
        y
        d
        e
        l
        e
        t
        e
        t
        h
        e
        s
        u
        b
        s
        c
        r
        i
        p
        t
        i
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.error = None
        """ 
        L
        a
        t
        e
        s
        t
        e
        r
        r
        o
        r
        n
        o
        t
        e
        .
        Type `str`. """
        
        self.reason = None
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
        w
        h
        y
        t
        h
        i
        s
        s
        u
        b
        s
        c
        r
        i
        p
        t
        i
        o
        n
        w
        a
        s
        c
        r
        e
        a
        t
        e
        d
        .
        Type `str`. """
        
        self.status = None
        """ 
        r
        e
        q
        u
        e
        s
        t
        e
        d
        |
        a
        c
        t
        i
        v
        e
        |
        e
        r
        r
        o
        r
        |
        o
        f
        f
        .
        Type `str`. """
        
        super(Subscription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Subscription, self).elementProperties()
        js.extend([
            ("channel", "channel", SubscriptionChannel, False, None, True),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("criteria", "criteria", str, False, None, True),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("error", "error", str, False, None, False),
            ("reason", "reason", str, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class SubscriptionChannel(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    c
    h
    a
    n
    n
    e
    l
    o
    n
    w
    h
    i
    c
    h
    t
    o
    r
    e
    p
    o
    r
    t
    m
    a
    t
    c
    h
    e
    s
    t
    o
    t
    h
    e
    c
    r
    i
    t
    e
    r
    i
    a
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    w
    h
    e
    r
    e
    t
    o
    s
    e
    n
    d
    n
    o
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
    s
    w
    h
    e
    n
    r
    e
    s
    o
    u
    r
    c
    e
    s
    a
    r
    e
    r
    e
    c
    e
    i
    v
    e
    d
    t
    h
    a
    t
    m
    e
    e
    t
    t
    h
    e
    c
    r
    i
    t
    e
    r
    i
    a
    .
    
    """
    
    resource_type = "SubscriptionChannel"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        c
        h
        a
        n
        n
        e
        l
        p
        o
        i
        n
        t
        s
        t
        o
        .
        Type `str`. """
        
        self.header = None
        """ 
        U
        s
        a
        g
        e
        d
        e
        p
        e
        n
        d
        s
        o
        n
        t
        h
        e
        c
        h
        a
        n
        n
        e
        l
        t
        y
        p
        e
        .
        List of `str` items. """
        
        self.payload = None
        """ 
        M
        I
        M
        E
        t
        y
        p
        e
        t
        o
        s
        e
        n
        d
        ,
        o
        r
        o
        m
        i
        t
        f
        o
        r
        n
        o
        p
        a
        y
        l
        o
        a
        d
        .
        Type `str`. """
        
        self.type = None
        """ 
        r
        e
        s
        t
        -
        h
        o
        o
        k
        |
        w
        e
        b
        s
        o
        c
        k
        e
        t
        |
        e
        m
        a
        i
        l
        |
        s
        m
        s
        |
        m
        e
        s
        s
        a
        g
        e
        .
        Type `str`. """
        
        super(SubscriptionChannel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubscriptionChannel, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, False),
            ("header", "header", str, True, None, False),
            ("payload", "payload", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
