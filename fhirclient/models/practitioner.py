#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Practitioner) on 2015-04-08.
#  2015, SMART Health IT.


import address
import attachment
import codeableconcept
import contactpoint
import domainresource
import fhirdate
import fhirelement
import fhirreference
import humanname
import identifier
import period


class Practitioner(domainresource.DomainResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    
    A person who is directly or indirectly involved in the provisioning of
    healthcare.
    """
    
    resource_name = "Practitioner"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Where practitioner can be found/visited.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The date  of birth for the practitioner.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.communication = None
        """ A language the practitioner is able to use in patient communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ A identifier for the person as this agent.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.practitionerRole = None
        """ The list of Roles/Organizations that the Practitioner is associated
        with.
        List of `PractitionerPractitionerRole` items (represented as `dict` in JSON). """
        
        self.qualification = None
        """ Qualifications obtained by training and certification.
        List of `PractitionerQualification` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the practitioner.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(Practitioner, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Practitioner, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'birthDate' in jsondict:
            self.birthDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['birthDate'], self)
        if 'communication' in jsondict:
            self.communication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['communication'], self)
        if 'gender' in jsondict:
            self.gender = jsondict['gender']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json_and_owner(jsondict['name'], self)
        if 'photo' in jsondict:
            self.photo = attachment.Attachment.with_json_and_owner(jsondict['photo'], self)
        if 'practitionerRole' in jsondict:
            self.practitionerRole = PractitionerPractitionerRole.with_json_and_owner(jsondict['practitionerRole'], self)
        if 'qualification' in jsondict:
            self.qualification = PractitionerQualification.with_json_and_owner(jsondict['qualification'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class PractitionerPractitionerRole(fhirelement.FHIRElement):
    """ The list of Roles/Organizations that the Practitioner is associated with.
    """
    
    resource_name = "PractitionerPractitionerRole"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.healthcareService = None
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items referencing `HealthcareService` (represented as `dict` in JSON). """
        
        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.managingOrganization = None
        """ The Organization where the Practitioner performs the roles
        associated.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        
        self.role = None
        """ Roles which this practitioner may perform.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(PractitionerPractitionerRole, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PractitionerPractitionerRole, self).update_with_json(jsondict)
        if 'healthcareService' in jsondict:
            self.healthcareService = fhirreference.FHIRReference.with_json_and_owner(jsondict['healthcareService'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'managingOrganization' in jsondict:
            self.managingOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['managingOrganization'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)
        if 'specialty' in jsondict:
            self.specialty = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['specialty'], self)


class PractitionerQualification(fhirelement.FHIRElement):
    """ Qualifications obtained by training and certification.
    """
    
    resource_name = "PractitionerQualification"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Coded representation of the qualification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ An identifier for this qualification for the practitioner.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issuer = None
        """ Organization that regulates and issues the qualification.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period during which the qualification is valid.
        Type `Period` (represented as `dict` in JSON). """
        
        super(PractitionerQualification, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PractitionerQualification, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'issuer' in jsondict:
            self.issuer = fhirreference.FHIRReference.with_json_and_owner(jsondict['issuer'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)

