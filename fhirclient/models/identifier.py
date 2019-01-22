#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Identifier) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Identifier(element.Element):
    """ 
    A
    n
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
    i
    n
    t
    e
    n
    d
    e
    d
    f
    o
    r
    c
    o
    m
    p
    u
    t
    a
    t
    i
    o
    n
    .
    
    
    A
    n
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
    -
    i
    d
    e
    n
    t
    i
    f
    i
    e
    s
    s
    o
    m
    e
    e
    n
    t
    i
    t
    y
    u
    n
    i
    q
    u
    e
    l
    y
    a
    n
    d
    u
    n
    a
    m
    b
    i
    g
    u
    o
    u
    s
    l
    y
    .
    T
    y
    p
    i
    c
    a
    l
    l
    y
    t
    h
    i
    s
    i
    s
    u
    s
    e
    d
    f
    o
    r
    b
    u
    s
    i
    n
    e
    s
    s
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
    s
    .
    
    """
    
    resource_type = "Identifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assigner = None
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
        t
        h
        a
        t
        i
        s
        s
        u
        e
        d
        i
        d
        (
        m
        a
        y
        b
        e
        j
        u
        s
        t
        t
        e
        x
        t
        )
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ 
        T
        i
        m
        e
        p
        e
        r
        i
        o
        d
        w
        h
        e
        n
        i
        d
        i
        s
        /
        w
        a
        s
        v
        a
        l
        i
        d
        f
        o
        r
        u
        s
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ 
        T
        h
        e
        n
        a
        m
        e
        s
        p
        a
        c
        e
        f
        o
        r
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
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        self.type = None
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        """ 
        u
        s
        u
        a
        l
        |
        o
        f
        f
        i
        c
        i
        a
        l
        |
        t
        e
        m
        p
        |
        s
        e
        c
        o
        n
        d
        a
        r
        y
        |
        o
        l
        d
        (
        I
        f
        k
        n
        o
        w
        n
        )
        .
        Type `str`. """
        
        self.value = None
        """ 
        T
        h
        e
        v
        a
        l
        u
        e
        t
        h
        a
        t
        i
        s
        u
        n
        i
        q
        u
        e
        .
        Type `str`. """
        
        super(Identifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("assigner", "assigner", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("system", "system", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("use", "use", str, False, None, False),
            ("value", "value", str, False, None, False),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
