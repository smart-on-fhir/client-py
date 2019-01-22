#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Contract) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Contract(domainresource.DomainResource):
    """ 
    L
    e
    g
    a
    l
    A
    g
    r
    e
    e
    m
    e
    n
    t
    .
    
    
    L
    e
    g
    a
    l
    l
    y
    e
    n
    f
    o
    r
    c
    e
    a
    b
    l
    e
    ,
    f
    o
    r
    m
    a
    l
    l
    y
    r
    e
    c
    o
    r
    d
    e
    d
    u
    n
    i
    l
    a
    t
    e
    r
    a
    l
    o
    r
    b
    i
    l
    a
    t
    e
    r
    a
    l
    d
    i
    r
    e
    c
    t
    i
    v
    e
    i
    .
    e
    .
    ,
    a
    p
    o
    l
    i
    c
    y
    o
    r
    a
    g
    r
    e
    e
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "Contract"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        """ 
        A
        c
        r
        o
        n
        y
        m
        o
        r
        s
        h
        o
        r
        t
        n
        a
        m
        e
        .
        List of `str` items. """
        
        self.applies = None
        """ 
        E
        f
        f
        e
        c
        t
        i
        v
        e
        t
        i
        m
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.author = None
        """ 
        S
        o
        u
        r
        c
        e
        o
        f
        C
        o
        n
        t
        r
        a
        c
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authority = None
        """ 
        A
        u
        t
        h
        o
        r
        i
        t
        y
        u
        n
        d
        e
        r
        w
        h
        i
        c
        h
        t
        h
        i
        s
        C
        o
        n
        t
        r
        a
        c
        t
        h
        a
        s
        s
        t
        a
        n
        d
        i
        n
        g
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.contentDefinition = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        p
        r
        e
        c
        u
        r
        s
        o
        r
        c
        o
        n
        t
        e
        n
        t
        .
        Type `ContractContentDefinition` (represented as `dict` in JSON). """
        
        self.contentDerivative = None
        """ 
        C
        o
        n
        t
        e
        n
        t
        d
        e
        r
        i
        v
        e
        d
        f
        r
        o
        m
        t
        h
        e
        b
        a
        s
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.domain = None
        """ 
        A
        s
        p
        h
        e
        r
        e
        o
        f
        c
        o
        n
        t
        r
        o
        l
        g
        o
        v
        e
        r
        n
        e
        d
        b
        y
        a
        n
        a
        u
        t
        h
        o
        r
        i
        t
        a
        t
        i
        v
        e
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
        ,
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
        ,
        o
        r
        p
        e
        r
        s
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.expirationType = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        c
        e
        s
        s
        a
        t
        i
        o
        n
        c
        a
        u
        s
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.friendly = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        F
        r
        i
        e
        n
        d
        l
        y
        L
        a
        n
        g
        u
        a
        g
        e
        .
        List of `ContractFriendly` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        n
        u
        m
        b
        e
        r
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ 
        S
        o
        u
        r
        c
        e
        C
        o
        n
        t
        r
        a
        c
        t
        D
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.instantiatesUri = None
        """ 
        E
        x
        t
        e
        r
        n
        a
        l
        C
        o
        n
        t
        r
        a
        c
        t
        D
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
        
        self.issued = None
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
        t
        r
        a
        c
        t
        w
        a
        s
        i
        s
        s
        u
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.legal = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        L
        e
        g
        a
        l
        L
        a
        n
        g
        u
        a
        g
        e
        .
        List of `ContractLegal` items (represented as `dict` in JSON). """
        
        self.legalState = None
        """ 
        N
        e
        g
        o
        t
        i
        a
        t
        i
        o
        n
        s
        t
        a
        t
        u
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.legallyBindingAttachment = None
        """ 
        B
        i
        n
        d
        i
        n
        g
        C
        o
        n
        t
        r
        a
        c
        t
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.legallyBindingReference = None
        """ 
        B
        i
        n
        d
        i
        n
        g
        C
        o
        n
        t
        r
        a
        c
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        C
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
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.relevantHistory = None
        """ 
        K
        e
        y
        e
        v
        e
        n
        t
        i
        n
        C
        o
        n
        t
        r
        a
        c
        t
        H
        i
        s
        t
        o
        r
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.rule = None
        """ 
        C
        o
        m
        p
        u
        t
        a
        b
        l
        e
        C
        o
        n
        t
        r
        a
        c
        t
        L
        a
        n
        g
        u
        a
        g
        e
        .
        List of `ContractRule` items (represented as `dict` in JSON). """
        
        self.scope = None
        """ 
        R
        a
        n
        g
        e
        o
        f
        L
        e
        g
        a
        l
        C
        o
        n
        c
        e
        r
        n
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.signer = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        S
        i
        g
        n
        a
        t
        o
        r
        y
        .
        List of `ContractSigner` items (represented as `dict` in JSON). """
        
        self.site = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        L
        o
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
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        self.subType = None
        """ 
        S
        u
        b
        t
        y
        p
        e
        w
        i
        t
        h
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
        t
        y
        p
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        a
        r
        g
        e
        t
        E
        n
        t
        i
        t
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        F
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
        .
        Type `str`. """
        
        self.supportingInfo = None
        """ 
        E
        x
        t
        r
        a
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.term = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        L
        i
        s
        t
        .
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        H
        u
        m
        a
        n
        F
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
        .
        Type `str`. """
        
        self.topicCodeableConcept = None
        """ 
        F
        o
        c
        u
        s
        o
        f
        c
        o
        n
        t
        r
        a
        c
        t
        i
        n
        t
        e
        r
        e
        s
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference = None
        """ 
        F
        o
        c
        u
        s
        o
        f
        c
        o
        n
        t
        r
        a
        c
        t
        i
        n
        t
        e
        r
        e
        s
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        L
        e
        g
        a
        l
        i
        n
        s
        t
        r
        u
        m
        e
        n
        t
        c
        a
        t
        e
        g
        o
        r
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.url = None
        """ 
        B
        a
        s
        a
        l
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
        e
        d
        i
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(Contract, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contract, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authority", "authority", fhirreference.FHIRReference, True, None, False),
            ("contentDefinition", "contentDefinition", ContractContentDefinition, False, None, False),
            ("contentDerivative", "contentDerivative", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", fhirreference.FHIRReference, True, None, False),
            ("expirationType", "expirationType", codeableconcept.CodeableConcept, False, None, False),
            ("friendly", "friendly", ContractFriendly, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", fhirreference.FHIRReference, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("legal", "legal", ContractLegal, True, None, False),
            ("legalState", "legalState", codeableconcept.CodeableConcept, False, None, False),
            ("legallyBindingAttachment", "legallyBindingAttachment", attachment.Attachment, False, "legallyBinding", False),
            ("legallyBindingReference", "legallyBindingReference", fhirreference.FHIRReference, False, "legallyBinding", False),
            ("name", "name", str, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("rule", "rule", ContractRule, True, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("signer", "signer", ContractSigner, True, None, False),
            ("site", "site", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("term", "term", ContractTerm, True, None, False),
            ("title", "title", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ContractContentDefinition(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    r
    a
    c
    t
    p
    r
    e
    c
    u
    r
    s
    o
    r
    c
    o
    n
    t
    e
    n
    t
    .
    
    
    P
    r
    e
    c
    u
    s
    o
    r
    y
    c
    o
    n
    t
    e
    n
    t
    d
    e
    v
    e
    l
    o
    p
    e
    d
    w
    i
    t
    h
    a
    f
    o
    c
    u
    s
    a
    n
    d
    i
    n
    t
    e
    n
    t
    o
    f
    s
    u
    p
    p
    o
    r
    t
    i
    n
    g
    t
    h
    e
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
    C
    o
    n
    t
    r
    a
    c
    t
    i
    n
    s
    t
    a
    n
    c
    e
    ,
    w
    h
    i
    c
    h
    m
    a
    y
    b
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
    a
    n
    d
    t
    r
    a
    n
    s
    f
    o
    r
    m
    a
    b
    l
    e
    i
    n
    t
    o
    a
    C
    o
    n
    t
    r
    a
    c
    t
    .
    
    """
    
    resource_type = "ContractContentDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.copyright = None
        """ 
        P
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
        O
        w
        n
        e
        r
        s
        h
        i
        p
        .
        Type `str`. """
        
        self.publicationDate = None
        """ 
        W
        h
        e
        n
        p
        u
        b
        l
        i
        s
        h
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.publicationStatus = None
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
        
        self.publisher = None
        """ 
        P
        u
        b
        l
        i
        s
        h
        e
        r
        E
        n
        t
        i
        t
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.subType = None
        """ 
        D
        e
        t
        a
        i
        l
        e
        d
        C
        o
        n
        t
        e
        n
        t
        T
        y
        p
        e
        D
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        o
        n
        t
        e
        n
        t
        s
        t
        r
        u
        c
        t
        u
        r
        e
        a
        n
        d
        u
        s
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractContentDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractContentDefinition, self).elementProperties()
        js.extend([
            ("copyright", "copyright", str, False, None, False),
            ("publicationDate", "publicationDate", fhirdate.FHIRDate, False, None, False),
            ("publicationStatus", "publicationStatus", str, False, None, True),
            ("publisher", "publisher", fhirreference.FHIRReference, False, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractFriendly(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    r
    a
    c
    t
    F
    r
    i
    e
    n
    d
    l
    y
    L
    a
    n
    g
    u
    a
    g
    e
    .
    
    
    T
    h
    e
    "
    p
    a
    t
    i
    e
    n
    t
    f
    r
    i
    e
    n
    d
    l
    y
    l
    a
    n
    g
    u
    a
    g
    e
    "
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
    C
    o
    n
    t
    r
    a
    c
    t
    i
    n
    w
    h
    o
    l
    e
    o
    r
    i
    n
    p
    a
    r
    t
    s
    .
    "
    P
    a
    t
    i
    e
    n
    t
    f
    r
    i
    e
    n
    d
    l
    y
    l
    a
    n
    g
    u
    a
    g
    e
    "
    m
    e
    a
    n
    s
    t
    h
    e
    r
    e
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
    o
    f
    t
    h
    e
    C
    o
    n
    t
    r
    a
    c
    t
    a
    n
    d
    C
    o
    n
    t
    r
    a
    c
    t
    P
    r
    o
    v
    i
    s
    i
    o
    n
    s
    i
    n
    a
    m
    a
    n
    n
    e
    r
    t
    h
    a
    t
    i
    s
    r
    e
    a
    d
    i
    l
    y
    a
    c
    c
    e
    s
    s
    i
    b
    l
    e
    a
    n
    d
    u
    n
    d
    e
    r
    s
    t
    a
    n
    d
    a
    b
    l
    e
    b
    y
    a
    l
    a
    y
    p
    e
    r
    s
    o
    n
    i
    n
    a
    c
    c
    o
    r
    d
    a
    n
    c
    e
    w
    i
    t
    h
    b
    e
    s
    t
    p
    r
    a
    c
    t
    i
    c
    e
    s
    f
    o
    r
    c
    o
    m
    m
    u
    n
    i
    c
    a
    t
    i
    o
    n
    s
    t
    y
    l
    e
    s
    t
    h
    a
    t
    e
    n
    s
    u
    r
    e
    t
    h
    a
    t
    t
    h
    o
    s
    e
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
    o
    r
    s
    i
    g
    n
    i
    n
    g
    t
    h
    e
    C
    o
    n
    t
    r
    a
    c
    t
    u
    n
    d
    e
    r
    s
    t
    a
    n
    d
    t
    h
    e
    r
    o
    l
    e
    s
    ,
    a
    c
    t
    i
    o
    n
    s
    ,
    o
    b
    l
    i
    g
    a
    t
    i
    o
    n
    s
    ,
    r
    e
    s
    p
    o
    n
    s
    i
    b
    i
    l
    i
    t
    i
    e
    s
    ,
    a
    n
    d
    i
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
    o
    f
    t
    h
    e
    a
    g
    r
    e
    e
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "ContractFriendly"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ 
        E
        a
        s
        i
        l
        y
        c
        o
        m
        p
        r
        e
        h
        e
        n
        d
        e
        d
        r
        e
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
        o
        f
        t
        h
        i
        s
        C
        o
        n
        t
        r
        a
        c
        t
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ 
        E
        a
        s
        i
        l
        y
        c
        o
        m
        p
        r
        e
        h
        e
        n
        d
        e
        d
        r
        e
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
        o
        f
        t
        h
        i
        s
        C
        o
        n
        t
        r
        a
        c
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractFriendly, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractFriendly, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractLegal(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    r
    a
    c
    t
    L
    e
    g
    a
    l
    L
    a
    n
    g
    u
    a
    g
    e
    .
    
    
    L
    i
    s
    t
    o
    f
    L
    e
    g
    a
    l
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
    s
    o
    r
    r
    e
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
    s
    o
    f
    t
    h
    i
    s
    C
    o
    n
    t
    r
    a
    c
    t
    .
    
    """
    
    resource_type = "ContractLegal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        L
        e
        g
        a
        l
        T
        e
        x
        t
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        L
        e
        g
        a
        l
        T
        e
        x
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractLegal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractLegal, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractRule(backboneelement.BackboneElement):
    """ 
    C
    o
    m
    p
    u
    t
    a
    b
    l
    e
    C
    o
    n
    t
    r
    a
    c
    t
    L
    a
    n
    g
    u
    a
    g
    e
    .
    
    
    L
    i
    s
    t
    o
    f
    C
    o
    m
    p
    u
    t
    a
    b
    l
    e
    P
    o
    l
    i
    c
    y
    R
    u
    l
    e
    L
    a
    n
    g
    u
    a
    g
    e
    R
    e
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
    s
    o
    f
    t
    h
    i
    s
    C
    o
    n
    t
    r
    a
    c
    t
    .
    
    """
    
    resource_type = "ContractRule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ 
        C
        o
        m
        p
        u
        t
        a
        b
        l
        e
        C
        o
        n
        t
        r
        a
        c
        t
        R
        u
        l
        e
        s
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ 
        C
        o
        m
        p
        u
        t
        a
        b
        l
        e
        C
        o
        n
        t
        r
        a
        c
        t
        R
        u
        l
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ContractRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractRule, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
        ])
        return js


class ContractSigner(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    r
    a
    c
    t
    S
    i
    g
    n
    a
    t
    o
    r
    y
    .
    
    
    P
    a
    r
    t
    i
    e
    s
    w
    i
    t
    h
    l
    e
    g
    a
    l
    s
    t
    a
    n
    d
    i
    n
    g
    i
    n
    t
    h
    e
    C
    o
    n
    t
    r
    a
    c
    t
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
    t
    h
    e
    p
    r
    i
    n
    c
    i
    p
    a
    l
    p
    a
    r
    t
    i
    e
    s
    ,
    t
    h
    e
    g
    r
    a
    n
    t
    o
    r
    (
    s
    )
    a
    n
    d
    g
    r
    a
    n
    t
    e
    e
    (
    s
    )
    ,
    w
    h
    i
    c
    h
    a
    r
    e
    a
    n
    y
    p
    e
    r
    s
    o
    n
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
    b
    o
    u
    n
    d
    b
    y
    t
    h
    e
    c
    o
    n
    t
    r
    a
    c
    t
    ,
    a
    n
    d
    a
    n
    y
    a
    n
    c
    i
    l
    l
    a
    r
    y
    p
    a
    r
    t
    i
    e
    s
    ,
    w
    h
    i
    c
    h
    f
    a
    c
    i
    l
    i
    t
    a
    t
    e
    t
    h
    e
    e
    x
    e
    c
    u
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
    t
    r
    a
    c
    t
    s
    u
    c
    h
    a
    s
    a
    n
    o
    t
    a
    r
    y
    o
    r
    w
    i
    t
    n
    e
    s
    s
    .
    
    """
    
    resource_type = "ContractSigner"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.party = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        S
        i
        g
        n
        a
        t
        o
        r
        y
        P
        a
        r
        t
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.signature = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        D
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
        S
        i
        g
        n
        a
        t
        u
        r
        e
        .
        List of `Signature` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        S
        i
        g
        n
        a
        t
        o
        r
        y
        R
        o
        l
        e
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ContractSigner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractSigner, self).elementProperties()
        js.extend([
            ("party", "party", fhirreference.FHIRReference, False, None, True),
            ("signature", "signature", signature.Signature, True, None, True),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ContractTerm(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    r
    a
    c
    t
    T
    e
    r
    m
    L
    i
    s
    t
    .
    
    
    O
    n
    e
    o
    r
    m
    o
    r
    e
    C
    o
    n
    t
    r
    a
    c
    t
    P
    r
    o
    v
    i
    s
    i
    o
    n
    s
    ,
    w
    h
    i
    c
    h
    m
    a
    y
    b
    e
    r
    e
    l
    a
    t
    e
    d
    a
    n
    d
    c
    o
    n
    v
    e
    y
    e
    d
    a
    s
    a
    g
    r
    o
    u
    p
    ,
    a
    n
    d
    m
    a
    y
    c
    o
    n
    t
    a
    i
    n
    n
    e
    s
    t
    e
    d
    g
    r
    o
    u
    p
    s
    .
    
    """
    
    resource_type = "ContractTerm"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        E
        n
        t
        i
        t
        y
        b
        e
        i
        n
        g
        a
        s
        c
        r
        i
        b
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
        i
        l
        i
        t
        y
        .
        List of `ContractTermAction` items (represented as `dict` in JSON). """
        
        self.applies = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        E
        f
        f
        e
        c
        t
        i
        v
        e
        T
        i
        m
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.asset = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        A
        s
        s
        e
        t
        L
        i
        s
        t
        .
        List of `ContractTermAsset` items (represented as `dict` in JSON). """
        
        self.group = None
        """ 
        N
        e
        s
        t
        e
        d
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        G
        r
        o
        u
        p
        .
        List of `ContractTerm` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        N
        u
        m
        b
        e
        r
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        I
        s
        s
        u
        e
        D
        a
        t
        e
        T
        i
        m
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.offer = None
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
        t
        h
        e
        C
        o
        n
        t
        r
        a
        c
        t
        t
        e
        r
        m
        .
        Type `ContractTermOffer` (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ 
        P
        r
        o
        t
        e
        c
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
        T
        e
        r
        m
        .
        List of `ContractTermSecurityLabel` items (represented as `dict` in JSON). """
        
        self.subType = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        T
        y
        p
        e
        s
        p
        e
        c
        i
        f
        i
        c
        c
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        T
        e
        r
        m
        S
        t
        a
        t
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.topicCodeableConcept = None
        """ 
        T
        e
        r
        m
        C
        o
        n
        c
        e
        r
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.topicReference = None
        """ 
        T
        e
        r
        m
        C
        o
        n
        c
        e
        r
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        T
        y
        p
        e
        o
        r
        F
        o
        r
        m
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTerm, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTerm, self).elementProperties()
        js.extend([
            ("action", "action", ContractTermAction, True, None, False),
            ("applies", "applies", period.Period, False, None, False),
            ("asset", "asset", ContractTermAsset, True, None, False),
            ("group", "group", ContractTerm, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("offer", "offer", ContractTermOffer, False, None, True),
            ("securityLabel", "securityLabel", ContractTermSecurityLabel, True, None, False),
            ("subType", "subType", codeableconcept.CodeableConcept, False, None, False),
            ("text", "text", str, False, None, False),
            ("topicCodeableConcept", "topicCodeableConcept", codeableconcept.CodeableConcept, False, "topic", False),
            ("topicReference", "topicReference", fhirreference.FHIRReference, False, "topic", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermAction(backboneelement.BackboneElement):
    """ 
    E
    n
    t
    i
    t
    y
    b
    e
    i
    n
    g
    a
    s
    c
    r
    i
    b
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
    i
    l
    i
    t
    y
    .
    
    
    A
    n
    a
    c
    t
    o
    r
    t
    a
    k
    i
    n
    g
    a
    r
    o
    l
    e
    i
    n
    a
    n
    a
    c
    t
    i
    v
    i
    t
    y
    f
    o
    r
    w
    h
    i
    c
    h
    i
    t
    c
    a
    n
    b
    e
    a
    s
    s
    i
    g
    n
    e
    d
    s
    o
    m
    e
    d
    e
    g
    r
    e
    e
    o
    f
    r
    e
    s
    p
    o
    n
    s
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
    t
    a
    k
    i
    n
    g
    p
    l
    a
    c
    e
    .
    
    """
    
    resource_type = "ContractTermAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context = None
        """ 
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
        a
        c
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contextLinkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        s
        p
        e
        c
        i
        f
        i
        c
        i
        t
        e
        m
        .
        List of `str` items. """
        
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
        t
        e
        r
        m
        p
        r
        o
        h
        i
        b
        i
        t
        s
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
        Type `bool`. """
        
        self.intent = None
        """ 
        P
        u
        r
        p
        o
        s
        e
        f
        o
        r
        t
        h
        e
        C
        o
        n
        t
        r
        a
        c
        t
        T
        e
        r
        m
        A
        c
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.linkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        s
        p
        e
        c
        i
        f
        i
        c
        i
        t
        e
        m
        .
        List of `str` items. """
        
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
        a
        c
        t
        i
        o
        n
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        o
        n
        h
        a
        p
        p
        e
        n
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        o
        n
        h
        a
        p
        p
        e
        n
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ 
        W
        h
        e
        n
        a
        c
        t
        i
        o
        n
        h
        a
        p
        p
        e
        n
        s
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.performer = None
        """ 
        A
        c
        t
        o
        r
        t
        h
        a
        t
        w
        i
        l
        e
        x
        e
        c
        u
        t
        e
        (
        o
        r
        n
        o
        t
        )
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.performerLinkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        s
        p
        e
        c
        i
        f
        i
        c
        i
        t
        e
        m
        .
        List of `str` items. """
        
        self.performerRole = None
        """ 
        C
        o
        m
        p
        e
        t
        e
        n
        c
        y
        o
        f
        t
        h
        e
        p
        e
        r
        f
        o
        r
        m
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ 
        K
        i
        n
        d
        o
        f
        s
        e
        r
        v
        i
        c
        e
        p
        e
        r
        f
        o
        r
        m
        e
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reason = None
        """ 
        W
        h
        y
        a
        c
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
        List of `str` items. """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        i
        s
        a
        c
        t
        i
        o
        n
        (
        n
        o
        t
        )
        n
        e
        e
        d
        e
        d
        ?
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonLinkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        s
        p
        e
        c
        i
        f
        i
        c
        i
        t
        e
        m
        .
        List of `str` items. """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        i
        s
        a
        c
        t
        i
        o
        n
        (
        n
        o
        t
        )
        n
        e
        e
        d
        e
        d
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        """ 
        W
        h
        o
        a
        s
        k
        e
        d
        f
        o
        r
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requesterLinkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        s
        p
        e
        c
        i
        f
        i
        c
        i
        t
        e
        m
        .
        List of `str` items. """
        
        self.securityLabelNumber = None
        """ 
        A
        c
        t
        i
        o
        n
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
        n
        u
        m
        b
        e
        r
        s
        .
        List of `int` items. """
        
        self.status = None
        """ 
        S
        t
        a
        t
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
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        E
        n
        t
        i
        t
        y
        o
        f
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
        List of `ContractTermActionSubject` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        r
        f
        o
        r
        m
        o
        f
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAction, self).elementProperties()
        js.extend([
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("contextLinkId", "contextLinkId", str, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("intent", "intent", codeableconcept.CodeableConcept, False, None, True),
            ("linkId", "linkId", str, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("performerLinkId", "performerLinkId", str, True, None, False),
            ("performerRole", "performerRole", codeableconcept.CodeableConcept, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("reason", "reason", str, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonLinkId", "reasonLinkId", str, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, True, None, False),
            ("requesterLinkId", "requesterLinkId", str, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("status", "status", codeableconcept.CodeableConcept, False, None, True),
            ("subject", "subject", ContractTermActionSubject, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractTermActionSubject(backboneelement.BackboneElement):
    """ 
    E
    n
    t
    i
    t
    y
    o
    f
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
    """
    
    resource_type = "ContractTermActionSubject"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ 
        E
        n
        t
        i
        t
        y
        o
        f
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        R
        o
        l
        e
        t
        y
        p
        e
        o
        f
        t
        h
        e
        a
        g
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermActionSubject, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermActionSubject, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermAsset(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    r
    a
    c
    t
    T
    e
    r
    m
    A
    s
    s
    e
    t
    L
    i
    s
    t
    .
    """
    
    resource_type = "ContractTermAsset"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer = None
        """ 
        R
        e
        s
        p
        o
        n
        s
        e
        t
        o
        a
        s
        s
        e
        t
        s
        .
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ 
        Q
        u
        a
        l
        i
        t
        y
        d
        e
        s
        c
        t
        i
        p
        t
        i
        o
        n
        o
        f
        a
        s
        s
        e
        t
        .
        Type `str`. """
        
        self.context = None
        """ 
        C
        i
        r
        c
        u
        m
        s
        t
        a
        n
        c
        e
        o
        f
        t
        h
        e
        a
        s
        s
        e
        t
        .
        List of `ContractTermAssetContext` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        a
        s
        s
        e
        t
        t
        e
        x
        t
        .
        List of `str` items. """
        
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
        o
        f
        t
        h
        e
        a
        s
        s
        e
        t
        .
        List of `Period` items (represented as `dict` in JSON). """
        
        self.periodType = None
        """ 
        A
        s
        s
        e
        t
        a
        v
        a
        i
        l
        a
        b
        i
        l
        i
        t
        y
        t
        y
        p
        e
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        K
        i
        n
        s
        h
        i
        p
        o
        f
        t
        h
        e
        a
        s
        s
        e
        t
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.scope = None
        """ 
        R
        a
        n
        g
        e
        o
        f
        a
        s
        s
        e
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
        """ 
        A
        s
        s
        e
        t
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
        n
        u
        m
        b
        e
        r
        s
        .
        List of `int` items. """
        
        self.subtype = None
        """ 
        A
        s
        s
        e
        t
        s
        u
        b
        -
        c
        a
        t
        e
        g
        o
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        A
        s
        s
        e
        t
        c
        l
        a
        u
        s
        e
        o
        r
        q
        u
        e
        s
        t
        i
        o
        n
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.type = None
        """ 
        A
        s
        s
        e
        t
        c
        a
        t
        e
        g
        o
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.typeReference = None
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
        e
        n
        t
        i
        t
        i
        e
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.usePeriod = None
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
        .
        List of `Period` items (represented as `dict` in JSON). """
        
        self.valuedItem = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        L
        i
        s
        t
        .
        List of `ContractTermAssetValuedItem` items (represented as `dict` in JSON). """
        
        super(ContractTermAsset, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAsset, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", ContractTermAssetContext, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("period", "period", period.Period, True, None, False),
            ("periodType", "periodType", codeableconcept.CodeableConcept, True, None, False),
            ("relationship", "relationship", coding.Coding, False, None, False),
            ("scope", "scope", codeableconcept.CodeableConcept, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("typeReference", "typeReference", fhirreference.FHIRReference, True, None, False),
            ("usePeriod", "usePeriod", period.Period, True, None, False),
            ("valuedItem", "valuedItem", ContractTermAssetValuedItem, True, None, False),
        ])
        return js


class ContractTermAssetContext(backboneelement.BackboneElement):
    """ 
    C
    i
    r
    c
    u
    m
    s
    t
    a
    n
    c
    e
    o
    f
    t
    h
    e
    a
    s
    s
    e
    t
    .
    """
    
    resource_type = "ContractTermAssetContext"
    
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
        d
        e
        a
        b
        l
        e
        a
        s
        s
        e
        t
        c
        o
        n
        t
        e
        x
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ 
        C
        r
        e
        a
        t
        o
        r
        ,
        c
        u
        s
        t
        o
        d
        i
        a
        n
        o
        r
        o
        w
        n
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        C
        o
        n
        t
        e
        x
        t
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
        .
        Type `str`. """
        
        super(ContractTermAssetContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetContext, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


class ContractTermAssetValuedItem(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    r
    a
    c
    t
    V
    a
    l
    u
    e
    d
    I
    t
    e
    m
    L
    i
    s
    t
    .
    """
    
    resource_type = "ContractTermAssetValuedItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.effectiveTime = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        E
        f
        f
        e
        c
        t
        i
        v
        e
        T
        i
        e
        m
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.entityCodeableConcept = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        T
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entityReference = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        T
        y
        p
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.factor = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        P
        r
        i
        c
        e
        S
        c
        a
        l
        i
        n
        g
        F
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.identifier = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        N
        u
        m
        b
        e
        r
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.linkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        s
        p
        e
        c
        i
        f
        i
        c
        i
        t
        e
        m
        .
        List of `str` items. """
        
        self.net = None
        """ 
        T
        o
        t
        a
        l
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        V
        a
        l
        u
        e
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.payment = None
        """ 
        T
        e
        r
        m
        s
        o
        f
        v
        a
        l
        u
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.paymentDate = None
        """ 
        W
        h
        e
        n
        p
        a
        y
        m
        e
        n
        t
        i
        s
        d
        u
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.points = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        D
        i
        f
        f
        i
        c
        u
        l
        t
        y
        S
        c
        a
        l
        i
        n
        g
        F
        a
        c
        t
        o
        r
        .
        Type `float`. """
        
        self.quantity = None
        """ 
        C
        o
        u
        n
        t
        o
        f
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ 
        W
        h
        o
        w
        i
        l
        l
        r
        e
        c
        e
        i
        v
        e
        p
        a
        y
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ 
        W
        h
        o
        w
        i
        l
        l
        m
        a
        k
        e
        p
        a
        y
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
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
        t
        e
        r
        m
        s
        .
        List of `int` items. """
        
        self.unitPrice = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        V
        a
        l
        u
        e
        d
        I
        t
        e
        m
        f
        e
        e
        ,
        c
        h
        a
        r
        g
        e
        ,
        o
        r
        c
        o
        s
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        super(ContractTermAssetValuedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermAssetValuedItem, self).elementProperties()
        js.extend([
            ("effectiveTime", "effectiveTime", fhirdate.FHIRDate, False, None, False),
            ("entityCodeableConcept", "entityCodeableConcept", codeableconcept.CodeableConcept, False, "entity", False),
            ("entityReference", "entityReference", fhirreference.FHIRReference, False, "entity", False),
            ("factor", "factor", float, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("net", "net", money.Money, False, None, False),
            ("payment", "payment", str, False, None, False),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
        ])
        return js


class ContractTermOffer(backboneelement.BackboneElement):
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
    t
    h
    e
    C
    o
    n
    t
    r
    a
    c
    t
    t
    e
    r
    m
    .
    
    
    T
    h
    e
    m
    a
    t
    t
    e
    r
    o
    f
    c
    o
    n
    c
    e
    r
    n
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
    t
    h
    i
    s
    p
    r
    o
    v
    i
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
    g
    r
    e
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "ContractTermOffer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.answer = None
        """ 
        R
        e
        s
        p
        o
        n
        s
        e
        t
        o
        o
        f
        f
        e
        r
        t
        e
        x
        t
        .
        List of `ContractTermOfferAnswer` items (represented as `dict` in JSON). """
        
        self.decision = None
        """ 
        A
        c
        c
        e
        p
        t
        i
        n
        g
        p
        a
        r
        t
        y
        c
        h
        o
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.decisionMode = None
        """ 
        H
        o
        w
        d
        e
        c
        i
        s
        i
        o
        n
        i
        s
        c
        o
        n
        v
        e
        y
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        O
        f
        f
        e
        r
        b
        u
        s
        i
        n
        e
        s
        s
        I
        D
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.linkId = None
        """ 
        P
        o
        i
        n
        t
        e
        r
        t
        o
        t
        e
        x
        t
        .
        List of `str` items. """
        
        self.party = None
        """ 
        O
        f
        f
        e
        r
        R
        e
        c
        i
        p
        i
        e
        n
        t
        .
        List of `ContractTermOfferParty` items (represented as `dict` in JSON). """
        
        self.securityLabelNumber = None
        """ 
        O
        f
        f
        e
        r
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
        n
        u
        m
        b
        e
        r
        s
        .
        List of `int` items. """
        
        self.text = None
        """ 
        H
        u
        m
        a
        n
        r
        e
        a
        d
        a
        b
        l
        e
        o
        f
        f
        e
        r
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.topic = None
        """ 
        N
        e
        g
        o
        t
        i
        a
        b
        l
        e
        o
        f
        f
        e
        r
        a
        s
        s
        e
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        C
        o
        n
        t
        r
        a
        c
        t
        O
        f
        f
        e
        r
        T
        y
        p
        e
        o
        r
        F
        o
        r
        m
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOffer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOffer, self).elementProperties()
        js.extend([
            ("answer", "answer", ContractTermOfferAnswer, True, None, False),
            ("decision", "decision", codeableconcept.CodeableConcept, False, None, False),
            ("decisionMode", "decisionMode", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("linkId", "linkId", str, True, None, False),
            ("party", "party", ContractTermOfferParty, True, None, False),
            ("securityLabelNumber", "securityLabelNumber", int, True, None, False),
            ("text", "text", str, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ContractTermOfferAnswer(backboneelement.BackboneElement):
    """ 
    R
    e
    s
    p
    o
    n
    s
    e
    t
    o
    o
    f
    f
    e
    r
    t
    e
    x
    t
    .
    """
    
    resource_type = "ContractTermOfferAnswer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueAttachment = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `bool`. """
        
        self.valueCoding = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueDate = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `float`. """
        
        self.valueInteger = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `int`. """
        
        self.valueQuantity = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueReference = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueString = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `str`. """
        
        self.valueTime = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueUri = None
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
        a
        n
        s
        w
        e
        r
        r
        e
        s
        p
        o
        n
        s
        e
        .
        Type `str`. """
        
        super(ContractTermOfferAnswer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferAnswer, self).elementProperties()
        js.extend([
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
        ])
        return js


class ContractTermOfferParty(backboneelement.BackboneElement):
    """ 
    O
    f
    f
    e
    r
    R
    e
    c
    i
    p
    i
    e
    n
    t
    .
    """
    
    resource_type = "ContractTermOfferParty"
    
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
        f
        e
        r
        e
        n
        c
        e
        d
        e
        n
        t
        i
        t
        y
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        P
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        e
        n
        g
        a
        g
        e
        m
        e
        n
        t
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ContractTermOfferParty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermOfferParty, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ContractTermSecurityLabel(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    t
    e
    c
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
    T
    e
    r
    m
    .
    
    
    S
    e
    c
    u
    r
    i
    t
    y
    l
    a
    b
    e
    l
    s
    t
    h
    a
    t
    p
    r
    o
    t
    e
    c
    t
    t
    h
    e
    h
    a
    n
    d
    l
    i
    n
    g
    o
    f
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
    t
    e
    r
    m
    a
    n
    d
    i
    t
    s
    e
    l
    e
    m
    e
    n
    t
    s
    ,
    w
    h
    i
    c
    h
    m
    a
    y
    b
    e
    s
    p
    e
    c
    i
    f
    i
    c
    a
    l
    l
    y
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
    .
    
    """
    
    resource_type = "ContractTermSecurityLabel"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ 
        A
        p
        p
        l
        i
        c
        a
        b
        l
        e
        P
        o
        l
        i
        c
        y
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.classification = None
        """ 
        C
        o
        n
        f
        i
        d
        e
        n
        t
        i
        a
        l
        i
        t
        y
        P
        r
        o
        t
        e
        c
        t
        i
        o
        n
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.control = None
        """ 
        H
        a
        n
        d
        l
        i
        n
        g
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
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.number = None
        """ 
        L
        i
        n
        k
        t
        o
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
        .
        List of `int` items. """
        
        super(ContractTermSecurityLabel, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContractTermSecurityLabel, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, True, None, False),
            ("classification", "classification", coding.Coding, False, None, True),
            ("control", "control", coding.Coding, True, None, False),
            ("number", "number", int, True, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
