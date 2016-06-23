#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SearchParameter) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class SearchParameter(domainresource.DomainResource):
    """ Search Parameter for a resource.
    
    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """
    
    resource_name = "SearchParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.base = None
        """ The resource type this search parameter applies to.
        Type `str`. """
        
        self.code = None
        """ Code used in URL.
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
        """ Informal name for this search parameter.
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
        """ Absolute URL used to reference this search parameter.
        Type `str`. """
        
        self.xpath = None
        """ XPath that extracts the values.
        Type `str`. """
        
        self.xpathUsage = None
        """ normal | phonetic | nearby | distance | other.
        Type `str`. """
        
        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend([
            ("base", "base", str, False, None, True),
            ("code", "code", str, False, None, True),
            ("contact", "contact", SearchParameterContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("status", "status", str, False, None, False),
            ("target", "target", str, True, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("xpath", "xpath", str, False, None, False),
            ("xpathUsage", "xpathUsage", str, False, None, False),
        ])
        return js


from . import backboneelement

class SearchParameterContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "SearchParameterContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(SearchParameterContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SearchParameterContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import contactpoint
from . import fhirdate
