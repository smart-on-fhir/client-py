#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (allergyintolerance.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import duration
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class AllergyIntolerance(fhirresource.FHIRResource):
    """ Allergy or Intolerance (generally: Risk Of Adverse reaction to a substance).
    
    Risk of harmful or undesirable, physiological response which is unique to
    an individual and associated with exposure to a substance.
    """
    
    resource_name = "AllergyIntolerance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ food | medication | environment - Category of Substance.
        Type `str`. """
        
        self.comment = None
        """ Additional text not captured in other fields.
        Type `str`. """
        
        self.criticality = None
        """ low | high | unassessible - Estimated potential clinical harm.
        Type `str`. """
        
        self.event = None
        """ Adverse Reaction Events linked to exposure to substance.
        List of `AllergyIntoleranceEvent` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastOccurence = None
        """ Date(/time) of last known occurence of a reaction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recordedDate = None
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recorder = None
        """ Who recorded the sensitivity.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ unconfirmed | confirmed | resolved | refuted.
        Type `str`. """
        
        self.subject = None
        """ Who the sensitivity is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.substance = None
        """ Substance, (or class) considered to be responsible for risk.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ immune | non-immune - Underlying mechanism (if known).
        Type `str`. """
        
        super(AllergyIntolerance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AllergyIntolerance, self).update_with_json(jsondict)
        if 'category' in jsondict:
            self.category = jsondict['category']
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'criticality' in jsondict:
            self.criticality = jsondict['criticality']
        if 'event' in jsondict:
            self.event = AllergyIntoleranceEvent.with_json_and_owner(jsondict['event'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'lastOccurence' in jsondict:
            self.lastOccurence = fhirdate.FHIRDate.with_json_and_owner(jsondict['lastOccurence'], self)
        if 'recordedDate' in jsondict:
            self.recordedDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['recordedDate'], self)
        if 'recorder' in jsondict:
            self.recorder = fhirreference.FHIRReference.with_json_and_owner(jsondict['recorder'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'substance' in jsondict:
            self.substance = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['substance'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']


class AllergyIntoleranceEvent(fhirelement.FHIRElement):
    """ Adverse Reaction Events linked to exposure to substance.
    
    Details about each Adverse Reaction Event linked to exposure to the
    identified Substance.
    """
    
    resource_name = "AllergyIntoleranceEvent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.certainty = None
        """ unlikely | likely | confirmed - clinical certainty about the
        specific substance.
        Type `str`. """
        
        self.comment = None
        """ Text about event not captured in other fields.
        Type `str`. """
        
        self.description = None
        """ Description of the event as a whole.
        Type `str`. """
        
        self.duration = None
        """ How long Manifestations persisted.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.exposureRoute = None
        """ How the subject was exposed to the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manifestation = None
        """ Clinical symptoms/signs associated with the Event.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.onset = None
        """ Date(/time) when manifestations showed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.severity = None
        """ mild | moderate | severe (of event as a whole).
        Type `str`. """
        
        self.substance = None
        """ Specific substance considered to be responsible for event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(AllergyIntoleranceEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AllergyIntoleranceEvent, self).update_with_json(jsondict)
        if 'certainty' in jsondict:
            self.certainty = jsondict['certainty']
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'duration' in jsondict:
            self.duration = duration.Duration.with_json_and_owner(jsondict['duration'], self)
        if 'exposureRoute' in jsondict:
            self.exposureRoute = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['exposureRoute'], self)
        if 'manifestation' in jsondict:
            self.manifestation = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['manifestation'], self)
        if 'onset' in jsondict:
            self.onset = fhirdate.FHIRDate.with_json_and_owner(jsondict['onset'], self)
        if 'severity' in jsondict:
            self.severity = jsondict['severity']
        if 'substance' in jsondict:
            self.substance = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['substance'], self)

