#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PractitionerRole) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class PractitionerRole(domainresource.DomainResource):
    """ 
    R
    o
    l
    e
    s
    /
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
    .
    
    
    A
    s
    p
    e
    c
    i
    f
    i
    c
    s
    e
    t
    o
    f
    R
    o
    l
    e
    s
    /
    L
    o
    c
    a
    t
    i
    o
    n
    s
    /
    s
    p
    e
    c
    i
    a
    l
    t
    i
    e
    s
    /
    s
    e
    r
    v
    i
    c
    e
    s
    t
    h
    a
    t
    a
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
    m
    a
    y
    p
    e
    r
    f
    o
    r
    m
    a
    t
    a
    n
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
    p
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
    .
    
    """
    
    resource_type = "PractitionerRole"
    
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
        r
        o
        l
        e
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
        
        self.availabilityExceptions = None
        """ 
        D
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
        a
        v
        a
        i
        l
        a
        b
        i
        l
        i
        t
        y
        e
        x
        c
        e
        p
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
        self.availableTime = None
        """ 
        T
        i
        m
        e
        s
        t
        h
        e
        S
        e
        r
        v
        i
        c
        e
        S
        i
        t
        e
        i
        s
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
        List of `PractitionerRoleAvailableTime` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        R
        o
        l
        e
        s
        w
        h
        i
        c
        h
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
        m
        a
        y
        p
        e
        r
        f
        o
        r
        m
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        i
        t
        h
        t
        h
        i
        s
        r
        o
        l
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.healthcareService = None
        """ 
        T
        h
        e
        l
        i
        s
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
        s
        e
        r
        v
        i
        c
        e
        s
        t
        h
        a
        t
        t
        h
        i
        s
        w
        o
        r
        k
        e
        r
        p
        r
        o
        v
        i
        d
        e
        s
        f
        o
        r
        t
        h
        i
        s
        r
        o
        l
        e
        '
        s
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
        /
        L
        o
        c
        a
        t
        i
        o
        n
        (
        s
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
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
        t
        h
        a
        t
        a
        r
        e
        s
        p
        e
        c
        i
        f
        i
        c
        t
        o
        a
        r
        o
        l
        e
        /
        l
        o
        c
        a
        t
        i
        o
        n
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ 
        T
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        (
        s
        )
        a
        t
        w
        h
        i
        c
        h
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
        p
        r
        o
        v
        i
        d
        e
        s
        c
        a
        r
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.notAvailable = None
        """ 
        N
        o
        t
        a
        v
        a
        i
        l
        a
        b
        l
        e
        d
        u
        r
        i
        n
        g
        t
        h
        i
        s
        t
        i
        m
        e
        d
        u
        e
        t
        o
        p
        r
        o
        v
        i
        d
        e
        d
        r
        e
        a
        s
        o
        n
        .
        List of `PractitionerRoleNotAvailable` items (represented as `dict` in JSON). """
        
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
        w
        h
        e
        r
        e
        t
        h
        e
        r
        o
        l
        e
        s
        a
        r
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
        i
        s
        a
        u
        t
        h
        o
        r
        i
        z
        e
        d
        t
        o
        p
        e
        r
        f
        o
        r
        m
        i
        n
        t
        h
        e
        s
        e
        r
        o
        l
        e
        (
        s
        )
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.practitioner = None
        """ 
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
        t
        h
        a
        t
        i
        s
        a
        b
        l
        e
        t
        o
        p
        r
        o
        v
        i
        d
        e
        t
        h
        e
        d
        e
        f
        i
        n
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        s
        p
        e
        c
        i
        a
        l
        t
        y
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        t
        h
        a
        t
        a
        r
        e
        s
        p
        e
        c
        i
        f
        i
        c
        t
        o
        t
        h
        e
        r
        o
        l
        e
        /
        l
        o
        c
        a
        t
        i
        o
        n
        /
        s
        e
        r
        v
        i
        c
        e
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(PractitionerRole, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRole, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", PractitionerRoleAvailableTime, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("notAvailable", "notAvailable", PractitionerRoleNotAvailable, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("practitioner", "practitioner", fhirreference.FHIRReference, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """ 
    T
    i
    m
    e
    s
    t
    h
    e
    S
    e
    r
    v
    i
    c
    e
    S
    i
    t
    e
    i
    s
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
    t
    i
    m
    e
    s
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
    i
    s
    a
    v
    a
    i
    l
    a
    b
    l
    e
    o
    r
    p
    e
    r
    f
    o
    r
    m
    i
    n
    g
    t
    h
    i
    s
    r
    o
    l
    e
    a
    t
    t
    h
    e
    l
    o
    c
    a
    t
    i
    o
    n
    a
    n
    d
    /
    o
    r
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
    .
    
    """
    
    resource_type = "PractitionerRoleAvailableTime"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        """ 
        A
        l
        w
        a
        y
        s
        a
        v
        a
        i
        l
        a
        b
        l
        e
        ?
        e
        .
        g
        .
        2
        4
        h
        o
        u
        r
        s
        e
        r
        v
        i
        c
        e
        .
        Type `bool`. """
        
        self.availableEndTime = None
        """ 
        C
        l
        o
        s
        i
        n
        g
        t
        i
        m
        e
        o
        f
        d
        a
        y
        (
        i
        g
        n
        o
        r
        e
        d
        i
        f
        a
        l
        l
        D
        a
        y
        =
        t
        r
        u
        e
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.availableStartTime = None
        """ 
        O
        p
        e
        n
        i
        n
        g
        t
        i
        m
        e
        o
        f
        d
        a
        y
        (
        i
        g
        n
        o
        r
        e
        d
        i
        f
        a
        l
        l
        D
        a
        y
        =
        t
        r
        u
        e
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None
        """ 
        m
        o
        n
        |
        t
        u
        e
        |
        w
        e
        d
        |
        t
        h
        u
        |
        f
        r
        i
        |
        s
        a
        t
        |
        s
        u
        n
        .
        List of `str` items. """
        
        super(PractitionerRoleAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRoleAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js


class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """ 
    N
    o
    t
    a
    v
    a
    i
    l
    a
    b
    l
    e
    d
    u
    r
    i
    n
    g
    t
    h
    i
    s
    t
    i
    m
    e
    d
    u
    e
    t
    o
    p
    r
    o
    v
    i
    d
    e
    d
    r
    e
    a
    s
    o
    n
    .
    
    
    T
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
    i
    s
    n
    o
    t
    a
    v
    a
    i
    l
    a
    b
    l
    e
    o
    r
    p
    e
    r
    f
    o
    r
    m
    i
    n
    g
    t
    h
    i
    s
    r
    o
    l
    e
    d
    u
    r
    i
    n
    g
    t
    h
    i
    s
    p
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
    d
    u
    e
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
    d
    e
    d
    r
    e
    a
    s
    o
    n
    .
    
    """
    
    resource_type = "PractitionerRoleNotAvailable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        R
        e
        a
        s
        o
        n
        p
        r
        e
        s
        e
        n
        t
        e
        d
        t
        o
        t
        h
        e
        u
        s
        e
        r
        e
        x
        p
        l
        a
        i
        n
        i
        n
        g
        w
        h
        y
        t
        i
        m
        e
        n
        o
        t
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
        Type `str`. """
        
        self.during = None
        """ 
        S
        e
        r
        v
        i
        c
        e
        n
        o
        t
        a
        v
        a
        i
        l
        a
        b
        l
        e
        f
        r
        o
        m
        t
        h
        i
        s
        d
        a
        t
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(PractitionerRoleNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
        ])
        return js


import sys
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
