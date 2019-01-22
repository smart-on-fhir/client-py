#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Library) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Library(domainresource.DomainResource):
    """ 
    R
    e
    p
    r
    e
    s
    e
    n
    t
    s
    a
    l
    i
    b
    r
    a
    r
    y
    o
    f
    q
    u
    a
    l
    i
    t
    y
    i
    m
    p
    r
    o
    v
    e
    m
    e
    n
    t
    c
    o
    m
    p
    o
    n
    e
    n
    t
    s
    .
    
    
    T
    h
    e
    L
    i
    b
    r
    a
    r
    y
    r
    e
    s
    o
    u
    r
    c
    e
    i
    s
    a
    g
    e
    n
    e
    r
    a
    l
    -
    p
    u
    r
    p
    o
    s
    e
    c
    o
    n
    t
    a
    i
    n
    e
    r
    f
    o
    r
    k
    n
    o
    w
    l
    e
    d
    g
    e
    a
    s
    s
    e
    t
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
    s
    .
    I
    t
    c
    a
    n
    b
    e
    u
    s
    e
    d
    t
    o
    d
    e
    s
    c
    r
    i
    b
    e
    a
    n
    d
    e
    x
    p
    o
    s
    e
    e
    x
    i
    s
    t
    i
    n
    g
    k
    n
    o
    w
    l
    e
    d
    g
    e
    a
    s
    s
    e
    t
    s
    s
    u
    c
    h
    a
    s
    l
    o
    g
    i
    c
    l
    i
    b
    r
    a
    r
    i
    e
    s
    a
    n
    d
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
    m
    o
    d
    e
    l
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
    s
    ,
    a
    s
    w
    e
    l
    l
    a
    s
    t
    o
    d
    e
    s
    c
    r
    i
    b
    e
    a
    c
    o
    l
    l
    e
    c
    t
    i
    o
    n
    o
    f
    k
    n
    o
    w
    l
    e
    d
    g
    e
    a
    s
    s
    e
    t
    s
    .
    
    """
    
    resource_type = "Library"
    
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
        l
        i
        b
        r
        a
        r
        y
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
        
        self.content = None
        """ 
        C
        o
        n
        t
        e
        n
        t
        s
        o
        f
        t
        h
        e
        l
        i
        b
        r
        a
        r
        y
        ,
        e
        i
        t
        h
        e
        r
        e
        m
        b
        e
        d
        d
        e
        d
        o
        r
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
        List of `Attachment` items (represented as `dict` in JSON). """
        
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
        
        self.dataRequirement = None
        """ 
        W
        h
        a
        t
        d
        a
        t
        a
        i
        s
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
        b
        y
        t
        h
        i
        s
        l
        i
        b
        r
        a
        r
        y
        .
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
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
        
        self.parameter = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        s
        d
        e
        f
        i
        n
        e
        d
        b
        y
        t
        h
        e
        l
        i
        b
        r
        a
        r
        y
        .
        List of `ParameterDefinition` items (represented as `dict` in JSON). """
        
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
        c
        o
        n
        t
        e
        n
        t
        i
        s
        f
        o
        c
        u
        s
        e
        d
        o
        n
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
        l
        i
        b
        r
        a
        r
        y
        c
        o
        n
        t
        e
        n
        t
        i
        s
        f
        o
        c
        u
        s
        e
        d
        o
        n
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
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
        
        self.type = None
        """ 
        l
        o
        g
        i
        c
        -
        l
        i
        b
        r
        a
        r
        y
        |
        m
        o
        d
        e
        l
        -
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
        |
        a
        s
        s
        e
        t
        -
        c
        o
        l
        l
        e
        c
        t
        i
        o
        n
        |
        m
        o
        d
        u
        l
        e
        -
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
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
        l
        i
        b
        r
        a
        r
        y
        .
        Type `str`. """
        
        super(Library, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Library, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("content", "content", attachment.Attachment, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("status", "status", str, False, None, True),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("subtitle", "subtitle", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("url", "url", str, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
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
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
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
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']
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
