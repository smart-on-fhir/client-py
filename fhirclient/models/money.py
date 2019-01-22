#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Money) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Money(element.Element):
    """ 
    A
    n
    a
    m
    o
    u
    n
    t
    o
    f
    e
    c
    o
    n
    o
    m
    i
    c
    u
    t
    i
    l
    i
    t
    y
    i
    n
    s
    o
    m
    e
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
    c
    u
    r
    r
    e
    n
    c
    y
    .
    """
    
    resource_type = "Money"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.currency = None
        """ 
        I
        S
        O
        4
        2
        1
        7
        C
        u
        r
        r
        e
        n
        c
        y
        C
        o
        d
        e
        .
        Type `str`. """
        
        self.value = None
        """ 
        N
        u
        m
        e
        r
        i
        c
        a
        l
        v
        a
        l
        u
        e
        (
        w
        i
        t
        h
        i
        m
        p
        l
        i
        c
        i
        t
        p
        r
        e
        c
        i
        s
        i
        o
        n
        )
        .
        Type `float`. """
        
        super(Money, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Money, self).elementProperties()
        js.extend([
            ("currency", "currency", str, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


