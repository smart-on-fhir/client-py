#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Expression) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Expression(element.Element):
    """ 
    A
    n
    e
    x
    p
    r
    e
    s
    s
    i
    o
    n
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
    g
    e
    n
    e
    r
    a
    t
    e
    a
    v
    a
    l
    u
    e
    .
    
    
    A
    e
    x
    p
    r
    e
    s
    s
    i
    o
    n
    t
    h
    a
    t
    i
    s
    e
    v
    a
    l
    u
    a
    t
    e
    d
    i
    n
    a
    s
    p
    e
    c
    i
    f
    i
    e
    d
    c
    o
    n
    t
    e
    x
    t
    a
    n
    d
    r
    e
    t
    u
    r
    n
    s
    a
    v
    a
    l
    u
    e
    .
    T
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
    o
    f
    t
    h
    e
    e
    x
    p
    r
    e
    s
    s
    i
    o
    n
    m
    u
    s
    t
    s
    p
    e
    c
    i
    f
    y
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
    e
    x
    p
    r
    e
    s
    s
    i
    o
    n
    i
    s
    e
    v
    a
    l
    u
    a
    t
    e
    d
    ,
    a
    n
    d
    h
    o
    w
    t
    h
    e
    r
    e
    s
    u
    l
    t
    o
    f
    t
    h
    e
    e
    x
    p
    r
    e
    s
    s
    i
    o
    n
    i
    s
    u
    s
    e
    d
    .
    
    """
    
    resource_type = "Expression"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
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
        c
        o
        n
        d
        i
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.expression = None
        """ 
        E
        x
        p
        r
        e
        s
        s
        i
        o
        n
        i
        n
        s
        p
        e
        c
        i
        f
        i
        e
        d
        l
        a
        n
        g
        u
        a
        g
        e
        .
        Type `str`. """
        
        self.language = None
        """ 
        t
        e
        x
        t
        /
        c
        q
        l
        |
        t
        e
        x
        t
        /
        f
        h
        i
        r
        p
        a
        t
        h
        |
        a
        p
        p
        l
        i
        c
        a
        t
        i
        o
        n
        /
        x
        -
        f
        h
        i
        r
        -
        q
        u
        e
        r
        y
        |
        e
        t
        c
        .
        .
        Type `str`. """
        
        self.name = None
        """ 
        S
        h
        o
        r
        t
        n
        a
        m
        e
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
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        f
        o
        r
        r
        e
        u
        s
        e
        .
        Type `str`. """
        
        self.reference = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        i
        s
        f
        o
        u
        n
        d
        .
        Type `str`. """
        
        super(Expression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Expression, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js


