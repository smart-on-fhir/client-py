#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Appointment) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Appointment(domainresource.DomainResource):
    """ 
    A
    b
    o
    o
    k
    i
    n
    g
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
    e
    v
    e
    n
    t
    a
    m
    o
    n
    g
    p
    a
    t
    i
    e
    n
    t
    (
    s
    )
    ,
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
    s
    )
    ,
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
    (
    s
    )
    a
    n
    d
    /
    o
    r
    d
    e
    v
    i
    c
    e
    (
    s
    )
    f
    o
    r
    a
    s
    p
    e
    c
    i
    f
    i
    c
    d
    a
    t
    e
    /
    t
    i
    m
    e
    .
    T
    h
    i
    s
    m
    a
    y
    r
    e
    s
    u
    l
    t
    i
    n
    o
    n
    e
    o
    r
    m
    o
    r
    e
    E
    n
    c
    o
    u
    n
    t
    e
    r
    (
    s
    )
    .
    """
    
    resource_type = "Appointment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appointmentType = None
        """ 
        T
        h
        e
        s
        t
        y
        l
        e
        o
        f
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
        o
        r
        p
        a
        t
        i
        e
        n
        t
        t
        h
        a
        t
        h
        a
        s
        b
        e
        e
        n
        b
        o
        o
        k
        e
        d
        i
        n
        t
        h
        e
        s
        l
        o
        t
        (
        n
        o
        t
        s
        e
        r
        v
        i
        c
        e
        t
        y
        p
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.basedOn = None
        """ 
        T
        h
        e
        s
        e
        r
        v
        i
        c
        e
        r
        e
        q
        u
        e
        s
        t
        t
        h
        i
        s
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
        a
        l
        l
        o
        c
        a
        t
        e
        d
        t
        o
        a
        s
        s
        e
        s
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.cancelationReason = None
        """ 
        T
        h
        e
        c
        o
        d
        e
        d
        r
        e
        a
        s
        o
        n
        f
        o
        r
        t
        h
        e
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
        b
        e
        i
        n
        g
        c
        a
        n
        c
        e
        l
        l
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        c
        o
        m
        m
        e
        n
        t
        s
        .
        Type `str`. """
        
        self.created = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        t
        h
        a
        t
        t
        h
        i
        s
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
        w
        a
        s
        i
        n
        i
        t
        i
        a
        l
        l
        y
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
        S
        h
        o
        w
        n
        o
        n
        a
        s
        u
        b
        j
        e
        c
        t
        l
        i
        n
        e
        i
        n
        a
        m
        e
        e
        t
        i
        n
        g
        r
        e
        q
        u
        e
        s
        t
        ,
        o
        r
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
        l
        i
        s
        t
        .
        Type `str`. """
        
        self.end = None
        """ 
        W
        h
        e
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
        t
        o
        c
        o
        n
        c
        l
        u
        d
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        I
        d
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
        
        self.minutesDuration = None
        """ 
        C
        a
        n
        b
        e
        l
        e
        s
        s
        t
        h
        a
        n
        s
        t
        a
        r
        t
        /
        e
        n
        d
        (
        e
        .
        g
        .
        e
        s
        t
        i
        m
        a
        t
        e
        )
        .
        Type `int`. """
        
        self.participant = None
        """ 
        P
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
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
        .
        List of `AppointmentParticipant` items (represented as `dict` in JSON). """
        
        self.patientInstruction = None
        """ 
        D
        e
        t
        a
        i
        l
        e
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
        a
        n
        d
        i
        n
        s
        t
        r
        u
        c
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
        p
        a
        t
        i
        e
        n
        t
        .
        Type `str`. """
        
        self.priority = None
        """ 
        U
        s
        e
        d
        t
        o
        m
        a
        k
        e
        i
        n
        f
        o
        r
        m
        e
        d
        d
        e
        c
        i
        s
        i
        o
        n
        s
        i
        f
        n
        e
        e
        d
        i
        n
        g
        t
        o
        r
        e
        -
        p
        r
        i
        o
        r
        i
        t
        i
        z
        e
        .
        Type `int`. """
        
        self.reasonCode = None
        """ 
        C
        o
        d
        e
        d
        r
        e
        a
        s
        o
        n
        t
        h
        i
        s
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
        s
        c
        h
        e
        d
        u
        l
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        R
        e
        a
        s
        o
        n
        t
        h
        e
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
        t
        o
        t
        a
        k
        e
        p
        l
        a
        c
        e
        (
        r
        e
        s
        o
        u
        r
        c
        e
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requestedPeriod = None
        """ 
        P
        o
        t
        e
        n
        t
        i
        a
        l
        d
        a
        t
        e
        /
        t
        i
        m
        e
        i
        n
        t
        e
        r
        v
        a
        l
        (
        s
        )
        r
        e
        q
        u
        e
        s
        t
        e
        d
        t
        o
        a
        l
        l
        o
        c
        a
        t
        e
        t
        h
        e
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
        w
        i
        t
        h
        i
        n
        .
        List of `Period` items (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ 
        A
        b
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
        i
        z
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
        t
        h
        a
        t
        i
        s
        t
        o
        b
        e
        p
        e
        r
        f
        o
        r
        m
        e
        d
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ 
        T
        h
        e
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
        r
        v
        i
        c
        e
        t
        h
        a
        t
        i
        s
        t
        o
        b
        e
        p
        e
        r
        f
        o
        r
        m
        e
        d
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.slot = None
        """ 
        T
        h
        e
        s
        l
        o
        t
        s
        t
        h
        a
        t
        t
        h
        i
        s
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
        f
        i
        l
        l
        i
        n
        g
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ 
        T
        h
        e
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
        t
        h
        a
        t
        w
        o
        u
        l
        d
        b
        e
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
        p
        e
        r
        f
        o
        r
        m
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
        r
        e
        q
        u
        e
        s
        t
        e
        d
        i
        n
        t
        h
        i
        s
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.start = None
        """ 
        W
        h
        e
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
        t
        o
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ 
        p
        r
        o
        p
        o
        s
        e
        d
        |
        p
        e
        n
        d
        i
        n
        g
        |
        b
        o
        o
        k
        e
        d
        |
        a
        r
        r
        i
        v
        e
        d
        |
        f
        u
        l
        f
        i
        l
        l
        e
        d
        |
        c
        a
        n
        c
        e
        l
        l
        e
        d
        |
        n
        o
        s
        h
        o
        w
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
        |
        c
        h
        e
        c
        k
        e
        d
        -
        i
        n
        |
        w
        a
        i
        t
        l
        i
        s
        t
        .
        Type `str`. """
        
        self.supportingInformation = None
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
        t
        o
        s
        u
        p
        p
        o
        r
        t
        t
        h
        e
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
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(Appointment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("cancelationReason", "cancelationReason", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("minutesDuration", "minutesDuration", int, False, None, False),
            ("participant", "participant", AppointmentParticipant, True, None, True),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("priority", "priority", int, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requestedPeriod", "requestedPeriod", period.Period, True, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("slot", "slot", fhirreference.FHIRReference, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class AppointmentParticipant(backboneelement.BackboneElement):
    """ 
    P
    a
    r
    t
    i
    c
    i
    p
    a
    n
    t
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
    .
    
    
    L
    i
    s
    t
    o
    f
    p
    a
    r
    t
    i
    c
    i
    p
    a
    n
    t
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
    .
    
    """
    
    resource_type = "AppointmentParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ 
        P
        e
        r
        s
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
        /
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
        o
        r
        D
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        P
        a
        r
        t
        i
        c
        i
        p
        a
        t
        i
        o
        n
        p
        e
        r
        i
        o
        d
        o
        f
        t
        h
        e
        a
        c
        t
        o
        r
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.required = None
        """ 
        r
        e
        q
        u
        i
        r
        e
        d
        |
        o
        p
        t
        i
        o
        n
        a
        l
        |
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
        -
        o
        n
        l
        y
        .
        Type `str`. """
        
        self.status = None
        """ 
        a
        c
        c
        e
        p
        t
        e
        d
        |
        d
        e
        c
        l
        i
        n
        e
        d
        |
        t
        e
        n
        t
        a
        t
        i
        v
        e
        |
        n
        e
        e
        d
        s
        -
        a
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.type = None
        """ 
        R
        o
        l
        e
        o
        f
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        i
        n
        t
        h
        e
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(AppointmentParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("required", "required", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
