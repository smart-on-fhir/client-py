#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Communication) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Communication(domainresource.DomainResource):
    """ 
    A
    r
    e
    c
    o
    r
    d
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
    t
    r
    a
    n
    s
    m
    i
    t
    t
    e
    d
    f
    r
    o
    m
    a
    s
    e
    n
    d
    e
    r
    t
    o
    a
    r
    e
    c
    e
    i
    v
    e
    r
    .
    
    
    A
    n
    o
    c
    c
    u
    r
    r
    e
    n
    c
    e
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
    b
    e
    i
    n
    g
    t
    r
    a
    n
    s
    m
    i
    t
    t
    e
    d
    ;
    e
    .
    g
    .
    a
    n
    a
    l
    e
    r
    t
    t
    h
    a
    t
    w
    a
    s
    s
    e
    n
    t
    t
    o
    a
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
    r
    o
    v
    i
    d
    e
    r
    ,
    a
    p
    u
    b
    l
    i
    c
    h
    e
    a
    l
    t
    h
    a
    g
    e
    n
    c
    y
    t
    h
    a
    t
    w
    a
    s
    n
    o
    t
    i
    f
    i
    e
    d
    a
    b
    o
    u
    t
    a
    r
    e
    p
    o
    r
    t
    a
    b
    l
    e
    c
    o
    n
    d
    i
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "Communication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.about = None
        """ 
        R
        e
        s
        o
        u
        r
        c
        e
        s
        t
        h
        a
        t
        p
        e
        r
        t
        a
        i
        n
        t
        o
        t
        h
        i
        s
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ 
        R
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        M
        e
        s
        s
        a
        g
        e
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
        
        self.identifier = None
        """ 
        U
        n
        i
        q
        u
        e
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
        
        self.inResponseTo = None
        """ 
        R
        e
        p
        l
        y
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
        
        self.medium = None
        """ 
        A
        c
        h
        a
        n
        n
        e
        l
        o
        f
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        m
        a
        d
        e
        a
        b
        o
        u
        t
        t
        h
        e
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
        
        self.payload = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        p
        a
        y
        l
        o
        a
        d
        .
        List of `CommunicationPayload` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        u
        r
        g
        e
        n
        c
        y
        .
        Type `str`. """
        
        self.reasonCode = None
        """ 
        I
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
        m
        e
        s
        s
        a
        g
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        w
        a
        s
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
        d
        o
        n
        e
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.received = None
        """ 
        W
        h
        e
        n
        r
        e
        c
        e
        i
        v
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recipient = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        r
        e
        c
        i
        p
        i
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.sender = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        s
        e
        n
        d
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.sent = None
        """ 
        W
        h
        e
        n
        s
        e
        n
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        F
        o
        c
        u
        s
        o
        f
        m
        e
        s
        s
        a
        g
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.topic = None
        """ 
        D
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
        p
        u
        r
        p
        o
        s
        e
        /
        c
        o
        n
        t
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Communication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Communication, self).elementProperties()
        js.extend([
            ("about", "about", fhirreference.FHIRReference, True, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("inResponseTo", "inResponseTo", fhirreference.FHIRReference, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("payload", "payload", CommunicationPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("received", "received", fhirdate.FHIRDate, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("sent", "sent", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class CommunicationPayload(backboneelement.BackboneElement):
    """ 
    M
    e
    s
    s
    a
    g
    e
    p
    a
    y
    l
    o
    a
    d
    .
    
    
    T
    e
    x
    t
    ,
    a
    t
    t
    a
    c
    h
    m
    e
    n
    t
    (
    s
    )
    ,
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
    (
    s
    )
    t
    h
    a
    t
    w
    a
    s
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
    e
    d
    t
    o
    t
    h
    e
    r
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
    
    resource_type = "CommunicationPayload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        p
        a
        r
        t
        c
        o
        n
        t
        e
        n
        t
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        p
        a
        r
        t
        c
        o
        n
        t
        e
        n
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.contentString = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        p
        a
        r
        t
        c
        o
        n
        t
        e
        n
        t
        .
        Type `str`. """
        
        super(CommunicationPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
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
