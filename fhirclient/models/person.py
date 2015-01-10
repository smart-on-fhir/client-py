#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (person.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import address
import attachment
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import humanname
import identifier


class Person(fhirresource.FHIRResource):
    """ A generic person record.
    
    Demographics and administrative information about a person independent of a
    specific health-related context.
    """
    
    resource_name = "Person"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.active = False
        """ This person's record is in active use.
        Type `bool`. """
        
        self.address = None
        """ One or more addresses for the person.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The birth date for the person.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ A Human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Link to a resource that converns the same actual person.
        List of `PersonLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The Organization that is the custodian of the person record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the Person.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Person, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Person, self).update_with_json(jsondict)
        if 'active' in jsondict:
            self.active = jsondict['active']
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'birthDate' in jsondict:
            self.birthDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['birthDate'], self)
        if 'gender' in jsondict:
            self.gender = jsondict['gender']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'link' in jsondict:
            self.link = PersonLink.with_json_and_owner(jsondict['link'], self)
        if 'managingOrganization' in jsondict:
            self.managingOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['managingOrganization'], self)
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json_and_owner(jsondict['name'], self)
        if 'photo' in jsondict:
            self.photo = attachment.Attachment.with_json_and_owner(jsondict['photo'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class PersonLink(fhirelement.FHIRElement):
    """ Link to a resource that converns the same actual person.
    """
    
    resource_name = "PersonLink"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.assurance = None
        """ level1 | level2 | level3 | level4.
        Type `str`. """
        
        self.other = None
        """ The resource to which this actual person is associated.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Person` (represented as `dict` in JSON). """
        
        super(PersonLink, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PersonLink, self).update_with_json(jsondict)
        if 'assurance' in jsondict:
            self.assurance = jsondict['assurance']
        if 'other' in jsondict:
            self.other = fhirreference.FHIRReference.with_json_and_owner(jsondict['other'], self)

