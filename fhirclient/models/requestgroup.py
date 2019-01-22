#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class RequestGroup(domainresource.DomainResource):
    """ 
    A
    g
    r
    o
    u
    p
    o
    f
    r
    e
    l
    a
    t
    e
    d
    r
    e
    q
    u
    e
    s
    t
    s
    .
    
    
    A
    g
    r
    o
    u
    p
    o
    f
    r
    e
    l
    a
    t
    e
    d
    r
    e
    q
    u
    e
    s
    t
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
    c
    a
    p
    t
    u
    r
    e
    i
    n
    t
    e
    n
    d
    e
    d
    a
    c
    t
    i
    v
    i
    t
    i
    e
    s
    t
    h
    a
    t
    h
    a
    v
    e
    i
    n
    t
    e
    r
    -
    d
    e
    p
    e
    n
    d
    e
    n
    c
    i
    e
    s
    s
    u
    c
    h
    a
    s
    "
    g
    i
    v
    e
    t
    h
    i
    s
    m
    e
    d
    i
    c
    a
    t
    i
    o
    n
    a
    f
    t
    e
    r
    t
    h
    a
    t
    o
    n
    e
    "
    .
    
    """
    
    resource_type = "RequestGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        P
        r
        o
        p
        o
        s
        e
        d
        a
        c
        t
        i
        o
        n
        s
        ,
        i
        f
        a
        n
        y
        .
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        self.author = None
        """ 
        D
        e
        v
        i
        c
        e
        o
        r
        p
        r
        a
        c
        t
        i
        t
        i
        o
        n
        e
        r
        t
        h
        a
        t
        a
        u
        t
        h
        o
        r
        e
        d
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        g
        r
        o
        u
        p
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        g
        r
        o
        u
        p
        w
        a
        s
        a
        u
        t
        h
        o
        r
        e
        d
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ 
        F
        u
        l
        f
        i
        l
        l
        s
        p
        l
        a
        n
        ,
        p
        r
        o
        p
        o
        s
        a
        l
        ,
        o
        r
        o
        r
        d
        e
        r
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        W
        h
        a
        t
        '
        s
        b
        e
        i
        n
        g
        r
        e
        q
        u
        e
        s
        t
        e
        d
        /
        o
        r
        d
        e
        r
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ 
        C
        r
        e
        a
        t
        e
        d
        a
        s
        p
        a
        r
        t
        o
        f
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ 
        C
        o
        m
        p
        o
        s
        i
        t
        e
        r
        e
        q
        u
        e
        s
        t
        t
        h
        i
        s
        i
        s
        p
        a
        r
        t
        o
        f
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        B
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
        .
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        F
        H
        I
        R
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
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
        List of `str` items. """
        
        self.instantiatesUri = None
        """ 
        I
        n
        s
        t
        a
        n
        t
        i
        a
        t
        e
        s
        e
        x
        t
        e
        r
        n
        a
        l
        p
        r
        o
        t
        o
        c
        o
        l
        o
        r
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
        List of `str` items. """
        
        self.intent = None
        """ 
        p
        r
        o
        p
        o
        s
        a
        l
        |
        p
        l
        a
        n
        |
        o
        r
        d
        e
        r
        .
        Type `str`. """
        
        self.note = None
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
        n
        o
        t
        e
        s
        a
        b
        o
        u
        t
        t
        h
        e
        r
        e
        s
        p
        o
        n
        s
        e
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ 
        r
        o
        u
        t
        i
        n
        e
        |
        u
        r
        g
        e
        n
        t
        |
        a
        s
        a
        p
        |
        s
        t
        a
        t
        .
        Type `str`. """
        
        self.reasonCode = None
        """ 
        W
        h
        y
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        g
        r
        o
        u
        p
        i
        s
        n
        e
        e
        d
        e
        d
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        g
        r
        o
        u
        p
        i
        s
        n
        e
        e
        d
        e
        d
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.replaces = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        (
        s
        )
        r
        e
        p
        l
        a
        c
        e
        d
        b
        y
        t
        h
        i
        s
        r
        e
        q
        u
        e
        s
        t
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
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
        s
        u
        s
        p
        e
        n
        d
        e
        d
        |
        c
        a
        n
        c
        e
        l
        l
        e
        d
        |
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
        
        self.subject = None
        """ 
        W
        h
        o
        t
        h
        e
        r
        e
        q
        u
        e
        s
        t
        g
        r
        o
        u
        p
        i
        s
        a
        b
        o
        u
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        super(RequestGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class RequestGroupAction(backboneelement.BackboneElement):
    """ 
    P
    r
    o
    p
    o
    s
    e
    d
    a
    c
    t
    i
    o
    n
    s
    ,
    i
    f
    a
    n
    y
    .
    
    
    T
    h
    e
    a
    c
    t
    i
    o
    n
    s
    ,
    i
    f
    a
    n
    y
    ,
    p
    r
    o
    d
    u
    c
    e
    d
    b
    y
    t
    h
    e
    e
    v
    a
    l
    u
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
    a
    r
    t
    i
    f
    a
    c
    t
    .
    
    """
    
    resource_type = "RequestGroupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ 
        S
        u
        b
        a
        c
        t
        i
        o
        n
        .
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        self.cardinalityBehavior = None
        """ 
        s
        i
        n
        g
        l
        e
        |
        m
        u
        l
        t
        i
        p
        l
        e
        .
        Type `str`. """
        
        self.code = None
        """ 
        C
        o
        d
        e
        r
        e
        p
        r
        e
        s
        e
        n
        t
        i
        n
        g
        t
        h
        e
        m
        e
        a
        n
        i
        n
        g
        o
        f
        t
        h
        e
        a
        c
        t
        i
        o
        n
        o
        r
        s
        u
        b
        -
        a
        c
        t
        i
        o
        n
        s
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ 
        W
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
        t
        h
        e
        a
        c
        t
        i
        o
        n
        i
        s
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
        .
        List of `RequestGroupActionCondition` items (represented as `dict` in JSON). """
        
        self.description = None
        """ 
        S
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
        a
        c
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.documentation = None
        """ 
        S
        u
        p
        p
        o
        r
        t
        i
        n
        g
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
        f
        o
        r
        t
        h
        e
        i
        n
        t
        e
        n
        d
        e
        d
        p
        e
        r
        f
        o
        r
        m
        e
        r
        o
        f
        t
        h
        e
        a
        c
        t
        i
        o
        n
        .
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.groupingBehavior = None
        """ 
        v
        i
        s
        u
        a
        l
        -
        g
        r
        o
        u
        p
        |
        l
        o
        g
        i
        c
        a
        l
        -
        g
        r
        o
        u
        p
        |
        s
        e
        n
        t
        e
        n
        c
        e
        -
        g
        r
        o
        u
        p
        .
        Type `str`. """
        
        self.participant = None
        """ 
        W
        h
        o
        s
        h
        o
        u
        l
        d
        p
        e
        r
        f
        o
        r
        m
        t
        h
        e
        a
        c
        t
        i
        o
        n
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.precheckBehavior = None
        """ 
        y
        e
        s
        |
        n
        o
        .
        Type `str`. """
        
        self.prefix = None
        """ 
        U
        s
        e
        r
        -
        v
        i
        s
        i
        b
        l
        e
        p
        r
        e
        f
        i
        x
        f
        o
        r
        t
        h
        e
        a
        c
        t
        i
        o
        n
        (
        e
        .
        g
        .
        1
        .
        o
        r
        A
        .
        )
        .
        Type `str`. """
        
        self.priority = None
        """ 
        r
        o
        u
        t
        i
        n
        e
        |
        u
        r
        g
        e
        n
        t
        |
        a
        s
        a
        p
        |
        s
        t
        a
        t
        .
        Type `str`. """
        
        self.relatedAction = None
        """ 
        R
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
        t
        o
        a
        n
        o
        t
        h
        e
        r
        a
        c
        t
        i
        o
        n
        .
        List of `RequestGroupActionRelatedAction` items (represented as `dict` in JSON). """
        
        self.requiredBehavior = None
        """ 
        m
        u
        s
        t
        |
        c
        o
        u
        l
        d
        |
        m
        u
        s
        t
        -
        u
        n
        l
        e
        s
        s
        -
        d
        o
        c
        u
        m
        e
        n
        t
        e
        d
        .
        Type `str`. """
        
        self.resource = None
        """ 
        T
        h
        e
        t
        a
        r
        g
        e
        t
        o
        f
        t
        h
        e
        a
        c
        t
        i
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.selectionBehavior = None
        """ 
        a
        n
        y
        |
        a
        l
        l
        |
        a
        l
        l
        -
        o
        r
        -
        n
        o
        n
        e
        |
        e
        x
        a
        c
        t
        l
        y
        -
        o
        n
        e
        |
        a
        t
        -
        m
        o
        s
        t
        -
        o
        n
        e
        |
        o
        n
        e
        -
        o
        r
        -
        m
        o
        r
        e
        .
        Type `str`. """
        
        self.textEquivalent = None
        """ 
        S
        t
        a
        t
        i
        c
        t
        e
        x
        t
        e
        q
        u
        i
        v
        a
        l
        e
        n
        t
        o
        f
        t
        h
        e
        a
        c
        t
        i
        o
        n
        ,
        u
        s
        e
        d
        i
        f
        t
        h
        e
        d
        y
        n
        a
        m
        i
        c
        a
        s
        p
        e
        c
        t
        s
        c
        a
        n
        n
        o
        t
        b
        e
        i
        n
        t
        e
        r
        p
        r
        e
        t
        e
        d
        b
        y
        t
        h
        e
        r
        e
        c
        e
        i
        v
        i
        n
        g
        s
        y
        s
        t
        e
        m
        .
        Type `str`. """
        
        self.timingAge = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDuration = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingRange = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ 
        W
        h
        e
        n
        t
        h
        e
        a
        c
        t
        i
        o
        n
        s
        h
        o
        u
        l
        d
        t
        a
        k
        e
        p
        l
        a
        c
        e
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        """ 
        U
        s
        e
        r
        -
        v
        i
        s
        i
        b
        l
        e
        t
        i
        t
        l
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        c
        r
        e
        a
        t
        e
        |
        u
        p
        d
        a
        t
        e
        |
        r
        e
        m
        o
        v
        e
        |
        f
        i
        r
        e
        -
        e
        v
        e
        n
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(RequestGroupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class RequestGroupActionCondition(backboneelement.BackboneElement):
    """ 
    W
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
    t
    h
    e
    a
    c
    t
    i
    o
    n
    i
    s
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
    .
    
    
    A
    n
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
    t
    h
    a
    t
    d
    e
    s
    c
    r
    i
    b
    e
    s
    a
    p
    p
    l
    i
    c
    a
    b
    i
    l
    i
    t
    y
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
    s
    t
    a
    r
    t
    /
    s
    t
    o
    p
    c
    o
    n
    d
    i
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
    e
    a
    c
    t
    i
    o
    n
    .
    
    """
    
    resource_type = "RequestGroupActionCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ 
        B
        o
        o
        l
        e
        a
        n
        -
        v
        a
        l
        u
        e
        d
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
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.kind = None
        """ 
        a
        p
        p
        l
        i
        c
        a
        b
        i
        l
        i
        t
        y
        |
        s
        t
        a
        r
        t
        |
        s
        t
        o
        p
        .
        Type `str`. """
        
        super(RequestGroupActionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("kind", "kind", str, False, None, True),
        ])
        return js


class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """ 
    R
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
    t
    o
    a
    n
    o
    t
    h
    e
    r
    a
    c
    t
    i
    o
    n
    .
    
    
    A
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
    t
    o
    a
    n
    o
    t
    h
    e
    r
    a
    c
    t
    i
    o
    n
    s
    u
    c
    h
    a
    s
    "
    b
    e
    f
    o
    r
    e
    "
    o
    r
    "
    3
    0
    -
    6
    0
    m
    i
    n
    u
    t
    e
    s
    a
    f
    t
    e
    r
    s
    t
    a
    r
    t
    o
    f
    "
    .
    
    """
    
    resource_type = "RequestGroupActionRelatedAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionId = None
        """ 
        W
        h
        a
        t
        a
        c
        t
        i
        o
        n
        t
        h
        i
        s
        i
        s
        r
        e
        l
        a
        t
        e
        d
        t
        o
        .
        Type `str`. """
        
        self.offsetDuration = None
        """ 
        T
        i
        m
        e
        o
        f
        f
        s
        e
        t
        f
        o
        r
        t
        h
        e
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
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.offsetRange = None
        """ 
        T
        i
        m
        e
        o
        f
        f
        s
        e
        t
        f
        o
        r
        t
        h
        e
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
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ 
        b
        e
        f
        o
        r
        e
        -
        s
        t
        a
        r
        t
        |
        b
        e
        f
        o
        r
        e
        |
        b
        e
        f
        o
        r
        e
        -
        e
        n
        d
        |
        c
        o
        n
        c
        u
        r
        r
        e
        n
        t
        -
        w
        i
        t
        h
        -
        s
        t
        a
        r
        t
        |
        c
        o
        n
        c
        u
        r
        r
        e
        n
        t
        |
        c
        o
        n
        c
        u
        r
        r
        e
        n
        t
        -
        w
        i
        t
        h
        -
        e
        n
        d
        |
        a
        f
        t
        e
        r
        -
        s
        t
        a
        r
        t
        |
        a
        f
        t
        e
        r
        |
        a
        f
        t
        e
        r
        -
        e
        n
        d
        .
        Type `str`. """
        
        super(RequestGroupActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


import sys
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + '.age']
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
