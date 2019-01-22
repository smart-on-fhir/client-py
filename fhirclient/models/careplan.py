#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CarePlan(domainresource.DomainResource):
    """ 
    H
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
    l
    a
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
    t
    i
    o
    n
    o
    f
    h
    o
    w
    o
    n
    e
    o
    r
    m
    o
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
    s
    i
    n
    t
    e
    n
    d
    t
    o
    d
    e
    l
    i
    v
    e
    r
    c
    a
    r
    e
    f
    o
    r
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
    g
    r
    o
    u
    p
    o
    r
    c
    o
    m
    m
    u
    n
    i
    t
    y
    f
    o
    r
    a
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
    ,
    p
    o
    s
    s
    i
    b
    l
    y
    l
    i
    m
    i
    t
    e
    d
    t
    o
    c
    a
    r
    e
    f
    o
    r
    a
    s
    p
    e
    c
    i
    f
    i
    c
    c
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
    s
    e
    t
    o
    f
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
    .
    
    """
    
    resource_type = "CarePlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activity = None
        """ 
        A
        c
        t
        i
        o
        n
        t
        o
        o
        c
        c
        u
        r
        a
        s
        p
        a
        r
        t
        o
        f
        p
        l
        a
        n
        .
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
        
        self.addresses = None
        """ 
        H
        e
        a
        l
        t
        h
        i
        s
        s
        u
        e
        s
        t
        h
        i
        s
        p
        l
        a
        n
        a
        d
        d
        r
        e
        s
        s
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.author = None
        """ 
        W
        h
        o
        i
        s
        t
        h
        e
        d
        e
        s
        i
        g
        n
        a
        t
        e
        d
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
        p
        a
        r
        t
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ 
        F
        u
        l
        f
        i
        l
        l
        s
        C
        a
        r
        e
        P
        l
        a
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.careTeam = None
        """ 
        W
        h
        o
        '
        s
        i
        n
        v
        o
        l
        v
        e
        d
        i
        n
        p
        l
        a
        n
        ?
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
        p
        l
        a
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.contributor = None
        """ 
        W
        h
        o
        p
        r
        o
        v
        i
        d
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
        o
        f
        t
        h
        e
        c
        a
        r
        e
        p
        l
        a
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.created = None
        """ 
        D
        a
        t
        e
        r
        e
        c
        o
        r
        d
        w
        a
        s
        f
        i
        r
        s
        t
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
        
        self.description = None
        """ 
        S
        u
        m
        m
        a
        r
        y
        o
        f
        n
        a
        t
        u
        r
        e
        o
        f
        p
        l
        a
        n
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
        
        self.goal = None
        """ 
        D
        e
        s
        i
        r
        e
        d
        o
        u
        t
        c
        o
        m
        e
        o
        f
        p
        l
        a
        n
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
        p
        l
        a
        n
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
        p
        t
        i
        o
        n
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
        p
        l
        a
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
        C
        a
        r
        e
        P
        l
        a
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.period = None
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
        p
        l
        a
        n
        c
        o
        v
        e
        r
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.replaces = None
        """ 
        C
        a
        r
        e
        P
        l
        a
        n
        r
        e
        p
        l
        a
        c
        e
        d
        b
        y
        t
        h
        i
        s
        C
        a
        r
        e
        P
        l
        a
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
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        self.subject = None
        """ 
        W
        h
        o
        t
        h
        e
        c
        a
        r
        e
        p
        l
        a
        n
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.supportingInfo = None
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
        a
        s
        p
        a
        r
        t
        o
        f
        p
        l
        a
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        H
        u
        m
        a
        n
        -
        f
        r
        i
        e
        n
        d
        l
        y
        n
        a
        m
        e
        f
        o
        r
        t
        h
        e
        c
        a
        r
        e
        p
        l
        a
        n
        .
        Type `str`. """
        
        super(CarePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("activity", "activity", CarePlanActivity, True, None, False),
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("careTeam", "careTeam", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("contributor", "contributor", fhirreference.FHIRReference, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


from . import backboneelement

class CarePlanActivity(backboneelement.BackboneElement):
    """ 
    A
    c
    t
    i
    o
    n
    t
    o
    o
    c
    c
    u
    r
    a
    s
    p
    a
    r
    t
    o
    f
    p
    l
    a
    n
    .
    
    
    I
    d
    e
    n
    t
    i
    f
    i
    e
    s
    a
    p
    l
    a
    n
    n
    e
    d
    a
    c
    t
    i
    o
    n
    t
    o
    o
    c
    c
    u
    r
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
    p
    l
    a
    n
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
    b
    e
    u
    s
    e
    d
    ,
    l
    a
    b
    t
    e
    s
    t
    s
    t
    o
    p
    e
    r
    f
    o
    r
    m
    ,
    s
    e
    l
    f
    -
    m
    o
    n
    i
    t
    o
    r
    i
    n
    g
    ,
    e
    d
    u
    c
    a
    t
    i
    o
    n
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "CarePlanActivity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detail = None
        """ 
        I
        n
        -
        l
        i
        n
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
        c
        t
        i
        v
        i
        t
        y
        .
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """
        
        self.outcomeCodeableConcept = None
        """ 
        R
        e
        s
        u
        l
        t
        s
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcomeReference = None
        """ 
        A
        p
        p
        o
        i
        n
        t
        m
        e
        n
        t
        ,
        E
        n
        c
        o
        u
        n
        t
        e
        r
        ,
        P
        r
        o
        c
        e
        d
        u
        r
        e
        ,
        e
        t
        c
        .
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.progress = None
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
        a
        c
        t
        i
        v
        i
        t
        y
        s
        t
        a
        t
        u
        s
        /
        p
        r
        o
        g
        r
        e
        s
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ 
        A
        c
        t
        i
        v
        i
        t
        y
        d
        e
        t
        a
        i
        l
        s
        d
        e
        f
        i
        n
        e
        d
        i
        n
        s
        p
        e
        c
        i
        f
        i
        c
        r
        e
        s
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(CarePlanActivity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("detail", "detail", CarePlanActivityDetail, False, None, False),
            ("outcomeCodeableConcept", "outcomeCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("progress", "progress", annotation.Annotation, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ 
    I
    n
    -
    l
    i
    n
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
    c
    t
    i
    v
    i
    t
    y
    .
    
    
    A
    s
    i
    m
    p
    l
    e
    s
    u
    m
    m
    a
    r
    y
    o
    f
    a
    p
    l
    a
    n
    n
    e
    d
    a
    c
    t
    i
    v
    i
    t
    y
    s
    u
    i
    t
    a
    b
    l
    e
    f
    o
    r
    a
    g
    e
    n
    e
    r
    a
    l
    c
    a
    r
    e
    p
    l
    a
    n
    s
    y
    s
    t
    e
    m
    (
    e
    .
    g
    .
    f
    o
    r
    m
    d
    r
    i
    v
    e
    n
    )
    t
    h
    a
    t
    d
    o
    e
    s
    n
    '
    t
    k
    n
    o
    w
    a
    b
    o
    u
    t
    s
    p
    e
    c
    i
    f
    i
    c
    r
    e
    s
    o
    u
    r
    c
    e
    s
    s
    u
    c
    h
    a
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
    e
    t
    c
    .
    
    """
    
    resource_type = "CarePlanActivityDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.dailyAmount = None
        """ 
        H
        o
        w
        t
        o
        c
        o
        n
        s
        u
        m
        e
        /
        d
        a
        y
        ?
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.description = None
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
        p
        e
        r
        f
        o
        r
        m
        .
        Type `str`. """
        
        self.doNotPerform = None
        """ 
        I
        f
        t
        r
        u
        e
        ,
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
        
        self.goal = None
        """ 
        G
        o
        a
        l
        s
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
        r
        e
        l
        a
        t
        e
        s
        t
        o
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        
        self.performer = None
        """ 
        W
        h
        o
        w
        i
        l
        l
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
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.productCodeableConcept = None
        """ 
        W
        h
        a
        t
        i
        s
        t
        o
        b
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
        i
        s
        t
        o
        b
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
        
        self.quantity = None
        """ 
        H
        o
        w
        m
        u
        c
        h
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
        /
        s
        u
        p
        p
        l
        y
        /
        c
        o
        n
        s
        u
        m
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
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
        b
        e
        d
        o
        n
        e
        o
        r
        w
        h
        y
        a
        c
        t
        i
        v
        i
        t
        y
        w
        a
        s
        p
        r
        o
        h
        i
        b
        i
        t
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
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
        n
        e
        e
        d
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.scheduledPeriod = None
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
        
        self.scheduledString = None
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
        Type `str`. """
        
        self.scheduledTiming = None
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
        
        self.status = None
        """ 
        n
        o
        t
        -
        s
        t
        a
        r
        t
        e
        d
        |
        s
        c
        h
        e
        d
        u
        l
        e
        d
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
        
        super(CarePlanActivityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("dailyAmount", "dailyAmount", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("kind", "kind", str, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False),
            ("scheduledString", "scheduledString", str, False, "scheduled", False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False, "scheduled", False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
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
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
