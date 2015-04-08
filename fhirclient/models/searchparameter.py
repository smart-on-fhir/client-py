#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2015-04-08.
#  2015, SMART Health IT.


import contactpoint
import domainresource
import fhirdate
import fhirelement


class SearchParameter(domainresource.DomainResource):
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
        
        self.contact = None
        """ Contact details of the publisher.
        List of `SearchParameterContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Documentation for  search parameter.
        Type `str`. """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.name = None
        """ Name of search parameter.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None
        """ Why this search parameter is defined.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """
        
        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri.
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
        if 'contact' in jsondict:
            self.contact = SearchParameterContact.with_json_and_owner(jsondict['contact'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'requirements' in jsondict:
            self.requirements = jsondict['requirements']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'target' in jsondict:
            self.target = jsondict['target']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'xpath' in jsondict:
            self.xpath = jsondict['xpath']


class SearchParameterContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "SearchParameterContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(SearchParameterContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SearchParameterContact, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)

