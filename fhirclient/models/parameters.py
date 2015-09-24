#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Parameters) on 2015-09-24.
#  2015, SMART Health IT.


from . import address
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import humanname
from . import identifier
from . import meta
from . import period
from . import quantity
from . import range
from . import ratio
from . import resource
from . import sampleddata
from . import signature
from . import timing


class Parameters(resource.Resource):
    """ Operation Request or Response.
    
    This special resource type is used to represent an operation request and
    response (operations.html). It has no other use, and there is no RESTful
    endpoint associated with it.
    """
    
    resource_name = "Parameters"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.parameter = None
        """ Operation Parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        super(Parameters, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True),
        ])
        return js


class ParametersParameter(fhirelement.FHIRElement):
    """ Operation Parameter.
    
    A parameter passed to or received from the operation.
    """
    
    resource_name = "ParametersParameter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name from the definition.
        Type `str`. """
        
        self.part = None
        """ Named part of a parameter (e.g. Tuple).
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        
        self.resource = None
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
        
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
        
        self.valueDate = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ If parameter is a data type.
        Type `float`. """
        
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
        
        super(ParametersParameter, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("part", "part", ParametersParameter, True),
            ("resource", "resource", resource.Resource, False),
            ("valueAddress", "valueAddress", address.Address, False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False),
            ("valueBase64Binary", "valueBase64Binary", str, False),
            ("valueBoolean", "valueBoolean", bool, False),
            ("valueCode", "valueCode", str, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False),
            ("valueCoding", "valueCoding", coding.Coding, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False),
            ("valueDecimal", "valueDecimal", float, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False),
            ("valueId", "valueId", str, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False),
            ("valueInteger", "valueInteger", int, False),
            ("valueMarkdown", "valueMarkdown", str, False),
            ("valueMeta", "valueMeta", meta.Meta, False),
            ("valueOid", "valueOid", str, False),
            ("valuePeriod", "valuePeriod", period.Period, False),
            ("valuePositiveInt", "valuePositiveInt", int, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False),
            ("valueRange", "valueRange", range.Range, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False),
            ("valueSignature", "valueSignature", signature.Signature, False),
            ("valueString", "valueString", str, False),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False),
            ("valueTiming", "valueTiming", timing.Timing, False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False),
            ("valueUri", "valueUri", str, False),
        ])
        return js

