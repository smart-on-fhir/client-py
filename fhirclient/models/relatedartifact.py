#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RelatedArtifact) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class RelatedArtifact(element.Element):
    """ 
    R
    e
    l
    a
    t
    e
    d
    a
    r
    t
    i
    f
    a
    c
    t
    s
    f
    o
    r
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
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    
    R
    e
    l
    a
    t
    e
    d
    a
    r
    t
    i
    f
    a
    c
    t
    s
    s
    u
    c
    h
    a
    s
    a
    d
    d
    i
    t
    i
    o
    n
    a
    l
    d
    o
    c
    u
    m
    e
    n
    t
    a
    t
    i
    o
    n
    ,
    j
    u
    s
    t
    i
    f
    i
    c
    a
    t
    i
    o
    n
    ,
    o
    r
    b
    i
    b
    l
    i
    o
    g
    r
    a
    p
    h
    i
    c
    r
    e
    f
    e
    r
    e
    n
    c
    e
    s
    .
    
    """
    
    resource_type = "RelatedArtifact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.citation = None
        """ 
        B
        i
        b
        l
        i
        o
        g
        r
        a
        p
        h
        i
        c
        c
        i
        t
        a
        t
        i
        o
        n
        f
        o
        r
        t
        h
        e
        a
        r
        t
        i
        f
        a
        c
        t
        .
        Type `str`. """
        
        self.display = None
        """ 
        B
        r
        i
        e
        f
        d
        e
        s
        c
        r
        i
        p
        t
        i
        o
        n
        o
        f
        t
        h
        e
        r
        e
        l
        a
        t
        e
        d
        a
        r
        t
        i
        f
        a
        c
        t
        .
        Type `str`. """
        
        self.document = None
        """ 
        W
        h
        a
        t
        d
        o
        c
        u
        m
        e
        n
        t
        i
        s
        b
        e
        i
        n
        g
        r
        e
        f
        e
        r
        e
        n
        c
        e
        d
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.label = None
        """ 
        S
        h
        o
        r
        t
        l
        a
        b
        e
        l
        .
        Type `str`. """
        
        self.resource = None
        """ 
        W
        h
        a
        t
        r
        e
        s
        o
        u
        r
        c
        e
        i
        s
        b
        e
        i
        n
        g
        r
        e
        f
        e
        r
        e
        n
        c
        e
        d
        .
        Type `str`. """
        
        self.type = None
        """ 
        d
        o
        c
        u
        m
        e
        n
        t
        a
        t
        i
        o
        n
        |
        j
        u
        s
        t
        i
        f
        i
        c
        a
        t
        i
        o
        n
        |
        c
        i
        t
        a
        t
        i
        o
        n
        |
        p
        r
        e
        d
        e
        c
        e
        s
        s
        o
        r
        |
        s
        u
        c
        c
        e
        s
        s
        o
        r
        |
        d
        e
        r
        i
        v
        e
        d
        -
        f
        r
        o
        m
        |
        d
        e
        p
        e
        n
        d
        s
        -
        o
        n
        |
        c
        o
        m
        p
        o
        s
        e
        d
        -
        o
        f
        .
        Type `str`. """
        
        self.url = None
        """ 
        W
        h
        e
        r
        e
        t
        h
        e
        a
        r
        t
        i
        f
        a
        c
        t
        c
        a
        n
        b
        e
        a
        c
        c
        e
        s
        s
        e
        d
        .
        Type `str`. """
        
        super(RelatedArtifact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("citation", "citation", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("document", "document", attachment.Attachment, False, None, False),
            ("label", "label", str, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
