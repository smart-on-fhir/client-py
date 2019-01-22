#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/OperationDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class OperationDefinition(domainresource.DomainResource):
    """ 
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
    o
    f
    a
    n
    o
    p
    e
    r
    a
    t
    i
    o
    n
    o
    r
    a
    n
    a
    m
    e
    d
    q
    u
    e
    r
    y
    .
    
    
    A
    f
    o
    r
    m
    a
    l
    c
    o
    m
    p
    u
    t
    a
    b
    l
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
    o
    f
    a
    n
    o
    p
    e
    r
    a
    t
    i
    o
    n
    (
    o
    n
    t
    h
    e
    R
    E
    S
    T
    f
    u
    l
    i
    n
    t
    e
    r
    f
    a
    c
    e
    )
    o
    r
    a
    n
    a
    m
    e
    d
    q
    u
    e
    r
    y
    (
    u
    s
    i
    n
    g
    t
    h
    e
    s
    e
    a
    r
    c
    h
    i
    n
    t
    e
    r
    a
    c
    t
    i
    o
    n
    )
    .
    
    """
    
    resource_type = "OperationDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.affectsState = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        c
        o
        n
        t
        e
        n
        t
        i
        s
        c
        h
        a
        n
        g
        e
        d
        b
        y
        t
        h
        e
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `bool`. """
        
        self.base = None
        """ 
        M
        a
        r
        k
        s
        t
        h
        i
        s
        a
        s
        a
        p
        r
        o
        f
        i
        l
        e
        o
        f
        t
        h
        e
        b
        a
        s
        e
        .
        Type `str`. """
        
        self.code = None
        """ 
        N
        a
        m
        e
        u
        s
        e
        d
        t
        o
        i
        n
        v
        o
        k
        e
        t
        h
        e
        o
        p
        e
        r
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.comment = None
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
        u
        s
        e
        .
        Type `str`. """
        
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
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        
        self.inputProfile = None
        """ 
        V
        a
        l
        i
        d
        a
        t
        i
        o
        n
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
        i
        n
        p
        a
        r
        a
        m
        e
        t
        e
        r
        s
        .
        Type `str`. """
        
        self.instance = None
        """ 
        I
        n
        v
        o
        k
        e
        o
        n
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
        ?
        .
        Type `bool`. """
        
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
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        
        self.kind = None
        """ 
        o
        p
        e
        r
        a
        t
        i
        o
        n
        |
        q
        u
        e
        r
        y
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
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        
        self.outputProfile = None
        """ 
        V
        a
        l
        i
        d
        a
        t
        i
        o
        n
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
        o
        u
        t
        p
        a
        r
        a
        m
        e
        t
        e
        r
        s
        .
        Type `str`. """
        
        self.overload = None
        """ 
        D
        e
        f
        i
        n
        e
        o
        v
        e
        r
        l
        o
        a
        d
        e
        d
        v
        a
        r
        i
        a
        n
        t
        s
        f
        o
        r
        w
        h
        e
        n
        g
        e
        n
        e
        r
        a
        t
        i
        n
        g
        c
        o
        d
        e
        .
        List of `OperationDefinitionOverload` items (represented as `dict` in JSON). """
        
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
        f
        o
        r
        t
        h
        e
        o
        p
        e
        r
        a
        t
        i
        o
        n
        /
        q
        u
        e
        r
        y
        .
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
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
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        
        self.resource = None
        """ 
        T
        y
        p
        e
        s
        t
        h
        i
        s
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        List of `str` items. """
        
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
        
        self.system = None
        """ 
        I
        n
        v
        o
        k
        e
        a
        t
        t
        h
        e
        s
        y
        s
        t
        e
        m
        l
        e
        v
        e
        l
        ?
        .
        Type `bool`. """
        
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
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        
        self.type = None
        """ 
        I
        n
        v
        o
        k
        e
        a
        t
        t
        h
        e
        t
        y
        p
        e
        l
        e
        v
        e
        l
        ?
        .
        Type `bool`. """
        
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
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        o
        p
        e
        r
        a
        t
        i
        o
        n
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
        
        super(OperationDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinition, self).elementProperties()
        js.extend([
            ("affectsState", "affectsState", bool, False, None, False),
            ("base", "base", str, False, None, False),
            ("code", "code", str, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("inputProfile", "inputProfile", str, False, None, False),
            ("instance", "instance", bool, False, None, True),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("outputProfile", "outputProfile", str, False, None, False),
            ("overload", "overload", OperationDefinitionOverload, True, None, False),
            ("parameter", "parameter", OperationDefinitionParameter, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("resource", "resource", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("system", "system", bool, False, None, True),
            ("title", "title", str, False, None, False),
            ("type", "type", bool, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class OperationDefinitionOverload(backboneelement.BackboneElement):
    """ 
    D
    e
    f
    i
    n
    e
    o
    v
    e
    r
    l
    o
    a
    d
    e
    d
    v
    a
    r
    i
    a
    n
    t
    s
    f
    o
    r
    w
    h
    e
    n
    g
    e
    n
    e
    r
    a
    t
    i
    n
    g
    c
    o
    d
    e
    .
    
    
    D
    e
    f
    i
    n
    e
    s
    a
    n
    a
    p
    p
    r
    o
    p
    r
    i
    a
    t
    e
    c
    o
    m
    b
    i
    n
    a
    t
    i
    o
    n
    o
    f
    p
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
    u
    s
    e
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
    i
    s
    o
    p
    e
    r
    a
    t
    i
    o
    n
    ,
    t
    o
    h
    e
    l
    p
    c
    o
    d
    e
    g
    e
    n
    e
    r
    a
    t
    o
    r
    s
    w
    h
    e
    n
    g
    e
    n
    e
    r
    a
    t
    i
    n
    g
    o
    v
    e
    r
    l
    o
    a
    d
    e
    d
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    e
    t
    s
    f
    o
    r
    t
    h
    i
    s
    o
    p
    e
    r
    a
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "OperationDefinitionOverload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        s
        t
        o
        g
        o
        o
        n
        o
        v
        e
        r
        l
        o
        a
        d
        .
        Type `str`. """
        
        self.parameterName = None
        """ 
        N
        a
        m
        e
        o
        f
        p
        a
        r
        a
        m
        e
        t
        e
        r
        t
        o
        i
        n
        c
        l
        u
        d
        e
        i
        n
        o
        v
        e
        r
        l
        o
        a
        d
        .
        List of `str` items. """
        
        super(OperationDefinitionOverload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionOverload, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("parameterName", "parameterName", str, True, None, False),
        ])
        return js


class OperationDefinitionParameter(backboneelement.BackboneElement):
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
    f
    o
    r
    t
    h
    e
    o
    p
    e
    r
    a
    t
    i
    o
    n
    /
    q
    u
    e
    r
    y
    .
    
    
    T
    h
    e
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    f
    o
    r
    t
    h
    e
    o
    p
    e
    r
    a
    t
    i
    o
    n
    /
    q
    u
    e
    r
    y
    .
    
    """
    
    resource_type = "OperationDefinitionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.binding = None
        """ 
        V
        a
        l
        u
        e
        S
        e
        t
        d
        e
        t
        a
        i
        l
        s
        i
        f
        t
        h
        i
        s
        i
        s
        c
        o
        d
        e
        d
        .
        Type `OperationDefinitionParameterBinding` (represented as `dict` in JSON). """
        
        self.documentation = None
        """ 
        D
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
        m
        e
        a
        n
        i
        n
        g
        /
        u
        s
        e
        .
        Type `str`. """
        
        self.max = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        C
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
        a
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
        M
        i
        n
        i
        m
        u
        m
        C
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
        
        self.name = None
        """ 
        N
        a
        m
        e
        i
        n
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
        .
        p
        a
        r
        a
        m
        e
        t
        e
        r
        .
        n
        a
        m
        e
        o
        r
        i
        n
        U
        R
        L
        .
        Type `str`. """
        
        self.part = None
        """ 
        P
        a
        r
        t
        s
        o
        f
        a
        n
        e
        s
        t
        e
        d
        P
        a
        r
        a
        m
        e
        t
        e
        r
        .
        List of `OperationDefinitionParameter` items (represented as `dict` in JSON). """
        
        self.referencedFrom = None
        """ 
        R
        e
        f
        e
        r
        e
        n
        c
        e
        s
        t
        o
        t
        h
        i
        s
        p
        a
        r
        a
        m
        e
        t
        e
        r
        .
        List of `OperationDefinitionParameterReferencedFrom` items (represented as `dict` in JSON). """
        
        self.searchType = None
        """ 
        n
        u
        m
        b
        e
        r
        |
        d
        a
        t
        e
        |
        s
        t
        r
        i
        n
        g
        |
        t
        o
        k
        e
        n
        |
        r
        e
        f
        e
        r
        e
        n
        c
        e
        |
        c
        o
        m
        p
        o
        s
        i
        t
        e
        |
        q
        u
        a
        n
        t
        i
        t
        y
        |
        u
        r
        i
        |
        s
        p
        e
        c
        i
        a
        l
        .
        Type `str`. """
        
        self.targetProfile = None
        """ 
        I
        f
        t
        y
        p
        e
        i
        s
        R
        e
        f
        e
        r
        e
        n
        c
        e
        |
        c
        a
        n
        o
        n
        i
        c
        a
        l
        ,
        a
        l
        l
        o
        w
        e
        d
        t
        a
        r
        g
        e
        t
        s
        .
        List of `str` items. """
        
        self.type = None
        """ 
        W
        h
        a
        t
        t
        y
        p
        e
        t
        h
        i
        s
        p
        a
        r
        a
        m
        e
        t
        e
        r
        h
        a
        s
        .
        Type `str`. """
        
        self.use = None
        """ 
        i
        n
        |
        o
        u
        t
        .
        Type `str`. """
        
        super(OperationDefinitionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameter, self).elementProperties()
        js.extend([
            ("binding", "binding", OperationDefinitionParameterBinding, False, None, False),
            ("documentation", "documentation", str, False, None, False),
            ("max", "max", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("name", "name", str, False, None, True),
            ("part", "part", OperationDefinitionParameter, True, None, False),
            ("referencedFrom", "referencedFrom", OperationDefinitionParameterReferencedFrom, True, None, False),
            ("searchType", "searchType", str, False, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("type", "type", str, False, None, False),
            ("use", "use", str, False, None, True),
        ])
        return js


class OperationDefinitionParameterBinding(backboneelement.BackboneElement):
    """ 
    V
    a
    l
    u
    e
    S
    e
    t
    d
    e
    t
    a
    i
    l
    s
    i
    f
    t
    h
    i
    s
    i
    s
    c
    o
    d
    e
    d
    .
    
    
    B
    i
    n
    d
    s
    t
    o
    a
    v
    a
    l
    u
    e
    s
    e
    t
    i
    f
    t
    h
    i
    s
    p
    a
    r
    a
    m
    e
    t
    e
    r
    i
    s
    c
    o
    d
    e
    d
    (
    c
    o
    d
    e
    ,
    C
    o
    d
    i
    n
    g
    ,
    C
    o
    d
    e
    a
    b
    l
    e
    C
    o
    n
    c
    e
    p
    t
    )
    .
    
    """
    
    resource_type = "OperationDefinitionParameterBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.strength = None
        """ 
        r
        e
        q
        u
        i
        r
        e
        d
        |
        e
        x
        t
        e
        n
        s
        i
        b
        l
        e
        |
        p
        r
        e
        f
        e
        r
        r
        e
        d
        |
        e
        x
        a
        m
        p
        l
        e
        .
        Type `str`. """
        
        self.valueSet = None
        """ 
        S
        o
        u
        r
        c
        e
        o
        f
        v
        a
        l
        u
        e
        s
        e
        t
        .
        Type `str`. """
        
        super(OperationDefinitionParameterBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterBinding, self).elementProperties()
        js.extend([
            ("strength", "strength", str, False, None, True),
            ("valueSet", "valueSet", str, False, None, True),
        ])
        return js


class OperationDefinitionParameterReferencedFrom(backboneelement.BackboneElement):
    """ 
    R
    e
    f
    e
    r
    e
    n
    c
    e
    s
    t
    o
    t
    h
    i
    s
    p
    a
    r
    a
    m
    e
    t
    e
    r
    .
    
    
    I
    d
    e
    n
    t
    i
    f
    i
    e
    s
    o
    t
    h
    e
    r
    r
    e
    s
    o
    u
    r
    c
    e
    p
    a
    r
    a
    m
    e
    t
    e
    r
    s
    w
    i
    t
    h
    i
    n
    t
    h
    e
    o
    p
    e
    r
    a
    t
    i
    o
    n
    i
    n
    v
    o
    c
    a
    t
    i
    o
    n
    t
    h
    a
    t
    a
    r
    e
    e
    x
    p
    e
    c
    t
    e
    d
    t
    o
    r
    e
    s
    o
    l
    v
    e
    t
    o
    t
    h
    i
    s
    r
    e
    s
    o
    u
    r
    c
    e
    .
    
    """
    
    resource_type = "OperationDefinitionParameterReferencedFrom"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        """ 
        R
        e
        f
        e
        r
        e
        n
        c
        i
        n
        g
        p
        a
        r
        a
        m
        e
        t
        e
        r
        .
        Type `str`. """
        
        self.sourceId = None
        """ 
        E
        l
        e
        m
        e
        n
        t
        i
        d
        o
        f
        r
        e
        f
        e
        r
        e
        n
        c
        e
        .
        Type `str`. """
        
        super(OperationDefinitionParameterReferencedFrom, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(OperationDefinitionParameterReferencedFrom, self).elementProperties()
        js.extend([
            ("source", "source", str, False, None, True),
            ("sourceId", "sourceId", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + '.contactdetail']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
