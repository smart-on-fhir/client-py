#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/TestReport) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class TestReport(domainresource.DomainResource):
    """ 
    D
    e
    s
    c
    r
    i
    b
    e
    s
    t
    h
    e
    r
    e
    s
    u
    l
    t
    s
    o
    f
    a
    T
    e
    s
    t
    S
    c
    r
    i
    p
    t
    e
    x
    e
    c
    u
    t
    i
    o
    n
    .
    
    
    A
    s
    u
    m
    m
    a
    r
    y
    o
    f
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
    r
    e
    s
    u
    l
    t
    s
    o
    f
    e
    x
    e
    c
    u
    t
    i
    n
    g
    a
    T
    e
    s
    t
    S
    c
    r
    i
    p
    t
    .
    
    """
    
    resource_type = "TestReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ 
        E
        x
        t
        e
        r
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
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.issued = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        T
        e
        s
        t
        S
        c
        r
        i
        p
        t
        w
        a
        s
        e
        x
        e
        c
        u
        t
        e
        d
        a
        n
        d
        t
        h
        i
        s
        T
        e
        s
        t
        R
        e
        p
        o
        r
        t
        w
        a
        s
        g
        e
        n
        e
        r
        a
        t
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ 
        I
        n
        f
        o
        r
        m
        a
        l
        n
        a
        m
        e
        o
        f
        t
        h
        e
        e
        x
        e
        c
        u
        t
        e
        d
        T
        e
        s
        t
        S
        c
        r
        i
        p
        t
        .
        Type `str`. """
        
        self.participant = None
        """ 
        A
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        i
        n
        t
        h
        e
        t
        e
        s
        t
        e
        x
        e
        c
        u
        t
        i
        o
        n
        ,
        e
        i
        t
        h
        e
        r
        t
        h
        e
        e
        x
        e
        c
        u
        t
        i
        o
        n
        e
        n
        g
        i
        n
        e
        ,
        a
        c
        l
        i
        e
        n
        t
        ,
        o
        r
        a
        s
        e
        r
        v
        e
        r
        .
        List of `TestReportParticipant` items (represented as `dict` in JSON). """
        
        self.result = None
        """ 
        p
        a
        s
        s
        |
        f
        a
        i
        l
        |
        p
        e
        n
        d
        i
        n
        g
        .
        Type `str`. """
        
        self.score = None
        """ 
        T
        h
        e
        f
        i
        n
        a
        l
        s
        c
        o
        r
        e
        (
        p
        e
        r
        c
        e
        n
        t
        a
        g
        e
        o
        f
        t
        e
        s
        t
        s
        p
        a
        s
        s
        e
        d
        )
        r
        e
        s
        u
        l
        t
        i
        n
        g
        f
        r
        o
        m
        t
        h
        e
        e
        x
        e
        c
        u
        t
        i
        o
        n
        o
        f
        t
        h
        e
        T
        e
        s
        t
        S
        c
        r
        i
        p
        t
        .
        Type `float`. """
        
        self.setup = None
        """ 
        T
        h
        e
        r
        e
        s
        u
        l
        t
        s
        o
        f
        t
        h
        e
        s
        e
        r
        i
        e
        s
        o
        f
        r
        e
        q
        u
        i
        r
        e
        d
        s
        e
        t
        u
        p
        o
        p
        e
        r
        a
        t
        i
        o
        n
        s
        b
        e
        f
        o
        r
        e
        t
        h
        e
        t
        e
        s
        t
        s
        w
        e
        r
        e
        e
        x
        e
        c
        u
        t
        e
        d
        .
        Type `TestReportSetup` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        c
        o
        m
        p
        l
        e
        t
        e
        d
        |
        i
        n
        -
        p
        r
        o
        g
        r
        e
        s
        s
        |
        w
        a
        i
        t
        i
        n
        g
        |
        s
        t
        o
        p
        p
        e
        d
        |
        e
        n
        t
        e
        r
        e
        d
        -
        i
        n
        -
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        self.teardown = None
        """ 
        T
        h
        e
        r
        e
        s
        u
        l
        t
        s
        o
        f
        r
        u
        n
        n
        i
        n
        g
        t
        h
        e
        s
        e
        r
        i
        e
        s
        o
        f
        r
        e
        q
        u
        i
        r
        e
        d
        c
        l
        e
        a
        n
        u
        p
        s
        t
        e
        p
        s
        .
        Type `TestReportTeardown` (represented as `dict` in JSON). """
        
        self.test = None
        """ 
        A
        t
        e
        s
        t
        e
        x
        e
        c
        u
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
        t
        e
        s
        t
        s
        c
        r
        i
        p
        t
        .
        List of `TestReportTest` items (represented as `dict` in JSON). """
        
        self.testScript = None
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
        t
        o
        t
        h
        e
        v
        e
        r
        s
        i
        o
        n
        -
        s
        p
        e
        c
        i
        f
        i
        c
        T
        e
        s
        t
        S
        c
        r
        i
        p
        t
        t
        h
        a
        t
        w
        a
        s
        e
        x
        e
        c
        u
        t
        e
        d
        t
        o
        p
        r
        o
        d
        u
        c
        e
        t
        h
        i
        s
        T
        e
        s
        t
        R
        e
        p
        o
        r
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.tester = None
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
        t
        e
        s
        t
        e
        r
        p
        r
        o
        d
        u
        c
        i
        n
        g
        t
        h
        i
        s
        r
        e
        p
        o
        r
        t
        (
        O
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
        
        super(TestReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReport, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("participant", "participant", TestReportParticipant, True, None, False),
            ("result", "result", str, False, None, True),
            ("score", "score", float, False, None, False),
            ("setup", "setup", TestReportSetup, False, None, False),
            ("status", "status", str, False, None, True),
            ("teardown", "teardown", TestReportTeardown, False, None, False),
            ("test", "test", TestReportTest, True, None, False),
            ("testScript", "testScript", fhirreference.FHIRReference, False, None, True),
            ("tester", "tester", str, False, None, False),
        ])
        return js


from . import backboneelement

class TestReportParticipant(backboneelement.BackboneElement):
    """ 
    A
    p
    a
    r
    t
    i
    c
    i
    p
    a
    n
    t
    i
    n
    t
    h
    e
    t
    e
    s
    t
    e
    x
    e
    c
    u
    t
    i
    o
    n
    ,
    e
    i
    t
    h
    e
    r
    t
    h
    e
    e
    x
    e
    c
    u
    t
    i
    o
    n
    e
    n
    g
    i
    n
    e
    ,
    a
    c
    l
    i
    e
    n
    t
    ,
    o
    r
    a
    s
    e
    r
    v
    e
    r
    .
    """
    
    resource_type = "TestReportParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.display = None
        """ 
        T
        h
        e
        d
        i
        s
        p
        l
        a
        y
        n
        a
        m
        e
        o
        f
        t
        h
        e
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        .
        Type `str`. """
        
        self.type = None
        """ 
        t
        e
        s
        t
        -
        e
        n
        g
        i
        n
        e
        |
        c
        l
        i
        e
        n
        t
        |
        s
        e
        r
        v
        e
        r
        .
        Type `str`. """
        
        self.uri = None
        """ 
        T
        h
        e
        u
        r
        i
        o
        f
        t
        h
        e
        p
        a
        r
        t
        i
        c
        i
        p
        a
        n
        t
        .
        A
        n
        a
        b
        s
        o
        l
        u
        t
        e
        U
        R
        L
        i
        s
        p
        r
        e
        f
        e
        r
        r
        e
        d
        .
        Type `str`. """
        
        super(TestReportParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportParticipant, self).elementProperties()
        js.extend([
            ("display", "display", str, False, None, False),
            ("type", "type", str, False, None, True),
            ("uri", "uri", str, False, None, True),
        ])
        return js


class TestReportSetup(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    r
    e
    s
    u
    l
    t
    s
    o
    f
    t
    h
    e
    s
    e
    r
    i
    e
    s
    o
    f
    r
    e
    q
    u
    i
    r
    e
    d
    s
    e
    t
    u
    p
    o
    p
    e
    r
    a
    t
    i
    o
    n
    s
    b
    e
    f
    o
    r
    e
    t
    h
    e
    t
    e
    s
    t
    s
    w
    e
    r
    e
    e
    x
    e
    c
    u
    t
    e
    d
    .
    """
    
    resource_type = "TestReportSetup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        A
        s
        e
        t
        u
        p
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
        s
        s
        e
        r
        t
        t
        h
        a
        t
        w
        a
        s
        e
        x
        e
        c
        u
        t
        e
        d
        .
        List of `TestReportSetupAction` items (represented as `dict` in JSON). """
        
        super(TestReportSetup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetup, self).elementProperties()
        js.extend([
            ("action", "action", TestReportSetupAction, True, None, True),
        ])
        return js


class TestReportSetupAction(backboneelement.BackboneElement):
    """ 
    A
    s
    e
    t
    u
    p
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
    s
    s
    e
    r
    t
    t
    h
    a
    t
    w
    a
    s
    e
    x
    e
    c
    u
    t
    e
    d
    .
    
    
    A
    c
    t
    i
    o
    n
    w
    o
    u
    l
    d
    c
    o
    n
    t
    a
    i
    n
    e
    i
    t
    h
    e
    r
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
    s
    s
    e
    r
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "TestReportSetupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ 
        T
        h
        e
        a
        s
        s
        e
        r
        t
        i
        o
        n
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation = None
        """ 
        T
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
        t
        o
        p
        e
        r
        f
        o
        r
        m
        .
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestReportSetupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
        ])
        return js


class TestReportSetupActionAssert(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    a
    s
    s
    e
    r
    t
    i
    o
    n
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    
    T
    h
    e
    r
    e
    s
    u
    l
    t
    s
    o
    f
    t
    h
    e
    a
    s
    s
    e
    r
    t
    i
    o
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
    o
    n
    t
    h
    e
    p
    r
    e
    v
    i
    o
    u
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
    s
    .
    
    """
    
    resource_type = "TestReportSetupActionAssert"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detail = None
        """ 
        A
        l
        i
        n
        k
        t
        o
        f
        u
        r
        t
        h
        e
        r
        d
        e
        t
        a
        i
        l
        s
        o
        n
        t
        h
        e
        r
        e
        s
        u
        l
        t
        .
        Type `str`. """
        
        self.message = None
        """ 
        A
        m
        e
        s
        s
        a
        g
        e
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        t
        h
        e
        r
        e
        s
        u
        l
        t
        .
        Type `str`. """
        
        self.result = None
        """ 
        p
        a
        s
        s
        |
        s
        k
        i
        p
        |
        f
        a
        i
        l
        |
        w
        a
        r
        n
        i
        n
        g
        |
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        super(TestReportSetupActionAssert, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupActionAssert, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("message", "message", str, False, None, False),
            ("result", "result", str, False, None, True),
        ])
        return js


class TestReportSetupActionOperation(backboneelement.BackboneElement):
    """ 
    T
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
    t
    o
    p
    e
    r
    f
    o
    r
    m
    .
    
    
    T
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
    
    resource_type = "TestReportSetupActionOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detail = None
        """ 
        A
        l
        i
        n
        k
        t
        o
        f
        u
        r
        t
        h
        e
        r
        d
        e
        t
        a
        i
        l
        s
        o
        n
        t
        h
        e
        r
        e
        s
        u
        l
        t
        .
        Type `str`. """
        
        self.message = None
        """ 
        A
        m
        e
        s
        s
        a
        g
        e
        a
        s
        s
        o
        c
        i
        a
        t
        e
        d
        w
        i
        t
        h
        t
        h
        e
        r
        e
        s
        u
        l
        t
        .
        Type `str`. """
        
        self.result = None
        """ 
        p
        a
        s
        s
        |
        s
        k
        i
        p
        |
        f
        a
        i
        l
        |
        w
        a
        r
        n
        i
        n
        g
        |
        e
        r
        r
        o
        r
        .
        Type `str`. """
        
        super(TestReportSetupActionOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportSetupActionOperation, self).elementProperties()
        js.extend([
            ("detail", "detail", str, False, None, False),
            ("message", "message", str, False, None, False),
            ("result", "result", str, False, None, True),
        ])
        return js


class TestReportTeardown(backboneelement.BackboneElement):
    """ 
    T
    h
    e
    r
    e
    s
    u
    l
    t
    s
    o
    f
    r
    u
    n
    n
    i
    n
    g
    t
    h
    e
    s
    e
    r
    i
    e
    s
    o
    f
    r
    e
    q
    u
    i
    r
    e
    d
    c
    l
    e
    a
    n
    u
    p
    s
    t
    e
    p
    s
    .
    
    
    T
    h
    e
    r
    e
    s
    u
    l
    t
    s
    o
    f
    t
    h
    e
    s
    e
    r
    i
    e
    s
    o
    f
    o
    p
    e
    r
    a
    t
    i
    o
    n
    s
    r
    e
    q
    u
    i
    r
    e
    d
    t
    o
    c
    l
    e
    a
    n
    u
    p
    a
    f
    t
    e
    r
    a
    l
    l
    t
    h
    e
    t
    e
    s
    t
    s
    w
    e
    r
    e
    e
    x
    e
    c
    u
    t
    e
    d
    (
    s
    u
    c
    c
    e
    s
    s
    f
    u
    l
    l
    y
    o
    r
    o
    t
    h
    e
    r
    w
    i
    s
    e
    )
    .
    
    """
    
    resource_type = "TestReportTeardown"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        O
        n
        e
        o
        r
        m
        o
        r
        e
        t
        e
        a
        r
        d
        o
        w
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
        s
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
        List of `TestReportTeardownAction` items (represented as `dict` in JSON). """
        
        super(TestReportTeardown, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTeardown, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTeardownAction, True, None, True),
        ])
        return js


class TestReportTeardownAction(backboneelement.BackboneElement):
    """ 
    O
    n
    e
    o
    r
    m
    o
    r
    e
    t
    e
    a
    r
    d
    o
    w
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
    s
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
    
    
    T
    h
    e
    t
    e
    a
    r
    d
    o
    w
    n
    a
    c
    t
    i
    o
    n
    w
    i
    l
    l
    o
    n
    l
    y
    c
    o
    n
    t
    a
    i
    n
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
    .
    
    """
    
    resource_type = "TestReportTeardownAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.operation = None
        """ 
        T
        h
        e
        t
        e
        a
        r
        d
        o
        w
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
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestReportTeardownAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTeardownAction, self).elementProperties()
        js.extend([
            ("operation", "operation", TestReportSetupActionOperation, False, None, True),
        ])
        return js


class TestReportTest(backboneelement.BackboneElement):
    """ 
    A
    t
    e
    s
    t
    e
    x
    e
    c
    u
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
    t
    e
    s
    t
    s
    c
    r
    i
    p
    t
    .
    """
    
    resource_type = "TestReportTest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        A
        t
        e
        s
        t
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
        s
        s
        e
        r
        t
        t
        h
        a
        t
        w
        a
        s
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
        List of `TestReportTestAction` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        r
        e
        p
        o
        r
        t
        i
        n
        g
        s
        h
        o
        r
        t
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
        t
        e
        s
        t
        .
        Type `str`. """
        
        self.name = None
        """ 
        T
        r
        a
        c
        k
        i
        n
        g
        /
        l
        o
        g
        g
        i
        n
        g
        n
        a
        m
        e
        o
        f
        t
        h
        i
        s
        t
        e
        s
        t
        .
        Type `str`. """
        
        super(TestReportTest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTest, self).elementProperties()
        js.extend([
            ("action", "action", TestReportTestAction, True, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


class TestReportTestAction(backboneelement.BackboneElement):
    """ 
    A
    t
    e
    s
    t
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
    s
    s
    e
    r
    t
    t
    h
    a
    t
    w
    a
    s
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
    
    
    A
    c
    t
    i
    o
    n
    w
    o
    u
    l
    d
    c
    o
    n
    t
    a
    i
    n
    e
    i
    t
    h
    e
    r
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
    s
    s
    e
    r
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "TestReportTestAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assert_fhir = None
        """ 
        T
        h
        e
        a
        s
        s
        e
        r
        t
        i
        o
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
        Type `TestReportSetupActionAssert` (represented as `dict` in JSON). """
        
        self.operation = None
        """ 
        T
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
        Type `TestReportSetupActionOperation` (represented as `dict` in JSON). """
        
        super(TestReportTestAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TestReportTestAction, self).elementProperties()
        js.extend([
            ("assert_fhir", "assert", TestReportSetupActionAssert, False, None, False),
            ("operation", "operation", TestReportSetupActionOperation, False, None, False),
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
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
