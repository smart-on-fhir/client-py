#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Period) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Period(element.Element):
    """ 
    T
    i
    m
    e
    r
    a
    n
    g
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
    s
    t
    a
    r
    t
    a
    n
    d
    e
    n
    d
    d
    a
    t
    e
    /
    t
    i
    m
    e
    .
    
    
    A
    t
    i
    m
    e
    p
    e
    r
    i
    o
    d
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
    s
    t
    a
    r
    t
    a
    n
    d
    e
    n
    d
    d
    a
    t
    e
    a
    n
    d
    o
    p
    t
    i
    o
    n
    a
    l
    l
    y
    t
    i
    m
    e
    .
    
    """
    
    resource_type = "Period"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.end = None
        """ 
        E
        n
        d
        t
        i
        m
        e
        w
        i
        t
        h
        i
        n
        c
        l
        u
        s
        i
        v
        e
        b
        o
        u
        n
        d
        a
        r
        y
        ,
        i
        f
        n
        o
        t
        o
        n
        g
        o
        i
        n
        g
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.start = None
        """ 
        S
        t
        a
        r
        t
        i
        n
        g
        t
        i
        m
        e
        w
        i
        t
        h
        i
        n
        c
        l
        u
        s
        i
        v
        e
        b
        o
        u
        n
        d
        a
        r
        y
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Period, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend([
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
