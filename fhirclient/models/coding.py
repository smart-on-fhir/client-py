#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Coding.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirelement
import fhirreference
import valueset


class Coding(fhirelement.FHIRElement):
    """ A reference to a code defined by a terminology system.
    """
    
    resource_name = "Coding"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Symbol in syntax defined by the system.
        Type `str`. """
        
        self.display = None
        """ Representation defined by the system.
        Type `str`. """
        
        self.primary = False
        """ If this code was chosen directly by the user.
        Type `bool`. """
        
        self.system = None
        """ Identity of the terminology system.
        Type `str`. """
        
        self.valueSet = None
        """ Set this coding was chosen from.
        Type `FHIRReference` referencing `ValueSet` (represented as `dict` in JSON). """
        
        self.version = None
        """ Version of the system - if relevant.
        Type `str`. """
        
        super(Coding, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Coding, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'primary' in jsondict:
            self.primary = jsondict['primary']
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'valueSet' in jsondict:
            self.valueSet = fhirreference.FHIRReference.with_json_and_owner(jsondict['valueSet'], self, valueset.ValueSet)
        if 'version' in jsondict:
            self.version = jsondict['version']

