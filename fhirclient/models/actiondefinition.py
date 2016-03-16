#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/ActionDefinition) on 2016-03-16.
#  2016, SMART Health IT.


from . import element

class ActionDefinition(element.Element):
    """ None.
    
    The definition of the actions that should be returned by evaluation of the
    artifact.
    """
    
    resource_name = "ActionDefinition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actionIdentifier = None
        """ None.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.actions = None
        """ None.
        List of `ActionDefinition` items (represented as `dict` in JSON). """
        
        self.behavior = None
        """ None.
        List of `ActionDefinitionBehavior` items (represented as `dict` in JSON). """
        
        self.concept = None
        """ None.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.customization = None
        """ None.
        List of `ActionDefinitionCustomization` items (represented as `dict` in JSON). """
        
        self.description = None
        """ None.
        Type `str`. """
        
        self.documentation = None
        """ None.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.number = None
        """ None.
        Type `str`. """
        
        self.participantType = None
        """ patient | practitioner | related-person.
        List of `str` items. """
        
        self.resource = None
        """ None.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.supportingEvidence = None
        """ None.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.textEquivalent = None
        """ None.
        Type `str`. """
        
        self.title = None
        """ None.
        Type `str`. """
        
        self.type = None
        """ create | update | remove | fire-event.
        Type `str`. """
        
        super(ActionDefinition, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ActionDefinition, self).elementProperties()
        js.extend([
            ("actionIdentifier", "actionIdentifier", identifier.Identifier, False, None, False),
            ("actions", "actions", ActionDefinition, True, None, False),
            ("behavior", "behavior", ActionDefinitionBehavior, True, None, False),
            ("concept", "concept", codeableconcept.CodeableConcept, True, None, False),
            ("customization", "customization", ActionDefinitionCustomization, True, None, False),
            ("description", "description", str, False, None, False),
            ("documentation", "documentation", attachment.Attachment, True, None, False),
            ("number", "number", str, False, None, False),
            ("participantType", "participantType", str, True, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("supportingEvidence", "supportingEvidence", attachment.Attachment, True, None, False),
            ("textEquivalent", "textEquivalent", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class ActionDefinitionBehavior(element.Element):
    """ None.
    
    A behavior associated with the action. Behaviors define how the action is
    to be presented and/or executed within the receiving environment.
    """
    
    resource_name = "ActionDefinitionBehavior"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.type = None
        """ None.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ None.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ActionDefinitionBehavior, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ActionDefinitionBehavior, self).elementProperties()
        js.extend([
            ("type", "type", coding.Coding, False, None, True),
            ("value", "value", coding.Coding, False, None, True),
        ])
        return js


class ActionDefinitionCustomization(element.Element):
    """ None.
    
    Customizations that should be applied to the statically defined resource.
    """
    
    resource_name = "ActionDefinitionCustomization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.expression = None
        """ None.
        Type `str`. """
        
        self.path = None
        """ None.
        Type `str`. """
        
        super(ActionDefinitionCustomization, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ActionDefinitionCustomization, self).elementProperties()
        js.extend([
            ("expression", "expression", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import coding
from . import fhirreference
from . import identifier
