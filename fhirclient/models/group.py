#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Group) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Group(domainresource.DomainResource):
    """ 
    G
    r
    o
    u
    p
    o
    f
    m
    u
    l
    t
    i
    p
    l
    e
    e
    n
    t
    i
    t
    i
    e
    s
    .
    
    
    R
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
    d
    e
    f
    i
    n
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
    e
    n
    t
    i
    t
    i
    e
    s
    t
    h
    a
    t
    m
    a
    y
    b
    e
    d
    i
    s
    c
    u
    s
    s
    e
    d
    o
    r
    a
    c
    t
    e
    d
    u
    p
    o
    n
    c
    o
    l
    l
    e
    c
    t
    i
    v
    e
    l
    y
    b
    u
    t
    w
    h
    i
    c
    h
    a
    r
    e
    n
    o
    t
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
    a
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
    v
    e
    l
    y
    ,
    a
    n
    d
    a
    r
    e
    n
    o
    t
    f
    o
    r
    m
    a
    l
    l
    y
    o
    r
    l
    e
    g
    a
    l
    l
    y
    r
    e
    c
    o
    g
    n
    i
    z
    e
    d
    ;
    i
    .
    e
    .
    a
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
    e
    n
    t
    i
    t
    i
    e
    s
    t
    h
    a
    t
    i
    s
    n
    '
    t
    a
    n
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
    
    """
    
    resource_type = "Group"
    
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
        g
        r
        o
        u
        p
        '
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
        
        self.actual = None
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
        o
        r
        a
        c
        t
        u
        a
        l
        .
        Type `bool`. """
        
        self.characteristic = None
        """ 
        I
        n
        c
        l
        u
        d
        e
        /
        E
        x
        c
        l
        u
        d
        e
        g
        r
        o
        u
        p
        m
        e
        m
        b
        e
        r
        s
        b
        y
        T
        r
        a
        i
        t
        .
        List of `GroupCharacteristic` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        K
        i
        n
        d
        o
        f
        G
        r
        o
        u
        p
        m
        e
        m
        b
        e
        r
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingEntity = None
        """ 
        E
        n
        t
        i
        t
        y
        t
        h
        a
        t
        i
        s
        t
        h
        e
        c
        u
        s
        t
        o
        d
        i
        a
        n
        o
        f
        t
        h
        e
        G
        r
        o
        u
        p
        '
        s
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.member = None
        """ 
        W
        h
        o
        o
        r
        w
        h
        a
        t
        i
        s
        i
        n
        g
        r
        o
        u
        p
        .
        List of `GroupMember` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        L
        a
        b
        e
        l
        f
        o
        r
        G
        r
        o
        u
        p
        .
        Type `str`. """
        
        self.quantity = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        m
        e
        m
        b
        e
        r
        s
        .
        Type `int`. """
        
        self.type = None
        """ 
        p
        e
        r
        s
        o
        n
        |
        a
        n
        i
        m
        a
        l
        |
        p
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        |
        d
        e
        v
        i
        c
        e
        |
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
        |
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
        Type `str`. """
        
        super(Group, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("actual", "actual", bool, False, None, True),
            ("characteristic", "characteristic", GroupCharacteristic, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingEntity", "managingEntity", fhirreference.FHIRReference, False, None, False),
            ("member", "member", GroupMember, True, None, False),
            ("name", "name", str, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import backboneelement

class GroupCharacteristic(backboneelement.BackboneElement):
    """ 
    I
    n
    c
    l
    u
    d
    e
    /
    E
    x
    c
    l
    u
    d
    e
    g
    r
    o
    u
    p
    m
    e
    m
    b
    e
    r
    s
    b
    y
    T
    r
    a
    i
    t
    .
    
    
    I
    d
    e
    n
    t
    i
    f
    i
    e
    s
    t
    r
    a
    i
    t
    s
    w
    h
    o
    s
    e
    p
    r
    e
    s
    e
    n
    c
    e
    r
    a
    b
    s
    e
    n
    c
    e
    i
    s
    s
    h
    a
    r
    e
    d
    b
    y
    m
    e
    m
    b
    e
    r
    s
    o
    f
    t
    h
    e
    g
    r
    o
    u
    p
    .
    
    """
    
    resource_type = "GroupCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        K
        i
        n
        d
        o
        f
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.exclude = None
        """ 
        G
        r
        o
        u
        p
        i
        n
        c
        l
        u
        d
        e
        s
        o
        r
        e
        x
        c
        l
        u
        d
        e
        s
        .
        Type `bool`. """
        
        self.period = None
        """ 
        P
        e
        r
        i
        o
        d
        o
        v
        e
        r
        w
        h
        i
        c
        h
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
        i
        s
        t
        e
        s
        t
        e
        d
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ 
        V
        a
        l
        u
        e
        h
        e
        l
        d
        b
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
        .
        Type `bool`. """
        
        self.valueCodeableConcept = None
        """ 
        V
        a
        l
        u
        e
        h
        e
        l
        d
        b
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
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ 
        V
        a
        l
        u
        e
        h
        e
        l
        d
        b
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
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        V
        a
        l
        u
        e
        h
        e
        l
        d
        b
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
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ 
        V
        a
        l
        u
        e
        h
        e
        l
        d
        b
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(GroupCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("exclude", "exclude", bool, False, None, True),
            ("period", "period", period.Period, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
        ])
        return js


class GroupMember(backboneelement.BackboneElement):
    """ 
    W
    h
    o
    o
    r
    w
    h
    a
    t
    i
    s
    i
    n
    g
    r
    o
    u
    p
    .
    
    
    I
    d
    e
    n
    t
    i
    f
    i
    e
    s
    t
    h
    e
    r
    e
    s
    o
    u
    r
    c
    e
    i
    n
    s
    t
    a
    n
    c
    e
    s
    t
    h
    a
    t
    a
    r
    e
    m
    e
    m
    b
    e
    r
    s
    o
    f
    t
    h
    e
    g
    r
    o
    u
    p
    .
    
    """
    
    resource_type = "GroupMember"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entity = None
        """ 
        R
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
        g
        r
        o
        u
        p
        m
        e
        m
        b
        e
        r
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.inactive = None
        """ 
        I
        f
        m
        e
        m
        b
        e
        r
        i
        s
        n
        o
        l
        o
        n
        g
        e
        r
        i
        n
        g
        r
        o
        u
        p
        .
        Type `bool`. """
        
        self.period = None
        """ 
        P
        e
        r
        i
        o
        d
        m
        e
        m
        b
        e
        r
        b
        e
        l
        o
        n
        g
        e
        d
        t
        o
        t
        h
        e
        g
        r
        o
        u
        p
        .
        Type `Period` (represented as `dict` in JSON). """
        
        super(GroupMember, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GroupMember, self).elementProperties()
        js.extend([
            ("entity", "entity", fhirreference.FHIRReference, False, None, True),
            ("inactive", "inactive", bool, False, None, False),
            ("period", "period", period.Period, False, None, False),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
