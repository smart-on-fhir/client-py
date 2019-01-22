#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Reference) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Reference(element.Element):
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
    f
    r
    o
    m
    o
    n
    e
    r
    e
    s
    o
    u
    r
    c
    e
    t
    o
    a
    n
    o
    t
    h
    e
    r
    .
    """
    
    resource_type = "Reference"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.display = None
        """ 
        T
        e
        x
        t
        a
        l
        t
        e
        r
        n
        a
        t
        i
        v
        e
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
        Type `str`. """
        
        self.identifier = None
        """ 
        L
        o
        g
        i
        c
        a
        l
        r
        e
        f
        e
        r
        e
        n
        c
        e
        ,
        w
        h
        e
        n
        l
        i
        t
        e
        r
        a
        l
        r
        e
        f
        e
        r
        e
        n
        c
        e
        i
        s
        n
        o
        t
        k
        n
        o
        w
        n
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.reference = None
        """ 
        L
        i
        t
        e
        r
        a
        l
        r
        e
        f
        e
        r
        e
        n
        c
        e
        ,
        R
        e
        l
        a
        t
        i
        v
        e
        ,
        i
        n
        t
        e
        r
        n
        a
        l
        o
        r
        a
        b
        s
        o
        l
        u
        t
        e
        U
        R
        L
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
        y
        p
        e
        t
        h
        e
        r
        e
        f
        e
        r
        e
        n
        c
        e
        r
        e
        f
        e
        r
        s
        t
        o
        (
        e
        .
        g
        .
        "
        P
        a
        t
        i
        e
        n
        t
        "
        )
        .
        Type `str`. """
        
        super(Reference, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


import sys
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
