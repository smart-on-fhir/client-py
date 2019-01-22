#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ResearchDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ResearchDefinition(domainresource.DomainResource):
    """ 
    A
    r
    e
    s
    e
    a
    r
    c
    h
    c
    o
    n
    t
    e
    x
    t
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
    .
    
    
    T
    h
    e
    R
    e
    s
    e
    a
    r
    c
    h
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
    r
    e
    s
    o
    u
    r
    c
    e
    d
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
    o
    n
    d
    i
    t
    i
    o
    n
    a
    l
    s
    t
    a
    t
    e
    (
    p
    o
    p
    u
    l
    a
    t
    i
    o
    n
    a
    n
    d
    a
    n
    y
    e
    x
    p
    o
    s
    u
    r
    e
    s
    b
    e
    i
    n
    g
    c
    o
    m
    p
    a
    r
    e
    d
    w
    i
    t
    h
    i
    n
    t
    h
    e
    p
    o
    p
    u
    l
    a
    t
    i
    o
    n
    )
    a
    n
    d
    o
    u
    t
    c
    o
    m
    e
    (
    i
    f
    s
    p
    e
    c
    i
    f
    i
    e
    d
    )
    t
    h
    a
    t
    t
    h
    e
    k
    n
    o
    w
    l
    e
    d
    g
    e
    (
    e
    v
    i
    d
    e
    n
    c
    e
    ,
    a
    s
    s
    e
    r
    t
    i
    o
    n
    ,
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
    )
    i
    s
    a
    b
    o
    u
    t
    .
    
    """
    
    resource_type = "ResearchDefinition"
    
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        
        self.comment = None
        """ 
        U
        s
        e
        d
        f
        o
        r
        f
        o
        o
        t
        n
        o
        t
        e
        s
        o
        r
        e
        x
        p
        l
        a
        n
        a
        t
        o
        r
        y
        n
        o
        t
        e
        s
        .
        List of `str` items. """
        
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        
        self.exposure = None
        """ 
        W
        h
        a
        t
        e
        x
        p
        o
        s
        u
        r
        e
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exposureAlternative = None
        """ 
        W
        h
        a
        t
        a
        l
        t
        e
        r
        n
        a
        t
        i
        v
        e
        e
        x
        p
        o
        s
        u
        r
        e
        s
        t
        a
        t
        e
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        
        self.lastReviewDate = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        r
        e
        s
        e
        a
        r
        c
        h
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
        R
        e
        s
        e
        a
        r
        c
        h
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
        List of `str` items. """
        
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        
        self.outcome = None
        """ 
        W
        h
        a
        t
        o
        u
        t
        c
        o
        m
        e
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.population = None
        """ 
        W
        h
        a
        t
        p
        o
        p
        u
        l
        a
        t
        i
        o
        n
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        
        self.shortTitle = None
        """ 
        T
        i
        t
        l
        e
        f
        o
        r
        u
        s
        e
        i
        n
        i
        n
        f
        o
        r
        m
        a
        l
        c
        o
        n
        t
        e
        x
        t
        s
        .
        Type `str`. """
        
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
        E
        .
        g
        .
        P
        a
        t
        i
        e
        n
        t
        ,
        P
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
        R
        e
        l
        a
        t
        e
        d
        P
        e
        r
        s
        o
        n
        ,
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
        ,
        L
        o
        c
        a
        t
        i
        o
        n
        ,
        D
        e
        v
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subjectReference = None
        """ 
        E
        .
        g
        .
        P
        a
        t
        i
        e
        n
        t
        ,
        P
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
        R
        e
        l
        a
        t
        e
        d
        P
        e
        r
        s
        o
        n
        ,
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
        ,
        L
        o
        c
        a
        t
        i
        o
        n
        ,
        D
        e
        v
        i
        c
        e
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
        R
        e
        s
        e
        a
        r
        c
        h
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        T
        h
        e
        c
        a
        t
        e
        g
        o
        r
        y
        o
        f
        t
        h
        e
        R
        e
        s
        e
        a
        r
        c
        h
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
        ,
        s
        u
        c
        h
        a
        s
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        R
        e
        s
        e
        a
        r
        c
        h
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
        r
        e
        s
        e
        a
        r
        c
        h
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
        
        super(ResearchDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ResearchDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("comment", "comment", str, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("exposure", "exposure", fhirreference.FHIRReference, False, None, False),
            ("exposureAlternative", "exposureAlternative", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("library", "library", str, True, None, False),
            ("name", "name", str, False, None, False),
            ("outcome", "outcome", fhirreference.FHIRReference, False, None, False),
            ("population", "population", fhirreference.FHIRReference, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("shortTitle", "shortTitle", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
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
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
