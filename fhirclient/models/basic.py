#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Basic) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Basic(domainresource.DomainResource):
    """ 
    R
    e
    s
    o
    u
    r
    c
    e
    f
    o
    r
    n
    o
    n
    -
    s
    u
    p
    p
    o
    r
    t
    e
    d
    c
    o
    n
    t
    e
    n
    t
    .
    
    
    B
    a
    s
    i
    c
    i
    s
    u
    s
    e
    d
    f
    o
    r
    h
    a
    n
    d
    l
    i
    n
    g
    c
    o
    n
    c
    e
    p
    t
    s
    n
    o
    t
    y
    e
    t
    d
    e
    f
    i
    n
    e
    d
    i
    n
    F
    H
    I
    R
    ,
    n
    a
    r
    r
    a
    t
    i
    v
    e
    -
    o
    n
    l
    y
    r
    e
    s
    o
    u
    r
    c
    e
    s
    t
    h
    a
    t
    d
    o
    n
    '
    t
    m
    a
    p
    t
    o
    a
    n
    e
    x
    i
    s
    t
    i
    n
    g
    r
    e
    s
    o
    u
    r
    c
    e
    ,
    a
    n
    d
    c
    u
    s
    t
    o
    m
    r
    e
    s
    o
    u
    r
    c
    e
    s
    n
    o
    t
    a
    p
    p
    r
    o
    p
    r
    i
    a
    t
    e
    f
    o
    r
    i
    n
    c
    l
    u
    s
    i
    o
    n
    i
    n
    t
    h
    e
    F
    H
    I
    R
    s
    p
    e
    c
    i
    f
    i
    c
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "Basic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ 
        W
        h
        o
        c
        r
        e
        a
        t
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        K
        i
        n
        d
        o
        f
        R
        e
        s
        o
        u
        r
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.created = None
        """ 
        W
        h
        e
        n
        c
        r
        e
        a
        t
        e
        d
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
        
        self.subject = None
        """ 
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
        t
        h
        e
        f
        o
        c
        u
        s
        o
        f
        t
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(Basic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Basic, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
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
