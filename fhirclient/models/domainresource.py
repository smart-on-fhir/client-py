#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DomainResource) on 2015-04-08.
#  2015, SMART Health IT.


import narrative
import resource


class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.
    
    A resource that includes narrative, extensions, and contained resources.
    """
    
    resource_name = "DomainResource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(DomainResource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DomainResource, self).update_with_json(jsondict)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json_and_owner(jsondict['text'], self)

