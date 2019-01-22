#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Bundle) on 2019-01-22.
#  2019, SMART Health IT.


from . import resource

class Bundle(resource.Resource):
    """ 
    C
    o
    n
    t
    a
    i
    n
    s
    a
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
    
    
    A
    c
    o
    n
    t
    a
    i
    n
    e
    r
    f
    o
    r
    a
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
    
    """
    
    resource_type = "Bundle"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entry = None
        """ 
        E
        n
        t
        r
        y
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
        -
        w
        i
        l
        l
        h
        a
        v
        e
        a
        r
        e
        s
        o
        u
        r
        c
        e
        o
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
        .
        List of `BundleEntry` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        P
        e
        r
        s
        i
        s
        t
        e
        n
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
        r
        f
        o
        r
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
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.link = None
        """ 
        L
        i
        n
        k
        s
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
        i
        s
        B
        u
        n
        d
        l
        e
        .
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.signature = None
        """ 
        D
        i
        g
        i
        t
        a
        l
        S
        i
        g
        n
        a
        t
        u
        r
        e
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.timestamp = None
        """ 
        W
        h
        e
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
        w
        a
        s
        a
        s
        s
        e
        m
        b
        l
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.total = None
        """ 
        I
        f
        s
        e
        a
        r
        c
        h
        ,
        t
        h
        e
        t
        o
        t
        a
        l
        n
        u
        m
        b
        e
        r
        o
        f
        m
        a
        t
        c
        h
        e
        s
        .
        Type `int`. """
        
        self.type = None
        """ 
        d
        o
        c
        u
        m
        e
        n
        t
        |
        m
        e
        s
        s
        a
        g
        e
        |
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        |
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        -
        r
        e
        s
        p
        o
        n
        s
        e
        |
        b
        a
        t
        c
        h
        |
        b
        a
        t
        c
        h
        -
        r
        e
        s
        p
        o
        n
        s
        e
        |
        h
        i
        s
        t
        o
        r
        y
        |
        s
        e
        a
        r
        c
        h
        s
        e
        t
        |
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
        
        super(Bundle, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Bundle, self).elementProperties()
        js.extend([
            ("entry", "entry", BundleEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("signature", "signature", signature.Signature, False, None, False),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, False),
            ("total", "total", int, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import backboneelement

class BundleEntry(backboneelement.BackboneElement):
    """ 
    E
    n
    t
    r
    y
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
    -
    w
    i
    l
    l
    h
    a
    v
    e
    a
    r
    e
    s
    o
    u
    r
    c
    e
    o
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
    .
    
    
    A
    n
    e
    n
    t
    r
    y
    i
    n
    a
    b
    u
    n
    d
    l
    e
    r
    e
    s
    o
    u
    r
    c
    e
    -
    w
    i
    l
    l
    e
    i
    t
    h
    e
    r
    c
    o
    n
    t
    a
    i
    n
    a
    r
    e
    s
    o
    u
    r
    c
    e
    o
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
    a
    b
    o
    u
    t
    a
    r
    e
    s
    o
    u
    r
    c
    e
    (
    t
    r
    a
    n
    s
    a
    c
    t
    i
    o
    n
    s
    a
    n
    d
    h
    i
    s
    t
    o
    r
    y
    o
    n
    l
    y
    )
    .
    
    """
    
    resource_type = "BundleEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fullUrl = None
        """ 
        U
        R
        I
        f
        o
        r
        r
        e
        s
        o
        u
        r
        c
        e
        (
        A
        b
        s
        o
        l
        u
        t
        e
        U
        R
        L
        s
        e
        r
        v
        e
        r
        a
        d
        d
        r
        e
        s
        s
        o
        r
        U
        R
        I
        f
        o
        r
        U
        U
        I
        D
        /
        O
        I
        D
        )
        .
        Type `str`. """
        
        self.link = None
        """ 
        L
        i
        n
        k
        s
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
        i
        s
        e
        n
        t
        r
        y
        .
        List of `BundleLink` items (represented as `dict` in JSON). """
        
        self.request = None
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
        e
        x
        e
        c
        u
        t
        i
        o
        n
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
        (
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        /
        b
        a
        t
        c
        h
        /
        h
        i
        s
        t
        o
        r
        y
        )
        .
        Type `BundleEntryRequest` (represented as `dict` in JSON). """
        
        self.resource = None
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
        Type `Resource` (represented as `dict` in JSON). """
        
        self.response = None
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
        e
        x
        e
        c
        u
        t
        i
        o
        n
        (
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        /
        b
        a
        t
        c
        h
        /
        h
        i
        s
        t
        o
        r
        y
        )
        .
        Type `BundleEntryResponse` (represented as `dict` in JSON). """
        
        self.search = None
        """ 
        S
        e
        a
        r
        c
        h
        r
        e
        l
        a
        t
        e
        d
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
        Type `BundleEntrySearch` (represented as `dict` in JSON). """
        
        super(BundleEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntry, self).elementProperties()
        js.extend([
            ("fullUrl", "fullUrl", str, False, None, False),
            ("link", "link", BundleLink, True, None, False),
            ("request", "request", BundleEntryRequest, False, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("response", "response", BundleEntryResponse, False, None, False),
            ("search", "search", BundleEntrySearch, False, None, False),
        ])
        return js


class BundleEntryRequest(backboneelement.BackboneElement):
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
    e
    x
    e
    c
    u
    t
    i
    o
    n
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
    (
    t
    r
    a
    n
    s
    a
    c
    t
    i
    o
    n
    /
    b
    a
    t
    c
    h
    /
    h
    i
    s
    t
    o
    r
    y
    )
    .
    
    
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
    h
    o
    w
    t
    h
    i
    s
    e
    n
    t
    r
    y
    s
    h
    o
    u
    l
    d
    b
    e
    p
    r
    o
    c
    e
    s
    s
    e
    d
    a
    s
    p
    a
    r
    t
    o
    f
    a
    t
    r
    a
    n
    s
    a
    c
    t
    i
    o
    n
    o
    r
    b
    a
    t
    c
    h
    .
    F
    o
    r
    h
    i
    s
    t
    o
    r
    y
    ,
    i
    t
    s
    h
    o
    w
    s
    h
    o
    w
    t
    h
    e
    e
    n
    t
    r
    y
    w
    a
    s
    p
    r
    o
    c
    e
    s
    s
    e
    d
    t
    o
    c
    r
    e
    a
    t
    e
    t
    h
    e
    v
    e
    r
    s
    i
    o
    n
    c
    o
    n
    t
    a
    i
    n
    e
    d
    i
    n
    t
    h
    e
    e
    n
    t
    r
    y
    .
    
    """
    
    resource_type = "BundleEntryRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ifMatch = None
        """ 
        F
        o
        r
        m
        a
        n
        a
        g
        i
        n
        g
        u
        p
        d
        a
        t
        e
        c
        o
        n
        t
        e
        n
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.ifModifiedSince = None
        """ 
        F
        o
        r
        m
        a
        n
        a
        g
        i
        n
        g
        c
        a
        c
        h
        e
        c
        u
        r
        r
        e
        n
        c
        y
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.ifNoneExist = None
        """ 
        F
        o
        r
        c
        o
        n
        d
        i
        t
        i
        o
        n
        a
        l
        c
        r
        e
        a
        t
        e
        s
        .
        Type `str`. """
        
        self.ifNoneMatch = None
        """ 
        F
        o
        r
        m
        a
        n
        a
        g
        i
        n
        g
        c
        a
        c
        h
        e
        c
        u
        r
        r
        e
        n
        c
        y
        .
        Type `str`. """
        
        self.method = None
        """ 
        G
        E
        T
        |
        H
        E
        A
        D
        |
        P
        O
        S
        T
        |
        P
        U
        T
        |
        D
        E
        L
        E
        T
        E
        |
        P
        A
        T
        C
        H
        .
        Type `str`. """
        
        self.url = None
        """ 
        U
        R
        L
        f
        o
        r
        H
        T
        T
        P
        e
        q
        u
        i
        v
        a
        l
        e
        n
        t
        o
        f
        t
        h
        i
        s
        e
        n
        t
        r
        y
        .
        Type `str`. """
        
        super(BundleEntryRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntryRequest, self).elementProperties()
        js.extend([
            ("ifMatch", "ifMatch", str, False, None, False),
            ("ifModifiedSince", "ifModifiedSince", fhirdate.FHIRDate, False, None, False),
            ("ifNoneExist", "ifNoneExist", str, False, None, False),
            ("ifNoneMatch", "ifNoneMatch", str, False, None, False),
            ("method", "method", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


class BundleEntryResponse(backboneelement.BackboneElement):
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
    e
    x
    e
    c
    u
    t
    i
    o
    n
    (
    t
    r
    a
    n
    s
    a
    c
    t
    i
    o
    n
    /
    b
    a
    t
    c
    h
    /
    h
    i
    s
    t
    o
    r
    y
    )
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
    p
    r
    o
    c
    e
    s
    s
    i
    n
    g
    t
    h
    e
    c
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
    '
    r
    e
    q
    u
    e
    s
    t
    '
    e
    n
    t
    r
    y
    i
    n
    t
    h
    e
    b
    a
    t
    c
    h
    o
    r
    t
    r
    a
    n
    s
    a
    c
    t
    i
    o
    n
    b
    e
    i
    n
    g
    r
    e
    s
    p
    o
    n
    d
    e
    d
    t
    o
    o
    r
    w
    h
    a
    t
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
    a
    n
    o
    p
    e
    r
    a
    t
    i
    o
    n
    w
    h
    e
    r
    e
    w
    h
    e
    n
    r
    e
    t
    u
    r
    n
    i
    n
    g
    h
    i
    s
    t
    o
    r
    y
    .
    
    """
    
    resource_type = "BundleEntryResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.etag = None
        """ 
        T
        h
        e
        E
        t
        a
        g
        f
        o
        r
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
        (
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
        )
        .
        Type `str`. """
        
        self.lastModified = None
        """ 
        S
        e
        r
        v
        e
        r
        '
        s
        d
        a
        t
        e
        t
        i
        m
        e
        m
        o
        d
        i
        f
        i
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.location = None
        """ 
        T
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        (
        i
        f
        t
        h
        e
        o
        p
        e
        r
        a
        t
        i
        o
        n
        r
        e
        t
        u
        r
        n
        s
        a
        l
        o
        c
        a
        t
        i
        o
        n
        )
        .
        Type `str`. """
        
        self.outcome = None
        """ 
        O
        p
        e
        r
        a
        t
        i
        o
        n
        O
        u
        t
        c
        o
        m
        e
        w
        i
        t
        h
        h
        i
        n
        t
        s
        a
        n
        d
        w
        a
        r
        n
        i
        n
        g
        s
        (
        f
        o
        r
        b
        a
        t
        c
        h
        /
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        )
        .
        Type `Resource` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        S
        t
        a
        t
        u
        s
        r
        e
        s
        p
        o
        n
        s
        e
        c
        o
        d
        e
        (
        t
        e
        x
        t
        o
        p
        t
        i
        o
        n
        a
        l
        )
        .
        Type `str`. """
        
        super(BundleEntryResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntryResponse, self).elementProperties()
        js.extend([
            ("etag", "etag", str, False, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, False),
            ("location", "location", str, False, None, False),
            ("outcome", "outcome", resource.Resource, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


class BundleEntrySearch(backboneelement.BackboneElement):
    """ 
    S
    e
    a
    r
    c
    h
    r
    e
    l
    a
    t
    e
    d
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
    s
    e
    a
    r
    c
    h
    p
    r
    o
    c
    e
    s
    s
    t
    h
    a
    t
    l
    e
    a
    d
    t
    o
    t
    h
    e
    c
    r
    e
    a
    t
    i
    o
    n
    o
    f
    t
    h
    i
    s
    e
    n
    t
    r
    y
    .
    
    """
    
    resource_type = "BundleEntrySearch"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.mode = None
        """ 
        m
        a
        t
        c
        h
        |
        i
        n
        c
        l
        u
        d
        e
        |
        o
        u
        t
        c
        o
        m
        e
        -
        w
        h
        y
        t
        h
        i
        s
        i
        s
        i
        n
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
        e
        t
        .
        Type `str`. """
        
        self.score = None
        """ 
        S
        e
        a
        r
        c
        h
        r
        a
        n
        k
        i
        n
        g
        (
        b
        e
        t
        w
        e
        e
        n
        0
        a
        n
        d
        1
        )
        .
        Type `float`. """
        
        super(BundleEntrySearch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleEntrySearch, self).elementProperties()
        js.extend([
            ("mode", "mode", str, False, None, False),
            ("score", "score", float, False, None, False),
        ])
        return js


class BundleLink(backboneelement.BackboneElement):
    """ 
    L
    i
    n
    k
    s
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
    i
    s
    B
    u
    n
    d
    l
    e
    .
    
    
    A
    s
    e
    r
    i
    e
    s
    o
    f
    l
    i
    n
    k
    s
    t
    h
    a
    t
    p
    r
    o
    v
    i
    d
    e
    c
    o
    n
    t
    e
    x
    t
    t
    o
    t
    h
    i
    s
    b
    u
    n
    d
    l
    e
    .
    
    """
    
    resource_type = "BundleLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.relation = None
        """ 
        S
        e
        e
        h
        t
        t
        p
        :
        /
        /
        w
        w
        w
        .
        i
        a
        n
        a
        .
        o
        r
        g
        /
        a
        s
        s
        i
        g
        n
        m
        e
        n
        t
        s
        /
        l
        i
        n
        k
        -
        r
        e
        l
        a
        t
        i
        o
        n
        s
        /
        l
        i
        n
        k
        -
        r
        e
        l
        a
        t
        i
        o
        n
        s
        .
        x
        h
        t
        m
        l
        #
        l
        i
        n
        k
        -
        r
        e
        l
        a
        t
        i
        o
        n
        s
        -
        1
        .
        Type `str`. """
        
        self.url = None
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
        t
        h
        e
        l
        i
        n
        k
        .
        Type `str`. """
        
        super(BundleLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BundleLink, self).elementProperties()
        js.extend([
            ("relation", "relation", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
