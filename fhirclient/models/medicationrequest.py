#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationRequest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicationRequest(domainresource.DomainResource):
    """ 
    O
    r
    d
    e
    r
    i
    n
    g
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
    o
    r
    g
    r
    o
    u
    p
    .
    
    
    A
    n
    o
    r
    d
    e
    r
    o
    r
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
    b
    o
    t
    h
    s
    u
    p
    p
    l
    y
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
    r
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
    T
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
    s
    c
    a
    l
    l
    e
    d
    "
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
    R
    e
    q
    u
    e
    s
    t
    "
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
    "
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
    P
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
    "
    o
    r
    "
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
    O
    r
    d
    e
    r
    "
    t
    o
    g
    e
    n
    e
    r
    a
    l
    i
    z
    e
    t
    h
    e
    u
    s
    e
    a
    c
    r
    o
    s
    s
    i
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
    s
    e
    t
    t
    i
    n
    g
    s
    ,
    i
    n
    c
    l
    u
    d
    i
    n
    g
    c
    a
    r
    e
    p
    l
    a
    n
    s
    ,
    e
    t
    c
    .
    ,
    a
    n
    d
    t
    o
    h
    a
    r
    m
    o
    n
    i
    z
    e
    w
    i
    t
    h
    w
    o
    r
    k
    f
    l
    o
    w
    p
    a
    t
    t
    e
    r
    n
    s
    .
    
    """
    
    resource_type = "MedicationRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ 
        W
        h
        e
        n
        r
        e
        q
        u
        e
        s
        t
        w
        a
        s
        i
        n
        i
        t
        i
        a
        l
        l
        y
        a
        u
        t
        h
        o
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ 
        W
        h
        a
        t
        r
        e
        q
        u
        e
        s
        t
        f
        u
        l
        f
        i
        l
        l
        s
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
        u
        s
        a
        g
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.courseOfTherapyType = None
        """ 
        O
        v
        e
        r
        a
        l
        l
        p
        a
        t
        t
        e
        r
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        I
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
        
        self.dispenseRequest = None
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
        s
        u
        p
        p
        l
        y
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        Type `MedicationRequestDispenseRequest` (represented as `dict` in JSON). """
        
        self.doNotPerform = None
        """ 
        T
        r
        u
        e
        i
        f
        r
        e
        q
        u
        e
        s
        t
        i
        s
        p
        r
        o
        h
        i
        b
        i
        t
        i
        n
        g
        a
        c
        t
        i
        o
        n
        .
        Type `bool`. """
        
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
        s
        h
        o
        u
        l
        d
        b
        e
        t
        a
        k
        e
        n
        .
        List of `Dosage` items (represented as `dict` in JSON). """
        
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
        e
        n
        c
        o
        u
        n
        t
        e
        r
        /
        a
        d
        m
        i
        s
        s
        i
        o
        n
        /
        s
        t
        a
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.groupIdentifier = None
        """ 
        C
        o
        m
        p
        o
        s
        i
        t
        e
        r
        e
        q
        u
        e
        s
        t
        t
        h
        i
        s
        i
        s
        p
        a
        r
        t
        o
        f
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
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
        r
        e
        q
        u
        e
        s
        t
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
        
        self.insurance = None
        """ 
        A
        s
        s
        o
        c
        i
        a
        t
        e
        d
        i
        n
        s
        u
        r
        a
        n
        c
        e
        c
        o
        v
        e
        r
        a
        g
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent = None
        """ 
        p
        r
        o
        p
        o
        s
        a
        l
        |
        p
        l
        a
        n
        |
        o
        r
        d
        e
        r
        |
        o
        r
        i
        g
        i
        n
        a
        l
        -
        o
        r
        d
        e
        r
        |
        i
        n
        s
        t
        a
        n
        c
        e
        -
        o
        r
        d
        e
        r
        |
        o
        p
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.medicationCodeableConcept = None
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
        t
        o
        b
        e
        t
        a
        k
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
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
        t
        o
        b
        e
        t
        a
        k
        e
        n
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
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        p
        e
        r
        f
        o
        r
        m
        e
        r
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ 
        D
        e
        s
        i
        r
        e
        d
        k
        i
        n
        d
        o
        f
        p
        e
        r
        f
        o
        r
        m
        e
        r
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.priorPrescription = None
        """ 
        A
        n
        o
        r
        d
        e
        r
        /
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
        r
        e
        p
        l
        a
        c
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priority = None
        """ 
        r
        o
        u
        t
        i
        n
        e
        |
        u
        r
        g
        e
        n
        t
        |
        a
        s
        a
        p
        |
        s
        t
        a
        t
        .
        Type `str`. """
        
        self.reasonCode = None
        """ 
        R
        e
        a
        s
        o
        n
        o
        r
        i
        n
        d
        i
        c
        a
        t
        i
        o
        n
        f
        o
        r
        o
        r
        d
        e
        r
        i
        n
        g
        o
        r
        n
        o
        t
        o
        r
        d
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
        i
        s
        b
        e
        i
        n
        g
        w
        r
        i
        t
        t
        e
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recorder = None
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
        e
        n
        t
        e
        r
        e
        d
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reportedBoolean = None
        """ 
        R
        e
        p
        o
        r
        t
        e
        d
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
        p
        r
        i
        m
        a
        r
        y
        r
        e
        c
        o
        r
        d
        .
        Type `bool`. """
        
        self.reportedReference = None
        """ 
        R
        e
        p
        o
        r
        t
        e
        d
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
        p
        r
        i
        m
        a
        r
        y
        r
        e
        c
        o
        r
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requester = None
        """ 
        W
        h
        o
        /
        W
        h
        a
        t
        r
        e
        q
        u
        e
        s
        t
        e
        d
        t
        h
        e
        R
        e
        q
        u
        e
        s
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
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
        a
        n
        c
        e
        l
        l
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
        s
        t
        o
        p
        p
        e
        d
        |
        d
        r
        a
        f
        t
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
        o
        r
        g
        r
        o
        u
        p
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
        r
        e
        q
        u
        e
        s
        t
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.substitution = None
        """ 
        A
        n
        y
        r
        e
        s
        t
        r
        i
        c
        t
        i
        o
        n
        s
        o
        n
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
        Type `MedicationRequestSubstitution` (represented as `dict` in JSON). """
        
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
        o
        s
        u
        p
        p
        o
        r
        t
        o
        r
        d
        e
        r
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
        
        super(MedicationRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("courseOfTherapyType", "courseOfTherapyType", codeableconcept.CodeableConcept, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("dispenseRequest", "dispenseRequest", MedicationRequestDispenseRequest, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("priorPrescription", "priorPrescription", fhirreference.FHIRReference, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("reportedBoolean", "reportedBoolean", bool, False, "reported", False),
            ("reportedReference", "reportedReference", fhirreference.FHIRReference, False, "reported", False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("substitution", "substitution", MedicationRequestSubstitution, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
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
    s
    u
    p
    p
    l
    y
    a
    u
    t
    h
    o
    r
    i
    z
    a
    t
    i
    o
    n
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
    e
    s
    p
    e
    c
    i
    f
    i
    c
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
    d
    i
    s
    p
    e
    n
    s
    e
    o
    r
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
    s
    u
    p
    p
    l
    y
    p
    a
    r
    t
    o
    f
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
    r
    e
    q
    u
    e
    s
    t
    (
    a
    l
    s
    o
    k
    n
    o
    w
    n
    a
    s
    a
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
    P
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
    o
    r
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
    O
    r
    d
    e
    r
    )
    .
    N
    o
    t
    e
    t
    h
    a
    t
    t
    h
    i
    s
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
    i
    s
    n
    o
    t
    a
    l
    w
    a
    y
    s
    s
    e
    n
    t
    w
    i
    t
    h
    t
    h
    e
    o
    r
    d
    e
    r
    .
    T
    h
    e
    r
    e
    m
    a
    y
    b
    e
    i
    n
    s
    o
    m
    e
    s
    e
    t
    t
    i
    n
    g
    s
    (
    e
    .
    g
    .
    h
    o
    s
    p
    i
    t
    a
    l
    s
    )
    i
    n
    s
    t
    i
    t
    u
    t
    i
    o
    n
    a
    l
    o
    r
    s
    y
    s
    t
    e
    m
    s
    u
    p
    p
    o
    r
    t
    f
    o
    r
    c
    o
    m
    p
    l
    e
    t
    i
    n
    g
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
    d
    e
    t
    a
    i
    l
    s
    i
    n
    t
    h
    e
    p
    h
    a
    r
    m
    a
    c
    y
    d
    e
    p
    a
    r
    t
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "MedicationRequestDispenseRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dispenseInterval = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        p
        e
        r
        i
        o
        d
        o
        f
        t
        i
        m
        e
        b
        e
        t
        w
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
        s
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.expectedSupplyDuration = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        d
        a
        y
        s
        s
        u
        p
        p
        l
        y
        p
        e
        r
        d
        i
        s
        p
        e
        n
        s
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.initialFill = None
        """ 
        F
        i
        r
        s
        t
        f
        i
        l
        l
        d
        e
        t
        a
        i
        l
        s
        .
        Type `MedicationRequestDispenseRequestInitialFill` (represented as `dict` in JSON). """
        
        self.numberOfRepeatsAllowed = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        r
        e
        f
        i
        l
        l
        s
        a
        u
        t
        h
        o
        r
        i
        z
        e
        d
        .
        Type `int`. """
        
        self.performer = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        d
        i
        s
        p
        e
        n
        s
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.quantity = None
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
        t
        o
        s
        u
        p
        p
        l
        y
        p
        e
        r
        d
        i
        s
        p
        e
        n
        s
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ 
        T
        i
        m
        e
        p
        e
        r
        i
        o
        d
        s
        u
        p
        p
        l
        y
        i
        s
        a
        u
        t
        h
        o
        r
        i
        z
        e
        d
        f
        o
        r
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationRequestDispenseRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestDispenseRequest, self).elementProperties()
        js.extend([
            ("dispenseInterval", "dispenseInterval", duration.Duration, False, None, False),
            ("expectedSupplyDuration", "expectedSupplyDuration", duration.Duration, False, None, False),
            ("initialFill", "initialFill", MedicationRequestDispenseRequestInitialFill, False, None, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


class MedicationRequestDispenseRequestInitialFill(backboneelement.BackboneElement):
    """ 
    F
    i
    r
    s
    t
    f
    i
    l
    l
    d
    e
    t
    a
    i
    l
    s
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
    e
    q
    u
    a
    n
    t
    i
    t
    y
    o
    r
    d
    u
    r
    a
    t
    i
    o
    n
    f
    o
    r
    t
    h
    e
    f
    i
    r
    s
    t
    d
    i
    s
    p
    e
    n
    s
    e
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
    
    """
    
    resource_type = "MedicationRequestDispenseRequestInitialFill"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.duration = None
        """ 
        F
        i
        r
        s
        t
        f
        i
        l
        l
        d
        u
        r
        a
        t
        i
        o
        n
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        F
        i
        r
        s
        t
        f
        i
        l
        l
        q
        u
        a
        n
        t
        i
        t
        y
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(MedicationRequestDispenseRequestInitialFill, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestDispenseRequestInitialFill, self).elementProperties()
        js.extend([
            ("duration", "duration", duration.Duration, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """ 
    A
    n
    y
    r
    e
    s
    t
    r
    i
    c
    t
    i
    o
    n
    s
    o
    n
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
    c
    a
    n
    o
    r
    s
    h
    o
    u
    l
    d
    b
    e
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
    m
    u
    s
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
    m
    u
    s
    t
    n
    o
    t
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
    t
    h
    e
    p
    r
    e
    s
    c
    r
    i
    b
    e
    r
    '
    s
    i
    n
    t
    e
    n
    t
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
    y
    b
    e
    d
    o
    n
    e
    .
    
    """
    
    resource_type = "MedicationRequestSubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedBoolean = None
        """ 
        W
        h
        e
        t
        h
        e
        r
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
        a
        l
        l
        o
        w
        e
        d
        o
        r
        n
        o
        t
        .
        Type `bool`. """
        
        self.allowedCodeableConcept = None
        """ 
        W
        h
        e
        t
        h
        e
        r
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
        a
        l
        l
        o
        w
        e
        d
        o
        r
        n
        o
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ 
        W
        h
        y
        s
        h
        o
        u
        l
        d
        (
        n
        o
        t
        )
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
        b
        e
        m
        a
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationRequestSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestSubstitution, self).elementProperties()
        js.extend([
            ("allowedBoolean", "allowedBoolean", bool, False, "allowed", True),
            ("allowedCodeableConcept", "allowedCodeableConcept", codeableconcept.CodeableConcept, False, "allowed", True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
