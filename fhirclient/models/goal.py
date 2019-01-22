#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Goal) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Goal(domainresource.DomainResource):
    """ 
    D
    e
    s
    c
    r
    i
    b
    e
    s
    t
    h
    e
    i
    n
    t
    e
    n
    d
    e
    d
    o
    b
    j
    e
    c
    t
    i
    v
    e
    (
    s
    )
    f
    o
    r
    a
    p
    a
    t
    i
    e
    n
    t
    ,
    g
    r
    o
    u
    p
    o
    r
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
    .
    
    
    D
    e
    s
    c
    r
    i
    b
    e
    s
    t
    h
    e
    i
    n
    t
    e
    n
    d
    e
    d
    o
    b
    j
    e
    c
    t
    i
    v
    e
    (
    s
    )
    f
    o
    r
    a
    p
    a
    t
    i
    e
    n
    t
    ,
    g
    r
    o
    u
    p
    o
    r
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
    c
    a
    r
    e
    ,
    f
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
    w
    e
    i
    g
    h
    t
    l
    o
    s
    s
    ,
    r
    e
    s
    t
    o
    r
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
    i
    t
    y
    o
    f
    d
    a
    i
    l
    y
    l
    i
    v
    i
    n
    g
    ,
    o
    b
    t
    a
    i
    n
    i
    n
    g
    h
    e
    r
    d
    i
    m
    m
    u
    n
    i
    t
    y
    v
    i
    a
    i
    m
    m
    u
    n
    i
    z
    a
    t
    i
    o
    n
    ,
    m
    e
    e
    t
    i
    n
    g
    a
    p
    r
    o
    c
    e
    s
    s
    i
    m
    p
    r
    o
    v
    e
    m
    e
    n
    t
    o
    b
    j
    e
    c
    t
    i
    v
    e
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "Goal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.achievementStatus = None
        """ 
        i
        n
        -
        p
        r
        o
        g
        r
        e
        s
        s
        |
        i
        m
        p
        r
        o
        v
        i
        n
        g
        |
        w
        o
        r
        s
        e
        n
        i
        n
        g
        |
        n
        o
        -
        c
        h
        a
        n
        g
        e
        |
        a
        c
        h
        i
        e
        v
        e
        d
        |
        s
        u
        s
        t
        a
        i
        n
        i
        n
        g
        |
        n
        o
        t
        -
        a
        c
        h
        i
        e
        v
        e
        d
        |
        n
        o
        -
        p
        r
        o
        g
        r
        e
        s
        s
        |
        n
        o
        t
        -
        a
        t
        t
        a
        i
        n
        a
        b
        l
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.addresses = None
        """ 
        I
        s
        s
        u
        e
        s
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
        i
        s
        g
        o
        a
        l
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        E
        .
        g
        .
        T
        r
        e
        a
        t
        m
        e
        n
        t
        ,
        d
        i
        e
        t
        a
        r
        y
        ,
        b
        e
        h
        a
        v
        i
        o
        r
        a
        l
        ,
        e
        t
        c
        .
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        C
        o
        d
        e
        o
        r
        t
        e
        x
        t
        d
        e
        s
        c
        r
        i
        b
        i
        n
        g
        g
        o
        a
        l
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.expressedBy = None
        """ 
        W
        h
        o
        '
        s
        r
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        f
        o
        r
        c
        r
        e
        a
        t
        i
        n
        g
        G
        o
        a
        l
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        E
        x
        t
        e
        r
        n
        a
        l
        I
        d
        s
        f
        o
        r
        t
        h
        i
        s
        g
        o
        a
        l
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lifecycleStatus = None
        """ 
        p
        r
        o
        p
        o
        s
        e
        d
        |
        p
        l
        a
        n
        n
        e
        d
        |
        a
        c
        c
        e
        p
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
        o
        n
        -
        h
        o
        l
        d
        |
        c
        o
        m
        p
        l
        e
        t
        e
        d
        |
        c
        a
        n
        c
        e
        l
        l
        e
        d
        |
        e
        n
        t
        e
        r
        e
        d
        -
        i
        n
        -
        e
        r
        r
        o
        r
        |
        r
        e
        j
        e
        c
        t
        e
        d
        .
        Type `str`. """
        
        self.note = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        s
        a
        b
        o
        u
        t
        t
        h
        e
        g
        o
        a
        l
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcomeCode = None
        """ 
        W
        h
        a
        t
        r
        e
        s
        u
        l
        t
        w
        a
        s
        a
        c
        h
        i
        e
        v
        e
        d
        r
        e
        g
        a
        r
        d
        i
        n
        g
        t
        h
        e
        g
        o
        a
        l
        ?
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcomeReference = None
        """ 
        O
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
        e
        d
        f
        r
        o
        m
        g
        o
        a
        l
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ 
        h
        i
        g
        h
        -
        p
        r
        i
        o
        r
        i
        t
        y
        |
        m
        e
        d
        i
        u
        m
        -
        p
        r
        i
        o
        r
        i
        t
        y
        |
        l
        o
        w
        -
        p
        r
        i
        o
        r
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startCodeableConcept = None
        """ 
        W
        h
        e
        n
        g
        o
        a
        l
        p
        u
        r
        s
        u
        i
        t
        b
        e
        g
        i
        n
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startDate = None
        """ 
        W
        h
        e
        n
        g
        o
        a
        l
        p
        u
        r
        s
        u
        i
        t
        b
        e
        g
        i
        n
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.statusDate = None
        """ 
        W
        h
        e
        n
        g
        o
        a
        l
        s
        t
        a
        t
        u
        s
        t
        o
        o
        k
        e
        f
        f
        e
        c
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ 
        R
        e
        a
        s
        o
        n
        f
        o
        r
        c
        u
        r
        r
        e
        n
        t
        s
        t
        a
        t
        u
        s
        .
        Type `str`. """
        
        self.subject = None
        """ 
        W
        h
        o
        t
        h
        i
        s
        g
        o
        a
        l
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.target = None
        """ 
        T
        a
        r
        g
        e
        t
        o
        u
        t
        c
        o
        m
        e
        f
        o
        r
        t
        h
        e
        g
        o
        a
        l
        .
        List of `GoalTarget` items (represented as `dict` in JSON). """
        
        super(Goal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("achievementStatus", "achievementStatus", codeableconcept.CodeableConcept, False, None, False),
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", codeableconcept.CodeableConcept, False, None, True),
            ("expressedBy", "expressedBy", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lifecycleStatus", "lifecycleStatus", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcomeCode", "outcomeCode", codeableconcept.CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, False, "start", False),
            ("startDate", "startDate", fhirdate.FHIRDate, False, "start", False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("statusReason", "statusReason", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("target", "target", GoalTarget, True, None, False),
        ])
        return js


from . import backboneelement

class GoalTarget(backboneelement.BackboneElement):
    """ 
    T
    a
    r
    g
    e
    t
    o
    u
    t
    c
    o
    m
    e
    f
    o
    r
    t
    h
    e
    g
    o
    a
    l
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
    s
    h
    o
    u
    l
    d
    b
    e
    d
    o
    n
    e
    b
    y
    w
    h
    e
    n
    .
    
    """
    
    resource_type = "GoalTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detailBoolean = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `bool`. """
        
        self.detailCodeableConcept = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailInteger = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `int`. """
        
        self.detailQuantity = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.detailRange = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.detailRatio = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.detailString = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        v
        a
        l
        u
        e
        t
        o
        b
        e
        a
        c
        h
        i
        e
        v
        e
        d
        .
        Type `str`. """
        
        self.dueDate = None
        """ 
        R
        e
        a
        c
        h
        g
        o
        a
        l
        o
        n
        o
        r
        b
        e
        f
        o
        r
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dueDuration = None
        """ 
        R
        e
        a
        c
        h
        g
        o
        a
        l
        o
        n
        o
        r
        b
        e
        f
        o
        r
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.measure = None
        """ 
        T
        h
        e
        p
        a
        r
        a
        m
        e
        t
        e
        r
        w
        h
        o
        s
        e
        v
        a
        l
        u
        e
        i
        s
        b
        e
        i
        n
        g
        t
        r
        a
        c
        k
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(GoalTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("detailBoolean", "detailBoolean", bool, False, "detail", False),
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False),
            ("detailInteger", "detailInteger", int, False, "detail", False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False),
            ("detailRange", "detailRange", range.Range, False, "detail", False),
            ("detailRatio", "detailRatio", ratio.Ratio, False, "detail", False),
            ("detailString", "detailString", str, False, "detail", False),
            ("dueDate", "dueDate", fhirdate.FHIRDate, False, "due", False),
            ("dueDuration", "dueDuration", duration.Duration, False, "due", False),
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
