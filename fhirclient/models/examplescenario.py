#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ExampleScenario) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class ExampleScenario(domainresource.DomainResource):
    """ 
    E
    x
    a
    m
    p
    l
    e
    o
    f
    w
    o
    r
    k
    f
    l
    o
    w
    i
    n
    s
    t
    a
    n
    c
    e
    .
    """
    
    resource_type = "ExampleScenario"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ 
        A
        c
        t
        o
        r
        p
        a
        r
        t
        i
        c
        i
        p
        a
        t
        i
        n
        g
        i
        n
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
        .
        List of `ExampleScenarioActor` items (represented as `dict` in JSON). """
        
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
        e
        x
        a
        m
        p
        l
        e
        s
        c
        e
        n
        a
        r
        i
        o
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ 
        E
        a
        c
        h
        r
        e
        s
        o
        u
        r
        c
        e
        a
        n
        d
        e
        a
        c
        h
        v
        e
        r
        s
        i
        o
        n
        t
        h
        a
        t
        i
        s
        p
        r
        e
        s
        e
        n
        t
        i
        n
        t
        h
        e
        w
        o
        r
        k
        f
        l
        o
        w
        .
        List of `ExampleScenarioInstance` items (represented as `dict` in JSON). """
        
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
        e
        x
        a
        m
        p
        l
        e
        s
        c
        e
        n
        a
        r
        i
        o
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
        e
        x
        a
        m
        p
        l
        e
        s
        c
        e
        n
        a
        r
        i
        o
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
        
        self.process = None
        """ 
        E
        a
        c
        h
        m
        a
        j
        o
        r
        p
        r
        o
        c
        e
        s
        s
        -
        a
        g
        r
        o
        u
        p
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
        .
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
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
        T
        h
        e
        p
        u
        r
        p
        o
        s
        e
        o
        f
        t
        h
        e
        e
        x
        a
        m
        p
        l
        e
        ,
        e
        .
        g
        .
        t
        o
        i
        l
        l
        u
        s
        t
        r
        a
        t
        e
        a
        s
        c
        e
        n
        a
        r
        i
        o
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
        e
        x
        a
        m
        p
        l
        e
        s
        c
        e
        n
        a
        r
        i
        o
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
        e
        x
        a
        m
        p
        l
        e
        s
        c
        e
        n
        a
        r
        i
        o
        .
        Type `str`. """
        
        self.workflow = None
        """ 
        A
        n
        o
        t
        h
        e
        r
        n
        e
        s
        t
        e
        d
        w
        o
        r
        k
        f
        l
        o
        w
        .
        List of `str` items. """
        
        super(ExampleScenario, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenario, self).elementProperties()
        js.extend([
            ("actor", "actor", ExampleScenarioActor, True, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instance", "instance", ExampleScenarioInstance, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("name", "name", str, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
            ("workflow", "workflow", str, True, None, False),
        ])
        return js


from . import backboneelement

class ExampleScenarioActor(backboneelement.BackboneElement):
    """ 
    A
    c
    t
    o
    r
    p
    a
    r
    t
    i
    c
    i
    p
    a
    t
    i
    n
    g
    i
    n
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
    .
    """
    
    resource_type = "ExampleScenarioActor"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actorId = None
        """ 
        I
        D
        o
        r
        a
        c
        r
        o
        n
        y
        m
        o
        f
        t
        h
        e
        a
        c
        t
        o
        r
        .
        Type `str`. """
        
        self.description = None
        """ 
        T
        h
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
        a
        c
        t
        o
        r
        .
        Type `str`. """
        
        self.name = None
        """ 
        T
        h
        e
        n
        a
        m
        e
        o
        f
        t
        h
        e
        a
        c
        t
        o
        r
        a
        s
        s
        h
        o
        w
        n
        i
        n
        t
        h
        e
        p
        a
        g
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        p
        e
        r
        s
        o
        n
        |
        e
        n
        t
        i
        t
        y
        .
        Type `str`. """
        
        super(ExampleScenarioActor, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioActor, self).elementProperties()
        js.extend([
            ("actorId", "actorId", str, False, None, True),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class ExampleScenarioInstance(backboneelement.BackboneElement):
    """ 
    E
    a
    c
    h
    r
    e
    s
    o
    u
    r
    c
    e
    a
    n
    d
    e
    a
    c
    h
    v
    e
    r
    s
    i
    o
    n
    t
    h
    a
    t
    i
    s
    p
    r
    e
    s
    e
    n
    t
    i
    n
    t
    h
    e
    w
    o
    r
    k
    f
    l
    o
    w
    .
    """
    
    resource_type = "ExampleScenarioInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.containedInstance = None
        """ 
        R
        e
        s
        o
        u
        r
        c
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
        e
        i
        n
        s
        t
        a
        n
        c
        e
        .
        List of `ExampleScenarioInstanceContainedInstance` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        H
        u
        m
        a
        n
        -
        f
        r
        i
        e
        n
        d
        l
        y
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
        .
        Type `str`. """
        
        self.name = None
        """ 
        A
        s
        h
        o
        r
        t
        n
        a
        m
        e
        f
        o
        r
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
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.resourceId = None
        """ 
        T
        h
        e
        i
        d
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
        i
        n
        g
        .
        Type `str`. """
        
        self.resourceType = None
        """ 
        T
        h
        e
        t
        y
        p
        e
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
        .
        Type `str`. """
        
        self.version = None
        """ 
        A
        s
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
        r
        e
        s
        o
        u
        r
        c
        e
        .
        List of `ExampleScenarioInstanceVersion` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstance, self).elementProperties()
        js.extend([
            ("containedInstance", "containedInstance", ExampleScenarioInstanceContainedInstance, True, None, False),
            ("description", "description", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("resourceId", "resourceId", str, False, None, True),
            ("resourceType", "resourceType", str, False, None, True),
            ("version", "version", ExampleScenarioInstanceVersion, True, None, False),
        ])
        return js


class ExampleScenarioInstanceContainedInstance(backboneelement.BackboneElement):
    """ 
    R
    e
    s
    o
    u
    r
    c
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
    e
    i
    n
    s
    t
    a
    n
    c
    e
    .
    
    
    R
    e
    s
    o
    u
    r
    c
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
    e
    i
    n
    s
    t
    a
    n
    c
    e
    (
    e
    .
    g
    .
    t
    h
    e
    o
    b
    s
    e
    r
    v
    a
    t
    i
    o
    n
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
    a
    b
    u
    n
    d
    l
    e
    )
    .
    
    """
    
    resource_type = "ExampleScenarioInstanceContainedInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resourceId = None
        """ 
        E
        a
        c
        h
        r
        e
        s
        o
        u
        r
        c
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
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        self.versionId = None
        """ 
        A
        s
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
        a
        r
        e
        s
        o
        u
        r
        c
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
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `str`. """
        
        super(ExampleScenarioInstanceContainedInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceContainedInstance, self).elementProperties()
        js.extend([
            ("resourceId", "resourceId", str, False, None, True),
            ("versionId", "versionId", str, False, None, False),
        ])
        return js


class ExampleScenarioInstanceVersion(backboneelement.BackboneElement):
    """ 
    A
    s
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
    
    resource_type = "ExampleScenarioInstanceVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        T
        h
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
        r
        e
        s
        o
        u
        r
        c
        e
        v
        e
        r
        s
        i
        o
        n
        .
        Type `str`. """
        
        self.versionId = None
        """ 
        T
        h
        e
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
        o
        f
        a
        s
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
        a
        r
        e
        s
        o
        u
        r
        c
        e
        .
        Type `str`. """
        
        super(ExampleScenarioInstanceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioInstanceVersion, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("versionId", "versionId", str, False, None, True),
        ])
        return js


class ExampleScenarioProcess(backboneelement.BackboneElement):
    """ 
    E
    a
    c
    h
    m
    a
    j
    o
    r
    p
    r
    o
    c
    e
    s
    s
    -
    a
    g
    r
    o
    u
    p
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
    .
    """
    
    resource_type = "ExampleScenarioProcess"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        A
        l
        o
        n
        g
        e
        r
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
        g
        r
        o
        u
        p
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
        .
        Type `str`. """
        
        self.postConditions = None
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
        f
        i
        n
        a
        l
        s
        t
        a
        t
        u
        s
        a
        f
        t
        e
        r
        t
        h
        e
        p
        r
        o
        c
        e
        s
        s
        e
        n
        d
        s
        .
        Type `str`. """
        
        self.preConditions = None
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
        i
        n
        i
        t
        i
        a
        l
        s
        t
        a
        t
        u
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
        p
        r
        o
        c
        e
        s
        s
        s
        t
        a
        r
        t
        s
        .
        Type `str`. """
        
        self.step = None
        """ 
        E
        a
        c
        h
        s
        t
        e
        p
        o
        f
        t
        h
        e
        p
        r
        o
        c
        e
        s
        s
        .
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        T
        h
        e
        d
        i
        a
        g
        r
        a
        m
        t
        i
        t
        l
        e
        o
        f
        t
        h
        e
        g
        r
        o
        u
        p
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
        .
        Type `str`. """
        
        super(ExampleScenarioProcess, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcess, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("postConditions", "postConditions", str, False, None, False),
            ("preConditions", "preConditions", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
        ])
        return js


class ExampleScenarioProcessStep(backboneelement.BackboneElement):
    """ 
    E
    a
    c
    h
    s
    t
    e
    p
    o
    f
    t
    h
    e
    p
    r
    o
    c
    e
    s
    s
    .
    """
    
    resource_type = "ExampleScenarioProcessStep"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alternative = None
        """ 
        A
        l
        t
        e
        r
        n
        a
        t
        e
        n
        o
        n
        -
        t
        y
        p
        i
        c
        a
        l
        s
        t
        e
        p
        a
        c
        t
        i
        o
        n
        .
        List of `ExampleScenarioProcessStepAlternative` items (represented as `dict` in JSON). """
        
        self.operation = None
        """ 
        E
        a
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
        o
        r
        a
        c
        t
        i
        o
        n
        .
        Type `ExampleScenarioProcessStepOperation` (represented as `dict` in JSON). """
        
        self.pause = None
        """ 
        I
        f
        t
        h
        e
        r
        e
        i
        s
        a
        p
        a
        u
        s
        e
        i
        n
        t
        h
        e
        f
        l
        o
        w
        .
        Type `bool`. """
        
        self.process = None
        """ 
        N
        e
        s
        t
        e
        d
        p
        r
        o
        c
        e
        s
        s
        .
        List of `ExampleScenarioProcess` items (represented as `dict` in JSON). """
        
        super(ExampleScenarioProcessStep, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStep, self).elementProperties()
        js.extend([
            ("alternative", "alternative", ExampleScenarioProcessStepAlternative, True, None, False),
            ("operation", "operation", ExampleScenarioProcessStepOperation, False, None, False),
            ("pause", "pause", bool, False, None, False),
            ("process", "process", ExampleScenarioProcess, True, None, False),
        ])
        return js


class ExampleScenarioProcessStepAlternative(backboneelement.BackboneElement):
    """ 
    A
    l
    t
    e
    r
    n
    a
    t
    e
    n
    o
    n
    -
    t
    y
    p
    i
    c
    a
    l
    s
    t
    e
    p
    a
    c
    t
    i
    o
    n
    .
    
    
    I
    n
    d
    i
    c
    a
    t
    e
    s
    a
    n
    a
    l
    t
    e
    r
    n
    a
    t
    i
    v
    e
    s
    t
    e
    p
    t
    h
    a
    t
    c
    a
    n
    b
    e
    t
    a
    k
    e
    n
    i
    n
    s
    t
    e
    a
    d
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
    s
    o
    n
    t
    h
    e
    b
    a
    s
    e
    s
    t
    e
    p
    i
    n
    e
    x
    c
    e
    p
    t
    i
    o
    n
    a
    l
    /
    a
    t
    y
    p
    i
    c
    a
    l
    c
    i
    r
    c
    u
    m
    s
    t
    a
    n
    c
    e
    s
    .
    
    """
    
    resource_type = "ExampleScenarioProcessStepAlternative"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        A
        h
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
        e
        a
        c
        h
        o
        p
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.step = None
        """ 
        W
        h
        a
        t
        h
        a
        p
        p
        e
        n
        s
        i
        n
        e
        a
        c
        h
        a
        l
        t
        e
        r
        n
        a
        t
        i
        v
        e
        o
        p
        t
        i
        o
        n
        .
        List of `ExampleScenarioProcessStep` items (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        L
        a
        b
        e
        l
        f
        o
        r
        a
        l
        t
        e
        r
        n
        a
        t
        i
        v
        e
        .
        Type `str`. """
        
        super(ExampleScenarioProcessStepAlternative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepAlternative, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("step", "step", ExampleScenarioProcessStep, True, None, False),
            ("title", "title", str, False, None, True),
        ])
        return js


class ExampleScenarioProcessStepOperation(backboneelement.BackboneElement):
    """ 
    E
    a
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
    o
    r
    a
    c
    t
    i
    o
    n
    .
    """
    
    resource_type = "ExampleScenarioProcessStepOperation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        A
        c
        o
        m
        m
        e
        n
        t
        t
        o
        b
        e
        i
        n
        s
        e
        r
        t
        e
        d
        i
        n
        t
        h
        e
        d
        i
        a
        g
        r
        a
        m
        .
        Type `str`. """
        
        self.initiator = None
        """ 
        W
        h
        o
        s
        t
        a
        r
        t
        s
        t
        h
        e
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.initiatorActive = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        e
        i
        n
        i
        t
        i
        a
        t
        o
        r
        i
        s
        d
        e
        a
        c
        t
        i
        v
        a
        t
        e
        d
        r
        i
        g
        h
        t
        a
        f
        t
        e
        r
        t
        h
        e
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        .
        Type `bool`. """
        
        self.name = None
        """ 
        T
        h
        e
        h
        u
        m
        a
        n
        -
        f
        r
        i
        e
        n
        d
        l
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
        .
        Type `str`. """
        
        self.number = None
        """ 
        T
        h
        e
        s
        e
        q
        u
        e
        n
        t
        i
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
        t
        h
        e
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
        .
        Type `str`. """
        
        self.receiver = None
        """ 
        W
        h
        o
        r
        e
        c
        e
        i
        v
        e
        s
        t
        h
        e
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.receiverActive = None
        """ 
        W
        h
        e
        t
        h
        e
        r
        t
        h
        e
        r
        e
        c
        e
        i
        v
        e
        r
        i
        s
        d
        e
        a
        c
        t
        i
        v
        a
        t
        e
        d
        r
        i
        g
        h
        t
        a
        f
        t
        e
        r
        t
        h
        e
        t
        r
        a
        n
        s
        a
        c
        t
        i
        o
        n
        .
        Type `bool`. """
        
        self.request = None
        """ 
        E
        a
        c
        h
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
        u
        s
        e
        d
        b
        y
        t
        h
        e
        i
        n
        i
        t
        i
        a
        t
        o
        r
        .
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        self.response = None
        """ 
        E
        a
        c
        h
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
        u
        s
        e
        d
        b
        y
        t
        h
        e
        r
        e
        s
        p
        o
        n
        d
        e
        r
        .
        Type `ExampleScenarioInstanceContainedInstance` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        h
        e
        t
        y
        p
        e
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
        -
        C
        R
        U
        D
        .
        Type `str`. """
        
        super(ExampleScenarioProcessStepOperation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ExampleScenarioProcessStepOperation, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("initiator", "initiator", str, False, None, False),
            ("initiatorActive", "initiatorActive", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("number", "number", str, False, None, True),
            ("receiver", "receiver", str, False, None, False),
            ("receiverActive", "receiverActive", bool, False, None, False),
            ("request", "request", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("response", "response", ExampleScenarioInstanceContainedInstance, False, None, False),
            ("type", "type", str, False, None, False),
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + '.usagecontext']
