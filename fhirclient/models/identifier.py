#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (Identifier.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


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
        
        self.label = None
        """ Description of identifier.
        Type `str`. """
        
        self.period = None
        """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ The namespace for the identifier.
        Type `str`. """
        
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
        if 'label' in jsondict:
            self.label = jsondict['label']
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'use' in jsondict:
            self.use = jsondict['use']
        if 'value' in jsondict:
            self.value = jsondict['value']

