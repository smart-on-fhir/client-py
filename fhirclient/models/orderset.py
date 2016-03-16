#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/OrderSet) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class OrderSet(domainresource.DomainResource):
    """ The definition of an order set.
    
    This resource allows for the definition of an order set as a sharable,
    consumable, and executable artifact in support of clinical decision
    support.
    """
    
    resource_name = "OrderSet"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ None.
        List of `ActionDefinition` items (represented as `dict` in JSON). """
        
        self.library = None
        """ Logic used by the orderset.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ The metadata for the orderset.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        super(OrderSet, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(OrderSet, self).elementProperties()
        js.extend([
            ("action", "action", actiondefinition.ActionDefinition, True, None, False),
            ("library", "library", fhirreference.FHIRReference, True, None, False),
            ("moduleMetadata", "moduleMetadata", modulemetadata.ModuleMetadata, False, None, False),
        ])
        return js


from . import actiondefinition
from . import fhirreference
from . import modulemetadata
