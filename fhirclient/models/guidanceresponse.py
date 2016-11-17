#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2016-10-24.
#  2016, SMART Health IT.


from . import domainresource

class GuidanceResponse(domainresource.DomainResource):
    """ The formal response to a guidance request.
    
    A guidance response is the formal response to a guidance request, including
    any output parameters returned by the evaluation, as well as the
    description of any proposed actions to be taken.
    """
    
    resource_name = "GuidanceResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Proposed actions, if any.
        List of `GuidanceResponseAction` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or Episode during which the response was returned.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.dataRequirement = None
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.evaluationMessage = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items referencing `OperationOutcome` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.module = None
        """ A reference to a knowledge module.
        Type `FHIRReference` referencing `DecisionSupportServiceModule` (represented as `dict` in JSON). """
        
        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When the guidance response was processed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.outputParameters = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` referencing `Parameters` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Device returning the guidance.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason for the response.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason for the response.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.requestId = None
        """ The id of the request associated with this response, if any.
        Type `str`. """
        
        self.status = None
        """ success | data-requested | data-required | in-progress | failure.
        Type `str`. """
        
        self.subject = None
        """ Patient the request was performed for.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("action", "action", GuidanceResponseAction, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("module", "module", fhirreference.FHIRReference, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, None, False),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("requestId", "requestId", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class GuidanceResponseAction(backboneelement.BackboneElement):
    """ Proposed actions, if any.
    
    The actions, if any, produced by the evaluation of the artifact.
    """
    
    resource_name = "GuidanceResponseAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Sub action.
        List of `GuidanceResponseAction` items (represented as `dict` in JSON). """
        
        self.actionIdentifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.cardinalityBehavior = None
        """ single | multiple.
        Type `str`. """
        
        self.concept = None
        """ The meaning of the action or its sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Short description of the action.
        Type `str`. """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        
        self.groupingBehavior = None
        """ visual-group | logical-group | sentence-group.
        Type `str`. """
        
        self.label = None
        """ User-visible label for the action (e.g. 1. or A.).
        Type `str`. """
        
        self.participant = None
        """ Participant.
        List of `FHIRReference` items referencing `Patient, Person, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.precheckBehavior = None
        """ yes | no.
        Type `str`. """
        
        self.relatedAction = None
        """ Relationship to another action.
        Type `GuidanceResponseActionRelatedAction` (represented as `dict` in JSON). """
        
        self.requiredBehavior = None
        """ must | could | must-unless-documented.
        Type `str`. """
        
        self.resource = None
        """ The target of the action.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.selectionBehavior = None
        """ any | all | all-or-none | exactly-one | at-most-one | one-or-more.
        Type `str`. """
        
        self.textEquivalent = None
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `str`. """
        
        self.timingDateTime = None
        """ When the action should take place.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingDuration = None
        """ When the action should take place.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ When the action should take place.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingRange = None
        """ When the action should take place.
        Type `Range` (represented as `dict` in JSON). """
        
        self.title = None
        """ User-visible title.
        Type `str`. """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(GuidanceResponseAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponseAction, self).elementProperties()
        js.extend([
            ("action", "action", GuidanceResponseAction, True, None, False),
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("concept", "concept", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("relatedAction", "relatedAction", GuidanceResponseActionRelatedAction, False, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class GuidanceResponseActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    resource_name = "GuidanceResponseActionRelatedAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionIdentifier = None
        """ Identifier of the related action.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.anchor = None
        """ start | end.
        Type `str`. """
        
        self.offsetDuration = None
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.offsetRange = None
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ before | after.
        Type `str`. """
        
        super(GuidanceResponseActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponseActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, True),
            ("anchor", "anchor", str, False, None, False),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import coding
from . import datarequirement
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import relatedartifact
