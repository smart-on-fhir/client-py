#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/DecisionSupportRule) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class DecisionSupportRule(domainresource.DomainResource):
    """ A decision support rule.
    
    This resource defines a decision support rule of the form [on Event] if
    Condition then Action. It is intended to be a shareable, computable
    definition of a actions that should be taken whenever some condition is met
    in response to a particular event or events.
    """
    
    resource_name = "DecisionSupportRule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(DecisionSupportRule, self).__init__(jsondict=jsondict, strict=strict)
    
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
