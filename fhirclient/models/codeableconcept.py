#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-CodeableConcept.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import coding
import fhirelement


class CodeableConcept(fhirelement.FHIRElement):
    """ Concept - reference to a terminology or just  text.
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
            self.coding = coding.Coding.with_json(jsondict['coding'])
        if 'text' in jsondict:
            self.text = jsondict['text']

