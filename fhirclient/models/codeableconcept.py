#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (CodeableConcept.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import fhirelement


class CodeableConcept(fhirelement.FHIRElement):
    """ Concept - reference to a terminology or just  text.
    
    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    """
    
    resource_name = "CodeableConcept"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.coding = None
        """ Code defined by a terminology system.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Plain text representation of the concept.
        Type `str`. """
        
        super(CodeableConcept, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CodeableConcept, self).update_with_json(jsondict)
        if 'coding' in jsondict:
            self.coding = coding.Coding.with_json_and_owner(jsondict['coding'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']

