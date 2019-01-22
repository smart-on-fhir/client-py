#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EnrollmentResponse) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class EnrollmentResponse(domainresource.DomainResource):
    """ 
    E
    n
    r
    o
    l
    l
    m
    e
    n
    t
    R
    e
    s
    p
    o
    n
    s
    e
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    
    T
    h
    i
    s
    r
    e
    s
    o
    u
    r
    c
    e
    p
    r
    o
    v
    i
    d
    e
    s
    e
    n
    r
    o
    l
    l
    m
    e
    n
    t
    a
    n
    d
    p
    l
    a
    n
    d
    e
    t
    a
    i
    l
    s
    f
    r
    o
    m
    t
    h
    e
    p
    r
    o
    c
    e
    s
    s
    i
    n
    g
    o
    f
    a
    n
    E
    n
    r
    o
    l
    l
    m
    e
    n
    t
    R
    e
    q
    u
    e
    s
    t
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    """
    
    resource_type = "EnrollmentResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ 
        C
        r
        e
        a
        t
        i
        o
        n
        d
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        """ 
        D
        i
        s
        p
        o
        s
        i
        t
        i
        o
        n
        M
        e
        s
        s
        a
        g
        e
        .
        Type `str`. """
        
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ 
        I
        n
        s
        u
        r
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ 
        q
        u
        e
        u
        e
        d
        |
        c
        o
        m
        p
        l
        e
        t
        e
        |
        e
        r
        r
        o
        r
        |
        p
        a
        r
        t
        i
        a
        l
        .
        Type `str`. """
        
        self.request = None
        """ 
        C
        l
        a
        i
        m
        r
        e
        f
        e
        r
        e
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ 
        R
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
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
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
        d
        r
        a
        f
        t
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
        
        super(EnrollmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js


import sys
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
