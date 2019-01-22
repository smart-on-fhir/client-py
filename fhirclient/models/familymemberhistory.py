#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
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
    p
    a
    t
    i
    e
    n
    t
    '
    s
    r
    e
    l
    a
    t
    i
    v
    e
    s
    ,
    r
    e
    l
    e
    v
    a
    n
    t
    f
    o
    r
    p
    a
    t
    i
    e
    n
    t
    .
    
    
    S
    i
    g
    n
    i
    f
    i
    c
    a
    n
    t
    h
    e
    a
    l
    t
    h
    c
    o
    n
    d
    i
    t
    i
    o
    n
    s
    f
    o
    r
    a
    p
    e
    r
    s
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
    p
    a
    t
    i
    e
    n
    t
    r
    e
    l
    e
    v
    a
    n
    t
    i
    n
    t
    h
    e
    c
    o
    n
    t
    e
    x
    t
    o
    f
    c
    a
    r
    e
    f
    o
    r
    t
    h
    e
    p
    a
    t
    i
    e
    n
    t
    .
    
    """
    
    resource_type = "FamilyMemberHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageAge = None
        """ 
        (
        a
        p
        p
        r
        o
        x
        i
        m
        a
        t
        e
        )
        a
        g
        e
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.ageRange = None
        """ 
        (
        a
        p
        p
        r
        o
        x
        i
        m
        a
        t
        e
        )
        a
        g
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.ageString = None
        """ 
        (
        a
        p
        p
        r
        o
        x
        i
        m
        a
        t
        e
        )
        a
        g
        e
        .
        Type `str`. """
        
        self.bornDate = None
        """ 
        (
        a
        p
        p
        r
        o
        x
        i
        m
        a
        t
        e
        )
        d
        a
        t
        e
        o
        f
        b
        i
        r
        t
        h
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.bornPeriod = None
        """ 
        (
        a
        p
        p
        r
        o
        x
        i
        m
        a
        t
        e
        )
        d
        a
        t
        e
        o
        f
        b
        i
        r
        t
        h
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.bornString = None
        """ 
        (
        a
        p
        p
        r
        o
        x
        i
        m
        a
        t
        e
        )
        d
        a
        t
        e
        o
        f
        b
        i
        r
        t
        h
        .
        Type `str`. """
        
        self.condition = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
        t
        h
        a
        t
        t
        h
        e
        r
        e
        l
        a
        t
        e
        d
        p
        e
        r
        s
        o
        n
        h
        a
        d
        .
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
        
        self.dataAbsentReason = None
        """ 
        s
        u
        b
        j
        e
        c
        t
        -
        u
        n
        k
        n
        o
        w
        n
        |
        w
        i
        t
        h
        h
        e
        l
        d
        |
        u
        n
        a
        b
        l
        e
        -
        t
        o
        -
        o
        b
        t
        a
        i
        n
        |
        d
        e
        f
        e
        r
        r
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        W
        h
        e
        n
        h
        i
        s
        t
        o
        r
        y
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
        o
        r
        l
        a
        s
        t
        u
        p
        d
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedAge = None
        """ 
        D
        e
        a
        d
        ?
        H
        o
        w
        o
        l
        d
        /
        w
        h
        e
        n
        ?
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.deceasedBoolean = None
        """ 
        D
        e
        a
        d
        ?
        H
        o
        w
        o
        l
        d
        /
        w
        h
        e
        n
        ?
        .
        Type `bool`. """
        
        self.deceasedDate = None
        """ 
        D
        e
        a
        d
        ?
        H
        o
        w
        o
        l
        d
        /
        w
        h
        e
        n
        ?
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedRange = None
        """ 
        D
        e
        a
        d
        ?
        H
        o
        w
        o
        l
        d
        /
        w
        h
        e
        n
        ?
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.deceasedString = None
        """ 
        D
        e
        a
        d
        ?
        H
        o
        w
        o
        l
        d
        /
        w
        h
        e
        n
        ?
        .
        Type `str`. """
        
        self.estimatedAge = None
        """ 
        A
        g
        e
        i
        s
        e
        s
        t
        i
        m
        a
        t
        e
        d
        ?
        .
        Type `bool`. """
        
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
        (
        s
        )
        f
        o
        r
        t
        h
        i
        s
        r
        e
        c
        o
        r
        d
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        F
        H
        I
        R
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
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
        List of `str` items. """
        
        self.instantiatesUri = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        e
        x
        t
        e
        r
        n
        a
        l
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
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
        List of `str` items. """
        
        self.name = None
        """ 
        T
        h
        e
        f
        a
        m
        i
        l
        y
        m
        e
        m
        b
        e
        r
        d
        e
        s
        c
        r
        i
        b
        e
        d
        .
        Type `str`. """
        
        self.note = None
        """ 
        G
        e
        n
        e
        r
        a
        l
        n
        o
        t
        e
        a
        b
        o
        u
        t
        r
        e
        l
        a
        t
        e
        d
        p
        e
        r
        s
        o
        n
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        h
        i
        s
        t
        o
        r
        y
        i
        s
        a
        b
        o
        u
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        w
        a
        s
        f
        a
        m
        i
        l
        y
        m
        e
        m
        b
        e
        r
        h
        i
        s
        t
        o
        r
        y
        p
        e
        r
        f
        o
        r
        m
        e
        d
        ?
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        w
        a
        s
        f
        a
        m
        i
        l
        y
        m
        e
        m
        b
        e
        r
        h
        i
        s
        t
        o
        r
        y
        p
        e
        r
        f
        o
        r
        m
        e
        d
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        R
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        t
        o
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sex = None
        """ 
        m
        a
        l
        e
        |
        f
        e
        m
        a
        l
        e
        |
        o
        t
        h
        e
        r
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        p
        a
        r
        t
        i
        a
        l
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
        h
        e
        a
        l
        t
        h
        -
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        super(FamilyMemberHistory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageAge", "ageAge", age.Age, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("ageString", "ageString", str, False, "age", False),
            ("bornDate", "bornDate", fhirdate.FHIRDate, False, "born", False),
            ("bornPeriod", "bornPeriod", period.Period, False, "born", False),
            ("bornString", "bornString", str, False, "born", False),
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False),
            ("dataAbsentReason", "dataAbsentReason", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deceasedAge", "deceasedAge", age.Age, False, "deceased", False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDate", "deceasedDate", fhirdate.FHIRDate, False, "deceased", False),
            ("deceasedRange", "deceasedRange", range.Range, False, "deceased", False),
            ("deceasedString", "deceasedString", str, False, "deceased", False),
            ("estimatedAge", "estimatedAge", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, True),
            ("sex", "sex", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    d
    i
    t
    i
    o
    n
    t
    h
    a
    t
    t
    h
    e
    r
    e
    l
    a
    t
    e
    d
    p
    e
    r
    s
    o
    n
    h
    a
    d
    .
    
    
    T
    h
    e
    s
    i
    g
    n
    i
    f
    i
    c
    a
    n
    t
    C
    o
    n
    d
    i
    t
    i
    o
    n
    s
    (
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
    )
    t
    h
    a
    t
    t
    h
    e
    f
    a
    m
    i
    l
    y
    m
    e
    m
    b
    e
    r
    h
    a
    d
    .
    T
    h
    i
    s
    i
    s
    a
    r
    e
    p
    e
    a
    t
    i
    n
    g
    s
    e
    c
    t
    i
    o
    n
    t
    o
    a
    l
    l
    o
    w
    a
    s
    y
    s
    t
    e
    m
    t
    o
    r
    e
    p
    r
    e
    s
    e
    n
    t
    m
    o
    r
    e
    t
    h
    a
    n
    o
    n
    e
    c
    o
    n
    d
    i
    t
    i
    o
    n
    p
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
    ,
    t
    h
    o
    u
    g
    h
    t
    h
    e
    r
    e
    i
    s
    n
    o
    t
    h
    i
    n
    g
    s
    t
    o
    p
    p
    i
    n
    g
    m
    u
    l
    t
    i
    p
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
    s
    -
    o
    n
    e
    p
    e
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
    .
    
    """
    
    resource_type = "FamilyMemberHistoryCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
        s
        u
        f
        f
        e
        r
        e
        d
        b
        y
        r
        e
        l
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contributedToDeath = None
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
        c
        o
        n
        d
        i
        t
        i
        o
        n
        c
        o
        n
        t
        r
        i
        b
        u
        t
        e
        d
        t
        o
        t
        h
        e
        c
        a
        u
        s
        e
        o
        f
        d
        e
        a
        t
        h
        .
        Type `bool`. """
        
        self.note = None
        """ 
        E
        x
        t
        r
        a
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
        c
        o
        n
        d
        i
        t
        i
        o
        n
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge = None
        """ 
        W
        h
        e
        n
        c
        o
        n
        d
        i
        t
        i
        o
        n
        f
        i
        r
        s
        t
        m
        a
        n
        i
        f
        e
        s
        t
        e
        d
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetPeriod = None
        """ 
        W
        h
        e
        n
        c
        o
        n
        d
        i
        t
        i
        o
        n
        f
        i
        r
        s
        t
        m
        a
        n
        i
        f
        e
        s
        t
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ 
        W
        h
        e
        n
        c
        o
        n
        d
        i
        t
        i
        o
        n
        f
        i
        r
        s
        t
        m
        a
        n
        i
        f
        e
        s
        t
        e
        d
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ 
        W
        h
        e
        n
        c
        o
        n
        d
        i
        t
        i
        o
        n
        f
        i
        r
        s
        t
        m
        a
        n
        i
        f
        e
        s
        t
        e
        d
        .
        Type `str`. """
        
        self.outcome = None
        """ 
        d
        e
        c
        e
        a
        s
        e
        d
        |
        p
        e
        r
        m
        a
        n
        e
        n
        t
        d
        i
        s
        a
        b
        i
        l
        i
        t
        y
        |
        e
        t
        c
        .
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(FamilyMemberHistoryCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("contributedToDeath", "contributedToDeath", bool, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
