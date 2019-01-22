#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Organization) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Organization(domainresource.DomainResource):
    """ 
    A
    g
    r
    o
    u
    p
    i
    n
    g
    o
    f
    p
    e
    o
    p
    l
    e
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
    s
    w
    i
    t
    h
    a
    c
    o
    m
    m
    o
    n
    p
    u
    r
    p
    o
    s
    e
    .
    
    
    A
    f
    o
    r
    m
    a
    l
    l
    y
    o
    r
    i
    n
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
    g
    n
    i
    z
    e
    d
    g
    r
    o
    u
    p
    i
    n
    g
    o
    f
    p
    e
    o
    p
    l
    e
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
    s
    f
    o
    r
    m
    e
    d
    f
    o
    r
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
    o
    f
    a
    c
    h
    i
    e
    v
    i
    n
    g
    s
    o
    m
    e
    f
    o
    r
    m
    o
    f
    c
    o
    l
    l
    e
    c
    t
    i
    v
    e
    a
    c
    t
    i
    o
    n
    .
    I
    n
    c
    l
    u
    d
    e
    s
    c
    o
    m
    p
    a
    n
    i
    e
    s
    ,
    i
    n
    s
    t
    i
    t
    u
    t
    i
    o
    n
    s
    ,
    c
    o
    r
    p
    o
    r
    a
    t
    i
    o
    n
    s
    ,
    d
    e
    p
    a
    r
    t
    m
    e
    n
    t
    s
    ,
    c
    o
    m
    m
    u
    n
    i
    t
    y
    g
    r
    o
    u
    p
    s
    ,
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
    p
    r
    a
    c
    t
    i
    c
    e
    g
    r
    o
    u
    p
    s
    ,
    p
    a
    y
    e
    r
    /
    i
    n
    s
    u
    r
    e
    r
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "Organization"
    
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
        e
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
        s
        t
        i
        l
        l
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
        n
        a
        d
        d
        r
        e
        s
        s
        f
        o
        r
        t
        h
        e
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
        .
        List of `Address` items (represented as `dict` in JSON). """
        
        self.alias = None
        """ 
        A
        l
        i
        s
        t
        o
        f
        a
        l
        t
        e
        r
        n
        a
        t
        e
        n
        a
        m
        e
        s
        t
        h
        a
        t
        t
        h
        e
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
        i
        s
        k
        n
        o
        w
        n
        a
        s
        ,
        o
        r
        w
        a
        s
        k
        n
        o
        w
        n
        a
        s
        i
        n
        t
        h
        e
        p
        a
        s
        t
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
        f
        o
        r
        t
        h
        e
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
        f
        o
        r
        a
        c
        e
        r
        t
        a
        i
        n
        p
        u
        r
        p
        o
        s
        e
        .
        List of `OrganizationContact` items (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ 
        T
        e
        c
        h
        n
        i
        c
        a
        l
        e
        n
        d
        p
        o
        i
        n
        t
        s
        p
        r
        o
        v
        i
        d
        i
        n
        g
        a
        c
        c
        e
        s
        s
        t
        o
        s
        e
        r
        v
        i
        c
        e
        s
        o
        p
        e
        r
        a
        t
        e
        d
        f
        o
        r
        t
        h
        e
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        s
        t
        h
        i
        s
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
        a
        c
        r
        o
        s
        s
        m
        u
        l
        t
        i
        p
        l
        e
        s
        y
        s
        t
        e
        m
        s
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        N
        a
        m
        e
        u
        s
        e
        d
        f
        o
        r
        t
        h
        e
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
        .
        Type `str`. """
        
        self.partOf = None
        """ 
        T
        h
        e
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
        f
        w
        h
        i
        c
        h
        t
        h
        i
        s
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
        f
        o
        r
        m
        s
        a
        p
        a
        r
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        K
        i
        n
        d
        o
        f
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Organization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Organization, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("alias", "alias", str, True, None, False),
            ("contact", "contact", OrganizationContact, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class OrganizationContact(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    a
    c
    t
    f
    o
    r
    t
    h
    e
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
    f
    o
    r
    a
    c
    e
    r
    t
    a
    i
    n
    p
    u
    r
    p
    o
    s
    e
    .
    """
    
    resource_type = "OrganizationContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ 
        V
        i
        s
        i
        t
        i
        n
        g
        o
        r
        p
        o
        s
        t
        a
        l
        a
        d
        d
        r
        e
        s
        s
        e
        s
        f
        o
        r
        t
        h
        e
        c
        o
        n
        t
        a
        c
        t
        .
        Type `Address` (represented as `dict` in JSON). """
        
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
        c
        o
        n
        t
        a
        c
        t
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.purpose = None
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
        c
        o
        n
        t
        a
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
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
        (
        t
        e
        l
        e
        p
        h
        o
        n
        e
        ,
        e
        m
        a
        i
        l
        ,
        e
        t
        c
        .
        )
        f
        o
        r
        a
        c
        o
        n
        t
        a
        c
        t
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OrganizationContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OrganizationContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
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
