#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/OrderSet) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class OrderSet(domainresource.DomainResource):
    """ The definition of an order set.
    
    This resource allows for the definition of an order set as a sharable,
    consumable, and executable artifact in support of clinical decision
    support.
    """
    
    resource_name = "OrderSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Groups, sections, and line items of the order set.
        List of `ActionDefinition` items (represented as `dict` in JSON). """
        
        self.library = None
        """ Logic used by the orderset.
        List of `FHIRReference` items referencing `Library` (represented as `dict` in JSON). """
        
        self.moduleMetadata = None
        """ The metadata for the orderset.
        Type `ModuleMetadata` (represented as `dict` in JSON). """
        
        super(OrderSet, self).__init__(jsondict=jsondict, strict=strict)
    
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
