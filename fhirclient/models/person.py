#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Person) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Person(domainresource.DomainResource):
    """ 
    A
    g
    e
    n
    e
    r
    i
    c
    p
    e
    r
    s
    o
    n
    r
    e
    c
    o
    r
    d
    .
    
    
    D
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
    a
    n
    d
    a
    d
    m
    i
    n
    i
    s
    t
    r
    a
    t
    i
    v
    e
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
    i
    n
    d
    e
    p
    e
    n
    d
    e
    n
    t
    o
    f
    a
    s
    p
    e
    c
    i
    f
    i
    c
    h
    e
    a
    l
    t
    h
    -
    r
    e
    l
    a
    t
    e
    d
    c
    o
    n
    t
    e
    x
    t
    .
    
    """
    
    resource_type = "Person"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ 
        T
        h
        i
        s
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
        O
        n
        e
        o
        r
        m
        o
        r
        e
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
        p
        e
        r
        s
        o
        n
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
        
        self.link = None
        """ 
        L
        i
        n
        k
        t
        o
        a
        r
        e
        s
        o
        u
        r
        c
        e
        t
        h
        a
        t
        c
        o
        n
        c
        e
        r
        n
        s
        t
        h
        e
        s
        a
        m
        e
        a
        c
        t
        u
        a
        l
        p
        e
        r
        s
        o
        n
        .
        List of `PersonLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
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
        t
        h
        a
        t
        i
        s
        t
        h
        e
        c
        u
        s
        t
        o
        d
        i
        a
        n
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
        r
        e
        c
        o
        r
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        Type `Attachment` (represented as `dict` in JSON). """
        
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
        
        super(Person, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Person, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("link", "link", PersonLink, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PersonLink(backboneelement.BackboneElement):
    """ 
    L
    i
    n
    k
    t
    o
    a
    r
    e
    s
    o
    u
    r
    c
    e
    t
    h
    a
    t
    c
    o
    n
    c
    e
    r
    n
    s
    t
    h
    e
    s
    a
    m
    e
    a
    c
    t
    u
    a
    l
    p
    e
    r
    s
    o
    n
    .
    """
    
    resource_type = "PersonLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assurance = None
        """ 
        l
        e
        v
        e
        l
        1
        |
        l
        e
        v
        e
        l
        2
        |
        l
        e
        v
        e
        l
        3
        |
        l
        e
        v
        e
        l
        4
        .
        Type `str`. """
        
        self.target = None
        """ 
        T
        h
        e
        r
        e
        s
        o
        u
        r
        c
        e
        t
        o
        w
        h
        i
        c
        h
        t
        h
        i
        s
        a
        c
        t
        u
        a
        l
        p
        e
        r
        s
        o
        n
        i
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(PersonLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PersonLink, self).elementProperties()
        js.extend([
            ("assurance", "assurance", str, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, True),
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
