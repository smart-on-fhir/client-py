#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/StructureMap) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class StructureMap(domainresource.DomainResource):
    """ 
    A
    M
    a
    p
    o
    f
    r
    e
    l
    a
    t
    i
    o
    n
    s
    h
    i
    p
    s
    b
    e
    t
    w
    e
    e
    n
    2
    s
    t
    r
    u
    c
    t
    u
    r
    e
    s
    t
    h
    a
    t
    c
    a
    n
    b
    e
    u
    s
    e
    d
    t
    o
    t
    r
    a
    n
    s
    f
    o
    r
    m
    d
    a
    t
    a
    .
    """
    
    resource_type = "StructureMap"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
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
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        .
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ 
        U
        s
        e
        a
        n
        d
        /
        o
        r
        p
        u
        b
        l
        i
        s
        h
        i
        n
        g
        r
        e
        s
        t
        r
        i
        c
        t
        i
        o
        n
        s
        .
        Type `str`. """
        
        self.date = None
        """ 
        D
        a
        t
        e
        l
        a
        s
        t
        c
        h
        a
        n
        g
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ 
        N
        a
        t
        u
        r
        a
        l
        l
        a
        n
        g
        u
        a
        g
        e
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
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        .
        Type `str`. """
        
        self.experimental = None
        """ 
        F
        o
        r
        t
        e
        s
        t
        i
        n
        g
        p
        u
        r
        p
        o
        s
        e
        s
        ,
        n
        o
        t
        r
        e
        a
        l
        u
        s
        a
        g
        e
        .
        Type `bool`. """
        
        self.group = None
        """ 
        N
        a
        m
        e
        d
        s
        e
        c
        t
        i
        o
        n
        s
        f
        o
        r
        r
        e
        a
        d
        e
        r
        c
        o
        n
        v
        e
        n
        i
        e
        n
        c
        e
        .
        List of `StructureMapGroup` items (represented as `dict` in JSON). """
        
        self.identifier = None
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
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        f
        o
        r
        t
        h
        e
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.import_fhir = None
        """ 
        O
        t
        h
        e
        r
        m
        a
        p
        s
        u
        s
        e
        d
        b
        y
        t
        h
        i
        s
        m
        a
        p
        (
        c
        a
        n
        o
        n
        i
        c
        a
        l
        U
        R
        L
        s
        )
        .
        List of `str` items. """
        
        self.jurisdiction = None
        """ 
        I
        n
        t
        e
        n
        d
        e
        d
        j
        u
        r
        i
        s
        d
        i
        c
        t
        i
        o
        n
        f
        o
        r
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        (
        i
        f
        a
        p
        p
        l
        i
        c
        a
        b
        l
        e
        )
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        (
        c
        o
        m
        p
        u
        t
        e
        r
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.publisher = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        p
        u
        b
        l
        i
        s
        h
        e
        r
        (
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
        )
        .
        Type `str`. """
        
        self.purpose = None
        """ 
        W
        h
        y
        t
        h
        i
        s
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        i
        s
        d
        e
        f
        i
        n
        e
        d
        .
        Type `str`. """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        a
        c
        t
        i
        v
        e
        |
        r
        e
        t
        i
        r
        e
        d
        |
        u
        n
        k
        n
        o
        w
        n
        .
        Type `str`. """
        
        self.structure = None
        """ 
        S
        t
        r
        u
        c
        t
        u
        r
        e
        D
        e
        f
        i
        n
        i
        t
        i
        o
        n
        u
        s
        e
        d
        b
        y
        t
        h
        i
        s
        m
        a
        p
        .
        List of `StructureMapStructure` items (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        (
        h
        u
        m
        a
        n
        f
        r
        i
        e
        n
        d
        l
        y
        )
        .
        Type `str`. """
        
        self.url = None
        """ 
        C
        a
        n
        o
        n
        i
        c
        a
        l
        i
        d
        e
        n
        t
        i
        f
        i
        e
        r
        f
        o
        r
        t
        h
        i
        s
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        ,
        r
        e
        p
        r
        e
        s
        e
        n
        t
        e
        d
        a
        s
        a
        U
        R
        I
        (
        g
        l
        o
        b
        a
        l
        l
        y
        u
        n
        i
        q
        u
        e
        )
        .
        Type `str`. """
        
        self.useContext = None
        """ 
        T
        h
        e
        c
        o
        n
        t
        e
        x
        t
        t
        h
        a
        t
        t
        h
        e
        c
        o
        n
        t
        e
        n
        t
        i
        s
        i
        n
        t
        e
        n
        d
        e
        d
        t
        o
        s
        u
        p
        p
        o
        r
        t
        .
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ 
        B
        u
        s
        i
        n
        e
        s
        s
        v
        e
        r
        s
        i
        o
        n
        o
        f
        t
        h
        e
        s
        t
        r
        u
        c
        t
        u
        r
        e
        m
        a
        p
        .
        Type `str`. """
        
        super(StructureMap, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMap, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("group", "group", StructureMapGroup, True, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("structure", "structure", StructureMapStructure, True, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class StructureMapGroup(backboneelement.BackboneElement):
    """ 
    N
    a
    m
    e
    d
    s
    e
    c
    t
    i
    o
    n
    s
    f
    o
    r
    r
    e
    a
    d
    e
    r
    c
    o
    n
    v
    e
    n
    i
    e
    n
    c
    e
    .
    
    
    O
    r
    g
    a
    n
    i
    z
    e
    s
    t
    h
    e
    m
    a
    p
    p
    i
    n
    g
    i
    n
    t
    o
    m
    a
    n
    a
    g
    e
    a
    b
    l
    e
    c
    h
    u
    n
    k
    s
    f
    o
    r
    h
    u
    m
    a
    n
    r
    e
    v
    i
    e
    w
    /
    e
    a
    s
    e
    o
    f
    m
    a
    i
    n
    t
    e
    n
    a
    n
    c
    e
    .
    
    """
    
    resource_type = "StructureMapGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
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
        /
        e
        x
        p
        l
        a
        n
        a
        t
        i
        o
        n
        f
        o
        r
        g
        r
        o
        u
        p
        .
        Type `str`. """
        
        self.extends = None
        """ 
        A
        n
        o
        t
        h
        e
        r
        g
        r
        o
        u
        p
        t
        h
        a
        t
        t
        h
        i
        s
        g
        r
        o
        u
        p
        a
        d
        d
        s
        r
        u
        l
        e
        s
        t
        o
        .
        Type `str`. """
        
        self.input = None
        """ 
        N
        a
        m
        e
        d
        i
        n
        s
        t
        a
        n
        c
        e
        p
        r
        o
        v
        i
        d
        e
        d
        w
        h
        e
        n
        i
        n
        v
        o
        k
        i
        n
        g
        t
        h
        e
        m
        a
        p
        .
        List of `StructureMapGroupInput` items (represented as `dict` in JSON). """
        
        self.name = None
        """ 
        H
        u
        m
        a
        n
        -
        r
        e
        a
        d
        a
        b
        l
        e
        l
        a
        b
        e
        l
        .
        Type `str`. """
        
        self.rule = None
        """ 
        T
        r
        a
        n
        s
        f
        o
        r
        m
        R
        u
        l
        e
        f
        r
        o
        m
        s
        o
        u
        r
        c
        e
        t
        o
        t
        a
        r
        g
        e
        t
        .
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        self.typeMode = None
        """ 
        n
        o
        n
        e
        |
        t
        y
        p
        e
        s
        |
        t
        y
        p
        e
        -
        a
        n
        d
        -
        t
        y
        p
        e
        s
        .
        Type `str`. """
        
        super(StructureMapGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroup, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("extends", "extends", str, False, None, False),
            ("input", "input", StructureMapGroupInput, True, None, True),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, True),
            ("typeMode", "typeMode", str, False, None, True),
        ])
        return js


class StructureMapGroupInput(backboneelement.BackboneElement):
    """ 
    N
    a
    m
    e
    d
    i
    n
    s
    t
    a
    n
    c
    e
    p
    r
    o
    v
    i
    d
    e
    d
    w
    h
    e
    n
    i
    n
    v
    o
    k
    i
    n
    g
    t
    h
    e
    m
    a
    p
    .
    
    
    A
    n
    a
    m
    e
    a
    s
    s
    i
    g
    n
    e
    d
    t
    o
    a
    n
    i
    n
    s
    t
    a
    n
    c
    e
    o
    f
    d
    a
    t
    a
    .
    T
    h
    e
    i
    n
    s
    t
    a
    n
    c
    e
    m
    u
    s
    t
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
    w
    h
    e
    n
    t
    h
    e
    m
    a
    p
    p
    i
    n
    g
    i
    s
    i
    n
    v
    o
    k
    e
    d
    .
    
    """
    
    resource_type = "StructureMapGroupInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.documentation = None
        """ 
        D
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
        f
        o
        r
        t
        h
        i
        s
        i
        n
        s
        t
        a
        n
        c
        e
        o
        f
        d
        a
        t
        a
        .
        Type `str`. """
        
        self.mode = None
        """ 
        s
        o
        u
        r
        c
        e
        |
        t
        a
        r
        g
        e
        t
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        h
        i
        s
        i
        n
        s
        t
        a
        n
        c
        e
        o
        f
        d
        a
        t
        a
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
        y
        p
        e
        f
        o
        r
        t
        h
        i
        s
        i
        n
        s
        t
        a
        n
        c
        e
        o
        f
        d
        a
        t
        a
        .
        Type `str`. """
        
        super(StructureMapGroupInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupInput, self).elementProperties()
        js.extend([
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("type", "type", str, False, None, False),
        ])
        return js


class StructureMapGroupRule(backboneelement.BackboneElement):
    """ 
    T
    r
    a
    n
    s
    f
    o
    r
    m
    R
    u
    l
    e
    f
    r
    o
    m
    s
    o
    u
    r
    c
    e
    t
    o
    t
    a
    r
    g
    e
    t
    .
    """
    
    resource_type = "StructureMapGroupRule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dependent = None
        """ 
        W
        h
        i
        c
        h
        o
        t
        h
        e
        r
        r
        u
        l
        e
        s
        t
        o
        a
        p
        p
        l
        y
        i
        n
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        o
        f
        t
        h
        i
        s
        r
        u
        l
        e
        .
        List of `StructureMapGroupRuleDependent` items (represented as `dict` in JSON). """
        
        self.documentation = None
        """ 
        D
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
        f
        o
        r
        t
        h
        i
        s
        i
        n
        s
        t
        a
        n
        c
        e
        o
        f
        d
        a
        t
        a
        .
        Type `str`. """
        
        self.name = None
        """ 
        N
        a
        m
        e
        o
        f
        t
        h
        e
        r
        u
        l
        e
        f
        o
        r
        i
        n
        t
        e
        r
        n
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
        s
        .
        Type `str`. """
        
        self.rule = None
        """ 
        R
        u
        l
        e
        s
        c
        o
        n
        t
        a
        i
        n
        e
        d
        i
        n
        t
        h
        i
        s
        r
        u
        l
        e
        .
        List of `StructureMapGroupRule` items (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        S
        o
        u
        r
        c
        e
        i
        n
        p
        u
        t
        s
        t
        o
        t
        h
        e
        m
        a
        p
        p
        i
        n
        g
        .
        List of `StructureMapGroupRuleSource` items (represented as `dict` in JSON). """
        
        self.target = None
        """ 
        C
        o
        n
        t
        e
        n
        t
        t
        o
        c
        r
        e
        a
        t
        e
        b
        e
        c
        a
        u
        s
        e
        o
        f
        t
        h
        i
        s
        m
        a
        p
        p
        i
        n
        g
        r
        u
        l
        e
        .
        List of `StructureMapGroupRuleTarget` items (represented as `dict` in JSON). """
        
        super(StructureMapGroupRule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRule, self).elementProperties()
        js.extend([
            ("dependent", "dependent", StructureMapGroupRuleDependent, True, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("name", "name", str, False, None, True),
            ("rule", "rule", StructureMapGroupRule, True, None, False),
            ("source", "source", StructureMapGroupRuleSource, True, None, True),
            ("target", "target", StructureMapGroupRuleTarget, True, None, False),
        ])
        return js


class StructureMapGroupRuleDependent(backboneelement.BackboneElement):
    """ 
    W
    h
    i
    c
    h
    o
    t
    h
    e
    r
    r
    u
    l
    e
    s
    t
    o
    a
    p
    p
    l
    y
    i
    n
    t
    h
    e
    c
    o
    n
    t
    e
    x
    t
    o
    f
    t
    h
    i
    s
    r
    u
    l
    e
    .
    """
    
    resource_type = "StructureMapGroupRuleDependent"
    
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
        r
        u
        l
        e
        o
        r
        g
        r
        o
        u
        p
        t
        o
        a
        p
        p
        l
        y
        .
        Type `str`. """
        
        self.variable = None
        """ 
        V
        a
        r
        i
        a
        b
        l
        e
        t
        o
        p
        a
        s
        s
        t
        o
        t
        h
        e
        r
        u
        l
        e
        o
        r
        g
        r
        o
        u
        p
        .
        List of `str` items. """
        
        super(StructureMapGroupRuleDependent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleDependent, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("variable", "variable", str, True, None, True),
        ])
        return js


class StructureMapGroupRuleSource(backboneelement.BackboneElement):
    """ 
    S
    o
    u
    r
    c
    e
    i
    n
    p
    u
    t
    s
    t
    o
    t
    h
    e
    m
    a
    p
    p
    i
    n
    g
    .
    """
    
    resource_type = "StructureMapGroupRuleSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.check = None
        """ 
        F
        H
        I
        R
        P
        a
        t
        h
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        -
        m
        u
        s
        t
        b
        e
        t
        r
        u
        e
        o
        r
        t
        h
        e
        m
        a
        p
        p
        i
        n
        g
        e
        n
        g
        i
        n
        e
        t
        h
        r
        o
        w
        s
        a
        n
        e
        r
        r
        o
        r
        i
        n
        s
        t
        e
        a
        d
        o
        f
        c
        o
        m
        p
        l
        e
        t
        i
        n
        g
        .
        Type `str`. """
        
        self.condition = None
        """ 
        F
        H
        I
        R
        P
        a
        t
        h
        e
        x
        p
        r
        e
        s
        s
        i
        o
        n
        -
        m
        u
        s
        t
        b
        e
        t
        r
        u
        e
        o
        r
        t
        h
        e
        r
        u
        l
        e
        d
        o
        e
        s
        n
        o
        t
        a
        p
        p
        l
        y
        .
        Type `str`. """
        
        self.context = None
        """ 
        T
        y
        p
        e
        o
        r
        v
        a
        r
        i
        a
        b
        l
        e
        t
        h
        i
        s
        r
        u
        l
        e
        a
        p
        p
        l
        i
        e
        s
        t
        o
        .
        Type `str`. """
        
        self.defaultValueAddress = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAge = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueBoolean = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `bool`. """
        
        self.defaultValueCanonical = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueCode = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueCodeableConcept = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactDetail = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueContributor = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.defaultValueCount = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.defaultValueDataRequirement = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.defaultValueDate = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDateTime = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDecimal = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `float`. """
        
        self.defaultValueDistance = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.defaultValueDosage = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.defaultValueDuration = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.defaultValueExpression = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.defaultValueHumanName = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueId = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueIdentifier = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueInteger = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `int`. """
        
        self.defaultValueMarkdown = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueMoney = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.defaultValueOid = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueParameterDefinition = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.defaultValuePeriod = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValuePositiveInt = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `int`. """
        
        self.defaultValueQuantity = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueRelatedArtifact = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueString = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueTime = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueTiming = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueTriggerDefinition = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueUnsignedInt = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `int`. """
        
        self.defaultValueUri = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueUrl = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.defaultValueUsageContext = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.defaultValueUuid = None
        """ 
        D
        e
        f
        a
        u
        l
        t
        v
        a
        l
        u
        e
        i
        f
        n
        o
        v
        a
        l
        u
        e
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.element = None
        """ 
        O
        p
        t
        i
        o
        n
        a
        l
        f
        i
        e
        l
        d
        f
        o
        r
        t
        h
        i
        s
        s
        o
        u
        r
        c
        e
        .
        Type `str`. """
        
        self.listMode = None
        """ 
        f
        i
        r
        s
        t
        |
        n
        o
        t
        _
        f
        i
        r
        s
        t
        |
        l
        a
        s
        t
        |
        n
        o
        t
        _
        l
        a
        s
        t
        |
        o
        n
        l
        y
        _
        o
        n
        e
        .
        Type `str`. """
        
        self.logMessage = None
        """ 
        M
        e
        s
        s
        a
        g
        e
        t
        o
        p
        u
        t
        i
        n
        l
        o
        g
        i
        f
        s
        o
        u
        r
        c
        e
        e
        x
        i
        s
        t
        s
        (
        F
        H
        I
        R
        P
        a
        t
        h
        )
        .
        Type `str`. """
        
        self.max = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        d
        m
        a
        x
        i
        m
        u
        m
        c
        a
        r
        d
        i
        n
        a
        l
        i
        t
        y
        (
        n
        u
        m
        b
        e
        r
        o
        r
        *
        )
        .
        Type `str`. """
        
        self.min = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        e
        d
        m
        i
        n
        i
        m
        u
        m
        c
        a
        r
        d
        i
        n
        a
        l
        i
        t
        y
        .
        Type `int`. """
        
        self.type = None
        """ 
        R
        u
        l
        e
        o
        n
        l
        y
        a
        p
        p
        l
        i
        e
        s
        i
        f
        s
        o
        u
        r
        c
        e
        h
        a
        s
        t
        h
        i
        s
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.variable = None
        """ 
        N
        a
        m
        e
        d
        c
        o
        n
        t
        e
        x
        t
        f
        o
        r
        f
        i
        e
        l
        d
        ,
        i
        f
        a
        f
        i
        e
        l
        d
        i
        s
        s
        p
        e
        c
        i
        f
        i
        e
        d
        .
        Type `str`. """
        
        super(StructureMapGroupRuleSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleSource, self).elementProperties()
        js.extend([
            ("check", "check", str, False, None, False),
            ("condition", "condition", str, False, None, False),
            ("context", "context", str, False, None, True),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, False, None, False),
            ("logMessage", "logMessage", str, False, None, False),
            ("max", "max", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("type", "type", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js


class StructureMapGroupRuleTarget(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    e
    n
    t
    t
    o
    c
    r
    e
    a
    t
    e
    b
    e
    c
    a
    u
    s
    e
    o
    f
    t
    h
    i
    s
    m
    a
    p
    p
    i
    n
    g
    r
    u
    l
    e
    .
    """
    
    resource_type = "StructureMapGroupRuleTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.context = None
        """ 
        T
        y
        p
        e
        o
        r
        v
        a
        r
        i
        a
        b
        l
        e
        t
        h
        i
        s
        r
        u
        l
        e
        a
        p
        p
        l
        i
        e
        s
        t
        o
        .
        Type `str`. """
        
        self.contextType = None
        """ 
        t
        y
        p
        e
        |
        v
        a
        r
        i
        a
        b
        l
        e
        .
        Type `str`. """
        
        self.element = None
        """ 
        F
        i
        e
        l
        d
        t
        o
        c
        r
        e
        a
        t
        e
        i
        n
        t
        h
        e
        c
        o
        n
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.listMode = None
        """ 
        f
        i
        r
        s
        t
        |
        s
        h
        a
        r
        e
        |
        l
        a
        s
        t
        |
        c
        o
        l
        l
        a
        t
        e
        .
        List of `str` items. """
        
        self.listRuleId = None
        """ 
        I
        n
        t
        e
        r
        n
        a
        l
        r
        u
        l
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
        f
        o
        r
        s
        h
        a
        r
        e
        d
        l
        i
        s
        t
        i
        t
        e
        m
        s
        .
        Type `str`. """
        
        self.parameter = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        s
        t
        o
        t
        h
        e
        t
        r
        a
        n
        s
        f
        o
        r
        m
        .
        List of `StructureMapGroupRuleTargetParameter` items (represented as `dict` in JSON). """
        
        self.transform = None
        """ 
        c
        r
        e
        a
        t
        e
        |
        c
        o
        p
        y
        +
        .
        Type `str`. """
        
        self.variable = None
        """ 
        N
        a
        m
        e
        d
        c
        o
        n
        t
        e
        x
        t
        f
        o
        r
        f
        i
        e
        l
        d
        ,
        i
        f
        d
        e
        s
        i
        r
        e
        d
        ,
        a
        n
        d
        a
        f
        i
        e
        l
        d
        i
        s
        s
        p
        e
        c
        i
        f
        i
        e
        d
        .
        Type `str`. """
        
        super(StructureMapGroupRuleTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleTarget, self).elementProperties()
        js.extend([
            ("context", "context", str, False, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("element", "element", str, False, None, False),
            ("listMode", "listMode", str, True, None, False),
            ("listRuleId", "listRuleId", str, False, None, False),
            ("parameter", "parameter", StructureMapGroupRuleTargetParameter, True, None, False),
            ("transform", "transform", str, False, None, False),
            ("variable", "variable", str, False, None, False),
        ])
        return js


class StructureMapGroupRuleTargetParameter(backboneelement.BackboneElement):
    """ 
    P
    a
    r
    a
    m
    e
    t
    e
    r
    s
    t
    o
    t
    h
    e
    t
    r
    a
    n
    s
    f
    o
    r
    m
    .
    """
    
    resource_type = "StructureMapGroupRuleTargetParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.valueBoolean = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        v
        a
        l
        u
        e
        -
        v
        a
        r
        i
        a
        b
        l
        e
        o
        r
        l
        i
        t
        e
        r
        a
        l
        .
        Type `bool`. """
        
        self.valueDecimal = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        v
        a
        l
        u
        e
        -
        v
        a
        r
        i
        a
        b
        l
        e
        o
        r
        l
        i
        t
        e
        r
        a
        l
        .
        Type `float`. """
        
        self.valueId = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        v
        a
        l
        u
        e
        -
        v
        a
        r
        i
        a
        b
        l
        e
        o
        r
        l
        i
        t
        e
        r
        a
        l
        .
        Type `str`. """
        
        self.valueInteger = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        v
        a
        l
        u
        e
        -
        v
        a
        r
        i
        a
        b
        l
        e
        o
        r
        l
        i
        t
        e
        r
        a
        l
        .
        Type `int`. """
        
        self.valueString = None
        """ 
        P
        a
        r
        a
        m
        e
        t
        e
        r
        v
        a
        l
        u
        e
        -
        v
        a
        r
        i
        a
        b
        l
        e
        o
        r
        l
        i
        t
        e
        r
        a
        l
        .
        Type `str`. """
        
        super(StructureMapGroupRuleTargetParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapGroupRuleTargetParameter, self).elementProperties()
        js.extend([
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
        ])
        return js


class StructureMapStructure(backboneelement.BackboneElement):
    """ 
    S
    t
    r
    u
    c
    t
    u
    r
    e
    D
    e
    f
    i
    n
    i
    t
    i
    o
    n
    u
    s
    e
    d
    b
    y
    t
    h
    i
    s
    m
    a
    p
    .
    
    
    A
    s
    t
    r
    u
    c
    t
    u
    r
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
    u
    s
    e
    d
    b
    y
    t
    h
    i
    s
    m
    a
    p
    .
    T
    h
    e
    s
    t
    r
    u
    c
    t
    u
    r
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
    m
    a
    y
    d
    e
    s
    c
    r
    i
    b
    e
    i
    n
    s
    t
    a
    n
    c
    e
    s
    t
    h
    a
    t
    a
    r
    e
    c
    o
    n
    v
    e
    r
    t
    e
    d
    ,
    o
    r
    t
    h
    e
    i
    n
    s
    t
    a
    n
    c
    e
    s
    t
    h
    a
    t
    a
    r
    e
    p
    r
    o
    d
    u
    c
    e
    d
    .
    
    """
    
    resource_type = "StructureMapStructure"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        t
        y
        p
        e
        i
        n
        t
        h
        i
        s
        m
        a
        p
        .
        Type `str`. """
        
        self.documentation = None
        """ 
        D
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
        o
        n
        u
        s
        e
        o
        f
        s
        t
        r
        u
        c
        t
        u
        r
        e
        .
        Type `str`. """
        
        self.mode = None
        """ 
        s
        o
        u
        r
        c
        e
        |
        q
        u
        e
        r
        i
        e
        d
        |
        t
        a
        r
        g
        e
        t
        |
        p
        r
        o
        d
        u
        c
        e
        d
        .
        Type `str`. """
        
        self.url = None
        """ 
        C
        a
        n
        o
        n
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
        t
        o
        s
        t
        r
        u
        c
        t
        u
        r
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
        .
        Type `str`. """
        
        super(StructureMapStructure, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(StructureMapStructure, self).elementProperties()
        js.extend([
            ("alias", "alias", str, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("mode", "mode", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


import sys
try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + '.address']
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import contributor
except ImportError:
    contributor = sys.modules[__package__ + '.contributor']
try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']
try:
    from . import datarequirement
except ImportError:
    datarequirement = sys.modules[__package__ + '.datarequirement']
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + '.expression']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + '.humanname']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import parameterdefinition
except ImportError:
    parameterdefinition = sys.modules[__package__ + '.parameterdefinition']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + '.ratio']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + '.sampleddata']
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + '.signature']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
try:
    from . import triggerdefinition
except ImportError:
    triggerdefinition = sys.modules[__package__ + '.triggerdefinition']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
