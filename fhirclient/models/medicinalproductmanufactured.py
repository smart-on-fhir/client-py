#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProductManufactured(domainresource.DomainResource):
    """ 
    T
    h
    e
    m
    a
    n
    u
    f
    a
    c
    t
    u
    r
    e
    d
    i
    t
    e
    m
    a
    s
    c
    o
    n
    t
    a
    i
    n
    e
    d
    i
    n
    t
    h
    e
    p
    a
    c
    k
    a
    g
    e
    d
    m
    e
    d
    i
    c
    i
    n
    a
    l
    p
    r
    o
    d
    u
    c
    t
    .
    """
    
    resource_type = "MedicinalProductManufactured"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ingredient = None
        """ 
        I
        n
        g
        r
        e
        d
        i
        e
        n
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.manufacturedDoseForm = None
        """ 
        D
        o
        s
        e
        f
        o
        r
        m
        a
        s
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        d
        a
        n
        d
        b
        e
        f
        o
        r
        e
        a
        n
        y
        t
        r
        a
        n
        s
        f
        o
        r
        m
        a
        t
        i
        o
        n
        i
        n
        t
        o
        t
        h
        e
        p
        h
        a
        r
        m
        a
        c
        e
        u
        t
        i
        c
        a
        l
        p
        r
        o
        d
        u
        c
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ 
        M
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        r
        o
        f
        t
        h
        e
        i
        t
        e
        m
        (
        N
        o
        t
        e
        t
        h
        a
        t
        t
        h
        i
        s
        s
        h
        o
        u
        l
        d
        b
        e
        n
        a
        m
        e
        d
        "
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        r
        "
        b
        u
        t
        i
        t
        c
        u
        r
        r
        e
        n
        t
        l
        y
        c
        a
        u
        s
        e
        s
        t
        e
        c
        h
        n
        i
        c
        a
        l
        i
        s
        s
        u
        e
        s
        )
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.otherCharacteristics = None
        """ 
        O
        t
        h
        e
        r
        c
        o
        d
        e
        a
        b
        l
        e
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.physicalCharacteristics = None
        """ 
        D
        i
        m
        e
        n
        s
        i
        o
        n
        s
        ,
        c
        o
        l
        o
        r
        e
        t
        c
        .
        .
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ 
        T
        h
        e
        q
        u
        a
        n
        t
        i
        t
        y
        o
        r
        "
        c
        o
        u
        n
        t
        n
        u
        m
        b
        e
        r
        "
        o
        f
        t
        h
        e
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        d
        i
        t
        e
        m
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitOfPresentation = None
        """ 
        T
        h
        e
        “
        r
        e
        a
        l
        w
        o
        r
        l
        d
        ”
        u
        n
        i
        t
        s
        i
        n
        w
        h
        i
        c
        h
        t
        h
        e
        q
        u
        a
        n
        t
        i
        t
        y
        o
        f
        t
        h
        e
        m
        a
        n
        u
        f
        a
        c
        t
        u
        r
        e
        d
        i
        t
        e
        m
        i
        s
        d
        e
        s
        c
        r
        i
        b
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductManufactured, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductManufactured, self).elementProperties()
        js.extend([
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("manufacturedDoseForm", "manufacturedDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
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
    from . import prodcharacteristic
except ImportError:
    prodcharacteristic = sys.modules[__package__ + '.prodcharacteristic']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
