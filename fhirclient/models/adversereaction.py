#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (adversereaction.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner
import substance


class AdverseReaction(fhirresource.FHIRResource):
    """ Specific reactions to a substance.
    
    Scope and Usage Adverse Reaction resources are used to provide information
    about specific reactions to a substance. These are normally associated with
    an AllergyIntolerance resource, but can be reported on their own when no
    assumption of further reactions is being made, or when specific events are
    being described.
    """
    
    resource_name = "AdverseReaction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ When the reaction occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.didNotOccurFlag = False
        """ Indicates lack of reaction.
        Type `bool`. """
        
        self.exposure = None
        """ Suspected substance.
        List of `AdverseReactionExposure` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this adverse reaction.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.recorder = None
        """ Who recorded the reaction.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who had the reaction.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.symptom = None
        """ What was reaction?.
        List of `AdverseReactionSymptom` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(AdverseReaction, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AdverseReaction, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'didNotOccurFlag' in jsondict:
            self.didNotOccurFlag = jsondict['didNotOccurFlag']
        if 'exposure' in jsondict:
            self.exposure = AdverseReactionExposure.with_json(jsondict['exposure'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'recorder' in jsondict:
            self.recorder = fhirreference.FHIRReference.with_json_and_owner(jsondict['recorder'], self, practitioner.Practitioner)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'symptom' in jsondict:
            self.symptom = AdverseReactionSymptom.with_json(jsondict['symptom'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class AdverseReactionSymptom(fhirelement.FHIRElement):
    """ What was reaction?.
    
    The signs and symptoms that were observed as part of the reaction.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ E.g. Rash, vomiting.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.severity = None
        """ severe | serious | moderate | minor.
        Type `str`. """
        
        super(AdverseReactionSymptom, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AdverseReactionSymptom, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'severity' in jsondict:
            self.severity = jsondict['severity']


class AdverseReactionExposure(fhirelement.FHIRElement):
    """ Suspected substance.
    
    An exposure to a substance that preceded a reaction occurrence.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.causalityExpectation = None
        """ likely | unlikely | confirmed | unknown.
        Type `str`. """
        
        self.date = None
        """ When the exposure occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.substance = None
        """ Presumed causative substance.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        self.type = None
        """ drugadmin | immuniz | coincidental.
        Type `str`. """
        
        super(AdverseReactionExposure, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AdverseReactionExposure, self).update_with_json(jsondict)
        if 'causalityExpectation' in jsondict:
            self.causalityExpectation = jsondict['causalityExpectation']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'substance' in jsondict:
            self.substance = fhirreference.FHIRReference.with_json_and_owner(jsondict['substance'], self, substance.Substance)
        if 'type' in jsondict:
            self.type = jsondict['type']

