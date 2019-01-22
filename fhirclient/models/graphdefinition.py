#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/GraphDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class GraphDefinition(domainresource.DomainResource):
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
    o
    f
    a
    g
    r
    a
    p
    h
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
    f
    o
    r
    m
    a
    l
    c
    o
    m
    p
    u
    t
    a
    b
    l
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
    f
    a
    g
    r
    a
    p
    h
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
    -
    t
    h
    a
    t
    i
    s
    ,
    a
    c
    o
    h
    e
    r
    e
    n
    t
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
    t
    h
    a
    t
    f
    o
    r
    m
    a
    g
    r
    a
    p
    h
    b
    y
    f
    o
    l
    l
    o
    w
    i
    n
    g
    r
    e
    f
    e
    r
    e
    n
    c
    e
    s
    .
    T
    h
    e
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
    r
    e
    s
    o
    u
    r
    c
    e
    d
    e
    f
    i
    n
    e
    s
    a
    s
    e
    t
    a
    n
    d
    m
    a
    k
    e
    s
    r
    u
    l
    e
    s
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
    t
    .
    
    """
    
    resource_type = "GraphDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        g
        r
        a
        p
        h
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
        g
        r
        a
        p
        h
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
        
        self.link = None
        """ 
        L
        i
        n
        k
        s
        t
        h
        i
        s
        g
        r
        a
        p
        h
        m
        a
        k
        e
        s
        r
        u
        l
        e
        s
        a
        b
        o
        u
        t
        .
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
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
        g
        r
        a
        p
        h
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
        
        self.profile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        o
        n
        b
        a
        s
        e
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
        g
        r
        a
        p
        h
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
        
        self.start = None
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
        a
        t
        w
        h
        i
        c
        h
        t
        h
        e
        g
        r
        a
        p
        h
        s
        t
        a
        r
        t
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
        
        self.url = None
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
        g
        r
        a
        p
        h
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
        ,
        r
        e
        p
        r
        e
        s
        e
        n
        t
        e
        d
        a
        s
        a
        U
        R
        I
        (
        g
        l
        o
        b
        a
        l
        l
        y
        u
        n
        i
        q
        u
        e
        )
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
        g
        r
        a
        p
        h
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
        
        super(GraphDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinition, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("name", "name", str, False, None, True),
            ("profile", "profile", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("start", "start", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class GraphDefinitionLink(backboneelement.BackboneElement):
    """ 
    L
    i
    n
    k
    s
    t
    h
    i
    s
    g
    r
    a
    p
    h
    m
    a
    k
    e
    s
    r
    u
    l
    e
    s
    a
    b
    o
    u
    t
    .
    """
    
    resource_type = "GraphDefinitionLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        W
        h
        y
        t
        h
        i
        s
        l
        i
        n
        k
        i
        s
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
        s
        f
        o
        r
        t
        h
        i
        s
        l
        i
        n
        k
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
        s
        f
        o
        r
        t
        h
        i
        s
        l
        i
        n
        k
        .
        Type `int`. """
        
        self.path = None
        """ 
        P
        a
        t
        h
        i
        n
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
        t
        h
        a
        t
        c
        o
        n
        t
        a
        i
        n
        s
        t
        h
        e
        l
        i
        n
        k
        .
        Type `str`. """
        
        self.sliceName = None
        """ 
        W
        h
        i
        c
        h
        s
        l
        i
        c
        e
        (
        i
        f
        p
        r
        o
        f
        i
        l
        e
        d
        )
        .
        Type `str`. """
        
        self.target = None
        """ 
        P
        o
        t
        e
        n
        t
        i
        a
        l
        t
        a
        r
        g
        e
        t
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
        List of `GraphDefinitionLinkTarget` items (represented as `dict` in JSON). """
        
        super(GraphDefinitionLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLink, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("path", "path", str, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("target", "target", GraphDefinitionLinkTarget, True, None, False),
        ])
        return js


class GraphDefinitionLinkTarget(backboneelement.BackboneElement):
    """ 
    P
    o
    t
    e
    n
    t
    i
    a
    l
    t
    a
    r
    g
    e
    t
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
    """
    
    resource_type = "GraphDefinitionLinkTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compartment = None
        """ 
        C
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        C
        o
        n
        s
        i
        s
        t
        e
        n
        c
        y
        R
        u
        l
        e
        s
        .
        List of `GraphDefinitionLinkTargetCompartment` items (represented as `dict` in JSON). """
        
        self.link = None
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
        l
        i
        n
        k
        s
        f
        r
        o
        m
        t
        a
        r
        g
        e
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
        List of `GraphDefinitionLink` items (represented as `dict` in JSON). """
        
        self.params = None
        """ 
        C
        r
        i
        t
        e
        r
        i
        a
        f
        o
        r
        r
        e
        v
        e
        r
        s
        e
        l
        o
        o
        k
        u
        p
        .
        Type `str`. """
        
        self.profile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        f
        o
        r
        t
        h
        e
        t
        a
        r
        g
        e
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
        Type `str`. """
        
        self.type = None
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
        t
        h
        i
        s
        l
        i
        n
        k
        r
        e
        f
        e
        r
        s
        t
        o
        .
        Type `str`. """
        
        super(GraphDefinitionLinkTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTarget, self).elementProperties()
        js.extend([
            ("compartment", "compartment", GraphDefinitionLinkTargetCompartment, True, None, False),
            ("link", "link", GraphDefinitionLink, True, None, False),
            ("params", "params", str, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class GraphDefinitionLinkTargetCompartment(backboneelement.BackboneElement):
    """ 
    C
    o
    m
    p
    a
    r
    t
    m
    e
    n
    t
    C
    o
    n
    s
    i
    s
    t
    e
    n
    c
    y
    R
    u
    l
    e
    s
    .
    """
    
    resource_type = "GraphDefinitionLinkTargetCompartment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
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
        s
        t
        h
        e
        c
        o
        m
        p
        a
        r
        t
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.description = None
        """ 
        D
        o
        c
        u
        m
        e
        n
        t
        a
        t
        i
        o
        n
        f
        o
        r
        F
        H
        I
        R
        P
        a
        t
        h
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
        .
        Type `str`. """
        
        self.expression = None
        """ 
        C
        u
        s
        t
        o
        m
        r
        u
        l
        e
        ,
        a
        s
        a
        F
        H
        I
        R
        P
        a
        t
        h
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
        .
        Type `str`. """
        
        self.rule = None
        """ 
        i
        d
        e
        n
        t
        i
        c
        a
        l
        |
        m
        a
        t
        c
        h
        i
        n
        g
        |
        d
        i
        f
        f
        e
        r
        e
        n
        t
        |
        c
        u
        s
        t
        o
        m
        .
        Type `str`. """
        
        self.use = None
        """ 
        c
        o
        n
        d
        i
        t
        i
        o
        n
        |
        r
        e
        q
        u
        i
        r
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        super(GraphDefinitionLinkTargetCompartment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GraphDefinitionLinkTargetCompartment, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("rule", "rule", str, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
