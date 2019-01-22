#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class HealthcareService(domainresource.DomainResource):
    """ 
    T
    h
    e
    d
    e
    t
    a
    i
    l
    s
    o
    f
    a
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
    a
    v
    a
    i
    l
    a
    b
    l
    e
    a
    t
    a
    l
    o
    c
    a
    t
    i
    o
    n
    .
    """
    
    resource_type = "HealthcareService"
    
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
        H
        e
        a
        l
        t
        h
        c
        a
        r
        e
        S
        e
        r
        v
        i
        c
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
        
        self.appointmentRequired = None
        """ 
        I
        f
        a
        n
        a
        p
        p
        o
        i
        n
        t
        m
        e
        n
        t
        i
        s
        r
        e
        q
        u
        i
        r
        e
        d
        f
        o
        r
        a
        c
        c
        e
        s
        s
        t
        o
        t
        h
        i
        s
        s
        e
        r
        v
        i
        c
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
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        B
        r
        o
        a
        d
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
        s
        e
        r
        v
        i
        c
        e
        b
        e
        i
        n
        g
        p
        e
        r
        f
        o
        r
        m
        e
        d
        o
        r
        d
        e
        l
        i
        v
        e
        r
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ 
        C
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
        c
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        s
        (
        a
        t
        t
        r
        i
        b
        u
        t
        e
        s
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.comment = None
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
        a
        n
        d
        /
        o
        r
        a
        n
        y
        s
        p
        e
        c
        i
        f
        i
        c
        i
        s
        s
        u
        e
        s
        n
        o
        t
        c
        o
        v
        e
        r
        e
        d
        e
        l
        s
        e
        w
        h
        e
        r
        e
        .
        Type `str`. """
        
        self.communication = None
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
        t
        h
        a
        t
        t
        h
        i
        s
        s
        e
        r
        v
        i
        c
        e
        i
        s
        o
        f
        f
        e
        r
        e
        d
        i
        n
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.coverageArea = None
        """ 
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
        s
        e
        r
        v
        i
        c
        e
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
        f
        o
        r
        /
        a
        v
        a
        i
        l
        a
        b
        l
        e
        t
        o
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.eligibility = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
        e
        l
        i
        g
        i
        b
        i
        l
        i
        t
        y
        r
        e
        q
        u
        i
        r
        e
        m
        e
        n
        t
        s
        r
        e
        q
        u
        i
        r
        e
        d
        t
        o
        u
        s
        e
        t
        h
        e
        s
        e
        r
        v
        i
        c
        e
        .
        List of `HealthcareServiceEligibility` items (represented as `dict` in JSON). """
        
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
        e
        l
        e
        c
        t
        r
        o
        n
        i
        c
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.extraDetails = None
        """ 
        E
        x
        t
        r
        a
        d
        e
        t
        a
        i
        l
        s
        a
        b
        o
        u
        t
        t
        h
        e
        s
        e
        r
        v
        i
        c
        e
        t
        h
        a
        t
        c
        a
        n
        '
        t
        b
        e
        p
        l
        a
        c
        e
        d
        i
        n
        t
        h
        e
        o
        t
        h
        e
        r
        f
        i
        e
        l
        d
        s
        .
        Type `str`. """
        
        self.identifier = None
        """ 
        E
        x
        t
        e
        r
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
        s
        f
        o
        r
        t
        h
        i
        s
        i
        t
        e
        m
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ 
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
        w
        h
        e
        r
        e
        s
        e
        r
        v
        i
        c
        e
        m
        a
        y
        b
        e
        p
        r
        o
        v
        i
        d
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name = None
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
        s
        e
        r
        v
        i
        c
        e
        a
        s
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
        a
        c
        o
        n
        s
        u
        m
        e
        r
        w
        h
        i
        l
        e
        s
        e
        a
        r
        c
        h
        i
        n
        g
        .
        Type `str`. """
        
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
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ 
        F
        a
        c
        i
        l
        i
        t
        a
        t
        e
        s
        q
        u
        i
        c
        k
        i
        d
        e
        n
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
        o
        f
        t
        h
        e
        s
        e
        r
        v
        i
        c
        e
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.program = None
        """ 
        P
        r
        o
        g
        r
        a
        m
        s
        t
        h
        a
        t
        t
        h
        i
        s
        s
        e
        r
        v
        i
        c
        e
        i
        s
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
        t
        o
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.providedBy = None
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
        p
        r
        o
        v
        i
        d
        e
        s
        t
        h
        i
        s
        s
        e
        r
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.referralMethod = None
        """ 
        W
        a
        y
        s
        t
        h
        a
        t
        t
        h
        e
        s
        e
        r
        v
        i
        c
        e
        a
        c
        c
        e
        p
        t
        s
        r
        e
        f
        e
        r
        r
        a
        l
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceProvisionCode = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
        s
        u
        n
        d
        e
        r
        w
        h
        i
        c
        h
        s
        e
        r
        v
        i
        c
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
        /
        o
        f
        f
        e
        r
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ 
        S
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
        h
        a
        n
        d
        l
        e
        d
        b
        y
        t
        h
        e
        H
        e
        a
        l
        t
        h
        c
        a
        r
        e
        S
        e
        r
        v
        i
        c
        e
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
        t
        h
        e
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
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        s
        e
        r
        v
        i
        c
        e
        t
        h
        a
        t
        m
        a
        y
        b
        e
        d
        e
        l
        i
        v
        e
        r
        e
        d
        o
        r
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("program", "program", codeableconcept.CodeableConcept, True, None, False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
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
    a
    t
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
    
    """
    
    resource_type = "HealthcareServiceAvailableTime"
    
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
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js


class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ 
    S
    p
    e
    c
    i
    f
    i
    c
    e
    l
    i
    g
    i
    b
    i
    l
    i
    t
    y
    r
    e
    q
    u
    i
    r
    e
    m
    e
    n
    t
    s
    r
    e
    q
    u
    i
    r
    e
    d
    t
    o
    u
    s
    e
    t
    h
    e
    s
    e
    r
    v
    i
    c
    e
    .
    
    
    D
    o
    e
    s
    t
    h
    i
    s
    s
    e
    r
    v
    i
    c
    e
    h
    a
    v
    e
    s
    p
    e
    c
    i
    f
    i
    c
    e
    l
    i
    g
    i
    b
    i
    l
    i
    t
    y
    r
    e
    q
    u
    i
    r
    e
    m
    e
    n
    t
    s
    t
    h
    a
    t
    n
    e
    e
    d
    t
    o
    b
    e
    m
    e
    t
    i
    n
    o
    r
    d
    e
    r
    t
    o
    u
    s
    e
    t
    h
    e
    s
    e
    r
    v
    i
    c
    e
    ?
    
    """
    
    resource_type = "HealthcareServiceEligibility"
    
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
        v
        a
        l
        u
        e
        f
        o
        r
        t
        h
        e
        e
        l
        i
        g
        i
        b
        i
        l
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment = None
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
        e
        l
        i
        g
        i
        b
        i
        l
        i
        t
        y
        c
        o
        n
        d
        i
        t
        i
        o
        n
        s
        f
        o
        r
        t
        h
        e
        s
        e
        r
        v
        i
        c
        e
        .
        Type `str`. """
        
        super(HealthcareServiceEligibility, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
        ])
        return js


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
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
    H
    e
    a
    l
    t
    h
    c
    a
    r
    e
    S
    e
    r
    v
    i
    c
    e
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
    
    resource_type = "HealthcareServiceNotAvailable"
    
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
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
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
