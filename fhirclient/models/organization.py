#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (organization.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import address
import codeableconcept
import contactpoint
import fhirelement
import fhirreference
import fhirresource
import humanname
import identifier


class Organization(fhirresource.FHIRResource):
    """ A grouping of people or organizations with a common purpose.
    
    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, etc.
    """
    
    resource_name = "Organization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.active = False
        """ Whether the organization's record is still in active use.
        Type `bool`. """
        
        self.address = None
        """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Location(s) the organization uses to provide services.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name used for the organization.
        Type `str`. """
        
        self.partOf = None
        """ The organization of which this organization forms a part.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the organization.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of organization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Organization, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Organization, self).update_with_json(jsondict)
        if 'active' in jsondict:
            self.active = jsondict['active']
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'contact' in jsondict:
            self.contact = OrganizationContact.with_json_and_owner(jsondict['contact'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'partOf' in jsondict:
            self.partOf = fhirreference.FHIRReference.with_json_and_owner(jsondict['partOf'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class OrganizationContact(fhirelement.FHIRElement):
    """ Contact for the organization for a certain purpose.
    """
    
    resource_name = "OrganizationContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details (telephone, email, etc)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(OrganizationContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OrganizationContact, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'gender' in jsondict:
            self.gender = jsondict['gender']
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json_and_owner(jsondict['name'], self)
        if 'purpose' in jsondict:
            self.purpose = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['purpose'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)

