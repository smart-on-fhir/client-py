#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/GuidanceResponse) on 2016-04-01.
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
        
        self.dataRequirement = None
        """ Additional required data.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.evaluationMessage = None
        """ Messages resulting from the evaluation of the artifact or artifacts.
        List of `FHIRReference` items referencing `OperationOutcome` (represented as `dict` in JSON). """
        
        self.module = None
        """ A reference to a knowledge module.
        Type `FHIRReference` referencing `DecisionSupportServiceModule, DecisionSupportRule` (represented as `dict` in JSON). """
        
        self.outputParameters = None
        """ The output parameters of the evaluation, if any.
        Type `FHIRReference` referencing `Parameters` (represented as `dict` in JSON). """
        
        self.requestId = None
        """ The id of the request associated with this response, if any.
        Type `str`. """
        
        self.status = None
        """ success | data-requested | data-required | in-progress | failure.
        Type `str`. """
        
        super(GuidanceResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponse, self).elementProperties()
        js.extend([
            ("action", "action", GuidanceResponseAction, True, None, False),
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("evaluationMessage", "evaluationMessage", fhirreference.FHIRReference, True, None, False),
            ("module", "module", fhirreference.FHIRReference, False, None, True),
            ("outputParameters", "outputParameters", fhirreference.FHIRReference, False, None, False),
            ("requestId", "requestId", str, False, None, False),
            ("status", "status", str, False, None, True),
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
        
        self.behavior = None
        """ Defines behaviors such as selection and grouping.
        List of `GuidanceResponseActionBehavior` items (represented as `dict` in JSON). """
        
        self.concept = None
        """ The meaning of the action or its sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Short description of the action.
        Type `str`. """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.label = None
        """ User-visible label for the action (e.g. 1. or A.).
        Type `str`. """
        
        self.participant = None
        """ Participant.
        List of `FHIRReference` items referencing `Patient, Person, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.relatedAction = None
        """ Relationship to another action.
        Type `GuidanceResponseActionRelatedAction` (represented as `dict` in JSON). """
        
        self.resource = None
        """ The target of the action.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.supportingEvidence = None
        """ Evidence that supports taking the action.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.textEquivalent = None
        """ Static text equivalent of the action, used if the dynamic aspects
        cannot be interpreted by the receiving system.
        Type `str`. """
        
        self.title = None
        """ User-visible title.
        Type `str`. """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `str`. """
        
        super(GuidanceResponseAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponseAction, self).elementProperties()
        js.extend([
            ("action", "action", GuidanceResponseAction, True, None, False),
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, False),
            ("behavior", "behavior", GuidanceResponseActionBehavior, True, None, False),
            ("concept", "concept", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", attachment.Attachment, True, None, False),
            ("label", "label", str, False, None, False),
            ("participant", "participant", fhirreference.FHIRReference, True, None, False),
            ("relatedAction", "relatedAction", GuidanceResponseActionRelatedAction, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("supportingEvidence", "supportingEvidence", attachment.Attachment, True, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class GuidanceResponseActionBehavior(backboneelement.BackboneElement):
    """ Defines behaviors such as selection and grouping.
    
    A behavior associated with the action. Behaviors define how the action is
    to be presented and/or executed within the receiving environment.
    """
    
    resource_name = "GuidanceResponseActionBehavior"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ The type of behavior (grouping, precheck, selection, cardinality,
        etc).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Specific behavior (e.g. required, at-most-one, single, etc).
        Type `Coding` (represented as `dict` in JSON). """
        
        super(GuidanceResponseActionBehavior, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GuidanceResponseActionBehavior, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("value", "value", coding.Coding, False, None, True),
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
        
        self.offsetQuantity = None
        """ Time offset for the relationship.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
        
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
            ("offsetQuantity", "offsetQuantity", quantity.Quantity, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import datarequirement
from . import fhirreference
from . import identifier
from . import quantity
from . import range
