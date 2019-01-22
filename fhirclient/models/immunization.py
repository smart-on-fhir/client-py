#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Immunization) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Immunization(domainresource.DomainResource):
    """ 
    I
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
    e
    v
    e
    n
    t
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
    v
    a
    c
    c
    i
    n
    e
    o
    r
    a
    r
    e
    c
    o
    r
    d
    o
    f
    a
    n
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
    a
    s
    r
    e
    p
    o
    r
    t
    e
    d
    b
    y
    a
    p
    a
    t
    i
    e
    n
    t
    ,
    a
    c
    l
    i
    n
    i
    c
    i
    a
    n
    o
    r
    a
    n
    o
    t
    h
    e
    r
    p
    a
    r
    t
    y
    .
    
    """
    
    resource_type = "Immunization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.doseQuantity = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
        v
        a
        c
        c
        i
        n
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
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.education = None
        """ 
        E
        d
        u
        c
        a
        t
        i
        o
        n
        a
        l
        m
        a
        t
        e
        r
        i
        a
        l
        p
        r
        e
        s
        e
        n
        t
        e
        d
        t
        o
        p
        a
        t
        i
        e
        n
        t
        .
        List of `ImmunizationEducation` items (represented as `dict` in JSON). """
        
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
        w
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
        
        self.expirationDate = None
        """ 
        V
        a
        c
        c
        i
        n
        e
        e
        x
        p
        i
        r
        a
        t
        i
        o
        n
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fundingSource = None
        """ 
        F
        u
        n
        d
        i
        n
        g
        s
        o
        u
        r
        c
        e
        f
        o
        r
        t
        h
        e
        v
        a
        c
        c
        i
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        
        self.isSubpotent = None
        """ 
        D
        o
        s
        e
        p
        o
        t
        e
        n
        c
        y
        .
        Type `bool`. """
        
        self.location = None
        """ 
        W
        h
        e
        r
        e
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
        
        self.lotNumber = None
        """ 
        V
        a
        c
        c
        i
        n
        e
        l
        o
        t
        n
        u
        m
        b
        e
        r
        .
        Type `str`. """
        
        self.manufacturer = None
        """ 
        V
        a
        c
        c
        i
        n
        e
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        r
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
        n
        o
        t
        e
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ 
        V
        a
        c
        c
        i
        n
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
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrenceString = None
        """ 
        V
        a
        c
        c
        i
        n
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
        d
        a
        t
        e
        .
        Type `str`. """
        
        self.patient = None
        """ 
        W
        h
        o
        w
        a
        s
        i
        m
        m
        u
        n
        i
        z
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        List of `ImmunizationPerformer` items (represented as `dict` in JSON). """
        
        self.primarySource = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        c
        o
        n
        t
        e
        x
        t
        t
        h
        e
        d
        a
        t
        a
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
        i
        n
        .
        Type `bool`. """
        
        self.programEligibility = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        e
        l
        i
        g
        i
        b
        i
        l
        i
        t
        y
        f
        o
        r
        a
        v
        a
        c
        c
        i
        n
        a
        t
        i
        o
        n
        p
        r
        o
        g
        r
        a
        m
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.protocolApplied = None
        """ 
        P
        r
        o
        t
        o
        c
        o
        l
        f
        o
        l
        l
        o
        w
        e
        d
        b
        y
        t
        h
        e
        p
        r
        o
        v
        i
        d
        e
        r
        .
        List of `ImmunizationProtocolApplied` items (represented as `dict` in JSON). """
        
        self.reaction = None
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
        a
        r
        e
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
        f
        o
        l
        l
        o
        w
        s
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
        .
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
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
        o
        c
        c
        u
        r
        r
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
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
        o
        c
        c
        u
        r
        r
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.recorded = None
        """ 
        W
        h
        e
        n
        t
        h
        e
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
        w
        a
        s
        f
        i
        r
        s
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
        '
        s
        r
        e
        c
        o
        r
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reportOrigin = None
        """ 
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
        o
        u
        r
        c
        e
        o
        f
        a
        s
        e
        c
        o
        n
        d
        a
        r
        i
        l
        y
        r
        e
        p
        o
        r
        t
        e
        d
        r
        e
        c
        o
        r
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.route = None
        """ 
        H
        o
        w
        v
        a
        c
        c
        i
        n
        e
        e
        n
        t
        e
        r
        e
        d
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
        v
        a
        c
        c
        i
        n
        e
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
        
        self.status = None
        """ 
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
        n
        o
        t
        -
        d
        o
        n
        e
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
        n
        o
        t
        d
        o
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subpotentReason = None
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
        b
        e
        i
        n
        g
        s
        u
        b
        p
        o
        t
        e
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        """ 
        V
        a
        c
        c
        i
        n
        e
        p
        r
        o
        d
        u
        c
        t
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
        
        super(Immunization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, None, False),
            ("education", "education", ImmunizationEducation, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("fundingSource", "fundingSource", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("isSubpotent", "isSubpotent", bool, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", True),
            ("occurrenceString", "occurrenceString", str, False, "occurrence", True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("performer", "performer", ImmunizationPerformer, True, None, False),
            ("primarySource", "primarySource", bool, False, None, False),
            ("programEligibility", "programEligibility", codeableconcept.CodeableConcept, True, None, False),
            ("protocolApplied", "protocolApplied", ImmunizationProtocolApplied, True, None, False),
            ("reaction", "reaction", ImmunizationReaction, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False, None, False),
            ("reportOrigin", "reportOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subpotentReason", "subpotentReason", codeableconcept.CodeableConcept, True, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationEducation(backboneelement.BackboneElement):
    """ 
    E
    d
    u
    c
    a
    t
    i
    o
    n
    a
    l
    m
    a
    t
    e
    r
    i
    a
    l
    p
    r
    e
    s
    e
    n
    t
    e
    d
    t
    o
    p
    a
    t
    i
    e
    n
    t
    .
    
    
    E
    d
    u
    c
    a
    t
    i
    o
    n
    a
    l
    m
    a
    t
    e
    r
    i
    a
    l
    p
    r
    e
    s
    e
    n
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
    (
    o
    r
    g
    u
    a
    r
    d
    i
    a
    n
    )
    a
    t
    t
    h
    e
    t
    i
    m
    e
    o
    f
    v
    a
    c
    c
    i
    n
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
    
    """
    
    resource_type = "ImmunizationEducation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentType = None
        """ 
        E
        d
        u
        c
        a
        t
        i
        o
        n
        a
        l
        m
        a
        t
        e
        r
        i
        a
        l
        d
        o
        c
        u
        m
        e
        n
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
        .
        Type `str`. """
        
        self.presentationDate = None
        """ 
        E
        d
        u
        c
        a
        t
        i
        o
        n
        a
        l
        m
        a
        t
        e
        r
        i
        a
        l
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publicationDate = None
        """ 
        E
        d
        u
        c
        a
        t
        i
        o
        n
        a
        l
        m
        a
        t
        e
        r
        i
        a
        l
        p
        u
        b
        l
        i
        c
        a
        t
        i
        o
        n
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reference = None
        """ 
        E
        d
        u
        c
        a
        t
        i
        o
        n
        a
        l
        m
        a
        t
        e
        r
        i
        a
        l
        r
        e
        f
        e
        r
        e
        n
        c
        e
        p
        o
        i
        n
        t
        e
        r
        .
        Type `str`. """
        
        super(ImmunizationEducation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationEducation, self).elementProperties()
        js.extend([
            ("documentType", "documentType", str, False, None, False),
            ("presentationDate", "presentationDate", fhirdate.FHIRDate, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js


class ImmunizationPerformer(backboneelement.BackboneElement):
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
    e
    v
    e
    n
    t
    .
    
    """
    
    resource_type = "ImmunizationPerformer"
    
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
        a
        t
        t
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
        w
        a
        s
        d
        o
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ImmunizationProtocolApplied(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    t
    o
    c
    o
    l
    f
    o
    l
    l
    o
    w
    e
    d
    b
    y
    t
    h
    e
    p
    r
    o
    v
    i
    d
    e
    r
    .
    
    
    T
    h
    e
    p
    r
    o
    t
    o
    c
    o
    l
    (
    s
    e
    t
    o
    f
    r
    e
    c
    o
    m
    m
    e
    n
    d
    a
    t
    i
    o
    n
    s
    )
    b
    e
    i
    n
    g
    f
    o
    l
    l
    o
    w
    e
    d
    b
    y
    t
    h
    e
    p
    r
    o
    v
    i
    d
    e
    r
    w
    h
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
    e
    d
    t
    h
    e
    d
    o
    s
    e
    .
    
    """
    
    resource_type = "ImmunizationProtocolApplied"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
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
        p
        u
        b
        l
        i
        s
        h
        i
        n
        g
        t
        h
        e
        r
        e
        c
        o
        m
        m
        e
        n
        d
        a
        t
        i
        o
        n
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.doseNumberPositiveInt = None
        """ 
        D
        o
        s
        e
        n
        u
        m
        b
        e
        r
        w
        i
        t
        h
        i
        n
        s
        e
        r
        i
        e
        s
        .
        Type `int`. """
        
        self.doseNumberString = None
        """ 
        D
        o
        s
        e
        n
        u
        m
        b
        e
        r
        w
        i
        t
        h
        i
        n
        s
        e
        r
        i
        e
        s
        .
        Type `str`. """
        
        self.series = None
        """ 
        N
        a
        m
        e
        o
        f
        v
        a
        c
        c
        i
        n
        e
        s
        e
        r
        i
        e
        s
        .
        Type `str`. """
        
        self.seriesDosesPositiveInt = None
        """ 
        R
        e
        c
        o
        m
        m
        e
        n
        d
        e
        d
        n
        u
        m
        b
        e
        r
        o
        f
        d
        o
        s
        e
        s
        f
        o
        r
        i
        m
        m
        u
        n
        i
        t
        y
        .
        Type `int`. """
        
        self.seriesDosesString = None
        """ 
        R
        e
        c
        o
        m
        m
        e
        n
        d
        e
        d
        n
        u
        m
        b
        e
        r
        o
        f
        d
        o
        s
        e
        s
        f
        o
        r
        i
        m
        m
        u
        n
        i
        t
        y
        .
        Type `str`. """
        
        self.targetDisease = None
        """ 
        V
        a
        c
        c
        i
        n
        e
        p
        r
        e
        v
        e
        n
        t
        a
        t
        a
        b
        l
        e
        d
        i
        s
        e
        a
        s
        e
        b
        e
        i
        n
        g
        t
        a
        r
        g
        e
        t
        t
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationProtocolApplied, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationProtocolApplied, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("doseNumberPositiveInt", "doseNumberPositiveInt", int, False, "doseNumber", True),
            ("doseNumberString", "doseNumberString", str, False, "doseNumber", True),
            ("series", "series", str, False, None, False),
            ("seriesDosesPositiveInt", "seriesDosesPositiveInt", int, False, "seriesDoses", False),
            ("seriesDosesString", "seriesDosesString", str, False, "seriesDoses", False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class ImmunizationReaction(backboneelement.BackboneElement):
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
    a
    r
    e
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
    f
    o
    l
    l
    o
    w
    s
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
    .
    
    
    C
    a
    t
    e
    g
    o
    r
    i
    c
    a
    l
    d
    a
    t
    a
    i
    n
    d
    i
    c
    a
    t
    i
    n
    g
    t
    h
    a
    t
    a
    n
    a
    d
    v
    e
    r
    s
    e
    e
    v
    e
    n
    t
    i
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
    i
    n
    t
    i
    m
    e
    t
    o
    a
    n
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
    .
    
    """
    
    resource_type = "ImmunizationReaction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ 
        W
        h
        e
        n
        r
        e
        a
        c
        t
        i
        o
        n
        s
        t
        a
        r
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
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
        o
        n
        r
        e
        a
        c
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.reported = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        s
        e
        l
        f
        -
        r
        e
        p
        o
        r
        t
        e
        d
        r
        e
        a
        c
        t
        i
        o
        n
        .
        Type `bool`. """
        
        super(ImmunizationReaction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, False, None, False),
            ("reported", "reported", bool, False, None, False),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
