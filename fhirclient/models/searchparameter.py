#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (searchparameter.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import contactpoint
import fhirresource


class SearchParameter(fhirresource.FHIRResource):
    """ Search Parameter for a resource.
    
    A Search Parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    
    resource_name = "SearchParameter"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.base = None
        """ The resource type this search parameter applies to.
        Type `str`. """
        
        self.description = None
        """ Documentation for  search parameter.
        Type `str`. """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Why this search parameter is defined.
        Type `str`. """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.telecom = None
        """ Contact information of the publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity.
        Type `str`. """
        
        self.url = None
        """ Literal URL used to reference this search parameter.
        Type `str`. """
        
        self.xpath = None
        """ XPath that extracts the values.
        Type `str`. """
        
        super(SearchParameter, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SearchParameter, self).update_with_json(jsondict)
        if 'base' in jsondict:
            self.base = jsondict['base']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'target' in jsondict:
            self.target = jsondict['target']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'xpath' in jsondict:
            self.xpath = jsondict['xpath']

