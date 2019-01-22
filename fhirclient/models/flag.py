#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Flag) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Flag(domainresource.DomainResource):
    """ 
    K
    e
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
    t
    o
    f
    l
    a
    g
    t
    o
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
    p
    r
    o
    v
    i
    d
    e
    r
    s
    .
    
    
    P
    r
    o
    s
    p
    e
    c
    t
    i
    v
    e
    w
    a
    r
    n
    i
    n
    g
    s
    o
    f
    p
    o
    t
    e
    n
    t
    i
    a
    l
    i
    s
    s
    u
    e
    s
    w
    h
    e
    n
    p
    r
    o
    v
    i
    d
    i
    n
    g
    c
    a
    r
    e
    t
    o
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
    
    resource_type = "Flag"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ 
        F
        l
        a
        g
        c
        r
        e
        a
        t
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.category = None
        """ 
        C
        l
        i
        n
        i
        c
        a
        l
        ,
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
        ,
        e
        t
        c
        .
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        C
        o
        d
        e
        d
        o
        r
        t
        e
        x
        t
        u
        a
        l
        m
        e
        s
        s
        a
        g
        e
        t
        o
        d
        i
        s
        p
        l
        a
        y
        t
        o
        u
        s
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        A
        l
        e
        r
        t
        r
        e
        l
        e
        v
        a
        n
        t
        d
        u
        r
        i
        n
        g
        e
        n
        c
        o
        u
        n
        t
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
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
        w
        h
        e
        n
        f
        l
        a
        g
        i
        s
        a
        c
        t
        i
        v
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
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
        /
        W
        h
        a
        t
        i
        s
        f
        l
        a
        g
        a
        b
        o
        u
        t
        ?
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Flag, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
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
