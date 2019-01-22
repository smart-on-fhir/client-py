#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Patient) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Patient(domainresource.DomainResource):
    """ 
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
    n
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
    o
    r
    a
    n
    i
    m
    a
    l
    r
    e
    c
    e
    i
    v
    i
    n
    g
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
    s
    e
    r
    v
    i
    c
    e
    s
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
    o
    t
    h
    e
    r
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
    n
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
    o
    r
    a
    n
    i
    m
    a
    l
    r
    e
    c
    e
    i
    v
    i
    n
    g
    c
    a
    r
    e
    o
    r
    o
    t
    h
    e
    r
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
    s
    e
    r
    v
    i
    c
    e
    s
    .
    
    """
    
    resource_type = "Patient"
    
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
        a
        t
        i
        e
        n
        t
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
        f
        b
        i
        r
        t
        h
        f
        o
        r
        t
        h
        e
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
        List of `PatientCommunication` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ 
        A
        c
        o
        n
        t
        a
        c
        t
        p
        a
        r
        t
        y
        (
        e
        .
        g
        .
        g
        u
        a
        r
        d
        i
        a
        n
        ,
        p
        a
        r
        t
        n
        e
        r
        ,
        f
        r
        i
        e
        n
        d
        )
        f
        o
        r
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
        .
        List of `PatientContact` items (represented as `dict` in JSON). """
        
        self.deceasedBoolean = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        i
        f
        t
        h
        e
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
        i
        s
        d
        e
        c
        e
        a
        s
        e
        d
        o
        r
        n
        o
        t
        .
        Type `bool`. """
        
        self.deceasedDateTime = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        i
        f
        t
        h
        e
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
        i
        s
        d
        e
        c
        e
        a
        s
        e
        d
        o
        r
        n
        o
        t
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
        
        self.generalPractitioner = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        '
        s
        n
        o
        m
        i
        n
        a
        t
        e
        d
        p
        r
        i
        m
        a
        r
        y
        c
        a
        r
        e
        p
        r
        o
        v
        i
        d
        e
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        p
        a
        t
        i
        e
        n
        t
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
        n
        o
        t
        h
        e
        r
        p
        a
        t
        i
        e
        n
        t
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
        List of `PatientLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
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
        a
        t
        i
        e
        n
        t
        r
        e
        c
        o
        r
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.maritalStatus = None
        """ 
        M
        a
        r
        i
        t
        a
        l
        (
        c
        i
        v
        i
        l
        )
        s
        t
        a
        t
        u
        s
        o
        f
        a
        p
        a
        t
        i
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleBirthBoolean = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        p
        a
        t
        i
        e
        n
        t
        i
        s
        p
        a
        r
        t
        o
        f
        a
        m
        u
        l
        t
        i
        p
        l
        e
        b
        i
        r
        t
        h
        .
        Type `bool`. """
        
        self.multipleBirthInteger = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        p
        a
        t
        i
        e
        n
        t
        i
        s
        p
        a
        r
        t
        o
        f
        a
        m
        u
        l
        t
        i
        p
        l
        e
        b
        i
        r
        t
        h
        .
        Type `int`. """
        
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
        a
        t
        i
        e
        n
        t
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
        a
        t
        i
        e
        n
        t
        .
        List of `Attachment` items (represented as `dict` in JSON). """
        
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
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Patient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Patient, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("address", "address", address.Address, True, None, False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, False, None, False),
            ("communication", "communication", PatientCommunication, True, None, False),
            ("contact", "contact", PatientContact, True, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDateTime", "deceasedDateTime", fhirdate.FHIRDate, False, "deceased", False),
            ("gender", "gender", str, False, None, False),
            ("generalPractitioner", "generalPractitioner", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("link", "link", PatientLink, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("maritalStatus", "maritalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("multipleBirthBoolean", "multipleBirthBoolean", bool, False, "multipleBirth", False),
            ("multipleBirthInteger", "multipleBirthInteger", int, False, "multipleBirth", False),
            ("name", "name", humanname.HumanName, True, None, False),
            ("photo", "photo", attachment.Attachment, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PatientCommunication(backboneelement.BackboneElement):
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
    """
    
    resource_type = "PatientCommunication"
    
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
        
        super(PatientCommunication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, True),
            ("preferred", "preferred", bool, False, None, False),
        ])
        return js


class PatientContact(backboneelement.BackboneElement):
    """ 
    A
    c
    o
    n
    t
    a
    c
    t
    p
    a
    r
    t
    y
    (
    e
    .
    g
    .
    g
    u
    a
    r
    d
    i
    a
    n
    ,
    p
    a
    r
    t
    n
    e
    r
    ,
    f
    r
    i
    e
    n
    d
    )
    f
    o
    r
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
    .
    """
    
    resource_type = "PatientContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ 
        A
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
        c
        o
        n
        t
        a
        c
        t
        p
        e
        r
        s
        o
        n
        .
        Type `Address` (represented as `dict` in JSON). """
        
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
        p
        e
        r
        s
        o
        n
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.organization = None
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        T
        h
        e
        p
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
        i
        s
        c
        o
        n
        t
        a
        c
        t
        p
        e
        r
        s
        o
        n
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
        i
        s
        v
        a
        l
        i
        d
        t
        o
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
        r
        e
        l
        a
        t
        i
        n
        g
        t
        o
        t
        h
        i
        s
        p
        a
        t
        i
        e
        n
        t
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        T
        h
        e
        k
        i
        n
        d
        o
        f
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
        
        super(PatientContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("gender", "gender", str, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class PatientLink(backboneelement.BackboneElement):
    """ 
    L
    i
    n
    k
    t
    o
    a
    n
    o
    t
    h
    e
    r
    p
    a
    t
    i
    e
    n
    t
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
    
    
    L
    i
    n
    k
    t
    o
    a
    n
    o
    t
    h
    e
    r
    p
    a
    t
    i
    e
    n
    t
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
    a
    t
    i
    e
    n
    t
    .
    
    """
    
    resource_type = "PatientLink"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.other = None
        """ 
        T
        h
        e
        o
        t
        h
        e
        r
        p
        a
        t
        i
        e
        n
        t
        o
        r
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
        t
        h
        e
        l
        i
        n
        k
        r
        e
        f
        e
        r
        s
        t
        o
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        r
        e
        p
        l
        a
        c
        e
        d
        -
        b
        y
        |
        r
        e
        p
        l
        a
        c
        e
        s
        |
        r
        e
        f
        e
        r
        |
        s
        e
        e
        a
        l
        s
        o
        .
        Type `str`. """
        
        super(PatientLink, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PatientLink, self).elementProperties()
        js.extend([
            ("other", "other", fhirreference.FHIRReference, False, None, True),
            ("type", "type", str, False, None, True),
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
