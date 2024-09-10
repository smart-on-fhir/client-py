# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RequestGroup).
# 2024, SMART Health IT.


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
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.author = None
        """ Device or practitioner that authored the request group.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.authoredOn = None
        """ When the request group was authored.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._authoredOn = None
        """ Primitive extension for authoredOn. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ Fulfills plan, proposal, or order.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ What's being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        self._groupIdentifier = None
        """ Primitive extension for groupIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """
        self._intent = None
        """ Primitive extension for intent. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Additional notes about the response.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why the request group is needed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why the request group is needed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._replaces = None
        """ Primitive extension for replaces. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who the request group is about.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        super(RequestGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroup, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("_authoredOn", "_authoredOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("_groupIdentifier", "_groupIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("_replaces", "_replaces", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._action = None
        """ Primitive extension for action. Type `FHIRPrimitiveExtension` """
        
        self.cardinalityBehavior = None
        """ single | multiple.
        Type `str`. """
        self._cardinalityBehavior = None
        """ Primitive extension for cardinalityBehavior. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code representing the meaning of the action or sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.condition = None
        """ Whether or not the action is applicable.
        List of `RequestGroupActionCondition` items (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Short description of the action.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `RelatedArtifact` items (represented as `dict` in JSON). """
        self._documentation = None
        """ Primitive extension for documentation. Type `FHIRPrimitiveExtension` """
        
        self.groupingBehavior = None
        """ visual-group | logical-group | sentence-group.
        Type `str`. """
        self._groupingBehavior = None
        """ Primitive extension for groupingBehavior. Type `FHIRPrimitiveExtension` """
        
        self.participant = None
        """ Who should perform the action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._participant = None
        """ Primitive extension for participant. Type `FHIRPrimitiveExtension` """
        
        self.precheckBehavior = None
        """ yes | no.
        Type `str`. """
        self._precheckBehavior = None
        """ Primitive extension for precheckBehavior. Type `FHIRPrimitiveExtension` """
        
        self.prefix = None
        """ User-visible prefix for the action (e.g. 1. or A.).
        Type `str`. """
        self._prefix = None
        """ Primitive extension for prefix. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.relatedAction = None
        """ Relationship to another action.
        List of `RequestGroupActionRelatedAction` items (represented as `dict` in JSON). """
        self._relatedAction = None
        """ Primitive extension for relatedAction. Type `FHIRPrimitiveExtension` """
        
        self.requiredBehavior = None
        """ must | could | must-unless-documented.
        Type `str`. """
        self._requiredBehavior = None
        """ Primitive extension for requiredBehavior. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ The target of the action.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.selectionBehavior = None
        """ any | all | all-or-none | exactly-one | at-most-one | one-or-more.
        Type `str`. """
        self._selectionBehavior = None
        """ Primitive extension for selectionBehavior. Type `FHIRPrimitiveExtension` """
        
        self.textEquivalent = None
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `str`. """
        self._textEquivalent = None
        """ Primitive extension for textEquivalent. Type `FHIRPrimitiveExtension` """
        
        self.timingAge = None
        """ When the action should take place.
        Type `Age` (represented as `dict` in JSON). """
        self._timingAge = None
        """ Primitive extension for timingAge. Type `FHIRPrimitiveExtension` """
        
        self.timingDateTime = None
        """ When the action should take place.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timingDateTime = None
        """ Primitive extension for timingDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timingDuration = None
        """ When the action should take place.
        Type `Duration` (represented as `dict` in JSON). """
        self._timingDuration = None
        """ Primitive extension for timingDuration. Type `FHIRPrimitiveExtension` """
        
        self.timingPeriod = None
        """ When the action should take place.
        Type `Period` (represented as `dict` in JSON). """
        self._timingPeriod = None
        """ Primitive extension for timingPeriod. Type `FHIRPrimitiveExtension` """
        
        self.timingRange = None
        """ When the action should take place.
        Type `Range` (represented as `dict` in JSON). """
        self._timingRange = None
        """ Primitive extension for timingRange. Type `FHIRPrimitiveExtension` """
        
        self.timingTiming = None
        """ When the action should take place.
        Type `Timing` (represented as `dict` in JSON). """
        self._timingTiming = None
        """ Primitive extension for timingTiming. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ User-visible title.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(RequestGroupAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupAction, self).elementProperties()
        js.extend([
            ("action", "action", RequestGroupAction, True, None, False),
            ("_action", "_action", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("cardinalityBehavior", "cardinalityBehavior", str, False, None, False),
            ("_cardinalityBehavior", "_cardinalityBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("condition", "condition", RequestGroupActionCondition, True, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("documentation", "documentation", relatedartifact.RelatedArtifact, True, None, False),
            ("_documentation", "_documentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("groupingBehavior", "groupingBehavior", str, False, None, False),
            ("_groupingBehavior", "_groupingBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("_participant", "_participant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("precheckBehavior", "precheckBehavior", str, False, None, False),
            ("_precheckBehavior", "_precheckBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prefix", "prefix", str, False, None, False),
            ("_prefix", "_prefix", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedAction", "relatedAction", RequestGroupActionRelatedAction, True, None, False),
            ("_relatedAction", "_relatedAction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requiredBehavior", "requiredBehavior", str, False, None, False),
            ("_requiredBehavior", "_requiredBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("selectionBehavior", "selectionBehavior", str, False, None, False),
            ("_selectionBehavior", "_selectionBehavior", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("_textEquivalent", "_textEquivalent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.expression = None
        """ Boolean-valued expression.
        Type `Expression` (represented as `dict` in JSON). """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.kind = None
        """ applicability | start | stop.
        Type `str`. """
        self._kind = None
        """ Primitive extension for kind. Type `FHIRPrimitiveExtension` """
        
        super(RequestGroupActionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionCondition, self).elementProperties()
        js.extend([
            ("expression", "expression", expression.Expression, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("_kind", "_kind", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._actionId = None
        """ Primitive extension for actionId. Type `FHIRPrimitiveExtension` """
        
        self.offsetDuration = None
        """ Time offset for the relationship.
        Type `Duration` (represented as `dict` in JSON). """
        self._offsetDuration = None
        """ Primitive extension for offsetDuration. Type `FHIRPrimitiveExtension` """
        
        self.offsetRange = None
        """ Time offset for the relationship.
        Type `Range` (represented as `dict` in JSON). """
        self._offsetRange = None
        """ Primitive extension for offsetRange. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ before-start | before | before-end | concurrent-with-start |
        concurrent | concurrent-with-end | after-start | after | after-end.
        Type `str`. """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        super(RequestGroupActionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RequestGroupActionRelatedAction, self).elementProperties()
        js.extend([
            ("actionId", "actionId", str, False, None, True),
            ("_actionId", "_actionId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("_offsetDuration", "_offsetDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("_offsetRange", "_offsetRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", str, False, None, True),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import age
from . import annotation
from . import codeableconcept
from . import duration
from . import expression
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range
from . import relatedartifact
from . import timing