#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2016-06-23.
#  2016, SMART Health IT.


from . import element

class ElementDefinition(element.Element):
    """ Definition of an element in a resource or extension.
    
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    
    resource_name = "ElementDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alias = None
        """ Other names.
        List of `str` items. """
        
        self.base = None
        """ Base definition information for tools.
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """
        
        self.code = None
        """ Defining code.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.comments = None
        """ Comments about the use of this element.
        Type `str`. """
        
        self.condition = None
        """ Reference to invariant about presence.
        List of `str` items. """
        
        self.constraint = None
        """ Condition that must evaluate to true.
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """
        
        self.defaultValueAddress = None
        """ Specified value it missing from instance.
        Type `Address` (represented as `dict` in JSON). """
        
        self.defaultValueAnnotation = None
        """ Specified value it missing from instance.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.defaultValueAttachment = None
        """ Specified value it missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValueBoolean = None
        """ Specified value it missing from instance.
        Type `bool`. """
        
        self.defaultValueCode = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValueCodeableConcept = None
        """ Specified value it missing from instance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.defaultValueCoding = None
        """ Specified value it missing from instance.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.defaultValueContactPoint = None
        """ Specified value it missing from instance.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.defaultValueDate = None
        """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDateTime = None
        """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueDecimal = None
        """ Specified value it missing from instance.
        Type `float`. """
        
        self.defaultValueHumanName = None
        """ Specified value it missing from instance.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.defaultValueId = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValueIdentifier = None
        """ Specified value it missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant = None
        """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueInteger = None
        """ Specified value it missing from instance.
        Type `int`. """
        
        self.defaultValueMarkdown = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValueMeta = None
        """ Specified value it missing from instance.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.defaultValueOid = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValuePeriod = None
        """ Specified value it missing from instance.
        Type `Period` (represented as `dict` in JSON). """
        
        self.defaultValuePositiveInt = None
        """ Specified value it missing from instance.
        Type `int`. """
        
        self.defaultValueQuantity = None
        """ Specified value it missing from instance.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.defaultValueRange = None
        """ Specified value it missing from instance.
        Type `Range` (represented as `dict` in JSON). """
        
        self.defaultValueRatio = None
        """ Specified value it missing from instance.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.defaultValueReference = None
        """ Specified value it missing from instance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.defaultValueSampledData = None
        """ Specified value it missing from instance.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.defaultValueSignature = None
        """ Specified value it missing from instance.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.defaultValueString = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValueTime = None
        """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueTiming = None
        """ Specified value it missing from instance.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueUnsignedInt = None
        """ Specified value it missing from instance.
        Type `int`. """
        
        self.defaultValueUri = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.definition = None
        """ Full formal definition as narrative text.
        Type `str`. """
        
        self.exampleAddress = None
        """ Example value: [as defined for type].
        Type `Address` (represented as `dict` in JSON). """
        
        self.exampleAnnotation = None
        """ Example value: [as defined for type].
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.exampleAttachment = None
        """ Example value: [as defined for type].
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.exampleBase64Binary = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleBoolean = None
        """ Example value: [as defined for type].
        Type `bool`. """
        
        self.exampleCode = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleCodeableConcept = None
        """ Example value: [as defined for type].
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.exampleCoding = None
        """ Example value: [as defined for type].
        Type `Coding` (represented as `dict` in JSON). """
        
        self.exampleContactPoint = None
        """ Example value: [as defined for type].
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.exampleDate = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleDateTime = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleDecimal = None
        """ Example value: [as defined for type].
        Type `float`. """
        
        self.exampleHumanName = None
        """ Example value: [as defined for type].
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.exampleId = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleIdentifier = None
        """ Example value: [as defined for type].
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.exampleInstant = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleInteger = None
        """ Example value: [as defined for type].
        Type `int`. """
        
        self.exampleMarkdown = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleMeta = None
        """ Example value: [as defined for type].
        Type `Meta` (represented as `dict` in JSON). """
        
        self.exampleOid = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.examplePeriod = None
        """ Example value: [as defined for type].
        Type `Period` (represented as `dict` in JSON). """
        
        self.examplePositiveInt = None
        """ Example value: [as defined for type].
        Type `int`. """
        
        self.exampleQuantity = None
        """ Example value: [as defined for type].
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.exampleRange = None
        """ Example value: [as defined for type].
        Type `Range` (represented as `dict` in JSON). """
        
        self.exampleRatio = None
        """ Example value: [as defined for type].
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.exampleReference = None
        """ Example value: [as defined for type].
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.exampleSampledData = None
        """ Example value: [as defined for type].
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.exampleSignature = None
        """ Example value: [as defined for type].
        Type `Signature` (represented as `dict` in JSON). """
        
        self.exampleString = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleTime = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleTiming = None
        """ Example value: [as defined for type].
        Type `Timing` (represented as `dict` in JSON). """
        
        self.exampleUnsignedInt = None
        """ Example value: [as defined for type].
        Type `int`. """
        
        self.exampleUri = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.fixedAddress = None
        """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """
        
        self.fixedAnnotation = None
        """ Value must be exactly this.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.fixedAttachment = None
        """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.fixedBase64Binary = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedBoolean = None
        """ Value must be exactly this.
        Type `bool`. """
        
        self.fixedCode = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedCodeableConcept = None
        """ Value must be exactly this.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fixedCoding = None
        """ Value must be exactly this.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.fixedContactPoint = None
        """ Value must be exactly this.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.fixedDate = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedDateTime = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedDecimal = None
        """ Value must be exactly this.
        Type `float`. """
        
        self.fixedHumanName = None
        """ Value must be exactly this.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.fixedId = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedIdentifier = None
        """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.fixedInstant = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedInteger = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedMarkdown = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedMeta = None
        """ Value must be exactly this.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.fixedOid = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedPeriod = None
        """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """
        
        self.fixedPositiveInt = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedQuantity = None
        """ Value must be exactly this.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.fixedRange = None
        """ Value must be exactly this.
        Type `Range` (represented as `dict` in JSON). """
        
        self.fixedRatio = None
        """ Value must be exactly this.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.fixedReference = None
        """ Value must be exactly this.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.fixedSampledData = None
        """ Value must be exactly this.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.fixedSignature = None
        """ Value must be exactly this.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.fixedString = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedTime = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedTiming = None
        """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.fixedUnsignedInt = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedUri = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.isModifier = None
        """ If this modifies the meaning of other elements.
        Type `bool`. """
        
        self.isSummary = None
        """ Include when _summary = true?.
        Type `bool`. """
        
        self.label = None
        """ Name for element to display with or prompt for element.
        Type `str`. """
        
        self.mapping = None
        """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self.maxLength = None
        """ Max length for strings.
        Type `int`. """
        
        self.maxValueAddress = None
        """ Maximum Allowed Value (for some types).
        Type `Address` (represented as `dict` in JSON). """
        
        self.maxValueAnnotation = None
        """ Maximum Allowed Value (for some types).
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.maxValueAttachment = None
        """ Maximum Allowed Value (for some types).
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.maxValueBase64Binary = None
        """ Maximum Allowed Value (for some types).
        Type `str`. """
        
        self.maxValueBoolean = None
        """ Maximum Allowed Value (for some types).
        Type `bool`. """
        
        self.maxValueCode = None
        """ Maximum Allowed Value (for some types).
        Type `str`. """
        
        self.maxValueCodeableConcept = None
        """ Maximum Allowed Value (for some types).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.maxValueCoding = None
        """ Maximum Allowed Value (for some types).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.maxValueContactPoint = None
        """ Maximum Allowed Value (for some types).
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.maxValueDate = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueDateTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueDecimal = None
        """ Maximum Allowed Value (for some types).
        Type `float`. """
        
        self.maxValueHumanName = None
        """ Maximum Allowed Value (for some types).
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.maxValueId = None
        """ Maximum Allowed Value (for some types).
        Type `str`. """
        
        self.maxValueIdentifier = None
        """ Maximum Allowed Value (for some types).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.maxValueInstant = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueInteger = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self.maxValueMarkdown = None
        """ Maximum Allowed Value (for some types).
        Type `str`. """
        
        self.maxValueMeta = None
        """ Maximum Allowed Value (for some types).
        Type `Meta` (represented as `dict` in JSON). """
        
        self.maxValueOid = None
        """ Maximum Allowed Value (for some types).
        Type `str`. """
        
        self.maxValuePeriod = None
        """ Maximum Allowed Value (for some types).
        Type `Period` (represented as `dict` in JSON). """
        
        self.maxValuePositiveInt = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self.maxValueQuantity = None
        """ Maximum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxValueRange = None
        """ Maximum Allowed Value (for some types).
        Type `Range` (represented as `dict` in JSON). """
        
        self.maxValueRatio = None
        """ Maximum Allowed Value (for some types).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.maxValueReference = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.maxValueSampledData = None
        """ Maximum Allowed Value (for some types).
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.maxValueSignature = None
        """ Maximum Allowed Value (for some types).
        Type `Signature` (represented as `dict` in JSON). """
        
        self.maxValueString = None
        """ Maximum Allowed Value (for some types).
        Type `str`. """
        
        self.maxValueTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.maxValueTiming = None
        """ Maximum Allowed Value (for some types).
        Type `Timing` (represented as `dict` in JSON). """
        
        self.maxValueUnsignedInt = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """
        
        self.maxValueUri = None
        """ Maximum Allowed Value (for some types).
        Type `str`. """
        
        self.meaningWhenMissing = None
        """ Implicit meaning when this element is missing.
        Type `str`. """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        
        self.minValueAddress = None
        """ Minimum Allowed Value (for some types).
        Type `Address` (represented as `dict` in JSON). """
        
        self.minValueAnnotation = None
        """ Minimum Allowed Value (for some types).
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.minValueAttachment = None
        """ Minimum Allowed Value (for some types).
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.minValueBase64Binary = None
        """ Minimum Allowed Value (for some types).
        Type `str`. """
        
        self.minValueBoolean = None
        """ Minimum Allowed Value (for some types).
        Type `bool`. """
        
        self.minValueCode = None
        """ Minimum Allowed Value (for some types).
        Type `str`. """
        
        self.minValueCodeableConcept = None
        """ Minimum Allowed Value (for some types).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.minValueCoding = None
        """ Minimum Allowed Value (for some types).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.minValueContactPoint = None
        """ Minimum Allowed Value (for some types).
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.minValueDate = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueDateTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueDecimal = None
        """ Minimum Allowed Value (for some types).
        Type `float`. """
        
        self.minValueHumanName = None
        """ Minimum Allowed Value (for some types).
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.minValueId = None
        """ Minimum Allowed Value (for some types).
        Type `str`. """
        
        self.minValueIdentifier = None
        """ Minimum Allowed Value (for some types).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.minValueInstant = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueInteger = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self.minValueMarkdown = None
        """ Minimum Allowed Value (for some types).
        Type `str`. """
        
        self.minValueMeta = None
        """ Minimum Allowed Value (for some types).
        Type `Meta` (represented as `dict` in JSON). """
        
        self.minValueOid = None
        """ Minimum Allowed Value (for some types).
        Type `str`. """
        
        self.minValuePeriod = None
        """ Minimum Allowed Value (for some types).
        Type `Period` (represented as `dict` in JSON). """
        
        self.minValuePositiveInt = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self.minValueQuantity = None
        """ Minimum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.minValueRange = None
        """ Minimum Allowed Value (for some types).
        Type `Range` (represented as `dict` in JSON). """
        
        self.minValueRatio = None
        """ Minimum Allowed Value (for some types).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.minValueReference = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.minValueSampledData = None
        """ Minimum Allowed Value (for some types).
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.minValueSignature = None
        """ Minimum Allowed Value (for some types).
        Type `Signature` (represented as `dict` in JSON). """
        
        self.minValueString = None
        """ Minimum Allowed Value (for some types).
        Type `str`. """
        
        self.minValueTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.minValueTiming = None
        """ Minimum Allowed Value (for some types).
        Type `Timing` (represented as `dict` in JSON). """
        
        self.minValueUnsignedInt = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """
        
        self.minValueUri = None
        """ Minimum Allowed Value (for some types).
        Type `str`. """
        
        self.mustSupport = None
        """ If the element must supported.
        Type `bool`. """
        
        self.name = None
        """ Name for this particular element definition (reference target).
        Type `str`. """
        
        self.nameReference = None
        """ To another element constraint (by element.name).
        Type `str`. """
        
        self.path = None
        """ The path of the element (see the Detailed Descriptions).
        Type `str`. """
        
        self.patternAddress = None
        """ Value must have at least these property values.
        Type `Address` (represented as `dict` in JSON). """
        
        self.patternAnnotation = None
        """ Value must have at least these property values.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.patternAttachment = None
        """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.patternBase64Binary = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternBoolean = None
        """ Value must have at least these property values.
        Type `bool`. """
        
        self.patternCode = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternCodeableConcept = None
        """ Value must have at least these property values.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patternCoding = None
        """ Value must have at least these property values.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patternContactPoint = None
        """ Value must have at least these property values.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.patternDate = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternDateTime = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternDecimal = None
        """ Value must have at least these property values.
        Type `float`. """
        
        self.patternHumanName = None
        """ Value must have at least these property values.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patternId = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternIdentifier = None
        """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patternInstant = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternInteger = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternMarkdown = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternMeta = None
        """ Value must have at least these property values.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.patternOid = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternPeriod = None
        """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """
        
        self.patternPositiveInt = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternQuantity = None
        """ Value must have at least these property values.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.patternRange = None
        """ Value must have at least these property values.
        Type `Range` (represented as `dict` in JSON). """
        
        self.patternRatio = None
        """ Value must have at least these property values.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.patternReference = None
        """ Value must have at least these property values.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patternSampledData = None
        """ Value must have at least these property values.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.patternSignature = None
        """ Value must have at least these property values.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.patternString = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternTime = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternTiming = None
        """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.patternUnsignedInt = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternUri = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.representation = None
        """ How this element is represented in instances.
        List of `str` items. """
        
        self.requirements = None
        """ Why is this needed?.
        Type `str`. """
        
        self.short = None
        """ Concise definition for xml presentation.
        Type `str`. """
        
        self.slicing = None
        """ This element is sliced - slices follow.
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """
        
        self.type = None
        """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """
        
        super(ElementDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True, None, False),
            ("base", "base", ElementDefinitionBase, False, None, False),
            ("binding", "binding", ElementDefinitionBinding, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("comments", "comments", str, False, None, False),
            ("condition", "condition", str, True, None, False),
            ("constraint", "constraint", ElementDefinitionConstraint, True, None, False),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False, "defaultValue", False),
            ("defaultValueAnnotation", "defaultValueAnnotation", annotation.Annotation, False, "defaultValue", False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False, "defaultValue", False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False, "defaultValue", False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False, "defaultValue", False),
            ("defaultValueCode", "defaultValueCode", str, False, "defaultValue", False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False, "defaultValue", False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False, "defaultValue", False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False, "defaultValue", False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False, "defaultValue", False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False, "defaultValue", False),
            ("defaultValueId", "defaultValueId", str, False, "defaultValue", False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False, "defaultValue", False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueInteger", "defaultValueInteger", int, False, "defaultValue", False),
            ("defaultValueMarkdown", "defaultValueMarkdown", str, False, "defaultValue", False),
            ("defaultValueMeta", "defaultValueMeta", meta.Meta, False, "defaultValue", False),
            ("defaultValueOid", "defaultValueOid", str, False, "defaultValue", False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False, "defaultValue", False),
            ("defaultValuePositiveInt", "defaultValuePositiveInt", int, False, "defaultValue", False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False, "defaultValue", False),
            ("defaultValueRange", "defaultValueRange", range.Range, False, "defaultValue", False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False, "defaultValue", False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False, "defaultValue", False),
            ("defaultValueSampledData", "defaultValueSampledData", sampleddata.SampledData, False, "defaultValue", False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False, "defaultValue", False),
            ("defaultValueString", "defaultValueString", str, False, "defaultValue", False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, False, "defaultValue", False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False, "defaultValue", False),
            ("defaultValueUnsignedInt", "defaultValueUnsignedInt", int, False, "defaultValue", False),
            ("defaultValueUri", "defaultValueUri", str, False, "defaultValue", False),
            ("definition", "definition", str, False, None, False),
            ("exampleAddress", "exampleAddress", address.Address, False, "example", False),
            ("exampleAnnotation", "exampleAnnotation", annotation.Annotation, False, "example", False),
            ("exampleAttachment", "exampleAttachment", attachment.Attachment, False, "example", False),
            ("exampleBase64Binary", "exampleBase64Binary", str, False, "example", False),
            ("exampleBoolean", "exampleBoolean", bool, False, "example", False),
            ("exampleCode", "exampleCode", str, False, "example", False),
            ("exampleCodeableConcept", "exampleCodeableConcept", codeableconcept.CodeableConcept, False, "example", False),
            ("exampleCoding", "exampleCoding", coding.Coding, False, "example", False),
            ("exampleContactPoint", "exampleContactPoint", contactpoint.ContactPoint, False, "example", False),
            ("exampleDate", "exampleDate", fhirdate.FHIRDate, False, "example", False),
            ("exampleDateTime", "exampleDateTime", fhirdate.FHIRDate, False, "example", False),
            ("exampleDecimal", "exampleDecimal", float, False, "example", False),
            ("exampleHumanName", "exampleHumanName", humanname.HumanName, False, "example", False),
            ("exampleId", "exampleId", str, False, "example", False),
            ("exampleIdentifier", "exampleIdentifier", identifier.Identifier, False, "example", False),
            ("exampleInstant", "exampleInstant", fhirdate.FHIRDate, False, "example", False),
            ("exampleInteger", "exampleInteger", int, False, "example", False),
            ("exampleMarkdown", "exampleMarkdown", str, False, "example", False),
            ("exampleMeta", "exampleMeta", meta.Meta, False, "example", False),
            ("exampleOid", "exampleOid", str, False, "example", False),
            ("examplePeriod", "examplePeriod", period.Period, False, "example", False),
            ("examplePositiveInt", "examplePositiveInt", int, False, "example", False),
            ("exampleQuantity", "exampleQuantity", quantity.Quantity, False, "example", False),
            ("exampleRange", "exampleRange", range.Range, False, "example", False),
            ("exampleRatio", "exampleRatio", ratio.Ratio, False, "example", False),
            ("exampleReference", "exampleReference", fhirreference.FHIRReference, False, "example", False),
            ("exampleSampledData", "exampleSampledData", sampleddata.SampledData, False, "example", False),
            ("exampleSignature", "exampleSignature", signature.Signature, False, "example", False),
            ("exampleString", "exampleString", str, False, "example", False),
            ("exampleTime", "exampleTime", fhirdate.FHIRDate, False, "example", False),
            ("exampleTiming", "exampleTiming", timing.Timing, False, "example", False),
            ("exampleUnsignedInt", "exampleUnsignedInt", int, False, "example", False),
            ("exampleUri", "exampleUri", str, False, "example", False),
            ("fixedAddress", "fixedAddress", address.Address, False, "fixed", False),
            ("fixedAnnotation", "fixedAnnotation", annotation.Annotation, False, "fixed", False),
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False, "fixed", False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False, "fixed", False),
            ("fixedBoolean", "fixedBoolean", bool, False, "fixed", False),
            ("fixedCode", "fixedCode", str, False, "fixed", False),
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False, "fixed", False),
            ("fixedCoding", "fixedCoding", coding.Coding, False, "fixed", False),
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False, "fixed", False),
            ("fixedDate", "fixedDate", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedDateTime", "fixedDateTime", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedDecimal", "fixedDecimal", float, False, "fixed", False),
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False, "fixed", False),
            ("fixedId", "fixedId", str, False, "fixed", False),
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False, "fixed", False),
            ("fixedInstant", "fixedInstant", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedInteger", "fixedInteger", int, False, "fixed", False),
            ("fixedMarkdown", "fixedMarkdown", str, False, "fixed", False),
            ("fixedMeta", "fixedMeta", meta.Meta, False, "fixed", False),
            ("fixedOid", "fixedOid", str, False, "fixed", False),
            ("fixedPeriod", "fixedPeriod", period.Period, False, "fixed", False),
            ("fixedPositiveInt", "fixedPositiveInt", int, False, "fixed", False),
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False, "fixed", False),
            ("fixedRange", "fixedRange", range.Range, False, "fixed", False),
            ("fixedRatio", "fixedRatio", ratio.Ratio, False, "fixed", False),
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False, "fixed", False),
            ("fixedSampledData", "fixedSampledData", sampleddata.SampledData, False, "fixed", False),
            ("fixedSignature", "fixedSignature", signature.Signature, False, "fixed", False),
            ("fixedString", "fixedString", str, False, "fixed", False),
            ("fixedTime", "fixedTime", fhirdate.FHIRDate, False, "fixed", False),
            ("fixedTiming", "fixedTiming", timing.Timing, False, "fixed", False),
            ("fixedUnsignedInt", "fixedUnsignedInt", int, False, "fixed", False),
            ("fixedUri", "fixedUri", str, False, "fixed", False),
            ("isModifier", "isModifier", bool, False, None, False),
            ("isSummary", "isSummary", bool, False, None, False),
            ("label", "label", str, False, None, False),
            ("mapping", "mapping", ElementDefinitionMapping, True, None, False),
            ("max", "max", str, False, None, False),
            ("maxLength", "maxLength", int, False, None, False),
            ("maxValueAddress", "maxValueAddress", address.Address, False, "maxValue", False),
            ("maxValueAnnotation", "maxValueAnnotation", annotation.Annotation, False, "maxValue", False),
            ("maxValueAttachment", "maxValueAttachment", attachment.Attachment, False, "maxValue", False),
            ("maxValueBase64Binary", "maxValueBase64Binary", str, False, "maxValue", False),
            ("maxValueBoolean", "maxValueBoolean", bool, False, "maxValue", False),
            ("maxValueCode", "maxValueCode", str, False, "maxValue", False),
            ("maxValueCodeableConcept", "maxValueCodeableConcept", codeableconcept.CodeableConcept, False, "maxValue", False),
            ("maxValueCoding", "maxValueCoding", coding.Coding, False, "maxValue", False),
            ("maxValueContactPoint", "maxValueContactPoint", contactpoint.ContactPoint, False, "maxValue", False),
            ("maxValueDate", "maxValueDate", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueDateTime", "maxValueDateTime", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueDecimal", "maxValueDecimal", float, False, "maxValue", False),
            ("maxValueHumanName", "maxValueHumanName", humanname.HumanName, False, "maxValue", False),
            ("maxValueId", "maxValueId", str, False, "maxValue", False),
            ("maxValueIdentifier", "maxValueIdentifier", identifier.Identifier, False, "maxValue", False),
            ("maxValueInstant", "maxValueInstant", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueInteger", "maxValueInteger", int, False, "maxValue", False),
            ("maxValueMarkdown", "maxValueMarkdown", str, False, "maxValue", False),
            ("maxValueMeta", "maxValueMeta", meta.Meta, False, "maxValue", False),
            ("maxValueOid", "maxValueOid", str, False, "maxValue", False),
            ("maxValuePeriod", "maxValuePeriod", period.Period, False, "maxValue", False),
            ("maxValuePositiveInt", "maxValuePositiveInt", int, False, "maxValue", False),
            ("maxValueQuantity", "maxValueQuantity", quantity.Quantity, False, "maxValue", False),
            ("maxValueRange", "maxValueRange", range.Range, False, "maxValue", False),
            ("maxValueRatio", "maxValueRatio", ratio.Ratio, False, "maxValue", False),
            ("maxValueReference", "maxValueReference", fhirreference.FHIRReference, False, "maxValue", False),
            ("maxValueSampledData", "maxValueSampledData", sampleddata.SampledData, False, "maxValue", False),
            ("maxValueSignature", "maxValueSignature", signature.Signature, False, "maxValue", False),
            ("maxValueString", "maxValueString", str, False, "maxValue", False),
            ("maxValueTime", "maxValueTime", fhirdate.FHIRDate, False, "maxValue", False),
            ("maxValueTiming", "maxValueTiming", timing.Timing, False, "maxValue", False),
            ("maxValueUnsignedInt", "maxValueUnsignedInt", int, False, "maxValue", False),
            ("maxValueUri", "maxValueUri", str, False, "maxValue", False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False, None, False),
            ("min", "min", int, False, None, False),
            ("minValueAddress", "minValueAddress", address.Address, False, "minValue", False),
            ("minValueAnnotation", "minValueAnnotation", annotation.Annotation, False, "minValue", False),
            ("minValueAttachment", "minValueAttachment", attachment.Attachment, False, "minValue", False),
            ("minValueBase64Binary", "minValueBase64Binary", str, False, "minValue", False),
            ("minValueBoolean", "minValueBoolean", bool, False, "minValue", False),
            ("minValueCode", "minValueCode", str, False, "minValue", False),
            ("minValueCodeableConcept", "minValueCodeableConcept", codeableconcept.CodeableConcept, False, "minValue", False),
            ("minValueCoding", "minValueCoding", coding.Coding, False, "minValue", False),
            ("minValueContactPoint", "minValueContactPoint", contactpoint.ContactPoint, False, "minValue", False),
            ("minValueDate", "minValueDate", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueDateTime", "minValueDateTime", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueDecimal", "minValueDecimal", float, False, "minValue", False),
            ("minValueHumanName", "minValueHumanName", humanname.HumanName, False, "minValue", False),
            ("minValueId", "minValueId", str, False, "minValue", False),
            ("minValueIdentifier", "minValueIdentifier", identifier.Identifier, False, "minValue", False),
            ("minValueInstant", "minValueInstant", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueInteger", "minValueInteger", int, False, "minValue", False),
            ("minValueMarkdown", "minValueMarkdown", str, False, "minValue", False),
            ("minValueMeta", "minValueMeta", meta.Meta, False, "minValue", False),
            ("minValueOid", "minValueOid", str, False, "minValue", False),
            ("minValuePeriod", "minValuePeriod", period.Period, False, "minValue", False),
            ("minValuePositiveInt", "minValuePositiveInt", int, False, "minValue", False),
            ("minValueQuantity", "minValueQuantity", quantity.Quantity, False, "minValue", False),
            ("minValueRange", "minValueRange", range.Range, False, "minValue", False),
            ("minValueRatio", "minValueRatio", ratio.Ratio, False, "minValue", False),
            ("minValueReference", "minValueReference", fhirreference.FHIRReference, False, "minValue", False),
            ("minValueSampledData", "minValueSampledData", sampleddata.SampledData, False, "minValue", False),
            ("minValueSignature", "minValueSignature", signature.Signature, False, "minValue", False),
            ("minValueString", "minValueString", str, False, "minValue", False),
            ("minValueTime", "minValueTime", fhirdate.FHIRDate, False, "minValue", False),
            ("minValueTiming", "minValueTiming", timing.Timing, False, "minValue", False),
            ("minValueUnsignedInt", "minValueUnsignedInt", int, False, "minValue", False),
            ("minValueUri", "minValueUri", str, False, "minValue", False),
            ("mustSupport", "mustSupport", bool, False, None, False),
            ("name", "name", str, False, None, False),
            ("nameReference", "nameReference", str, False, None, False),
            ("path", "path", str, False, None, True),
            ("patternAddress", "patternAddress", address.Address, False, "pattern", False),
            ("patternAnnotation", "patternAnnotation", annotation.Annotation, False, "pattern", False),
            ("patternAttachment", "patternAttachment", attachment.Attachment, False, "pattern", False),
            ("patternBase64Binary", "patternBase64Binary", str, False, "pattern", False),
            ("patternBoolean", "patternBoolean", bool, False, "pattern", False),
            ("patternCode", "patternCode", str, False, "pattern", False),
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False, "pattern", False),
            ("patternCoding", "patternCoding", coding.Coding, False, "pattern", False),
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False, "pattern", False),
            ("patternDate", "patternDate", fhirdate.FHIRDate, False, "pattern", False),
            ("patternDateTime", "patternDateTime", fhirdate.FHIRDate, False, "pattern", False),
            ("patternDecimal", "patternDecimal", float, False, "pattern", False),
            ("patternHumanName", "patternHumanName", humanname.HumanName, False, "pattern", False),
            ("patternId", "patternId", str, False, "pattern", False),
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False, "pattern", False),
            ("patternInstant", "patternInstant", fhirdate.FHIRDate, False, "pattern", False),
            ("patternInteger", "patternInteger", int, False, "pattern", False),
            ("patternMarkdown", "patternMarkdown", str, False, "pattern", False),
            ("patternMeta", "patternMeta", meta.Meta, False, "pattern", False),
            ("patternOid", "patternOid", str, False, "pattern", False),
            ("patternPeriod", "patternPeriod", period.Period, False, "pattern", False),
            ("patternPositiveInt", "patternPositiveInt", int, False, "pattern", False),
            ("patternQuantity", "patternQuantity", quantity.Quantity, False, "pattern", False),
            ("patternRange", "patternRange", range.Range, False, "pattern", False),
            ("patternRatio", "patternRatio", ratio.Ratio, False, "pattern", False),
            ("patternReference", "patternReference", fhirreference.FHIRReference, False, "pattern", False),
            ("patternSampledData", "patternSampledData", sampleddata.SampledData, False, "pattern", False),
            ("patternSignature", "patternSignature", signature.Signature, False, "pattern", False),
            ("patternString", "patternString", str, False, "pattern", False),
            ("patternTime", "patternTime", fhirdate.FHIRDate, False, "pattern", False),
            ("patternTiming", "patternTiming", timing.Timing, False, "pattern", False),
            ("patternUnsignedInt", "patternUnsignedInt", int, False, "pattern", False),
            ("patternUri", "patternUri", str, False, "pattern", False),
            ("representation", "representation", str, True, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("short", "short", str, False, None, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False, None, False),
            ("type", "type", ElementDefinitionType, True, None, False),
        ])
        return js


class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.
    
    Information about the base definition of the element, provided to make it
    unncessary for tools to trace the deviation of the element through the
    derived and related profiles. This information is only provided where the
    element definition represents a constraint on another element definition,
    and must be present if there is a base element definition.
    """
    
    resource_name = "ElementDefinitionBase"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.max = None
        """ Max cardinality of the base element.
        Type `str`. """
        
        self.min = None
        """ Min cardinality of the base element.
        Type `int`. """
        
        self.path = None
        """ Path that identifies the base element.
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
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_name = "ElementDefinitionBinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Human explanation of the value set.
        Type `str`. """
        
        self.strength = None
        """ required | extensible | preferred | example.
        Type `str`. """
        
        self.valueSetReference = None
        """ Source of value set.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.valueSetUri = None
        """ Source of value set.
        Type `str`. """
        
        super(ElementDefinitionBinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("strength", "strength", str, False, None, True),
            ("valueSetReference", "valueSetReference", fhirreference.FHIRReference, False, "valueSet", False),
            ("valueSetUri", "valueSetUri", str, False, "valueSet", False),
        ])
        return js


class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.
    
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    
    resource_name = "ElementDefinitionConstraint"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.human = None
        """ Human description of constraint.
        Type `str`. """
        
        self.key = None
        """ Target of 'condition' reference above.
        Type `str`. """
        
        self.requirements = None
        """ Why this constraint necessary or appropriate.
        Type `str`. """
        
        self.severity = None
        """ error | warning.
        Type `str`. """
        
        self.xpath = None
        """ XPath expression of constraint.
        Type `str`. """
        
        super(ElementDefinitionConstraint, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("human", "human", str, False, None, True),
            ("key", "key", str, False, None, True),
            ("requirements", "requirements", str, False, None, False),
            ("severity", "severity", str, False, None, True),
            ("xpath", "xpath", str, False, None, True),
        ])
        return js


class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    resource_name = "ElementDefinitionMapping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identity = None
        """ Reference to mapping declaration.
        Type `str`. """
        
        self.language = None
        """ Computable language of mapping.
        Type `str`. """
        
        self.map = None
        """ Details of the mapping.
        Type `str`. """
        
        super(ElementDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("identity", "identity", str, False, None, True),
            ("language", "language", str, False, None, False),
            ("map", "map", str, False, None, True),
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
    
    resource_name = "ElementDefinitionSlicing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Text description of how slicing works (or not).
        Type `str`. """
        
        self.discriminator = None
        """ Element values that used to distinguish the slices.
        List of `str` items. """
        
        self.ordered = None
        """ If elements must be in same order as slices.
        Type `bool`. """
        
        self.rules = None
        """ closed | open | openAtEnd.
        Type `str`. """
        
        super(ElementDefinitionSlicing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("discriminator", "discriminator", str, True, None, False),
            ("ordered", "ordered", bool, False, None, False),
            ("rules", "rules", str, False, None, True),
        ])
        return js


class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.
    
    The data type or resource that the value of this element is permitted to
    be.
    """
    
    resource_name = "ElementDefinitionType"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.aggregation = None
        """ contained | referenced | bundled - how aggregated.
        List of `str` items. """
        
        self.code = None
        """ Name of Data type or Resource.
        Type `str`. """
        
        self.profile = None
        """ Profile (StructureDefinition) to apply (or IG).
        List of `str` items. """
        
        super(ElementDefinitionType, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("aggregation", "aggregation", str, True, None, False),
            ("code", "code", str, False, None, True),
            ("profile", "profile", str, True, None, False),
        ])
        return js


from . import address
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import meta
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import signature
from . import timing
