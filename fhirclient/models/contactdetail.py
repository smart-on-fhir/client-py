#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ContactDetail) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class ContactDetail(element.Element):
    """ 
    C
    o
    n
    t
    a
    c
    t
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
    
    
    S
    p
    e
    c
    i
    f
    i
    e
    s
    c
    o
    n
    t
    a
    c
    t
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
    a
    p
    e
    r
    s
    o
    n
    o
    r
    o
    r
    g
    a
    n
    i
    z
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "ContactDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        f
        a
        n
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        t
        o
        c
        o
        n
        t
        a
        c
        t
        .
        Type `str`. """
        
        self.telecom = None
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
        f
        o
        r
        i
        n
        d
        i
        v
        i
        d
        u
        a
        l
        o
        r
        o
        r
        g
        a
        n
        i
        z
        a
        t
        i
        o
        n
        .
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ContactDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ContactDetail, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


import sys
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
