#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Parameters) on 2019-01-22.
#  2019, SMART Health IT.


from . import resource

class Parameters(resource.Resource):
    """ 
    O
    p
    e
    r
    a
    t
    i
    o
    n
    R
    e
    q
    u
    e
    s
    t
    o
    r
    R
    e
    s
    p
    o
    n
    s
    e
    .
    
    
    T
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
    i
    s
    a
    n
    o
    n
    -
    p
    e
    r
    s
    i
    s
    t
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
    u
    s
    e
    d
    t
    o
    p
    a
    s
    s
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
    t
    o
    a
    n
    d
    b
    a
    c
    k
    f
    r
    o
    m
    a
    n
    [
    o
    p
    e
    r
    a
    t
    i
    o
    n
    ]
    (
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
    h
    t
    m
    l
    )
    .
    I
    t
    h
    a
    s
    n
    o
    o
    t
    h
    e
    r
    u
    s
    e
    ,
    a
    n
    d
    t
    h
    e
    r
    e
    i
    s
    n
    o
    R
    E
    S
    T
    f
    u
    l
    e
    n
    d
    p
    o
    i
    n
    t
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
    i
    t
    .
    
    """
    
    resource_type = "Parameters"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.parameter = None
        """ 
        O
        p
        e
        r
        a
        t
        i
        o
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
        .
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(Parameters, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True, None, False),
        ])
        return js


from . import backboneelement

class ParametersParameter(backboneelement.BackboneElement):
    """ 
    O
    p
    e
    r
    a
    t
    i
    o
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
    p
    a
    s
    s
    e
    d
    t
    o
    o
    r
    r
    e
    c
    e
    i
    v
    e
    d
    f
    r
    o
    m
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
    
    """
    
    resource_type = "ParametersParameter"
    
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
        f
        r
        o
        m
        t
        h
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
        
        self.part = None
        """ 
        N
        a
        m
        e
        d
        p
        a
        r
        t
        o
        f
        a
        m
        u
        l
        t
        i
        -
        p
        a
        r
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
        .
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ 
        I
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
        i
        s
        a
        w
        h
        o
        l
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
        Type `Resource` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueBoolean = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `bool`. """
        
        self.valueCanonical = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueCode = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactDetail = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `ContactDetail` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueContributor = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Contributor` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDataRequirement = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `DataRequirement` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `float`. """
        
        self.valueDistance = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDosage = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Dosage` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueExpression = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Expression` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueIdentifier = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `int`. """
        
        self.valueMarkdown = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueMoney = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueParameterDefinition = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        
        self.valuePeriod = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `int`. """
        
        self.valueQuantity = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueRelatedArtifact = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueTime = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueTriggerDefinition = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `int`. """
        
        self.valueUri = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueUrl = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        self.valueUsageContext = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `UsageContext` (represented as `dict` in JSON). """
        
        self.valueUuid = None
        """ 
        I
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
        i
        s
        a
        d
        a
        t
        a
        t
        y
        p
        e
        .
        Type `str`. """
        
        super(ParametersParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("part", "part", ParametersParameter, True, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("valueAddress", "valueAddress", address.Address, False, "value", False),
            ("valueAge", "valueAge", age.Age, False, "value", False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCanonical", "valueCanonical", str, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", False),
            ("valueCount", "valueCount", count.Count, False, "value", False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False),
            ("valueId", "valueId", str, False, "value", False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("valueMoney", "valueMoney", money.Money, False, "value", False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("valueUrl", "valueUrl", str, False, "value", False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", False),
            ("valueUuid", "valueUuid", str, False, "value", False),
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
