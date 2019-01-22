#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Procedure) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Procedure(domainresource.DomainResource):
    """ 
    A
    n
    a
    c
    t
    i
    o
    n
    t
    h
    a
    t
    i
    s
    b
    e
    i
    n
    g
    o
    r
    w
    a
    s
    p
    e
    r
    f
    o
    r
    m
    e
    d
    o
    n
    a
    p
    a
    t
    i
    e
    n
    t
    .
    
    
    A
    n
    a
    c
    t
    i
    o
    n
    t
    h
    a
    t
    i
    s
    o
    r
    w
    a
    s
    p
    e
    r
    f
    o
    r
    m
    e
    d
    o
    n
    o
    r
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
    .
    T
    h
    i
    s
    c
    a
    n
    b
    e
    a
    p
    h
    y
    s
    i
    c
    a
    l
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
    l
    i
    k
    e
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
    ,
    o
    r
    l
    e
    s
    s
    i
    n
    v
    a
    s
    i
    v
    e
    l
    i
    k
    e
    l
    o
    n
    g
    t
    e
    r
    m
    s
    e
    r
    v
    i
    c
    e
    s
    ,
    c
    o
    u
    n
    s
    e
    l
    i
    n
    g
    ,
    o
    r
    h
    y
    p
    n
    o
    t
    h
    e
    r
    a
    p
    y
    .
    
    """
    
    resource_type = "Procedure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asserter = None
        """ 
        P
        e
        r
        s
        o
        n
        w
        h
        o
        a
        s
        s
        e
        r
        t
        s
        t
        h
        i
        s
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ 
        A
        r
        e
        q
        u
        e
        s
        t
        f
        o
        r
        t
        h
        i
        s
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ 
        T
        a
        r
        g
        e
        t
        b
        o
        d
        y
        s
        i
        t
        e
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        C
        l
        a
        s
        s
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
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        c
        a
        t
        i
        o
        n
        o
        f
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.complication = None
        """ 
        C
        o
        m
        p
        l
        i
        c
        a
        t
        i
        o
        n
        f
        o
        l
        l
        o
        w
        i
        n
        g
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complicationDetail = None
        """ 
        A
        c
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
        i
        s
        a
        r
        e
        s
        u
        l
        t
        o
        f
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        c
        r
        e
        a
        t
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.focalDevice = None
        """ 
        M
        a
        n
        i
        p
        u
        l
        a
        t
        e
        d
        ,
        i
        m
        p
        l
        a
        n
        t
        e
        d
        ,
        o
        r
        r
        e
        m
        o
        v
        e
        d
        d
        e
        v
        i
        c
        e
        .
        List of `ProcedureFocalDevice` items (represented as `dict` in JSON). """
        
        self.followUp = None
        """ 
        I
        n
        s
        t
        r
        u
        c
        t
        i
        o
        n
        s
        f
        o
        r
        f
        o
        l
        l
        o
        w
        u
        p
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        e
        n
        t
        i
        f
        i
        e
        r
        s
        f
        o
        r
        t
        h
        i
        s
        p
        r
        o
        c
        e
        d
        u
        r
        e
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
        
        self.location = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        h
        a
        p
        p
        e
        n
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ 
        T
        h
        e
        r
        e
        s
        u
        l
        t
        o
        f
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ 
        P
        a
        r
        t
        o
        f
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
        e
        v
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performedAge = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.performedDateTime = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.performedPeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.performedRange = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.performedString = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        Type `str`. """
        
        self.performer = None
        """ 
        T
        h
        e
        p
        e
        o
        p
        l
        e
        w
        h
        o
        p
        e
        r
        f
        o
        r
        m
        e
        d
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        C
        o
        d
        e
        d
        r
        e
        a
        s
        o
        n
        p
        r
        o
        c
        e
        d
        u
        r
        e
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        T
        h
        e
        j
        u
        s
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
        t
        h
        a
        t
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.report = None
        """ 
        A
        n
        y
        r
        e
        p
        o
        r
        t
        r
        e
        s
        u
        l
        t
        i
        n
        g
        f
        r
        o
        m
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        p
        r
        e
        p
        a
        r
        a
        t
        i
        o
        n
        |
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
        n
        o
        t
        -
        d
        o
        n
        e
        |
        s
        u
        s
        p
        e
        n
        d
        e
        d
        |
        a
        b
        o
        r
        t
        e
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
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        W
        h
        o
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        w
        a
        s
        p
        e
        r
        f
        o
        r
        m
        e
        d
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.usedCode = None
        """ 
        C
        o
        d
        e
        d
        i
        t
        e
        m
        s
        u
        s
        e
        d
        d
        u
        r
        i
        n
        g
        t
        h
        e
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.usedReference = None
        """ 
        I
        t
        e
        m
        s
        u
        s
        e
        d
        d
        u
        r
        i
        n
        g
        p
        r
        o
        c
        e
        d
        u
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Procedure, self).elementProperties()
        js.extend([
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("complication", "complication", codeableconcept.CodeableConcept, True, None, False),
            ("complicationDetail", "complicationDetail", fhirreference.FHIRReference, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("focalDevice", "focalDevice", ProcedureFocalDevice, True, None, False),
            ("followUp", "followUp", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performedAge", "performedAge", age.Age, False, "performed", False),
            ("performedDateTime", "performedDateTime", fhirdate.FHIRDate, False, "performed", False),
            ("performedPeriod", "performedPeriod", period.Period, False, "performed", False),
            ("performedRange", "performedRange", range.Range, False, "performed", False),
            ("performedString", "performedString", str, False, "performed", False),
            ("performer", "performer", ProcedurePerformer, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("report", "report", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("usedCode", "usedCode", codeableconcept.CodeableConcept, True, None, False),
            ("usedReference", "usedReference", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class ProcedureFocalDevice(backboneelement.BackboneElement):
    """ 
    M
    a
    n
    i
    p
    u
    l
    a
    t
    e
    d
    ,
    i
    m
    p
    l
    a
    n
    t
    e
    d
    ,
    o
    r
    r
    e
    m
    o
    v
    e
    d
    d
    e
    v
    i
    c
    e
    .
    
    
    A
    d
    e
    v
    i
    c
    e
    t
    h
    a
    t
    i
    s
    i
    m
    p
    l
    a
    n
    t
    e
    d
    ,
    r
    e
    m
    o
    v
    e
    d
    o
    r
    o
    t
    h
    e
    r
    w
    i
    s
    e
    m
    a
    n
    i
    p
    u
    l
    a
    t
    e
    d
    (
    c
    a
    l
    i
    b
    r
    a
    t
    i
    o
    n
    ,
    b
    a
    t
    t
    e
    r
    y
    r
    e
    p
    l
    a
    c
    e
    m
    e
    n
    t
    ,
    f
    i
    t
    t
    i
    n
    g
    a
    p
    r
    o
    s
    t
    h
    e
    s
    i
    s
    ,
    a
    t
    t
    a
    c
    h
    i
    n
    g
    a
    w
    o
    u
    n
    d
    -
    v
    a
    c
    ,
    e
    t
    c
    .
    )
    a
    s
    a
    f
    o
    c
    a
    l
    p
    o
    r
    t
    i
    o
    n
    o
    f
    t
    h
    e
    P
    r
    o
    c
    e
    d
    u
    r
    e
    .
    
    """
    
    resource_type = "ProcedureFocalDevice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        K
        i
        n
        d
        o
        f
        c
        h
        a
        n
        g
        e
        t
        o
        d
        e
        v
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manipulated = None
        """ 
        D
        e
        v
        i
        c
        e
        t
        h
        a
        t
        w
        a
        s
        c
        h
        a
        n
        g
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedureFocalDevice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedureFocalDevice, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, False),
            ("manipulated", "manipulated", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ProcedurePerformer(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    p
    e
    o
    p
    l
    e
    w
    h
    o
    p
    e
    r
    f
    o
    r
    m
    e
    d
    t
    h
    e
    p
    r
    o
    c
    e
    d
    u
    r
    e
    .
    
    
    L
    i
    m
    i
    t
    e
    d
    t
    o
    "
    r
    e
    a
    l
    "
    p
    e
    o
    p
    l
    e
    r
    a
    t
    h
    e
    r
    t
    h
    a
    n
    e
    q
    u
    i
    p
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "ProcedurePerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ 
        T
        h
        e
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
        t
        h
        e
        p
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function = None
        """ 
        T
        y
        p
        e
        o
        f
        p
        e
        r
        f
        o
        r
        m
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ 
        O
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
        t
        h
        e
        d
        e
        v
        i
        c
        e
        o
        r
        p
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        w
        a
        s
        a
        c
        t
        i
        n
        g
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProcedurePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
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
