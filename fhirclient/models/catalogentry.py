#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CatalogEntry) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class CatalogEntry(domainresource.DomainResource):
    """ 
    A
    n
    e
    n
    t
    r
    y
    i
    n
    a
    c
    a
    t
    a
    l
    o
    g
    .
    
    
    C
    a
    t
    a
    l
    o
    g
    e
    n
    t
    r
    i
    e
    s
    a
    r
    e
    w
    r
    a
    p
    p
    e
    r
    s
    t
    h
    a
    t
    c
    o
    n
    t
    e
    x
    t
    u
    a
    l
    i
    z
    e
    i
    t
    e
    m
    s
    i
    n
    c
    l
    u
    d
    e
    d
    i
    n
    a
    c
    a
    t
    a
    l
    o
    g
    .
    
    """
    
    resource_type = "CatalogEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additionalCharacteristic = None
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
        h
        a
        r
        a
        c
        t
        e
        r
        i
        s
        t
        i
        c
        s
        o
        f
        t
        h
        e
        c
        a
        t
        a
        l
        o
        g
        e
        n
        t
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.additionalClassification = None
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
        l
        a
        s
        s
        i
        f
        i
        c
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
        c
        a
        t
        a
        l
        o
        g
        e
        n
        t
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.additionalIdentifier = None
        """ 
        A
        n
        y
        a
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
        d
        e
        n
        t
        i
        f
        i
        e
        r
        (
        s
        )
        f
        o
        r
        t
        h
        e
        c
        a
        t
        a
        l
        o
        g
        i
        t
        e
        m
        ,
        i
        n
        t
        h
        e
        s
        a
        m
        e
        g
        r
        a
        n
        u
        l
        a
        r
        i
        t
        y
        o
        r
        c
        o
        n
        c
        e
        p
        t
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.classification = None
        """ 
        C
        l
        a
        s
        s
        i
        f
        i
        c
        a
        t
        i
        o
        n
        (
        c
        a
        t
        e
        g
        o
        r
        y
        o
        r
        c
        l
        a
        s
        s
        )
        o
        f
        t
        h
        e
        i
        t
        e
        m
        e
        n
        t
        r
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        U
        n
        i
        q
        u
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
        o
        f
        t
        h
        e
        c
        a
        t
        a
        l
        o
        g
        i
        t
        e
        m
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastUpdated = None
        """ 
        W
        h
        e
        n
        w
        a
        s
        t
        h
        i
        s
        c
        a
        t
        a
        l
        o
        g
        l
        a
        s
        t
        u
        p
        d
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.orderable = None
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
        e
        e
        n
        t
        r
        y
        r
        e
        p
        r
        e
        s
        e
        n
        t
        s
        a
        n
        o
        r
        d
        e
        r
        a
        b
        l
        e
        i
        t
        e
        m
        .
        Type `bool`. """
        
        self.referencedItem = None
        """ 
        T
        h
        e
        i
        t
        e
        m
        t
        h
        a
        t
        i
        s
        b
        e
        i
        n
        g
        d
        e
        f
        i
        n
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relatedEntry = None
        """ 
        A
        n
        i
        t
        e
        m
        t
        h
        a
        t
        t
        h
        i
        s
        c
        a
        t
        a
        l
        o
        g
        e
        n
        t
        r
        y
        i
        s
        r
        e
        l
        a
        t
        e
        d
        t
        o
        .
        List of `CatalogEntryRelatedEntry` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        a
        c
        t
        i
        v
        e
        |
        r
        e
        t
        i
        r
        e
        d
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
        h
        e
        t
        y
        p
        e
        o
        f
        i
        t
        e
        m
        -
        m
        e
        d
        i
        c
        a
        t
        i
        o
        n
        ,
        d
        e
        v
        i
        c
        e
        ,
        s
        e
        r
        v
        i
        c
        e
        ,
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
        o
        t
        h
        e
        r
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.validTo = None
        """ 
        T
        h
        e
        d
        a
        t
        e
        u
        n
        t
        i
        l
        w
        h
        i
        c
        h
        t
        h
        i
        s
        c
        a
        t
        a
        l
        o
        g
        e
        n
        t
        r
        y
        i
        s
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
        a
        c
        t
        i
        v
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.validityPeriod = None
        """ 
        T
        h
        e
        t
        i
        m
        e
        p
        e
        r
        i
        o
        d
        i
        n
        w
        h
        i
        c
        h
        t
        h
        i
        s
        c
        a
        t
        a
        l
        o
        g
        e
        n
        t
        r
        y
        i
        s
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
        a
        c
        t
        i
        v
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(CatalogEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntry, self).elementProperties()
        js.extend([
            ("additionalCharacteristic", "additionalCharacteristic", codeableconcept.CodeableConcept, True, None, False),
            ("additionalClassification", "additionalClassification", codeableconcept.CodeableConcept, True, None, False),
            ("additionalIdentifier", "additionalIdentifier", identifier.Identifier, True, None, False),
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
            ("orderable", "orderable", bool, False, None, True),
            ("referencedItem", "referencedItem", fhirreference.FHIRReference, False, None, True),
            ("relatedEntry", "relatedEntry", CatalogEntryRelatedEntry, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("validTo", "validTo", fhirdate.FHIRDate, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


from . import backboneelement

class CatalogEntryRelatedEntry(backboneelement.BackboneElement):
    """ 
    A
    n
    i
    t
    e
    m
    t
    h
    a
    t
    t
    h
    i
    s
    c
    a
    t
    a
    l
    o
    g
    e
    n
    t
    r
    y
    i
    s
    r
    e
    l
    a
    t
    e
    d
    t
    o
    .
    
    
    U
    s
    e
    d
    f
    o
    r
    e
    x
    a
    m
    p
    l
    e
    ,
    t
    o
    p
    o
    i
    n
    t
    t
    o
    a
    s
    u
    b
    s
    t
    a
    n
    c
    e
    ,
    o
    r
    t
    o
    a
    d
    e
    v
    i
    c
    e
    u
    s
    e
    d
    t
    o
    a
    d
    m
    i
    n
    i
    s
    t
    e
    r
    a
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "CatalogEntryRelatedEntry"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ 
        T
        h
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        t
        o
        t
        h
        e
        r
        e
        l
        a
        t
        e
        d
        i
        t
        e
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relationtype = None
        """ 
        t
        r
        i
        g
        g
        e
        r
        s
        |
        i
        s
        -
        r
        e
        p
        l
        a
        c
        e
        d
        -
        b
        y
        .
        Type `str`. """
        
        super(CatalogEntryRelatedEntry, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CatalogEntryRelatedEntry, self).elementProperties()
        js.extend([
            ("item", "item", fhirreference.FHIRReference, False, None, True),
            ("relationtype", "relationtype", str, False, None, True),
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
