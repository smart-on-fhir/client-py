# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ActivityDefinition).
# 2024, SMART Health IT.


from . import domainresource

class ActivityDefinition(domainresource.DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.
    
    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """
    
    resource_type = "ActivityDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.approvalDate = None
        """ When the activity definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._approvalDate = None
        """ Primitive extension for approvalDate. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ What part of body to perform on.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the activity definition.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.doNotPerform = None
        """ True if the activity should not be performed.
        Type `bool`. """
        self._doNotPerform = None
        """ Primitive extension for doNotPerform. Type `FHIRPrimitiveExtension` """
        
        self.dosage = None
        """ Detailed dosage instructions.
        List of `Dosage` items (represented as `dict` in JSON). """
        self._dosage = None
        """ Primitive extension for dosage. Type `FHIRPrimitiveExtension` """
        
        self.dynamicValue = None
        """ Dynamic aspects of the definition.
        List of `ActivityDefinitionDynamicValue` items (represented as `dict` in JSON). """
        self._dynamicValue = None
        """ Primitive extension for dynamicValue. Type `FHIRPrimitiveExtension` """
        
        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._editor = None
        """ Primitive extension for editor. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ When the activity definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._endorser = None
        """ Primitive extension for endorser. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the activity definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """
        self._intent = None
        """ Primitive extension for intent. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for activity definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ Kind of resource.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        self.lastReviewDate = None
        """ When the activity definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._lastReviewDate = None
        """ Primitive extension for lastReviewDate. Type `FHIRPrimitiveExtension` """
        
        self.library = None
        """ Logic used by the activity definition.
        List of `str` items. """
        self._library = None
        """ Primitive extension for library. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name for this activity definition (computer friendly).
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.observationRequirement = None
        """ What observations are required to perform this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._observationRequirement = None
        """ Primitive extension for observationRequirement. Type `FHIRPrimitiveExtension` """
        
        self.observationResultRequirement = None
        """ What observations must be produced by this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._observationResultRequirement = None
        """ Primitive extension for observationResultRequirement. Type `FHIRPrimitiveExtension` """
        
        self.participant = None
        """ Who should participate in the action.
        List of `ActivityDefinitionParticipant` items (represented as `dict` in JSON). """
        self._participant = None
        """ Primitive extension for participant. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.productCodeableConcept = None
        """ What's administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productCodeableConcept = None
        """ Primitive extension for productCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.productReference = None
        """ What's administered/supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._productReference = None
        """ Primitive extension for productReference. Type `FHIRPrimitiveExtension` """
        
        self.profile = None
        """ What profile the resource needs to conform to.
        Type `str`. """
        self._profile = None
        """ Primitive extension for profile. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ Why this activity definition is defined.
        Type `str`. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ How much is administered/consumed/supplied.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._relatedArtifact = None
        """ Primitive extension for relatedArtifact. Type `FHIRPrimitiveExtension` """
        
        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._reviewer = None
        """ Primitive extension for reviewer. Type `FHIRPrimitiveExtension` """
        
        self.specimenRequirement = None
        """ What specimens are required to perform this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._specimenRequirement = None
        """ Primitive extension for specimenRequirement. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subjectCodeableConcept = None
        """ Type of individual the activity definition is intended for.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._subjectCodeableConcept = None
        """ Primitive extension for subjectCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.subjectReference = None
        """ Type of individual the activity definition is intended for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subjectReference = None
        """ Primitive extension for subjectReference. Type `FHIRPrimitiveExtension` """
        
        self.subtitle = None
        """ Subordinate title of the activity definition.
        Type `str`. """
        self._subtitle = None
        """ Primitive extension for subtitle. Type `FHIRPrimitiveExtension` """
        
        self.timingAge = None
        """ When activity is to occur.
        Type `Age` (represented as `dict` in JSON). """
        self._timingAge = None
        """ Primitive extension for timingAge. Type `FHIRPrimitiveExtension` """
        
        self.timingDateTime = None
        """ When activity is to occur.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timingDateTime = None
        """ Primitive extension for timingDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timingDuration = None
        """ When activity is to occur.
        Type `Duration` (represented as `dict` in JSON). """
        self._timingDuration = None
        """ Primitive extension for timingDuration. Type `FHIRPrimitiveExtension` """
        
        self.timingPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """
        self._timingPeriod = None
        """ Primitive extension for timingPeriod. Type `FHIRPrimitiveExtension` """
        
        self.timingRange = None
        """ When activity is to occur.
        Type `Range` (represented as `dict` in JSON). """
        self._timingRange = None
        """ Primitive extension for timingRange. Type `FHIRPrimitiveExtension` """
        
        self.timingTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        self._timingTiming = None
        """ Primitive extension for timingTiming. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this activity definition (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.topic = None
        """ E.g. Education, Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._topic = None
        """ Primitive extension for topic. Type `FHIRPrimitiveExtension` """
        
        self.transform = None
        """ Transform to apply the template.
        Type `str`. """
        self._transform = None
        """ Primitive extension for transform. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this activity definition, represented as a
        URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.usage = None
        """ Describes the clinical usage of the activity definition.
        Type `str`. """
        self._usage = None
        """ Primitive extension for usage. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the activity definition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ActivityDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("_approvalDate", "_approvalDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", contactdetail.ContactDetail, True, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("_doNotPerform", "_doNotPerform", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dosage", "dosage", dosage.Dosage, True, None, False),
            ("_dosage", "_dosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dynamicValue", "dynamicValue", ActivityDefinitionDynamicValue, True, None, False),
            ("_dynamicValue", "_dynamicValue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("editor", "editor", contactdetail.ContactDetail, True, None, False),
            ("_editor", "_editor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endorser", "endorser", contactdetail.ContactDetail, True, None, False),
            ("_endorser", "_endorser", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intent", "intent", str, False, None, False),
            ("_intent", "_intent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, False),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("_lastReviewDate", "_lastReviewDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("library", "library", str, True, None, False),
            ("_library", "_library", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("observationRequirement", "observationRequirement", fhirreference.FHIRReference, True, None, False),
            ("_observationRequirement", "_observationRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("observationResultRequirement", "observationResultRequirement", fhirreference.FHIRReference, True, None, False),
            ("_observationResultRequirement", "_observationResultRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participant", "participant", ActivityDefinitionParticipant, True, None, False),
            ("_participant", "_participant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("_productCodeableConcept", "_productCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("_productReference", "_productReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("profile", "profile", str, False, None, False),
            ("_profile", "_profile", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedArtifact", "relatedArtifact", relatedartifact.RelatedArtifact, True, None, False),
            ("_relatedArtifact", "_relatedArtifact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reviewer", "reviewer", contactdetail.ContactDetail, True, None, False),
            ("_reviewer", "_reviewer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specimenRequirement", "specimenRequirement", fhirreference.FHIRReference, True, None, False),
            ("_specimenRequirement", "_specimenRequirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", codeableconcept.CodeableConcept, False, "subject", False),
            ("_subjectCodeableConcept", "_subjectCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subjectReference", "subjectReference", fhirreference.FHIRReference, False, "subject", False),
            ("_subjectReference", "_subjectReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subtitle", "subtitle", str, False, None, False),
            ("_subtitle", "_subtitle", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingAge", "timingAge", age.Age, False, "timing", False),
            ("_timingAge", "_timingAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDateTime", "timingDateTime", fhirdatetime.FHIRDateTime, False, "timing", False),
            ("_timingDateTime", "_timingDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("_timingDuration", "_timingDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("_timingPeriod", "_timingPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("_timingRange", "_timingRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("_timingTiming", "_timingTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, True, None, False),
            ("_topic", "_topic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("transform", "transform", str, False, None, False),
            ("_transform", "_transform", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usage", "usage", str, False, None, False),
            ("_usage", "_usage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    
    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """
    
    resource_type = "ActivityDefinitionDynamicValue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ An expression that provides the dynamic value for the customization.
        Type `Expression` (represented as `dict` in JSON). """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.path = None
        """ The path to the element to be set dynamically.
        Type `str`. """
        self._path = None
        """ Primitive extension for path. Type `FHIRPrimitiveExtension` """
        
        super(ActivityDefinitionDynamicValue, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, True),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("path", "path", str, False, None, True),
            ("_path", "_path", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.
    
    Indicates who should participate in performing the action described.
    """
    
    resource_type = "ActivityDefinitionParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.role = None
        """ E.g. Nurse, Surgeon, Parent, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ patient | practitioner | related-person | device.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ActivityDefinitionParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActivityDefinitionParticipant, self).elementProperties()
        js.extend([
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import age
from . import codeableconcept
from . import contactdetail
from . import dosage
from . import duration
from . import expression
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import relatedartifact
from . import timing
from . import usagecontext