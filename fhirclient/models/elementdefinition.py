#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (ElementDefinition.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import address
import attachment
import codeableconcept
import coding
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import humanname
import identifier
import period
import quantity
import range
import ratio
import timing


class ElementDefinition(fhirelement.FHIRElement):
    """ Definition of an elements in a resource or extension.
    
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    
    resource_name = "ElementDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.binding = None
        """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """
        
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
        
        self.defaultValueAttachment = None
        """ Specified value it missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.defaultValueBase64Binary = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValueBoolean = False
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
        
        self.defaultValueIdentifier = None
        """ Specified value it missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.defaultValueInstant = None
        """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueInteger = None
        """ Specified value it missing from instance.
        Type `int`. """
        
        self.defaultValuePeriod = None
        """ Specified value it missing from instance.
        Type `Period` (represented as `dict` in JSON). """
        
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
        
        self.defaultValueString = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.defaultValueTime = None
        """ Specified value it missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.defaultValueTiming = None
        """ Specified value it missing from instance.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.defaultValueUri = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.exampleAddress = None
        """ Example value: [as defined for type].
        Type `Address` (represented as `dict` in JSON). """
        
        self.exampleAttachment = None
        """ Example value: [as defined for type].
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.exampleBase64Binary = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleBoolean = False
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
        
        self.exampleIdentifier = None
        """ Example value: [as defined for type].
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.exampleInstant = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleInteger = None
        """ Example value: [as defined for type].
        Type `int`. """
        
        self.examplePeriod = None
        """ Example value: [as defined for type].
        Type `Period` (represented as `dict` in JSON). """
        
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
        
        self.exampleString = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.exampleTime = None
        """ Example value: [as defined for type].
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exampleTiming = None
        """ Example value: [as defined for type].
        Type `Timing` (represented as `dict` in JSON). """
        
        self.exampleUri = None
        """ Example value: [as defined for type].
        Type `str`. """
        
        self.fixedAddress = None
        """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """
        
        self.fixedAttachment = None
        """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.fixedBase64Binary = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedBoolean = False
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
        
        self.fixedIdentifier = None
        """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.fixedInstant = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedInteger = None
        """ Value must be exactly this.
        Type `int`. """
        
        self.fixedPeriod = None
        """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """
        
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
        
        self.fixedString = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.fixedTime = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.fixedTiming = None
        """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.fixedUri = None
        """ Value must be exactly this.
        Type `str`. """
        
        self.formal = None
        """ Full formal definition in human language.
        Type `str`. """
        
        self.isModifier = False
        """ If this modifies the meaning of other elements.
        Type `bool`. """
        
        self.isSummary = False
        """ Include when _summary = true?.
        Type `bool`. """
        
        self.mapping = None
        """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """
        
        self.maxLength = None
        """ Max length for strings.
        Type `int`. """
        
        self.meaningWhenMissing = None
        """ Implicit meaning when this element is missing.
        Type `str`. """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        
        self.mustSupport = False
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
        
        self.patternAttachment = None
        """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.patternBase64Binary = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternBoolean = False
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
        
        self.patternIdentifier = None
        """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patternInstant = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternInteger = None
        """ Value must have at least these property values.
        Type `int`. """
        
        self.patternPeriod = None
        """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """
        
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
        
        self.patternString = None
        """ Value must have at least these property values.
        Type `str`. """
        
        self.patternTime = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.patternTiming = None
        """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """
        
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
        
        self.synonym = None
        """ Other names.
        List of `str` items. """
        
        self.type = None
        """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """
        
        super(ElementDefinition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ElementDefinition, self).update_with_json(jsondict)
        if 'binding' in jsondict:
            self.binding = ElementDefinitionBinding.with_json_and_owner(jsondict['binding'], self)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'condition' in jsondict:
            self.condition = jsondict['condition']
        if 'constraint' in jsondict:
            self.constraint = ElementDefinitionConstraint.with_json_and_owner(jsondict['constraint'], self)
        if 'defaultValueAddress' in jsondict:
            self.defaultValueAddress = address.Address.with_json_and_owner(jsondict['defaultValueAddress'], self)
        if 'defaultValueAttachment' in jsondict:
            self.defaultValueAttachment = attachment.Attachment.with_json_and_owner(jsondict['defaultValueAttachment'], self)
        if 'defaultValueBase64Binary' in jsondict:
            self.defaultValueBase64Binary = jsondict['defaultValueBase64Binary']
        if 'defaultValueBoolean' in jsondict:
            self.defaultValueBoolean = jsondict['defaultValueBoolean']
        if 'defaultValueCode' in jsondict:
            self.defaultValueCode = jsondict['defaultValueCode']
        if 'defaultValueCodeableConcept' in jsondict:
            self.defaultValueCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['defaultValueCodeableConcept'], self)
        if 'defaultValueCoding' in jsondict:
            self.defaultValueCoding = coding.Coding.with_json_and_owner(jsondict['defaultValueCoding'], self)
        if 'defaultValueContactPoint' in jsondict:
            self.defaultValueContactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['defaultValueContactPoint'], self)
        if 'defaultValueDate' in jsondict:
            self.defaultValueDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['defaultValueDate'], self)
        if 'defaultValueDateTime' in jsondict:
            self.defaultValueDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['defaultValueDateTime'], self)
        if 'defaultValueDecimal' in jsondict:
            self.defaultValueDecimal = jsondict['defaultValueDecimal']
        if 'defaultValueHumanName' in jsondict:
            self.defaultValueHumanName = humanname.HumanName.with_json_and_owner(jsondict['defaultValueHumanName'], self)
        if 'defaultValueIdentifier' in jsondict:
            self.defaultValueIdentifier = identifier.Identifier.with_json_and_owner(jsondict['defaultValueIdentifier'], self)
        if 'defaultValueInstant' in jsondict:
            self.defaultValueInstant = fhirdate.FHIRDate.with_json_and_owner(jsondict['defaultValueInstant'], self)
        if 'defaultValueInteger' in jsondict:
            self.defaultValueInteger = jsondict['defaultValueInteger']
        if 'defaultValuePeriod' in jsondict:
            self.defaultValuePeriod = period.Period.with_json_and_owner(jsondict['defaultValuePeriod'], self)
        if 'defaultValueQuantity' in jsondict:
            self.defaultValueQuantity = quantity.Quantity.with_json_and_owner(jsondict['defaultValueQuantity'], self)
        if 'defaultValueRange' in jsondict:
            self.defaultValueRange = range.Range.with_json_and_owner(jsondict['defaultValueRange'], self)
        if 'defaultValueRatio' in jsondict:
            self.defaultValueRatio = ratio.Ratio.with_json_and_owner(jsondict['defaultValueRatio'], self)
        if 'defaultValueReference' in jsondict:
            self.defaultValueReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['defaultValueReference'], self)
        if 'defaultValueString' in jsondict:
            self.defaultValueString = jsondict['defaultValueString']
        if 'defaultValueTime' in jsondict:
            self.defaultValueTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['defaultValueTime'], self)
        if 'defaultValueTiming' in jsondict:
            self.defaultValueTiming = timing.Timing.with_json_and_owner(jsondict['defaultValueTiming'], self)
        if 'defaultValueUri' in jsondict:
            self.defaultValueUri = jsondict['defaultValueUri']
        if 'exampleAddress' in jsondict:
            self.exampleAddress = address.Address.with_json_and_owner(jsondict['exampleAddress'], self)
        if 'exampleAttachment' in jsondict:
            self.exampleAttachment = attachment.Attachment.with_json_and_owner(jsondict['exampleAttachment'], self)
        if 'exampleBase64Binary' in jsondict:
            self.exampleBase64Binary = jsondict['exampleBase64Binary']
        if 'exampleBoolean' in jsondict:
            self.exampleBoolean = jsondict['exampleBoolean']
        if 'exampleCode' in jsondict:
            self.exampleCode = jsondict['exampleCode']
        if 'exampleCodeableConcept' in jsondict:
            self.exampleCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['exampleCodeableConcept'], self)
        if 'exampleCoding' in jsondict:
            self.exampleCoding = coding.Coding.with_json_and_owner(jsondict['exampleCoding'], self)
        if 'exampleContactPoint' in jsondict:
            self.exampleContactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['exampleContactPoint'], self)
        if 'exampleDate' in jsondict:
            self.exampleDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleDate'], self)
        if 'exampleDateTime' in jsondict:
            self.exampleDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleDateTime'], self)
        if 'exampleDecimal' in jsondict:
            self.exampleDecimal = jsondict['exampleDecimal']
        if 'exampleHumanName' in jsondict:
            self.exampleHumanName = humanname.HumanName.with_json_and_owner(jsondict['exampleHumanName'], self)
        if 'exampleIdentifier' in jsondict:
            self.exampleIdentifier = identifier.Identifier.with_json_and_owner(jsondict['exampleIdentifier'], self)
        if 'exampleInstant' in jsondict:
            self.exampleInstant = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleInstant'], self)
        if 'exampleInteger' in jsondict:
            self.exampleInteger = jsondict['exampleInteger']
        if 'examplePeriod' in jsondict:
            self.examplePeriod = period.Period.with_json_and_owner(jsondict['examplePeriod'], self)
        if 'exampleQuantity' in jsondict:
            self.exampleQuantity = quantity.Quantity.with_json_and_owner(jsondict['exampleQuantity'], self)
        if 'exampleRange' in jsondict:
            self.exampleRange = range.Range.with_json_and_owner(jsondict['exampleRange'], self)
        if 'exampleRatio' in jsondict:
            self.exampleRatio = ratio.Ratio.with_json_and_owner(jsondict['exampleRatio'], self)
        if 'exampleReference' in jsondict:
            self.exampleReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['exampleReference'], self)
        if 'exampleString' in jsondict:
            self.exampleString = jsondict['exampleString']
        if 'exampleTime' in jsondict:
            self.exampleTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['exampleTime'], self)
        if 'exampleTiming' in jsondict:
            self.exampleTiming = timing.Timing.with_json_and_owner(jsondict['exampleTiming'], self)
        if 'exampleUri' in jsondict:
            self.exampleUri = jsondict['exampleUri']
        if 'fixedAddress' in jsondict:
            self.fixedAddress = address.Address.with_json_and_owner(jsondict['fixedAddress'], self)
        if 'fixedAttachment' in jsondict:
            self.fixedAttachment = attachment.Attachment.with_json_and_owner(jsondict['fixedAttachment'], self)
        if 'fixedBase64Binary' in jsondict:
            self.fixedBase64Binary = jsondict['fixedBase64Binary']
        if 'fixedBoolean' in jsondict:
            self.fixedBoolean = jsondict['fixedBoolean']
        if 'fixedCode' in jsondict:
            self.fixedCode = jsondict['fixedCode']
        if 'fixedCodeableConcept' in jsondict:
            self.fixedCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['fixedCodeableConcept'], self)
        if 'fixedCoding' in jsondict:
            self.fixedCoding = coding.Coding.with_json_and_owner(jsondict['fixedCoding'], self)
        if 'fixedContactPoint' in jsondict:
            self.fixedContactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['fixedContactPoint'], self)
        if 'fixedDate' in jsondict:
            self.fixedDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['fixedDate'], self)
        if 'fixedDateTime' in jsondict:
            self.fixedDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['fixedDateTime'], self)
        if 'fixedDecimal' in jsondict:
            self.fixedDecimal = jsondict['fixedDecimal']
        if 'fixedHumanName' in jsondict:
            self.fixedHumanName = humanname.HumanName.with_json_and_owner(jsondict['fixedHumanName'], self)
        if 'fixedIdentifier' in jsondict:
            self.fixedIdentifier = identifier.Identifier.with_json_and_owner(jsondict['fixedIdentifier'], self)
        if 'fixedInstant' in jsondict:
            self.fixedInstant = fhirdate.FHIRDate.with_json_and_owner(jsondict['fixedInstant'], self)
        if 'fixedInteger' in jsondict:
            self.fixedInteger = jsondict['fixedInteger']
        if 'fixedPeriod' in jsondict:
            self.fixedPeriod = period.Period.with_json_and_owner(jsondict['fixedPeriod'], self)
        if 'fixedQuantity' in jsondict:
            self.fixedQuantity = quantity.Quantity.with_json_and_owner(jsondict['fixedQuantity'], self)
        if 'fixedRange' in jsondict:
            self.fixedRange = range.Range.with_json_and_owner(jsondict['fixedRange'], self)
        if 'fixedRatio' in jsondict:
            self.fixedRatio = ratio.Ratio.with_json_and_owner(jsondict['fixedRatio'], self)
        if 'fixedReference' in jsondict:
            self.fixedReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['fixedReference'], self)
        if 'fixedString' in jsondict:
            self.fixedString = jsondict['fixedString']
        if 'fixedTime' in jsondict:
            self.fixedTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['fixedTime'], self)
        if 'fixedTiming' in jsondict:
            self.fixedTiming = timing.Timing.with_json_and_owner(jsondict['fixedTiming'], self)
        if 'fixedUri' in jsondict:
            self.fixedUri = jsondict['fixedUri']
        if 'formal' in jsondict:
            self.formal = jsondict['formal']
        if 'isModifier' in jsondict:
            self.isModifier = jsondict['isModifier']
        if 'isSummary' in jsondict:
            self.isSummary = jsondict['isSummary']
        if 'mapping' in jsondict:
            self.mapping = ElementDefinitionMapping.with_json_and_owner(jsondict['mapping'], self)
        if 'max' in jsondict:
            self.max = jsondict['max']
        if 'maxLength' in jsondict:
            self.maxLength = jsondict['maxLength']
        if 'meaningWhenMissing' in jsondict:
            self.meaningWhenMissing = jsondict['meaningWhenMissing']
        if 'min' in jsondict:
            self.min = jsondict['min']
        if 'mustSupport' in jsondict:
            self.mustSupport = jsondict['mustSupport']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'nameReference' in jsondict:
            self.nameReference = jsondict['nameReference']
        if 'path' in jsondict:
            self.path = jsondict['path']
        if 'patternAddress' in jsondict:
            self.patternAddress = address.Address.with_json_and_owner(jsondict['patternAddress'], self)
        if 'patternAttachment' in jsondict:
            self.patternAttachment = attachment.Attachment.with_json_and_owner(jsondict['patternAttachment'], self)
        if 'patternBase64Binary' in jsondict:
            self.patternBase64Binary = jsondict['patternBase64Binary']
        if 'patternBoolean' in jsondict:
            self.patternBoolean = jsondict['patternBoolean']
        if 'patternCode' in jsondict:
            self.patternCode = jsondict['patternCode']
        if 'patternCodeableConcept' in jsondict:
            self.patternCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['patternCodeableConcept'], self)
        if 'patternCoding' in jsondict:
            self.patternCoding = coding.Coding.with_json_and_owner(jsondict['patternCoding'], self)
        if 'patternContactPoint' in jsondict:
            self.patternContactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['patternContactPoint'], self)
        if 'patternDate' in jsondict:
            self.patternDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['patternDate'], self)
        if 'patternDateTime' in jsondict:
            self.patternDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['patternDateTime'], self)
        if 'patternDecimal' in jsondict:
            self.patternDecimal = jsondict['patternDecimal']
        if 'patternHumanName' in jsondict:
            self.patternHumanName = humanname.HumanName.with_json_and_owner(jsondict['patternHumanName'], self)
        if 'patternIdentifier' in jsondict:
            self.patternIdentifier = identifier.Identifier.with_json_and_owner(jsondict['patternIdentifier'], self)
        if 'patternInstant' in jsondict:
            self.patternInstant = fhirdate.FHIRDate.with_json_and_owner(jsondict['patternInstant'], self)
        if 'patternInteger' in jsondict:
            self.patternInteger = jsondict['patternInteger']
        if 'patternPeriod' in jsondict:
            self.patternPeriod = period.Period.with_json_and_owner(jsondict['patternPeriod'], self)
        if 'patternQuantity' in jsondict:
            self.patternQuantity = quantity.Quantity.with_json_and_owner(jsondict['patternQuantity'], self)
        if 'patternRange' in jsondict:
            self.patternRange = range.Range.with_json_and_owner(jsondict['patternRange'], self)
        if 'patternRatio' in jsondict:
            self.patternRatio = ratio.Ratio.with_json_and_owner(jsondict['patternRatio'], self)
        if 'patternReference' in jsondict:
            self.patternReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['patternReference'], self)
        if 'patternString' in jsondict:
            self.patternString = jsondict['patternString']
        if 'patternTime' in jsondict:
            self.patternTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['patternTime'], self)
        if 'patternTiming' in jsondict:
            self.patternTiming = timing.Timing.with_json_and_owner(jsondict['patternTiming'], self)
        if 'patternUri' in jsondict:
            self.patternUri = jsondict['patternUri']
        if 'representation' in jsondict:
            self.representation = jsondict['representation']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'short' in jsondict:
            self.short = jsondict['short']
        if 'slicing' in jsondict:
            self.slicing = ElementDefinitionSlicing.with_json_and_owner(jsondict['slicing'], self)
        if 'synonym' in jsondict:
            self.synonym = jsondict['synonym']
        if 'type' in jsondict:
            self.type = ElementDefinitionType.with_json_and_owner(jsondict['type'], self)


class ElementDefinitionBinding(fhirelement.FHIRElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_name = "ElementDefinitionBinding"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.conformance = None
        """ required | preferred | example.
        Type `str`. """
        
        self.description = None
        """ Human explanation of the value set.
        Type `str`. """
        
        self.isExtensible = False
        """ Can additional codes be used?.
        Type `bool`. """
        
        self.name = None
        """ Descriptive Name.
        Type `str`. """
        
        self.referenceReference = None
        """ Source of value set.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.referenceUri = None
        """ Source of value set.
        Type `str`. """
        
        super(ElementDefinitionBinding, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ElementDefinitionBinding, self).update_with_json(jsondict)
        if 'conformance' in jsondict:
            self.conformance = jsondict['conformance']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'isExtensible' in jsondict:
            self.isExtensible = jsondict['isExtensible']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'referenceReference' in jsondict:
            self.referenceReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['referenceReference'], self)
        if 'referenceUri' in jsondict:
            self.referenceUri = jsondict['referenceUri']


class ElementDefinitionConstraint(fhirelement.FHIRElement):
    """ Condition that must evaluate to true.
    
    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """
    
    resource_name = "ElementDefinitionConstraint"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.human = None
        """ Human description of constraint.
        Type `str`. """
        
        self.key = None
        """ Target of 'condition' reference above.
        Type `str`. """
        
        self.name = None
        """ Short human label.
        Type `str`. """
        
        self.severity = None
        """ error | warning.
        Type `str`. """
        
        self.xpath = None
        """ XPath expression of constraint.
        Type `str`. """
        
        super(ElementDefinitionConstraint, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ElementDefinitionConstraint, self).update_with_json(jsondict)
        if 'human' in jsondict:
            self.human = jsondict['human']
        if 'key' in jsondict:
            self.key = jsondict['key']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'severity' in jsondict:
            self.severity = jsondict['severity']
        if 'xpath' in jsondict:
            self.xpath = jsondict['xpath']


class ElementDefinitionMapping(fhirelement.FHIRElement):
    """ Map element to another set of definitions.
    
    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """
    
    resource_name = "ElementDefinitionMapping"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identity = None
        """ Reference to mapping declaration.
        Type `str`. """
        
        self.map = None
        """ Details of the mapping.
        Type `str`. """
        
        super(ElementDefinitionMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ElementDefinitionMapping, self).update_with_json(jsondict)
        if 'identity' in jsondict:
            self.identity = jsondict['identity']
        if 'map' in jsondict:
            self.map = jsondict['map']


class ElementDefinitionSlicing(fhirelement.FHIRElement):
    """ This element is sliced - slices follow.
    
    Indicates that the element is sliced into a set of alternative definitions
    (there are multiple definitions on a single element in the base resource).
    The set of slices is any elements that come after this in the element
    sequence that have the same path, until a shorter path occurs (the shorter
    path terminates the set).
    """
    
    resource_name = "ElementDefinitionSlicing"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Text description of how slicing works (or not).
        Type `str`. """
        
        self.discriminator = None
        """ Element values that used to distinguish the slices.
        List of `str` items. """
        
        self.ordered = False
        """ If elements must be in same order as slices.
        Type `bool`. """
        
        self.rules = None
        """ closed | open | openAtEnd.
        Type `str`. """
        
        super(ElementDefinitionSlicing, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ElementDefinitionSlicing, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'discriminator' in jsondict:
            self.discriminator = jsondict['discriminator']
        if 'ordered' in jsondict:
            self.ordered = jsondict['ordered']
        if 'rules' in jsondict:
            self.rules = jsondict['rules']


class ElementDefinitionType(fhirelement.FHIRElement):
    """ Data type and Profile for this element.
    
    The data type or resource that the value of this element is permitted to
    be.
    """
    
    resource_name = "ElementDefinitionType"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.aggregation = None
        """ contained | referenced | bundled - how aggregated.
        List of `str` items. """
        
        self.code = None
        """ Name of Data type or Resource.
        Type `str`. """
        
        self.profile = None
        """ Profile.structure to apply.
        Type `str`. """
        
        super(ElementDefinitionType, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ElementDefinitionType, self).update_with_json(jsondict)
        if 'aggregation' in jsondict:
            self.aggregation = jsondict['aggregation']
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'profile' in jsondict:
            self.profile = jsondict['profile']

