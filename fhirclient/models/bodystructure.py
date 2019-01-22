#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BodyStructure) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class BodyStructure(domainresource.DomainResource):
    """ 
    S
    p
    e
    c
    i
    f
    i
    c
    a
    n
    d
    i
    d
    e
    n
    t
    i
    f
    i
    e
    d
    a
    n
    a
    t
    o
    m
    i
    c
    a
    l
    s
    t
    r
    u
    c
    t
    u
    r
    e
    .
    
    
    R
    e
    c
    o
    r
    d
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
    a
    n
    a
    n
    a
    t
    o
    m
    i
    c
    a
    l
    s
    t
    r
    u
    c
    t
    u
    r
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
    m
    a
    y
    b
    e
    u
    s
    e
    d
    w
    h
    e
    n
    a
    c
    o
    d
    e
    d
    c
    o
    n
    c
    e
    p
    t
    d
    o
    e
    s
    n
    o
    t
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
    n
    e
    c
    e
    s
    s
    a
    r
    y
    d
    e
    t
    a
    i
    l
    n
    e
    e
    d
    e
    d
    f
    o
    r
    t
    h
    e
    u
    s
    e
    c
    a
    s
    e
    .
    
    """
    
    resource_type = "BodyStructure"
    
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
        
        self.description = None
        """ 
        T
        e
        x
        t
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
        .
        Type `str`. """
        
        self.identifier = None
        """ 
        B
        o
        d
        y
        s
        t
        r
        u
        c
        t
        u
        r
        e
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
        
        self.image = None
        """ 
        A
        t
        t
        a
        c
        h
        e
        d
        i
        m
        a
        g
        e
        s
        .
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.location = None
        """ 
        B
        o
        d
        y
        s
        i
        t
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.locationQualifier = None
        """ 
        B
        o
        d
        y
        s
        i
        t
        e
        m
        o
        d
        i
        f
        i
        e
        r
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.morphology = None
        """ 
        K
        i
        n
        d
        o
        f
        S
        t
        r
        u
        c
        t
        u
        r
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        W
        h
        o
        t
        h
        i
        s
        i
        s
        a
        b
        o
        u
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(BodyStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BodyStructure, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("location", "location", codeableconcept.CodeableConcept, False, None, False),
            ("locationQualifier", "locationQualifier", codeableconcept.CodeableConcept, True, None, False),
            ("morphology", "morphology", codeableconcept.CodeableConcept, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
