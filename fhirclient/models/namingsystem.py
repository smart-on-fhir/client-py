#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import period


class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.
    
    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    
    resource_name = "NamingSystem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ e.g. driver,  provider,  patient, bank etc.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `NamingSystemContact` items (represented as `dict` in JSON). """
        
        self.country = None
        """ ISO 3-char country code.
        Type `str`. """
        
        self.date = None
        """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ What does namingsystem identify?.
        Type `str`. """
        
        self.name = None
        """ Human-readable label.
        Type `str`. """
        
        self.publisher = None
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.replacedBy = None
        """ Use this instead.
        Type `FHIRReference` referencing `NamingSystem` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Who maintains system namespace?.
        Type `str`. """
        
        self.status = None
        """ draft | active | retired.
        Type `str`. """
        
        self.type = None
        """ codesystem | identifier | root.
        Type `str`. """
        
        self.uniqueId = None
        """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """
        
        self.usage = None
        """ How/where is it used.
        Type `str`. """
        
        super(NamingSystem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("contact", "contact", NamingSystemContact, True),
            ("country", "country", str, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("name", "name", str, False),
            ("publisher", "publisher", str, False),
            ("replacedBy", "replacedBy", fhirreference.FHIRReference, False),
            ("responsible", "responsible", str, False),
            ("status", "status", str, False),
            ("type", "type", str, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True),
            ("usage", "usage", str, False),
        ])
        return js


class NamingSystemContact(fhirelement.FHIRElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "NamingSystemContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(NamingSystemContact, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NamingSystemContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class NamingSystemUniqueId(fhirelement.FHIRElement):
    """ Unique identifiers used for system.
    
    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    
    resource_name = "NamingSystemUniqueId"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """
        
        self.preferred = None
        """ Is this the id that should be used for this type.
        Type `bool`. """
        
        self.type = None
        """ oid | uuid | uri | other.
        Type `str`. """
        
        self.value = None
        """ The unique identifier.
        Type `str`. """
        
        super(NamingSystemUniqueId, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False),
            ("preferred", "preferred", bool, False),
            ("type", "type", str, False),
            ("value", "value", str, False),
        ])
        return js

