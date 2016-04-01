#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/ActionDefinition) on 2016-04-01.
#  2016, SMART Health IT.


from . import element

class ActionDefinition(element.Element):
    """ The definition of an action to be performed.
    
    The definition of an action to be performed. Some aspects of the definition
    are specified statically, and some aspects can be specified dynamically by
    referencing logic defined in a library.
    """
    
    resource_name = "ActionDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ A sub-action.
        List of `ActionDefinition` items (represented as `dict` in JSON). """
        
        self.actionIdentifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.behavior = None
        """ Defines behaviors such as selection and grouping.
        List of `ActionDefinitionBehavior` items (represented as `dict` in JSON). """
        
        self.concept = None
        """ The meaning of the action or its sub-actions.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.customization = None
        """ Dynamic aspects of the definition.
        List of `ActionDefinitionCustomization` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Short description of the action.
        Type `str`. """
        
        self.documentation = None
        """ Supporting documentation for the intended performer of the action.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.label = None
        """ User-visible label for the action (e.g. 1. or A.).
        Type `str`. """
        
        self.participantType = None
        """ patient | practitioner | related-person.
        List of `str` items. """
        
        self.relatedAction = None
        """ Relationship to another action.
        Type `ActionDefinitionRelatedAction` (represented as `dict` in JSON). """
        
        self.resource = None
        """ Static portion of the action definition.
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
        
        super(ActionDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActionDefinition, self).elementProperties()
        js.extend([
            ("action", "action", ActionDefinition, True, None, False),
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, False),
            ("behavior", "behavior", ActionDefinitionBehavior, True, None, False),
            ("concept", "concept", codeableconcept.CodeableConcept, True, None, False),
            ("customization", "customization", ActionDefinitionCustomization, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", attachment.Attachment, True, None, False),
            ("label", "label", str, False, None, False),
            ("participantType", "participantType", str, True, None, False),
            ("relatedAction", "relatedAction", ActionDefinitionRelatedAction, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("supportingEvidence", "supportingEvidence", attachment.Attachment, True, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class ActionDefinitionBehavior(element.Element):
    """ Defines behaviors such as selection and grouping.
    
    A behavior associated with the action. Behaviors define how the action is
    to be presented and/or executed within the receiving environment.
    """
    
    resource_name = "ActionDefinitionBehavior"
    
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
        
        super(ActionDefinitionBehavior, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActionDefinitionBehavior, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("value", "value", coding.Coding, False, None, True),
        ])
        return js


class ActionDefinitionCustomization(element.Element):
    """ Dynamic aspects of the definition.
    
    Customizations that should be applied to the statically defined resource.
    For example, if the dosage of a medication must be computed based on the
    patient's weight, a customization would be used to specify an expression
    that calculated the weight, and the path on the resource that would contain
    the result.
    """
    
    resource_name = "ActionDefinitionCustomization"
    
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
        
        super(ActionDefinitionCustomization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActionDefinitionCustomization, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


class ActionDefinitionRelatedAction(element.Element):
    """ Relationship to another action.
    
    A relationship to another action such as "before" or "30-60 minutes after
    start of".
    """
    
    resource_name = "ActionDefinitionRelatedAction"
    
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
        
        super(ActionDefinitionRelatedAction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ActionDefinitionRelatedAction, self).elementProperties()
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
from . import fhirreference
from . import identifier
from . import quantity
from . import range
