#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CodeableConcept) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class CodeableConcept(element.Element):
    """ 
    C
    o
    n
    c
    e
    p
    t
    -
    r
    e
    f
    e
    r
    e
    n
    c
    e
    t
    o
    a
    t
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    o
    r
    j
    u
    s
    t
    t
    e
    x
    t
    .
    
    
    A
    c
    o
    n
    c
    e
    p
    t
    t
    h
    a
    t
    m
    a
    y
    b
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
    a
    f
    o
    r
    m
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
    t
    o
    a
    t
    e
    r
    m
    i
    n
    o
    l
    o
    g
    y
    o
    r
    o
    n
    t
    o
    l
    o
    g
    y
    o
    r
    m
    a
    y
    b
    e
    p
    r
    o
    v
    i
    d
    e
    d
    b
    y
    t
    e
    x
    t
    .
    
    """
    
    resource_type = "CodeableConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coding = None
        """ 
        C
        o
        d
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
        a
        t
        e
        r
        m
        i
        n
        o
        l
        o
        g
        y
        s
        y
        s
        t
        e
        m
        .
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        P
        l
        a
        i
        n
        t
        e
        x
        t
        r
        e
        p
        r
        e
        s
        e
        n
        t
        a
        t
        i
        o
        n
        o
        f
        t
        h
        e
        c
        o
        n
        c
        e
        p
        t
        .
        Type `str`. """
        
        super(CodeableConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CodeableConcept, self).elementProperties()
        js.extend([
            ("coding", "coding", coding.Coding, True, None, False),
            ("text", "text", str, False, None, False),
        ])
        return js


import sys
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
