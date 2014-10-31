#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (relatedperson.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import address
import attachment
import codeableconcept
import contact
import fhirreference
import fhirresource
import humanname
import identifier
import narrative
import patient


class RelatedPerson(fhirresource.FHIRResource):
    """ An person that is related to a patient, but who is not a direct target of
    care.
    
    Scope and Usage RelatedPersons typically have a personal or non-healthcare-
    specific professional relationship to the patient. A RelatedPerson resource
    is primarily used for attribution of information, since RelatedPersons are
    often a source of information about the patient. For keeping information
    about persons for contact purposes for a patient, use a Patient's Contact
    element instead.
    
    Example RelatedPersons are:
    
    * A patient's wife or husband
    * A patient's relatives or friends
    * A neighbor bringing a patient to the hospital
    * The owner or trainer of a horse
    * A patient's attorney or guardian
    """
    
    resource_name = "RelatedPerson"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Address where the related person can be contacted or visited.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ Gender for administrative purposes.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ A Human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient this person is related to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ The nature of the relationship.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(RelatedPerson, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(RelatedPerson, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = address.Address.with_json(jsondict['address'])
        if 'gender' in jsondict:
            self.gender = codeableconcept.CodeableConcept.with_json(jsondict['gender'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json(jsondict['name'])
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self, patient.Patient)
        if 'photo' in jsondict:
            self.photo = attachment.Attachment.with_json(jsondict['photo'])
        if 'relationship' in jsondict:
            self.relationship = codeableconcept.CodeableConcept.with_json(jsondict['relationship'])
        if 'telecom' in jsondict:
            self.telecom = contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])

