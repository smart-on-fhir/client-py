#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/DecisionSupportServiceModule) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class DecisionSupportServiceModule(domainresource.DomainResource):
    """ A description of decision support service functionality.
    
    The DecisionSupportServiceModule describes a unit of decision support
    functionality that is made available as a service, such as immunization
    modules or drug-drug interaction checking.
    """
    
    resource_name = "DecisionSupportServiceModule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dataRequirement = None
        """ Data requirements for the module.
        List of `DataRequirement` items (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ Metadata for the service module.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        self.parameter = None
        """ Parameters to the module.
        List of `ParameterDefinition` items (represented as `dict` in JSON). """
        
        self.trigger = None
        """ "when" the module should be invoked.
        List of `TriggerDefinition` items (represented as `dict` in JSON). """
        
        super(DecisionSupportServiceModule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DecisionSupportServiceModule, self).elementProperties()
        js.extend([
            ("dataRequirement", "dataRequirement", datarequirement.DataRequirement, True, None, False),
            ("moduleMetadata", "moduleMetadata", modulemetadata.ModuleMetadata, False, None, False),
            ("parameter", "parameter", parameterdefinition.ParameterDefinition, True, None, False),
            ("trigger", "trigger", triggerdefinition.TriggerDefinition, True, None, False),
        ])
        return js


from . import datarequirement
from . import modulemetadata
from . import parameterdefinition
from . import triggerdefinition
