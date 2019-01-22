#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Element) on 2019-01-22.
#  2019, SMART Health IT.


from . import fhirabstractbase

class Element(fhirabstractbase.FHIRAbstractBase):
    """ 
    B
    a
    s
    e
    f
    o
    r
    a
    l
    l
    e
    l
    e
    m
    e
    n
    t
    s
    .
    
    
    B
    a
    s
    e
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
    f
    o
    r
    a
    l
    l
    e
    l
    e
    m
    e
    n
    t
    s
    i
    n
    a
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
    
    resource_type = "Element"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.extension = None
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
        b
        y
        i
        m
        p
        l
        e
        m
        e
        n
        t
        a
        t
        i
        o
        n
        s
        .
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.id = None
        """ 
        U
        n
        i
        q
        u
        e
        i
        d
        f
        o
        r
        i
        n
        t
        e
        r
        -
        e
        l
        e
        m
        e
        n
        t
        r
        e
        f
        e
        r
        e
        n
        c
        i
        n
        g
        .
        Type `str`. """
        
        super(Element, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Element, self).elementProperties()
        from . import extension
        js.extend([
            ("extension", "extension", extension.Extension, True, None, False),
            ("id", "id", str, False, None, False),
        ])
        return js


