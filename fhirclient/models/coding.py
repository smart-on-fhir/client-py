#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Coding) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Coding(element.Element):
    """ 
    A
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
    a
    c
    o
    d
    e
    d
    e
    f
    i
    n
    e
    d
    b
    y
    a
    t
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    s
    y
    s
    t
    e
    m
    .
    """
    
    resource_type = "Coding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        S
        y
        m
        b
        o
        l
        i
        n
        s
        y
        n
        t
        a
        x
        d
        e
        f
        i
        n
        e
        d
        b
        y
        t
        h
        e
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.display = None
        """ 
        R
        e
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        d
        e
        f
        i
        n
        e
        d
        b
        y
        t
        h
        e
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.system = None
        """ 
        I
        d
        e
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
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.userSelected = None
        """ 
        I
        f
        t
        h
        i
        s
        c
        o
        d
        i
        n
        g
        w
        a
        s
        c
        h
        o
        s
        e
        n
        d
        i
        r
        e
        c
        t
        l
        y
        b
        y
        t
        h
        e
        u
        s
        e
        r
        .
        Type `bool`. """
        
        self.version = None
        """ 
        V
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
        y
        s
        t
        e
        m
        -
        i
        f
        r
        e
        l
        e
        v
        a
        n
        t
        .
        Type `str`. """
        
        super(Coding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("system", "system", str, False, None, False),
            ("userSelected", "userSelected", bool, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


