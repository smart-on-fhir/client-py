#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/DecisionSupportRule) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class DecisionSupportRule(domainresource.DomainResource):
    """ A decision support rule.
    
    This resource defines a decision support rule of the form [on Event] if
    Condition then Action.
    """
    
    resource_name = "DecisionSupportRule"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ "then" perform these actions.
        List of `ActionDefinition` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ "if" some condition is true.
        Type `str`. """
        
        self.library = None
        """ Logic used within the rule.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ Module information for the rule.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        self.trigger = None
        """ "when" the rule should be invoked.
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        
        super(DecisionSupportRule, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DecisionSupportRule, self).elementProperties()
        js.extend([
            ("action", "action", actiondefinition.ActionDefinition, True, None, False),
            ("condition", "condition", str, False, None, False),
            ("library", "library", fhirreference.FHIRReference, True, None, False),
            ("moduleMetadata", "moduleMetadata", modulemetadata.ModuleMetadata, False, None, False),
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, False),
        ])
        return js


from . import actiondefinition
from . import fhirreference
from . import modulemetadata
from . import triggerdefinition
