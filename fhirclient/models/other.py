#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (other.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier


class Other(fhirresource.FHIRResource):
    """ Resource for non-supported content.
    
    Other is a conformant for handling resource concepts not yet defined for
    FHIR or outside HL7's scope of interest.
    """
    
    resource_name = "Other"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who created.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.code = None
        """ Kind of Resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.created = None
        """ When created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Identifies the.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        super(Other, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Other, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)

