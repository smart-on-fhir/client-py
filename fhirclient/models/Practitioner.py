#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (practitioner.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import Address
import Attachment
import CodeableConcept
import Contact
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import HumanName
import Identifier
import Location
import Narrative
import Organization
import Period


class Practitioner(FHIRResource.FHIRResource):
    """ A person with a  formal responsibility in the provisioning of healthcare or
    related services.
    
    Scope and Usage Practitioner covers all individuals who are engaged in the
    healthcare process and healthcare-related services as part of their formal
    responsibilities and this Resource is used for attribution of activities
    and responsibilities to these individuals. Practitioners include (but are
    not limited to):
    
    * physicians, dentists, pharmacists
    * physician assistants, nurses, scribes
    * midwives, dietitians, therapists, optometrists, paramedics
    * medical technicians, laboratory scientists, prosthetic technicians,
    radiographers
    * social workers, professional home carers, official volunteers
    * receptionists handling patient registration
    * IT personnel merging or unmerging patient records
    """
    
    resource_name = "Practitioner"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Where practitioner can be found/visited.
        Type `Address` (represented as `dict` in JSON). """
        
        self.birthDate = None
        """ The date and time of birth for the practitioner.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.communication = None
        """ A language the practitioner is able to use in patient communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.gender = None
        """ Gender for administrative purposes.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ A identifier for the person as this agent.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.organization = None
        """ The represented organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.qualification = None
        """ Qualifications obtained by training and certification.
        List of `PractitionerQualification` items (represented as `dict` in JSON). """
        
        self.role = None
        """ Roles which this practitioner may perform.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the practitioner.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Practitioner, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Practitioner, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = Address.Address.with_json(jsondict['address'])
        if 'birthDate' in jsondict:
            self.birthDate = FHIRDate.FHIRDate.with_json(jsondict['birthDate'])
        if 'communication' in jsondict:
            self.communication = CodeableConcept.CodeableConcept.with_json(jsondict['communication'])
        if 'gender' in jsondict:
            self.gender = CodeableConcept.CodeableConcept.with_json(jsondict['gender'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'location' in jsondict:
            self.location = FHIRReference.FHIRReference.with_json_and_owner(jsondict['location'], self, Location.Location)
        if 'name' in jsondict:
            self.name = HumanName.HumanName.with_json(jsondict['name'])
        if 'organization' in jsondict:
            self.organization = FHIRReference.FHIRReference.with_json_and_owner(jsondict['organization'], self, Organization.Organization)
        if 'period' in jsondict:
            self.period = Period.Period.with_json(jsondict['period'])
        if 'photo' in jsondict:
            self.photo = Attachment.Attachment.with_json(jsondict['photo'])
        if 'qualification' in jsondict:
            self.qualification = PractitionerQualification.with_json(jsondict['qualification'])
        if 'role' in jsondict:
            self.role = CodeableConcept.CodeableConcept.with_json(jsondict['role'])
        if 'specialty' in jsondict:
            self.specialty = CodeableConcept.CodeableConcept.with_json(jsondict['specialty'])
        if 'telecom' in jsondict:
            self.telecom = Contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])


class PractitionerQualification(FHIRElement.FHIRElement):
    """ Qualifications obtained by training and certification.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Coded representation of the qualification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
            self.code = CodeableConcept.CodeableConcept.with_json(jsondict['code'])
        if 'issuer' in jsondict:
            self.issuer = FHIRReference.FHIRReference.with_json_and_owner(jsondict['issuer'], self, Organization.Organization)
        if 'period' in jsondict:
            self.period = Period.Period.with_json(jsondict['period'])

