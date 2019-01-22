#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Task) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class Task(domainresource.DomainResource):
    """ 
    A
    t
    a
    s
    k
    t
    o
    b
    e
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
    
    resource_type = "Task"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ 
        T
        a
        s
        k
        C
        r
        e
        a
        t
        i
        o
        n
        D
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ 
        R
        e
        q
        u
        e
        s
        t
        f
        u
        l
        f
        i
        l
        l
        e
        d
        b
        y
        t
        h
        i
        s
        t
        a
        s
        k
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.businessStatus = None
        """ 
        E
        .
        g
        .
        "
        S
        p
        e
        c
        i
        m
        e
        n
        c
        o
        l
        l
        e
        c
        t
        e
        d
        "
        ,
        "
        I
        V
        p
        r
        e
        p
        p
        e
        d
        "
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        T
        a
        s
        k
        T
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
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
        o
        f
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.encounter = None
        """ 
        H
        e
        a
        l
        t
        h
        c
        a
        r
        e
        e
        v
        e
        n
        t
        d
        u
        r
        i
        n
        g
        w
        h
        i
        c
        h
        t
        h
        i
        s
        t
        a
        s
        k
        o
        r
        i
        g
        i
        n
        a
        t
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.executionPeriod = None
        """ 
        S
        t
        a
        r
        t
        a
        n
        d
        e
        n
        d
        t
        i
        m
        e
        o
        f
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
        Type `Period` (represented as `dict` in JSON). """
        
        self.focus = None
        """ 
        W
        h
        a
        t
        t
        a
        s
        k
        i
        s
        a
        c
        t
        i
        n
        g
        o
        n
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.for_fhir = None
        """ 
        B
        e
        n
        e
        f
        i
        c
        i
        a
        r
        y
        o
        f
        t
        h
        e
        T
        a
        s
        k
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ 
        R
        e
        q
        u
        i
        s
        i
        t
        i
        o
        n
        o
        r
        g
        r
        o
        u
        p
        e
        r
        i
        d
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ 
        T
        a
        s
        k
        I
        n
        s
        t
        a
        n
        c
        e
        I
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
        
        self.input = None
        """ 
        I
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
        u
        s
        e
        d
        t
        o
        p
        e
        r
        f
        o
        r
        m
        t
        a
        s
        k
        .
        List of `TaskInput` items (represented as `dict` in JSON). """
        
        self.instantiatesCanonical = None
        """ 
        F
        o
        r
        m
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
        a
        s
        k
        .
        Type `str`. """
        
        self.instantiatesUri = None
        """ 
        F
        o
        r
        m
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
        a
        s
        k
        .
        Type `str`. """
        
        self.insurance = None
        """ 
        A
        s
        s
        o
        c
        i
        a
        t
        e
        d
        i
        n
        s
        u
        r
        a
        n
        c
        e
        c
        o
        v
        e
        r
        a
        g
        e
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.intent = None
        """ 
        u
        n
        k
        n
        o
        w
        n
        |
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
        |
        o
        r
        i
        g
        i
        n
        a
        l
        -
        o
        r
        d
        e
        r
        |
        r
        e
        f
        l
        e
        x
        -
        o
        r
        d
        e
        r
        |
        f
        i
        l
        l
        e
        r
        -
        o
        r
        d
        e
        r
        |
        i
        n
        s
        t
        a
        n
        c
        e
        -
        o
        r
        d
        e
        r
        |
        o
        p
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.lastModified = None
        """ 
        T
        a
        s
        k
        L
        a
        s
        t
        M
        o
        d
        i
        f
        i
        e
        d
        D
        a
        t
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.location = None
        """ 
        W
        h
        e
        r
        e
        t
        a
        s
        k
        o
        c
        c
        u
        r
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.note = None
        """ 
        C
        o
        m
        m
        e
        n
        t
        s
        m
        a
        d
        e
        a
        b
        o
        u
        t
        t
        h
        e
        t
        a
        s
        k
        .
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.output = None
        """ 
        I
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
        p
        r
        o
        d
        u
        c
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
        t
        a
        s
        k
        .
        List of `TaskOutput` items (represented as `dict` in JSON). """
        
        self.owner = None
        """ 
        R
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
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partOf = None
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
        t
        a
        s
        k
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.performerType = None
        """ 
        R
        e
        q
        u
        e
        s
        t
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
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        a
        s
        k
        i
        s
        n
        e
        e
        d
        e
        d
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ 
        W
        h
        y
        t
        a
        s
        k
        i
        s
        n
        e
        e
        d
        e
        d
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.relevantHistory = None
        """ 
        K
        e
        y
        e
        v
        e
        n
        t
        s
        i
        n
        h
        i
        s
        t
        o
        r
        y
        o
        f
        t
        h
        e
        T
        a
        s
        k
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.requester = None
        """ 
        W
        h
        o
        i
        s
        a
        s
        k
        i
        n
        g
        f
        o
        r
        t
        a
        s
        k
        t
        o
        b
        e
        d
        o
        n
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.restriction = None
        """ 
        C
        o
        n
        s
        t
        r
        a
        i
        n
        t
        s
        o
        n
        f
        u
        l
        f
        i
        l
        l
        m
        e
        n
        t
        t
        a
        s
        k
        s
        .
        Type `TaskRestriction` (represented as `dict` in JSON). """
        
        self.status = None
        """ 
        d
        r
        a
        f
        t
        |
        r
        e
        q
        u
        e
        s
        t
        e
        d
        |
        r
        e
        c
        e
        i
        v
        e
        d
        |
        a
        c
        c
        e
        p
        t
        e
        d
        |
        +
        .
        Type `str`. """
        
        self.statusReason = None
        """ 
        R
        e
        a
        s
        o
        n
        f
        o
        r
        c
        u
        r
        r
        e
        n
        t
        s
        t
        a
        t
        u
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Task, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("executionPeriod", "executionPeriod", period.Period, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("output", "output", TaskOutput, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("restriction", "restriction", TaskRestriction, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class TaskInput(backboneelement.BackboneElement):
    """ 
    I
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
    u
    s
    e
    d
    t
    o
    p
    e
    r
    f
    o
    r
    m
    t
    a
    s
    k
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
    t
    h
    a
    t
    m
    a
    y
    b
    e
    n
    e
    e
    d
    e
    d
    i
    n
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
    t
    a
    s
    k
    .
    
    """
    
    resource_type = "TaskInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ 
        L
        a
        b
        e
        l
        f
        o
        r
        t
        h
        e
        i
        n
        p
        u
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueBoolean = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `bool`. """
        
        self.valueCanonical = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueCode = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueCodeableConcept = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `float`. """
        
        self.valueDistance = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueIdentifier = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `int`. """
        
        self.valueMarkdown = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueMoney = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueParameterDefinition = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `int`. """
        
        self.valueQuantity = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueTime = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `int`. """
        
        self.valueUri = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueUrl = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        self.valueUsageContext = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
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
        u
        s
        e
        i
        n
        p
        e
        r
        f
        o
        r
        m
        i
        n
        g
        t
        h
        e
        t
        a
        s
        k
        .
        Type `str`. """
        
        super(TaskInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
        ])
        return js


class TaskOutput(backboneelement.BackboneElement):
    """ 
    I
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
    p
    r
    o
    d
    u
    c
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
    t
    a
    s
    k
    .
    
    
    O
    u
    t
    p
    u
    t
    s
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
    T
    a
    s
    k
    .
    
    """
    
    resource_type = "TaskOutput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ 
        L
        a
        b
        e
        l
        f
        o
        r
        o
        u
        t
        p
        u
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueBoolean = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `bool`. """
        
        self.valueCanonical = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueCode = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `float`. """
        
        self.valueDistance = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueIdentifier = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `int`. """
        
        self.valueMarkdown = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueMoney = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueParameterDefinition = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `int`. """
        
        self.valueQuantity = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueTime = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `int`. """
        
        self.valueUri = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueUrl = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        self.valueUsageContext = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        """ 
        R
        e
        s
        u
        l
        t
        o
        f
        o
        u
        t
        p
        u
        t
        .
        Type `str`. """
        
        super(TaskOutput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("valueUuid", "valueUuid", str, False, "value", True),
        ])
        return js


class TaskRestriction(backboneelement.BackboneElement):
    """ 
    C
    o
    n
    s
    t
    r
    a
    i
    n
    t
    s
    o
    n
    f
    u
    l
    f
    i
    l
    l
    m
    e
    n
    t
    t
    a
    s
    k
    s
    .
    
    
    I
    f
    t
    h
    e
    T
    a
    s
    k
    .
    f
    o
    c
    u
    s
    i
    s
    a
    r
    e
    q
    u
    e
    s
    t
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
    t
    h
    e
    t
    a
    s
    k
    i
    s
    s
    e
    e
    k
    i
    n
    g
    f
    u
    l
    f
    i
    l
    l
    m
    e
    n
    t
    (
    i
    .
    e
    .
    i
    s
    a
    s
    k
    i
    n
    g
    f
    o
    r
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
    t
    o
    b
    e
    a
    c
    t
    i
    o
    n
    e
    d
    )
    ,
    t
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
    i
    d
    e
    n
    t
    i
    f
    i
    e
    s
    a
    n
    y
    l
    i
    m
    i
    t
    a
    t
    i
    o
    n
    s
    o
    n
    w
    h
    a
    t
    p
    a
    r
    t
    s
    o
    f
    t
    h
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
    d
    r
    e
    q
    u
    e
    s
    t
    s
    h
    o
    u
    l
    d
    b
    e
    a
    c
    t
    i
    o
    n
    e
    d
    .
    
    """
    
    resource_type = "TaskRestriction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ 
        W
        h
        e
        n
        f
        u
        l
        f
        i
        l
        l
        m
        e
        n
        t
        s
        o
        u
        g
        h
        t
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ 
        F
        o
        r
        w
        h
        o
        m
        i
        s
        f
        u
        l
        f
        i
        l
        l
        m
        e
        n
        t
        s
        o
        u
        g
        h
        t
        ?
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.repetitions = None
        """ 
        H
        o
        w
        m
        a
        n
        y
        t
        i
        m
        e
        s
        t
        o
        r
        e
        p
        e
        a
        t
        .
        Type `int`. """
        
        super(TaskRestriction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskRestriction, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("repetitions", "repetitions", int, False, None, False),
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
