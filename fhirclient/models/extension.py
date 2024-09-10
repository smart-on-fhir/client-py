# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Extension).
# 2024, SMART Health IT.


from . import element

class Extension(element.Element):
    """ Optional Extensions Element.
    
    Optional Extension Element - found in all resources.
    """
    
    resource_type = "Extension"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.url = None
        """ identifies the meaning of the extension.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.valueAddress = None
        """ Value of extension.
        Type `Address` (represented as `dict` in JSON). """
        self._valueAddress = None
        """ Primitive extension for valueAddress. Type `FHIRPrimitiveExtension` """
        
        self.valueAge = None
        """ Value of extension.
        Type `Age` (represented as `dict` in JSON). """
        self._valueAge = None
        """ Primitive extension for valueAge. Type `FHIRPrimitiveExtension` """
        
        self.valueAnnotation = None
        """ Value of extension.
        Type `Annotation` (represented as `dict` in JSON). """
        self._valueAnnotation = None
        """ Primitive extension for valueAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.valueAttachment = None
        """ Value of extension.
        Type `Attachment` (represented as `dict` in JSON). """
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBase64Binary = None
        """ Value of extension.
        Type `str`. """
        self._valueBase64Binary = None
        """ Primitive extension for valueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Value of extension.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCanonical = None
        """ Value of extension.
        Type `str`. """
        self._valueCanonical = None
        """ Primitive extension for valueCanonical. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ Value of extension.
        Type `str`. """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Value of extension.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ Value of extension.
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueContactDetail = None
        """ Value of extension.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._valueContactDetail = None
        """ Primitive extension for valueContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.valueContactPoint = None
        """ Value of extension.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._valueContactPoint = None
        """ Primitive extension for valueContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.valueContributor = None
        """ Value of extension.
        Type `Contributor` (represented as `dict` in JSON). """
        self._valueContributor = None
        """ Primitive extension for valueContributor. Type `FHIRPrimitiveExtension` """
        
        self.valueCount = None
        """ Value of extension.
        Type `Count` (represented as `dict` in JSON). """
        self._valueCount = None
        """ Primitive extension for valueCount. Type `FHIRPrimitiveExtension` """
        
        self.valueDataRequirement = None
        """ Value of extension.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._valueDataRequirement = None
        """ Primitive extension for valueDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ Value of extension.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Value of extension.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Value of extension.
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueDistance = None
        """ Value of extension.
        Type `Distance` (represented as `dict` in JSON). """
        self._valueDistance = None
        """ Primitive extension for valueDistance. Type `FHIRPrimitiveExtension` """
        
        self.valueDosage = None
        """ Value of extension.
        Type `Dosage` (represented as `dict` in JSON). """
        self._valueDosage = None
        """ Primitive extension for valueDosage. Type `FHIRPrimitiveExtension` """
        
        self.valueDuration = None
        """ Value of extension.
        Type `Duration` (represented as `dict` in JSON). """
        self._valueDuration = None
        """ Primitive extension for valueDuration. Type `FHIRPrimitiveExtension` """
        
        self.valueExpression = None
        """ Value of extension.
        Type `Expression` (represented as `dict` in JSON). """
        self._valueExpression = None
        """ Primitive extension for valueExpression. Type `FHIRPrimitiveExtension` """
        
        self.valueHumanName = None
        """ Value of extension.
        Type `HumanName` (represented as `dict` in JSON). """
        self._valueHumanName = None
        """ Primitive extension for valueHumanName. Type `FHIRPrimitiveExtension` """
        
        self.valueId = None
        """ Value of extension.
        Type `str`. """
        self._valueId = None
        """ Primitive extension for valueId. Type `FHIRPrimitiveExtension` """
        
        self.valueIdentifier = None
        """ Value of extension.
        Type `Identifier` (represented as `dict` in JSON). """
        self._valueIdentifier = None
        """ Primitive extension for valueIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.valueInstant = None
        """ Value of extension.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._valueInstant = None
        """ Primitive extension for valueInstant. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Value of extension.
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueMarkdown = None
        """ Value of extension.
        Type `str`. """
        self._valueMarkdown = None
        """ Primitive extension for valueMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.valueMeta = None
        """ Value of extension.
        Type `Meta` (represented as `dict` in JSON). """
        self._valueMeta = None
        """ Primitive extension for valueMeta. Type `FHIRPrimitiveExtension` """
        
        self.valueMoney = None
        """ Value of extension.
        Type `Money` (represented as `dict` in JSON). """
        self._valueMoney = None
        """ Primitive extension for valueMoney. Type `FHIRPrimitiveExtension` """
        
        self.valueOid = None
        """ Value of extension.
        Type `str`. """
        self._valueOid = None
        """ Primitive extension for valueOid. Type `FHIRPrimitiveExtension` """
        
        self.valueParameterDefinition = None
        """ Value of extension.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._valueParameterDefinition = None
        """ Primitive extension for valueParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ Value of extension.
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valuePositiveInt = None
        """ Value of extension.
        Type `int`. """
        self._valuePositiveInt = None
        """ Primitive extension for valuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Value of extension.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Value of extension.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueRatio = None
        """ Value of extension.
        Type `Ratio` (represented as `dict` in JSON). """
        self._valueRatio = None
        """ Primitive extension for valueRatio. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Value of extension.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueRelatedArtifact = None
        """ Value of extension.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._valueRelatedArtifact = None
        """ Primitive extension for valueRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.valueSampledData = None
        """ Value of extension.
        Type `SampledData` (represented as `dict` in JSON). """
        self._valueSampledData = None
        """ Primitive extension for valueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.valueSignature = None
        """ Value of extension.
        Type `Signature` (represented as `dict` in JSON). """
        self._valueSignature = None
        """ Primitive extension for valueSignature. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Value of extension.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Value of extension.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        self.valueTiming = None
        """ Value of extension.
        Type `Timing` (represented as `dict` in JSON). """
        self._valueTiming = None
        """ Primitive extension for valueTiming. Type `FHIRPrimitiveExtension` """
        
        self.valueTriggerDefinition = None
        """ Value of extension.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._valueTriggerDefinition = None
        """ Primitive extension for valueTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valueUnsignedInt = None
        """ Value of extension.
        Type `int`. """
        self._valueUnsignedInt = None
        """ Primitive extension for valueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ Value of extension.
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        self.valueUrl = None
        """ Value of extension.
        Type `str`. """
        self._valueUrl = None
        """ Primitive extension for valueUrl. Type `FHIRPrimitiveExtension` """
        
        self.valueUsageContext = None
        """ Value of extension.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._valueUsageContext = None
        """ Primitive extension for valueUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.valueUuid = None
        """ Value of extension.
        Type `str`. """
        self._valueUuid = None
        """ Primitive extension for valueUuid. Type `FHIRPrimitiveExtension` """
        
        super(Extension, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Extension, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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