#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class DeviceDefinition(domainresource.DomainResource):
    """ 
    A
    n
    i
    n
    s
    t
    a
    n
    c
    e
    o
    f
    a
    m
    e
    d
    i
    c
    a
    l
    -
    r
    e
    l
    a
    t
    e
    d
    c
    o
    m
    p
    o
    n
    e
    n
    t
    o
    f
    a
    m
    e
    d
    i
    c
    a
    l
    d
    e
    v
    i
    c
    e
    .
    
    
    T
    h
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
    ,
    o
    p
    e
    r
    a
    t
    i
    o
    n
    a
    l
    s
    t
    a
    t
    u
    s
    a
    n
    d
    c
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    o
    f
    a
    m
    e
    d
    i
    c
    a
    l
    -
    r
    e
    l
    a
    t
    e
    d
    c
    o
    m
    p
    o
    n
    e
    n
    t
    o
    f
    a
    m
    e
    d
    i
    c
    a
    l
    d
    e
    v
    i
    c
    e
    .
    
    """
    
    resource_type = "DeviceDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capability = None
        """ 
        D
        e
        v
        i
        c
        e
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
        .
        List of `DeviceDefinitionCapability` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        f
        o
        r
        h
        u
        m
        a
        n
        /
        o
        r
        g
        a
        n
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
        s
        u
        p
        p
        o
        r
        t
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.deviceName = None
        """ 
        A
        n
        a
        m
        e
        g
        i
        v
        e
        n
        t
        o
        t
        h
        e
        d
        e
        v
        i
        c
        e
        t
        o
        i
        d
        e
        n
        t
        i
        f
        y
        i
        t
        .
        List of `DeviceDefinitionDeviceName` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        I
        n
        s
        t
        a
        n
        c
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
        
        self.languageCode = None
        """ 
        L
        a
        n
        g
        u
        a
        g
        e
        c
        o
        d
        e
        f
        o
        r
        t
        h
        e
        h
        u
        m
        a
        n
        -
        r
        e
        a
        d
        a
        b
        l
        e
        t
        e
        x
        t
        s
        t
        r
        i
        n
        g
        s
        p
        r
        o
        d
        u
        c
        e
        d
        b
        y
        t
        h
        e
        d
        e
        v
        i
        c
        e
        (
        a
        l
        l
        s
        u
        p
        p
        o
        r
        t
        e
        d
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.manufacturerReference = None
        """ 
        N
        a
        m
        e
        o
        f
        d
        e
        v
        i
        c
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
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.manufacturerString = None
        """ 
        N
        a
        m
        e
        o
        f
        d
        e
        v
        i
        c
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
        r
        .
        Type `str`. """
        
        self.material = None
        """ 
        A
        s
        u
        b
        s
        t
        a
        n
        c
        e
        u
        s
        e
        d
        t
        o
        c
        r
        e
        a
        t
        e
        t
        h
        e
        m
        a
        t
        e
        r
        i
        a
        l
        (
        s
        )
        o
        f
        w
        h
        i
        c
        h
        t
        h
        e
        d
        e
        v
        i
        c
        e
        i
        s
        m
        a
        d
        e
        .
        List of `DeviceDefinitionMaterial` items (represented as `dict` in JSON). """
        
        self.modelNumber = None
        """ 
        T
        h
        e
        m
        o
        d
        e
        l
        n
        u
        m
        b
        e
        r
        f
        o
        r
        t
        h
        e
        d
        e
        v
        i
        c
        e
        .
        Type `str`. """
        
        self.note = None
        """ 
        D
        e
        v
        i
        c
        e
        n
        o
        t
        e
        s
        a
        n
        d
        c
        o
        m
        m
        e
        n
        t
        s
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.onlineInformation = None
        """ 
        A
        c
        c
        e
        s
        s
        t
        o
        o
        n
        -
        l
        i
        n
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
        Type `str`. """
        
        self.owner = None
        """ 
        O
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        r
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
        f
        o
        r
        d
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.parentDevice = None
        """ 
        T
        h
        e
        p
        a
        r
        e
        n
        t
        d
        e
        v
        i
        c
        e
        i
        t
        c
        a
        n
        b
        e
        p
        a
        r
        t
        o
        f
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        
        self.property = None
        """ 
        T
        h
        e
        a
        c
        t
        u
        a
        l
        c
        o
        n
        f
        i
        g
        u
        r
        a
        t
        i
        o
        n
        s
        e
        t
        t
        i
        n
        g
        s
        o
        f
        a
        d
        e
        v
        i
        c
        e
        a
        s
        i
        t
        a
        c
        t
        u
        a
        l
        l
        y
        o
        p
        e
        r
        a
        t
        e
        s
        ,
        e
        .
        g
        .
        ,
        r
        e
        g
        u
        l
        a
        t
        i
        o
        n
        s
        t
        a
        t
        u
        s
        ,
        t
        i
        m
        e
        p
        r
        o
        p
        e
        r
        t
        i
        e
        s
        .
        List of `DeviceDefinitionProperty` items (represented as `dict` in JSON). """
        
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
        e
        d
        e
        v
        i
        c
        e
        p
        r
        e
        s
        e
        n
        t
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
        i
        n
        g
        (
        e
        .
        g
        .
        t
        h
        e
        n
        u
        m
        b
        e
        r
        o
        f
        d
        e
        v
        i
        c
        e
        s
        p
        r
        e
        s
        e
        n
        t
        i
        n
        a
        p
        a
        c
        k
        ,
        o
        r
        t
        h
        e
        n
        u
        m
        b
        e
        r
        o
        f
        d
        e
        v
        i
        c
        e
        s
        i
        n
        t
        h
        e
        s
        a
        m
        e
        p
        a
        c
        k
        a
        g
        e
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
        )
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.safety = None
        """ 
        S
        a
        f
        e
        t
        y
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
        d
        e
        v
        i
        c
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        
        self.specialization = None
        """ 
        T
        h
        e
        c
        a
        p
        a
        b
        i
        l
        i
        t
        i
        e
        s
        s
        u
        p
        p
        o
        r
        t
        e
        d
        o
        n
        a
        d
        e
        v
        i
        c
        e
        ,
        t
        h
        e
        s
        t
        a
        n
        d
        a
        r
        d
        s
        t
        o
        w
        h
        i
        c
        h
        t
        h
        e
        d
        e
        v
        i
        c
        e
        c
        o
        n
        f
        o
        r
        m
        s
        f
        o
        r
        a
        p
        a
        r
        t
        i
        c
        u
        l
        a
        r
        p
        u
        r
        p
        o
        s
        e
        ,
        a
        n
        d
        u
        s
        e
        d
        f
        o
        r
        t
        h
        e
        c
        o
        m
        m
        u
        n
        i
        c
        a
        t
        i
        o
        n
        .
        List of `DeviceDefinitionSpecialization` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        W
        h
        a
        t
        k
        i
        n
        d
        o
        f
        d
        e
        v
        i
        c
        e
        o
        r
        d
        e
        v
        i
        c
        e
        s
        y
        s
        t
        e
        m
        t
        h
        i
        s
        i
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udiDeviceIdentifier = None
        """ 
        U
        n
        i
        q
        u
        e
        D
        e
        v
        i
        c
        e
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
        (
        U
        D
        I
        )
        B
        a
        r
        c
        o
        d
        e
        s
        t
        r
        i
        n
        g
        .
        List of `DeviceDefinitionUdiDeviceIdentifier` items (represented as `dict` in JSON). """
        
        self.url = None
        """ 
        N
        e
        t
        w
        o
        r
        k
        a
        d
        d
        r
        e
        s
        s
        t
        o
        c
        o
        n
        t
        a
        c
        t
        d
        e
        v
        i
        c
        e
        .
        Type `str`. """
        
        self.version = None
        """ 
        A
        v
        a
        i
        l
        a
        b
        l
        e
        v
        e
        r
        s
        i
        o
        n
        s
        .
        List of `str` items. """
        
        super(DeviceDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinition, self).elementProperties()
        js.extend([
            ("capability", "capability", DeviceDefinitionCapability, True, None, False),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("deviceName", "deviceName", DeviceDefinitionDeviceName, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, True, None, False),
            ("manufacturerReference", "manufacturerReference", fhirreference.FHIRReference, False, "manufacturer", False),
            ("manufacturerString", "manufacturerString", str, False, "manufacturer", False),
            ("material", "material", DeviceDefinitionMaterial, True, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("onlineInformation", "onlineInformation", str, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parentDevice", "parentDevice", fhirreference.FHIRReference, False, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("property", "property", DeviceDefinitionProperty, True, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False),
            ("specialization", "specialization", DeviceDefinitionSpecialization, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("udiDeviceIdentifier", "udiDeviceIdentifier", DeviceDefinitionUdiDeviceIdentifier, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """ 
    D
    e
    v
    i
    c
    e
    c
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    .
    """
    
    resource_type = "DeviceDefinitionCapability"
    
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
        c
        a
        p
        a
        b
        i
        l
        i
        t
        y
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        c
        a
        p
        a
        b
        i
        l
        i
        t
        y
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceDefinitionCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionCapability, self).elementProperties()
        js.extend([
            ("description", "description", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """ 
    A
    n
    a
    m
    e
    g
    i
    v
    e
    n
    t
    o
    t
    h
    e
    d
    e
    v
    i
    c
    e
    t
    o
    i
    d
    e
    n
    t
    i
    f
    y
    i
    t
    .
    """
    
    resource_type = "DeviceDefinitionDeviceName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ 
        T
        h
        e
        n
        a
        m
        e
        o
        f
        t
        h
        e
        d
        e
        v
        i
        c
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        u
        d
        i
        -
        l
        a
        b
        e
        l
        -
        n
        a
        m
        e
        |
        u
        s
        e
        r
        -
        f
        r
        i
        e
        n
        d
        l
        y
        -
        n
        a
        m
        e
        |
        p
        a
        t
        i
        e
        n
        t
        -
        r
        e
        p
        o
        r
        t
        e
        d
        -
        n
        a
        m
        e
        |
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
        -
        n
        a
        m
        e
        |
        m
        o
        d
        e
        l
        -
        n
        a
        m
        e
        |
        o
        t
        h
        e
        r
        .
        Type `str`. """
        
        super(DeviceDefinitionDeviceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """ 
    A
    s
    u
    b
    s
    t
    a
    n
    c
    e
    u
    s
    e
    d
    t
    o
    c
    r
    e
    a
    t
    e
    t
    h
    e
    m
    a
    t
    e
    r
    i
    a
    l
    (
    s
    )
    o
    f
    w
    h
    i
    c
    h
    t
    h
    e
    d
    e
    v
    i
    c
    e
    i
    s
    m
    a
    d
    e
    .
    """
    
    resource_type = "DeviceDefinitionMaterial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergenicIndicator = None
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
        s
        u
        b
        s
        t
        a
        n
        c
        e
        i
        s
        a
        k
        n
        o
        w
        n
        o
        r
        s
        u
        s
        p
        e
        c
        t
        e
        d
        a
        l
        l
        e
        r
        g
        e
        n
        .
        Type `bool`. """
        
        self.alternate = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        a
        n
        a
        l
        t
        e
        r
        n
        a
        t
        i
        v
        e
        m
        a
        t
        e
        r
        i
        a
        l
        o
        f
        t
        h
        e
        d
        e
        v
        i
        c
        e
        .
        Type `bool`. """
        
        self.substance = None
        """ 
        T
        h
        e
        s
        u
        b
        s
        t
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceDefinitionMaterial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionMaterial, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("alternate", "alternate", bool, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    a
    c
    t
    u
    a
    l
    c
    o
    n
    f
    i
    g
    u
    r
    a
    t
    i
    o
    n
    s
    e
    t
    t
    i
    n
    g
    s
    o
    f
    a
    d
    e
    v
    i
    c
    e
    a
    s
    i
    t
    a
    c
    t
    u
    a
    l
    l
    y
    o
    p
    e
    r
    a
    t
    e
    s
    ,
    e
    .
    g
    .
    ,
    r
    e
    g
    u
    l
    a
    t
    i
    o
    n
    s
    t
    a
    t
    u
    s
    ,
    t
    i
    m
    e
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    .
    """
    
    resource_type = "DeviceDefinitionProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ 
        C
        o
        d
        e
        t
        h
        a
        t
        s
        p
        e
        c
        i
        f
        i
        e
        s
        t
        h
        e
        p
        r
        o
        p
        e
        r
        t
        y
        D
        e
        v
        i
        c
        e
        D
        e
        f
        i
        n
        i
        t
        i
        o
        n
        P
        r
        o
        p
        e
        t
        y
        C
        o
        d
        e
        (
        E
        x
        t
        e
        n
        s
        i
        b
        l
        e
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCode = None
        """ 
        P
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        a
        s
        a
        c
        o
        d
        e
        ,
        e
        .
        g
        .
        ,
        N
        T
        P
        4
        (
        s
        y
        n
        c
        e
        d
        t
        o
        N
        T
        P
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ 
        P
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        a
        s
        a
        q
        u
        a
        n
        t
        i
        t
        y
        .
        List of `Quantity` items (represented as `dict` in JSON). """
        
        super(DeviceDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
        ])
        return js


class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    c
    a
    p
    a
    b
    i
    l
    i
    t
    i
    e
    s
    s
    u
    p
    p
    o
    r
    t
    e
    d
    o
    n
    a
    d
    e
    v
    i
    c
    e
    ,
    t
    h
    e
    s
    t
    a
    n
    d
    a
    r
    d
    s
    t
    o
    w
    h
    i
    c
    h
    t
    h
    e
    d
    e
    v
    i
    c
    e
    c
    o
    n
    f
    o
    r
    m
    s
    f
    o
    r
    a
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    p
    u
    r
    p
    o
    s
    e
    ,
    a
    n
    d
    u
    s
    e
    d
    f
    o
    r
    t
    h
    e
    c
    o
    m
    m
    u
    n
    i
    c
    a
    t
    i
    o
    n
    .
    """
    
    resource_type = "DeviceDefinitionSpecialization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.systemType = None
        """ 
        T
        h
        e
        s
        t
        a
        n
        d
        a
        r
        d
        t
        h
        a
        t
        i
        s
        u
        s
        e
        d
        t
        o
        o
        p
        e
        r
        a
        t
        e
        a
        n
        d
        c
        o
        m
        m
        u
        n
        i
        c
        a
        t
        e
        .
        Type `str`. """
        
        self.version = None
        """ 
        T
        h
        e
        v
        e
        r
        s
        i
        o
        n
        o
        f
        t
        h
        e
        s
        t
        a
        n
        d
        a
        r
        d
        t
        h
        a
        t
        i
        s
        u
        s
        e
        d
        t
        o
        o
        p
        e
        r
        a
        t
        e
        a
        n
        d
        c
        o
        m
        m
        u
        n
        i
        c
        a
        t
        e
        .
        Type `str`. """
        
        super(DeviceDefinitionSpecialization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    """ 
    U
    n
    i
    q
    u
    e
    D
    e
    v
    i
    c
    e
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
    (
    U
    D
    I
    )
    B
    a
    r
    c
    o
    d
    e
    s
    t
    r
    i
    n
    g
    .
    
    
    U
    n
    i
    q
    u
    e
    d
    e
    v
    i
    c
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
    (
    U
    D
    I
    )
    a
    s
    s
    i
    g
    n
    e
    d
    t
    o
    d
    e
    v
    i
    c
    e
    l
    a
    b
    e
    l
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
    e
    D
    e
    v
    i
    c
    e
    m
    a
    y
    i
    n
    c
    l
    u
    d
    e
    m
    u
    l
    t
    i
    p
    l
    e
    u
    d
    i
    C
    a
    r
    r
    i
    e
    r
    s
    a
    s
    i
    t
    e
    i
    t
    h
    e
    r
    m
    a
    y
    i
    n
    c
    l
    u
    d
    e
    j
    u
    s
    t
    t
    h
    e
    u
    d
    i
    C
    a
    r
    r
    i
    e
    r
    f
    o
    r
    t
    h
    e
    j
    u
    r
    i
    s
    d
    i
    c
    t
    i
    o
    n
    i
    t
    i
    s
    s
    o
    l
    d
    ,
    o
    r
    f
    o
    r
    m
    u
    l
    t
    i
    p
    l
    e
    j
    u
    r
    i
    s
    d
    i
    c
    t
    i
    o
    n
    s
    i
    t
    c
    o
    u
    l
    d
    h
    a
    v
    e
    b
    e
    e
    n
    s
    o
    l
    d
    .
    
    """
    
    resource_type = "DeviceDefinitionUdiDeviceIdentifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.deviceIdentifier = None
        """ 
        T
        h
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
        t
        h
        a
        t
        i
        s
        t
        o
        b
        e
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        e
        v
        e
        r
        y
        D
        e
        v
        i
        c
        e
        t
        h
        a
        t
        r
        e
        f
        e
        r
        e
        n
        c
        e
        s
        t
        h
        i
        s
        D
        e
        v
        i
        c
        e
        D
        e
        f
        i
        n
        t
        i
        i
        o
        n
        f
        o
        r
        t
        h
        e
        i
        s
        s
        u
        e
        r
        a
        n
        d
        j
        u
        r
        i
        s
        d
        i
        c
        a
        t
        i
        o
        n
        p
        o
        r
        v
        i
        d
        e
        d
        i
        n
        t
        h
        e
        D
        e
        v
        i
        c
        e
        D
        e
        f
        i
        n
        i
        t
        i
        o
        n
        .
        u
        d
        i
        D
        e
        v
        i
        c
        e
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
        Type `str`. """
        
        self.issuer = None
        """ 
        T
        h
        e
        o
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        t
        h
        a
        t
        a
        s
        s
        i
        g
        n
        s
        t
        h
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
        a
        l
        g
        o
        r
        i
        t
        h
        m
        .
        Type `str`. """
        
        self.jurisdiction = None
        """ 
        T
        h
        e
        j
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        t
        o
        w
        h
        i
        c
        h
        t
        h
        e
        d
        e
        v
        i
        c
        e
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
        a
        p
        p
        l
        i
        e
        s
        .
        Type `str`. """
        
        super(DeviceDefinitionUdiDeviceIdentifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionUdiDeviceIdentifier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", str, False, None, True),
            ("issuer", "issuer", str, False, None, True),
            ("jurisdiction", "jurisdiction", str, False, None, True),
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
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
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
