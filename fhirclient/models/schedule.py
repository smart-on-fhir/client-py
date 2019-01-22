#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Schedule) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Schedule(domainresource.DomainResource):
    """ 
    A
    c
    o
    n
    t
    a
    i
    n
    e
    r
    f
    o
    r
    s
    l
    o
    t
    s
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
    m
    a
    y
    b
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
    f
    o
    r
    b
    o
    o
    k
    i
    n
    g
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
    s
    .
    """
    
    resource_type = "Schedule"
    
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
        s
        c
        h
        e
        d
        u
        l
        e
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
        
        self.actor = None
        """ 
        R
        e
        s
        o
        u
        r
        c
        e
        (
        s
        )
        t
        h
        a
        t
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
        i
        s
        b
        e
        i
        n
        g
        p
        r
        o
        v
        i
        d
        e
        d
        f
        o
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.comment = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        s
        o
        n
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
        
        self.planningHorizon = None
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
        c
        o
        v
        e
        r
        e
        d
        b
        y
        s
        c
        h
        e
        d
        u
        l
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ 
        H
        i
        g
        h
        -
        l
        e
        v
        e
        l
        c
        a
        t
        e
        g
        o
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
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
        e
        r
        v
        i
        c
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ 
        T
        y
        p
        e
        o
        f
        s
        p
        e
        c
        i
        a
        l
        t
        y
        n
        e
        e
        d
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Schedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Schedule, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("actor", "actor", fhirreference.FHIRReference, True, None, True),
            ("comment", "comment", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("planningHorizon", "planningHorizon", period.Period, False, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
