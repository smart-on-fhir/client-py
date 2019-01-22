#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ 
    A
    m
    a
    t
    e
    r
    i
    a
    l
    s
    u
    b
    s
    t
    a
    n
    c
    e
    o
    r
    i
    g
    i
    n
    a
    t
    i
    n
    g
    f
    r
    o
    m
    a
    b
    i
    o
    l
    o
    g
    i
    c
    a
    l
    e
    n
    t
    i
    t
    y
    .
    
    
    A
    m
    a
    t
    e
    r
    i
    a
    l
    s
    u
    b
    s
    t
    a
    n
    c
    e
    o
    r
    i
    g
    i
    n
    a
    t
    i
    n
    g
    f
    r
    o
    m
    a
    b
    i
    o
    l
    o
    g
    i
    c
    a
    l
    e
    n
    t
    i
    t
    y
    i
    n
    t
    e
    n
    d
    e
    d
    t
    o
    b
    e
    t
    r
    a
    n
    s
    p
    l
    a
    n
    t
    e
    d
    o
    r
    i
    n
    f
    u
    s
    e
    d
    
    i
    n
    t
    o
    a
    n
    o
    t
    h
    e
    r
    (
    p
    o
    s
    s
    i
    b
    l
    y
    t
    h
    e
    s
    a
    m
    e
    )
    b
    i
    o
    l
    o
    g
    i
    c
    a
    l
    e
    n
    t
    i
    t
    y
    .
    
    """
    
    resource_type = "BiologicallyDerivedProduct"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection = None
        """ 
        H
        o
        w
        t
        h
        i
        s
        p
        r
        o
        d
        u
        c
        t
        w
        a
        s
        c
        o
        l
        l
        e
        c
        t
        e
        d
        .
        Type `BiologicallyDerivedProductCollection` (represented as `dict` in JSON). """
        
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
        i
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
        
        self.manipulation = None
        """ 
        A
        n
        y
        m
        a
        n
        i
        p
        u
        l
        a
        t
        i
        o
        n
        o
        f
        p
        r
        o
        d
        u
        c
        t
        p
        o
        s
        t
        -
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
        .
        Type `BiologicallyDerivedProductManipulation` (represented as `dict` in JSON). """
        
        self.parent = None
        """ 
        B
        i
        o
        l
        o
        g
        i
        c
        a
        l
        l
        y
        D
        e
        r
        i
        v
        e
        d
        P
        r
        o
        d
        u
        c
        t
        p
        a
        r
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.processing = None
        """ 
        A
        n
        y
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
        t
        h
        e
        p
        r
        o
        d
        u
        c
        t
        d
        u
        r
        i
        n
        g
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
        .
        List of `BiologicallyDerivedProductProcessing` items (represented as `dict` in JSON). """
        
        self.productCategory = None
        """ 
        o
        r
        g
        a
        n
        |
        t
        i
        s
        s
        u
        e
        |
        f
        l
        u
        i
        d
        |
        c
        e
        l
        l
        s
        |
        b
        i
        o
        l
        o
        g
        i
        c
        a
        l
        A
        g
        e
        n
        t
        .
        Type `str`. """
        
        self.productCode = None
        """ 
        W
        h
        a
        t
        t
        h
        i
        s
        b
        i
        o
        l
        o
        g
        i
        c
        a
        l
        l
        y
        d
        e
        r
        i
        v
        e
        d
        p
        r
        o
        d
        u
        c
        t
        i
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        T
        h
        e
        a
        m
        o
        u
        n
        t
        o
        f
        t
        h
        i
        s
        b
        i
        o
        l
        o
        g
        i
        c
        a
        l
        l
        y
        d
        e
        r
        i
        v
        e
        d
        p
        r
        o
        d
        u
        c
        t
        .
        Type `int`. """
        
        self.request = None
        """ 
        P
        r
        o
        c
        e
        d
        u
        r
        e
        r
        e
        q
        u
        e
        s
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        v
        a
        i
        l
        a
        b
        l
        e
        |
        u
        n
        a
        v
        a
        i
        l
        a
        b
        l
        e
        .
        Type `str`. """
        
        self.storage = None
        """ 
        P
        r
        o
        d
        u
        c
        t
        s
        t
        o
        r
        a
        g
        e
        .
        List of `BiologicallyDerivedProductStorage` items (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend([
            ("collection", "collection", BiologicallyDerivedProductCollection, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("manipulation", "manipulation", BiologicallyDerivedProductManipulation, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("processing", "processing", BiologicallyDerivedProductProcessing, True, None, False),
            ("productCategory", "productCategory", str, False, None, False),
            ("productCode", "productCode", codeableconcept.CodeableConcept, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("request", "request", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("storage", "storage", BiologicallyDerivedProductStorage, True, None, False),
        ])
        return js


from . import backboneelement

class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ 
    H
    o
    w
    t
    h
    i
    s
    p
    r
    o
    d
    u
    c
    t
    w
    a
    s
    c
    o
    l
    l
    e
    c
    t
    e
    d
    .
    """
    
    resource_type = "BiologicallyDerivedProductCollection"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collectedDateTime = None
        """ 
        T
        i
        m
        e
        o
        f
        p
        r
        o
        d
        u
        c
        t
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
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.collectedPeriod = None
        """ 
        T
        i
        m
        e
        o
        f
        p
        r
        o
        d
        u
        c
        t
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
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.collector = None
        """ 
        I
        n
        d
        i
        v
        i
        d
        u
        a
        l
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        W
        h
        o
        i
        s
        p
        r
        o
        d
        u
        c
        t
        f
        r
        o
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductCollection, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend([
            ("collectedDateTime", "collectedDateTime", fhirdate.FHIRDate, False, "collected", False),
            ("collectedPeriod", "collectedPeriod", period.Period, False, "collected", False),
            ("collector", "collector", fhirreference.FHIRReference, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ 
    A
    n
    y
    m
    a
    n
    i
    p
    u
    l
    a
    t
    i
    o
    n
    o
    f
    p
    r
    o
    d
    u
    c
    t
    p
    o
    s
    t
    -
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
    .
    
    
    A
    n
    y
    m
    a
    n
    i
    p
    u
    l
    a
    t
    i
    o
    n
    o
    f
    p
    r
    o
    d
    u
    c
    t
    p
    o
    s
    t
    -
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
    t
    h
    a
    t
    i
    s
    i
    n
    t
    e
    n
    d
    e
    d
    t
    o
    a
    l
    t
    e
    r
    t
    h
    e
    p
    r
    o
    d
    u
    c
    t
    .
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    a
    b
    u
    f
    f
    y
    -
    c
    o
    a
    t
    e
    n
    r
    i
    c
    h
    m
    e
    n
    t
    o
    r
    C
    D
    8
    r
    e
    d
    u
    c
    t
    i
    o
    n
    o
    f
    P
    e
    r
    i
    p
    h
    e
    r
    a
    l
    B
    l
    o
    o
    d
    S
    t
    e
    m
    C
    e
    l
    l
    s
    t
    o
    m
    a
    k
    e
    i
    t
    m
    o
    r
    e
    s
    u
    i
    t
    a
    b
    l
    e
    f
    o
    r
    i
    n
    f
    u
    s
    i
    o
    n
    .
    
    """
    
    resource_type = "BiologicallyDerivedProductManipulation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
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
        o
        n
        o
        f
        m
        a
        n
        i
        p
        u
        l
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.timeDateTime = None
        """ 
        T
        i
        m
        e
        o
        f
        m
        a
        n
        i
        p
        u
        l
        a
        t
        i
        o
        n
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timePeriod = None
        """ 
        T
        i
        m
        e
        o
        f
        m
        a
        n
        i
        p
        u
        l
        a
        t
        i
        o
        n
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductManipulation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ 
    A
    n
    y
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
    t
    h
    e
    p
    r
    o
    d
    u
    c
    t
    d
    u
    r
    i
    n
    g
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
    .
    
    
    A
    n
    y
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
    t
    h
    e
    p
    r
    o
    d
    u
    c
    t
    d
    u
    r
    i
    n
    g
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
    t
    h
    a
    t
    d
    o
    e
    s
    n
    o
    t
    c
    h
    a
    n
    g
    e
    t
    h
    e
    f
    u
    n
    d
    a
    m
    e
    n
    t
    a
    l
    n
    a
    t
    u
    r
    e
    o
    f
    t
    h
    e
    p
    r
    o
    d
    u
    c
    t
    .
    F
    o
    r
    e
    x
    a
    m
    p
    l
    e
    a
    d
    d
    i
    n
    g
    a
    n
    t
    i
    -
    c
    o
    a
    g
    u
    l
    a
    n
    t
    s
    d
    u
    r
    i
    n
    g
    t
    h
    e
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
    P
    e
    r
    i
    p
    h
    e
    r
    a
    l
    B
    l
    o
    o
    d
    S
    t
    e
    m
    C
    e
    l
    l
    s
    .
    
    """
    
    resource_type = "BiologicallyDerivedProductProcessing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        """ 
        S
        u
        b
        s
        t
        a
        n
        c
        e
        a
        d
        d
        e
        d
        d
        u
        r
        i
        n
        g
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.description = None
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
        o
        n
        o
        f
        o
        f
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
        .
        Type `str`. """
        
        self.procedure = None
        """ 
        P
        r
        o
        c
        e
        s
        i
        n
        g
        c
        o
        d
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timeDateTime = None
        """ 
        T
        i
        m
        e
        o
        f
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
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timePeriod = None
        """ 
        T
        i
        m
        e
        o
        f
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
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(BiologicallyDerivedProductProcessing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend([
            ("additive", "additive", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("procedure", "procedure", codeableconcept.CodeableConcept, False, None, False),
            ("timeDateTime", "timeDateTime", fhirdate.FHIRDate, False, "time", False),
            ("timePeriod", "timePeriod", period.Period, False, "time", False),
        ])
        return js


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    d
    u
    c
    t
    s
    t
    o
    r
    a
    g
    e
    .
    """
    
    resource_type = "BiologicallyDerivedProductStorage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
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
        o
        n
        o
        f
        s
        t
        o
        r
        a
        g
        e
        .
        Type `str`. """
        
        self.duration = None
        """ 
        S
        t
        o
        r
        a
        g
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
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.scale = None
        """ 
        f
        a
        r
        e
        n
        h
        e
        i
        t
        |
        c
        e
        l
        s
        i
        u
        s
        |
        k
        e
        l
        v
        i
        n
        .
        Type `str`. """
        
        self.temperature = None
        """ 
        S
        t
        o
        r
        a
        g
        e
        t
        e
        m
        p
        e
        r
        a
        t
        u
        r
        e
        .
        Type `float`. """
        
        super(BiologicallyDerivedProductStorage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("duration", "duration", period.Period, False, None, False),
            ("scale", "scale", str, False, None, False),
            ("temperature", "temperature", float, False, None, False),
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
