#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RelatedPerson) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class RelatedPerson(domainresource.DomainResource):
    """ 
    A
    p
    e
    r
    s
    o
    n
    t
    h
    a
    t
    i
    s
    r
    e
    l
    a
    t
    e
    d
    t
    o
    a
    p
    a
    t
    i
    e
    n
    t
    ,
    b
    u
    t
    w
    h
    o
    i
    s
    n
    o
    t
    a
    d
    i
    r
    e
    c
    t
    t
    a
    r
    g
    e
    t
    o
    f
    c
    a
    r
    e
    .
    
    
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
    a
    b
    o
    u
    t
    a
    p
    e
    r
    s
    o
    n
    t
    h
    a
    t
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
    i
    n
    t
    h
    e
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
    t
    i
    e
    n
    t
    ,
    b
    u
    t
    w
    h
    o
    i
    s
    n
    o
    t
    t
    h
    e
    t
    a
    r
    g
    e
    t
    o
    f
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
    ,
    n
    o
    r
    h
    a
    s
    a
    f
    o
    r
    m
    a
    l
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
    i
    n
    t
    h
    e
    c
    a
    r
    e
    p
    r
    o
    c
    e
    s
    s
    .
    
    """
    
    resource_type = "RelatedPerson"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        i
        s
        r
        e
        l
        a
        t
        e
        d
        p
        e
        r
        s
        o
        n
        '
        s
        r
        e
        c
        o
        r
        d
        i
        s
        i
        n
        a
        c
        t
        i
        v
        e
        u
        s
        e
        .
        Type `bool`. """
        
        self.address = None
        """ 
        A
        d
        d
        r
        e
        s
        s
        w
        h
        e
        r
        e
        t
        h
        e
        r
        e
        l
        a
        t
        e
        d
        p
        e
        r
        s
        o
        n
        c
        a
        n
        b
        e
        c
        o
        n
        t
        a
        c
        t
        e
        d
        o
        r
        v
        i
        s
        i
        t
        e
        d
        .
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        o
        n
        w
        h
        i
        c
        h
        t
        h
        e
        r
        e
        l
        a
        t
        e
        d
        p
        e
        r
        s
        o
        n
        w
        a
        s
        b
        o
        r
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.communication = None
        """ 
        A
        l
        a
        n
        g
        u
        a
        g
        e
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
        u
        s
        e
        d
        t
        o
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
        w
        i
        t
        h
        a
        b
        o
        u
        t
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
        '
        s
        h
        e
        a
        l
        t
        h
        .
        List of `RelatedPersonCommunication` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ 
        m
        a
        l
        e
        |
        f
        e
        m
        a
        l
        e
        |
        o
        t
        h
        e
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
        
        self.identifier = None
        """ 
        A
        h
        u
        m
        a
        n
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
        p
        e
        r
        s
        o
        n
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        A
        n
        a
        m
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
        t
        h
        e
        p
        e
        r
        s
        o
        n
        .
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        T
        h
        e
        p
        a
        t
        i
        e
        n
        t
        t
        h
        i
        s
        p
        e
        r
        s
        o
        n
        i
        s
        r
        e
        l
        a
        t
        e
        d
        t
        o
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        P
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
        t
        h
        a
        t
        t
        h
        i
        s
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
        i
        s
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
        v
        a
        l
        i
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.photo = None
        """ 
        I
        m
        a
        g
        e
        o
        f
        t
        h
        e
        p
        e
        r
        s
        o
        n
        .
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        T
        h
        e
        n
        a
        t
        u
        r
        e
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ 
        A
        c
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
        f
        o
        r
        t
        h
        e
        p
        e
        r
        s
        o
        n
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(RelatedPerson, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("communication", "communication", RelatedPersonCommunication, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class RelatedPersonCommunication(backboneelement.BackboneElement):
    """ 
    A
    l
    a
    n
    g
    u
    a
    g
    e
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
    u
    s
    e
    d
    t
    o
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
    w
    i
    t
    h
    a
    b
    o
    u
    t
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
    '
    s
    h
    e
    a
    l
    t
    h
    .
    """
    
    resource_type = "RelatedPersonCommunication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ 
        T
        h
        e
        l
        a
        n
        g
        u
        a
        g
        e
        w
        h
        i
        c
        h
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
        a
        b
        o
        u
        t
        h
        i
        s
        o
        r
        h
        e
        r
        h
        e
        a
        l
        t
        h
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.preferred = None
        """ 
        L
        a
        n
        g
        u
        a
        g
        e
        p
        r
        e
        f
        e
        r
        e
        n
        c
        e
        i
        n
        d
        i
        c
        a
        t
        o
        r
        .
        Type `bool`. """
        
        super(RelatedPersonCommunication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedPersonCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
