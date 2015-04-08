#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Resource) on 2015-04-08.
#  2015, SMART Health IT.


import fhirresource
import meta


class Resource(fhirresource.FHIRResource):
    """ Base Resource.
    
    Base Resource for everything.
    """
    
    resource_name = "Resource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.implicitRules = None
        """ A set of rules under which this content was created.
        Type `str`. """
        
        self.language = None
        """ Language of the resource content.
        Type `str`. """
        
        self.meta = None
        """ Metadata about the resource.
        Type `Meta` (represented as `dict` in JSON). """
        
        super(Resource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Resource, self).update_with_json(jsondict)
        if 'implicitRules' in jsondict:
            self.implicitRules = jsondict['implicitRules']
        if 'language' in jsondict:
            self.language = jsondict['language']
        if 'meta' in jsondict:
            self.meta = meta.Meta.with_json_and_owner(jsondict['meta'], self)

