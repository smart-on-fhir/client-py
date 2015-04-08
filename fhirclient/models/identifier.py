#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Identifier) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import fhirelement
import fhirreference
import period


class Identifier(fhirelement.FHIRElement):
    """ An identifier intended for computation.
    
    A technical identifier - identifies some entity uniquely and unambiguously.
    """
    
    resource_name = "Identifier"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.assigner = None
        """ Organization that issued id (may be just text).
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ The namespace for the identifier.
        Type `str`. """
        
        self.type = None
        """ Description of identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.use = None
        """ usual | official | temp | secondary (If known).
        Type `str`. """
        
        self.value = None
        """ The value that is unique.
        Type `str`. """
        
        super(Identifier, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Identifier, self).update_with_json(jsondict)
        if 'assigner' in jsondict:
            self.assigner = fhirreference.FHIRReference.with_json_and_owner(jsondict['assigner'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'use' in jsondict:
            self.use = jsondict['use']
        if 'value' in jsondict:
            self.value = jsondict['value']

