#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (namingsystem.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import contactpoint
import fhirelement
import fhirreference
import fhirresource
import humanname
import period


class NamingSystem(fhirresource.FHIRResource):
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
        """ driver | provider | patient | bank.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Who should be contacted for questions about namingsystem.
        Type `NamingSystemContact` (represented as `dict` in JSON). """
        
        self.country = None
        """ ISO 3-char country code.
        Type `str`. """
        
        self.description = None
        """ What does namingsystem identify?.
        Type `str`. """
        
        self.name = None
        """ Human-readable label.
        Type `str`. """
        
        self.replacedBy = None
        """ Use this instead.
        Type `FHIRReference` referencing `NamingSystem` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Who maintains system namespace?.
        Type `str`. """
        
        self.status = None
        """ proposed | active | retired.
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
    
    def update_with_json(self, jsondict):
        super(NamingSystem, self).update_with_json(jsondict)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'contact' in jsondict:
            self.contact = NamingSystemContact.with_json_and_owner(jsondict['contact'], self)
        if 'country' in jsondict:
            self.country = jsondict['country']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'replacedBy' in jsondict:
            self.replacedBy = fhirreference.FHIRReference.with_json_and_owner(jsondict['replacedBy'], self)
        if 'responsible' in jsondict:
            self.responsible = jsondict['responsible']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'uniqueId' in jsondict:
            self.uniqueId = NamingSystemUniqueId.with_json_and_owner(jsondict['uniqueId'], self)
        if 'usage' in jsondict:
            self.usage = jsondict['usage']


class NamingSystemContact(fhirelement.FHIRElement):
    """ Who should be contacted for questions about namingsystem.
    
    The person who can be contacted about this system registration entry.
    """
    
    resource_name = "NamingSystemContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Name of person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Phone, email, etc..
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(NamingSystemContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NamingSystemContact, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json_and_owner(jsondict['name'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


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
        
        self.preferred = False
        """ Is this the id that should be used for this type.
        Type `bool`. """
        
        self.type = None
        """ oid | uuid | uri | other.
        Type `str`. """
        
        self.value = None
        """ The unique identifier.
        Type `str`. """
        
        super(NamingSystemUniqueId, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NamingSystemUniqueId, self).update_with_json(jsondict)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'preferred' in jsondict:
            self.preferred = jsondict['preferred']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'value' in jsondict:
            self.value = jsondict['value']

