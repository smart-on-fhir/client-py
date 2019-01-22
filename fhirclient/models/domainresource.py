#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2019-01-22.
#  2019, SMART Health IT.


from . import resource

class DomainResource(resource.Resource):
    """ 
    A
    r
    e
    s
    o
    u
    r
    c
    e
    w
    i
    t
    h
    n
    a
    r
    r
    a
    t
    i
    v
    e
    ,
    e
    x
    t
    e
    n
    s
    i
    o
    n
    s
    ,
    a
    n
    d
    c
    o
    n
    t
    a
    i
    n
    e
    d
    r
    e
    s
    o
    u
    r
    c
    e
    s
    .
    
    
    A
    r
    e
    s
    o
    u
    r
    c
    e
    t
    h
    a
    t
    i
    n
    c
    l
    u
    d
    e
    s
    n
    a
    r
    r
    a
    t
    i
    v
    e
    ,
    e
    x
    t
    e
    n
    s
    i
    o
    n
    s
    ,
    a
    n
    d
    c
    o
    n
    t
    a
    i
    n
    e
    d
    r
    e
    s
    o
    u
    r
    c
    e
    s
    .
    
    """
    
    resource_type = "DomainResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contained = None
        """ 
        C
        o
        n
        t
        a
        i
        n
        e
        d
        ,
        i
        n
        l
        i
        n
        e
        R
        e
        s
        o
        u
        r
        c
        e
        s
        .
        List of `Resource` items (represented as `dict` in JSON). """
        
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
        .
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.text = None
        """ 
        T
        e
        x
        t
        s
        u
        m
        m
        a
        r
        y
        o
        f
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
        ,
        f
        o
        r
        h
        u
        m
        a
        n
        i
        n
        t
        e
        r
        p
        r
        e
        t
        a
        t
        i
        o
        n
        .
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(DomainResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("contained", "contained", resource.Resource, True, None, False),
            ("extension", "extension", extension.Extension, True, None, False),
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
        ])
        return js


import sys
try:
    from . import extension
except ImportError:
    extension = sys.modules[__package__ + '.extension']
try:
    from . import narrative
except ImportError:
    narrative = sys.modules[__package__ + '.narrative']
