#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class MedicinalProductPackaged(domainresource.DomainResource):
    """ 
    A
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
    i
    n
    a
    c
    o
    n
    t
    a
    i
    n
    e
    r
    o
    r
    p
    a
    c
    k
    a
    g
    e
    .
    """
    
    resource_type = "MedicinalProductPackaged"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.batchIdentifier = None
        """ 
        B
        a
        t
        c
        h
        n
        u
        m
        b
        e
        r
        i
        n
        g
        .
        List of `MedicinalProductPackagedBatchIdentifier` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        e
        x
        t
        u
        a
        l
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.legalStatusOfSupply = None
        """ 
        T
        h
        e
        l
        e
        g
        a
        l
        s
        t
        a
        t
        u
        s
        o
        f
        s
        u
        p
        p
        l
        y
        o
        f
        t
        h
        e
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
        a
        s
        c
        l
        a
        s
        s
        i
        f
        i
        e
        d
        b
        y
        t
        h
        e
        r
        e
        g
        u
        l
        a
        t
        o
        r
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
        i
        s
        P
        a
        c
        k
        a
        g
        e
        I
        t
        e
        m
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.marketingAuthorization = None
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
        i
        s
        P
        a
        c
        k
        a
        g
        e
        I
        t
        e
        m
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.marketingStatus = None
        """ 
        M
        a
        r
        k
        e
        t
        i
        n
        g
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
        List of `MarketingStatus` items (represented as `dict` in JSON). """
        
        self.packageItem = None
        """ 
        A
        p
        a
        c
        k
        a
        g
        i
        n
        g
        i
        t
        e
        m
        ,
        a
        s
        a
        c
        o
        n
        t
        a
        i
        n
        e
        d
        f
        o
        r
        m
        e
        d
        i
        c
        i
        n
        e
        ,
        p
        o
        s
        s
        i
        b
        l
        y
        w
        i
        t
        h
        o
        t
        h
        e
        r
        p
        a
        c
        k
        a
        g
        i
        n
        g
        i
        t
        e
        m
        s
        w
        i
        t
        h
        i
        n
        .
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ 
        T
        h
        e
        p
        r
        o
        d
        u
        c
        t
        w
        i
        t
        h
        t
        h
        i
        s
        i
        s
        a
        p
        a
        c
        k
        f
        o
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(MedicinalProductPackaged, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackaged, self).elementProperties()
        js.extend([
            ("batchIdentifier", "batchIdentifier", MedicinalProductPackagedBatchIdentifier, True, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("marketingAuthorization", "marketingAuthorization", fhirreference.FHIRReference, False, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, True),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductPackagedBatchIdentifier(backboneelement.BackboneElement):
    """ 
    B
    a
    t
    c
    h
    n
    u
    m
    b
    e
    r
    i
    n
    g
    .
    """
    
    resource_type = "MedicinalProductPackagedBatchIdentifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.immediatePackaging = None
        """ 
        A
        n
        u
        m
        b
        e
        r
        a
        p
        p
        e
        a
        r
        i
        n
        g
        o
        n
        t
        h
        e
        i
        m
        m
        e
        d
        i
        a
        t
        e
        p
        a
        c
        k
        a
        g
        i
        n
        g
        (
        a
        n
        d
        n
        o
        t
        t
        h
        e
        o
        u
        t
        e
        r
        p
        a
        c
        k
        a
        g
        i
        n
        g
        )
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.outerPackaging = None
        """ 
        A
        n
        u
        m
        b
        e
        r
        a
        p
        p
        e
        a
        r
        i
        n
        g
        o
        n
        t
        h
        e
        o
        u
        t
        e
        r
        p
        a
        c
        k
        a
        g
        i
        n
        g
        o
        f
        a
        s
        p
        e
        c
        i
        f
        i
        c
        b
        a
        t
        c
        h
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(MedicinalProductPackagedBatchIdentifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackagedBatchIdentifier, self).elementProperties()
        js.extend([
            ("immediatePackaging", "immediatePackaging", identifier.Identifier, False, None, False),
            ("outerPackaging", "outerPackaging", identifier.Identifier, False, None, True),
        ])
        return js


class MedicinalProductPackagedPackageItem(backboneelement.BackboneElement):
    """ 
    A
    p
    a
    c
    k
    a
    g
    i
    n
    g
    i
    t
    e
    m
    ,
    a
    s
    a
    c
    o
    n
    t
    a
    i
    n
    e
    d
    f
    o
    r
    m
    e
    d
    i
    c
    i
    n
    e
    ,
    p
    o
    s
    s
    i
    b
    l
    y
    w
    i
    t
    h
    o
    t
    h
    e
    r
    p
    a
    c
    k
    a
    g
    i
    n
    g
    i
    t
    e
    m
    s
    w
    i
    t
    h
    i
    n
    .
    """
    
    resource_type = "MedicinalProductPackagedPackageItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alternateMaterial = None
        """ 
        A
        p
        o
        s
        s
        i
        b
        l
        e
        a
        l
        t
        e
        r
        n
        a
        t
        e
        m
        a
        t
        e
        r
        i
        a
        l
        f
        o
        r
        t
        h
        e
        p
        a
        c
        k
        a
        g
        i
        n
        g
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.device = None
        """ 
        A
        d
        e
        v
        i
        c
        e
        a
        c
        c
        o
        m
        p
        a
        n
        y
        i
        n
        g
        a
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        I
        n
        c
        l
        u
        d
        i
        n
        g
        p
        o
        s
        s
        i
        b
        l
        y
        D
        a
        t
        a
        C
        a
        r
        r
        i
        e
        r
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
        
        self.manufacturedItem = None
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
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        i
        s
        P
        a
        c
        k
        a
        g
        e
        I
        t
        e
        m
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.material = None
        """ 
        M
        a
        t
        e
        r
        i
        a
        l
        t
        y
        p
        e
        o
        f
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
        i
        t
        e
        m
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        
        self.packageItem = None
        """ 
        A
        l
        l
        o
        w
        s
        c
        o
        n
        t
        a
        i
        n
        e
        r
        s
        w
        i
        t
        h
        i
        n
        c
        o
        n
        t
        a
        i
        n
        e
        r
        s
        .
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """
        
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
        f
        t
        h
        i
        s
        p
        a
        c
        k
        a
        g
        e
        i
        n
        t
        h
        e
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
        ,
        a
        t
        t
        h
        e
        c
        u
        r
        r
        e
        n
        t
        l
        e
        v
        e
        l
        o
        f
        p
        a
        c
        k
        a
        g
        i
        n
        g
        .
        T
        h
        e
        o
        u
        t
        e
        r
        m
        o
        s
        t
        i
        s
        a
        l
        w
        a
        y
        s
        1
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.shelfLifeStorage = None
        """ 
        S
        h
        e
        l
        f
        L
        i
        f
        e
        a
        n
        d
        s
        t
        o
        r
        a
        g
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
        List of `ProductShelfLife` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        h
        e
        p
        h
        y
        s
        i
        c
        a
        l
        t
        y
        p
        e
        o
        f
        t
        h
        e
        c
        o
        n
        t
        a
        i
        n
        e
        r
        o
        f
        t
        h
        e
        m
        e
        d
        i
        c
        i
        n
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductPackagedPackageItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackagedPackageItem, self).elementProperties()
        js.extend([
            ("alternateMaterial", "alternateMaterial", codeableconcept.CodeableConcept, True, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("manufacturedItem", "manufacturedItem", fhirreference.FHIRReference, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("material", "material", codeableconcept.CodeableConcept, True, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
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
    from . import marketingstatus
except ImportError:
    marketingstatus = sys.modules[__package__ + '.marketingstatus']
try:
    from . import prodcharacteristic
except ImportError:
    prodcharacteristic = sys.modules[__package__ + '.prodcharacteristic']
try:
    from . import productshelflife
except ImportError:
    productshelflife = sys.modules[__package__ + '.productshelflife']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
