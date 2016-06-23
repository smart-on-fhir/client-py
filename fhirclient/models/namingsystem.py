#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/NamingSystem) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.
    
    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """
    
    resource_name = "NamingSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Contact details of the publisher.
        List of `NamingSystemContact` items (represented as `dict` in JSON). """
        
        self.date = None
        """ Publication Date(/time).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ What does naming system identify?.
        Type `str`. """
        
        self.kind = None
        """ codesystem | identifier | root.
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
        """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uniqueId = None
        """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """
        
        self.usage = None
        """ How/where is it used.
        Type `str`. """
        
        self.useContext = None
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(NamingSystem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend([
            ("contact", "contact", NamingSystemContact, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("description", "description", str, False, None, False),
            ("kind", "kind", str, False, None, True),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("replacedBy", "replacedBy", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("uniqueId", "uniqueId", NamingSystemUniqueId, True, None, True),
            ("usage", "usage", str, False, None, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import backboneelement

class NamingSystemContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "NamingSystemContact"
    
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
        
        super(NamingSystemContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystemContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.
    
    Indicates how the system may be identified when referenced in electronic
    exchange.
    """
    
    resource_name = "NamingSystemUniqueId"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(NamingSystemUniqueId, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("preferred", "preferred", bool, False, None, False),
            ("type", "type", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import period
