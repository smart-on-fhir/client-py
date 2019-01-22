#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/UsageContext) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class UsageContext(element.Element):
    """ 
    D
    e
    s
    c
    r
    i
    b
    e
    s
    t
    h
    e
    c
    o
    n
    t
    e
    x
    t
    o
    f
    u
    s
    e
    f
    o
    r
    a
    c
    o
    n
    f
    o
    r
    m
    a
    n
    c
    e
    o
    r
    k
    n
    o
    w
    l
    e
    d
    g
    e
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    
    S
    p
    e
    c
    i
    f
    i
    e
    s
    c
    l
    i
    n
    i
    c
    a
    l
    /
    b
    u
    s
    i
    n
    e
    s
    s
    /
    e
    t
    c
    .
    m
    e
    t
    a
    d
    a
    t
    a
    t
    h
    a
    t
    c
    a
    n
    b
    e
    u
    s
    e
    d
    t
    o
    r
    e
    t
    r
    i
    e
    v
    e
    ,
    i
    n
    d
    e
    x
    a
    n
    d
    /
    o
    r
    c
    a
    t
    e
    g
    o
    r
    i
    z
    e
    a
    n
    a
    r
    t
    i
    f
    a
    c
    t
    .
    T
    h
    i
    s
    m
    e
    t
    a
    d
    a
    t
    a
    c
    a
    n
    e
    i
    t
    h
    e
    r
    b
    e
    s
    p
    e
    c
    i
    f
    i
    c
    t
    o
    t
    h
    e
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
    p
    o
    p
    u
    l
    a
    t
    i
    o
    n
    (
    e
    .
    g
    .
    ,
    a
    g
    e
    c
    a
    t
    e
    g
    o
    r
    y
    ,
    D
    R
    G
    )
    o
    r
    t
    h
    e
    s
    p
    e
    c
    i
    f
    i
    c
    c
    o
    n
    t
    e
    x
    t
    o
    f
    c
    a
    r
    e
    (
    e
    .
    g
    .
    ,
    v
    e
    n
    u
    e
    ,
    c
    a
    r
    e
    s
    e
    t
    t
    i
    n
    g
    ,
    p
    r
    o
    v
    i
    d
    e
    r
    o
    f
    c
    a
    r
    e
    )
    .
    
    """
    
    resource_type = "UsageContext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        T
        y
        p
        e
        o
        f
        c
        o
        n
        t
        e
        x
        t
        b
        e
        i
        n
        g
        s
        p
        e
        c
        i
        f
        i
        e
        d
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueCodeableConcept = None
        """ 
        V
        a
        l
        u
        e
        t
        h
        a
        t
        d
        e
        f
        i
        n
        e
        s
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ 
        V
        a
        l
        u
        e
        t
        h
        a
        t
        d
        e
        f
        i
        n
        e
        s
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        V
        a
        l
        u
        e
        t
        h
        a
        t
        d
        e
        f
        i
        n
        e
        s
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ 
        V
        a
        l
        u
        e
        t
        h
        a
        t
        d
        e
        f
        i
        n
        e
        s
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(UsageContext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(UsageContext, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False, None, True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
