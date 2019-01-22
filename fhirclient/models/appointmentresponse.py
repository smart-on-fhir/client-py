#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class AppointmentResponse(domainresource.DomainResource):
    """ 
    A
    r
    e
    p
    l
    y
    t
    o
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
    r
    e
    q
    u
    e
    s
    t
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
    a
    n
    d
    /
    o
    r
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
    s
    u
    c
    h
    a
    s
    a
    c
    o
    n
    f
    i
    r
    m
    a
    t
    i
    o
    n
    o
    r
    r
    e
    j
    e
    c
    t
    i
    o
    n
    .
    """
    
    resource_type = "AppointmentResponse"
    
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
        ,
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
        ,
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
        
        self.appointment = None
        """ 
        A
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
        t
        h
        i
        s
        r
        e
        s
        p
        o
        n
        s
        e
        r
        e
        l
        a
        t
        e
        s
        t
        o
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.end = None
        """ 
        T
        i
        m
        e
        f
        r
        o
        m
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
        ,
        o
        r
        r
        e
        q
        u
        e
        s
        t
        e
        d
        n
        e
        w
        e
        n
        d
        t
        i
        m
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
        
        self.participantStatus = None
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
        i
        n
        -
        p
        r
        o
        c
        e
        s
        s
        |
        c
        o
        m
        p
        l
        e
        t
        e
        d
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
        
        self.participantType = None
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
        
        self.start = None
        """ 
        T
        i
        m
        e
        f
        r
        o
        m
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
        ,
        o
        r
        r
        e
        q
        u
        e
        s
        t
        e
        d
        n
        e
        w
        s
        t
        a
        r
        t
        t
        i
        m
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(AppointmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("participantStatus", "participantStatus", str, False, None, True),
            ("participantType", "participantType", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
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
