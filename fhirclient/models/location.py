#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Location) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Location(domainresource.DomainResource):
    """ 
    D
    e
    t
    a
    i
    l
    s
    a
    n
    d
    p
    o
    s
    i
    t
    i
    o
    n
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
    f
    o
    r
    a
    p
    h
    y
    s
    i
    c
    a
    l
    p
    l
    a
    c
    e
    .
    
    
    D
    e
    t
    a
    i
    l
    s
    a
    n
    d
    p
    o
    s
    i
    t
    i
    o
    n
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
    f
    o
    r
    a
    p
    h
    y
    s
    i
    c
    a
    l
    p
    l
    a
    c
    e
    w
    h
    e
    r
    e
    s
    e
    r
    v
    i
    c
    e
    s
    a
    r
    e
    p
    r
    o
    v
    i
    d
    e
    d
    a
    n
    d
    r
    e
    s
    o
    u
    r
    c
    e
    s
    a
    n
    d
    p
    a
    r
    t
    i
    c
    i
    p
    a
    n
    t
    s
    m
    a
    y
    b
    e
    s
    t
    o
    r
    e
    d
    ,
    f
    o
    u
    n
    d
    ,
    c
    o
    n
    t
    a
    i
    n
    e
    d
    ,
    o
    r
    a
    c
    c
    o
    m
    m
    o
    d
    a
    t
    e
    d
    .
    
    """
    
    resource_type = "Location"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ 
        P
        h
        y
        s
        i
        c
        a
        l
        l
        o
        c
        a
        t
        i
        o
        n
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.alias = None
        """ 
        A
        l
        i
        s
        t
        o
        f
        a
        l
        t
        e
        r
        n
        a
        t
        e
        n
        a
        m
        e
        s
        t
        h
        a
        t
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        i
        s
        k
        n
        o
        w
        n
        a
        s
        ,
        o
        r
        w
        a
        s
        k
        n
        o
        w
        n
        a
        s
        ,
        i
        n
        t
        h
        e
        p
        a
        s
        t
        .
        List of `str` items. """
        
        self.availabilityExceptions = None
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
        a
        v
        a
        i
        l
        a
        b
        i
        l
        i
        t
        y
        e
        x
        c
        e
        p
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
        self.description = None
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
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        t
        h
        a
        t
        c
        o
        u
        l
        d
        b
        e
        d
        i
        s
        p
        l
        a
        y
        e
        d
        a
        s
        f
        u
        r
        t
        h
        e
        r
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
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        b
        e
        y
        o
        n
        d
        i
        t
        s
        n
        a
        m
        e
        .
        Type `str`. """
        
        self.endpoint = None
        """ 
        T
        e
        c
        h
        n
        i
        c
        a
        l
        e
        n
        d
        p
        o
        i
        n
        t
        s
        p
        r
        o
        v
        i
        d
        i
        n
        g
        a
        c
        c
        e
        s
        s
        t
        o
        s
        e
        r
        v
        i
        c
        e
        s
        o
        p
        e
        r
        a
        t
        e
        d
        f
        o
        r
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.hoursOfOperation = None
        """ 
        W
        h
        a
        t
        d
        a
        y
        s
        /
        t
        i
        m
        e
        s
        d
        u
        r
        i
        n
        g
        a
        w
        e
        e
        k
        i
        s
        t
        h
        i
        s
        l
        o
        c
        a
        t
        i
        o
        n
        u
        s
        u
        a
        l
        l
        y
        o
        p
        e
        n
        .
        List of `LocationHoursOfOperation` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        U
        n
        i
        q
        u
        e
        c
        o
        d
        e
        o
        r
        n
        u
        m
        b
        e
        r
        i
        d
        e
        n
        t
        i
        f
        y
        i
        n
        g
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        t
        o
        i
        t
        s
        u
        s
        e
        r
        s
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
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
        p
        r
        o
        v
        i
        s
        i
        o
        n
        i
        n
        g
        a
        n
        d
        u
        p
        k
        e
        e
        p
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.mode = None
        """ 
        i
        n
        s
        t
        a
        n
        c
        e
        |
        k
        i
        n
        d
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        a
        s
        u
        s
        e
        d
        b
        y
        h
        u
        m
        a
        n
        s
        .
        Type `str`. """
        
        self.operationalStatus = None
        """ 
        T
        h
        e
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
        o
        f
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        (
        t
        y
        p
        i
        c
        a
        l
        l
        y
        o
        n
        l
        y
        f
        o
        r
        a
        b
        e
        d
        /
        r
        o
        o
        m
        )
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ 
        A
        n
        o
        t
        h
        e
        r
        L
        o
        c
        a
        t
        i
        o
        n
        t
        h
        i
        s
        o
        n
        e
        i
        s
        p
        h
        y
        s
        i
        c
        a
        l
        l
        y
        a
        p
        a
        r
        t
        o
        f
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.physicalType = None
        """ 
        P
        h
        y
        s
        i
        c
        a
        l
        f
        o
        r
        m
        o
        f
        t
        h
        e
        l
        o
        c
        a
        t
        i
        o
        n
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.position = None
        """ 
        T
        h
        e
        a
        b
        s
        o
        l
        u
        t
        e
        g
        e
        o
        g
        r
        a
        p
        h
        i
        c
        l
        o
        c
        a
        t
        i
        o
        n
        .
        Type `LocationPosition` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        a
        c
        t
        i
        v
        e
        |
        s
        u
        s
        p
        e
        n
        d
        e
        d
        |
        i
        n
        a
        c
        t
        i
        v
        e
        .
        Type `str`. """
        
        self.telecom = None
        """ 
        C
        o
        n
        t
        a
        c
        t
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
        l
        o
        c
        a
        t
        i
        o
        n
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        y
        p
        e
        o
        f
        f
        u
        n
        c
        t
        i
        o
        n
        p
        e
        r
        f
        o
        r
        m
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(Location, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("hoursOfOperation", "hoursOfOperation", LocationHoursOfOperation, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("operationalStatus", "operationalStatus", coding.Coding, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("position", "position", LocationPosition, False, None, False),
            ("status", "status", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class LocationHoursOfOperation(backboneelement.BackboneElement):
    """ 
    W
    h
    a
    t
    d
    a
    y
    s
    /
    t
    i
    m
    e
    s
    d
    u
    r
    i
    n
    g
    a
    w
    e
    e
    k
    i
    s
    t
    h
    i
    s
    l
    o
    c
    a
    t
    i
    o
    n
    u
    s
    u
    a
    l
    l
    y
    o
    p
    e
    n
    .
    """
    
    resource_type = "LocationHoursOfOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        """ 
        T
        h
        e
        L
        o
        c
        a
        t
        i
        o
        n
        i
        s
        o
        p
        e
        n
        a
        l
        l
        d
        a
        y
        .
        Type `bool`. """
        
        self.closingTime = None
        """ 
        T
        i
        m
        e
        t
        h
        a
        t
        t
        h
        e
        L
        o
        c
        a
        t
        i
        o
        n
        c
        l
        o
        s
        e
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None
        """ 
        m
        o
        n
        |
        t
        u
        e
        |
        w
        e
        d
        |
        t
        h
        u
        |
        f
        r
        i
        |
        s
        a
        t
        |
        s
        u
        n
        .
        List of `str` items. """
        
        self.openingTime = None
        """ 
        T
        i
        m
        e
        t
        h
        a
        t
        t
        h
        e
        L
        o
        c
        a
        t
        i
        o
        n
        o
        p
        e
        n
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(LocationHoursOfOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("closingTime", "closingTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("openingTime", "openingTime", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class LocationPosition(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    a
    b
    s
    o
    l
    u
    t
    e
    g
    e
    o
    g
    r
    a
    p
    h
    i
    c
    l
    o
    c
    a
    t
    i
    o
    n
    .
    
    
    T
    h
    e
    a
    b
    s
    o
    l
    u
    t
    e
    g
    e
    o
    g
    r
    a
    p
    h
    i
    c
    l
    o
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
    L
    o
    c
    a
    t
    i
    o
    n
    ,
    e
    x
    p
    r
    e
    s
    s
    e
    d
    u
    s
    i
    n
    g
    t
    h
    e
    W
    G
    S
    8
    4
    d
    a
    t
    u
    m
    (
    T
    h
    i
    s
    i
    s
    t
    h
    e
    s
    a
    m
    e
    c
    o
    -
    o
    r
    d
    i
    n
    a
    t
    e
    s
    y
    s
    t
    e
    m
    u
    s
    e
    d
    i
    n
    K
    M
    L
    )
    .
    
    """
    
    resource_type = "LocationPosition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altitude = None
        """ 
        A
        l
        t
        i
        t
        u
        d
        e
        w
        i
        t
        h
        W
        G
        S
        8
        4
        d
        a
        t
        u
        m
        .
        Type `float`. """
        
        self.latitude = None
        """ 
        L
        a
        t
        i
        t
        u
        d
        e
        w
        i
        t
        h
        W
        G
        S
        8
        4
        d
        a
        t
        u
        m
        .
        Type `float`. """
        
        self.longitude = None
        """ 
        L
        o
        n
        g
        i
        t
        u
        d
        e
        w
        i
        t
        h
        W
        G
        S
        8
        4
        d
        a
        t
        u
        m
        .
        Type `float`. """
        
        super(LocationPosition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, False, None, False),
            ("latitude", "latitude", float, False, None, True),
            ("longitude", "longitude", float, False, None, True),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
