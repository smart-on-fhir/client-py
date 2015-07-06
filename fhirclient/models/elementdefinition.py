#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ElementDefinition) on 2015-07-06.
#  2015, SMART Health IT.


from . import address
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import humanname
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import signature
from . import timing


class ElementDefinition(fhirelement.FHIRElement):
    """ Definition of an elements in a resource or extension.
    
    Captures constraints on each element within the resource, profile, or
    extension.
    """
    
    resource_name = "ElementDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.alias = None
        """ Other names.
        List of `str` items. """
        
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
        
        self.defaultValueUri = None
        """ Specified value it missing from instance.
        Type `str`. """
        
        self.definition = None
        """ Full formal definition as narrative text.
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
        
        self.meaningWhenMissing = None
        """ Implicit meaning when this element is missing.
        Type `str`. """
        
        self.min = None
        """ Minimum Cardinality.
        Type `int`. """
        
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
        
        super(ElementDefinition, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend([
            ("alias", "alias", str, True),
            ("binding", "binding", ElementDefinitionBinding, False),
            ("code", "code", coding.Coding, True),
            ("comments", "comments", str, False),
            ("condition", "condition", str, True),
            ("constraint", "constraint", ElementDefinitionConstraint, True),
            ("defaultValueAddress", "defaultValueAddress", address.Address, False),
            ("defaultValueAttachment", "defaultValueAttachment", attachment.Attachment, False),
            ("defaultValueBase64Binary", "defaultValueBase64Binary", str, False),
            ("defaultValueBoolean", "defaultValueBoolean", bool, False),
            ("defaultValueCode", "defaultValueCode", str, False),
            ("defaultValueCodeableConcept", "defaultValueCodeableConcept", codeableconcept.CodeableConcept, False),
            ("defaultValueCoding", "defaultValueCoding", coding.Coding, False),
            ("defaultValueContactPoint", "defaultValueContactPoint", contactpoint.ContactPoint, False),
            ("defaultValueDate", "defaultValueDate", fhirdate.FHIRDate, False),
            ("defaultValueDateTime", "defaultValueDateTime", fhirdate.FHIRDate, False),
            ("defaultValueDecimal", "defaultValueDecimal", float, False),
            ("defaultValueHumanName", "defaultValueHumanName", humanname.HumanName, False),
            ("defaultValueIdentifier", "defaultValueIdentifier", identifier.Identifier, False),
            ("defaultValueInstant", "defaultValueInstant", fhirdate.FHIRDate, False),
            ("defaultValueInteger", "defaultValueInteger", int, False),
            ("defaultValuePeriod", "defaultValuePeriod", period.Period, False),
            ("defaultValueQuantity", "defaultValueQuantity", quantity.Quantity, False),
            ("defaultValueRange", "defaultValueRange", range.Range, False),
            ("defaultValueRatio", "defaultValueRatio", ratio.Ratio, False),
            ("defaultValueReference", "defaultValueReference", fhirreference.FHIRReference, False),
            ("defaultValueSignature", "defaultValueSignature", signature.Signature, False),
            ("defaultValueString", "defaultValueString", str, False),
            ("defaultValueTime", "defaultValueTime", fhirdate.FHIRDate, False),
            ("defaultValueTiming", "defaultValueTiming", timing.Timing, False),
            ("defaultValueUri", "defaultValueUri", str, False),
            ("definition", "definition", str, False),
            ("exampleAddress", "exampleAddress", address.Address, False),
            ("exampleAttachment", "exampleAttachment", attachment.Attachment, False),
            ("exampleBase64Binary", "exampleBase64Binary", str, False),
            ("exampleBoolean", "exampleBoolean", bool, False),
            ("exampleCode", "exampleCode", str, False),
            ("exampleCodeableConcept", "exampleCodeableConcept", codeableconcept.CodeableConcept, False),
            ("exampleCoding", "exampleCoding", coding.Coding, False),
            ("exampleContactPoint", "exampleContactPoint", contactpoint.ContactPoint, False),
            ("exampleDate", "exampleDate", fhirdate.FHIRDate, False),
            ("exampleDateTime", "exampleDateTime", fhirdate.FHIRDate, False),
            ("exampleDecimal", "exampleDecimal", float, False),
            ("exampleHumanName", "exampleHumanName", humanname.HumanName, False),
            ("exampleIdentifier", "exampleIdentifier", identifier.Identifier, False),
            ("exampleInstant", "exampleInstant", fhirdate.FHIRDate, False),
            ("exampleInteger", "exampleInteger", int, False),
            ("examplePeriod", "examplePeriod", period.Period, False),
            ("exampleQuantity", "exampleQuantity", quantity.Quantity, False),
            ("exampleRange", "exampleRange", range.Range, False),
            ("exampleRatio", "exampleRatio", ratio.Ratio, False),
            ("exampleReference", "exampleReference", fhirreference.FHIRReference, False),
            ("exampleSignature", "exampleSignature", signature.Signature, False),
            ("exampleString", "exampleString", str, False),
            ("exampleTime", "exampleTime", fhirdate.FHIRDate, False),
            ("exampleTiming", "exampleTiming", timing.Timing, False),
            ("exampleUri", "exampleUri", str, False),
            ("fixedAddress", "fixedAddress", address.Address, False),
            ("fixedAttachment", "fixedAttachment", attachment.Attachment, False),
            ("fixedBase64Binary", "fixedBase64Binary", str, False),
            ("fixedBoolean", "fixedBoolean", bool, False),
            ("fixedCode", "fixedCode", str, False),
            ("fixedCodeableConcept", "fixedCodeableConcept", codeableconcept.CodeableConcept, False),
            ("fixedCoding", "fixedCoding", coding.Coding, False),
            ("fixedContactPoint", "fixedContactPoint", contactpoint.ContactPoint, False),
            ("fixedDate", "fixedDate", fhirdate.FHIRDate, False),
            ("fixedDateTime", "fixedDateTime", fhirdate.FHIRDate, False),
            ("fixedDecimal", "fixedDecimal", float, False),
            ("fixedHumanName", "fixedHumanName", humanname.HumanName, False),
            ("fixedIdentifier", "fixedIdentifier", identifier.Identifier, False),
            ("fixedInstant", "fixedInstant", fhirdate.FHIRDate, False),
            ("fixedInteger", "fixedInteger", int, False),
            ("fixedPeriod", "fixedPeriod", period.Period, False),
            ("fixedQuantity", "fixedQuantity", quantity.Quantity, False),
            ("fixedRange", "fixedRange", range.Range, False),
            ("fixedRatio", "fixedRatio", ratio.Ratio, False),
            ("fixedReference", "fixedReference", fhirreference.FHIRReference, False),
            ("fixedSignature", "fixedSignature", signature.Signature, False),
            ("fixedString", "fixedString", str, False),
            ("fixedTime", "fixedTime", fhirdate.FHIRDate, False),
            ("fixedTiming", "fixedTiming", timing.Timing, False),
            ("fixedUri", "fixedUri", str, False),
            ("isModifier", "isModifier", bool, False),
            ("isSummary", "isSummary", bool, False),
            ("label", "label", str, False),
            ("mapping", "mapping", ElementDefinitionMapping, True),
            ("max", "max", str, False),
            ("maxLength", "maxLength", int, False),
            ("meaningWhenMissing", "meaningWhenMissing", str, False),
            ("min", "min", int, False),
            ("mustSupport", "mustSupport", bool, False),
            ("name", "name", str, False),
            ("nameReference", "nameReference", str, False),
            ("path", "path", str, False),
            ("patternAddress", "patternAddress", address.Address, False),
            ("patternAttachment", "patternAttachment", attachment.Attachment, False),
            ("patternBase64Binary", "patternBase64Binary", str, False),
            ("patternBoolean", "patternBoolean", bool, False),
            ("patternCode", "patternCode", str, False),
            ("patternCodeableConcept", "patternCodeableConcept", codeableconcept.CodeableConcept, False),
            ("patternCoding", "patternCoding", coding.Coding, False),
            ("patternContactPoint", "patternContactPoint", contactpoint.ContactPoint, False),
            ("patternDate", "patternDate", fhirdate.FHIRDate, False),
            ("patternDateTime", "patternDateTime", fhirdate.FHIRDate, False),
            ("patternDecimal", "patternDecimal", float, False),
            ("patternHumanName", "patternHumanName", humanname.HumanName, False),
            ("patternIdentifier", "patternIdentifier", identifier.Identifier, False),
            ("patternInstant", "patternInstant", fhirdate.FHIRDate, False),
            ("patternInteger", "patternInteger", int, False),
            ("patternPeriod", "patternPeriod", period.Period, False),
            ("patternQuantity", "patternQuantity", quantity.Quantity, False),
            ("patternRange", "patternRange", range.Range, False),
            ("patternRatio", "patternRatio", ratio.Ratio, False),
            ("patternReference", "patternReference", fhirreference.FHIRReference, False),
            ("patternSignature", "patternSignature", signature.Signature, False),
            ("patternString", "patternString", str, False),
            ("patternTime", "patternTime", fhirdate.FHIRDate, False),
            ("patternTiming", "patternTiming", timing.Timing, False),
            ("patternUri", "patternUri", str, False),
            ("representation", "representation", str, True),
            ("requirements", "requirements", str, False),
            ("short", "short", str, False),
            ("slicing", "slicing", ElementDefinitionSlicing, False),
            ("type", "type", ElementDefinitionType, True),
        ])
        return js


class ElementDefinitionBinding(fhirelement.FHIRElement):
    """ ValueSet details if this is coded.
    
    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept).
    """
    
    resource_name = "ElementDefinitionBinding"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Human explanation of the value set.
        Type `str`. """
        
        self.name = None
        """ Descriptive Name.
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
        
        super(ElementDefinitionBinding, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend([
            ("description", "description", str, False),
            ("name", "name", str, False),
            ("strength", "strength", str, False),
            ("valueSetReference", "valueSetReference", fhirreference.FHIRReference, False),
            ("valueSetUri", "valueSetUri", str, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend([
            ("human", "human", str, False),
            ("key", "key", str, False),
            ("name", "name", str, False),
            ("severity", "severity", str, False),
            ("xpath", "xpath", str, False),
        ])
        return js


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
        
        self.language = None
        """ Computable language of mapping.
        Type `str`. """
        
        self.map = None
        """ Details of the mapping.
        Type `str`. """
        
        super(ElementDefinitionMapping, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend([
            ("identity", "identity", str, False),
            ("language", "language", str, False),
            ("map", "map", str, False),
        ])
        return js


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
        
        self.ordered = None
        """ If elements must be in same order as slices.
        Type `bool`. """
        
        self.rules = None
        """ closed | open | openAtEnd.
        Type `str`. """
        
        super(ElementDefinitionSlicing, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend([
            ("description", "description", str, False),
            ("discriminator", "discriminator", str, True),
            ("ordered", "ordered", bool, False),
            ("rules", "rules", str, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend([
            ("aggregation", "aggregation", str, True),
            ("code", "code", str, False),
            ("profile", "profile", str, False),
        ])
        return js

