#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DocumentManifest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DocumentManifest(domainresource.DomainResource):
    """ 
    A
    l
    i
    s
    t
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
    s
    a
    s
    e
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
    s
    .
    
    
    A
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
    d
    o
    c
    u
    m
    e
    n
    t
    s
    c
    o
    m
    p
    i
    l
    e
    d
    f
    o
    r
    a
    p
    u
    r
    p
    o
    s
    e
    t
    o
    g
    e
    t
    h
    e
    r
    w
    i
    t
    h
    m
    e
    t
    a
    d
    a
    t
    a
    t
    h
    a
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
    t
    h
    e
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
    .
    
    """
    
    resource_type = "DocumentManifest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        D
        o
        c
        u
        m
        e
        n
        t
        M
        a
        n
        i
        f
        e
        s
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.content = None
        """ 
        I
        t
        e
        m
        s
        i
        n
        m
        a
        n
        i
        f
        e
        s
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.created = None
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
        m
        a
        n
        i
        f
        e
        s
        t
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
        (
        t
        i
        t
        l
        e
        )
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
        m
        a
        n
        i
        f
        e
        s
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.masterIdentifier = None
        """ 
        U
        n
        i
        q
        u
        e
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
        e
        s
        e
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
        s
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        t
        o
        g
        e
        t
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
        t
        h
        i
        s
        s
        e
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
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.related = None
        """ 
        R
        e
        l
        a
        t
        e
        d
        t
        h
        i
        n
        g
        s
        .
        List of `DocumentManifestRelated` items (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        T
        h
        e
        s
        o
        u
        r
        c
        e
        s
        y
        s
        t
        e
        m
        /
        a
        p
        p
        l
        i
        c
        a
        t
        i
        o
        n
        /
        s
        o
        f
        t
        w
        a
        r
        e
        .
        Type `str`. """
        
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
        T
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
        s
        e
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
        s
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
        s
        e
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DocumentManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentManifest, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("content", "content", fhirreference.FHIRReference, True, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("masterIdentifier", "masterIdentifier", identifier.Identifier, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("related", "related", DocumentManifestRelated, True, None, False),
            ("source", "source", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class DocumentManifestRelated(backboneelement.BackboneElement):
    """ 
    R
    e
    l
    a
    t
    e
    d
    t
    h
    i
    n
    g
    s
    .
    
    
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
    t
    h
    e
    D
    o
    c
    u
    m
    e
    n
    t
    M
    a
    n
    i
    f
    e
    s
    t
    .
    
    """
    
    resource_type = "DocumentManifestRelated"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        s
        o
        f
        t
        h
        i
        n
        g
        s
        t
        h
        a
        t
        a
        r
        e
        r
        e
        l
        a
        t
        e
        d
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.ref = None
        """ 
        R
        e
        l
        a
        t
        e
        d
        R
        e
        s
        o
        u
        r
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(DocumentManifestRelated, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DocumentManifestRelated, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("ref", "ref", fhirreference.FHIRReference, False, None, False),
        ])
        return js


import sys
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
