#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class NamingSystem(domainresource.DomainResource):
    """ 
    S
    y
    s
    t
    e
    m
    o
    f
    u
    n
    i
    q
    u
    e
    i
    d
    e
    n
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
    
    
    A
    c
    u
    r
    a
    t
    e
    d
    n
    a
    m
    e
    s
    p
    a
    c
    e
    t
    h
    a
    t
    i
    s
    s
    u
    e
    s
    u
    n
    i
    q
    u
    e
    s
    y
    m
    b
    o
    l
    s
    w
    i
    t
    h
    i
    n
    t
    h
    a
    t
    n
    a
    m
    e
    s
    p
    a
    c
    e
    f
    o
    r
    t
    h
    e
    i
    d
    e
    n
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
    o
    f
    c
    o
    n
    c
    e
    p
    t
    s
    ,
    p
    e
    o
    p
    l
    e
    ,
    d
    e
    v
    i
    c
    e
    s
    ,
    e
    t
    c
    .
    R
    e
    p
    r
    e
    s
    e
    n
    t
    s
    a
    "
    S
    y
    s
    t
    e
    m
    "
    u
    s
    e
    d
    w
    i
    t
    h
    i
    n
    t
    h
    e
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
    a
    n
    d
    C
    o
    d
    i
    n
    g
    d
    a
    t
    a
    t
    y
    p
    e
    s
    .
    
    """
    
    resource_type = "NamingSystem"
    
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
        n
        a
        m
        i
        n
        g
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
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
        n
        a
        m
        i
        n
        g
        s
        y
        s
        t
        e
        m
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
        
        self.kind = None
        """ 
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        |
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
        |
        r
        o
        o
        t
        .
        Type `str`. """
        
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
        n
        a
        m
        i
        n
        g
        s
        y
        s
        t
        e
        m
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
        
        self.responsible = None
        """ 
        W
        h
        o
        m
        a
        i
        n
        t
        a
        i
        n
        s
        s
        y
        s
        t
        e
        m
        n
        a
        m
        e
        s
        p
        a
        c
        e
        ?
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
        
        self.type = None
        """ 
        e
        .
        g
        .
        d
        r
        i
        v
        e
        r
        ,
        p
        r
        o
        v
        i
        d
        e
        r
        ,
        p
        a
        t
        i
        e
        n
        t
        ,
        b
        a
        n
        k
        e
        t
        c
        .
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uniqueId = None
        """ 
        U
        n
        i
        q
        u
        e
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
        s
        u
        s
        e
        d
        f
        o
        r
        s
        y
        s
        t
        e
        m
        .
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """
        
        self.usage = None
        """ 
        H
        o
        w
        /
        w
        h
        e
        r
        e
        i
        s
        i
        t
        u
        s
        e
        d
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
        
        super(NamingSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
        ])
        return js


from . import backboneelement

class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ 
    U
    n
    i
    q
    u
    e
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
    s
    u
    s
    e
    d
    f
    o
    r
    s
    y
    s
    t
    e
    m
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
    s
    y
    s
    t
    e
    m
    m
    a
    y
    b
    e
    i
    d
    e
    n
    t
    i
    f
    i
    e
    d
    w
    h
    e
    n
    r
    e
    f
    e
    r
    e
    n
    c
    e
    d
    i
    n
    e
    l
    e
    c
    t
    r
    o
    n
    i
    c
    e
    x
    c
    h
    a
    n
    g
    e
    .
    
    """
    
    resource_type = "NamingSystemUniqueId"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ 
        N
        o
        t
        e
        s
        a
        b
        o
        u
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
        u
        s
        a
        g
        e
        .
        Type `str`. """
        
        self.period = None
        """ 
        W
        h
        e
        n
        i
        s
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
        v
        a
        l
        i
        d
        ?
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.preferred = None
        """ 
        I
        s
        t
        h
        i
        s
        t
        h
        e
        i
        d
        t
        h
        a
        t
        s
        h
        o
        u
        l
        d
        b
        e
        u
        s
        e
        d
        f
        o
        r
        t
        h
        i
        s
        t
        y
        p
        e
        .
        Type `bool`. """
        
        self.type = None
        """ 
        o
        i
        d
        |
        u
        u
        i
        d
        |
        u
        r
        i
        |
        o
        t
        h
        e
        r
        .
        Type `str`. """
        
        self.value = None
        """ 
        T
        h
        e
        u
        n
        i
        q
        u
        e
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
        .
        Type `str`. """
        
        super(NamingSystemUniqueId, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("type", "type", str, False, None, True),
            ("value", "value", str, False, None, True),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
