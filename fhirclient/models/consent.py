#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Consent) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Consent(domainresource.DomainResource):
    """ 
    A
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
    c
    o
    n
    s
    u
    m
    e
    r
    '
    s
    c
    h
    o
    i
    c
    e
    s
    t
    o
    p
    e
    r
    m
    i
    t
    o
    r
    d
    e
    n
    y
    r
    e
    c
    i
    p
    i
    e
    n
    t
    s
    o
    r
    r
    o
    l
    e
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
    a
    c
    t
    i
    o
    n
    s
    f
    o
    r
    s
    p
    e
    c
    i
    f
    i
    c
    p
    u
    r
    p
    o
    s
    e
    s
    a
    n
    d
    p
    e
    r
    i
    o
    d
    s
    o
    f
    t
    i
    m
    e
    .
    
    
    A
    r
    e
    c
    o
    r
    d
    o
    f
    a
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
    c
    o
    n
    s
    u
    m
    e
    r
    ’
    s
    c
    h
    o
    i
    c
    e
    s
    ,
    w
    h
    i
    c
    h
    p
    e
    r
    m
    i
    t
    s
    o
    r
    d
    e
    n
    i
    e
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
    r
    e
    c
    i
    p
    i
    e
    n
    t
    (
    s
    )
    o
    r
    r
    e
    c
    i
    p
    i
    e
    n
    t
    r
    o
    l
    e
    (
    s
    )
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
    e
    o
    r
    m
    o
    r
    e
    a
    c
    t
    i
    o
    n
    s
    w
    i
    t
    h
    i
    n
    a
    g
    i
    v
    e
    n
    p
    o
    l
    i
    c
    y
    c
    o
    n
    t
    e
    x
    t
    ,
    f
    o
    r
    s
    p
    e
    c
    i
    f
    i
    c
    p
    u
    r
    p
    o
    s
    e
    s
    a
    n
    d
    p
    e
    r
    i
    o
    d
    s
    o
    f
    t
    i
    m
    e
    .
    
    """
    
    resource_type = "Consent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        c
        o
        n
        s
        e
        n
        t
        s
        t
        a
        t
        e
        m
        e
        n
        t
        -
        f
        o
        r
        i
        n
        d
        e
        x
        i
        n
        g
        /
        r
        e
        t
        r
        i
        e
        v
        a
        l
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ 
        W
        h
        e
        n
        t
        h
        i
        s
        C
        o
        n
        s
        e
        n
        t
        w
        a
        s
        c
        r
        e
        a
        t
        e
        d
        o
        r
        i
        n
        d
        e
        x
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ 
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
        (
        e
        x
        t
        e
        r
        n
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
        s
        )
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ 
        C
        u
        s
        t
        o
        d
        i
        a
        n
        o
        f
        t
        h
        e
        c
        o
        n
        s
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        W
        h
        o
        t
        h
        e
        c
        o
        n
        s
        e
        n
        t
        a
        p
        p
        l
        i
        e
        s
        t
        o
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        W
        h
        o
        i
        s
        a
        g
        r
        e
        e
        i
        n
        g
        t
        o
        t
        h
        e
        p
        o
        l
        i
        c
        y
        a
        n
        d
        r
        u
        l
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.policy = None
        """ 
        P
        o
        l
        i
        c
        i
        e
        s
        c
        o
        v
        e
        r
        e
        d
        b
        y
        t
        h
        i
        s
        c
        o
        n
        s
        e
        n
        t
        .
        List of `ConsentPolicy` items (represented as `dict` in JSON). """
        
        self.policyRule = None
        """ 
        R
        e
        g
        u
        l
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
        i
        s
        c
        o
        n
        s
        e
        n
        t
        s
        t
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provision = None
        """ 
        C
        o
        n
        s
        t
        r
        a
        i
        n
        t
        s
        t
        o
        t
        h
        e
        b
        a
        s
        e
        C
        o
        n
        s
        e
        n
        t
        .
        p
        o
        l
        i
        c
        y
        R
        u
        l
        e
        .
        Type `ConsentProvision` (represented as `dict` in JSON). """
        
        self.scope = None
        """ 
        W
        h
        i
        c
        h
        o
        f
        t
        h
        e
        f
        o
        u
        r
        a
        r
        e
        a
        s
        t
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
        c
        o
        v
        e
        r
        s
        (
        e
        x
        t
        e
        n
        s
        i
        b
        l
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sourceAttachment = None
        """ 
        S
        o
        u
        r
        c
        e
        f
        r
        o
        m
        w
        h
        i
        c
        h
        t
        h
        i
        s
        c
        o
        n
        s
        e
        n
        t
        i
        s
        t
        a
        k
        e
        n
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.sourceReference = None
        """ 
        S
        o
        u
        r
        c
        e
        f
        r
        o
        m
        w
        h
        i
        c
        h
        t
        h
        i
        s
        c
        o
        n
        s
        e
        n
        t
        i
        s
        t
        a
        k
        e
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        p
        r
        o
        p
        o
        s
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
        r
        e
        j
        e
        c
        t
        e
        d
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
        
        self.verification = None
        """ 
        C
        o
        n
        s
        e
        n
        t
        V
        e
        r
        i
        f
        i
        e
        d
        b
        y
        p
        a
        t
        i
        e
        n
        t
        o
        r
        f
        a
        m
        i
        l
        y
        .
        List of `ConsentVerification` items (represented as `dict` in JSON). """
        
        super(Consent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, True),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("policy", "policy", ConsentPolicy, True, None, False),
            ("policyRule", "policyRule", codeableconcept.CodeableConcept, False, None, False),
            ("provision", "provision", ConsentProvision, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, True),
            ("sourceAttachment", "sourceAttachment", attachment.Attachment, False, "source", False),
            ("sourceReference", "sourceReference", fhirreference.FHIRReference, False, "source", False),
            ("status", "status", str, False, None, True),
            ("verification", "verification", ConsentVerification, True, None, False),
        ])
        return js


from . import backboneelement

class ConsentPolicy(backboneelement.BackboneElement):
    """ 
    P
    o
    l
    i
    c
    i
    e
    s
    c
    o
    v
    e
    r
    e
    d
    b
    y
    t
    h
    i
    s
    c
    o
    n
    s
    e
    n
    t
    .
    
    
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
    s
    t
    o
    t
    h
    e
    p
    o
    l
    i
    c
    i
    e
    s
    t
    h
    a
    t
    a
    r
    e
    i
    n
    c
    l
    u
    d
    e
    d
    i
    n
    t
    h
    i
    s
    c
    o
    n
    s
    e
    n
    t
    s
    c
    o
    p
    e
    .
    P
    o
    l
    i
    c
    i
    e
    s
    m
    a
    y
    b
    e
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
    a
    l
    ,
    b
    u
    t
    a
    r
    e
    o
    f
    t
    e
    n
    d
    e
    f
    i
    n
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
    a
    l
    l
    y
    ,
    o
    r
    i
    n
    l
    a
    w
    .
    
    """
    
    resource_type = "ConsentPolicy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None
        """ 
        E
        n
        f
        o
        r
        c
        e
        m
        e
        n
        t
        s
        o
        u
        r
        c
        e
        f
        o
        r
        p
        o
        l
        i
        c
        y
        .
        Type `str`. """
        
        self.uri = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        p
        o
        l
        i
        c
        y
        c
        o
        v
        e
        r
        e
        d
        b
        y
        t
        h
        i
        s
        c
        o
        n
        s
        e
        n
        t
        .
        Type `str`. """
        
        super(ConsentPolicy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentPolicy, self).elementProperties()
        js.extend([
            ("authority", "authority", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js


class ConsentProvision(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    s
    t
    r
    a
    i
    n
    t
    s
    t
    o
    t
    h
    e
    b
    a
    s
    e
    C
    o
    n
    s
    e
    n
    t
    .
    p
    o
    l
    i
    c
    y
    R
    u
    l
    e
    .
    
    
    A
    n
    e
    x
    c
    e
    p
    t
    i
    o
    n
    t
    o
    t
    h
    e
    b
    a
    s
    e
    p
    o
    l
    i
    c
    y
    o
    f
    t
    h
    i
    s
    c
    o
    n
    s
    e
    n
    t
    .
    A
    n
    e
    x
    c
    e
    p
    t
    i
    o
    n
    c
    a
    n
    b
    e
    a
    n
    a
    d
    d
    i
    t
    i
    o
    n
    o
    r
    r
    e
    m
    o
    v
    a
    l
    o
    f
    a
    c
    c
    e
    s
    s
    p
    e
    r
    m
    i
    s
    s
    i
    o
    n
    s
    .
    
    """
    
    resource_type = "ConsentProvision"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        A
        c
        t
        i
        o
        n
        s
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        b
        y
        t
        h
        i
        s
        r
        u
        l
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.actor = None
        """ 
        W
        h
        o
        |
        w
        h
        a
        t
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        b
        y
        t
        h
        i
        s
        r
        u
        l
        e
        (
        o
        r
        g
        r
        o
        u
        p
        ,
        b
        y
        r
        o
        l
        e
        )
        .
        List of `ConsentProvisionActor` items (represented as `dict` in JSON). """
        
        self.class_fhir = None
        """ 
        e
        .
        g
        .
        R
        e
        s
        o
        u
        r
        c
        e
        T
        y
        p
        e
        ,
        P
        r
        o
        f
        i
        l
        e
        ,
        C
        D
        A
        ,
        e
        t
        c
        .
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        e
        .
        g
        .
        L
        O
        I
        N
        C
        o
        r
        S
        N
        O
        M
        E
        D
        C
        T
        c
        o
        d
        e
        ,
        e
        t
        c
        .
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
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.data = None
        """ 
        D
        a
        t
        a
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        b
        y
        t
        h
        i
        s
        r
        u
        l
        e
        .
        List of `ConsentProvisionData` items (represented as `dict` in JSON). """
        
        self.dataPeriod = None
        """ 
        T
        i
        m
        e
        f
        r
        a
        m
        e
        f
        o
        r
        d
        a
        t
        a
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        b
        y
        t
        h
        i
        s
        r
        u
        l
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        T
        i
        m
        e
        f
        r
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
        r
        u
        l
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.provision = None
        """ 
        N
        e
        s
        t
        e
        d
        E
        x
        c
        e
        p
        t
        i
        o
        n
        R
        u
        l
        e
        s
        .
        List of `ConsentProvision` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ 
        C
        o
        n
        t
        e
        x
        t
        o
        f
        a
        c
        t
        i
        v
        i
        t
        i
        e
        s
        c
        o
        v
        e
        r
        e
        d
        b
        y
        t
        h
        i
        s
        r
        u
        l
        e
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ 
        S
        e
        c
        u
        r
        i
        t
        y
        L
        a
        b
        e
        l
        s
        t
        h
        a
        t
        d
        e
        f
        i
        n
        e
        a
        f
        f
        e
        c
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
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        d
        e
        n
        y
        |
        p
        e
        r
        m
        i
        t
        .
        Type `str`. """
        
        super(ConsentProvision, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvision, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, True, None, False),
            ("actor", "actor", ConsentProvisionActor, True, None, False),
            ("class_fhir", "class", coding.Coding, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("data", "data", ConsentProvisionData, True, None, False),
            ("dataPeriod", "dataPeriod", period.Period, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("provision", "provision", ConsentProvision, True, None, False),
            ("purpose", "purpose", coding.Coding, True, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class ConsentProvisionActor(backboneelement.BackboneElement):
    """ 
    W
    h
    o
    |
    w
    h
    a
    t
    c
    o
    n
    t
    r
    o
    l
    l
    e
    d
    b
    y
    t
    h
    i
    s
    r
    u
    l
    e
    (
    o
    r
    g
    r
    o
    u
    p
    ,
    b
    y
    r
    o
    l
    e
    )
    .
    
    
    W
    h
    o
    o
    r
    w
    h
    a
    t
    i
    s
    c
    o
    n
    t
    r
    o
    l
    l
    e
    d
    b
    y
    t
    h
    i
    s
    r
    u
    l
    e
    .
    U
    s
    e
    g
    r
    o
    u
    p
    t
    o
    i
    d
    e
    n
    t
    i
    f
    y
    a
    s
    e
    t
    o
    f
    a
    c
    t
    o
    r
    s
    b
    y
    s
    o
    m
    e
    p
    r
    o
    p
    e
    r
    t
    y
    t
    h
    e
    y
    s
    h
    a
    r
    e
    (
    e
    .
    g
    .
    '
    a
    d
    m
    i
    t
    t
    i
    n
    g
    o
    f
    f
    i
    c
    e
    r
    s
    '
    )
    .
    
    """
    
    resource_type = "ConsentProvisionActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ 
        R
        e
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
        a
        c
        t
        o
        r
        (
        o
        r
        g
        r
        o
        u
        p
        ,
        b
        y
        r
        o
        l
        e
        )
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        H
        o
        w
        t
        h
        e
        a
        c
        t
        o
        r
        i
        s
        i
        n
        v
        o
        l
        v
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConsentProvisionActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvisionActor, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ConsentProvisionData(backboneelement.BackboneElement):
    """ 
    D
    a
    t
    a
    c
    o
    n
    t
    r
    o
    l
    l
    e
    d
    b
    y
    t
    h
    i
    s
    r
    u
    l
    e
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
    s
    c
    o
    n
    t
    r
    o
    l
    l
    e
    d
    b
    y
    t
    h
    i
    s
    r
    u
    l
    e
    i
    f
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
    a
    r
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
    d
    .
    
    """
    
    resource_type = "ConsentProvisionData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.meaning = None
        """ 
        i
        n
        s
        t
        a
        n
        c
        e
        |
        r
        e
        l
        a
        t
        e
        d
        |
        d
        e
        p
        e
        n
        d
        e
        n
        t
        s
        |
        a
        u
        t
        h
        o
        r
        e
        d
        b
        y
        .
        Type `str`. """
        
        self.reference = None
        """ 
        T
        h
        e
        a
        c
        t
        u
        a
        l
        d
        a
        t
        a
        r
        e
        f
        e
        r
        e
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConsentProvisionData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentProvisionData, self).elementProperties()
        js.extend([
            ("meaning", "meaning", str, False, None, True),
            ("reference", "reference", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class ConsentVerification(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    s
    e
    n
    t
    V
    e
    r
    i
    f
    i
    e
    d
    b
    y
    p
    a
    t
    i
    e
    n
    t
    o
    r
    f
    a
    m
    i
    l
    y
    .
    
    
    W
    h
    e
    t
    h
    e
    r
    a
    t
    r
    e
    a
    t
    m
    e
    n
    t
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
    (
    e
    .
    g
    .
    a
    r
    t
    i
    f
    i
    c
    i
    a
    l
    r
    e
    s
    p
    i
    r
    a
    t
    i
    o
    n
    y
    e
    s
    o
    r
    n
    o
    )
    w
    a
    s
    v
    e
    r
    i
    f
    i
    e
    d
    w
    i
    t
    h
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
    ,
    h
    i
    s
    /
    h
    e
    r
    f
    a
    m
    i
    l
    y
    o
    r
    a
    n
    o
    t
    h
    e
    r
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
    p
    e
    r
    s
    o
    n
    .
    
    """
    
    resource_type = "ConsentVerification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.verificationDate = None
        """ 
        W
        h
        e
        n
        c
        o
        n
        s
        e
        n
        t
        v
        e
        r
        i
        f
        i
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.verified = None
        """ 
        H
        a
        s
        b
        e
        e
        n
        v
        e
        r
        i
        f
        i
        e
        d
        .
        Type `bool`. """
        
        self.verifiedWith = None
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
        v
        e
        r
        i
        f
        i
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ConsentVerification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConsentVerification, self).elementProperties()
        js.extend([
            ("verificationDate", "verificationDate", fhirdate.FHIRDate, False, None, False),
            ("verified", "verified", bool, False, None, True),
            ("verifiedWith", "verifiedWith", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
