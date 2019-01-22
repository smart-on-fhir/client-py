#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicationDispense(domainresource.DomainResource):
    """ 
    D
    i
    s
    p
    e
    n
    s
    i
    n
    g
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
    t
    o
    a
    n
    a
    m
    e
    d
    p
    a
    t
    i
    e
    n
    t
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
    t
    h
    a
    t
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
    p
    r
    o
    d
    u
    c
    t
    i
    s
    t
    o
    b
    e
    o
    r
    h
    a
    s
    b
    e
    e
    n
    d
    i
    s
    p
    e
    n
    s
    e
    d
    f
    o
    r
    a
    n
    a
    m
    e
    d
    p
    e
    r
    s
    o
    n
    /
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
    i
    n
    c
    l
    u
    d
    e
    s
    a
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
    d
    i
    c
    a
    t
    i
    o
    n
    p
    r
    o
    d
    u
    c
    t
    (
    s
    u
    p
    p
    l
    y
    )
    p
    r
    o
    v
    i
    d
    e
    d
    a
    n
    d
    t
    h
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
    f
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
    e
    r
    i
    n
    g
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
    .
    T
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
    i
    s
    p
    e
    n
    s
    e
    i
    s
    t
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
    a
    p
    h
    a
    r
    m
    a
    c
    y
    s
    y
    s
    t
    e
    m
    r
    e
    s
    p
    o
    n
    d
    i
    n
    g
    t
    o
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
    o
    r
    d
    e
    r
    .
    
    """
    
    resource_type = "MedicationDispense"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorizingPrescription = None
        """ 
        M
        e
        d
        i
        c
        a
        t
        i
        o
        n
        o
        r
        d
        e
        r
        t
        h
        a
        t
        a
        u
        t
        h
        o
        r
        i
        z
        e
        s
        t
        h
        e
        d
        i
        s
        p
        e
        n
        s
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        d
        i
        s
        p
        e
        n
        s
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
        /
        E
        p
        i
        s
        o
        d
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
        e
        v
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.daysSupply = None
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
        e
        x
        p
        r
        e
        s
        s
        e
        d
        a
        s
        a
        t
        i
        m
        i
        n
        g
        a
        m
        o
        u
        n
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.destination = None
        """ 
        W
        h
        e
        r
        e
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
        s
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.detectedIssue = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        i
        s
        s
        u
        e
        w
        i
        t
        h
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ 
        H
        o
        w
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
        i
        s
        t
        o
        b
        e
        u
        s
        e
        d
        b
        y
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
        e
        r
        e
        d
        b
        y
        t
        h
        e
        c
        a
        r
        e
        g
        i
        v
        e
        r
        .
        List of `Dosage` items (represented as `dict` in JSON). """
        
        self.eventHistory = None
        """ 
        A
        l
        i
        s
        t
        o
        f
        r
        e
        l
        e
        v
        a
        n
        t
        l
        i
        f
        e
        c
        y
        c
        l
        e
        e
        v
        e
        n
        t
        s
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
        d
        i
        s
        p
        e
        n
        s
        e
        o
        c
        c
        u
        r
        r
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ 
        W
        h
        a
        t
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
        s
        u
        p
        p
        l
        i
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
        s
        u
        p
        p
        l
        i
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
        d
        i
        s
        p
        e
        n
        s
        e
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ 
        E
        v
        e
        n
        t
        t
        h
        a
        t
        d
        i
        s
        p
        e
        n
        s
        e
        i
        s
        p
        a
        r
        t
        o
        f
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
        e
        v
        e
        n
        t
        .
        List of `MedicationDispensePerformer` items (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        A
        m
        o
        u
        n
        t
        d
        i
        s
        p
        e
        n
        s
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ 
        W
        h
        o
        c
        o
        l
        l
        e
        c
        t
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
        
        self.statusReasonCodeableConcept = None
        """ 
        W
        h
        y
        a
        d
        i
        s
        p
        e
        n
        s
        e
        w
        a
        s
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.statusReasonReference = None
        """ 
        W
        h
        y
        a
        d
        i
        s
        p
        e
        n
        s
        e
        w
        a
        s
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        W
        h
        o
        t
        h
        e
        d
        i
        s
        p
        e
        n
        s
        e
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.substitution = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        a
        s
        u
        b
        s
        t
        i
        t
        u
        t
        i
        o
        n
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
        t
        h
        e
        d
        i
        s
        p
        e
        n
        s
        e
        .
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
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
        t
        h
        e
        d
        i
        s
        p
        e
        n
        s
        i
        n
        g
        o
        f
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        r
        i
        a
        l
        f
        i
        l
        l
        ,
        p
        a
        r
        t
        i
        a
        l
        f
        i
        l
        l
        ,
        e
        m
        e
        r
        g
        e
        n
        c
        y
        f
        i
        l
        l
        ,
        e
        t
        c
        .
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.whenHandedOver = None
        """ 
        W
        h
        e
        n
        p
        r
        o
        d
        u
        c
        t
        w
        a
        s
        g
        i
        v
        e
        n
        o
        u
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whenPrepared = None
        """ 
        W
        h
        e
        n
        p
        r
        o
        d
        u
        c
        t
        w
        a
        s
        p
        a
        c
        k
        a
        g
        e
        d
        a
        n
        d
        r
        e
        v
        i
        e
        w
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(MedicationDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("daysSupply", "daysSupply", quantity.Quantity, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performer", "performer", MedicationDispensePerformer, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("statusReasonCodeableConcept", "statusReasonCodeableConcept", codeableconcept.CodeableConcept, False, "statusReason", False),
            ("statusReasonReference", "statusReasonReference", fhirreference.FHIRReference, False, "statusReason", False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("whenHandedOver", "whenHandedOver", fhirdate.FHIRDate, False, None, False),
            ("whenPrepared", "whenPrepared", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationDispensePerformer(backboneelement.BackboneElement):
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
    e
    v
    e
    n
    t
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
    e
    v
    e
    n
    t
    .
    
    """
    
    resource_type = "MedicationDispensePerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ 
        I
        n
        d
        i
        v
        i
        d
        u
        a
        l
        w
        h
        o
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
        i
        n
        g
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.function = None
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
        d
        i
        s
        p
        e
        n
        s
        e
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationDispensePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispensePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ 
    W
    h
    e
    t
    h
    e
    r
    a
    s
    u
    b
    s
    t
    i
    t
    u
    t
    i
    o
    n
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
    t
    h
    e
    d
    i
    s
    p
    e
    n
    s
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
    e
    t
    h
    e
    r
    o
    r
    n
    o
    t
    s
    u
    b
    s
    t
    i
    t
    u
    t
    i
    o
    n
    w
    a
    s
    m
    a
    d
    e
    a
    s
    p
    a
    r
    t
    o
    f
    t
    h
    e
    d
    i
    s
    p
    e
    n
    s
    e
    .
    I
    n
    s
    o
    m
    e
    c
    a
    s
    e
    s
    ,
    s
    u
    b
    s
    t
    i
    t
    u
    t
    i
    o
    n
    w
    i
    l
    l
    b
    e
    e
    x
    p
    e
    c
    t
    e
    d
    b
    u
    t
    d
    o
    e
    s
    n
    o
    t
    h
    a
    p
    p
    e
    n
    ,
    i
    n
    o
    t
    h
    e
    r
    c
    a
    s
    e
    s
    s
    u
    b
    s
    t
    i
    t
    u
    t
    i
    o
    n
    i
    s
    n
    o
    t
    e
    x
    p
    e
    c
    t
    e
    d
    b
    u
    t
    d
    o
    e
    s
    h
    a
    p
    p
    e
    n
    .
    T
    h
    i
    s
    b
    l
    o
    c
    k
    e
    x
    p
    l
    a
    i
    n
    s
    w
    h
    a
    t
    s
    u
    b
    s
    t
    i
    t
    u
    t
    i
    o
    n
    d
    i
    d
    o
    r
    d
    i
    d
    n
    o
    t
    h
    a
    p
    p
    e
    n
    a
    n
    d
    w
    h
    y
    .
    I
    f
    n
    o
    t
    h
    i
    n
    g
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
    ,
    s
    u
    b
    s
    t
    i
    t
    u
    t
    i
    o
    n
    w
    a
    s
    n
    o
    t
    d
    o
    n
    e
    .
    
    """
    
    resource_type = "MedicationDispenseSubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reason = None
        """ 
        W
        h
        y
        w
        a
        s
        s
        u
        b
        s
        t
        i
        t
        u
        t
        i
        o
        n
        m
        a
        d
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.responsibleParty = None
        """ 
        W
        h
        o
        i
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
        t
        h
        e
        s
        u
        b
        s
        t
        i
        t
        u
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        o
        d
        e
        s
        i
        g
        n
        i
        f
        y
        i
        n
        g
        w
        h
        e
        t
        h
        e
        r
        a
        d
        i
        f
        f
        e
        r
        e
        n
        t
        d
        r
        u
        g
        w
        a
        s
        d
        i
        s
        p
        e
        n
        s
        e
        d
        f
        r
        o
        m
        w
        h
        a
        t
        w
        a
        s
        p
        r
        e
        s
        c
        r
        i
        b
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.wasSubstituted = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        a
        s
        u
        b
        s
        t
        i
        t
        u
        t
        i
        o
        n
        w
        a
        s
        o
        r
        w
        a
        s
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
        o
        n
        t
        h
        e
        d
        i
        s
        p
        e
        n
        s
        e
        .
        Type `bool`. """
        
        super(MedicationDispenseSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("wasSubstituted", "wasSubstituted", bool, False, None, True),
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
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
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
