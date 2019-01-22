#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/List) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class List(domainresource.DomainResource):
    """ 
    A
    l
    i
    s
    t
    i
    s
    a
    c
    u
    r
    a
    t
    e
    d
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
    r
    e
    s
    o
    u
    r
    c
    e
    s
    .
    """
    
    resource_type = "List"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        W
        h
        a
        t
        t
        h
        e
        p
        u
        r
        p
        o
        s
        e
        o
        f
        t
        h
        i
        s
        l
        i
        s
        t
        i
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        l
        i
        s
        t
        w
        a
        s
        p
        r
        e
        p
        a
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.emptyReason = None
        """ 
        W
        h
        y
        l
        i
        s
        t
        i
        s
        e
        m
        p
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        C
        o
        n
        t
        e
        x
        t
        i
        n
        w
        h
        i
        c
        h
        l
        i
        s
        t
        c
        r
        e
        a
        t
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.entry = None
        """ 
        E
        n
        t
        r
        i
        e
        s
        i
        n
        t
        h
        e
        l
        i
        s
        t
        .
        List of `ListEntry` items (represented as `dict` in JSON). """
        
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
        
        self.mode = None
        """ 
        w
        o
        r
        k
        i
        n
        g
        |
        s
        n
        a
        p
        s
        h
        o
        t
        |
        c
        h
        a
        n
        g
        e
        s
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
        a
        b
        o
        u
        t
        t
        h
        e
        l
        i
        s
        t
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.orderedBy = None
        """ 
        W
        h
        a
        t
        o
        r
        d
        e
        r
        t
        h
        e
        l
        i
        s
        t
        h
        a
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        W
        h
        o
        a
        n
        d
        /
        o
        r
        w
        h
        a
        t
        d
        e
        f
        i
        n
        e
        d
        t
        h
        e
        l
        i
        s
        t
        c
        o
        n
        t
        e
        n
        t
        s
        (
        a
        k
        a
        A
        u
        t
        h
        o
        r
        )
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        c
        u
        r
        r
        e
        n
        t
        |
        r
        e
        t
        i
        r
        e
        d
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
        I
        f
        a
        l
        l
        r
        e
        s
        o
        u
        r
        c
        e
        s
        h
        a
        v
        e
        t
        h
        e
        s
        a
        m
        e
        s
        u
        b
        j
        e
        c
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.title = None
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
        v
        e
        n
        a
        m
        e
        f
        o
        r
        t
        h
        e
        l
        i
        s
        t
        .
        Type `str`. """
        
        super(List, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


from . import backboneelement

class ListEntry(backboneelement.BackboneElement):
    """ 
    E
    n
    t
    r
    i
    e
    s
    i
    n
    t
    h
    e
    l
    i
    s
    t
    .
    
    
    E
    n
    t
    r
    i
    e
    s
    i
    n
    t
    h
    i
    s
    l
    i
    s
    t
    .
    
    """
    
    resource_type = "ListEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ 
        W
        h
        e
        n
        i
        t
        e
        m
        a
        d
        d
        e
        d
        t
        o
        l
        i
        s
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deleted = None
        """ 
        I
        f
        t
        h
        i
        s
        i
        t
        e
        m
        i
        s
        a
        c
        t
        u
        a
        l
        l
        y
        m
        a
        r
        k
        e
        d
        a
        s
        d
        e
        l
        e
        t
        e
        d
        .
        Type `bool`. """
        
        self.flag = None
        """ 
        S
        t
        a
        t
        u
        s
        /
        W
        o
        r
        k
        f
        l
        o
        w
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
        b
        o
        u
        t
        t
        h
        i
        s
        i
        t
        e
        m
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        """ 
        A
        c
        t
        u
        a
        l
        e
        n
        t
        r
        y
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(ListEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("flag", "flag", codeableconcept.CodeableConcept, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
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
