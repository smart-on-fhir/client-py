#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 (http://hl7.org/fhir/StructureDefinition/RequestGroup) on 2019-10-12.
#  2019, SMART Health IT.


from . import domainresource

class RequestGroup(domainresource.DomainResource):
    """ A group of related requests.
    
    A group of related requests that can be used to capture intended activities
    that have inter-dependencies such as "give this medication after that one".
    """
    
    resource_type = "RequestGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Proposed actions, if any.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        self.author = None
        """ Device or practitioner that authored the request group.
        Type `FHIRReference` referencing `Device, Practitioner` (represented as `dict` in JSON). """
        
        self.authoredOn = None
        """ When the request group was authored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Fulfills plan, proposal, or order.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or Episode for the request group.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Instantiates protocol or definition.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.intent = None
        """ proposal | plan | order.
        Type `str`. """
        
        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        
        self.reasonCodeableConcept = None
        """ Reason for the request group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason for the request group.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended | cancelled | completed | entered-in-
        error | unknown.
        Type `str`. """
        
        self.subject = None
        """ Who the request group is about.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        super(RequestGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("intent", "intent", str, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class RequestGroupAction(backboneelement.BackboneElement):
    """ Proposed actions, if any.
    
    The actions, if any, produced by the evaluation of the artifact.
    """
    
    resource_type = "RequestGroupAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Sub action.
        List of `RequestGroupAction` items (represented as `dict` in JSON). """
        
        self.cardinalityBehavior = None
        """ single | multiple.
        Type `str`. """
        
        self.code = None
        """ Code representing the meaning of the action or sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Whether or not the action is applicable.
        List of `RequestGroupActionCondition` items (represented as `dict` in JSON). """
        
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
        """ Who should perform the action.
        List of `FHIRReference` items referencing `Patient, Person, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.precheckBehavior = None
        """ yes | no.
        Type `str`. """
        
        self.relatedAction = None
        """ Relationship to another action.
        List of `RequestGroupActionRelatedAction` items (represented as `dict` in JSON). """
        
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
        
        self.timingTiming = None
        """ When the action should take place.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.title = None
        """ User-visible title.
        Type `str`. """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(RequestGroupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("label", "label", str, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingDuration", "timingDuration", duration.Duration, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingRange", "timingRange", range.Range, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("title", "title", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class RequestGroupActionCondition(backboneelement.BackboneElement):
    """ Whether or not the action is applicable.
    
    An expression that describes applicability criteria, or start/stop
    conditions for the action.
    """
    
    resource_type = "RequestGroupActionCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the condition.
        Type `str`. """
        
        self.expression = None
        """ Boolean-valued expression.
        Type `str`. """
        
        self.kind = None
        """ applicability | start | stop.
        Type `str`. """
        
        self.language = None
        """ Language of the expression.
        Type `str`. """
        
        super(RequestGroupActionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("language", "language", str, False, None, False),
        ])
        return js


class RequestGroupActionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    resource_type = "RequestGroupActionRelatedAction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionId = None
        """ What action this is related to.
        Type `str`. """
        
        self.offsetDuration = None
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.offsetRange = None
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ before-start | before | before-end | concurrent-with-start |
        concurrent | concurrent-with-end | after-start | after | after-end.
        Type `str`. """
        
        super(RequestGroupActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + '.relatedartifact']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
