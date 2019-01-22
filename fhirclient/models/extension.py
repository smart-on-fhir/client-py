#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/Extension) on 2019-01-22.
#  2019, SMART Health IT.


from . import element

class Extension(element.Element):
    """ 
    O
    p
    t
    i
    o
    n
    a
    l
    E
    x
    t
    e
    n
    s
    i
    o
    n
    s
    E
    l
    e
    m
    e
    n
    t
    .
    
    
    O
    p
    t
    i
    o
    n
    a
    l
    E
    x
    t
    e
    n
    s
    i
    o
    n
    E
    l
    e
    m
    e
    n
    t
    -
    f
    o
    u
    n
    d
    i
    n
    a
    l
    l
    r
    e
    s
    o
    u
    r
    c
    e
    s
    .
    
    """
    
    resource_type = "Extension"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ 
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
        Type `str`. """
        
        super(Extension, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Extension, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
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
