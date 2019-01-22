#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ActivityDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ActivityDefinition(domainresource.DomainResource):
    """ 
    T
    h
    e
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
    o
    f
    a
    s
    p
    e
    c
    i
    f
    i
    c
    a
    c
    t
    i
    v
    i
    t
    y
    t
    o
    b
    e
    t
    a
    k
    e
    n
    ,
    i
    n
    d
    e
    p
    e
    n
    d
    e
    n
    t
    o
    f
    a
    n
    y
    p
    a
    r
    t
    i
    c
    u
    l
    a
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
    c
    o
    n
    t
    e
    x
    t
    .
    
    
    T
    h
    i
    s
    r
    e
    s
    o
    u
    r
    c
    e
    a
    l
    l
    o
    w
    s
    f
    o
    r
    t
    h
    e
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
    o
    f
    s
    o
    m
    e
    a
    c
    t
    i
    v
    i
    t
    y
    t
    o
    b
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
    ,
    i
    n
    d
    e
    p
    e
    n
    d
    e
    n
    t
    o
    f
    a
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    p
    a
    t
    i
    e
    n
    t
    ,
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
    ,
    o
    r
    o
    t
    h
    e
    r
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
    c
    o
    n
    t
    e
    x
    t
    .
    
    """
    
    resource_type = "ActivityDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        w
        a
        s
        a
        p
        p
        r
        o
        v
        e
        d
        b
        y
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.author = None
        """ 
        W
        h
        o
        a
        u
        t
        h
        o
        r
        e
        d
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ 
        W
        h
        a
        t
        p
        a
        r
        t
        o
        f
        b
        o
        d
        y
        t
        o
        p
        e
        r
        f
        o
        r
        m
        o
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        D
        e
        t
        a
        i
        l
        t
        y
        p
        e
        o
        f
        a
        c
        t
        i
        v
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ 
        C
        o
        n
        t
        a
        c
        t
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
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ 
        U
        s
        e
        a
        n
        d
        /
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
        .
        Type `str`. """
        
        self.date = None
        """ 
        D
        a
        t
        e
        l
        a
        s
        t
        c
        h
        a
        n
        g
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
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
        a
        c
        t
        i
        v
        i
        t
        y
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
        Type `str`. """
        
        self.doNotPerform = None
        """ 
        T
        r
        u
        e
        i
        f
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
        s
        h
        o
        u
        l
        d
        n
        o
        t
        b
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
        Type `bool`. """
        
        self.dosage = None
        """ 
        D
        e
        t
        a
        i
        l
        e
        d
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
        .
        List of `Dosage` items (represented as `dict` in JSON). """
        
        self.dynamicValue = None
        """ 
        D
        y
        n
        a
        m
        i
        c
        a
        s
        p
        e
        c
        t
        s
        o
        f
        t
        h
        e
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
        List of `ActivityDefinitionDynamicValue` items (represented as `dict` in JSON). """
        
        self.editor = None
        """ 
        W
        h
        o
        e
        d
        i
        t
        e
        d
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.effectivePeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        i
        s
        e
        x
        p
        e
        c
        t
        e
        d
        t
        o
        b
        e
        u
        s
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.endorser = None
        """ 
        W
        h
        o
        e
        n
        d
        o
        r
        s
        e
        d
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.experimental = None
        """ 
        F
        o
        r
        t
        e
        s
        t
        i
        n
        g
        p
        u
        r
        p
        o
        s
        e
        s
        ,
        n
        o
        t
        r
        e
        a
        l
        u
        s
        a
        g
        e
        .
        Type `bool`. """
        
        self.identifier = None
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
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        List of `Identifier` items (represented as `dict` in JSON). """
        
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
        .
        Type `str`. """
        
        self.jurisdiction = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        j
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        f
        o
        r
        a
        c
        t
        i
        v
        i
        t
        y
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
        (
        i
        f
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kind = None
        """ 
        K
        i
        n
        d
        o
        f
        r
        e
        s
        o
        u
        r
        c
        e
        .
        Type `str`. """
        
        self.lastReviewDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        w
        a
        s
        l
        a
        s
        t
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
        
        self.library = None
        """ 
        L
        o
        g
        i
        c
        u
        s
        e
        d
        b
        y
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        i
        t
        s
        h
        o
        u
        l
        d
        h
        a
        p
        p
        e
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        a
        c
        t
        i
        v
        i
        t
        y
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
        (
        c
        o
        m
        p
        u
        t
        e
        r
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.observationRequirement = None
        """ 
        W
        h
        a
        t
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
        s
        a
        r
        e
        r
        e
        q
        u
        i
        r
        e
        d
        t
        o
        p
        e
        r
        f
        o
        r
        m
        t
        h
        i
        s
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.observationResultRequirement = None
        """ 
        W
        h
        a
        t
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
        s
        m
        u
        s
        t
        b
        e
        p
        r
        o
        d
        u
        c
        e
        d
        b
        y
        t
        h
        i
        s
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ 
        W
        h
        o
        s
        h
        o
        u
        l
        d
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
        List of `ActivityDefinitionParticipant` items (represented as `dict` in JSON). """
        
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
        
        self.productCodeableConcept = None
        """ 
        W
        h
        a
        t
        '
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
        /
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
        
        self.productReference = None
        """ 
        W
        h
        a
        t
        '
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
        /
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
        
        self.profile = None
        """ 
        W
        h
        a
        t
        p
        r
        o
        f
        i
        l
        e
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
        n
        e
        e
        d
        s
        t
        o
        c
        o
        n
        f
        o
        r
        m
        t
        o
        .
        Type `str`. """
        
        self.publisher = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        (
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
        o
        r
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
        )
        .
        Type `str`. """
        
        self.purpose = None
        """ 
        W
        h
        y
        t
        h
        i
        s
        a
        c
        t
        i
        v
        i
        t
        y
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
        i
        s
        d
        e
        f
        i
        n
        e
        d
        .
        Type `str`. """
        
        self.quantity = None
        """ 
        H
        o
        w
        m
        u
        c
        h
        i
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
        /
        c
        o
        n
        s
        u
        m
        e
        d
        /
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.relatedArtifact = None
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
        o
        c
        u
        m
        e
        n
        t
        a
        t
        i
        o
        n
        ,
        c
        i
        t
        a
        t
        i
        o
        n
        s
        ,
        e
        t
        c
        .
        .
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.reviewer = None
        """ 
        W
        h
        o
        r
        e
        v
        i
        e
        w
        e
        d
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.specimenRequirement = None
        """ 
        W
        h
        a
        t
        s
        p
        e
        c
        i
        m
        e
        n
        s
        a
        r
        e
        r
        e
        q
        u
        i
        r
        e
        d
        t
        o
        p
        e
        r
        f
        o
        r
        m
        t
        h
        i
        s
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        a
        c
        t
        i
        v
        e
        |
        r
        e
        t
        i
        r
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
        
        self.subjectCodeableConcept = None
        """ 
        T
        y
        p
        e
        o
        f
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
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ 
        T
        y
        p
        e
        o
        f
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
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        
        self.subtitle = None
        """ 
        S
        u
        b
        o
        r
        d
        i
        n
        a
        t
        e
        t
        i
        t
        l
        e
        o
        f
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        Type `str`. """
        
        self.timingAge = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        v
        i
        t
        y
        i
        s
        t
        o
        o
        c
        c
        u
        r
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        v
        i
        t
        y
        i
        s
        t
        o
        o
        c
        c
        u
        r
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDuration = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        v
        i
        t
        y
        i
        s
        t
        o
        o
        c
        c
        u
        r
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        v
        i
        t
        y
        i
        s
        t
        o
        o
        c
        c
        u
        r
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingRange = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        v
        i
        t
        y
        i
        s
        t
        o
        o
        c
        c
        u
        r
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        v
        i
        t
        y
        i
        s
        t
        o
        o
        c
        c
        u
        r
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        a
        c
        t
        i
        v
        i
        t
        y
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
        (
        h
        u
        m
        a
        n
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.topic = None
        """ 
        E
        .
        g
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
        ,
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
        A
        s
        s
        e
        s
        s
        m
        e
        n
        t
        ,
        e
        t
        c
        .
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.transform = None
        """ 
        T
        r
        a
        n
        s
        f
        o
        r
        m
        t
        o
        a
        p
        p
        l
        y
        t
        h
        e
        t
        e
        m
        p
        l
        a
        t
        e
        .
        Type `str`. """
        
        self.url = None
        """ 
        C
        a
        n
        o
        n
        i
        c
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
        f
        o
        r
        t
        h
        i
        s
        a
        c
        t
        i
        v
        i
        t
        y
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
        ,
        r
        e
        p
        r
        e
        s
        e
        n
        t
        e
        d
        a
        s
        a
        U
        R
        I
        (
        g
        l
        o
        b
        a
        l
        l
        y
        u
        n
        i
        q
        u
        e
        )
        .
        Type `str`. """
        
        self.usage = None
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
        c
        l
        i
        n
        i
        c
        a
        l
        u
        s
        a
        g
        e
        o
        f
        t
        h
        e
        a
        c
        t
        i
        v
        i
        t
        y
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
        Type `str`. """
        
        self.useContext = None
        """ 
        T
        h
        e
        c
        o
        n
        t
        e
        x
        t
        t
        h
        a
        t
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
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
        t
        o
        s
        u
        p
        p
        o
        r
        t
        .
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
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
        a
        c
        t
        i
        v
        i
        t
        y
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
        Type `str`. """
        
        super(ActivityDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("dosage", "dosage", dosage.Dosage, True, None, False),
            ("dynamicValue", "dynamicValue", ActivityDefinitionDynamicValue, True, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("intent", "intent", str, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("name", "name", str, False, None, False),
            ("observationRequirement", "observationRequirement", fhirreference.FHIRReference, True, None, False),
            ("observationResultRequirement", "observationResultRequirement", fhirreference.FHIRReference, True, None, False),
            ("participant", "participant", ActivityDefinitionParticipant, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("profile", "profile", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("specimenRequirement", "specimenRequirement", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """ 
    D
    y
    n
    a
    m
    i
    c
    a
    s
    p
    e
    c
    t
    s
    o
    f
    t
    h
    e
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
    
    
    D
    y
    n
    a
    m
    i
    c
    v
    a
    l
    u
    e
    s
    t
    h
    a
    t
    w
    i
    l
    l
    b
    e
    e
    v
    a
    l
    u
    a
    t
    e
    d
    t
    o
    p
    r
    o
    d
    u
    c
    e
    v
    a
    l
    u
    e
    s
    f
    o
    r
    e
    l
    e
    m
    e
    n
    t
    s
    o
    f
    t
    h
    e
    r
    e
    s
    u
    l
    t
    i
    n
    g
    r
    e
    s
    o
    u
    r
    c
    e
    .
    F
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
    i
    f
    t
    h
    e
    d
    o
    s
    a
    g
    e
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
    m
    u
    s
    t
    b
    e
    c
    o
    m
    p
    u
    t
    e
    d
    b
    a
    s
    e
    d
    o
    n
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
    '
    s
    w
    e
    i
    g
    h
    t
    ,
    a
    d
    y
    n
    a
    m
    i
    c
    v
    a
    l
    u
    e
    w
    o
    u
    l
    d
    b
    e
    u
    s
    e
    d
    t
    o
    s
    p
    e
    c
    i
    f
    y
    a
    n
    e
    x
    p
    r
    e
    s
    s
    i
    o
    n
    t
    h
    a
    t
    c
    a
    l
    c
    u
    l
    a
    t
    e
    d
    t
    h
    e
    w
    e
    i
    g
    h
    t
    ,
    a
    n
    d
    t
    h
    e
    p
    a
    t
    h
    o
    n
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
    r
    e
    s
    o
    u
    r
    c
    e
    t
    h
    a
    t
    w
    o
    u
    l
    d
    c
    o
    n
    t
    a
    i
    n
    t
    h
    e
    r
    e
    s
    u
    l
    t
    .
    
    """
    
    resource_type = "ActivityDefinitionDynamicValue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ 
        A
        n
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        t
        h
        a
        t
        p
        r
        o
        v
        i
        d
        e
        s
        t
        h
        e
        d
        y
        n
        a
        m
        i
        c
        v
        a
        l
        u
        e
        f
        o
        r
        t
        h
        e
        c
        u
        s
        t
        o
        m
        i
        z
        a
        t
        i
        o
        n
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.path = None
        """ 
        T
        h
        e
        p
        a
        t
        h
        t
        o
        t
        h
        e
        e
        l
        e
        m
        e
        n
        t
        t
        o
        b
        e
        s
        e
        t
        d
        y
        n
        a
        m
        i
        c
        a
        l
        l
        y
        .
        Type `str`. """
        
        super(ActivityDefinitionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """ 
    W
    h
    o
    s
    h
    o
    u
    l
    d
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
    s
    h
    o
    u
    l
    d
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
    t
    h
    e
    a
    c
    t
    i
    o
    n
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
    
    """
    
    resource_type = "ActivityDefinitionParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ 
        E
        .
        g
        .
        N
        u
        r
        s
        e
        ,
        S
        u
        r
        g
        e
        o
        n
        ,
        P
        a
        r
        e
        n
        t
        ,
        e
        t
        c
        .
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        p
        a
        t
        i
        e
        n
        t
        |
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
        |
        r
        e
        l
        a
        t
        e
        d
        -
        p
        e
        r
        s
        o
        n
        |
        d
        e
        v
        i
        c
        e
        .
        Type `str`. """
        
        super(ActivityDefinitionParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinitionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
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
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
