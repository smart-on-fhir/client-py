#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchSubject) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ResearchSubject(domainresource.DomainResource):
    """ 
    P
    h
    y
    s
    i
    c
    a
    l
    e
    n
    t
    i
    t
    y
    w
    h
    i
    c
    h
    i
    s
    t
    h
    e
    p
    r
    i
    m
    a
    r
    y
    u
    n
    i
    t
    o
    f
    i
    n
    t
    e
    r
    e
    s
    t
    i
    n
    t
    h
    e
    s
    t
    u
    d
    y
    .
    
    
    A
    p
    h
    y
    s
    i
    c
    a
    l
    e
    n
    t
    i
    t
    y
    w
    h
    i
    c
    h
    i
    s
    t
    h
    e
    p
    r
    i
    m
    a
    r
    y
    u
    n
    i
    t
    o
    f
    o
    p
    e
    r
    a
    t
    i
    o
    n
    a
    l
    a
    n
    d
    /
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
    r
    a
    t
    i
    v
    e
    i
    n
    t
    e
    r
    e
    s
    t
    i
    n
    a
    s
    t
    u
    d
    y
    .
    
    """
    
    resource_type = "ResearchSubject"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actualArm = None
        """ 
        W
        h
        a
        t
        p
        a
        t
        h
        w
        a
        s
        f
        o
        l
        l
        o
        w
        e
        d
        .
        Type `str`. """
        
        self.assignedArm = None
        """ 
        W
        h
        a
        t
        p
        a
        t
        h
        s
        h
        o
        u
        l
        d
        b
        e
        f
        o
        l
        l
        o
        w
        e
        d
        .
        Type `str`. """
        
        self.consent = None
        """ 
        A
        g
        r
        e
        e
        m
        e
        n
        t
        t
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
        i
        n
        s
        t
        u
        d
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
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
        r
        e
        s
        e
        a
        r
        c
        h
        s
        u
        b
        j
        e
        c
        t
        i
        n
        a
        s
        t
        u
        d
        y
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.individual = None
        """ 
        W
        h
        o
        i
        s
        p
        a
        r
        t
        o
        f
        s
        t
        u
        d
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        S
        t
        a
        r
        t
        a
        n
        d
        e
        n
        d
        o
        f
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
        i
        o
        n
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        c
        a
        n
        d
        i
        d
        a
        t
        e
        |
        e
        l
        i
        g
        i
        b
        l
        e
        |
        f
        o
        l
        l
        o
        w
        -
        u
        p
        |
        i
        n
        e
        l
        i
        g
        i
        b
        l
        e
        |
        n
        o
        t
        -
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
        |
        o
        f
        f
        -
        s
        t
        u
        d
        y
        |
        o
        n
        -
        s
        t
        u
        d
        y
        |
        o
        n
        -
        s
        t
        u
        d
        y
        -
        i
        n
        t
        e
        r
        v
        e
        n
        t
        i
        o
        n
        |
        o
        n
        -
        s
        t
        u
        d
        y
        -
        o
        b
        s
        e
        r
        v
        a
        t
        i
        o
        n
        |
        p
        e
        n
        d
        i
        n
        g
        -
        o
        n
        -
        s
        t
        u
        d
        y
        |
        p
        o
        t
        e
        n
        t
        i
        a
        l
        -
        c
        a
        n
        d
        i
        d
        a
        t
        e
        |
        s
        c
        r
        e
        e
        n
        i
        n
        g
        |
        w
        i
        t
        h
        d
        r
        a
        w
        n
        .
        Type `str`. """
        
        self.study = None
        """ 
        S
        t
        u
        d
        y
        s
        u
        b
        j
        e
        c
        t
        i
        s
        p
        a
        r
        t
        o
        f
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ResearchSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchSubject, self).elementProperties()
        js.extend([
            ("actualArm", "actualArm", str, False, None, False),
            ("assignedArm", "assignedArm", str, False, None, False),
            ("consent", "consent", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("individual", "individual", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("study", "study", fhirreference.FHIRReference, False, None, True),
        ])
        return js


import sys
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
