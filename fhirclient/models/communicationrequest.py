#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CommunicationRequest(domainresource.DomainResource):
    """ 
    A
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
    b
    e
    s
    e
    n
    t
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
    r
    e
    q
    u
    e
    s
    t
    t
    o
    c
    o
    n
    v
    e
    y
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
    ;
    e
    .
    g
    .
    t
    h
    e
    C
    D
    S
    s
    y
    s
    t
    e
    m
    p
    r
    o
    p
    o
    s
    e
    s
    t
    h
    a
    t
    a
    n
    a
    l
    e
    r
    t
    b
    e
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
    t
    h
    e
    C
    D
    S
    s
    y
    s
    t
    e
    m
    p
    r
    o
    p
    o
    s
    e
    s
    t
    h
    a
    t
    t
    h
    e
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
    b
    e
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
    
    resource_type = "CommunicationRequest"
    
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
        r
        e
        q
        u
        e
        s
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        t
        r
        a
        n
        s
        i
        t
        i
        o
        n
        e
        d
        t
        o
        b
        e
        i
        n
        g
        a
        c
        t
        i
        o
        n
        a
        b
        l
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        p
        l
        a
        n
        o
        r
        p
        r
        o
        p
        o
        s
        a
        l
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
        r
        e
        q
        u
        e
        s
        t
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ 
        W
        h
        e
        n
        s
        c
        h
        e
        d
        u
        l
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ 
        W
        h
        e
        n
        s
        c
        h
        e
        d
        u
        l
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
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
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """
        
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
        W
        h
        y
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
        n
        e
        e
        d
        e
        d
        ?
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
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
        n
        e
        e
        d
        e
        d
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        
        self.replaces = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        (
        s
        )
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
        r
        e
        q
        u
        e
        s
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
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
        r
        e
        q
        u
        e
        s
        t
        i
        n
        g
        s
        e
        r
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        super(CommunicationRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("about", "about", fhirreference.FHIRReference, True, None, False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("payload", "payload", CommunicationRequestPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class CommunicationRequestPayload(backboneelement.BackboneElement):
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
    o
    b
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
    
    resource_type = "CommunicationRequestPayload"
    
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
        
        super(CommunicationRequestPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
