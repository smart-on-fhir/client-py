#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ParameterDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class ParameterDefinition(element.Element):
    """ 
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
    o
    f
    a
    p
    a
    r
    a
    m
    e
    t
    e
    r
    t
    o
    a
    m
    o
    d
    u
    l
    e
    .
    
    
    T
    h
    e
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    t
    o
    t
    h
    e
    m
    o
    d
    u
    l
    e
    .
    T
    h
    i
    s
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
    s
    p
    e
    c
    i
    f
    i
    e
    s
    b
    o
    t
    h
    t
    h
    e
    i
    n
    p
    u
    t
    a
    n
    d
    o
    u
    t
    p
    u
    t
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    .
    I
    n
    p
    u
    t
    p
    a
    r
    a
    m
    e
    t
    e
    r
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
    b
    y
    t
    h
    e
    c
    a
    l
    l
    e
    r
    a
    s
    p
    a
    r
    t
    o
    f
    t
    h
    e
    $
    e
    v
    a
    l
    u
    a
    t
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
    .
    O
    u
    t
    p
    u
    t
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    a
    r
    e
    i
    n
    c
    l
    u
    d
    e
    d
    i
    n
    t
    h
    e
    G
    u
    i
    d
    a
    n
    c
    e
    R
    e
    s
    p
    o
    n
    s
    e
    .
    
    """
    
    resource_type = "ParameterDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ 
        A
        b
        r
        i
        e
        f
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
        o
        f
        t
        h
        e
        p
        a
        r
        a
        m
        e
        t
        e
        r
        .
        Type `str`. """
        
        self.max = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        c
        a
        r
        d
        i
        n
        a
        l
        i
        t
        y
        (
        a
        n
        u
        m
        b
        e
        r
        o
        f
        *
        )
        .
        Type `str`. """
        
        self.min = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        c
        a
        r
        d
        i
        n
        a
        l
        i
        t
        y
        .
        Type `int`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        u
        s
        e
        d
        t
        o
        a
        c
        c
        e
        s
        s
        t
        h
        e
        p
        a
        r
        a
        m
        e
        t
        e
        r
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        self.profile = None
        """ 
        W
        h
        a
        t
        p
        r
        o
        f
        i
        l
        e
        t
        h
        e
        v
        a
        l
        u
        e
        i
        s
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
        b
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        W
        h
        a
        t
        t
        y
        p
        e
        o
        f
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        self.use = None
        """ 
        i
        n
        |
        o
        u
        t
        .
        Type `str`. """
        
        super(ParameterDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParameterDefinition, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("name", "name", str, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("use", "use", str, False, None, True),
        ])
        return js


