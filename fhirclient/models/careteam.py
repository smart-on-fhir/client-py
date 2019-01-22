#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CareTeam) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CareTeam(domainresource.DomainResource):
    """ 
    P
    l
    a
    n
    n
    e
    d
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
    t
    h
    e
    c
    o
    o
    r
    d
    i
    n
    a
    t
    i
    o
    n
    a
    n
    d
    d
    e
    l
    i
    v
    e
    r
    y
    o
    f
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
    o
    r
    g
    r
    o
    u
    p
    .
    
    
    T
    h
    e
    C
    a
    r
    e
    T
    e
    a
    m
    i
    n
    c
    l
    u
    d
    e
    s
    a
    l
    l
    t
    h
    e
    p
    e
    o
    p
    l
    e
    a
    n
    d
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
    h
    o
    p
    l
    a
    n
    t
    o
    p
    a
    r
    t
    i
    c
    i
    p
    a
    t
    e
    i
    n
    t
    h
    e
    c
    o
    o
    r
    d
    i
    n
    a
    t
    i
    o
    n
    a
    n
    d
    d
    e
    l
    i
    v
    e
    r
    y
    o
    f
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
    .
    
    """
    
    resource_type = "CareTeam"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ 
        T
        y
        p
        e
        o
        f
        t
        e
        a
        m
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        E
        n
        c
        o
        u
        n
        t
        e
        r
        c
        r
        e
        a
        t
        e
        d
        a
        s
        p
        a
        r
        t
        o
        f
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        t
        e
        a
        m
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
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
        r
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        f
        o
        r
        t
        h
        e
        c
        a
        r
        e
        t
        e
        a
        m
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        t
        e
        a
        m
        ,
        s
        u
        c
        h
        a
        s
        c
        r
        i
        s
        i
        s
        a
        s
        s
        e
        s
        s
        m
        e
        n
        t
        t
        e
        a
        m
        .
        Type `str`. """
        
        self.note = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        s
        m
        a
        d
        e
        a
        b
        o
        u
        t
        t
        h
        e
        C
        a
        r
        e
        T
        e
        a
        m
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ 
        M
        e
        m
        b
        e
        r
        s
        o
        f
        t
        h
        e
        t
        e
        a
        m
        .
        List of `CareTeamParticipant` items (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        T
        i
        m
        e
        p
        e
        r
        i
        o
        d
        t
        e
        a
        m
        c
        o
        v
        e
        r
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        t
        h
        e
        c
        a
        r
        e
        t
        e
        a
        m
        e
        x
        i
        s
        t
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        t
        h
        e
        c
        a
        r
        e
        t
        e
        a
        m
        e
        x
        i
        s
        t
        s
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        a
        c
        t
        i
        v
        e
        |
        s
        u
        s
        p
        e
        n
        d
        e
        d
        |
        i
        n
        a
        c
        t
        i
        v
        e
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
        
        self.subject = None
        """ 
        W
        h
        o
        c
        a
        r
        e
        t
        e
        a
        m
        i
        s
        f
        o
        r
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
        c
        a
        r
        e
        t
        e
        a
        m
        (
        t
        h
        a
        t
        a
        p
        p
        l
        i
        e
        s
        t
        o
        a
        l
        l
        m
        e
        m
        b
        e
        r
        s
        )
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(CareTeam, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CareTeam, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("participant", "participant", CareTeamParticipant, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class CareTeamParticipant(backboneelement.BackboneElement):
    """ 
    M
    e
    m
    b
    e
    r
    s
    o
    f
    t
    h
    e
    t
    e
    a
    m
    .
    
    
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
    a
    l
    l
    p
    e
    o
    p
    l
    e
    a
    n
    d
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
    h
    o
    a
    r
    e
    e
    x
    p
    e
    c
    t
    e
    d
    t
    o
    b
    e
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
    t
    e
    a
    m
    .
    
    """
    
    resource_type = "CareTeamParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.member = None
        """ 
        W
        h
        o
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        T
        i
        m
        e
        p
        e
        r
        i
        o
        d
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
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ 
        T
        y
        p
        e
        o
        f
        i
        n
        v
        o
        l
        v
        e
        m
        e
        n
        t
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(CareTeamParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CareTeamParticipant, self).elementProperties()
        js.extend([
            ("member", "member", fhirreference.FHIRReference, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
