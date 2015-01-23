#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (patient.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import address
import attachment
import codeableconcept
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import humanname
import identifier
import period


class Patient(fhirresource.FHIRResource):
    """ Information about a person or animal receiving health care services.
    
    Demographics and other administrative information about a person or animal
    receiving care or other health-related services.
    """
    
    resource_name = "Patient"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.active = False
        """ Whether this patient's record is in active use.
        Type `bool`. """
        
        self.address = None
        """ Addresses for the individual.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.animal = None
        """ If this patient is an animal (non-human).
        Type `PatientAnimal` (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The date and time of birth for the individual.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.careProvider = None
        """ Patient's nominated care provider.
        List of `FHIRReference` items referencing `Organization, Practitioner` (represented as `dict` in JSON). """
        
        self.communication = None
        """ Languages which may be used to communicate with the patient about
        his or her health.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ A contact party (e.g. guardian, partner, friend) for the patient.
        List of `PatientContact` items (represented as `dict` in JSON). """
        
        self.deceasedBoolean = False
        """ Indicates if the individual is deceased or not.
        Type `bool`. """
        
        self.deceasedDateTime = None
        """ Indicates if the individual is deceased or not.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ An identifier for the person as this patient.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.link = None
        """ Link to another patient resource that concerns the same actual
        person.
        List of `PatientLink` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ Organization that is the custodian of the patient record.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.maritalStatus = None
        """ Marital (civil) status of a person.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.multipleBirthBoolean = False
        """ Whether patient is part of a multiple birth.
        Type `bool`. """
        
        self.multipleBirthInteger = None
        """ Whether patient is part of a multiple birth.
        Type `int`. """
        
        self.name = None
        """ A name associated with the patient.
        List of `HumanName` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the individual.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Patient, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Patient, self).update_with_json(jsondict)
        if 'active' in jsondict:
            self.active = jsondict['active']
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'animal' in jsondict:
            self.animal = PatientAnimal.with_json_and_owner(jsondict['animal'], self)
        if 'birthDate' in jsondict:
            self.birthDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['birthDate'], self)
        if 'careProvider' in jsondict:
            self.careProvider = fhirreference.FHIRReference.with_json_and_owner(jsondict['careProvider'], self)
        if 'communication' in jsondict:
            self.communication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['communication'], self)
        if 'contact' in jsondict:
            self.contact = PatientContact.with_json_and_owner(jsondict['contact'], self)
        if 'deceasedBoolean' in jsondict:
            self.deceasedBoolean = jsondict['deceasedBoolean']
        if 'deceasedDateTime' in jsondict:
            self.deceasedDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['deceasedDateTime'], self)
        if 'gender' in jsondict:
            self.gender = jsondict['gender']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'link' in jsondict:
            self.link = PatientLink.with_json_and_owner(jsondict['link'], self)
        if 'managingOrganization' in jsondict:
            self.managingOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['managingOrganization'], self)
        if 'maritalStatus' in jsondict:
            self.maritalStatus = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['maritalStatus'], self)
        if 'multipleBirthBoolean' in jsondict:
            self.multipleBirthBoolean = jsondict['multipleBirthBoolean']
        if 'multipleBirthInteger' in jsondict:
            self.multipleBirthInteger = jsondict['multipleBirthInteger']
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json_and_owner(jsondict['name'], self)
        if 'photo' in jsondict:
            self.photo = attachment.Attachment.with_json_and_owner(jsondict['photo'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class PatientAnimal(fhirelement.FHIRElement):
    """ If this patient is an animal (non-human).
    
    This element has a value if the patient is an animal.
    """
    
    resource_name = "PatientAnimal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.breed = None
        """ E.g. Poodle, Angus.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.genderStatus = None
        """ E.g. Neutered, Intact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.species = None
        """ E.g. Dog, Cow.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PatientAnimal, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PatientAnimal, self).update_with_json(jsondict)
        if 'breed' in jsondict:
            self.breed = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['breed'], self)
        if 'genderStatus' in jsondict:
            self.genderStatus = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['genderStatus'], self)
        if 'species' in jsondict:
            self.species = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['species'], self)


class PatientContact(fhirelement.FHIRElement):
    """ A contact party (e.g. guardian, partner, friend) for the patient.
    """
    
    resource_name = "PatientContact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Address for the contact person.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Organization that is associated with the contact.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which this person or organization is valid to be
        contacted relating to this patient.
        Type `Period` (represented as `dict` in JSON). """
        
        self.relationship = None
        """ The kind of relationship.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(PatientContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PatientContact, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'gender' in jsondict:
            self.gender = jsondict['gender']
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json_and_owner(jsondict['name'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'relationship' in jsondict:
            self.relationship = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['relationship'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class PatientLink(fhirelement.FHIRElement):
    """ Link to another patient resource that concerns the same actual person.
    """
    
    resource_name = "PatientLink"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.other = None
        """ The other patient resource that the link refers to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.type = None
        """ replace | refer | seealso - type of link.
        Type `str`. """
        
        super(PatientLink, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PatientLink, self).update_with_json(jsondict)
        if 'other' in jsondict:
            self.other = fhirreference.FHIRReference.with_json_and_owner(jsondict['other'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']

