#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DataElement) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import elementdefinition
from . import fhirdate
from . import fhirelement
from . import identifier


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
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date for this version of the data element.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.element = None
        """ Definition of element.
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        self.experimental = None
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Logical id to reference this data element.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.mapping = None
        """ External specification mapped to.
        List of `DataElementMapping` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Descriptive label for this element definition.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.stringency = None
        """ comparable | fully-specified | equivalent | convertable | scaleable
        | flexible.
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
    
    def elementProperties(self):
        js = super(DataElement, self).elementProperties()
        js.extend([
            ("contact", "contact", DataElementContact, True),
            ("copyright", "copyright", str, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("element", "element", elementdefinition.ElementDefinition, True),
            ("experimental", "experimental", bool, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("mapping", "mapping", DataElementMapping, True),
            ("name", "name", str, False),
            ("publisher", "publisher", str, False),
            ("status", "status", str, False),
            ("stringency", "stringency", str, False),
            ("url", "url", str, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True),
            ("version", "version", str, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(DataElementContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class DataElementMapping(fhirelement.FHIRElement):
    """ External specification mapped to.
    
    Identifies a specification (other than a terminology) that the elements
    which make up the DataElement have some correspondence with.
    """
    
    resource_name = "DataElementMapping"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comments = None
        """ Versions, Issues, Scope limitations etc..
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
    
    def elementProperties(self):
        js = super(DataElementMapping, self).elementProperties()
        js.extend([
            ("comments", "comments", str, False),
            ("identity", "identity", str, False),
            ("name", "name", str, False),
            ("uri", "uri", str, False),
        ])
        return js

