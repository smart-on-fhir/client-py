#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Attachment) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Attachment(element.Element):
    """ 
    C
    o
    n
    t
    e
    n
    t
    i
    n
    a
    f
    o
    r
    m
    a
    t
    d
    e
    f
    i
    n
    e
    d
    e
    l
    s
    e
    w
    h
    e
    r
    e
    .
    
    
    F
    o
    r
    r
    e
    f
    e
    r
    r
    i
    n
    g
    t
    o
    d
    a
    t
    a
    c
    o
    n
    t
    e
    n
    t
    d
    e
    f
    i
    n
    e
    d
    i
    n
    o
    t
    h
    e
    r
    f
    o
    r
    m
    a
    t
    s
    .
    
    """
    
    resource_type = "Attachment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ 
        M
        i
        m
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
        c
        o
        n
        t
        e
        n
        t
        ,
        w
        i
        t
        h
        c
        h
        a
        r
        s
        e
        t
        e
        t
        c
        .
        .
        Type `str`. """
        
        self.creation = None
        """ 
        D
        a
        t
        e
        a
        t
        t
        a
        c
        h
        m
        e
        n
        t
        w
        a
        s
        f
        i
        r
        s
        t
        c
        r
        e
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.data = None
        """ 
        D
        a
        t
        a
        i
        n
        l
        i
        n
        e
        ,
        b
        a
        s
        e
        6
        4
        e
        d
        .
        Type `str`. """
        
        self.hash = None
        """ 
        H
        a
        s
        h
        o
        f
        t
        h
        e
        d
        a
        t
        a
        (
        s
        h
        a
        -
        1
        ,
        b
        a
        s
        e
        6
        4
        e
        d
        )
        .
        Type `str`. """
        
        self.language = None
        """ 
        H
        u
        m
        a
        n
        l
        a
        n
        g
        u
        a
        g
        e
        o
        f
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        (
        B
        C
        P
        -
        4
        7
        )
        .
        Type `str`. """
        
        self.size = None
        """ 
        N
        u
        m
        b
        e
        r
        o
        f
        b
        y
        t
        e
        s
        o
        f
        c
        o
        n
        t
        e
        n
        t
        (
        i
        f
        u
        r
        l
        p
        r
        o
        v
        i
        d
        e
        d
        )
        .
        Type `int`. """
        
        self.title = None
        """ 
        L
        a
        b
        e
        l
        t
        o
        d
        i
        s
        p
        l
        a
        y
        i
        n
        p
        l
        a
        c
        e
        o
        f
        t
        h
        e
        d
        a
        t
        a
        .
        Type `str`. """
        
        self.url = None
        """ 
        U
        r
        i
        w
        h
        e
        r
        e
        t
        h
        e
        d
        a
        t
        a
        c
        a
        n
        b
        e
        f
        o
        u
        n
        d
        .
        Type `str`. """
        
        super(Attachment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, False),
            ("creation", "creation", fhirdate.FHIRDate, False, None, False),
            ("data", "data", str, False, None, False),
            ("hash", "hash", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("size", "size", int, False, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
