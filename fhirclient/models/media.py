#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Media) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Media(domainresource.DomainResource):
    """ 
    A
    p
    h
    o
    t
    o
    ,
    v
    i
    d
    e
    o
    ,
    o
    r
    a
    u
    d
    i
    o
    r
    e
    c
    o
    r
    d
    i
    n
    g
    a
    c
    q
    u
    i
    r
    e
    d
    o
    r
    u
    s
    e
    d
    i
    n
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
    .
    T
    h
    e
    a
    c
    t
    u
    a
    l
    c
    o
    n
    t
    e
    n
    t
    m
    a
    y
    b
    e
    i
    n
    l
    i
    n
    e
    o
    r
    p
    r
    o
    v
    i
    d
    e
    d
    b
    y
    d
    i
    r
    e
    c
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
    .
    """
    
    resource_type = "Media"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ 
        P
        r
        o
        c
        e
        d
        u
        r
        e
        t
        h
        a
        t
        c
        a
        u
        s
        e
        d
        t
        h
        i
        s
        m
        e
        d
        i
        a
        t
        o
        b
        e
        c
        r
        e
        a
        t
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ 
        O
        b
        s
        e
        r
        v
        e
        d
        b
        o
        d
        y
        p
        a
        r
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ 
        A
        c
        t
        u
        a
        l
        M
        e
        d
        i
        a
        -
        r
        e
        f
        e
        r
        e
        n
        c
        e
        o
        r
        d
        a
        t
        a
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.createdDateTime = None
        """ 
        W
        h
        e
        n
        M
        e
        d
        i
        a
        w
        a
        s
        c
        o
        l
        l
        e
        c
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.createdPeriod = None
        """ 
        W
        h
        e
        n
        M
        e
        d
        i
        a
        w
        a
        s
        c
        o
        l
        l
        e
        c
        t
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.device = None
        """ 
        O
        b
        s
        e
        r
        v
        i
        n
        g
        D
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deviceName = None
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
        d
        e
        v
        i
        c
        e
        /
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
        Type `str`. """
        
        self.duration = None
        """ 
        L
        e
        n
        g
        t
        h
        i
        n
        s
        e
        c
        o
        n
        d
        s
        (
        a
        u
        d
        i
        o
        /
        v
        i
        d
        e
        o
        )
        .
        Type `float`. """
        
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
        m
        e
        d
        i
        a
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.frames = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        f
        r
        a
        m
        e
        s
        i
        f
        >
        1
        (
        p
        h
        o
        t
        o
        )
        .
        Type `int`. """
        
        self.height = None
        """ 
        H
        e
        i
        g
        h
        t
        o
        f
        t
        h
        e
        i
        m
        a
        g
        e
        i
        n
        p
        i
        x
        e
        l
        s
        (
        p
        h
        o
        t
        o
        /
        v
        i
        d
        e
        o
        )
        .
        Type `int`. """
        
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
        (
        s
        )
        f
        o
        r
        t
        h
        e
        i
        m
        a
        g
        e
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issued = None
        """ 
        D
        a
        t
        e
        /
        T
        i
        m
        e
        t
        h
        i
        s
        v
        e
        r
        s
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
        v
        a
        i
        l
        a
        b
        l
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.modality = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        a
        c
        q
        u
        i
        s
        i
        t
        i
        o
        n
        e
        q
        u
        i
        p
        m
        e
        n
        t
        /
        p
        r
        o
        c
        e
        s
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        m
        e
        d
        i
        a
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.operator = None
        """ 
        T
        h
        e
        p
        e
        r
        s
        o
        n
        w
        h
        o
        g
        e
        n
        e
        r
        a
        t
        e
        d
        t
        h
        e
        i
        m
        a
        g
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        e
        v
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        w
        a
        s
        e
        v
        e
        n
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
        ?
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        /
        W
        h
        a
        t
        t
        h
        i
        s
        M
        e
        d
        i
        a
        i
        s
        a
        r
        e
        c
        o
        r
        d
        o
        f
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
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
        m
        e
        d
        i
        a
        a
        s
        i
        m
        a
        g
        e
        ,
        v
        i
        d
        e
        o
        ,
        o
        r
        a
        u
        d
        i
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.view = None
        """ 
        I
        m
        a
        g
        i
        n
        g
        v
        i
        e
        w
        ,
        e
        .
        g
        .
        L
        a
        t
        e
        r
        a
        l
        o
        r
        A
        n
        t
        e
        r
        o
        -
        p
        o
        s
        t
        e
        r
        i
        o
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.width = None
        """ 
        W
        i
        d
        t
        h
        o
        f
        t
        h
        e
        i
        m
        a
        g
        e
        i
        n
        p
        i
        x
        e
        l
        s
        (
        p
        h
        o
        t
        o
        /
        v
        i
        d
        e
        o
        )
        .
        Type `int`. """
        
        super(Media, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("content", "content", attachment.Attachment, False, None, True),
            ("createdDateTime", "createdDateTime", fhirdate.FHIRDate, False, "created", False),
            ("createdPeriod", "createdPeriod", period.Period, False, "created", False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("deviceName", "deviceName", str, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("height", "height", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("modality", "modality", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("operator", "operator", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("view", "view", codeableconcept.CodeableConcept, False, None, False),
            ("width", "width", int, False, None, False),
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
