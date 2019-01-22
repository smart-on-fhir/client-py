#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ 
    E
    n
    r
    o
    l
    l
    i
    n
    c
    o
    v
    e
    r
    a
    g
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
    t
    h
    e
    i
    n
    s
    u
    r
    a
    n
    c
    e
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
    d
    e
    t
    a
    i
    l
    s
    t
    o
    t
    h
    e
    i
    n
    s
    u
    r
    e
    r
    r
    e
    g
    a
    r
    d
    i
    n
    g
    a
    s
    p
    e
    c
    i
    f
    i
    e
    d
    c
    o
    v
    e
    r
    a
    g
    e
    .
    
    """
    
    resource_type = "EnrollmentRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.candidate = None
        """ 
        T
        h
        e
        s
        u
        b
        j
        e
        c
        t
        t
        o
        b
        e
        e
        n
        r
        o
        l
        l
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ 
        I
        n
        s
        u
        r
        a
        n
        c
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.insurer = None
        """ 
        T
        a
        r
        g
        e
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.provider = None
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
        
        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("candidate", "candidate", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
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
