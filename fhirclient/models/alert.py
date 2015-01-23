#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (alert.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirreference
import fhirresource
import identifier


class Alert(fhirresource.FHIRResource):
    """ Key information to flag to healthcare providers.
    
    Prospective warnings of potential issues when providing care to the
    patient.
    """
    
    resource_name = "Alert"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Alert creator.
        Type `FHIRReference` referencing `Practitioner, Patient, Device` (represented as `dict` in JSON). """
        
        self.category = None
        """ Clinical, administrative, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Text of alert.
        Type `str`. """
        
        self.status = None
        """ active | inactive | entered in error.
        Type `str`. """
        
        self.subject = None
        """ Who is alert about?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(Alert, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Alert, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)

