#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DocumentReference) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DocumentReference(domainresource.DomainResource):
    """ 
    A
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
    a
    d
    o
    c
    u
    m
    e
    n
    t
    .
    
    
    A
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
    a
    d
    o
    c
    u
    m
    e
    n
    t
    o
    f
    a
    n
    y
    k
    i
    n
    d
    f
    o
    r
    a
    n
    y
    p
    u
    r
    p
    o
    s
    e
    .
    P
    r
    o
    v
    i
    d
    e
    s
    m
    e
    t
    a
    d
    a
    t
    a
    a
    b
    o
    u
    t
    t
    h
    e
    d
    o
    c
    u
    m
    e
    n
    t
    s
    o
    t
    h
    a
    t
    t
    h
    e
    d
    o
    c
    u
    m
    e
    n
    t
    c
    a
    n
    b
    e
    d
    i
    s
    c
    o
    v
    e
    r
    e
    d
    a
    n
    d
    m
    a
    n
    a
    g
    e
    d
    .
    T
    h
    e
    s
    c
    o
    p
    e
    o
    f
    a
    d
    o
    c
    u
    m
    e
    n
    t
    i
    s
    a
    n
    y
    s
    e
    r
    a
    l
    i
    z
    e
    d
    o
    b
    j
    e
    c
    t
    w
    i
    t
    h
    a
    m
    i
    m
    e
    -
    t
    y
    p
    e
    ,
    s
    o
    i
    n
    c
    l
    u
    d
    e
    s
    f
    o
    r
    m
    a
    l
    p
    a
    t
    i
    e
    n
    t
    c
    e
    n
    t
    r
    i
    c
    d
    o
    c
    u
    m
    e
    n
    t
    s
    (
    C
    D
    A
    )
    ,
    c
    l
    i
    i
    c
    a
    l
    n
    o
    t
    e
    s
    ,
    s
    c
    a
    n
    n
    e
    d
    p
    a
    p
    e
    r
    ,
    a
    n
    d
    n
    o
    n
    -
    p
    a
    t
    i
    e
    n
    t
    s
    p
    e
    c
    i
    f
    i
    c
    d
    o
    c
    u
    m
    e
    n
    t
    s
    l
    i
    k
    e
    p
    o
    l
    i
    c
    y
    t
    e
    x
    t
    .
    
    """
    
    resource_type = "DocumentReference"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authenticator = None
        """ 
        W
        h
        o
        /
        w
        h
        a
        t
        a
        u
        t
        h
        e
        n
        t
        i
        c
        a
        t
        e
        d
        t
        h
        e
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.author = None
        """ 
        W
        h
        o
        a
        n
        d
        /
        o
        r
        w
        h
        a
        t
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
        d
        o
        c
        u
        m
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        C
        a
        t
        e
        g
        o
        r
        i
        z
        a
        t
        i
        o
        n
        o
        f
        d
        o
        c
        u
        m
        e
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.content = None
        """ 
        D
        o
        c
        u
        m
        e
        n
        t
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
        List of `DocumentReferenceContent` items (represented as `dict` in JSON). """
        
        self.context = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        c
        o
        n
        t
        e
        x
        t
        o
        f
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `DocumentReferenceContext` (represented as `dict` in JSON). """
        
        self.custodian = None
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
        w
        h
        i
        c
        h
        m
        a
        i
        n
        t
        a
        i
        n
        s
        t
        h
        e
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        W
        h
        e
        n
        t
        h
        i
        s
        d
        o
        c
        u
        m
        e
        n
        t
        r
        e
        f
        e
        r
        e
        n
        c
        e
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
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ 
        H
        u
        m
        a
        n
        -
        r
        e
        a
        d
        a
        b
        l
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
        .
        Type `str`. """
        
        self.docStatus = None
        """ 
        p
        r
        e
        l
        i
        m
        i
        n
        a
        r
        y
        |
        f
        i
        n
        a
        l
        |
        a
        p
        p
        e
        n
        d
        e
        d
        |
        a
        m
        e
        n
        d
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
        Type `str`. """
        
        self.identifier = None
        """ 
        O
        t
        h
        e
        r
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
        s
        f
        o
        r
        t
        h
        e
        d
        o
        c
        u
        m
        e
        n
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.masterIdentifier = None
        """ 
        M
        a
        s
        t
        e
        r
        V
        e
        r
        s
        i
        o
        n
        S
        p
        e
        c
        i
        f
        i
        c
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
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.relatesTo = None
        """ 
        R
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        s
        t
        o
        o
        t
        h
        e
        r
        d
        o
        c
        u
        m
        e
        n
        t
        s
        .
        List of `DocumentReferenceRelatesTo` items (represented as `dict` in JSON). """
        
        self.securityLabel = None
        """ 
        D
        o
        c
        u
        m
        e
        n
        t
        s
        e
        c
        u
        r
        i
        t
        y
        -
        t
        a
        g
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        c
        u
        r
        r
        e
        n
        t
        |
        s
        u
        p
        e
        r
        s
        e
        d
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
        Type `str`. """
        
        self.subject = None
        """ 
        W
        h
        o
        /
        w
        h
        a
        t
        i
        s
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
        o
        f
        t
        h
        e
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        K
        i
        n
        d
        o
        f
        d
        o
        c
        u
        m
        e
        n
        t
        (
        L
        O
        I
        N
        C
        i
        f
        p
        o
        s
        s
        i
        b
        l
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentReference, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReference, self).elementProperties()
        js.extend([
            ("authenticator", "authenticator", fhirreference.FHIRReference, False, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("content", "content", DocumentReferenceContent, True, None, True),
            ("context", "context", DocumentReferenceContext, False, None, False),
            ("custodian", "custodian", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("docStatus", "docStatus", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("relatesTo", "relatesTo", DocumentReferenceRelatesTo, True, None, False),
            ("securityLabel", "securityLabel", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class DocumentReferenceContent(backboneelement.BackboneElement):
    """ 
    D
    o
    c
    u
    m
    e
    n
    t
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
    
    
    T
    h
    e
    d
    o
    c
    u
    m
    e
    n
    t
    a
    n
    d
    f
    o
    r
    m
    a
    t
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
    m
    u
    l
    t
    i
    p
    l
    e
    c
    o
    n
    t
    e
    n
    t
    e
    l
    e
    m
    e
    n
    t
    r
    e
    p
    e
    t
    i
    t
    i
    o
    n
    s
    ,
    e
    a
    c
    h
    w
    i
    t
    h
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
    f
    o
    r
    m
    a
    t
    .
    
    """
    
    resource_type = "DocumentReferenceContent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment = None
        """ 
        W
        h
        e
        r
        e
        t
        o
        a
        c
        c
        e
        s
        s
        t
        h
        e
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.format = None
        """ 
        F
        o
        r
        m
        a
        t
        /
        c
        o
        n
        t
        e
        n
        t
        r
        u
        l
        e
        s
        f
        o
        r
        t
        h
        e
        d
        o
        c
        u
        m
        e
        n
        t
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContent, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, True),
            ("format", "format", coding.Coding, False, None, False),
        ])
        return js


class DocumentReferenceContext(backboneelement.BackboneElement):
    """ 
    C
    l
    i
    n
    i
    c
    a
    l
    c
    o
    n
    t
    e
    x
    t
    o
    f
    d
    o
    c
    u
    m
    e
    n
    t
    .
    
    
    T
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
    c
    o
    n
    t
    e
    x
    t
    i
    n
    w
    h
    i
    c
    h
    t
    h
    e
    d
    o
    c
    u
    m
    e
    n
    t
    w
    a
    s
    p
    r
    e
    p
    a
    r
    e
    d
    .
    
    """
    
    resource_type = "DocumentReferenceContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.encounter = None
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
        d
        o
        c
        u
        m
        e
        n
        t
        c
        o
        n
        t
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.event = None
        """ 
        M
        a
        i
        n
        c
        l
        i
        n
        i
        c
        a
        l
        a
        c
        t
        s
        d
        o
        c
        u
        m
        e
        n
        t
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.facilityType = None
        """ 
        K
        i
        n
        d
        o
        f
        f
        a
        c
        i
        l
        i
        t
        y
        w
        h
        e
        r
        e
        p
        a
        t
        i
        e
        n
        t
        w
        a
        s
        s
        e
        e
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        T
        i
        m
        e
        o
        f
        s
        e
        r
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
        b
        e
        i
        n
        g
        d
        o
        c
        u
        m
        e
        n
        t
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.practiceSetting = None
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
        w
        h
        e
        r
        e
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
        (
        e
        .
        g
        .
        c
        l
        i
        n
        i
        c
        a
        l
        s
        p
        e
        c
        i
        a
        l
        t
        y
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.related = None
        """ 
        R
        e
        l
        a
        t
        e
        d
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
        s
        o
        r
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sourcePatientInfo = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        d
        e
        m
        o
        g
        r
        a
        p
        h
        i
        c
        s
        f
        r
        o
        m
        s
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DocumentReferenceContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReferenceContext, self).elementProperties()
        js.extend([
            ("encounter", "encounter", fhirreference.FHIRReference, True, None, False),
            ("event", "event", codeableconcept.CodeableConcept, True, None, False),
            ("facilityType", "facilityType", codeableconcept.CodeableConcept, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("practiceSetting", "practiceSetting", codeableconcept.CodeableConcept, False, None, False),
            ("related", "related", fhirreference.FHIRReference, True, None, False),
            ("sourcePatientInfo", "sourcePatientInfo", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class DocumentReferenceRelatesTo(backboneelement.BackboneElement):
    """ 
    R
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    s
    t
    o
    o
    t
    h
    e
    r
    d
    o
    c
    u
    m
    e
    n
    t
    s
    .
    
    
    R
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    s
    t
    h
    a
    t
    t
    h
    i
    s
    d
    o
    c
    u
    m
    e
    n
    t
    h
    a
    s
    w
    i
    t
    h
    o
    t
    h
    e
    r
    d
    o
    c
    u
    m
    e
    n
    t
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
    h
    a
    t
    a
    l
    r
    e
    a
    d
    y
    e
    x
    i
    s
    t
    .
    
    """
    
    resource_type = "DocumentReferenceRelatesTo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        r
        e
        p
        l
        a
        c
        e
        s
        |
        t
        r
        a
        n
        s
        f
        o
        r
        m
        s
        |
        s
        i
        g
        n
        s
        |
        a
        p
        p
        e
        n
        d
        s
        .
        Type `str`. """
        
        self.target = None
        """ 
        T
        a
        r
        g
        e
        t
        o
        f
        t
        h
        e
        r
        e
        l
        a
        t
        i
        o
        n
        s
        h
        i
        p
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DocumentReferenceRelatesTo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentReferenceRelatesTo, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
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
