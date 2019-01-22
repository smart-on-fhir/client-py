#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Practitioner) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Practitioner(domainresource.DomainResource):
    """ 
    A
    p
    e
    r
    s
    o
    n
    w
    i
    t
    h
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
    p
    r
    o
    v
    i
    s
    i
    o
    n
    i
    n
    g
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
    o
    r
    r
    e
    l
    a
    t
    e
    d
    s
    e
    r
    v
    i
    c
    e
    s
    .
    
    
    A
    p
    e
    r
    s
    o
    n
    w
    h
    o
    i
    s
    d
    i
    r
    e
    c
    t
    l
    y
    o
    r
    i
    n
    d
    i
    r
    e
    c
    t
    l
    y
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
    p
    r
    o
    v
    i
    s
    i
    o
    n
    i
    n
    g
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
    .
    
    """
    
    resource_type = "Practitioner"
    
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
        p
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
        (
        e
        s
        )
        o
        f
        t
        h
        e
        p
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
        t
        h
        a
        t
        a
        r
        e
        n
        o
        t
        r
        o
        l
        e
        s
        p
        e
        c
        i
        f
        i
        c
        (
        t
        y
        p
        i
        c
        a
        l
        l
        y
        h
        o
        m
        e
        a
        d
        d
        r
        e
        s
        s
        )
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
        p
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
        t
        h
        e
        p
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
        c
        a
        n
        u
        s
        e
        i
        n
        p
        a
        t
        i
        e
        n
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        e
        p
        e
        r
        s
        o
        n
        a
        s
        t
        h
        i
        s
        a
        g
        e
        n
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        T
        h
        e
        n
        a
        m
        e
        (
        s
        )
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
        .
        List of `HumanName` items (represented as `dict` in JSON). """
        
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
        
        self.qualification = None
        """ 
        C
        e
        r
        t
        i
        f
        i
        c
        a
        t
        i
        o
        n
        ,
        l
        i
        c
        e
        n
        s
        e
        s
        ,
        o
        r
        t
        r
        a
        i
        n
        i
        n
        g
        p
        e
        r
        t
        a
        i
        n
        i
        n
        g
        t
        o
        t
        h
        e
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
        c
        a
        r
        e
        .
        List of `PractitionerQualification` items (represented as `dict` in JSON). """
        
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
        (
        t
        h
        a
        t
        a
        p
        p
        l
        y
        t
        o
        a
        l
        l
        r
        o
        l
        e
        s
        )
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Practitioner, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Practitioner, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("qualification", "qualification", PractitionerQualification, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PractitionerQualification(backboneelement.BackboneElement):
    """ 
    C
    e
    r
    t
    i
    f
    i
    c
    a
    t
    i
    o
    n
    ,
    l
    i
    c
    e
    n
    s
    e
    s
    ,
    o
    r
    t
    r
    a
    i
    n
    i
    n
    g
    p
    e
    r
    t
    a
    i
    n
    i
    n
    g
    t
    o
    t
    h
    e
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
    c
    a
    r
    e
    .
    
    
    T
    h
    e
    o
    f
    f
    i
    c
    i
    a
    l
    c
    e
    r
    t
    i
    f
    i
    c
    a
    t
    i
    o
    n
    s
    ,
    t
    r
    a
    i
    n
    i
    n
    g
    ,
    a
    n
    d
    l
    i
    c
    e
    n
    s
    e
    s
    t
    h
    a
    t
    a
    u
    t
    h
    o
    r
    i
    z
    e
    o
    r
    o
    t
    h
    e
    r
    w
    i
    s
    e
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
    e
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
    c
    a
    r
    e
    b
    y
    t
    h
    e
    p
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
    .
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    ,
    a
    m
    e
    d
    i
    c
    a
    l
    l
    i
    c
    e
    n
    s
    e
    i
    s
    s
    u
    e
    d
    b
    y
    a
    m
    e
    d
    i
    c
    a
    l
    b
    o
    a
    r
    d
    a
    u
    t
    h
    o
    r
    i
    z
    i
    n
    g
    t
    h
    e
    p
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
    t
    o
    p
    r
    a
    c
    t
    i
    c
    e
    m
    e
    d
    i
    c
    i
    n
    e
    w
    i
    t
    h
    i
    n
    a
    c
    e
    r
    t
    i
    a
    n
    l
    o
    c
    a
    l
    i
    t
    y
    .
    
    """
    
    resource_type = "PractitionerQualification"
    
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
        e
        q
        u
        a
        l
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
        
        self.identifier = None
        """ 
        A
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
        q
        u
        a
        l
        i
        f
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
        t
        h
        e
        p
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issuer = None
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
        t
        h
        a
        t
        r
        e
        g
        u
        l
        a
        t
        e
        s
        a
        n
        d
        i
        s
        s
        u
        e
        s
        t
        h
        e
        q
        u
        a
        l
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        P
        e
        r
        i
        o
        d
        d
        u
        r
        i
        n
        g
        w
        h
        i
        c
        h
        t
        h
        e
        q
        u
        a
        l
        i
        f
        i
        c
        a
        t
        i
        o
        n
        i
        s
        v
        a
        l
        i
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(PractitionerQualification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerQualification, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
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
