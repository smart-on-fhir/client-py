#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (relatedperson.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import address
import attachment
import codeableconcept
import contactpoint
import fhirreference
import fhirresource
import humanname
import identifier
import period


class RelatedPerson(fhirresource.FHIRResource):
    """ An person that is related to a patient, but who is not a direct target of
    care.
    
    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    
    resource_name = "RelatedPerson"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Address where the related person can be contacted or visited.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None
        """ A Human identifier for this person.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the person.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient this person is related to.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period of time that this relationship is considered valid.
        Type `Period` (represented as `dict` in JSON). """
        
        self.photo = None
        """ Image of the person.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.relationship = None
        """ The nature of the relationship.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the person.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(RelatedPerson, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(RelatedPerson, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = address.Address.with_json_and_owner(jsondict['address'], self)
        if 'gender' in jsondict:
            self.gender = jsondict['gender']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'name' in jsondict:
            self.name = humanname.HumanName.with_json_and_owner(jsondict['name'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'photo' in jsondict:
            self.photo = attachment.Attachment.with_json_and_owner(jsondict['photo'], self)
        if 'relationship' in jsondict:
            self.relationship = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['relationship'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)

