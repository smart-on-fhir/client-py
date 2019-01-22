#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AllergyIntolerance) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class AllergyIntolerance(domainresource.DomainResource):
    """ 
    A
    l
    l
    e
    r
    g
    y
    o
    r
    I
    n
    t
    o
    l
    e
    r
    a
    n
    c
    e
    (
    g
    e
    n
    e
    r
    a
    l
    l
    y
    :
    R
    i
    s
    k
    o
    f
    a
    d
    v
    e
    r
    s
    e
    r
    e
    a
    c
    t
    i
    o
    n
    t
    o
    a
    s
    u
    b
    s
    t
    a
    n
    c
    e
    )
    .
    
    
    R
    i
    s
    k
    o
    f
    h
    a
    r
    m
    f
    u
    l
    o
    r
    u
    n
    d
    e
    s
    i
    r
    a
    b
    l
    e
    ,
    p
    h
    y
    s
    i
    o
    l
    o
    g
    i
    c
    a
    l
    r
    e
    s
    p
    o
    n
    s
    e
    w
    h
    i
    c
    h
    i
    s
    u
    n
    i
    q
    u
    e
    t
    o
    a
    n
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
    a
    n
    d
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
    e
    x
    p
    o
    s
    u
    r
    e
    t
    o
    a
    s
    u
    b
    s
    t
    a
    n
    c
    e
    .
    
    """
    
    resource_type = "AllergyIntolerance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asserter = None
        """ 
        S
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
        a
        l
        l
        e
        r
        g
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        f
        o
        o
        d
        |
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        |
        e
        n
        v
        i
        r
        o
        n
        m
        e
        n
        t
        |
        b
        i
        o
        l
        o
        g
        i
        c
        .
        List of `str` items. """
        
        self.clinicalStatus = None
        """ 
        a
        c
        t
        i
        v
        e
        |
        i
        n
        a
        c
        t
        i
        v
        e
        |
        r
        e
        s
        o
        l
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        C
        o
        d
        e
        t
        h
        a
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
        s
        t
        h
        e
        a
        l
        l
        e
        r
        g
        y
        o
        r
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.criticality = None
        """ 
        l
        o
        w
        |
        h
        i
        g
        h
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
        a
        s
        s
        e
        s
        s
        .
        Type `str`. """
        
        self.encounter = None
        """ 
        E
        n
        c
        o
        u
        n
        t
        e
        r
        w
        h
        e
        n
        t
        h
        e
        a
        l
        l
        e
        r
        g
        y
        o
        r
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        w
        a
        s
        a
        s
        s
        e
        r
        t
        e
        d
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
        i
        d
        s
        f
        o
        r
        t
        h
        i
        s
        i
        t
        e
        m
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastOccurrence = None
        """ 
        D
        a
        t
        e
        (
        /
        t
        i
        m
        e
        )
        o
        f
        l
        a
        s
        t
        k
        n
        o
        w
        n
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
        o
        f
        a
        r
        e
        a
        c
        t
        i
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.note = None
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
        t
        e
        x
        t
        n
        o
        t
        c
        a
        p
        t
        u
        r
        e
        d
        i
        n
        o
        t
        h
        e
        r
        f
        i
        e
        l
        d
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onsetAge = None
        """ 
        W
        h
        e
        n
        a
        l
        l
        e
        r
        g
        y
        o
        r
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        w
        a
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
        d
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetDateTime = None
        """ 
        W
        h
        e
        n
        a
        l
        l
        e
        r
        g
        y
        o
        r
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        w
        a
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
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onsetPeriod = None
        """ 
        W
        h
        e
        n
        a
        l
        l
        e
        r
        g
        y
        o
        r
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        w
        a
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
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ 
        W
        h
        e
        n
        a
        l
        l
        e
        r
        g
        y
        o
        r
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        w
        a
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
        d
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ 
        W
        h
        e
        n
        a
        l
        l
        e
        r
        g
        y
        o
        r
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        w
        a
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
        d
        .
        Type `str`. """
        
        self.patient = None
        """ 
        W
        h
        o
        t
        h
        e
        s
        e
        n
        s
        i
        t
        i
        v
        i
        t
        y
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reaction = None
        """ 
        A
        d
        v
        e
        r
        s
        e
        R
        e
        a
        c
        t
        i
        o
        n
        E
        v
        e
        n
        t
        s
        l
        i
        n
        k
        e
        d
        t
        o
        e
        x
        p
        o
        s
        u
        r
        e
        t
        o
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        List of `AllergyIntoleranceReaction` items (represented as `dict` in JSON). """
        
        self.recordedDate = None
        """ 
        D
        a
        t
        e
        f
        i
        r
        s
        t
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
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recorder = None
        """ 
        W
        h
        o
        r
        e
        c
        o
        r
        d
        e
        d
        t
        h
        e
        s
        e
        n
        s
        i
        t
        i
        v
        i
        t
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        a
        l
        l
        e
        r
        g
        y
        |
        i
        n
        t
        o
        l
        e
        r
        a
        n
        c
        e
        -
        U
        n
        d
        e
        r
        l
        y
        i
        n
        g
        m
        e
        c
        h
        a
        n
        i
        s
        m
        (
        i
        f
        k
        n
        o
        w
        n
        )
        .
        Type `str`. """
        
        self.verificationStatus = None
        """ 
        u
        n
        c
        o
        n
        f
        i
        r
        m
        e
        d
        |
        c
        o
        n
        f
        i
        r
        m
        e
        d
        |
        r
        e
        f
        u
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntolerance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AllergyIntolerance, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("category", "category", str, True, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("criticality", "criticality", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastOccurrence", "lastOccurrence", fhirdate.FHIRDate, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("reaction", "reaction", AllergyIntoleranceReaction, True, None, False),
            ("recordedDate", "recordedDate", fhirdate.FHIRDate, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, False),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class AllergyIntoleranceReaction(backboneelement.BackboneElement):
    """ 
    A
    d
    v
    e
    r
    s
    e
    R
    e
    a
    c
    t
    i
    o
    n
    E
    v
    e
    n
    t
    s
    l
    i
    n
    k
    e
    d
    t
    o
    e
    x
    p
    o
    s
    u
    r
    e
    t
    o
    s
    u
    b
    s
    t
    a
    n
    c
    e
    .
    
    
    D
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
    e
    a
    c
    h
    a
    d
    v
    e
    r
    s
    e
    r
    e
    a
    c
    t
    i
    o
    n
    e
    v
    e
    n
    t
    l
    i
    n
    k
    e
    d
    t
    o
    e
    x
    p
    o
    s
    u
    r
    e
    t
    o
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
    e
    d
    s
    u
    b
    s
    t
    a
    n
    c
    e
    .
    
    """
    
    resource_type = "AllergyIntoleranceReaction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
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
        t
        h
        e
        e
        v
        e
        n
        t
        a
        s
        a
        w
        h
        o
        l
        e
        .
        Type `str`. """
        
        self.exposureRoute = None
        """ 
        H
        o
        w
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
        w
        a
        s
        e
        x
        p
        o
        s
        e
        d
        t
        o
        t
        h
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manifestation = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        s
        y
        m
        p
        t
        o
        m
        s
        /
        s
        i
        g
        n
        s
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
        E
        v
        e
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ 
        T
        e
        x
        t
        a
        b
        o
        u
        t
        e
        v
        e
        n
        t
        n
        o
        t
        c
        a
        p
        t
        u
        r
        e
        d
        i
        n
        o
        t
        h
        e
        r
        f
        i
        e
        l
        d
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onset = None
        """ 
        D
        a
        t
        e
        (
        /
        t
        i
        m
        e
        )
        w
        h
        e
        n
        m
        a
        n
        i
        f
        e
        s
        t
        a
        t
        i
        o
        n
        s
        s
        h
        o
        w
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.severity = None
        """ 
        m
        i
        l
        d
        |
        m
        o
        d
        e
        r
        a
        t
        e
        |
        s
        e
        v
        e
        r
        e
        (
        o
        f
        e
        v
        e
        n
        t
        a
        s
        a
        w
        h
        o
        l
        e
        )
        .
        Type `str`. """
        
        self.substance = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        s
        u
        b
        s
        t
        a
        n
        c
        e
        o
        r
        p
        h
        a
        r
        m
        a
        c
        e
        u
        t
        i
        c
        a
        l
        p
        r
        o
        d
        u
        c
        t
        c
        o
        n
        s
        i
        d
        e
        r
        e
        d
        t
        o
        b
        e
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
        e
        v
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntoleranceReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AllergyIntoleranceReaction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("exposureRoute", "exposureRoute", codeableconcept.CodeableConcept, False, None, False),
            ("manifestation", "manifestation", codeableconcept.CodeableConcept, True, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onset", "onset", fhirdate.FHIRDate, False, None, False),
            ("severity", "severity", str, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
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
