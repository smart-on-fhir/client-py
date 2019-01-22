#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/OperationOutcome) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class OperationOutcome(domainresource.DomainResource):
    """ 
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
    u
    c
    c
    e
    s
    s
    /
    f
    a
    i
    l
    u
    r
    e
    o
    f
    a
    n
    a
    c
    t
    i
    o
    n
    .
    
    
    A
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
    e
    r
    r
    o
    r
    ,
    w
    a
    r
    n
    i
    n
    g
    ,
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
    m
    e
    s
    s
    a
    g
    e
    s
    t
    h
    a
    t
    r
    e
    s
    u
    l
    t
    f
    r
    o
    m
    a
    s
    y
    s
    t
    e
    m
    a
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "OperationOutcome"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.issue = None
        """ 
        A
        s
        i
        n
        g
        l
        e
        i
        s
        s
        u
        e
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        t
        h
        e
        a
        c
        t
        i
        o
        n
        .
        List of `OperationOutcomeIssue` items (represented as `dict` in JSON). """
        
        super(OperationOutcome, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcome, self).elementProperties()
        js.extend([
            ("issue", "issue", OperationOutcomeIssue, True, None, True),
        ])
        return js


from . import backboneelement

class OperationOutcomeIssue(backboneelement.BackboneElement):
    """ 
    A
    s
    i
    n
    g
    l
    e
    i
    s
    s
    u
    e
    a
    s
    s
    o
    c
    i
    a
    t
    e
    d
    w
    i
    t
    h
    t
    h
    e
    a
    c
    t
    i
    o
    n
    .
    
    
    A
    n
    e
    r
    r
    o
    r
    ,
    w
    a
    r
    n
    i
    n
    g
    ,
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
    r
    e
    s
    u
    l
    t
    s
    f
    r
    o
    m
    a
    s
    y
    s
    t
    e
    m
    a
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "OperationOutcomeIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        E
        r
        r
        o
        r
        o
        r
        w
        a
        r
        n
        i
        n
        g
        c
        o
        d
        e
        .
        Type `str`. """
        
        self.details = None
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
        d
        e
        t
        a
        i
        l
        s
        a
        b
        o
        u
        t
        t
        h
        e
        e
        r
        r
        o
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.diagnostics = None
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
        d
        i
        a
        g
        n
        o
        s
        t
        i
        c
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
        i
        s
        s
        u
        e
        .
        Type `str`. """
        
        self.expression = None
        """ 
        F
        H
        I
        R
        P
        a
        t
        h
        o
        f
        e
        l
        e
        m
        e
        n
        t
        (
        s
        )
        r
        e
        l
        a
        t
        e
        d
        t
        o
        i
        s
        s
        u
        e
        .
        List of `str` items. """
        
        self.location = None
        """ 
        D
        e
        p
        r
        e
        c
        a
        t
        e
        d
        :
        P
        a
        t
        h
        o
        f
        e
        l
        e
        m
        e
        n
        t
        (
        s
        )
        r
        e
        l
        a
        t
        e
        d
        t
        o
        i
        s
        s
        u
        e
        .
        List of `str` items. """
        
        self.severity = None
        """ 
        f
        a
        t
        a
        l
        |
        e
        r
        r
        o
        r
        |
        w
        a
        r
        n
        i
        n
        g
        |
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
        Type `str`. """
        
        super(OperationOutcomeIssue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationOutcomeIssue, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", codeableconcept.CodeableConcept, False, None, False),
            ("diagnostics", "diagnostics", str, False, None, False),
            ("expression", "expression", str, True, None, False),
            ("location", "location", str, True, None, False),
            ("severity", "severity", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
