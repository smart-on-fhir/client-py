# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Parameters).
# 2024, SMART Health IT.


from . import resource

class Parameters(resource.Resource):
    """ Operation Request or Response.
    
    This resource is a non-persisted resource used to pass information into and
    back from an [operation](operations.html). It has no other use, and there
    is no RESTful endpoint associated with it.
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
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        super(Parameters, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Parameters, self).elementProperties()
        js.extend([
            ("parameter", "parameter", ParametersParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.part = None
        """ Named part of a multi-part parameter.
        List of `ParametersParameter` items (represented as `dict` in JSON). """
        self._part = None
        """ Primitive extension for part. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ If parameter is a whole resource.
        Type `Resource` (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.valueAddress = None
        """ If parameter is a data type.
        Type `Address` (represented as `dict` in JSON). """
        self._valueAddress = None
        """ Primitive extension for valueAddress. Type `FHIRPrimitiveExtension` """
        
        self.valueAge = None
        """ If parameter is a data type.
        Type `Age` (represented as `dict` in JSON). """
        self._valueAge = None
        """ Primitive extension for valueAge. Type `FHIRPrimitiveExtension` """
        
        self.valueAnnotation = None
        """ If parameter is a data type.
        Type `Annotation` (represented as `dict` in JSON). """
        self._valueAnnotation = None
        """ Primitive extension for valueAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.valueAttachment = None
        """ If parameter is a data type.
        Type `Attachment` (represented as `dict` in JSON). """
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBase64Binary = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueBase64Binary = None
        """ Primitive extension for valueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ If parameter is a data type.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCanonical = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueCanonical = None
        """ Primitive extension for valueCanonical. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ If parameter is a data type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ If parameter is a data type.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueContactDetail = None
        """ If parameter is a data type.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._valueContactDetail = None
        """ Primitive extension for valueContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.valueContactPoint = None
        """ If parameter is a data type.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._valueContactPoint = None
        """ Primitive extension for valueContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.valueContributor = None
        """ If parameter is a data type.
        Type `Contributor` (represented as `dict` in JSON). """
        self._valueContributor = None
        """ Primitive extension for valueContributor. Type `FHIRPrimitiveExtension` """
        
        self.valueCount = None
        """ If parameter is a data type.
        Type `Count` (represented as `dict` in JSON). """
        self._valueCount = None
        """ Primitive extension for valueCount. Type `FHIRPrimitiveExtension` """
        
        self.valueDataRequirement = None
        """ If parameter is a data type.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._valueDataRequirement = None
        """ Primitive extension for valueDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ If parameter is a data type.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ If parameter is a data type.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ If parameter is a data type.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueDistance = None
        """ If parameter is a data type.
        Type `Distance` (represented as `dict` in JSON). """
        self._valueDistance = None
        """ Primitive extension for valueDistance. Type `FHIRPrimitiveExtension` """
        
        self.valueDosage = None
        """ If parameter is a data type.
        Type `Dosage` (represented as `dict` in JSON). """
        self._valueDosage = None
        """ Primitive extension for valueDosage. Type `FHIRPrimitiveExtension` """
        
        self.valueDuration = None
        """ If parameter is a data type.
        Type `Duration` (represented as `dict` in JSON). """
        self._valueDuration = None
        """ Primitive extension for valueDuration. Type `FHIRPrimitiveExtension` """
        
        self.valueExpression = None
        """ If parameter is a data type.
        Type `Expression` (represented as `dict` in JSON). """
        self._valueExpression = None
        """ Primitive extension for valueExpression. Type `FHIRPrimitiveExtension` """
        
        self.valueHumanName = None
        """ If parameter is a data type.
        Type `HumanName` (represented as `dict` in JSON). """
        self._valueHumanName = None
        """ Primitive extension for valueHumanName. Type `FHIRPrimitiveExtension` """
        
        self.valueId = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueId = None
        """ Primitive extension for valueId. Type `FHIRPrimitiveExtension` """
        
        self.valueIdentifier = None
        """ If parameter is a data type.
        Type `Identifier` (represented as `dict` in JSON). """
        self._valueIdentifier = None
        """ Primitive extension for valueIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.valueInstant = None
        """ If parameter is a data type.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._valueInstant = None
        """ Primitive extension for valueInstant. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ If parameter is a data type.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueMarkdown = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueMarkdown = None
        """ Primitive extension for valueMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.valueMeta = None
        """ If parameter is a data type.
        Type `Meta` (represented as `dict` in JSON). """
        self._valueMeta = None
        """ Primitive extension for valueMeta. Type `FHIRPrimitiveExtension` """
        
        self.valueMoney = None
        """ If parameter is a data type.
        Type `Money` (represented as `dict` in JSON). """
        self._valueMoney = None
        """ Primitive extension for valueMoney. Type `FHIRPrimitiveExtension` """
        
        self.valueOid = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueOid = None
        """ Primitive extension for valueOid. Type `FHIRPrimitiveExtension` """
        
        self.valueParameterDefinition = None
        """ If parameter is a data type.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._valueParameterDefinition = None
        """ Primitive extension for valueParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ If parameter is a data type.
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valuePositiveInt = None
        """ If parameter is a data type.
        Type `int`. """
        self._valuePositiveInt = None
        """ Primitive extension for valuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ If parameter is a data type.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ If parameter is a data type.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueRatio = None
        """ If parameter is a data type.
        Type `Ratio` (represented as `dict` in JSON). """
        self._valueRatio = None
        """ Primitive extension for valueRatio. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ If parameter is a data type.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueRelatedArtifact = None
        """ If parameter is a data type.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._valueRelatedArtifact = None
        """ Primitive extension for valueRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.valueSampledData = None
        """ If parameter is a data type.
        Type `SampledData` (represented as `dict` in JSON). """
        self._valueSampledData = None
        """ Primitive extension for valueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.valueSignature = None
        """ If parameter is a data type.
        Type `Signature` (represented as `dict` in JSON). """
        self._valueSignature = None
        """ Primitive extension for valueSignature. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ If parameter is a data type.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        self.valueTiming = None
        """ If parameter is a data type.
        Type `Timing` (represented as `dict` in JSON). """
        self._valueTiming = None
        """ Primitive extension for valueTiming. Type `FHIRPrimitiveExtension` """
        
        self.valueTriggerDefinition = None
        """ If parameter is a data type.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._valueTriggerDefinition = None
        """ Primitive extension for valueTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valueUnsignedInt = None
        """ If parameter is a data type.
        Type `int`. """
        self._valueUnsignedInt = None
        """ Primitive extension for valueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        self.valueUrl = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueUrl = None
        """ Primitive extension for valueUrl. Type `FHIRPrimitiveExtension` """
        
        self.valueUsageContext = None
        """ If parameter is a data type.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._valueUsageContext = None
        """ Primitive extension for valueUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.valueUuid = None
        """ If parameter is a data type.
        Type `str`. """
        self._valueUuid = None
        """ Primitive extension for valueUuid. Type `FHIRPrimitiveExtension` """
        
        super(ParametersParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ParametersParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("part", "part", ParametersParameter, True, None, False),
            ("_part", "_part", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", resource.Resource, False, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAddress", "valueAddress", address.Address, False, "value", False),
            ("_valueAddress", "_valueAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAge", "valueAge", age.Age, False, "value", False),
            ("_valueAge", "_valueAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", False),
            ("_valueAnnotation", "_valueAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", False),
            ("_valueAttachment", "_valueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("_valueBase64Binary", "_valueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", False),
            ("_valueCanonical", "_valueCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", False),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", False),
            ("_valueContactDetail", "_valueContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", False),
            ("_valueContactPoint", "_valueContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", False),
            ("_valueContributor", "_valueContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCount", "valueCount", count.Count, False, "value", False),
            ("_valueCount", "_valueCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", False),
            ("_valueDataRequirement", "_valueDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", False),
            ("_valueDate", "_valueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", False),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", False),
            ("_valueDistance", "_valueDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", False),
            ("_valueDosage", "_valueDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", False),
            ("_valueDuration", "_valueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", False),
            ("_valueExpression", "_valueExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", False),
            ("_valueHumanName", "_valueHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueId", "valueId", str, False, "value", False),
            ("_valueId", "_valueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", False),
            ("_valueIdentifier", "_valueIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInstant", "valueInstant", fhirinstant.FHIRInstant, False, "value", False),
            ("_valueInstant", "_valueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", False),
            ("_valueMarkdown", "_valueMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", False),
            ("_valueMeta", "_valueMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", False),
            ("_valueMoney", "_valueMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueOid", "valueOid", str, False, "value", False),
            ("_valueOid", "_valueOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", False),
            ("_valueParameterDefinition", "_valueParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", False),
            ("_valuePeriod", "_valuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", False),
            ("_valuePositiveInt", "_valuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", False),
            ("_valueRatio", "_valueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", False),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", False),
            ("_valueRelatedArtifact", "_valueRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", False),
            ("_valueSampledData", "_valueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", False),
            ("_valueSignature", "_valueSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", False),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", False),
            ("_valueTiming", "_valueTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", False),
            ("_valueTriggerDefinition", "_valueTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", False),
            ("_valueUnsignedInt", "_valueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUri", "valueUri", str, False, "value", False),
            ("_valueUri", "_valueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", False),
            ("_valueUrl", "_valueUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", False),
            ("_valueUsageContext", "_valueUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUuid", "valueUuid", str, False, "value", False),
            ("_valueUuid", "_valueUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactdetail
from . import contactpoint
from . import contributor
from . import count
from . import datarequirement
from . import distance
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import fhirtime
from . import humanname
from . import identifier
from . import meta
from . import money
from . import parameterdefinition
from . import period
from . import quantity
from . import range
from . import ratio
from . import relatedartifact
from . import sampleddata
from . import signature
from . import timing
from . import triggerdefinition
from . import usagecontext