#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DataElement) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import contactpoint
import domainresource
import elementdefinition
import fhirdate
import fhirelement
import identifier


class DataElement(domainresource.DomainResource):
    """ Resource data element.
    
    The formal description of a single piece of information that can be
    gathered and reported.
    """
    
    resource_name = "DataElement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `DataElementContact` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or Publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the data element.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.element = None
        """ Definition of element.
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        self.experimental = False
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Logical id to reference this data element.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.mapping = None
        """ External specification mapped to.
        List of `DataElementMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Descriptive label for this element definition.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.specificity = None
        """ comparable | fully-specified | equivalent | convertable | scaleable
        | flexible.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None
        """ Globally unique logical id for data element.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Logical id for this version of the data element.
        Type `str`. """
        
        super(DataElement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DataElement, self).update_with_json(jsondict)
        if 'contact' in jsondict:
            self.contact = DataElementContact.with_json_and_owner(jsondict['contact'], self)
        if 'copyright' in jsondict:
            self.copyright = jsondict['copyright']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'element' in jsondict:
            self.element = elementdefinition.ElementDefinition.with_json_and_owner(jsondict['element'], self)
        if 'experimental' in jsondict:
            self.experimental = jsondict['experimental']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'mapping' in jsondict:
            self.mapping = DataElementMapping.with_json_and_owner(jsondict['mapping'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'publisher' in jsondict:
            self.publisher = jsondict['publisher']
        if 'specificity' in jsondict:
            self.specificity = jsondict['specificity']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'useContext' in jsondict:
            self.useContext = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['useContext'], self)
        if 'version' in jsondict:
            self.version = jsondict['version']


class DataElementContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "DataElementContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(DataElementContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DataElementContact, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class DataElementMapping(fhirelement.FHIRElement):
    """ External specification mapped to.
    
    Identifies a specification (other than a terminology) that the elements
    that make up the DataElement hav some correspondance with.
    """
    
    resource_name = "DataElementMapping"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc.
        Type `str`. """
        
        self.identity = None
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self.name = None
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.uri = None
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        super(DataElementMapping, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DataElementMapping, self).update_with_json(jsondict)
        if 'comments' in jsondict:
            self.comments = jsondict['comments']
        if 'identity' in jsondict:
            self.identity = jsondict['identity']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'uri' in jsondict:
            self.uri = jsondict['uri']

