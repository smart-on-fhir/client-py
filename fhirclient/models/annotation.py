#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Annotation) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Annotation(element.Element):
    """ 
    T
    e
    x
    t
    n
    o
    d
    e
    w
    i
    t
    h
    a
    t
    t
    r
    i
    b
    u
    t
    i
    o
    n
    .
    
    
    A
    t
    e
    x
    t
    n
    o
    t
    e
    w
    h
    i
    c
    h
    a
    l
    s
    o
    c
    o
    n
    t
    a
    i
    n
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
    a
    b
    o
    u
    t
    w
    h
    o
    m
    a
    d
    e
    t
    h
    e
    s
    t
    a
    t
    e
    m
    e
    n
    t
    a
    n
    d
    w
    h
    e
    n
    .
    
    """
    
    resource_type = "Annotation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorReference = None
        """ 
        I
        n
        d
        i
        v
        i
        d
        u
        a
        l
        r
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        f
        o
        r
        t
        h
        e
        a
        n
        n
        o
        t
        a
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authorString = None
        """ 
        I
        n
        d
        i
        v
        i
        d
        u
        a
        l
        r
        e
        s
        p
        o
        n
        s
        i
        b
        l
        e
        f
        o
        r
        t
        h
        e
        a
        n
        n
        o
        t
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.text = None
        """ 
        T
        h
        e
        a
        n
        n
        o
        t
        a
        t
        i
        o
        n
        -
        t
        e
        x
        t
        c
        o
        n
        t
        e
        n
        t
        (
        a
        s
        m
        a
        r
        k
        d
        o
        w
        n
        )
        .
        Type `str`. """
        
        self.time = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        n
        n
        o
        t
        a
        t
        i
        o
        n
        w
        a
        s
        m
        a
        d
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Annotation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, False, "author", False),
            ("authorString", "authorString", str, False, "author", False),
            ("text", "text", str, False, None, True),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
        ])
        return js


import sys
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
