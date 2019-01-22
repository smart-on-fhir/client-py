#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Narrative) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Narrative(element.Element):
    """ 
    H
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
    s
    u
    m
    m
    a
    r
    y
    o
    f
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
    (
    e
    s
    s
    e
    n
    t
    i
    a
    l
    c
    l
    i
    n
    i
    c
    a
    l
    a
    n
    d
    b
    u
    s
    i
    n
    e
    s
    s
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
    )
    .
    
    
    A
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
    s
    u
    m
    m
    a
    r
    y
    o
    f
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
    c
    o
    n
    v
    e
    y
    i
    n
    g
    t
    h
    e
    e
    s
    s
    e
    n
    t
    i
    a
    l
    c
    l
    i
    n
    i
    c
    a
    l
    a
    n
    d
    b
    u
    s
    i
    n
    e
    s
    s
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
    .
    
    """
    
    resource_type = "Narrative"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.div = None
        """ 
        L
        i
        m
        i
        t
        e
        d
        x
        h
        t
        m
        l
        c
        o
        n
        t
        e
        n
        t
        .
        Type `str`. """
        
        self.status = None
        """ 
        g
        e
        n
        e
        r
        a
        t
        e
        d
        |
        e
        x
        t
        e
        n
        s
        i
        o
        n
        s
        |
        a
        d
        d
        i
        t
        i
        o
        n
        a
        l
        |
        e
        m
        p
        t
        y
        .
        Type `str`. """
        
        super(Narrative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("div", "div", str, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


