#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class VisionPrescription(domainresource.DomainResource):
    """ 
    P
    r
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
    f
    o
    r
    v
    i
    s
    i
    o
    n
    c
    o
    r
    r
    e
    c
    t
    i
    o
    n
    p
    r
    o
    d
    u
    c
    t
    s
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
    
    
    A
    n
    a
    u
    t
    h
    o
    r
    i
    z
    a
    t
    i
    o
    n
    f
    o
    r
    t
    h
    e
    p
    r
    o
    v
    i
    s
    i
    o
    n
    o
    f
    g
    l
    a
    s
    s
    e
    s
    a
    n
    d
    /
    o
    r
    c
    o
    n
    t
    a
    c
    t
    l
    e
    n
    s
    e
    s
    t
    o
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
    
    resource_type = "VisionPrescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ 
        R
        e
        s
        p
        o
        n
        s
        e
        c
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
        
        self.dateWritten = None
        """ 
        W
        h
        e
        n
        p
        r
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
        w
        a
        s
        a
        u
        t
        h
        o
        r
        i
        z
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ 
        C
        r
        e
        a
        t
        e
        d
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
        /
        a
        d
        m
        i
        s
        s
        i
        o
        n
        /
        s
        t
        a
        y
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
        f
        o
        r
        v
        i
        s
        i
        o
        n
        p
        r
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
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lensSpecification = None
        """ 
        V
        i
        s
        i
        o
        n
        l
        e
        n
        s
        a
        u
        t
        h
        o
        r
        i
        z
        a
        t
        i
        o
        n
        .
        List of `VisionPrescriptionLensSpecification` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ 
        W
        h
        o
        p
        r
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
        i
        s
        f
        o
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.prescriber = None
        """ 
        W
        h
        o
        a
        u
        t
        h
        o
        r
        i
        z
        e
        d
        t
        h
        e
        v
        i
        s
        i
        o
        n
        p
        r
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
        
        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("lensSpecification", "lensSpecification", VisionPrescriptionLensSpecification, True, None, True),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """ 
    V
    i
    s
    i
    o
    n
    l
    e
    n
    s
    a
    u
    t
    h
    o
    r
    i
    z
    a
    t
    i
    o
    n
    .
    
    
    C
    o
    n
    t
    a
    i
    n
    t
    h
    e
    d
    e
    t
    a
    i
    l
    s
    o
    f
    t
    h
    e
    i
    n
    d
    i
    v
    i
    d
    u
    a
    l
    l
    e
    n
    s
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
    s
    a
    n
    d
    s
    e
    r
    v
    e
    s
    a
    s
    t
    h
    e
    a
    u
    t
    h
    o
    r
    i
    z
    a
    t
    i
    o
    n
    f
    o
    r
    t
    h
    e
    f
    u
    l
    l
    f
    i
    l
    l
    m
    e
    n
    t
    b
    y
    c
    e
    r
    t
    i
    f
    i
    e
    d
    p
    r
    o
    f
    e
    s
    s
    i
    o
    n
    a
    l
    s
    .
    
    """
    
    resource_type = "VisionPrescriptionLensSpecification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.add = None
        """ 
        A
        d
        d
        e
        d
        p
        o
        w
        e
        r
        f
        o
        r
        m
        u
        l
        t
        i
        f
        o
        c
        a
        l
        l
        e
        v
        e
        l
        s
        .
        Type `float`. """
        
        self.axis = None
        """ 
        L
        e
        n
        s
        m
        e
        r
        i
        d
        i
        a
        n
        w
        h
        i
        c
        h
        c
        o
        n
        t
        a
        i
        n
        n
        o
        p
        o
        w
        e
        r
        f
        o
        r
        a
        s
        t
        i
        g
        m
        a
        t
        i
        s
        m
        .
        Type `int`. """
        
        self.backCurve = None
        """ 
        C
        o
        n
        t
        a
        c
        t
        l
        e
        n
        s
        b
        a
        c
        k
        c
        u
        r
        v
        a
        t
        u
        r
        e
        .
        Type `float`. """
        
        self.brand = None
        """ 
        B
        r
        a
        n
        d
        r
        e
        q
        u
        i
        r
        e
        d
        .
        Type `str`. """
        
        self.color = None
        """ 
        C
        o
        l
        o
        r
        r
        e
        q
        u
        i
        r
        e
        d
        .
        Type `str`. """
        
        self.cylinder = None
        """ 
        L
        e
        n
        s
        p
        o
        w
        e
        r
        f
        o
        r
        a
        s
        t
        i
        g
        m
        a
        t
        i
        s
        m
        .
        Type `float`. """
        
        self.diameter = None
        """ 
        C
        o
        n
        t
        a
        c
        t
        l
        e
        n
        s
        d
        i
        a
        m
        e
        t
        e
        r
        .
        Type `float`. """
        
        self.duration = None
        """ 
        L
        e
        n
        s
        w
        e
        a
        r
        d
        u
        r
        a
        t
        i
        o
        n
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.eye = None
        """ 
        r
        i
        g
        h
        t
        |
        l
        e
        f
        t
        .
        Type `str`. """
        
        self.note = None
        """ 
        N
        o
        t
        e
        s
        f
        o
        r
        c
        o
        a
        t
        i
        n
        g
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.power = None
        """ 
        C
        o
        n
        t
        a
        c
        t
        l
        e
        n
        s
        p
        o
        w
        e
        r
        .
        Type `float`. """
        
        self.prism = None
        """ 
        E
        y
        e
        a
        l
        i
        g
        n
        m
        e
        n
        t
        c
        o
        m
        p
        e
        n
        s
        a
        t
        i
        o
        n
        .
        List of `VisionPrescriptionLensSpecificationPrism` items (represented as `dict` in JSON). """
        
        self.product = None
        """ 
        P
        r
        o
        d
        u
        c
        t
        t
        o
        b
        e
        s
        u
        p
        p
        l
        i
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sphere = None
        """ 
        P
        o
        w
        e
        r
        o
        f
        t
        h
        e
        l
        e
        n
        s
        .
        Type `float`. """
        
        super(VisionPrescriptionLensSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecification, self).elementProperties()
        js.extend([
            ("add", "add", float, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("brand", "brand", str, False, None, False),
            ("color", "color", str, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("eye", "eye", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("power", "power", float, False, None, False),
            ("prism", "prism", VisionPrescriptionLensSpecificationPrism, True, None, False),
            ("product", "product", codeableconcept.CodeableConcept, False, None, True),
            ("sphere", "sphere", float, False, None, False),
        ])
        return js


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """ 
    E
    y
    e
    a
    l
    i
    g
    n
    m
    e
    n
    t
    c
    o
    m
    p
    e
    n
    s
    a
    t
    i
    o
    n
    .
    
    
    A
    l
    l
    o
    w
    s
    f
    o
    r
    a
    d
    j
    u
    s
    t
    m
    e
    n
    t
    o
    n
    t
    w
    o
    a
    x
    i
    s
    .
    
    """
    
    resource_type = "VisionPrescriptionLensSpecificationPrism"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        A
        m
        o
        u
        n
        t
        o
        f
        a
        d
        j
        u
        s
        t
        m
        e
        n
        t
        .
        Type `float`. """
        
        self.base = None
        """ 
        u
        p
        |
        d
        o
        w
        n
        |
        i
        n
        |
        o
        u
        t
        .
        Type `str`. """
        
        super(VisionPrescriptionLensSpecificationPrism, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecificationPrism, self).elementProperties()
        js.extend([
            ("amount", "amount", float, False, None, True),
            ("base", "base", str, False, None, True),
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
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
