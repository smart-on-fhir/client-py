#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2019-01-22.
#  2019, SMART Health IT.


from . import backboneelement

class ElementDefinition(backboneelement.BackboneElement):
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
    e
    l
    e
    m
    e
    n
    t
    i
    n
    a
    r
    e
    s
    o
    u
    r
    c
    e
    o
    r
    e
    x
    t
    e
    n
    s
    i
    o
    n
    .
    
    
    C
    a
    p
    t
    u
    r
    e
    s
    c
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
    e
    a
    c
    h
    e
    l
    e
    m
    e
    n
    t
    w
    i
    t
    h
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
    ,
    p
    r
    o
    f
    i
    l
    e
    ,
    o
    r
    e
    x
    t
    e
    n
    s
    i
    o
    n
    .
    
    """
    
    resource_type = "ElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        """ 
        O
        t
        h
        e
        r
        n
        a
        m
        e
        s
        .
        List of `str` items. """
        
        self.base = None
        """ 
        B
        a
        s
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
        t
        o
        o
        l
        s
        .
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """
        
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
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """
        
        self.code = None
        """ 
        C
        o
        r
        r
        e
        s
        p
        o
        n
        d
        i
        n
        g
        c
        o
        d
        e
        s
        i
        n
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
        List of `Coding` items (represented as `dict` in JSON). """
        
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
        a
        b
        o
        u
        t
        t
        h
        e
        u
        s
        e
        o
        f
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
        .
        Type `str`. """
        
        self.condition = None
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
        i
        n
        v
        a
        r
        i
        a
        n
        t
        a
        b
        o
        u
        t
        p
        r
        e
        s
        e
        n
        c
        e
        .
        List of `str` items. """
        
        self.constraint = None
        """ 
        C
        o
        n
        d
        i
        t
        i
        o
        n
        t
        h
        a
        t
        m
        u
        s
        t
        e
        v
        a
        l
        u
        a
        t
        e
        t
        o
        t
        r
        u
        e
        .
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """
        
        self.contentReference = None
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
        c
        o
        n
        t
        e
        n
        t
        f
        o
        r
        t
        h
        e
        e
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.defaultValueAddress = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAge = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueBoolean = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `bool`. """
        
        self.defaultValueCanonical = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueCode = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueCodeableConcept = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactDetail = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueContributor = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.defaultValueCount = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.defaultValueDataRequirement = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.defaultValueDate = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDateTime = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDecimal = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `float`. """
        
        self.defaultValueDistance = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.defaultValueDosage = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.defaultValueDuration = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.defaultValueExpression = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.defaultValueHumanName = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueId = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueIdentifier = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueInteger = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `int`. """
        
        self.defaultValueMarkdown = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueMoney = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.defaultValueOid = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueParameterDefinition = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.defaultValuePeriod = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValuePositiveInt = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `int`. """
        
        self.defaultValueQuantity = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueRelatedArtifact = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueString = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueTime = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueTiming = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueTriggerDefinition = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.defaultValueUnsignedInt = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `int`. """
        
        self.defaultValueUri = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueUrl = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.defaultValueUsageContext = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
        i
        n
        s
        t
        a
        n
        c
        e
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.defaultValueUuid = None
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
        v
        a
        l
        u
        e
        i
        f
        m
        i
        s
        s
        i
        n
        g
        f
        r
        o
        m
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
        
        self.definition = None
        """ 
        F
        u
        l
        l
        f
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
        a
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
        t
        e
        x
        t
        .
        Type `str`. """
        
        self.example = None
        """ 
        E
        x
        a
        m
        p
        l
        e
        v
        a
        l
        u
        e
        (
        a
        s
        d
        e
        f
        i
        n
        e
        d
        f
        o
        r
        t
        y
        p
        e
        )
        .
        List of `ElementDefinitionExample` items (represented as `dict` in JSON). """
        
        self.fixedAddress = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.fixedAge = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.fixedAnnotation = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.fixedAttachment = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.fixedBase64Binary = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedBoolean = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `bool`. """
        
        self.fixedCanonical = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedCode = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedCodeableConcept = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fixedCoding = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.fixedContactDetail = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.fixedContactPoint = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.fixedContributor = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.fixedCount = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.fixedDataRequirement = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.fixedDate = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedDateTime = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedDecimal = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `float`. """
        
        self.fixedDistance = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.fixedDosage = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.fixedDuration = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.fixedExpression = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.fixedHumanName = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.fixedId = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedIdentifier = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.fixedInstant = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedInteger = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `int`. """
        
        self.fixedMarkdown = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedMoney = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.fixedOid = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedParameterDefinition = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.fixedPeriod = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.fixedPositiveInt = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `int`. """
        
        self.fixedQuantity = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.fixedRange = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.fixedRatio = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.fixedReference = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fixedRelatedArtifact = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.fixedSampledData = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.fixedSignature = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.fixedString = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedTime = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedTiming = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.fixedTriggerDefinition = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.fixedUnsignedInt = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `int`. """
        
        self.fixedUri = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedUrl = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.fixedUsageContext = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.fixedUuid = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        b
        e
        e
        x
        a
        c
        t
        l
        y
        t
        h
        i
        s
        .
        Type `str`. """
        
        self.isModifier = None
        """ 
        I
        f
        t
        h
        i
        s
        m
        o
        d
        i
        f
        i
        e
        s
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
        o
        t
        h
        e
        r
        e
        l
        e
        m
        e
        n
        t
        s
        .
        Type `bool`. """
        
        self.isModifierReason = None
        """ 
        R
        e
        a
        s
        o
        n
        t
        h
        a
        t
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
        s
        m
        a
        r
        k
        e
        d
        a
        s
        a
        m
        o
        d
        i
        f
        i
        e
        r
        .
        Type `str`. """
        
        self.isSummary = None
        """ 
        I
        n
        c
        l
        u
        d
        e
        w
        h
        e
        n
        _
        s
        u
        m
        m
        a
        r
        y
        =
        t
        r
        u
        e
        ?
        .
        Type `bool`. """
        
        self.label = None
        """ 
        N
        a
        m
        e
        f
        o
        r
        e
        l
        e
        m
        e
        n
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
        w
        i
        t
        h
        o
        r
        p
        r
        o
        m
        p
        t
        f
        o
        r
        e
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.mapping = None
        """ 
        M
        a
        p
        e
        l
        e
        m
        e
        n
        t
        t
        o
        a
        n
        o
        t
        h
        e
        r
        s
        e
        t
        o
        f
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
        .
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """
        
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
        
        self.maxLength = None
        """ 
        M
        a
        x
        l
        e
        n
        g
        t
        h
        f
        o
        r
        s
        t
        r
        i
        n
        g
        s
        .
        Type `int`. """
        
        self.maxValueDate = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueDateTime = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueDecimal = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `float`. """
        
        self.maxValueInstant = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueInteger = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.maxValuePositiveInt = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.maxValueQuantity = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxValueTime = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueUnsignedInt = None
        """ 
        M
        a
        x
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.meaningWhenMissing = None
        """ 
        I
        m
        p
        l
        i
        c
        i
        t
        m
        e
        a
        n
        i
        n
        g
        w
        h
        e
        n
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
        s
        m
        i
        s
        s
        i
        n
        g
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
        
        self.minValueDate = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueDateTime = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueDecimal = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `float`. """
        
        self.minValueInstant = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueInteger = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.minValuePositiveInt = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.minValueQuantity = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minValueTime = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueUnsignedInt = None
        """ 
        M
        i
        n
        i
        m
        u
        m
        A
        l
        l
        o
        w
        e
        d
        V
        a
        l
        u
        e
        (
        f
        o
        r
        s
        o
        m
        e
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.mustSupport = None
        """ 
        I
        f
        t
        h
        e
        e
        l
        e
        m
        e
        n
        t
        m
        u
        s
        t
        b
        e
        s
        u
        p
        p
        o
        r
        t
        e
        d
        .
        Type `bool`. """
        
        self.orderMeaning = None
        """ 
        W
        h
        a
        t
        t
        h
        e
        o
        r
        d
        e
        r
        o
        f
        t
        h
        e
        e
        l
        e
        m
        e
        n
        t
        s
        m
        e
        a
        n
        s
        .
        Type `str`. """
        
        self.path = None
        """ 
        P
        a
        t
        h
        o
        f
        t
        h
        e
        e
        l
        e
        m
        e
        n
        t
        i
        n
        t
        h
        e
        h
        i
        e
        r
        a
        r
        c
        h
        y
        o
        f
        e
        l
        e
        m
        e
        n
        t
        s
        .
        Type `str`. """
        
        self.patternAddress = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.patternAge = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.patternAnnotation = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.patternAttachment = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.patternBase64Binary = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternBoolean = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `bool`. """
        
        self.patternCanonical = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternCode = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternCodeableConcept = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patternCoding = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patternContactDetail = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.patternContactPoint = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.patternContributor = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.patternCount = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.patternDataRequirement = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.patternDate = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternDateTime = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternDecimal = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `float`. """
        
        self.patternDistance = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.patternDosage = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.patternDuration = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.patternExpression = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.patternHumanName = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patternId = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternIdentifier = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patternInstant = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternInteger = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `int`. """
        
        self.patternMarkdown = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternMoney = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.patternOid = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternParameterDefinition = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.patternPeriod = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.patternPositiveInt = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `int`. """
        
        self.patternQuantity = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.patternRange = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.patternRatio = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.patternReference = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patternRelatedArtifact = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.patternSampledData = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.patternSignature = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.patternString = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternTime = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternTiming = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.patternTriggerDefinition = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.patternUnsignedInt = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `int`. """
        
        self.patternUri = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternUrl = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.patternUsageContext = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.patternUuid = None
        """ 
        V
        a
        l
        u
        e
        m
        u
        s
        t
        h
        a
        v
        e
        a
        t
        l
        e
        a
        s
        t
        t
        h
        e
        s
        e
        p
        r
        o
        p
        e
        r
        t
        y
        v
        a
        l
        u
        e
        s
        .
        Type `str`. """
        
        self.representation = None
        """ 
        x
        m
        l
        A
        t
        t
        r
        |
        x
        m
        l
        T
        e
        x
        t
        |
        t
        y
        p
        e
        A
        t
        t
        r
        |
        c
        d
        a
        T
        e
        x
        t
        |
        x
        h
        t
        m
        l
        .
        List of `str` items. """
        
        self.requirements = None
        """ 
        W
        h
        y
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
        h
        a
        s
        b
        e
        e
        n
        c
        r
        e
        a
        t
        e
        d
        .
        Type `str`. """
        
        self.short = None
        """ 
        C
        o
        n
        c
        i
        s
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
        f
        o
        r
        s
        p
        a
        c
        e
        -
        c
        o
        n
        s
        t
        r
        a
        i
        n
        e
        d
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
        .
        Type `str`. """
        
        self.sliceIsConstraining = None
        """ 
        I
        f
        t
        h
        i
        s
        s
        l
        i
        c
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
        c
        o
        n
        s
        t
        r
        a
        i
        n
        s
        a
        n
        i
        n
        h
        e
        r
        i
        t
        e
        d
        s
        l
        i
        c
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
        (
        o
        r
        n
        o
        t
        )
        .
        Type `bool`. """
        
        self.sliceName = None
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
        e
        l
        e
        m
        e
        n
        t
        (
        i
        n
        a
        s
        e
        t
        o
        f
        s
        l
        i
        c
        e
        s
        )
        .
        Type `str`. """
        
        self.slicing = None
        """ 
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
        i
        s
        s
        l
        i
        c
        e
        d
        -
        s
        l
        i
        c
        e
        s
        f
        o
        l
        l
        o
        w
        .
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        D
        a
        t
        a
        t
        y
        p
        e
        a
        n
        d
        P
        r
        o
        f
        i
        l
        e
        f
        o
        r
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
        .
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """
        
        super(ElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("contentReference", "contentReference", str, False, None, False),
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
            ("definition", "definition", str, False, None, False),
            ("example", "example", ElementDefinitionExample, True, None, False),
            ("fixedAddress", "fixedAddress", address.Address, False, "fixed", False),
            ("fixedAge", "fixedAge", age.Age, False, "fixed", False),
            ("fixedAnnotation", "fixedAnnotation", annotation.Annotation, False, "fixed", False),
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False, "fixed", False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("fixedCanonical", "fixedCanonical", str, False, "fixed", False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False, "fixed", False),
            ("fixedCoding", "fixedCoding", coding.Coding, False, "fixed", False),
            ("fixedContactDetail", "fixedContactDetail", contactdetail.ContactDetail, False, "fixed", False),
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False, "fixed", False),
            ("fixedContributor", "fixedContributor", contributor.Contributor, False, "fixed", False),
            ("fixedCount", "fixedCount", count.Count, False, "fixed", False),
            ("fixedDataRequirement", "fixedDataRequirement", datarequirement.DataRequirement, False, "fixed", False),
            ("fixedDate", "fixedDate", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedDateTime", "fixedDateTime", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("fixedDistance", "fixedDistance", distance.Distance, False, "fixed", False),
            ("fixedDosage", "fixedDosage", dosage.Dosage, False, "fixed", False),
            ("fixedDuration", "fixedDuration", duration.Duration, False, "fixed", False),
            ("fixedExpression", "fixedExpression", expression.Expression, False, "fixed", False),
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False, "fixed", False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False, "fixed", False),
            ("fixedInstant", "fixedInstant", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("fixedMoney", "fixedMoney", money.Money, False, "fixed", False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("fixedParameterDefinition", "fixedParameterDefinition", parameterdefinition.ParameterDefinition, False, "fixed", False),
            ("fixedPeriod", "fixedPeriod", period.Period, False, "fixed", False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False, "fixed", False),
            ("fixedRange", "fixedRange", range.Range, False, "fixed", False),
            ("fixedRatio", "fixedRatio", ratio.Ratio, False, "fixed", False),
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False, "fixed", False),
            ("fixedRelatedArtifact", "fixedRelatedArtifact", relatedartifact.RelatedArtifact, False, "fixed", False),
            ("fixedSampledData", "fixedSampledData", sampleddata.SampledData, False, "fixed", False),
            ("fixedSignature", "fixedSignature", signature.Signature, False, "fixed", False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("fixedTime", "fixedTime", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedTiming", "fixedTiming", timing.Timing, False, "fixed", False),
            ("fixedTriggerDefinition", "fixedTriggerDefinition", triggerdefinition.TriggerDefinition, False, "fixed", False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("fixedUrl", "fixedUrl", str, False, "fixed", False),
            ("fixedUsageContext", "fixedUsageContext", usagecontext.UsageContext, False, "fixed", False),
            ("fixedUuid", "fixedUuid", str, False, "fixed", False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("isModifierReason", "isModifierReason", str, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("label", "label", str, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
            ("max", "max", str, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("maxValueDate", "maxValueDate", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueDateTime", "maxValueDateTime", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("maxValueInstant", "maxValueInstant", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("maxValueQuantity", "maxValueQuantity", quantity.Quantity, False, "maxValue", False),
            ("maxValueTime", "maxValueTime", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("minValueDate", "minValueDate", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueDateTime", "minValueDateTime", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("minValueInstant", "minValueInstant", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("minValueQuantity", "minValueQuantity", quantity.Quantity, False, "minValue", False),
            ("minValueTime", "minValueTime", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("orderMeaning", "orderMeaning", str, False, None, False),
            ("path", "path", str, False, None, True),
            ("patternAddress", "patternAddress", address.Address, False, "pattern", False),
            ("patternAge", "patternAge", age.Age, False, "pattern", False),
            ("patternAnnotation", "patternAnnotation", annotation.Annotation, False, "pattern", False),
            ("patternAttachment", "patternAttachment", attachment.Attachment, False, "pattern", False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("patternCanonical", "patternCanonical", str, False, "pattern", False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False, "pattern", False),
            ("patternCoding", "patternCoding", coding.Coding, False, "pattern", False),
            ("patternContactDetail", "patternContactDetail", contactdetail.ContactDetail, False, "pattern", False),
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False, "pattern", False),
            ("patternContributor", "patternContributor", contributor.Contributor, False, "pattern", False),
            ("patternCount", "patternCount", count.Count, False, "pattern", False),
            ("patternDataRequirement", "patternDataRequirement", datarequirement.DataRequirement, False, "pattern", False),
            ("patternDate", "patternDate", fhirdate.FHIRDate, False, "pattern", False),
            ("patternDateTime", "patternDateTime", fhirdate.FHIRDate, False, "pattern", False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("patternDistance", "patternDistance", distance.Distance, False, "pattern", False),
            ("patternDosage", "patternDosage", dosage.Dosage, False, "pattern", False),
            ("patternDuration", "patternDuration", duration.Duration, False, "pattern", False),
            ("patternExpression", "patternExpression", expression.Expression, False, "pattern", False),
            ("patternHumanName", "patternHumanName", humanname.HumanName, False, "pattern", False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False, "pattern", False),
            ("patternInstant", "patternInstant", fhirdate.FHIRDate, False, "pattern", False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("patternMoney", "patternMoney", money.Money, False, "pattern", False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("patternParameterDefinition", "patternParameterDefinition", parameterdefinition.ParameterDefinition, False, "pattern", False),
            ("patternPeriod", "patternPeriod", period.Period, False, "pattern", False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("patternQuantity", "patternQuantity", quantity.Quantity, False, "pattern", False),
            ("patternRange", "patternRange", range.Range, False, "pattern", False),
            ("patternRatio", "patternRatio", ratio.Ratio, False, "pattern", False),
            ("patternReference", "patternReference", fhirreference.FHIRReference, False, "pattern", False),
            ("patternRelatedArtifact", "patternRelatedArtifact", relatedartifact.RelatedArtifact, False, "pattern", False),
            ("patternSampledData", "patternSampledData", sampleddata.SampledData, False, "pattern", False),
            ("patternSignature", "patternSignature", signature.Signature, False, "pattern", False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("patternTime", "patternTime", fhirdate.FHIRDate, False, "pattern", False),
            ("patternTiming", "patternTiming", timing.Timing, False, "pattern", False),
            ("patternTriggerDefinition", "patternTriggerDefinition", triggerdefinition.TriggerDefinition, False, "pattern", False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("patternUrl", "patternUrl", str, False, "pattern", False),
            ("patternUsageContext", "patternUsageContext", usagecontext.UsageContext, False, "pattern", False),
            ("patternUuid", "patternUuid", str, False, "pattern", False),
            ("representation", "representation", str, True, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("short", "short", str, False, None, False),
            ("sliceIsConstraining", "sliceIsConstraining", bool, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False),
            ("type", "type", ElementDefinitionType, True, None, False),
        ])
        return js


from . import element

class ElementDefinitionBase(element.Element):
    """ 
    B
    a
    s
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
    t
    o
    o
    l
    s
    .
    
    
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
    a
    b
    o
    u
    t
    t
    h
    e
    b
    a
    s
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
    t
    h
    e
    e
    l
    e
    m
    e
    n
    t
    ,
    p
    r
    o
    v
    i
    d
    e
    d
    t
    o
    m
    a
    k
    e
    i
    t
    u
    n
    n
    e
    c
    e
    s
    s
    a
    r
    y
    f
    o
    r
    t
    o
    o
    l
    s
    t
    o
    t
    r
    a
    c
    e
    t
    h
    e
    d
    e
    v
    i
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
    e
    l
    e
    m
    e
    n
    t
    t
    h
    r
    o
    u
    g
    h
    t
    h
    e
    d
    e
    r
    i
    v
    e
    d
    a
    n
    d
    r
    e
    l
    a
    t
    e
    d
    p
    r
    o
    f
    i
    l
    e
    s
    .
    W
    h
    e
    n
    t
    h
    e
    e
    l
    e
    m
    e
    n
    t
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
    n
    o
    t
    t
    h
    e
    o
    r
    i
    g
    i
    n
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
    a
    n
    e
    l
    e
    m
    e
    n
    t
    -
    i
    .
    g
    .
    e
    i
    t
    h
    e
    r
    i
    n
    a
    c
    o
    n
    s
    t
    r
    a
    i
    n
    t
    o
    n
    a
    n
    o
    t
    h
    e
    r
    t
    y
    p
    e
    ,
    o
    r
    f
    o
    r
    e
    l
    e
    m
    e
    n
    t
    s
    f
    r
    o
    m
    a
    s
    u
    p
    e
    r
    t
    y
    p
    e
    i
    n
    a
    s
    n
    a
    p
    s
    h
    o
    t
    -
    t
    h
    e
    n
    t
    h
    e
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
    i
    n
    p
    r
    o
    v
    i
    d
    e
    d
    i
    n
    t
    h
    e
    e
    l
    e
    m
    e
    n
    t
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
    b
    e
    d
    i
    f
    f
    e
    r
    e
    n
    t
    t
    o
    t
    h
    e
    b
    a
    s
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
    O
    n
    t
    h
    e
    o
    r
    i
    g
    i
    n
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
    e
    l
    e
    m
    e
    n
    t
    ,
    i
    t
    w
    i
    l
    l
    b
    e
    s
    a
    m
    e
    .
    
    """
    
    resource_type = "ElementDefinitionBase"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.max = None
        """ 
        M
        a
        x
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
        o
        f
        t
        h
        e
        b
        a
        s
        e
        e
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        self.min = None
        """ 
        M
        i
        n
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
        o
        f
        t
        h
        e
        b
        a
        s
        e
        e
        l
        e
        m
        e
        n
        t
        .
        Type `int`. """
        
        self.path = None
        """ 
        P
        a
        t
        h
        t
        h
        a
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
        t
        h
        e
        b
        a
        s
        e
        e
        l
        e
        m
        e
        n
        t
        .
        Type `str`. """
        
        super(ElementDefinitionBase, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("max", "max", str, False, None, True),
            ("min", "min", int, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


class ElementDefinitionBinding(element.Element):
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
    e
    l
    e
    m
    e
    n
    t
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
    ,
    Q
    u
    a
    n
    t
    i
    t
    y
    )
    ,
    o
    r
    t
    h
    e
    d
    a
    t
    a
    t
    y
    p
    e
    s
    (
    s
    t
    r
    i
    n
    g
    ,
    u
    r
    i
    )
    .
    
    """
    
    resource_type = "ElementDefinitionBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        H
        u
        m
        a
        n
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
        
        super(ElementDefinitionBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("strength", "strength", str, False, None, True),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js


class ElementDefinitionConstraint(element.Element):
    """ 
    C
    o
    n
    d
    i
    t
    i
    o
    n
    t
    h
    a
    t
    m
    u
    s
    t
    e
    v
    a
    l
    u
    a
    t
    e
    t
    o
    t
    r
    u
    e
    .
    
    
    F
    o
    r
    m
    a
    l
    c
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
    s
    u
    c
    h
    a
    s
    c
    o
    -
    o
    c
    c
    u
    r
    r
    e
    n
    c
    e
    a
    n
    d
    o
    t
    h
    e
    r
    c
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
    t
    h
    a
    t
    c
    a
    n
    b
    e
    c
    o
    m
    p
    u
    t
    a
    t
    i
    o
    n
    a
    l
    l
    y
    e
    v
    a
    l
    u
    a
    t
    e
    d
    w
    i
    t
    h
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
    
    """
    
    resource_type = "ElementDefinitionConstraint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
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
        o
        f
        c
        o
        n
        s
        t
        r
        a
        i
        n
        t
        .
        Type `str`. """
        
        self.human = None
        """ 
        H
        u
        m
        a
        n
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
        c
        o
        n
        s
        t
        r
        a
        i
        n
        t
        .
        Type `str`. """
        
        self.key = None
        """ 
        T
        a
        r
        g
        e
        t
        o
        f
        '
        c
        o
        n
        d
        i
        t
        i
        o
        n
        '
        r
        e
        f
        e
        r
        e
        n
        c
        e
        a
        b
        o
        v
        e
        .
        Type `str`. """
        
        self.requirements = None
        """ 
        W
        h
        y
        t
        h
        i
        s
        c
        o
        n
        s
        t
        r
        a
        i
        n
        t
        i
        s
        n
        e
        c
        e
        s
        s
        a
        r
        y
        o
        r
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
        .
        Type `str`. """
        
        self.severity = None
        """ 
        e
        r
        r
        o
        r
        |
        w
        a
        r
        n
        i
        n
        g
        .
        Type `str`. """
        
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
        e
        t
        o
        o
        r
        i
        g
        i
        n
        a
        l
        s
        o
        u
        r
        c
        e
        o
        f
        c
        o
        n
        s
        t
        r
        a
        i
        n
        t
        .
        Type `str`. """
        
        self.xpath = None
        """ 
        X
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
        o
        f
        c
        o
        n
        s
        t
        r
        a
        i
        n
        t
        .
        Type `str`. """
        
        super(ElementDefinitionConstraint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, False),
            ("human", "human", str, False, None, True),
            ("key", "key", str, False, None, True),
            ("requirements", "requirements", str, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("source", "source", str, False, None, False),
            ("xpath", "xpath", str, False, None, False),
        ])
        return js


class ElementDefinitionExample(element.Element):
    """ 
    E
    x
    a
    m
    p
    l
    e
    v
    a
    l
    u
    e
    (
    a
    s
    d
    e
    f
    i
    n
    e
    d
    f
    o
    r
    t
    y
    p
    e
    )
    .
    
    
    A
    s
    a
    m
    p
    l
    e
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
    e
    l
    e
    m
    e
    n
    t
    d
    e
    m
    o
    n
    s
    t
    r
    a
    t
    i
    n
    g
    t
    h
    e
    t
    y
    p
    e
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
    t
    h
    a
    t
    w
    o
    u
    l
    d
    t
    y
    p
    i
    c
    a
    l
    l
    y
    b
    e
    f
    o
    u
    n
    d
    i
    n
    t
    h
    e
    e
    l
    e
    m
    e
    n
    t
    .
    
    """
    
    resource_type = "ElementDefinitionExample"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.label = None
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
        i
        s
        e
        x
        a
        m
        p
        l
        e
        .
        Type `str`. """
        
        self.valueAddress = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
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
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `bool`. """
        
        self.valueCanonical = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueCode = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
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
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `float`. """
        
        self.valueDistance = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueIdentifier = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.valueMarkdown = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueMoney = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueParameterDefinition = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.valueQuantity = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueTime = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `int`. """
        
        self.valueUri = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueUrl = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        self.valueUsageContext = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        """ 
        V
        a
        l
        u
        e
        o
        f
        E
        x
        a
        m
        p
        l
        e
        (
        o
        n
        e
        o
        f
        a
        l
        l
        o
        w
        e
        d
        t
        y
        p
        e
        s
        )
        .
        Type `str`. """
        
        super(ElementDefinitionExample, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, True),
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


class ElementDefinitionMapping(element.Element):
    """ 
    M
    a
    p
    e
    l
    e
    m
    e
    n
    t
    t
    o
    a
    n
    o
    t
    h
    e
    r
    s
    e
    t
    o
    f
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
    a
    c
    o
    n
    c
    e
    p
    t
    f
    r
    o
    m
    a
    n
    e
    x
    t
    e
    r
    n
    a
    l
    s
    p
    e
    c
    i
    f
    i
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
    r
    o
    u
    g
    h
    l
    y
    c
    o
    r
    r
    e
    s
    p
    o
    n
    d
    s
    t
    o
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
    .
    
    """
    
    resource_type = "ElementDefinitionMapping"
    
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
        a
        b
        o
        u
        t
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
        o
        r
        i
        t
        s
        u
        s
        e
        .
        Type `str`. """
        
        self.identity = None
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
        m
        a
        p
        p
        i
        n
        g
        d
        e
        c
        l
        a
        r
        a
        t
        i
        o
        n
        .
        Type `str`. """
        
        self.language = None
        """ 
        C
        o
        m
        p
        u
        t
        a
        b
        l
        e
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
        m
        a
        p
        p
        i
        n
        g
        .
        Type `str`. """
        
        self.map = None
        """ 
        D
        e
        t
        a
        i
        l
        s
        o
        f
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
        Type `str`. """
        
        super(ElementDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("language", "language", str, False, None, False),
            ("map", "map", str, False, None, True),
        ])
        return js


class ElementDefinitionSlicing(element.Element):
    """ 
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
    i
    s
    s
    l
    i
    c
    e
    d
    -
    s
    l
    i
    c
    e
    s
    f
    o
    l
    l
    o
    w
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
    t
    h
    a
    t
    t
    h
    e
    e
    l
    e
    m
    e
    n
    t
    i
    s
    s
    l
    i
    c
    e
    d
    i
    n
    t
    o
    a
    s
    e
    t
    o
    f
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
    (
    i
    .
    e
    .
    i
    n
    a
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
    ,
    t
    h
    e
    r
    e
    a
    r
    e
    m
    u
    l
    t
    i
    p
    l
    e
    d
    i
    f
    f
    e
    r
    e
    n
    t
    c
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
    a
    s
    i
    n
    g
    l
    e
    e
    l
    e
    m
    e
    n
    t
    i
    n
    t
    h
    e
    b
    a
    s
    e
    r
    e
    s
    o
    u
    r
    c
    e
    )
    .
    S
    l
    i
    c
    i
    n
    g
    c
    a
    n
    b
    e
    u
    s
    e
    d
    i
    n
    a
    n
    y
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
    h
    a
    s
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
    .
    *
    o
    n
    t
    h
    e
    b
    a
    s
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
    o
    r
    a
    n
    y
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
    a
    c
    h
    o
    i
    c
    e
    o
    f
    t
    y
    p
    e
    s
    .
    T
    h
    e
    s
    e
    t
    o
    f
    s
    l
    i
    c
    e
    s
    i
    s
    a
    n
    y
    e
    l
    e
    m
    e
    n
    t
    s
    t
    h
    a
    t
    c
    o
    m
    e
    a
    f
    t
    e
    r
    t
    h
    i
    s
    i
    n
    t
    h
    e
    e
    l
    e
    m
    e
    n
    t
    s
    e
    q
    u
    e
    n
    c
    e
    t
    h
    a
    t
    h
    a
    v
    e
    t
    h
    e
    s
    a
    m
    e
    p
    a
    t
    h
    ,
    u
    n
    t
    i
    l
    a
    s
    h
    o
    r
    t
    e
    r
    p
    a
    t
    h
    o
    c
    c
    u
    r
    s
    (
    t
    h
    e
    s
    h
    o
    r
    t
    e
    r
    p
    a
    t
    h
    t
    e
    r
    m
    i
    n
    a
    t
    e
    s
    t
    h
    e
    s
    e
    t
    )
    .
    
    """
    
    resource_type = "ElementDefinitionSlicing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ 
        T
        e
        x
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
        h
        o
        w
        s
        l
        i
        c
        i
        n
        g
        w
        o
        r
        k
        s
        (
        o
        r
        n
        o
        t
        )
        .
        Type `str`. """
        
        self.discriminator = None
        """ 
        E
        l
        e
        m
        e
        n
        t
        v
        a
        l
        u
        e
        s
        t
        h
        a
        t
        a
        r
        e
        u
        s
        e
        d
        t
        o
        d
        i
        s
        t
        i
        n
        g
        u
        i
        s
        h
        t
        h
        e
        s
        l
        i
        c
        e
        s
        .
        List of `ElementDefinitionSlicingDiscriminator` items (represented as `dict` in JSON). """
        
        self.ordered = None
        """ 
        I
        f
        e
        l
        e
        m
        e
        n
        t
        s
        m
        u
        s
        t
        b
        e
        i
        n
        s
        a
        m
        e
        o
        r
        d
        e
        r
        a
        s
        s
        l
        i
        c
        e
        s
        .
        Type `bool`. """
        
        self.rules = None
        """ 
        c
        l
        o
        s
        e
        d
        |
        o
        p
        e
        n
        |
        o
        p
        e
        n
        A
        t
        E
        n
        d
        .
        Type `str`. """
        
        super(ElementDefinitionSlicing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("discriminator", "discriminator", ElementDefinitionSlicingDiscriminator, True, None, False),
            ("ordered", "ordered", bool, False, None, False),
            ("rules", "rules", str, False, None, True),
        ])
        return js


class ElementDefinitionSlicingDiscriminator(element.Element):
    """ 
    E
    l
    e
    m
    e
    n
    t
    v
    a
    l
    u
    e
    s
    t
    h
    a
    t
    a
    r
    e
    u
    s
    e
    d
    t
    o
    d
    i
    s
    t
    i
    n
    g
    u
    i
    s
    h
    t
    h
    e
    s
    l
    i
    c
    e
    s
    .
    
    
    D
    e
    s
    i
    g
    n
    a
    t
    e
    s
    w
    h
    i
    c
    h
    c
    h
    i
    l
    d
    e
    l
    e
    m
    e
    n
    t
    s
    a
    r
    e
    u
    s
    e
    d
    t
    o
    d
    i
    s
    c
    r
    i
    m
    i
    n
    a
    t
    e
    b
    e
    t
    w
    e
    e
    n
    t
    h
    e
    s
    l
    i
    c
    e
    s
    w
    h
    e
    n
    p
    r
    o
    c
    e
    s
    s
    i
    n
    g
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
    .
    I
    f
    o
    n
    e
    o
    r
    m
    o
    r
    e
    d
    i
    s
    c
    r
    i
    m
    i
    n
    a
    t
    o
    r
    s
    a
    r
    e
    p
    r
    o
    v
    i
    d
    e
    d
    ,
    t
    h
    e
    v
    a
    l
    u
    e
    o
    f
    t
    h
    e
    c
    h
    i
    l
    d
    e
    l
    e
    m
    e
    n
    t
    s
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
    d
    a
    t
    a
    S
    H
    A
    L
    L
    c
    o
    m
    p
    l
    e
    t
    e
    l
    y
    d
    i
    s
    t
    i
    n
    g
    u
    i
    s
    h
    w
    h
    i
    c
    h
    s
    l
    i
    c
    e
    t
    h
    e
    e
    l
    e
    m
    e
    n
    t
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
    m
    a
    t
    c
    h
    e
    s
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
    a
    l
    l
    o
    w
    e
    d
    v
    a
    l
    u
    e
    s
    f
    o
    r
    t
    h
    o
    s
    e
    e
    l
    e
    m
    e
    n
    t
    s
    i
    n
    e
    a
    c
    h
    o
    f
    t
    h
    e
    s
    l
    i
    c
    e
    s
    .
    
    """
    
    resource_type = "ElementDefinitionSlicingDiscriminator"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ 
        P
        a
        t
        h
        t
        o
        e
        l
        e
        m
        e
        n
        t
        v
        a
        l
        u
        e
        .
        Type `str`. """
        
        self.type = None
        """ 
        v
        a
        l
        u
        e
        |
        e
        x
        i
        s
        t
        s
        |
        p
        a
        t
        t
        e
        r
        n
        |
        t
        y
        p
        e
        |
        p
        r
        o
        f
        i
        l
        e
        .
        Type `str`. """
        
        super(ElementDefinitionSlicingDiscriminator, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("type", "type", str, False, None, True),
        ])
        return js


class ElementDefinitionType(element.Element):
    """ 
    D
    a
    t
    a
    t
    y
    p
    e
    a
    n
    d
    P
    r
    o
    f
    i
    l
    e
    f
    o
    r
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
    .
    
    
    T
    h
    e
    d
    a
    t
    a
    t
    y
    p
    e
    o
    r
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
    t
    h
    e
    v
    a
    l
    u
    e
    o
    f
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
    s
    p
    e
    r
    m
    i
    t
    t
    e
    d
    t
    o
    b
    e
    .
    
    """
    
    resource_type = "ElementDefinitionType"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.aggregation = None
        """ 
        c
        o
        n
        t
        a
        i
        n
        e
        d
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
        d
        |
        b
        u
        n
        d
        l
        e
        d
        -
        h
        o
        w
        a
        g
        g
        r
        e
        g
        a
        t
        e
        d
        .
        List of `str` items. """
        
        self.code = None
        """ 
        D
        a
        t
        a
        t
        y
        p
        e
        o
        r
        R
        e
        s
        o
        u
        r
        c
        e
        (
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
        )
        .
        Type `str`. """
        
        self.profile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        s
        (
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
        o
        r
        I
        G
        )
        -
        o
        n
        e
        m
        u
        s
        t
        a
        p
        p
        l
        y
        .
        List of `str` items. """
        
        self.targetProfile = None
        """ 
        P
        r
        o
        f
        i
        l
        e
        (
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
        o
        r
        I
        G
        )
        o
        n
        t
        h
        e
        R
        e
        f
        e
        r
        e
        n
        c
        e
        /
        c
        a
        n
        o
        n
        i
        c
        a
        l
        t
        a
        r
        g
        e
        t
        -
        o
        n
        e
        m
        u
        s
        t
        a
        p
        p
        l
        y
        .
        List of `str` items. """
        
        self.versioning = None
        """ 
        e
        i
        t
        h
        e
        r
        |
        i
        n
        d
        e
        p
        e
        n
        d
        e
        n
        t
        |
        s
        p
        e
        c
        i
        f
        i
        c
        .
        Type `str`. """
        
        super(ElementDefinitionType, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("aggregation", "aggregation", str, True, None, False),
            ("code", "code", str, False, None, True),
            ("profile", "profile", str, True, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("versioning", "versioning", str, False, None, False),
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
