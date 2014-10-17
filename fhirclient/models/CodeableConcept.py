#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-CodeableConcept.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import Coding
import FHIRElement


class CodeableConcept(FHIRElement.FHIRElement):
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
            self.coding = Coding.Coding.with_json(jsondict['coding'])
        if 'text' in jsondict:
            self.text = jsondict['text']

