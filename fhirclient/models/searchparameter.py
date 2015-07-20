#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2015-07-06.
#  2015, SMART Health IT.


from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement


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
        
        self.experimental = None
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
    
    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", str, False),
            ("contact", "contact", SearchParameterContact, True),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("experimental", "experimental", bool, False),
            ("name", "name", str, False),
            ("publisher", "publisher", str, False),
            ("requirements", "requirements", str, False),
            ("status", "status", str, False),
            ("target", "target", str, True),
            ("type", "type", str, False),
            ("url", "url", str, False),
            ("xpath", "xpath", str, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(SearchParameterContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js

