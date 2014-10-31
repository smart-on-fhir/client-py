#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (alert.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner


class Alert(fhirresource.FHIRResource):
    """ Key information to flag to healthcare providers.
    
    Scope and Usage The Alert resource provides a single interface for managing
    clinical and administrative facts that need to be brought to the attention
    of users of clinical systems. Examples can include many things. Patient's
    posing particular risks (falls, physical violence), patient's needing
    special accomodations (hard of hearing, use easy-open caps), administrative
    concerns (verify postal address, pre-payment required) or any other
    situation that needs to be brought to attention within the context of a
    particular workflow. (The workflow relevant to the issue can be identified
    by the category element.)
    
    Usually, resources specific to particular types of issues (health
    conditions, allergies, active medications will be used to communicate those
    issues. However, in some cases, particularly important information (a latex
    or severe food allergy) migt be highlighted as an Alert as well as the more
    typical resource.
    """
    
    resource_name = "Alert"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Alert creator.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
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
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Alert, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Alert, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self, practitioner.Practitioner)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json(jsondict['category'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])

