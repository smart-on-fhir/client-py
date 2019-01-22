#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Contributor) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Contributor(element.Element):
    """ 
    C
    o
    n
    t
    r
    i
    b
    u
    t
    o
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
    .
    
    
    A
    c
    o
    n
    t
    r
    i
    b
    u
    t
    o
    r
    t
    o
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
    o
    f
    a
    k
    n
    o
    w
    l
    e
    d
    g
    e
    a
    s
    s
    e
    t
    ,
    i
    n
    c
    l
    u
    d
    i
    n
    g
    a
    u
    t
    h
    o
    r
    s
    ,
    e
    d
    i
    t
    o
    r
    s
    ,
    r
    e
    v
    i
    e
    w
    e
    r
    s
    ,
    a
    n
    d
    e
    n
    d
    o
    r
    s
    e
    r
    s
    .
    
    """
    
    resource_type = "Contributor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
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
        c
        o
        n
        t
        r
        i
        b
        u
        t
        o
        r
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        W
        h
        o
        c
        o
        n
        t
        r
        i
        b
        u
        t
        e
        d
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
        .
        Type `str`. """
        
        self.type = None
        """ 
        a
        u
        t
        h
        o
        r
        |
        e
        d
        i
        t
        o
        r
        |
        r
        e
        v
        i
        e
        w
        e
        r
        |
        e
        n
        d
        o
        r
        s
        e
        r
        .
        Type `str`. """
        
        super(Contributor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Contributor, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


import sys
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
