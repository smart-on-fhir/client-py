#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicationAdministration(domainresource.DomainResource):
    """ 
    A
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
    o
    n
    o
    f
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
    t
    o
    a
    p
    a
    t
    i
    e
    n
    t
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
    e
    v
    e
    n
    t
    o
    f
    a
    p
    a
    t
    i
    e
    n
    t
    c
    o
    n
    s
    u
    m
    i
    n
    g
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
    b
    e
    i
    n
    g
    a
    d
    m
    i
    n
    i
    s
    t
    e
    r
    e
    d
    a
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
    .
    T
    h
    i
    s
    m
    a
    y
    b
    e
    a
    s
    s
    i
    m
    p
    l
    e
    a
    s
    s
    w
    a
    l
    l
    o
    w
    i
    n
    g
    a
    t
    a
    b
    l
    e
    t
    o
    r
    i
    t
    m
    a
    y
    b
    e
    a
    l
    o
    n
    g
    r
    u
    n
    n
    i
    n
    g
    i
    n
    f
    u
    s
    i
    o
    n
    .
    R
    e
    l
    a
    t
    e
    d
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
    i
    e
    t
    h
    i
    s
    e
    v
    e
    n
    t
    t
    o
    t
    h
    e
    a
    u
    t
    h
    o
    r
    i
    z
    i
    n
    g
    p
    r
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
    ,
    a
    n
    d
    t
    h
    e
    s
    p
    e
    c
    i
    f
    i
    c
    e
    n
    c
    o
    u
    n
    t
    e
    r
    b
    e
    t
    w
    e
    e
    n
    p
    a
    t
    i
    e
    n
    t
    a
    n
    d
    h
    e
    a
    l
    t
    h
    c
    a
    r
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
    
    """
    
    resource_type = "MedicationAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ 
        T
        y
        p
        e
        o
        f
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
        u
        s
        a
        g
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
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
        o
        r
        E
        p
        i
        s
        o
        d
        e
        o
        f
        C
        a
        r
        e
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
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
        
        self.device = None
        """ 
        D
        e
        v
        i
        c
        e
        u
        s
        e
        d
        t
        o
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.dosage = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        o
        f
        h
        o
        w
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
        w
        a
        s
        t
        a
        k
        e
        n
        .
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
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
        t
        i
        m
        e
        o
        f
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
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
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
        t
        i
        m
        e
        o
        f
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
        o
        n
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.eventHistory = None
        """ 
        A
        l
        i
        s
        t
        o
        f
        e
        v
        e
        n
        t
        s
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
        l
        i
        f
        e
        c
        y
        c
        l
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        e
        n
        t
        i
        f
        i
        e
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiates = None
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
        
        self.medicationCodeableConcept = None
        """ 
        W
        h
        a
        t
        w
        a
        s
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ 
        W
        h
        a
        t
        w
        a
        s
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note = None
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
        o
        n
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
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
        
        self.performer = None
        """ 
        W
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
        o
        n
        a
        n
        d
        w
        h
        a
        t
        t
        h
        e
        y
        d
        i
        d
        .
        List of `MedicationAdministrationPerformer` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        R
        e
        a
        s
        o
        n
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
        o
        n
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
        C
        o
        n
        d
        i
        t
        i
        o
        n
        o
        r
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
        t
        h
        a
        t
        s
        u
        p
        p
        o
        r
        t
        s
        w
        h
        y
        t
        h
        e
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
        w
        a
        s
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.request = None
        """ 
        R
        e
        q
        u
        e
        s
        t
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
        o
        n
        p
        e
        r
        f
        o
        r
        m
        e
        d
        a
        g
        a
        i
        n
        s
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
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
        n
        o
        t
        -
        d
        o
        n
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
        s
        t
        o
        p
        p
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
        
        self.statusReason = None
        """ 
        R
        e
        a
        s
        o
        n
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
        o
        n
        n
        o
        t
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
        
        self.subject = None
        """ 
        W
        h
        o
        r
        e
        c
        e
        i
        v
        e
        d
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
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
        t
        o
        s
        u
        p
        p
        o
        r
        t
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
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicationAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", True),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", True),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", MedicationAdministrationPerformer, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ 
    D
    e
    t
    a
    i
    l
    s
    o
    f
    h
    o
    w
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
    w
    a
    s
    t
    a
    k
    e
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
    d
    o
    s
    a
    g
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
    d
    e
    t
    a
    i
    l
    s
    e
    .
    g
    .
    d
    o
    s
    e
    ,
    r
    a
    t
    e
    ,
    s
    i
    t
    e
    ,
    r
    o
    u
    t
    e
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "MedicationAdministrationDosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dose = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
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
        p
        e
        r
        d
        o
        s
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.method = None
        """ 
        H
        o
        w
        d
        r
        u
        g
        w
        a
        s
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ 
        D
        o
        s
        e
        q
        u
        a
        n
        t
        i
        t
        y
        p
        e
        r
        u
        n
        i
        t
        o
        f
        t
        i
        m
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ 
        D
        o
        s
        e
        q
        u
        a
        n
        t
        i
        t
        y
        p
        e
        r
        u
        n
        i
        t
        o
        f
        t
        i
        m
        e
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ 
        P
        a
        t
        h
        o
        f
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        n
        t
        o
        b
        o
        d
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ 
        B
        o
        d
        y
        s
        i
        t
        e
        a
        d
        m
        i
        n
        i
        s
        t
        e
        r
        e
        d
        t
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        F
        r
        e
        e
        t
        e
        x
        t
        d
        o
        s
        a
        g
        e
        i
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
        e
        .
        g
        .
        S
        I
        G
        .
        Type `str`. """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("dose", "dose", quantity.Quantity, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """ 
    W
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
    o
    n
    a
    n
    d
    w
    h
    a
    t
    t
    h
    e
    y
    d
    i
    d
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
    o
    o
    r
    w
    h
    a
    t
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
    o
    n
    a
    n
    d
    h
    o
    w
    t
    h
    e
    y
    w
    e
    r
    e
    i
    n
    v
    o
    l
    v
    e
    d
    .
    
    """
    
    resource_type = "MedicationAdministrationPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ 
        W
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
        o
        n
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
        
        super(MedicationAdministrationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
