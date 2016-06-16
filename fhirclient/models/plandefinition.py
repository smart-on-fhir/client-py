#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8522 (http://hl7.org/fhir/StructureDefinition/PlanDefinition) on 2016-06-16.
#  2016, SMART Health IT.


from . import domainresource

class PlanDefinition(domainresource.DomainResource):
    """ The definition of a plan for a series of actions, independent of any
    specific patient.
    
    This resource allows for the definition of an order set as a sharable,
    consumable, and executable artifact in support of clinical decision
    support.
    """
    
    resource_name = "PlanDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionDefinition = None
        """ Action defined by the plan.
        List of `PlanDefinitionActionDefinition` items (represented as `dict` in JSON). """
        
        self.library = None
        """ Logic used by the plan definition.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ The metadata for the plan definition.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        super(PlanDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinition, self).elementProperties()
        js.extend([
            ("actionDefinition", "actionDefinition", PlanDefinitionActionDefinition, True, None, False),
            ("library", "library", fhirreference.FHIRReference, True, None, False),
            ("moduleMetadata", "moduleMetadata", modulemetadata.ModuleMetadata, False, None, False),
        ])
        return js


from . import backboneelement

class PlanDefinitionActionDefinition(backboneelement.BackboneElement):
    """ Action defined by the plan.
    
    An action to be taken as part of the plan.
    """
    
    resource_name = "PlanDefinitionActionDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionDefinition = None
        """ A sub-action.
        List of `PlanDefinitionActionDefinition` items (represented as `dict` in JSON). """
        
        self.actionIdentifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.activityDefinition = None
        """ Description of the activity to be performed.
        Type `FHIRReference` referencing `ActivityDefinition` (represented as `dict` in JSON). """
        
        self.behavior = None
        """ Defines behaviors such as selection and grouping.
        List of `PlanDefinitionActionDefinitionBehavior` items (represented as `dict` in JSON). """
        
        self.concept = None
        """ The meaning of the action or its sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ Whether or not the action is applicable.
        Type `str`. """
        
        self.customization = None
        """ Dynamic aspects of the definition.
        List of `PlanDefinitionActionDefinitionCustomization` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Short description of the action.
        Type `str`. """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.label = None
        """ User-visible label for the action (e.g. 1. or A.).
        Type `str`. """
        
        self.relatedAction = None
        """ Relationship to another action.
        Type `PlanDefinitionActionDefinitionRelatedAction` (represented as `dict` in JSON). """
        
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
        
        self.triggerDefinition = None
        """ When the action should be triggered.
        Type `TriggerDefinition` (represented as `dict` in JSON). """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `str`. """
        
        super(PlanDefinitionActionDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinition, self).elementProperties()
        js.extend([
            ("actionDefinition", "actionDefinition", PlanDefinitionActionDefinition, True, None, False),
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, False),
            ("activityDefinition", "activityDefinition", fhirreference.FHIRReference, False, None, False),
            ("behavior", "behavior", PlanDefinitionActionDefinitionBehavior, True, None, False),
            ("concept", "concept", codeableconcept.CodeableConcept, True, None, False),
            ("condition", "condition", str, False, None, False),
            ("customization", "customization", PlanDefinitionActionDefinitionCustomization, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", attachment.Attachment, True, None, False),
            ("label", "label", str, False, None, False),
            ("relatedAction", "relatedAction", PlanDefinitionActionDefinitionRelatedAction, False, None, False),
            ("supportingEvidence", "supportingEvidence", attachment.Attachment, True, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("triggerDefinition", "triggerDefinition", triggerdefinition.TriggerDefinition, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class PlanDefinitionActionDefinitionBehavior(backboneelement.BackboneElement):
    """ Defines behaviors such as selection and grouping.
    
    A behavior associated with the action. Behaviors define how the action is
    to be presented and/or executed within the receiving environment.
    """
    
    resource_name = "PlanDefinitionActionDefinitionBehavior"
    
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
        
        super(PlanDefinitionActionDefinitionBehavior, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinitionBehavior, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("value", "value", coding.Coding, False, None, True),
        ])
        return js


class PlanDefinitionActionDefinitionCustomization(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.
    
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    
    resource_name = "PlanDefinitionActionDefinitionCustomization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expression = None
        """ An expression that provides the dynamic value for the customization.
        Type `str`. """
        
        self.path = None
        """ The path to the element to be set dynamically.
        Type `str`. """
        
        super(PlanDefinitionActionDefinitionCustomization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinitionCustomization, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


class PlanDefinitionActionDefinitionRelatedAction(backboneelement.BackboneElement):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    resource_name = "PlanDefinitionActionDefinitionRelatedAction"
    
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
        
        super(PlanDefinitionActionDefinitionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PlanDefinitionActionDefinitionRelatedAction, self).elementProperties()
        js.extend([
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, True),
            ("anchor", "anchor", str, False, None, False),
            ("offsetDuration", "offsetDuration", duration.Duration, False, "offset", False),
            ("offsetRange", "offsetRange", range.Range, False, "offset", False),
            ("relationship", "relationship", str, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import duration
from . import fhirreference
from . import identifier
from . import modulemetadata
from . import range
from . import triggerdefinition
