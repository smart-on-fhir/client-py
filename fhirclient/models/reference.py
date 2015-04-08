#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Reference) on 2015-04-08.
#  2015, SMART Health IT.


import fhirelement


class Reference(fhirelement.FHIRElement):
    """ A reference from one resource to another.
    """
    
    resource_name = "Reference"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.display = None
        """ Text alternative for the resource.
        Type `str`. """
        
        self.reference = None
        """ Relative, internal or absolute URL reference.
        Type `str`. """
        
        super(Reference, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Reference, self).update_with_json(jsondict)
        if 'display' in jsondict:
            self.display = jsondict['display']
        if 'reference' in jsondict:
            self.reference = jsondict['reference']

