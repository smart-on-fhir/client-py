#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ValueSet) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ValueSet(domainresource.DomainResource):
    """ 
    A
    s
    e
    t
    o
    f
    c
    o
    d
    e
    s
    d
    r
    a
    w
    n
    f
    r
    o
    m
    o
    n
    e
    o
    r
    m
    o
    r
    e
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    s
    .
    
    
    A
    V
    a
    l
    u
    e
    S
    e
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
    n
    s
    t
    a
    n
    c
    e
    s
    p
    e
    c
    i
    f
    i
    e
    s
    a
    s
    e
    t
    o
    f
    c
    o
    d
    e
    s
    d
    r
    a
    w
    n
    f
    r
    o
    m
    o
    n
    e
    o
    r
    m
    o
    r
    e
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    s
    ,
    i
    n
    t
    e
    n
    d
    e
    d
    f
    o
    r
    u
    s
    e
    i
    n
    a
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    c
    o
    n
    t
    e
    x
    t
    .
    V
    a
    l
    u
    e
    s
    e
    t
    s
    l
    i
    n
    k
    b
    e
    t
    w
    e
    e
    n
    [
    C
    o
    d
    e
    S
    y
    s
    t
    e
    m
    ]
    (
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    .
    h
    t
    m
    l
    )
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
    s
    a
    n
    d
    t
    h
    e
    i
    r
    u
    s
    e
    i
    n
    [
    c
    o
    d
    e
    d
    e
    l
    e
    m
    e
    n
    t
    s
    ]
    (
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
    i
    e
    s
    .
    h
    t
    m
    l
    )
    .
    
    """
    
    resource_type = "ValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.compose = None
        """ 
        C
        o
        n
        t
        e
        n
        t
        l
        o
        g
        i
        c
        a
        l
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
        t
        h
        e
        v
        a
        l
        u
        e
        s
        e
        t
        (
        C
        L
        D
        )
        .
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
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
        
        self.expansion = None
        """ 
        U
        s
        e
        d
        w
        h
        e
        n
        t
        h
        e
        v
        a
        l
        u
        e
        s
        e
        t
        i
        s
        "
        e
        x
        p
        a
        n
        d
        e
        d
        "
        .
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
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
        v
        a
        l
        u
        e
        s
        e
        t
        (
        b
        u
        s
        i
        n
        e
        s
        s
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
        )
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.immutable = None
        """ 
        I
        n
        d
        i
        c
        a
        t
        e
        s
        w
        h
        e
        t
        h
        e
        r
        o
        r
        n
        o
        t
        a
        n
        y
        c
        h
        a
        n
        g
        e
        t
        o
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
        l
        o
        g
        i
        c
        a
        l
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
        o
        c
        c
        u
        r
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
        v
        a
        l
        u
        e
        s
        e
        t
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
        v
        a
        l
        u
        e
        s
        e
        t
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
        v
        a
        l
        u
        e
        s
        e
        t
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
        v
        a
        l
        u
        e
        s
        e
        t
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
        v
        a
        l
        u
        e
        s
        e
        t
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
        
        super(ValueSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("compose", "compose", ValueSetCompose, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("expansion", "expansion", ValueSetExpansion, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("immutable", "immutable", bool, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ValueSetCompose(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    t
    e
    n
    t
    l
    o
    g
    i
    c
    a
    l
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
    t
    h
    e
    v
    a
    l
    u
    e
    s
    e
    t
    (
    C
    L
    D
    )
    .
    
    
    A
    s
    e
    t
    o
    f
    c
    r
    i
    t
    e
    r
    i
    a
    t
    h
    a
    t
    d
    e
    f
    i
    n
    e
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
    s
    o
    f
    t
    h
    e
    v
    a
    l
    u
    e
    s
    e
    t
    b
    y
    i
    n
    c
    l
    u
    d
    i
    n
    g
    o
    r
    e
    x
    c
    l
    u
    d
    i
    n
    g
    c
    o
    d
    e
    s
    s
    e
    l
    e
    c
    t
    e
    d
    f
    r
    o
    m
    t
    h
    e
    s
    p
    e
    c
    i
    f
    i
    e
    d
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    (
    s
    )
    t
    h
    a
    t
    t
    h
    e
    v
    a
    l
    u
    e
    s
    e
    t
    d
    r
    a
    w
    s
    f
    r
    o
    m
    .
    T
    h
    i
    s
    i
    s
    a
    l
    s
    o
    k
    n
    o
    w
    n
    a
    s
    t
    h
    e
    C
    o
    n
    t
    e
    n
    t
    L
    o
    g
    i
    c
    a
    l
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
    (
    C
    L
    D
    )
    .
    
    """
    
    resource_type = "ValueSetCompose"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exclude = None
        """ 
        E
        x
        p
        l
        i
        c
        i
        t
        l
        y
        e
        x
        c
        l
        u
        d
        e
        c
        o
        d
        e
        s
        f
        r
        o
        m
        a
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        o
        r
        o
        t
        h
        e
        r
        v
        a
        l
        u
        e
        s
        e
        t
        s
        .
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.inactive = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        i
        n
        a
        c
        t
        i
        v
        e
        c
        o
        d
        e
        s
        a
        r
        e
        i
        n
        t
        h
        e
        v
        a
        l
        u
        e
        s
        e
        t
        .
        Type `bool`. """
        
        self.include = None
        """ 
        I
        n
        c
        l
        u
        d
        e
        o
        n
        e
        o
        r
        m
        o
        r
        e
        c
        o
        d
        e
        s
        f
        r
        o
        m
        a
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        o
        r
        o
        t
        h
        e
        r
        v
        a
        l
        u
        e
        s
        e
        t
        (
        s
        )
        .
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.lockedDate = None
        """ 
        F
        i
        x
        e
        d
        d
        a
        t
        e
        f
        o
        r
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
        w
        i
        t
        h
        n
        o
        s
        p
        e
        c
        i
        f
        i
        e
        d
        v
        e
        r
        s
        i
        o
        n
        (
        t
        r
        a
        n
        s
        i
        t
        i
        v
        e
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ValueSetComposeInclude, True, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("include", "include", ValueSetComposeInclude, True, None, True),
            ("lockedDate", "lockedDate", fhirdate.FHIRDate, False, None, False),
        ])
        return js


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ 
    I
    n
    c
    l
    u
    d
    e
    o
    n
    e
    o
    r
    m
    o
    r
    e
    c
    o
    d
    e
    s
    f
    r
    o
    m
    a
    c
    o
    d
    e
    s
    y
    s
    t
    e
    m
    o
    r
    o
    t
    h
    e
    r
    v
    a
    l
    u
    e
    s
    e
    t
    (
    s
    )
    .
    """
    
    resource_type = "ValueSetComposeInclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.concept = None
        """ 
        A
        c
        o
        n
        c
        e
        p
        t
        d
        e
        f
        i
        n
        e
        d
        i
        n
        t
        h
        e
        s
        y
        s
        t
        e
        m
        .
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        
        self.filter = None
        """ 
        S
        e
        l
        e
        c
        t
        c
        o
        d
        e
        s
        /
        c
        o
        n
        c
        e
        p
        t
        s
        b
        y
        t
        h
        e
        i
        r
        p
        r
        o
        p
        e
        r
        t
        i
        e
        s
        (
        i
        n
        c
        l
        u
        d
        i
        n
        g
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
        )
        .
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        
        self.system = None
        """ 
        T
        h
        e
        s
        y
        s
        t
        e
        m
        t
        h
        e
        c
        o
        d
        e
        s
        c
        o
        m
        e
        f
        r
        o
        m
        .
        Type `str`. """
        
        self.valueSet = None
        """ 
        S
        e
        l
        e
        c
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
        s
        i
        n
        c
        l
        u
        d
        e
        d
        i
        n
        t
        h
        i
        s
        v
        a
        l
        u
        e
        s
        e
        t
        .
        List of `str` items. """
        
        self.version = None
        """ 
        S
        p
        e
        c
        i
        f
        i
        c
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
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        r
        e
        f
        e
        r
        r
        e
        d
        t
        o
        .
        Type `str`. """
        
        super(ValueSetComposeInclude, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("concept", "concept", ValueSetComposeIncludeConcept, True, None, False),
            ("filter", "filter", ValueSetComposeIncludeFilter, True, None, False),
            ("system", "system", str, False, None, False),
            ("valueSet", "valueSet", str, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ 
    A
    c
    o
    n
    c
    e
    p
    t
    d
    e
    f
    i
    n
    e
    d
    i
    n
    t
    h
    e
    s
    y
    s
    t
    e
    m
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
    a
    c
    o
    n
    c
    e
    p
    t
    t
    o
    b
    e
    i
    n
    c
    l
    u
    d
    e
    d
    o
    r
    e
    x
    c
    l
    u
    d
    e
    d
    .
    
    """
    
    resource_type = "ValueSetComposeIncludeConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ 
        C
        o
        d
        e
        o
        r
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
        f
        r
        o
        m
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.designation = None
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
        s
        f
        o
        r
        t
        h
        i
        s
        c
        o
        n
        c
        e
        p
        t
        .
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ 
        T
        e
        x
        t
        t
        o
        d
        i
        s
        p
        l
        a
        y
        f
        o
        r
        t
        h
        i
        s
        c
        o
        d
        e
        f
        o
        r
        t
        h
        i
        s
        v
        a
        l
        u
        e
        s
        e
        t
        i
        n
        t
        h
        i
        s
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
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
        ])
        return js


class ValueSetComposeIncludeConceptDesignation(backboneelement.BackboneElement):
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
    s
    f
    o
    r
    t
    h
    i
    s
    c
    o
    n
    c
    e
    p
    t
    .
    
    
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
    s
    f
    o
    r
    t
    h
    i
    s
    c
    o
    n
    c
    e
    p
    t
    w
    h
    e
    n
    u
    s
    e
    d
    i
    n
    t
    h
    i
    s
    v
    a
    l
    u
    e
    s
    e
    t
    -
    o
    t
    h
    e
    r
    l
    a
    n
    g
    u
    a
    g
    e
    s
    ,
    a
    l
    i
    a
    s
    e
    s
    ,
    s
    p
    e
    c
    i
    a
    l
    i
    z
    e
    d
    p
    u
    r
    p
    o
    s
    e
    s
    ,
    u
    s
    e
    d
    f
    o
    r
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    p
    u
    r
    p
    o
    s
    e
    s
    ,
    e
    t
    c
    .
    
    """
    
    resource_type = "ValueSetComposeIncludeConceptDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ 
        H
        u
        m
        a
        n
        l
        a
        n
        g
        u
        a
        g
        e
        o
        f
        t
        h
        e
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.use = None
        """ 
        T
        y
        p
        e
        s
        o
        f
        u
        s
        e
        s
        o
        f
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        s
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ 
        T
        h
        e
        t
        e
        x
        t
        v
        a
        l
        u
        e
        f
        o
        r
        t
        h
        i
        s
        d
        e
        s
        i
        g
        n
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        super(ValueSetComposeIncludeConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ 
    S
    e
    l
    e
    c
    t
    c
    o
    d
    e
    s
    /
    c
    o
    n
    c
    e
    p
    t
    s
    b
    y
    t
    h
    e
    i
    r
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    (
    i
    n
    c
    l
    u
    d
    i
    n
    g
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
    )
    .
    
    
    S
    e
    l
    e
    c
    t
    c
    o
    n
    c
    e
    p
    t
    s
    b
    y
    s
    p
    e
    c
    i
    f
    y
    a
    m
    a
    t
    c
    h
    i
    n
    g
    c
    r
    i
    t
    e
    r
    i
    o
    n
    b
    a
    s
    e
    d
    o
    n
    t
    h
    e
    p
    r
    o
    p
    e
    r
    t
    i
    e
    s
    (
    i
    n
    c
    l
    u
    d
    i
    n
    g
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
    )
    d
    e
    f
    i
    n
    e
    d
    b
    y
    t
    h
    e
    s
    y
    s
    t
    e
    m
    ,
    o
    r
    o
    n
    f
    i
    l
    t
    e
    r
    s
    d
    e
    f
    i
    n
    e
    d
    b
    y
    t
    h
    e
    s
    y
    s
    t
    e
    m
    .
    I
    f
    m
    u
    l
    t
    i
    p
    l
    e
    f
    i
    l
    t
    e
    r
    s
    a
    r
    e
    s
    p
    e
    c
    i
    f
    i
    e
    d
    ,
    t
    h
    e
    y
    S
    H
    A
    L
    L
    a
    l
    l
    b
    e
    t
    r
    u
    e
    .
    
    """
    
    resource_type = "ValueSetComposeIncludeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.op = None
        """ 
        =
        |
        i
        s
        -
        a
        |
        d
        e
        s
        c
        e
        n
        d
        e
        n
        t
        -
        o
        f
        |
        i
        s
        -
        n
        o
        t
        -
        a
        |
        r
        e
        g
        e
        x
        |
        i
        n
        |
        n
        o
        t
        -
        i
        n
        |
        g
        e
        n
        e
        r
        a
        l
        i
        z
        e
        s
        |
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        self.property = None
        """ 
        A
        p
        r
        o
        p
        e
        r
        t
        y
        /
        f
        i
        l
        t
        e
        r
        d
        e
        f
        i
        n
        e
        d
        b
        y
        t
        h
        e
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.value = None
        """ 
        C
        o
        d
        e
        f
        r
        o
        m
        t
        h
        e
        s
        y
        s
        t
        e
        m
        ,
        o
        r
        r
        e
        g
        e
        x
        c
        r
        i
        t
        e
        r
        i
        a
        ,
        o
        r
        b
        o
        o
        l
        e
        a
        n
        v
        a
        l
        u
        e
        f
        o
        r
        e
        x
        i
        s
        t
        s
        .
        Type `str`. """
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("op", "op", str, False, None, True),
            ("property", "property", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class ValueSetExpansion(backboneelement.BackboneElement):
    """ 
    U
    s
    e
    d
    w
    h
    e
    n
    t
    h
    e
    v
    a
    l
    u
    e
    s
    e
    t
    i
    s
    "
    e
    x
    p
    a
    n
    d
    e
    d
    "
    .
    
    
    A
    v
    a
    l
    u
    e
    s
    e
    t
    c
    a
    n
    a
    l
    s
    o
    b
    e
    "
    e
    x
    p
    a
    n
    d
    e
    d
    "
    ,
    w
    h
    e
    r
    e
    t
    h
    e
    v
    a
    l
    u
    e
    s
    e
    t
    i
    s
    t
    u
    r
    n
    e
    d
    i
    n
    t
    o
    a
    s
    i
    m
    p
    l
    e
    c
    o
    l
    l
    e
    c
    t
    i
    o
    n
    o
    f
    e
    n
    u
    m
    e
    r
    a
    t
    e
    d
    c
    o
    d
    e
    s
    .
    T
    h
    i
    s
    e
    l
    e
    m
    e
    n
    t
    h
    o
    l
    d
    s
    t
    h
    e
    e
    x
    p
    a
    n
    s
    i
    o
    n
    ,
    i
    f
    i
    t
    h
    a
    s
    b
    e
    e
    n
    p
    e
    r
    f
    o
    r
    m
    e
    d
    .
    
    """
    
    resource_type = "ValueSetExpansion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contains = None
        """ 
        C
        o
        d
        e
        s
        i
        n
        t
        h
        e
        v
        a
        l
        u
        e
        s
        e
        t
        .
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
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
        t
        h
        e
        v
        a
        l
        u
        e
        s
        e
        t
        e
        x
        p
        a
        n
        s
        i
        o
        n
        (
        b
        u
        s
        i
        n
        e
        s
        s
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
        )
        .
        Type `str`. """
        
        self.offset = None
        """ 
        O
        f
        f
        s
        e
        t
        a
        t
        w
        h
        i
        c
        h
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
        s
        t
        a
        r
        t
        s
        .
        Type `int`. """
        
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
        t
        h
        a
        t
        c
        o
        n
        t
        r
        o
        l
        l
        e
        d
        t
        h
        e
        e
        x
        p
        a
        n
        s
        i
        o
        n
        p
        r
        o
        c
        e
        s
        s
        .
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """
        
        self.timestamp = None
        """ 
        T
        i
        m
        e
        V
        a
        l
        u
        e
        S
        e
        t
        e
        x
        p
        a
        n
        s
        i
        o
        n
        h
        a
        p
        p
        e
        n
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.total = None
        """ 
        T
        o
        t
        a
        l
        n
        u
        m
        b
        e
        r
        o
        f
        c
        o
        d
        e
        s
        i
        n
        t
        h
        e
        e
        x
        p
        a
        n
        s
        i
        o
        n
        .
        Type `int`. """
        
        super(ValueSetExpansion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("identifier", "identifier", str, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True, None, False),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, True),
            ("total", "total", int, False, None, False),
        ])
        return js


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ 
    C
    o
    d
    e
    s
    i
    n
    t
    h
    e
    v
    a
    l
    u
    e
    s
    e
    t
    .
    
    
    T
    h
    e
    c
    o
    d
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
    e
    v
    a
    l
    u
    e
    s
    e
    t
    e
    x
    p
    a
    n
    s
    i
    o
    n
    .
    
    """
    
    resource_type = "ValueSetExpansionContains"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None
        """ 
        I
        f
        u
        s
        e
        r
        c
        a
        n
        n
        o
        t
        s
        e
        l
        e
        c
        t
        t
        h
        i
        s
        e
        n
        t
        r
        y
        .
        Type `bool`. """
        
        self.code = None
        """ 
        C
        o
        d
        e
        -
        i
        f
        b
        l
        a
        n
        k
        ,
        t
        h
        i
        s
        i
        s
        n
        o
        t
        a
        s
        e
        l
        e
        c
        t
        a
        b
        l
        e
        c
        o
        d
        e
        .
        Type `str`. """
        
        self.contains = None
        """ 
        C
        o
        d
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
        u
        n
        d
        e
        r
        t
        h
        i
        s
        e
        n
        t
        r
        y
        .
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.designation = None
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
        s
        f
        o
        r
        t
        h
        i
        s
        i
        t
        e
        m
        .
        List of `ValueSetComposeIncludeConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None
        """ 
        U
        s
        e
        r
        d
        i
        s
        p
        l
        a
        y
        f
        o
        r
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
        
        self.inactive = None
        """ 
        I
        f
        c
        o
        n
        c
        e
        p
        t
        i
        s
        i
        n
        a
        c
        t
        i
        v
        e
        i
        n
        t
        h
        e
        c
        o
        d
        e
        s
        y
        s
        t
        e
        m
        .
        Type `bool`. """
        
        self.system = None
        """ 
        S
        y
        s
        t
        e
        m
        v
        a
        l
        u
        e
        f
        o
        r
        t
        h
        e
        c
        o
        d
        e
        .
        Type `str`. """
        
        self.version = None
        """ 
        V
        e
        r
        s
        i
        o
        n
        i
        n
        w
        h
        i
        c
        h
        t
        h
        i
        s
        c
        o
        d
        e
        /
        d
        i
        s
        p
        l
        a
        y
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
        
        super(ValueSetExpansionContains, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, False),
            ("code", "code", str, False, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("designation", "designation", ValueSetComposeIncludeConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("system", "system", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class ValueSetExpansionParameter(backboneelement.BackboneElement):
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
    t
    h
    a
    t
    c
    o
    n
    t
    r
    o
    l
    l
    e
    d
    t
    h
    e
    e
    x
    p
    a
    n
    s
    i
    o
    n
    p
    r
    o
    c
    e
    s
    s
    .
    
    
    A
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
    h
    a
    t
    c
    o
    n
    t
    r
    o
    l
    l
    e
    d
    t
    h
    e
    e
    x
    p
    a
    n
    s
    i
    o
    n
    p
    r
    o
    c
    e
    s
    s
    .
    T
    h
    e
    s
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
    m
    a
    y
    b
    e
    u
    s
    e
    d
    b
    y
    u
    s
    e
    r
    s
    o
    f
    e
    x
    p
    a
    n
    d
    e
    d
    v
    a
    l
    u
    e
    s
    e
    t
    s
    t
    o
    c
    h
    e
    c
    k
    w
    h
    e
    t
    h
    e
    r
    t
    h
    e
    e
    x
    p
    a
    n
    s
    i
    o
    n
    i
    s
    s
    u
    i
    t
    a
    b
    l
    e
    f
    o
    r
    a
    p
    a
    r
    t
    i
    c
    u
    l
    a
    r
    p
    u
    r
    p
    o
    s
    e
    ,
    o
    r
    t
    o
    p
    i
    c
    k
    t
    h
    e
    c
    o
    r
    r
    e
    c
    t
    e
    x
    p
    a
    n
    s
    i
    o
    n
    .
    
    """
    
    resource_type = "ValueSetExpansionParameter"
    
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
        a
        s
        a
        s
        s
        i
        g
        n
        e
        d
        b
        y
        t
        h
        e
        c
        l
        i
        e
        n
        t
        o
        r
        s
        e
        r
        v
        e
        r
        .
        Type `str`. """
        
        self.valueBoolean = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        t
        h
        e
        n
        a
        m
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
        .
        Type `bool`. """
        
        self.valueCode = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        t
        h
        e
        n
        a
        m
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
        .
        Type `str`. """
        
        self.valueDateTime = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        t
        h
        e
        n
        a
        m
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
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        t
        h
        e
        n
        a
        m
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
        .
        Type `float`. """
        
        self.valueInteger = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        t
        h
        e
        n
        a
        m
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
        .
        Type `int`. """
        
        self.valueString = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        t
        h
        e
        n
        a
        m
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
        .
        Type `str`. """
        
        self.valueUri = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        t
        h
        e
        n
        a
        m
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
        .
        Type `str`. """
        
        super(ValueSetExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


import sys
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
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
