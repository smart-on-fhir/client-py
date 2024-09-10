# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ElementDefinition).
# 2024, SMART Health IT.


from . import backboneelement

class ElementDefinition(backboneelement.BackboneElement):
    """ Definition of an element in a resource or extension.
    
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    
    resource_type = "ElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        """ Other names.
        List of `str` items. """
        self._alias = None
        """ Primitive extension for alias. Type `FHIRPrimitiveExtension` """
        
        self.base = None
        """ Base definition information for tools.
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """
        self._base = None
        """ Primitive extension for base. Type `FHIRPrimitiveExtension` """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """
        self._binding = None
        """ Primitive extension for binding. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Corresponding codes in terminologies.
        List of `Coding` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Comments about the use of this element.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Reference to invariant about presence.
        List of `str` items. """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.constraint = None
        """ Condition that must evaluate to true.
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """
        self._constraint = None
        """ Primitive extension for constraint. Type `FHIRPrimitiveExtension` """
        
        self.contentReference = None
        """ Reference to definition of content for the element.
        Type `str`. """
        self._contentReference = None
        """ Primitive extension for contentReference. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAddress = None
        """ Specified value if missing from instance.
        Type `Address` (represented as `dict` in JSON). """
        self._defaultValueAddress = None
        """ Primitive extension for defaultValueAddress. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAge = None
        """ Specified value if missing from instance.
        Type `Age` (represented as `dict` in JSON). """
        self._defaultValueAge = None
        """ Primitive extension for defaultValueAge. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAnnotation = None
        """ Specified value if missing from instance.
        Type `Annotation` (represented as `dict` in JSON). """
        self._defaultValueAnnotation = None
        """ Primitive extension for defaultValueAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueAttachment = None
        """ Specified value if missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """
        self._defaultValueAttachment = None
        """ Primitive extension for defaultValueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueBase64Binary = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueBase64Binary = None
        """ Primitive extension for defaultValueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueBoolean = None
        """ Specified value if missing from instance.
        Type `bool`. """
        self._defaultValueBoolean = None
        """ Primitive extension for defaultValueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCanonical = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueCanonical = None
        """ Primitive extension for defaultValueCanonical. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCode = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueCode = None
        """ Primitive extension for defaultValueCode. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCodeableConcept = None
        """ Specified value if missing from instance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._defaultValueCodeableConcept = None
        """ Primitive extension for defaultValueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCoding = None
        """ Specified value if missing from instance.
        Type `Coding` (represented as `dict` in JSON). """
        self._defaultValueCoding = None
        """ Primitive extension for defaultValueCoding. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueContactDetail = None
        """ Specified value if missing from instance.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._defaultValueContactDetail = None
        """ Primitive extension for defaultValueContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueContactPoint = None
        """ Specified value if missing from instance.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._defaultValueContactPoint = None
        """ Primitive extension for defaultValueContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueContributor = None
        """ Specified value if missing from instance.
        Type `Contributor` (represented as `dict` in JSON). """
        self._defaultValueContributor = None
        """ Primitive extension for defaultValueContributor. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueCount = None
        """ Specified value if missing from instance.
        Type `Count` (represented as `dict` in JSON). """
        self._defaultValueCount = None
        """ Primitive extension for defaultValueCount. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDataRequirement = None
        """ Specified value if missing from instance.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._defaultValueDataRequirement = None
        """ Primitive extension for defaultValueDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDate = None
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._defaultValueDate = None
        """ Primitive extension for defaultValueDate. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDateTime = None
        """ Specified value if missing from instance.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._defaultValueDateTime = None
        """ Primitive extension for defaultValueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDecimal = None
        """ Specified value if missing from instance.
        Type `float`. """
        self._defaultValueDecimal = None
        """ Primitive extension for defaultValueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDistance = None
        """ Specified value if missing from instance.
        Type `Distance` (represented as `dict` in JSON). """
        self._defaultValueDistance = None
        """ Primitive extension for defaultValueDistance. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDosage = None
        """ Specified value if missing from instance.
        Type `Dosage` (represented as `dict` in JSON). """
        self._defaultValueDosage = None
        """ Primitive extension for defaultValueDosage. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueDuration = None
        """ Specified value if missing from instance.
        Type `Duration` (represented as `dict` in JSON). """
        self._defaultValueDuration = None
        """ Primitive extension for defaultValueDuration. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueExpression = None
        """ Specified value if missing from instance.
        Type `Expression` (represented as `dict` in JSON). """
        self._defaultValueExpression = None
        """ Primitive extension for defaultValueExpression. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueHumanName = None
        """ Specified value if missing from instance.
        Type `HumanName` (represented as `dict` in JSON). """
        self._defaultValueHumanName = None
        """ Primitive extension for defaultValueHumanName. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueId = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueId = None
        """ Primitive extension for defaultValueId. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueIdentifier = None
        """ Specified value if missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """
        self._defaultValueIdentifier = None
        """ Primitive extension for defaultValueIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueInstant = None
        """ Specified value if missing from instance.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._defaultValueInstant = None
        """ Primitive extension for defaultValueInstant. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueInteger = None
        """ Specified value if missing from instance.
        Type `int`. """
        self._defaultValueInteger = None
        """ Primitive extension for defaultValueInteger. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueMarkdown = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueMarkdown = None
        """ Primitive extension for defaultValueMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueMeta = None
        """ Specified value if missing from instance.
        Type `Meta` (represented as `dict` in JSON). """
        self._defaultValueMeta = None
        """ Primitive extension for defaultValueMeta. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueMoney = None
        """ Specified value if missing from instance.
        Type `Money` (represented as `dict` in JSON). """
        self._defaultValueMoney = None
        """ Primitive extension for defaultValueMoney. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueOid = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueOid = None
        """ Primitive extension for defaultValueOid. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueParameterDefinition = None
        """ Specified value if missing from instance.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._defaultValueParameterDefinition = None
        """ Primitive extension for defaultValueParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.defaultValuePeriod = None
        """ Specified value if missing from instance.
        Type `Period` (represented as `dict` in JSON). """
        self._defaultValuePeriod = None
        """ Primitive extension for defaultValuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.defaultValuePositiveInt = None
        """ Specified value if missing from instance.
        Type `int`. """
        self._defaultValuePositiveInt = None
        """ Primitive extension for defaultValuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueQuantity = None
        """ Specified value if missing from instance.
        Type `Quantity` (represented as `dict` in JSON). """
        self._defaultValueQuantity = None
        """ Primitive extension for defaultValueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueRange = None
        """ Specified value if missing from instance.
        Type `Range` (represented as `dict` in JSON). """
        self._defaultValueRange = None
        """ Primitive extension for defaultValueRange. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueRatio = None
        """ Specified value if missing from instance.
        Type `Ratio` (represented as `dict` in JSON). """
        self._defaultValueRatio = None
        """ Primitive extension for defaultValueRatio. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueReference = None
        """ Specified value if missing from instance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._defaultValueReference = None
        """ Primitive extension for defaultValueReference. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueRelatedArtifact = None
        """ Specified value if missing from instance.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._defaultValueRelatedArtifact = None
        """ Primitive extension for defaultValueRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueSampledData = None
        """ Specified value if missing from instance.
        Type `SampledData` (represented as `dict` in JSON). """
        self._defaultValueSampledData = None
        """ Primitive extension for defaultValueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueSignature = None
        """ Specified value if missing from instance.
        Type `Signature` (represented as `dict` in JSON). """
        self._defaultValueSignature = None
        """ Primitive extension for defaultValueSignature. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueString = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueString = None
        """ Primitive extension for defaultValueString. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueTime = None
        """ Specified value if missing from instance.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._defaultValueTime = None
        """ Primitive extension for defaultValueTime. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueTiming = None
        """ Specified value if missing from instance.
        Type `Timing` (represented as `dict` in JSON). """
        self._defaultValueTiming = None
        """ Primitive extension for defaultValueTiming. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueTriggerDefinition = None
        """ Specified value if missing from instance.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._defaultValueTriggerDefinition = None
        """ Primitive extension for defaultValueTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUnsignedInt = None
        """ Specified value if missing from instance.
        Type `int`. """
        self._defaultValueUnsignedInt = None
        """ Primitive extension for defaultValueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUri = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueUri = None
        """ Primitive extension for defaultValueUri. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUrl = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueUrl = None
        """ Primitive extension for defaultValueUrl. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUsageContext = None
        """ Specified value if missing from instance.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._defaultValueUsageContext = None
        """ Primitive extension for defaultValueUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.defaultValueUuid = None
        """ Specified value if missing from instance.
        Type `str`. """
        self._defaultValueUuid = None
        """ Primitive extension for defaultValueUuid. Type `FHIRPrimitiveExtension` """
        
        self.definition = None
        """ Full formal definition as narrative text.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.example = None
        """ Example value (as defined for type).
        List of `ElementDefinitionExample` items (represented as `dict` in JSON). """
        self._example = None
        """ Primitive extension for example. Type `FHIRPrimitiveExtension` """
        
        self.fixedAddress = None
        """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """
        self._fixedAddress = None
        """ Primitive extension for fixedAddress. Type `FHIRPrimitiveExtension` """
        
        self.fixedAge = None
        """ Value must be exactly this.
        Type `Age` (represented as `dict` in JSON). """
        self._fixedAge = None
        """ Primitive extension for fixedAge. Type `FHIRPrimitiveExtension` """
        
        self.fixedAnnotation = None
        """ Value must be exactly this.
        Type `Annotation` (represented as `dict` in JSON). """
        self._fixedAnnotation = None
        """ Primitive extension for fixedAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.fixedAttachment = None
        """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """
        self._fixedAttachment = None
        """ Primitive extension for fixedAttachment. Type `FHIRPrimitiveExtension` """
        
        self.fixedBase64Binary = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedBase64Binary = None
        """ Primitive extension for fixedBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.fixedBoolean = None
        """ Value must be exactly this.
        Type `bool`. """
        self._fixedBoolean = None
        """ Primitive extension for fixedBoolean. Type `FHIRPrimitiveExtension` """
        
        self.fixedCanonical = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedCanonical = None
        """ Primitive extension for fixedCanonical. Type `FHIRPrimitiveExtension` """
        
        self.fixedCode = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedCode = None
        """ Primitive extension for fixedCode. Type `FHIRPrimitiveExtension` """
        
        self.fixedCodeableConcept = None
        """ Value must be exactly this.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._fixedCodeableConcept = None
        """ Primitive extension for fixedCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.fixedCoding = None
        """ Value must be exactly this.
        Type `Coding` (represented as `dict` in JSON). """
        self._fixedCoding = None
        """ Primitive extension for fixedCoding. Type `FHIRPrimitiveExtension` """
        
        self.fixedContactDetail = None
        """ Value must be exactly this.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._fixedContactDetail = None
        """ Primitive extension for fixedContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.fixedContactPoint = None
        """ Value must be exactly this.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._fixedContactPoint = None
        """ Primitive extension for fixedContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.fixedContributor = None
        """ Value must be exactly this.
        Type `Contributor` (represented as `dict` in JSON). """
        self._fixedContributor = None
        """ Primitive extension for fixedContributor. Type `FHIRPrimitiveExtension` """
        
        self.fixedCount = None
        """ Value must be exactly this.
        Type `Count` (represented as `dict` in JSON). """
        self._fixedCount = None
        """ Primitive extension for fixedCount. Type `FHIRPrimitiveExtension` """
        
        self.fixedDataRequirement = None
        """ Value must be exactly this.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._fixedDataRequirement = None
        """ Primitive extension for fixedDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.fixedDate = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._fixedDate = None
        """ Primitive extension for fixedDate. Type `FHIRPrimitiveExtension` """
        
        self.fixedDateTime = None
        """ Value must be exactly this.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._fixedDateTime = None
        """ Primitive extension for fixedDateTime. Type `FHIRPrimitiveExtension` """
        
        self.fixedDecimal = None
        """ Value must be exactly this.
        Type `float`. """
        self._fixedDecimal = None
        """ Primitive extension for fixedDecimal. Type `FHIRPrimitiveExtension` """
        
        self.fixedDistance = None
        """ Value must be exactly this.
        Type `Distance` (represented as `dict` in JSON). """
        self._fixedDistance = None
        """ Primitive extension for fixedDistance. Type `FHIRPrimitiveExtension` """
        
        self.fixedDosage = None
        """ Value must be exactly this.
        Type `Dosage` (represented as `dict` in JSON). """
        self._fixedDosage = None
        """ Primitive extension for fixedDosage. Type `FHIRPrimitiveExtension` """
        
        self.fixedDuration = None
        """ Value must be exactly this.
        Type `Duration` (represented as `dict` in JSON). """
        self._fixedDuration = None
        """ Primitive extension for fixedDuration. Type `FHIRPrimitiveExtension` """
        
        self.fixedExpression = None
        """ Value must be exactly this.
        Type `Expression` (represented as `dict` in JSON). """
        self._fixedExpression = None
        """ Primitive extension for fixedExpression. Type `FHIRPrimitiveExtension` """
        
        self.fixedHumanName = None
        """ Value must be exactly this.
        Type `HumanName` (represented as `dict` in JSON). """
        self._fixedHumanName = None
        """ Primitive extension for fixedHumanName. Type `FHIRPrimitiveExtension` """
        
        self.fixedId = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedId = None
        """ Primitive extension for fixedId. Type `FHIRPrimitiveExtension` """
        
        self.fixedIdentifier = None
        """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """
        self._fixedIdentifier = None
        """ Primitive extension for fixedIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.fixedInstant = None
        """ Value must be exactly this.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._fixedInstant = None
        """ Primitive extension for fixedInstant. Type `FHIRPrimitiveExtension` """
        
        self.fixedInteger = None
        """ Value must be exactly this.
        Type `int`. """
        self._fixedInteger = None
        """ Primitive extension for fixedInteger. Type `FHIRPrimitiveExtension` """
        
        self.fixedMarkdown = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedMarkdown = None
        """ Primitive extension for fixedMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.fixedMeta = None
        """ Value must be exactly this.
        Type `Meta` (represented as `dict` in JSON). """
        self._fixedMeta = None
        """ Primitive extension for fixedMeta. Type `FHIRPrimitiveExtension` """
        
        self.fixedMoney = None
        """ Value must be exactly this.
        Type `Money` (represented as `dict` in JSON). """
        self._fixedMoney = None
        """ Primitive extension for fixedMoney. Type `FHIRPrimitiveExtension` """
        
        self.fixedOid = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedOid = None
        """ Primitive extension for fixedOid. Type `FHIRPrimitiveExtension` """
        
        self.fixedParameterDefinition = None
        """ Value must be exactly this.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._fixedParameterDefinition = None
        """ Primitive extension for fixedParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.fixedPeriod = None
        """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """
        self._fixedPeriod = None
        """ Primitive extension for fixedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.fixedPositiveInt = None
        """ Value must be exactly this.
        Type `int`. """
        self._fixedPositiveInt = None
        """ Primitive extension for fixedPositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.fixedQuantity = None
        """ Value must be exactly this.
        Type `Quantity` (represented as `dict` in JSON). """
        self._fixedQuantity = None
        """ Primitive extension for fixedQuantity. Type `FHIRPrimitiveExtension` """
        
        self.fixedRange = None
        """ Value must be exactly this.
        Type `Range` (represented as `dict` in JSON). """
        self._fixedRange = None
        """ Primitive extension for fixedRange. Type `FHIRPrimitiveExtension` """
        
        self.fixedRatio = None
        """ Value must be exactly this.
        Type `Ratio` (represented as `dict` in JSON). """
        self._fixedRatio = None
        """ Primitive extension for fixedRatio. Type `FHIRPrimitiveExtension` """
        
        self.fixedReference = None
        """ Value must be exactly this.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._fixedReference = None
        """ Primitive extension for fixedReference. Type `FHIRPrimitiveExtension` """
        
        self.fixedRelatedArtifact = None
        """ Value must be exactly this.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._fixedRelatedArtifact = None
        """ Primitive extension for fixedRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.fixedSampledData = None
        """ Value must be exactly this.
        Type `SampledData` (represented as `dict` in JSON). """
        self._fixedSampledData = None
        """ Primitive extension for fixedSampledData. Type `FHIRPrimitiveExtension` """
        
        self.fixedSignature = None
        """ Value must be exactly this.
        Type `Signature` (represented as `dict` in JSON). """
        self._fixedSignature = None
        """ Primitive extension for fixedSignature. Type `FHIRPrimitiveExtension` """
        
        self.fixedString = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedString = None
        """ Primitive extension for fixedString. Type `FHIRPrimitiveExtension` """
        
        self.fixedTime = None
        """ Value must be exactly this.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._fixedTime = None
        """ Primitive extension for fixedTime. Type `FHIRPrimitiveExtension` """
        
        self.fixedTiming = None
        """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """
        self._fixedTiming = None
        """ Primitive extension for fixedTiming. Type `FHIRPrimitiveExtension` """
        
        self.fixedTriggerDefinition = None
        """ Value must be exactly this.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._fixedTriggerDefinition = None
        """ Primitive extension for fixedTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.fixedUnsignedInt = None
        """ Value must be exactly this.
        Type `int`. """
        self._fixedUnsignedInt = None
        """ Primitive extension for fixedUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.fixedUri = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedUri = None
        """ Primitive extension for fixedUri. Type `FHIRPrimitiveExtension` """
        
        self.fixedUrl = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedUrl = None
        """ Primitive extension for fixedUrl. Type `FHIRPrimitiveExtension` """
        
        self.fixedUsageContext = None
        """ Value must be exactly this.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._fixedUsageContext = None
        """ Primitive extension for fixedUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.fixedUuid = None
        """ Value must be exactly this.
        Type `str`. """
        self._fixedUuid = None
        """ Primitive extension for fixedUuid. Type `FHIRPrimitiveExtension` """
        
        self.isModifier = None
        """ If this modifies the meaning of other elements.
        Type `bool`. """
        self._isModifier = None
        """ Primitive extension for isModifier. Type `FHIRPrimitiveExtension` """
        
        self.isModifierReason = None
        """ Reason that this element is marked as a modifier.
        Type `str`. """
        self._isModifierReason = None
        """ Primitive extension for isModifierReason. Type `FHIRPrimitiveExtension` """
        
        self.isSummary = None
        """ Include when _summary = true?.
        Type `bool`. """
        self._isSummary = None
        """ Primitive extension for isSummary. Type `FHIRPrimitiveExtension` """
        
        self.label = None
        """ Name for element to display with or prompt for element.
        Type `str`. """
        self._label = None
        """ Primitive extension for label. Type `FHIRPrimitiveExtension` """
        
        self.mapping = None
        """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """
        self._mapping = None
        """ Primitive extension for mapping. Type `FHIRPrimitiveExtension` """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        self._max = None
        """ Primitive extension for max. Type `FHIRPrimitiveExtension` """
        
        self.maxLength = None
        """ Max length for strings.
        Type `int`. """
        self._maxLength = None
        """ Primitive extension for maxLength. Type `FHIRPrimitiveExtension` """
        
        self.maxValueDate = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        self._maxValueDate = None
        """ Primitive extension for maxValueDate. Type `FHIRPrimitiveExtension` """
        
        self.maxValueDateTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._maxValueDateTime = None
        """ Primitive extension for maxValueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.maxValueDecimal = None
        """ Maximum Allowed Value (for some types).
        Type `float`. """
        self._maxValueDecimal = None
        """ Primitive extension for maxValueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.maxValueInstant = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._maxValueInstant = None
        """ Primitive extension for maxValueInstant. Type `FHIRPrimitiveExtension` """
        
        self.maxValueInteger = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        self._maxValueInteger = None
        """ Primitive extension for maxValueInteger. Type `FHIRPrimitiveExtension` """
        
        self.maxValuePositiveInt = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        self._maxValuePositiveInt = None
        """ Primitive extension for maxValuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.maxValueQuantity = None
        """ Maximum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        self._maxValueQuantity = None
        """ Primitive extension for maxValueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.maxValueTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRTime` (represented as `str` in JSON). """
        self._maxValueTime = None
        """ Primitive extension for maxValueTime. Type `FHIRPrimitiveExtension` """
        
        self.maxValueUnsignedInt = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        self._maxValueUnsignedInt = None
        """ Primitive extension for maxValueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.meaningWhenMissing = None
        """ Implicit meaning when this element is missing.
        Type `str`. """
        self._meaningWhenMissing = None
        """ Primitive extension for meaningWhenMissing. Type `FHIRPrimitiveExtension` """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        self._min = None
        """ Primitive extension for min. Type `FHIRPrimitiveExtension` """
        
        self.minValueDate = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        self._minValueDate = None
        """ Primitive extension for minValueDate. Type `FHIRPrimitiveExtension` """
        
        self.minValueDateTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._minValueDateTime = None
        """ Primitive extension for minValueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.minValueDecimal = None
        """ Minimum Allowed Value (for some types).
        Type `float`. """
        self._minValueDecimal = None
        """ Primitive extension for minValueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.minValueInstant = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._minValueInstant = None
        """ Primitive extension for minValueInstant. Type `FHIRPrimitiveExtension` """
        
        self.minValueInteger = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        self._minValueInteger = None
        """ Primitive extension for minValueInteger. Type `FHIRPrimitiveExtension` """
        
        self.minValuePositiveInt = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        self._minValuePositiveInt = None
        """ Primitive extension for minValuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.minValueQuantity = None
        """ Minimum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        self._minValueQuantity = None
        """ Primitive extension for minValueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.minValueTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRTime` (represented as `str` in JSON). """
        self._minValueTime = None
        """ Primitive extension for minValueTime. Type `FHIRPrimitiveExtension` """
        
        self.minValueUnsignedInt = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        self._minValueUnsignedInt = None
        """ Primitive extension for minValueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.mustSupport = None
        """ If the element must be supported.
        Type `bool`. """
        self._mustSupport = None
        """ Primitive extension for mustSupport. Type `FHIRPrimitiveExtension` """
        
        self.orderMeaning = None
        """ What the order of the elements means.
        Type `str`. """
        self._orderMeaning = None
        """ Primitive extension for orderMeaning. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ Path of the element in the hierarchy of elements.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        self.patternAddress = None
        """ Value must have at least these property values.
        Type `Address` (represented as `dict` in JSON). """
        self._patternAddress = None
        """ Primitive extension for patternAddress. Type `FHIRPrimitiveExtension` """
        
        self.patternAge = None
        """ Value must have at least these property values.
        Type `Age` (represented as `dict` in JSON). """
        self._patternAge = None
        """ Primitive extension for patternAge. Type `FHIRPrimitiveExtension` """
        
        self.patternAnnotation = None
        """ Value must have at least these property values.
        Type `Annotation` (represented as `dict` in JSON). """
        self._patternAnnotation = None
        """ Primitive extension for patternAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.patternAttachment = None
        """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """
        self._patternAttachment = None
        """ Primitive extension for patternAttachment. Type `FHIRPrimitiveExtension` """
        
        self.patternBase64Binary = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternBase64Binary = None
        """ Primitive extension for patternBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.patternBoolean = None
        """ Value must have at least these property values.
        Type `bool`. """
        self._patternBoolean = None
        """ Primitive extension for patternBoolean. Type `FHIRPrimitiveExtension` """
        
        self.patternCanonical = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternCanonical = None
        """ Primitive extension for patternCanonical. Type `FHIRPrimitiveExtension` """
        
        self.patternCode = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternCode = None
        """ Primitive extension for patternCode. Type `FHIRPrimitiveExtension` """
        
        self.patternCodeableConcept = None
        """ Value must have at least these property values.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._patternCodeableConcept = None
        """ Primitive extension for patternCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.patternCoding = None
        """ Value must have at least these property values.
        Type `Coding` (represented as `dict` in JSON). """
        self._patternCoding = None
        """ Primitive extension for patternCoding. Type `FHIRPrimitiveExtension` """
        
        self.patternContactDetail = None
        """ Value must have at least these property values.
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._patternContactDetail = None
        """ Primitive extension for patternContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.patternContactPoint = None
        """ Value must have at least these property values.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._patternContactPoint = None
        """ Primitive extension for patternContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.patternContributor = None
        """ Value must have at least these property values.
        Type `Contributor` (represented as `dict` in JSON). """
        self._patternContributor = None
        """ Primitive extension for patternContributor. Type `FHIRPrimitiveExtension` """
        
        self.patternCount = None
        """ Value must have at least these property values.
        Type `Count` (represented as `dict` in JSON). """
        self._patternCount = None
        """ Primitive extension for patternCount. Type `FHIRPrimitiveExtension` """
        
        self.patternDataRequirement = None
        """ Value must have at least these property values.
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._patternDataRequirement = None
        """ Primitive extension for patternDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.patternDate = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._patternDate = None
        """ Primitive extension for patternDate. Type `FHIRPrimitiveExtension` """
        
        self.patternDateTime = None
        """ Value must have at least these property values.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._patternDateTime = None
        """ Primitive extension for patternDateTime. Type `FHIRPrimitiveExtension` """
        
        self.patternDecimal = None
        """ Value must have at least these property values.
        Type `float`. """
        self._patternDecimal = None
        """ Primitive extension for patternDecimal. Type `FHIRPrimitiveExtension` """
        
        self.patternDistance = None
        """ Value must have at least these property values.
        Type `Distance` (represented as `dict` in JSON). """
        self._patternDistance = None
        """ Primitive extension for patternDistance. Type `FHIRPrimitiveExtension` """
        
        self.patternDosage = None
        """ Value must have at least these property values.
        Type `Dosage` (represented as `dict` in JSON). """
        self._patternDosage = None
        """ Primitive extension for patternDosage. Type `FHIRPrimitiveExtension` """
        
        self.patternDuration = None
        """ Value must have at least these property values.
        Type `Duration` (represented as `dict` in JSON). """
        self._patternDuration = None
        """ Primitive extension for patternDuration. Type `FHIRPrimitiveExtension` """
        
        self.patternExpression = None
        """ Value must have at least these property values.
        Type `Expression` (represented as `dict` in JSON). """
        self._patternExpression = None
        """ Primitive extension for patternExpression. Type `FHIRPrimitiveExtension` """
        
        self.patternHumanName = None
        """ Value must have at least these property values.
        Type `HumanName` (represented as `dict` in JSON). """
        self._patternHumanName = None
        """ Primitive extension for patternHumanName. Type `FHIRPrimitiveExtension` """
        
        self.patternId = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternId = None
        """ Primitive extension for patternId. Type `FHIRPrimitiveExtension` """
        
        self.patternIdentifier = None
        """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """
        self._patternIdentifier = None
        """ Primitive extension for patternIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.patternInstant = None
        """ Value must have at least these property values.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._patternInstant = None
        """ Primitive extension for patternInstant. Type `FHIRPrimitiveExtension` """
        
        self.patternInteger = None
        """ Value must have at least these property values.
        Type `int`. """
        self._patternInteger = None
        """ Primitive extension for patternInteger. Type `FHIRPrimitiveExtension` """
        
        self.patternMarkdown = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternMarkdown = None
        """ Primitive extension for patternMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.patternMeta = None
        """ Value must have at least these property values.
        Type `Meta` (represented as `dict` in JSON). """
        self._patternMeta = None
        """ Primitive extension for patternMeta. Type `FHIRPrimitiveExtension` """
        
        self.patternMoney = None
        """ Value must have at least these property values.
        Type `Money` (represented as `dict` in JSON). """
        self._patternMoney = None
        """ Primitive extension for patternMoney. Type `FHIRPrimitiveExtension` """
        
        self.patternOid = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternOid = None
        """ Primitive extension for patternOid. Type `FHIRPrimitiveExtension` """
        
        self.patternParameterDefinition = None
        """ Value must have at least these property values.
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._patternParameterDefinition = None
        """ Primitive extension for patternParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.patternPeriod = None
        """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """
        self._patternPeriod = None
        """ Primitive extension for patternPeriod. Type `FHIRPrimitiveExtension` """
        
        self.patternPositiveInt = None
        """ Value must have at least these property values.
        Type `int`. """
        self._patternPositiveInt = None
        """ Primitive extension for patternPositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.patternQuantity = None
        """ Value must have at least these property values.
        Type `Quantity` (represented as `dict` in JSON). """
        self._patternQuantity = None
        """ Primitive extension for patternQuantity. Type `FHIRPrimitiveExtension` """
        
        self.patternRange = None
        """ Value must have at least these property values.
        Type `Range` (represented as `dict` in JSON). """
        self._patternRange = None
        """ Primitive extension for patternRange. Type `FHIRPrimitiveExtension` """
        
        self.patternRatio = None
        """ Value must have at least these property values.
        Type `Ratio` (represented as `dict` in JSON). """
        self._patternRatio = None
        """ Primitive extension for patternRatio. Type `FHIRPrimitiveExtension` """
        
        self.patternReference = None
        """ Value must have at least these property values.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patternReference = None
        """ Primitive extension for patternReference. Type `FHIRPrimitiveExtension` """
        
        self.patternRelatedArtifact = None
        """ Value must have at least these property values.
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._patternRelatedArtifact = None
        """ Primitive extension for patternRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.patternSampledData = None
        """ Value must have at least these property values.
        Type `SampledData` (represented as `dict` in JSON). """
        self._patternSampledData = None
        """ Primitive extension for patternSampledData. Type `FHIRPrimitiveExtension` """
        
        self.patternSignature = None
        """ Value must have at least these property values.
        Type `Signature` (represented as `dict` in JSON). """
        self._patternSignature = None
        """ Primitive extension for patternSignature. Type `FHIRPrimitiveExtension` """
        
        self.patternString = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternString = None
        """ Primitive extension for patternString. Type `FHIRPrimitiveExtension` """
        
        self.patternTime = None
        """ Value must have at least these property values.
        Type `FHIRTime` (represented as `str` in JSON). """
        self._patternTime = None
        """ Primitive extension for patternTime. Type `FHIRPrimitiveExtension` """
        
        self.patternTiming = None
        """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """
        self._patternTiming = None
        """ Primitive extension for patternTiming. Type `FHIRPrimitiveExtension` """
        
        self.patternTriggerDefinition = None
        """ Value must have at least these property values.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._patternTriggerDefinition = None
        """ Primitive extension for patternTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.patternUnsignedInt = None
        """ Value must have at least these property values.
        Type `int`. """
        self._patternUnsignedInt = None
        """ Primitive extension for patternUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.patternUri = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternUri = None
        """ Primitive extension for patternUri. Type `FHIRPrimitiveExtension` """
        
        self.patternUrl = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternUrl = None
        """ Primitive extension for patternUrl. Type `FHIRPrimitiveExtension` """
        
        self.patternUsageContext = None
        """ Value must have at least these property values.
        Type `UsageContext` (represented as `dict` in JSON). """
        self._patternUsageContext = None
        """ Primitive extension for patternUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.patternUuid = None
        """ Value must have at least these property values.
        Type `str`. """
        self._patternUuid = None
        """ Primitive extension for patternUuid. Type `FHIRPrimitiveExtension` """
        
        self.representation = None
        """ xmlAttr | xmlText | typeAttr | cdaText | xhtml.
        List of `str` items. """
        self._representation = None
        """ Primitive extension for representation. Type `FHIRPrimitiveExtension` """
        
        self.requirements = None
        """ Why this resource has been created.
        Type `str`. """
        self._requirements = None
        """ Primitive extension for requirements. Type `FHIRPrimitiveExtension` """
        
        self.short = None
        """ Concise definition for space-constrained presentation.
        Type `str`. """
        self._short = None
        """ Primitive extension for short. Type `FHIRPrimitiveExtension` """
        
        self.sliceIsConstraining = None
        """ If this slice definition constrains an inherited slice definition
        (or not).
        Type `bool`. """
        self._sliceIsConstraining = None
        """ Primitive extension for sliceIsConstraining. Type `FHIRPrimitiveExtension` """
        
        self.sliceName = None
        """ Name for this particular element (in a set of slices).
        Type `str`. """
        self._sliceName = None
        """ Primitive extension for sliceName. Type `FHIRPrimitiveExtension` """
        
        self.slicing = None
        """ This element is sliced - slices follow.
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """
        self._slicing = None
        """ Primitive extension for slicing. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("_alias", "_alias", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("_base", "_base", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("_binding", "_binding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("_constraint", "_constraint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentReference", "contentReference", str, False, None, False),
            ("_contentReference", "_contentReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("_defaultValueAddress", "_defaultValueAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAge", "defaultValueAge", age.Age, False, "defaultValue", False),
            ("_defaultValueAge", "_defaultValueAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("_defaultValueAnnotation", "_defaultValueAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("_defaultValueAttachment", "_defaultValueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("_defaultValueBase64Binary", "_defaultValueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("_defaultValueBoolean", "_defaultValueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCanonical", "defaultValueCanonical", str, False, "defaultValue", False),
            ("_defaultValueCanonical", "_defaultValueCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("_defaultValueCode", "_defaultValueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("_defaultValueCodeableConcept", "_defaultValueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("_defaultValueCoding", "_defaultValueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueContactDetail", "defaultValueContactDetail", contactdetail.ContactDetail, False, "defaultValue", False),
            ("_defaultValueContactDetail", "_defaultValueContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("_defaultValueContactPoint", "_defaultValueContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueContributor", "defaultValueContributor", contributor.Contributor, False, "defaultValue", False),
            ("_defaultValueContributor", "_defaultValueContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueCount", "defaultValueCount", count.Count, False, "defaultValue", False),
            ("_defaultValueCount", "_defaultValueCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDataRequirement", "defaultValueDataRequirement", datarequirement.DataRequirement, False, "defaultValue", False),
            ("_defaultValueDataRequirement", "_defaultValueDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("_defaultValueDate", "_defaultValueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdatetime.FHIRDateTime, False, "defaultValue", False),
            ("_defaultValueDateTime", "_defaultValueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("_defaultValueDecimal", "_defaultValueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDistance", "defaultValueDistance", distance.Distance, False, "defaultValue", False),
            ("_defaultValueDistance", "_defaultValueDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDosage", "defaultValueDosage", dosage.Dosage, False, "defaultValue", False),
            ("_defaultValueDosage", "_defaultValueDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueDuration", "defaultValueDuration", duration.Duration, False, "defaultValue", False),
            ("_defaultValueDuration", "_defaultValueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueExpression", "defaultValueExpression", expression.Expression, False, "defaultValue", False),
            ("_defaultValueExpression", "_defaultValueExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("_defaultValueHumanName", "_defaultValueHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("_defaultValueId", "_defaultValueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("_defaultValueIdentifier", "_defaultValueIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueInstant", "defaultValueInstant", fhirinstant.FHIRInstant, False, "defaultValue", False),
            ("_defaultValueInstant", "_defaultValueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("_defaultValueInteger", "_defaultValueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("_defaultValueMarkdown", "_defaultValueMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueMeta", "defaultValueMeta", meta.Meta, False, "defaultValue", False),
            ("_defaultValueMeta", "_defaultValueMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueMoney", "defaultValueMoney", money.Money, False, "defaultValue", False),
            ("_defaultValueMoney", "_defaultValueMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("_defaultValueOid", "_defaultValueOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueParameterDefinition", "defaultValueParameterDefinition", parameterdefinition.ParameterDefinition, False, "defaultValue", False),
            ("_defaultValueParameterDefinition", "_defaultValueParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("_defaultValuePeriod", "_defaultValuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("_defaultValuePositiveInt", "_defaultValuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("_defaultValueQuantity", "_defaultValueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("_defaultValueRange", "_defaultValueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("_defaultValueRatio", "_defaultValueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("_defaultValueReference", "_defaultValueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueRelatedArtifact", "defaultValueRelatedArtifact", relatedartifact.RelatedArtifact, False, "defaultValue", False),
            ("_defaultValueRelatedArtifact", "_defaultValueRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("_defaultValueSampledData", "_defaultValueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("_defaultValueSignature", "_defaultValueSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("_defaultValueString", "_defaultValueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueTime", "defaultValueTime", fhirtime.FHIRTime, False, "defaultValue", False),
            ("_defaultValueTime", "_defaultValueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("_defaultValueTiming", "_defaultValueTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueTriggerDefinition", "defaultValueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "defaultValue", False),
            ("_defaultValueTriggerDefinition", "_defaultValueTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("_defaultValueUnsignedInt", "_defaultValueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("_defaultValueUri", "_defaultValueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUrl", "defaultValueUrl", str, False, "defaultValue", False),
            ("_defaultValueUrl", "_defaultValueUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUsageContext", "defaultValueUsageContext", usagecontext.UsageContext, False, "defaultValue", False),
            ("_defaultValueUsageContext", "_defaultValueUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("defaultValueUuid", "defaultValueUuid", str, False, "defaultValue", False),
            ("_defaultValueUuid", "_defaultValueUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("example", "example", ElementDefinitionExample, True, None, False),
            ("_example", "_example", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedAddress", "fixedAddress", address.Address, False, "fixed", False),
            ("_fixedAddress", "_fixedAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedAge", "fixedAge", age.Age, False, "fixed", False),
            ("_fixedAge", "_fixedAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedAnnotation", "fixedAnnotation", annotation.Annotation, False, "fixed", False),
            ("_fixedAnnotation", "_fixedAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False, "fixed", False),
            ("_fixedAttachment", "_fixedAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("_fixedBase64Binary", "_fixedBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("_fixedBoolean", "_fixedBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedCanonical", "fixedCanonical", str, False, "fixed", False),
            ("_fixedCanonical", "_fixedCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("_fixedCode", "_fixedCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False, "fixed", False),
            ("_fixedCodeableConcept", "_fixedCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedCoding", "fixedCoding", coding.Coding, False, "fixed", False),
            ("_fixedCoding", "_fixedCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedContactDetail", "fixedContactDetail", contactdetail.ContactDetail, False, "fixed", False),
            ("_fixedContactDetail", "_fixedContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False, "fixed", False),
            ("_fixedContactPoint", "_fixedContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedContributor", "fixedContributor", contributor.Contributor, False, "fixed", False),
            ("_fixedContributor", "_fixedContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedCount", "fixedCount", count.Count, False, "fixed", False),
            ("_fixedCount", "_fixedCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedDataRequirement", "fixedDataRequirement", datarequirement.DataRequirement, False, "fixed", False),
            ("_fixedDataRequirement", "_fixedDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedDate", "fixedDate", fhirdate.FHIRDate, False, "fixed", False),
            ("_fixedDate", "_fixedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedDateTime", "fixedDateTime", fhirdatetime.FHIRDateTime, False, "fixed", False),
            ("_fixedDateTime", "_fixedDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("_fixedDecimal", "_fixedDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedDistance", "fixedDistance", distance.Distance, False, "fixed", False),
            ("_fixedDistance", "_fixedDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedDosage", "fixedDosage", dosage.Dosage, False, "fixed", False),
            ("_fixedDosage", "_fixedDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedDuration", "fixedDuration", duration.Duration, False, "fixed", False),
            ("_fixedDuration", "_fixedDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedExpression", "fixedExpression", expression.Expression, False, "fixed", False),
            ("_fixedExpression", "_fixedExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False, "fixed", False),
            ("_fixedHumanName", "_fixedHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("_fixedId", "_fixedId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False, "fixed", False),
            ("_fixedIdentifier", "_fixedIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedInstant", "fixedInstant", fhirinstant.FHIRInstant, False, "fixed", False),
            ("_fixedInstant", "_fixedInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("_fixedInteger", "_fixedInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("_fixedMarkdown", "_fixedMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedMeta", "fixedMeta", meta.Meta, False, "fixed", False),
            ("_fixedMeta", "_fixedMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedMoney", "fixedMoney", money.Money, False, "fixed", False),
            ("_fixedMoney", "_fixedMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("_fixedOid", "_fixedOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedParameterDefinition", "fixedParameterDefinition", parameterdefinition.ParameterDefinition, False, "fixed", False),
            ("_fixedParameterDefinition", "_fixedParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedPeriod", "fixedPeriod", period.Period, False, "fixed", False),
            ("_fixedPeriod", "_fixedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("_fixedPositiveInt", "_fixedPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False, "fixed", False),
            ("_fixedQuantity", "_fixedQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedRange", "fixedRange", range.Range, False, "fixed", False),
            ("_fixedRange", "_fixedRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedRatio", "fixedRatio", ratio.Ratio, False, "fixed", False),
            ("_fixedRatio", "_fixedRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False, "fixed", False),
            ("_fixedReference", "_fixedReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedRelatedArtifact", "fixedRelatedArtifact", relatedartifact.RelatedArtifact, False, "fixed", False),
            ("_fixedRelatedArtifact", "_fixedRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedSampledData", "fixedSampledData", sampleddata.SampledData, False, "fixed", False),
            ("_fixedSampledData", "_fixedSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedSignature", "fixedSignature", signature.Signature, False, "fixed", False),
            ("_fixedSignature", "_fixedSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("_fixedString", "_fixedString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedTime", "fixedTime", fhirtime.FHIRTime, False, "fixed", False),
            ("_fixedTime", "_fixedTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedTiming", "fixedTiming", timing.Timing, False, "fixed", False),
            ("_fixedTiming", "_fixedTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedTriggerDefinition", "fixedTriggerDefinition", triggerdefinition.TriggerDefinition, False, "fixed", False),
            ("_fixedTriggerDefinition", "_fixedTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("_fixedUnsignedInt", "_fixedUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("_fixedUri", "_fixedUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedUrl", "fixedUrl", str, False, "fixed", False),
            ("_fixedUrl", "_fixedUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedUsageContext", "fixedUsageContext", usagecontext.UsageContext, False, "fixed", False),
            ("_fixedUsageContext", "_fixedUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("fixedUuid", "fixedUuid", str, False, "fixed", False),
            ("_fixedUuid", "_fixedUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("_isModifier", "_isModifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isModifierReason", "isModifierReason", str, False, None, False),
            ("_isModifierReason", "_isModifierReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("_isSummary", "_isSummary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("label", "label", str, False, None, False),
            ("_label", "_label", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
            ("_mapping", "_mapping", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("max", "max", str, False, None, False),
            ("_max", "_max", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("_maxLength", "_maxLength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueDate", "maxValueDate", fhirdate.FHIRDate, False, "maxValue", False),
            ("_maxValueDate", "_maxValueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueDateTime", "maxValueDateTime", fhirdatetime.FHIRDateTime, False, "maxValue", False),
            ("_maxValueDateTime", "_maxValueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("_maxValueDecimal", "_maxValueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueInstant", "maxValueInstant", fhirinstant.FHIRInstant, False, "maxValue", False),
            ("_maxValueInstant", "_maxValueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("_maxValueInteger", "_maxValueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("_maxValuePositiveInt", "_maxValuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueQuantity", "maxValueQuantity", quantity.Quantity, False, "maxValue", False),
            ("_maxValueQuantity", "_maxValueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueTime", "maxValueTime", fhirtime.FHIRTime, False, "maxValue", False),
            ("_maxValueTime", "_maxValueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("_maxValueUnsignedInt", "_maxValueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("_meaningWhenMissing", "_meaningWhenMissing", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("min", "min", int, False, None, False),
            ("_min", "_min", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueDate", "minValueDate", fhirdate.FHIRDate, False, "minValue", False),
            ("_minValueDate", "_minValueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueDateTime", "minValueDateTime", fhirdatetime.FHIRDateTime, False, "minValue", False),
            ("_minValueDateTime", "_minValueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("_minValueDecimal", "_minValueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueInstant", "minValueInstant", fhirinstant.FHIRInstant, False, "minValue", False),
            ("_minValueInstant", "_minValueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("_minValueInteger", "_minValueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("_minValuePositiveInt", "_minValuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueQuantity", "minValueQuantity", quantity.Quantity, False, "minValue", False),
            ("_minValueQuantity", "_minValueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueTime", "minValueTime", fhirtime.FHIRTime, False, "minValue", False),
            ("_minValueTime", "_minValueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("_minValueUnsignedInt", "_minValueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("_mustSupport", "_mustSupport", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orderMeaning", "orderMeaning", str, False, None, False),
            ("_orderMeaning", "_orderMeaning", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, True),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternAddress", "patternAddress", address.Address, False, "pattern", False),
            ("_patternAddress", "_patternAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternAge", "patternAge", age.Age, False, "pattern", False),
            ("_patternAge", "_patternAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternAnnotation", "patternAnnotation", annotation.Annotation, False, "pattern", False),
            ("_patternAnnotation", "_patternAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternAttachment", "patternAttachment", attachment.Attachment, False, "pattern", False),
            ("_patternAttachment", "_patternAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("_patternBase64Binary", "_patternBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("_patternBoolean", "_patternBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternCanonical", "patternCanonical", str, False, "pattern", False),
            ("_patternCanonical", "_patternCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("_patternCode", "_patternCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False, "pattern", False),
            ("_patternCodeableConcept", "_patternCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternCoding", "patternCoding", coding.Coding, False, "pattern", False),
            ("_patternCoding", "_patternCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternContactDetail", "patternContactDetail", contactdetail.ContactDetail, False, "pattern", False),
            ("_patternContactDetail", "_patternContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False, "pattern", False),
            ("_patternContactPoint", "_patternContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternContributor", "patternContributor", contributor.Contributor, False, "pattern", False),
            ("_patternContributor", "_patternContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternCount", "patternCount", count.Count, False, "pattern", False),
            ("_patternCount", "_patternCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternDataRequirement", "patternDataRequirement", datarequirement.DataRequirement, False, "pattern", False),
            ("_patternDataRequirement", "_patternDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternDate", "patternDate", fhirdate.FHIRDate, False, "pattern", False),
            ("_patternDate", "_patternDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternDateTime", "patternDateTime", fhirdatetime.FHIRDateTime, False, "pattern", False),
            ("_patternDateTime", "_patternDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("_patternDecimal", "_patternDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternDistance", "patternDistance", distance.Distance, False, "pattern", False),
            ("_patternDistance", "_patternDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternDosage", "patternDosage", dosage.Dosage, False, "pattern", False),
            ("_patternDosage", "_patternDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternDuration", "patternDuration", duration.Duration, False, "pattern", False),
            ("_patternDuration", "_patternDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternExpression", "patternExpression", expression.Expression, False, "pattern", False),
            ("_patternExpression", "_patternExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternHumanName", "patternHumanName", humanname.HumanName, False, "pattern", False),
            ("_patternHumanName", "_patternHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("_patternId", "_patternId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False, "pattern", False),
            ("_patternIdentifier", "_patternIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternInstant", "patternInstant", fhirinstant.FHIRInstant, False, "pattern", False),
            ("_patternInstant", "_patternInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("_patternInteger", "_patternInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("_patternMarkdown", "_patternMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternMeta", "patternMeta", meta.Meta, False, "pattern", False),
            ("_patternMeta", "_patternMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternMoney", "patternMoney", money.Money, False, "pattern", False),
            ("_patternMoney", "_patternMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("_patternOid", "_patternOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternParameterDefinition", "patternParameterDefinition", parameterdefinition.ParameterDefinition, False, "pattern", False),
            ("_patternParameterDefinition", "_patternParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternPeriod", "patternPeriod", period.Period, False, "pattern", False),
            ("_patternPeriod", "_patternPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("_patternPositiveInt", "_patternPositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternQuantity", "patternQuantity", quantity.Quantity, False, "pattern", False),
            ("_patternQuantity", "_patternQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternRange", "patternRange", range.Range, False, "pattern", False),
            ("_patternRange", "_patternRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternRatio", "patternRatio", ratio.Ratio, False, "pattern", False),
            ("_patternRatio", "_patternRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternReference", "patternReference", fhirreference.FHIRReference, False, "pattern", False),
            ("_patternReference", "_patternReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternRelatedArtifact", "patternRelatedArtifact", relatedartifact.RelatedArtifact, False, "pattern", False),
            ("_patternRelatedArtifact", "_patternRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternSampledData", "patternSampledData", sampleddata.SampledData, False, "pattern", False),
            ("_patternSampledData", "_patternSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternSignature", "patternSignature", signature.Signature, False, "pattern", False),
            ("_patternSignature", "_patternSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("_patternString", "_patternString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternTime", "patternTime", fhirtime.FHIRTime, False, "pattern", False),
            ("_patternTime", "_patternTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternTiming", "patternTiming", timing.Timing, False, "pattern", False),
            ("_patternTiming", "_patternTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternTriggerDefinition", "patternTriggerDefinition", triggerdefinition.TriggerDefinition, False, "pattern", False),
            ("_patternTriggerDefinition", "_patternTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("_patternUnsignedInt", "_patternUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("_patternUri", "_patternUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternUrl", "patternUrl", str, False, "pattern", False),
            ("_patternUrl", "_patternUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternUsageContext", "patternUsageContext", usagecontext.UsageContext, False, "pattern", False),
            ("_patternUsageContext", "_patternUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patternUuid", "patternUuid", str, False, "pattern", False),
            ("_patternUuid", "_patternUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("representation", "representation", str, True, None, False),
            ("_representation", "_representation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("_requirements", "_requirements", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("short", "short", str, False, None, False),
            ("_short", "_short", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sliceIsConstraining", "sliceIsConstraining", bool, False, None, False),
            ("_sliceIsConstraining", "_sliceIsConstraining", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sliceName", "sliceName", str, False, None, False),
            ("_sliceName", "_sliceName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False),
            ("_slicing", "_slicing", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", ElementDefinitionType, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import element

class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.
    
    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. When the element definition is not the
    original definition of an element - i.g. either in a constraint on another
    type, or for elements from a super type in a snap shot - then the
    information in provided in the element definition may be different to the
    base definition. On the original definition of the element, it will be
    same.
    """
    
    resource_type = "ElementDefinitionBase"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.max = None
        """ Max cardinality of the base element.
        Type `str`. """
        self._max = None
        """ Primitive extension for max. Type `FHIRPrimitiveExtension` """
        
        self.min = None
        """ Min cardinality of the base element.
        Type `int`. """
        self._min = None
        """ Primitive extension for min. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ Path that identifies the base element.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionBase, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend([
            ("max", "max", str, False, None, True),
            ("_max", "_max", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("min", "min", int, False, None, True),
            ("_min", "_min", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, True),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """
    
    resource_type = "ElementDefinitionBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Human explanation of the value set.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.strength = None
        """ required | extensible | preferred | example.
        Type `str`. """
        self._strength = None
        """ Primitive extension for strength. Type `FHIRPrimitiveExtension` """
        
        self.valueSet = None
        """ Source of value set.
        Type `str`. """
        self._valueSet = None
        """ Primitive extension for valueSet. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("strength", "strength", str, False, None, True),
            ("_strength", "_strength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
            ("_valueSet", "_valueSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.
    
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    
    resource_type = "ElementDefinitionConstraint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ FHIRPath expression of constraint.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.human = None
        """ Human description of constraint.
        Type `str`. """
        self._human = None
        """ Primitive extension for human. Type `FHIRPrimitiveExtension` """
        
        self.key = None
        """ Target of 'condition' reference above.
        Type `str`. """
        self._key = None
        """ Primitive extension for key. Type `FHIRPrimitiveExtension` """
        
        self.requirements = None
        """ Why this constraint is necessary or appropriate.
        Type `str`. """
        self._requirements = None
        """ Primitive extension for requirements. Type `FHIRPrimitiveExtension` """
        
        self.severity = None
        """ error | warning.
        Type `str`. """
        self._severity = None
        """ Primitive extension for severity. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Reference to original source of constraint.
        Type `str`. """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.xpath = None
        """ XPath expression of constraint.
        Type `str`. """
        self._xpath = None
        """ Primitive extension for xpath. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionConstraint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("human", "human", str, False, None, True),
            ("_human", "_human", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("key", "key", str, False, None, True),
            ("_key", "_key", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("_requirements", "_requirements", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("_severity", "_severity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", str, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("xpath", "xpath", str, False, None, False),
            ("_xpath", "_xpath", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ElementDefinitionExample(element.Element):
    """ Example value (as defined for type).
    
    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """
    
    resource_type = "ElementDefinitionExample"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.label = None
        """ Describes the purpose of this example.
        Type `str`. """
        self._label = None
        """ Primitive extension for label. Type `FHIRPrimitiveExtension` """
        
        self.valueAddress = None
        """ Value of Example (one of allowed types).
        Type `Address` (represented as `dict` in JSON). """
        self._valueAddress = None
        """ Primitive extension for valueAddress. Type `FHIRPrimitiveExtension` """
        
        self.valueAge = None
        """ Value of Example (one of allowed types).
        Type `Age` (represented as `dict` in JSON). """
        self._valueAge = None
        """ Primitive extension for valueAge. Type `FHIRPrimitiveExtension` """
        
        self.valueAnnotation = None
        """ Value of Example (one of allowed types).
        Type `Annotation` (represented as `dict` in JSON). """
        self._valueAnnotation = None
        """ Primitive extension for valueAnnotation. Type `FHIRPrimitiveExtension` """
        
        self.valueAttachment = None
        """ Value of Example (one of allowed types).
        Type `Attachment` (represented as `dict` in JSON). """
        self._valueAttachment = None
        """ Primitive extension for valueAttachment. Type `FHIRPrimitiveExtension` """
        
        self.valueBase64Binary = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueBase64Binary = None
        """ Primitive extension for valueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Value of Example (one of allowed types).
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCanonical = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueCanonical = None
        """ Primitive extension for valueCanonical. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Value of Example (one of allowed types).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueCoding = None
        """ Value of Example (one of allowed types).
        Type `Coding` (represented as `dict` in JSON). """
        self._valueCoding = None
        """ Primitive extension for valueCoding. Type `FHIRPrimitiveExtension` """
        
        self.valueContactDetail = None
        """ Value of Example (one of allowed types).
        Type `ContactDetail` (represented as `dict` in JSON). """
        self._valueContactDetail = None
        """ Primitive extension for valueContactDetail. Type `FHIRPrimitiveExtension` """
        
        self.valueContactPoint = None
        """ Value of Example (one of allowed types).
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._valueContactPoint = None
        """ Primitive extension for valueContactPoint. Type `FHIRPrimitiveExtension` """
        
        self.valueContributor = None
        """ Value of Example (one of allowed types).
        Type `Contributor` (represented as `dict` in JSON). """
        self._valueContributor = None
        """ Primitive extension for valueContributor. Type `FHIRPrimitiveExtension` """
        
        self.valueCount = None
        """ Value of Example (one of allowed types).
        Type `Count` (represented as `dict` in JSON). """
        self._valueCount = None
        """ Primitive extension for valueCount. Type `FHIRPrimitiveExtension` """
        
        self.valueDataRequirement = None
        """ Value of Example (one of allowed types).
        Type `DataRequirement` (represented as `dict` in JSON). """
        self._valueDataRequirement = None
        """ Primitive extension for valueDataRequirement. Type `FHIRPrimitiveExtension` """
        
        self.valueDate = None
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """
        self._valueDate = None
        """ Primitive extension for valueDate. Type `FHIRPrimitiveExtension` """
        
        self.valueDateTime = None
        """ Value of Example (one of allowed types).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._valueDateTime = None
        """ Primitive extension for valueDateTime. Type `FHIRPrimitiveExtension` """
        
        self.valueDecimal = None
        """ Value of Example (one of allowed types).
        Type `float`. """
        self._valueDecimal = None
        """ Primitive extension for valueDecimal. Type `FHIRPrimitiveExtension` """
        
        self.valueDistance = None
        """ Value of Example (one of allowed types).
        Type `Distance` (represented as `dict` in JSON). """
        self._valueDistance = None
        """ Primitive extension for valueDistance. Type `FHIRPrimitiveExtension` """
        
        self.valueDosage = None
        """ Value of Example (one of allowed types).
        Type `Dosage` (represented as `dict` in JSON). """
        self._valueDosage = None
        """ Primitive extension for valueDosage. Type `FHIRPrimitiveExtension` """
        
        self.valueDuration = None
        """ Value of Example (one of allowed types).
        Type `Duration` (represented as `dict` in JSON). """
        self._valueDuration = None
        """ Primitive extension for valueDuration. Type `FHIRPrimitiveExtension` """
        
        self.valueExpression = None
        """ Value of Example (one of allowed types).
        Type `Expression` (represented as `dict` in JSON). """
        self._valueExpression = None
        """ Primitive extension for valueExpression. Type `FHIRPrimitiveExtension` """
        
        self.valueHumanName = None
        """ Value of Example (one of allowed types).
        Type `HumanName` (represented as `dict` in JSON). """
        self._valueHumanName = None
        """ Primitive extension for valueHumanName. Type `FHIRPrimitiveExtension` """
        
        self.valueId = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueId = None
        """ Primitive extension for valueId. Type `FHIRPrimitiveExtension` """
        
        self.valueIdentifier = None
        """ Value of Example (one of allowed types).
        Type `Identifier` (represented as `dict` in JSON). """
        self._valueIdentifier = None
        """ Primitive extension for valueIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.valueInstant = None
        """ Value of Example (one of allowed types).
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._valueInstant = None
        """ Primitive extension for valueInstant. Type `FHIRPrimitiveExtension` """
        
        self.valueInteger = None
        """ Value of Example (one of allowed types).
        Type `int`. """
        self._valueInteger = None
        """ Primitive extension for valueInteger. Type `FHIRPrimitiveExtension` """
        
        self.valueMarkdown = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueMarkdown = None
        """ Primitive extension for valueMarkdown. Type `FHIRPrimitiveExtension` """
        
        self.valueMeta = None
        """ Value of Example (one of allowed types).
        Type `Meta` (represented as `dict` in JSON). """
        self._valueMeta = None
        """ Primitive extension for valueMeta. Type `FHIRPrimitiveExtension` """
        
        self.valueMoney = None
        """ Value of Example (one of allowed types).
        Type `Money` (represented as `dict` in JSON). """
        self._valueMoney = None
        """ Primitive extension for valueMoney. Type `FHIRPrimitiveExtension` """
        
        self.valueOid = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueOid = None
        """ Primitive extension for valueOid. Type `FHIRPrimitiveExtension` """
        
        self.valueParameterDefinition = None
        """ Value of Example (one of allowed types).
        Type `ParameterDefinition` (represented as `dict` in JSON). """
        self._valueParameterDefinition = None
        """ Primitive extension for valueParameterDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valuePeriod = None
        """ Value of Example (one of allowed types).
        Type `Period` (represented as `dict` in JSON). """
        self._valuePeriod = None
        """ Primitive extension for valuePeriod. Type `FHIRPrimitiveExtension` """
        
        self.valuePositiveInt = None
        """ Value of Example (one of allowed types).
        Type `int`. """
        self._valuePositiveInt = None
        """ Primitive extension for valuePositiveInt. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Value of Example (one of allowed types).
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Value of Example (one of allowed types).
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueRatio = None
        """ Value of Example (one of allowed types).
        Type `Ratio` (represented as `dict` in JSON). """
        self._valueRatio = None
        """ Primitive extension for valueRatio. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Value of Example (one of allowed types).
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        self.valueRelatedArtifact = None
        """ Value of Example (one of allowed types).
        Type `RelatedArtifact` (represented as `dict` in JSON). """
        self._valueRelatedArtifact = None
        """ Primitive extension for valueRelatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.valueSampledData = None
        """ Value of Example (one of allowed types).
        Type `SampledData` (represented as `dict` in JSON). """
        self._valueSampledData = None
        """ Primitive extension for valueSampledData. Type `FHIRPrimitiveExtension` """
        
        self.valueSignature = None
        """ Value of Example (one of allowed types).
        Type `Signature` (represented as `dict` in JSON). """
        self._valueSignature = None
        """ Primitive extension for valueSignature. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        self.valueTime = None
        """ Value of Example (one of allowed types).
        Type `FHIRTime` (represented as `str` in JSON). """
        self._valueTime = None
        """ Primitive extension for valueTime. Type `FHIRPrimitiveExtension` """
        
        self.valueTiming = None
        """ Value of Example (one of allowed types).
        Type `Timing` (represented as `dict` in JSON). """
        self._valueTiming = None
        """ Primitive extension for valueTiming. Type `FHIRPrimitiveExtension` """
        
        self.valueTriggerDefinition = None
        """ Value of Example (one of allowed types).
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        self._valueTriggerDefinition = None
        """ Primitive extension for valueTriggerDefinition. Type `FHIRPrimitiveExtension` """
        
        self.valueUnsignedInt = None
        """ Value of Example (one of allowed types).
        Type `int`. """
        self._valueUnsignedInt = None
        """ Primitive extension for valueUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.valueUri = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueUri = None
        """ Primitive extension for valueUri. Type `FHIRPrimitiveExtension` """
        
        self.valueUrl = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueUrl = None
        """ Primitive extension for valueUrl. Type `FHIRPrimitiveExtension` """
        
        self.valueUsageContext = None
        """ Value of Example (one of allowed types).
        Type `UsageContext` (represented as `dict` in JSON). """
        self._valueUsageContext = None
        """ Primitive extension for valueUsageContext. Type `FHIRPrimitiveExtension` """
        
        self.valueUuid = None
        """ Value of Example (one of allowed types).
        Type `str`. """
        self._valueUuid = None
        """ Primitive extension for valueUuid. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionExample, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend([
            ("label", "label", str, False, None, True),
            ("_label", "_label", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("_valueAddress", "_valueAddress", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("_valueAge", "_valueAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("_valueAnnotation", "_valueAnnotation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("_valueAttachment", "_valueAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("_valueBase64Binary", "_valueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCanonical", "valueCanonical", str, False, "value", True),
            ("_valueCanonical", "_valueCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", str, False, "value", True),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("_valueCoding", "_valueCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactDetail", "valueContactDetail", contactdetail.ContactDetail, False, "value", True),
            ("_valueContactDetail", "_valueContactDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("_valueContactPoint", "_valueContactPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueContributor", "valueContributor", contributor.Contributor, False, "value", True),
            ("_valueContributor", "_valueContributor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("_valueCount", "_valueCount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDataRequirement", "valueDataRequirement", datarequirement.DataRequirement, False, "value", True),
            ("_valueDataRequirement", "_valueDataRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("_valueDate", "_valueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDateTime", "valueDateTime", fhirdatetime.FHIRDateTime, False, "value", True),
            ("_valueDateTime", "_valueDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("_valueDecimal", "_valueDecimal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("_valueDistance", "_valueDistance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDosage", "valueDosage", dosage.Dosage, False, "value", True),
            ("_valueDosage", "_valueDosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("_valueDuration", "_valueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueExpression", "valueExpression", expression.Expression, False, "value", True),
            ("_valueExpression", "_valueExpression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("_valueHumanName", "_valueHumanName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueId", "valueId", str, False, "value", True),
            ("_valueId", "_valueId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("_valueIdentifier", "_valueIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInstant", "valueInstant", fhirinstant.FHIRInstant, False, "value", True),
            ("_valueInstant", "_valueInstant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("_valueInteger", "_valueInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("_valueMarkdown", "_valueMarkdown", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
            ("_valueMeta", "_valueMeta", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("_valueMoney", "_valueMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueOid", "valueOid", str, False, "value", True),
            ("_valueOid", "_valueOid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueParameterDefinition", "valueParameterDefinition", parameterdefinition.ParameterDefinition, False, "value", True),
            ("_valueParameterDefinition", "_valueParameterDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("_valuePeriod", "_valuePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("_valuePositiveInt", "_valuePositiveInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("_valueRatio", "_valueRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRelatedArtifact", "valueRelatedArtifact", relatedartifact.RelatedArtifact, False, "value", True),
            ("_valueRelatedArtifact", "_valueRelatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("_valueSampledData", "_valueSampledData", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("_valueSignature", "_valueSignature", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", True),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTime", "valueTime", fhirtime.FHIRTime, False, "value", True),
            ("_valueTime", "_valueTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("_valueTiming", "_valueTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueTriggerDefinition", "valueTriggerDefinition", triggerdefinition.TriggerDefinition, False, "value", True),
            ("_valueTriggerDefinition", "_valueTriggerDefinition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("_valueUnsignedInt", "_valueUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUri", "valueUri", str, False, "value", True),
            ("_valueUri", "_valueUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUrl", "valueUrl", str, False, "value", True),
            ("_valueUrl", "_valueUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUsageContext", "valueUsageContext", usagecontext.UsageContext, False, "value", True),
            ("_valueUsageContext", "_valueUsageContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueUuid", "valueUuid", str, False, "value", True),
            ("_valueUuid", "_valueUuid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    resource_type = "ElementDefinitionMapping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Comments about the mapping or its use.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.identity = None
        """ Reference to mapping declaration.
        Type `str`. """
        self._identity = None
        """ Primitive extension for identity. Type `FHIRPrimitiveExtension` """
        
        self.language = None
        """ Computable language of mapping.
        Type `str`. """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.map = None
        """ Details of the mapping.
        Type `str`. """
        self._map = None
        """ Primitive extension for map. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("_identity", "_identity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("language", "language", str, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("map", "map", str, False, None, True),
            ("_map", "_map", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.
    
    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """
    
    resource_type = "ElementDefinitionSlicing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Text description of how slicing works (or not).
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.discriminator = None
        """ Element values that are used to distinguish the slices.
        List of `ElementDefinitionSlicingDiscriminator` items (represented as `dict` in JSON). """
        self._discriminator = None
        """ Primitive extension for discriminator. Type `FHIRPrimitiveExtension` """
        
        self.ordered = None
        """ If elements must be in same order as slices.
        Type `bool`. """
        self._ordered = None
        """ Primitive extension for ordered. Type `FHIRPrimitiveExtension` """
        
        self.rules = None
        """ closed | open | openAtEnd.
        Type `str`. """
        self._rules = None
        """ Primitive extension for rules. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionSlicing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("discriminator", "discriminator", ElementDefinitionSlicingDiscriminator, True, None, False),
            ("_discriminator", "_discriminator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ordered", "ordered", bool, False, None, False),
            ("_ordered", "_ordered", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rules", "rules", str, False, None, True),
            ("_rules", "_rules", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ElementDefinitionSlicingDiscriminator(element.Element):
    """ Element values that are used to distinguish the slices.
    
    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """
    
    resource_type = "ElementDefinitionSlicingDiscriminator"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.path = None
        """ Path to element value.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ value | exists | pattern | type | profile.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionSlicingDiscriminator, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, True),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.
    
    The data type or resource that the value of this element is permitted to
    be.
    """
    
    resource_type = "ElementDefinitionType"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.aggregation = None
        """ contained | referenced | bundled - how aggregated.
        List of `str` items. """
        self._aggregation = None
        """ Primitive extension for aggregation. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Data type or Resource (reference to definition).
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ Profiles (StructureDefinition or IG) - one must apply.
        List of `str` items. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.targetProfile = None
        """ Profile (StructureDefinition or IG) on the Reference/canonical
        target - one must apply.
        List of `str` items. """
        self._targetProfile = None
        """ Primitive extension for targetProfile. Type `FHIRPrimitiveExtension` """
        
        self.versioning = None
        """ either | independent | specific.
        Type `str`. """
        self._versioning = None
        """ Primitive extension for versioning. Type `FHIRPrimitiveExtension` """
        
        super(ElementDefinitionType, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("aggregation", "aggregation", str, True, None, False),
            ("_aggregation", "_aggregation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, True, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetProfile", "targetProfile", str, True, None, False),
            ("_targetProfile", "_targetProfile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("versioning", "versioning", str, False, None, False),
            ("_versioning", "_versioning", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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