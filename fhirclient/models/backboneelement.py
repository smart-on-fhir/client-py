#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BackboneElement) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class BackboneElement(element.Element):
    """ 
    B
    a
    s
    e
    f
    o
    r
    e
    l
    e
    m
    e
    n
    t
    s
    d
    e
    f
    i
    n
    e
    d
    i
    n
    s
    i
    d
    e
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
    t
    h
    a
    t
    a
    r
    e
    d
    e
    f
    i
    n
    e
    d
    i
    n
    s
    i
    d
    e
    a
    r
    e
    s
    o
    u
    r
    c
    e
    -
    b
    u
    t
    n
    o
    t
    t
    h
    o
    s
    e
    i
    n
    a
    d
    a
    t
    a
    t
    y
    p
    e
    .
    
    """
    
    resource_type = "BackboneElement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.modifierExtension = None
        """ 
        E
        x
        t
        e
        n
        s
        i
        o
        n
        s
        t
        h
        a
        t
        c
        a
        n
        n
        o
        t
        b
        e
        i
        g
        n
        o
        r
        e
        d
        e
        v
        e
        n
        i
        f
        u
        n
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
        .
        List of `Extension` items (represented as `dict` in JSON). """
        
        super(BackboneElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(BackboneElement, self).elementProperties()
        js.extend([
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False),
        ])
        return js


import sys
try:
    from . import extension
except ImportError:
    extension = sys.modules[__package__ + '.extension']
