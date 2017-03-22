#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2017-03-22.
#  2017, SMART Health IT.


from . import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.
    
    This special resource type is used to represent an operation request and
    response (operations.html). It has no other use, and there is no RESTful
    endpoint associated with it.
    """
    
    resource_type = "Parameters"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.parameter = None
        """ Operation Parameter.
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
    """ Operation Parameter.
    
    A parameter passed to or received from the operation.
    """
    
    resource_type = "ParametersParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name from the definition.
        Type `str`. """
        
        self.part = None
        """ Named part of a multi-part parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ If parameter is a data type.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueBoolean = None
        """ If parameter is a data type.
        Type `bool`. """
        
        self.valueCode = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ If parameter is a data type.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ If parameter is a data type.
        Type `float`. """
        
        self.valueDistance = None
        """ If parameter is a data type.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ If parameter is a data type.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueIdentifier = None
        """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valueMarkdown = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueMeta = None
        """ If parameter is a data type.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ If parameter is a data type.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valuePeriod = None
        """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valueQuantity = None
        """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ If parameter is a data type.
        Type `str`. """
        
        self.valueTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        """ If parameter is a data type.
        Type `int`. """
        
        self.valueUri = None
        """ If parameter is a data type.
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
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False),
            ("valueCount", "valueCount", count.Count, False, "value", False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False),
            ("valueId", "valueId", str, False, "value", False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", False),
            ("valueMoney", "valueMoney", money.Money, False, "value", False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
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
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + '.count']
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + '.distance']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
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
    from . import meta
except ImportError:
    meta = sys.modules[__package__ + '.meta']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
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
