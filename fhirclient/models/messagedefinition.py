#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MessageDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MessageDefinition(domainresource.DomainResource):
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
    f
    i
    n
    e
    s
    a
    t
    y
    p
    e
    o
    f
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
    c
    a
    n
    b
    e
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
    
    
    D
    e
    f
    i
    n
    e
    s
    t
    h
    e
    c
    h
    a
    r
    a
    c
    t
    e
    r
    i
    s
    t
    i
    c
    s
    o
    f
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
    c
    a
    n
    b
    e
    s
    h
    a
    r
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
    ,
    i
    n
    c
    l
    u
    d
    i
    n
    g
    t
    h
    e
    t
    y
    p
    e
    o
    f
    e
    v
    e
    n
    t
    t
    h
    a
    t
    i
    n
    i
    t
    i
    a
    t
    e
    s
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
    ,
    t
    h
    e
    c
    o
    n
    t
    e
    n
    t
    t
    o
    b
    e
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
    a
    n
    d
    w
    h
    a
    t
    r
    e
    s
    p
    o
    n
    s
    e
    (
    s
    )
    ,
    i
    f
    a
    n
    y
    ,
    a
    r
    e
    p
    e
    r
    m
    i
    t
    t
    e
    d
    .
    
    """
    
    resource_type = "MessageDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedResponse = None
        """ 
        R
        e
        s
        p
        o
        n
        s
        e
        s
        t
        o
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
        List of `MessageDefinitionAllowedResponse` items (represented as `dict` in JSON). """
        
        self.base = None
        """ 
        D
        e
        f
        i
        n
        i
        t
        i
        o
        n
        t
        h
        i
        s
        o
        n
        e
        i
        s
        b
        a
        s
        e
        d
        o
        n
        .
        Type `str`. """
        
        self.category = None
        """ 
        c
        o
        n
        s
        e
        q
        u
        e
        n
        c
        e
        |
        c
        u
        r
        r
        e
        n
        c
        y
        |
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
        .
        Type `str`. """
        
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
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ 
        U
        s
        e
        a
        n
        d
        /
        o
        r
        p
        u
        b
        l
        i
        s
        h
        i
        n
        g
        r
        e
        s
        t
        r
        i
        c
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
        self.date = None
        """ 
        D
        a
        t
        e
        l
        a
        s
        t
        c
        h
        a
        n
        g
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
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
        
        self.eventCoding = None
        """ 
        E
        v
        e
        n
        t
        c
        o
        d
        e
        o
        r
        l
        i
        n
        k
        t
        o
        t
        h
        e
        E
        v
        e
        n
        t
        D
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
        E
        v
        e
        n
        t
        c
        o
        d
        e
        o
        r
        l
        i
        n
        k
        t
        o
        t
        h
        e
        E
        v
        e
        n
        t
        D
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
        
        self.experimental = None
        """ 
        F
        o
        r
        t
        e
        s
        t
        i
        n
        g
        p
        u
        r
        p
        o
        s
        e
        s
        ,
        n
        o
        t
        r
        e
        a
        l
        u
        s
        a
        g
        e
        .
        Type `bool`. """
        
        self.focus = None
        """ 
        R
        e
        s
        o
        u
        r
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
        e
        v
        e
        n
        t
        .
        List of `MessageDefinitionFocus` items (represented as `dict` in JSON). """
        
        self.graph = None
        """ 
        C
        a
        n
        o
        n
        i
        c
        a
        l
        r
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
        a
        G
        r
        a
        p
        h
        D
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
        List of `str` items. """
        
        self.identifier = None
        """ 
        P
        r
        i
        m
        a
        r
        y
        k
        e
        y
        f
        o
        r
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
        o
        n
        a
        g
        i
        v
        e
        n
        s
        e
        r
        v
        e
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        j
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        f
        o
        r
        m
        e
        s
        s
        a
        g
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
        (
        i
        f
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        N
        a
        m
        e
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
        (
        c
        o
        m
        p
        u
        t
        e
        r
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.parent = None
        """ 
        P
        r
        o
        t
        o
        c
        o
        l
        /
        w
        o
        r
        k
        f
        l
        o
        w
        t
        h
        i
        s
        i
        s
        p
        a
        r
        t
        o
        f
        .
        List of `str` items. """
        
        self.publisher = None
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
        u
        b
        l
        i
        s
        h
        e
        r
        (
        o
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        o
        r
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        )
        .
        Type `str`. """
        
        self.purpose = None
        """ 
        W
        h
        y
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
        i
        s
        d
        e
        f
        i
        n
        e
        d
        .
        Type `str`. """
        
        self.replaces = None
        """ 
        T
        a
        k
        e
        s
        t
        h
        e
        p
        l
        a
        c
        e
        o
        f
        .
        List of `str` items. """
        
        self.responseRequired = None
        """ 
        a
        l
        w
        a
        y
        s
        |
        o
        n
        -
        e
        r
        r
        o
        r
        |
        n
        e
        v
        e
        r
        |
        o
        n
        -
        s
        u
        c
        c
        e
        s
        s
        .
        Type `str`. """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        a
        c
        t
        i
        v
        e
        |
        r
        e
        t
        i
        r
        e
        d
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        self.title = None
        """ 
        N
        a
        m
        e
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
        (
        h
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
        )
        .
        Type `str`. """
        
        self.url = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
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
        a
        g
        i
        v
        e
        n
        M
        e
        s
        s
        a
        g
        e
        D
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
        
        self.useContext = None
        """ 
        T
        h
        e
        c
        o
        n
        t
        e
        x
        t
        t
        h
        a
        t
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
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
        t
        o
        s
        u
        p
        p
        o
        r
        t
        .
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        v
        e
        r
        s
        i
        o
        n
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
        
        super(MessageDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinition, self).elementProperties()
        js.extend([
            ("allowedResponse", "allowedResponse", MessageDefinitionAllowedResponse, True, None, False),
            ("base", "base", str, False, None, False),
            ("category", "category", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("eventUri", "eventUri", str, False, "event", True),
            ("experimental", "experimental", bool, False, None, False),
            ("focus", "focus", MessageDefinitionFocus, True, None, False),
            ("graph", "graph", str, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("parent", "parent", str, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("responseRequired", "responseRequired", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class MessageDefinitionAllowedResponse(backboneelement.BackboneElement):
    """ 
    R
    e
    s
    p
    o
    n
    s
    e
    s
    t
    o
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
    
    
    I
    n
    d
    i
    c
    a
    t
    e
    s
    w
    h
    a
    t
    t
    y
    p
    e
    s
    o
    f
    m
    e
    s
    s
    a
    g
    e
    s
    m
    a
    y
    b
    e
    s
    e
    n
    t
    a
    s
    a
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
    -
    l
    e
    v
    e
    l
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
    
    """
    
    resource_type = "MessageDefinitionAllowedResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.message = None
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
        a
        l
        l
        o
        w
        e
        d
        m
        e
        s
        s
        a
        g
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
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `str`. """
        
        self.situation = None
        """ 
        W
        h
        e
        n
        s
        h
        o
        u
        l
        d
        t
        h
        i
        s
        r
        e
        s
        p
        o
        n
        s
        e
        b
        e
        u
        s
        e
        d
        .
        Type `str`. """
        
        super(MessageDefinitionAllowedResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinitionAllowedResponse, self).elementProperties()
        js.extend([
            ("message", "message", str, False, None, True),
            ("situation", "situation", str, False, None, False),
        ])
        return js


class MessageDefinitionFocus(backboneelement.BackboneElement):
    """ 
    R
    e
    s
    o
    u
    r
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
    e
    v
    e
    n
    t
    .
    
    
    I
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
    r
    e
    s
    o
    u
    r
    c
    e
    (
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
    s
    )
    t
    h
    a
    t
    a
    r
    e
    b
    e
    i
    n
    g
    a
    d
    d
    r
    e
    s
    s
    e
    d
    b
    y
    t
    h
    e
    e
    v
    e
    n
    t
    .
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    ,
    t
    h
    e
    E
    n
    c
    o
    u
    n
    t
    e
    r
    f
    o
    r
    a
    n
    a
    d
    m
    i
    t
    m
    e
    s
    s
    a
    g
    e
    o
    r
    t
    w
    o
    A
    c
    c
    o
    u
    n
    t
    r
    e
    c
    o
    r
    d
    s
    f
    o
    r
    a
    m
    e
    r
    g
    e
    .
    
    """
    
    resource_type = "MessageDefinitionFocus"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        T
        y
        p
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
        Type `str`. """
        
        self.max = None
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
        f
        o
        c
        u
        s
        e
        s
        o
        f
        t
        h
        i
        s
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.min = None
        """ 
        M
        i
        n
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
        f
        o
        c
        u
        s
        e
        s
        o
        f
        t
        h
        i
        s
        t
        y
        p
        e
        .
        Type `int`. """
        
        self.profile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        t
        h
        a
        t
        m
        u
        s
        t
        b
        e
        a
        d
        h
        e
        r
        e
        d
        t
        o
        b
        y
        f
        o
        c
        u
        s
        .
        Type `str`. """
        
        super(MessageDefinitionFocus, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageDefinitionFocus, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, True),
            ("profile", "profile", str, False, None, False),
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
