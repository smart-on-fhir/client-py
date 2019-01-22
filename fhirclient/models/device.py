#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Device) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Device(domainresource.DomainResource):
    """ 
    I
    t
    e
    m
    u
    s
    e
    d
    i
    n
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
    .
    
    
    A
    t
    y
    p
    e
    o
    f
    a
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
    i
    n
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
    w
    i
    t
    h
    o
    u
    t
    b
    e
    i
    n
    g
    s
    u
    b
    s
    t
    a
    n
    t
    i
    a
    l
    l
    y
    c
    h
    a
    n
    g
    e
    d
    t
    h
    r
    o
    u
    g
    h
    t
    h
    a
    t
    a
    c
    t
    i
    v
    i
    t
    y
    .
    T
    h
    e
    d
    e
    v
    i
    c
    e
    m
    a
    y
    b
    e
    a
    m
    e
    d
    i
    c
    a
    l
    o
    r
    n
    o
    n
    -
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
    
    resource_type = "Device"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        
        self.definition = None
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
        d
        e
        f
        i
        n
        i
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
        d
        e
        v
        i
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deviceName = None
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
        a
        s
        g
        i
        v
        e
        n
        b
        y
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
        r
        .
        List of `DeviceDeviceName` items (represented as `dict` in JSON). """
        
        self.distinctIdentifier = None
        """ 
        T
        h
        e
        d
        i
        s
        t
        i
        n
        c
        t
        i
        d
        e
        n
        t
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
        t
        r
        i
        n
        g
        .
        Type `str`. """
        
        self.expirationDate = None
        """ 
        D
        a
        t
        e
        a
        n
        d
        t
        i
        m
        e
        o
        f
        e
        x
        p
        i
        r
        y
        o
        f
        t
        h
        i
        s
        d
        e
        v
        i
        c
        e
        (
        i
        f
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
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
        
        self.location = None
        """ 
        W
        h
        e
        r
        e
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
        f
        o
        u
        n
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ 
        L
        o
        t
        n
        u
        m
        b
        e
        r
        o
        f
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
        .
        Type `str`. """
        
        self.manufactureDate = None
        """ 
        D
        a
        t
        e
        w
        h
        e
        n
        t
        h
        e
        d
        e
        v
        i
        c
        e
        w
        a
        s
        m
        a
        d
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.manufacturer = None
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
        
        self.parent = None
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partNumber = None
        """ 
        T
        h
        e
        p
        a
        r
        t
        n
        u
        m
        b
        e
        r
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
        
        self.patient = None
        """ 
        P
        a
        t
        i
        e
        n
        t
        t
        o
        w
        h
        o
        m
        D
        e
        v
        i
        c
        e
        i
        s
        a
        f
        f
        i
        x
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
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
        List of `DeviceProperty` items (represented as `dict` in JSON). """
        
        self.safety = None
        """ 
        S
        a
        f
        e
        t
        y
        C
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
        D
        e
        v
        i
        c
        e
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serialNumber = None
        """ 
        S
        e
        r
        i
        a
        l
        n
        u
        m
        b
        e
        r
        a
        s
        s
        i
        g
        n
        e
        d
        b
        y
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
        r
        .
        Type `str`. """
        
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
        List of `DeviceSpecialization` items (represented as `dict` in JSON). """
        
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
        
        self.statusReason = None
        """ 
        o
        n
        l
        i
        n
        e
        |
        p
        a
        u
        s
        e
        d
        |
        s
        t
        a
        n
        d
        b
        y
        |
        o
        f
        f
        l
        i
        n
        e
        |
        n
        o
        t
        -
        r
        e
        a
        d
        y
        |
        t
        r
        a
        n
        s
        d
        u
        c
        -
        d
        i
        s
        c
        o
        n
        |
        h
        w
        -
        d
        i
        s
        c
        o
        n
        |
        o
        f
        f
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        h
        e
        k
        i
        n
        d
        o
        r
        t
        y
        p
        e
        o
        f
        d
        e
        v
        i
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udiCarrier = None
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
        List of `DeviceUdiCarrier` items (represented as `dict` in JSON). """
        
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
        T
        h
        e
        a
        c
        t
        u
        a
        l
        d
        e
        s
        i
        g
        n
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
        o
        r
        s
        o
        f
        t
        w
        a
        r
        e
        v
        e
        r
        s
        i
        o
        n
        r
        u
        n
        n
        i
        n
        g
        o
        n
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
        List of `DeviceVersion` items (represented as `dict` in JSON). """
        
        super(Device, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("definition", "definition", fhirreference.FHIRReference, False, None, False),
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False),
            ("distinctIdentifier", "distinctIdentifier", str, False, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("partNumber", "partNumber", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("property", "property", DeviceProperty, True, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("specialization", "specialization", DeviceSpecialization, True, None, False),
            ("status", "status", str, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", DeviceVersion, True, None, False),
        ])
        return js


from . import backboneelement

class DeviceDeviceName(backboneelement.BackboneElement):
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
    a
    s
    g
    i
    v
    e
    n
    b
    y
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
    r
    .
    
    
    T
    h
    i
    s
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
    r
    '
    s
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
    a
    s
    p
    r
    o
    v
    i
    d
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
    ,
    f
    r
    o
    m
    a
    U
    D
    I
    l
    a
    b
    e
    l
    ,
    o
    r
    b
    y
    a
    p
    e
    r
    s
    o
    n
    d
    e
    s
    c
    r
    i
    b
    i
    n
    g
    t
    h
    e
    D
    e
    v
    i
    c
    e
    .
    T
    h
    i
    s
    t
    y
    p
    i
    c
    a
    l
    l
    y
    w
    o
    u
    l
    d
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
    p
    e
    r
    s
    o
    n
    p
    r
    o
    v
    i
    d
    e
    s
    t
    h
    e
    n
    a
    m
    e
    (
    s
    )
    o
    r
    w
    h
    e
    n
    t
    h
    e
    d
    e
    v
    i
    c
    e
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
    o
    n
    e
    o
    f
    t
    h
    e
    n
    a
    m
    e
    s
    a
    v
    a
    i
    l
    a
    b
    l
    e
    f
    r
    o
    m
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
    
    """
    
    resource_type = "DeviceDeviceName"
    
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
        
        super(DeviceDeviceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class DeviceProperty(backboneelement.BackboneElement):
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
    
    resource_type = "DeviceProperty"
    
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
        
        super(DeviceProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
        ])
        return js


class DeviceSpecialization(backboneelement.BackboneElement):
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
    
    resource_type = "DeviceSpecialization"
    
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        
        super(DeviceSpecialization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", codeableconcept.CodeableConcept, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class DeviceUdiCarrier(backboneelement.BackboneElement):
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
    
    resource_type = "DeviceUdiCarrier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.carrierAIDC = None
        """ 
        U
        D
        I
        M
        a
        c
        h
        i
        n
        e
        R
        e
        a
        d
        a
        b
        l
        e
        B
        a
        r
        c
        o
        d
        e
        S
        t
        r
        i
        n
        g
        .
        Type `str`. """
        
        self.carrierHRF = None
        """ 
        U
        D
        I
        H
        u
        m
        a
        n
        R
        e
        a
        d
        a
        b
        l
        e
        B
        a
        r
        c
        o
        d
        e
        S
        t
        r
        i
        n
        g
        .
        Type `str`. """
        
        self.deviceIdentifier = None
        """ 
        M
        a
        n
        d
        a
        t
        o
        r
        y
        f
        i
        x
        e
        d
        p
        o
        r
        t
        i
        o
        n
        o
        f
        U
        D
        I
        .
        Type `str`. """
        
        self.entryType = None
        """ 
        b
        a
        r
        c
        o
        d
        e
        |
        r
        f
        i
        d
        |
        m
        a
        n
        u
        a
        l
        +
        .
        Type `str`. """
        
        self.issuer = None
        """ 
        U
        D
        I
        I
        s
        s
        u
        i
        n
        g
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
        .
        Type `str`. """
        
        self.jurisdiction = None
        """ 
        R
        e
        g
        i
        o
        n
        a
        l
        U
        D
        I
        a
        u
        t
        h
        o
        r
        i
        t
        y
        .
        Type `str`. """
        
        super(DeviceUdiCarrier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUdiCarrier, self).elementProperties()
        js.extend([
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("deviceIdentifier", "deviceIdentifier", str, False, None, False),
            ("entryType", "entryType", str, False, None, False),
            ("issuer", "issuer", str, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, False),
        ])
        return js


class DeviceVersion(backboneelement.BackboneElement):
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
    d
    e
    s
    i
    g
    n
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
    o
    r
    s
    o
    f
    t
    w
    a
    r
    e
    v
    e
    r
    s
    i
    o
    n
    r
    u
    n
    n
    i
    n
    g
    o
    n
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
    """
    
    resource_type = "DeviceVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.component = None
        """ 
        A
        s
        i
        n
        g
        l
        e
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
        t
        h
        e
        d
        e
        v
        i
        c
        e
        v
        e
        r
        s
        i
        o
        n
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
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
        t
        h
        e
        d
        e
        v
        i
        c
        e
        v
        e
        r
        s
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
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
        t
        e
        x
        t
        .
        Type `str`. """
        
        super(DeviceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("component", "component", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", str, False, None, True),
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
