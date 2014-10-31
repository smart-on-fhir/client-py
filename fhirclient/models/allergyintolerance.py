#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (allergyintolerance.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import adversereaction
import fhirdate
import fhirreference
import fhirresource
import identifier
import narrative
import observation
import patient
import practitioner
import substance


class AllergyIntolerance(fhirresource.FHIRResource):
    """ Drug, food, environmental and others.
    
    Scope and Usage Allergy/Intolerance resources are used to provide
    information about adverse sensitivities to substances that lead to
    physiologic changes that are clinically observable. An adverse sensitivity
    is defined as:
    
    A condition expected to result in undesirable physiologic reaction to an
    amount of a substance that would not produce a reaction in most
    individuals. The substance is the trigger of an immunologic response that
    produces the observed physiologic changes, or in some instances
    nonimmunologic mechanisms that produce clinically identical physiologic
    changes. The immunologic response might be considered the actual cause of
    the reaction, but it is exposure to the trigger substance that is
    clinically observable.
    
    This definition excludes clinically identical episodes that may be caused
    by physical agents, such as heat, cold, sunlight, or vibration, by exercise
    activity, or by infectious agents. Those conditions caused by physical
    agents or infectious would be captured on the problem list (List/Condition
    Resources). The allergy/intolerance list is a list of conditions that
    represent a propensity unique to this individual for a reaction upon future
    exposure to a specified substance.
    
    Note that this specification draws a distinction between the patients
    condition/problem list and an allergy/intolerance list, even though
    allergies and intolerances are also conditions. This is because the
    distinction is a long established clinical workflow, even to patients.
    Asking an individual "if they have any problems" is not going to invoke an
    account of their past reactions to medications or foods. Instead, they are
    asked if they "have any allergies". An allergy/intolerance is also
    different in that a potential harm from exposure to an external substance
    that may be ordered by a provider in the course of their care but is not
    inherent to exposure to that substance for the general population.
    """
    
    resource_name = "AllergyIntolerance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.criticality = None
        """ fatal | high | medium | low.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.reaction = None
        """ Reactions associated with the sensitivity.
        List of `FHIRReference` items referencing `AdverseReaction` (represented as `dict` in JSON). """
        
        self.recordedDate = None
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recorder = None
        """ Who recorded the sensitivity.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.sensitivityTest = None
        """ Observations that confirm or refute.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """
        
        self.sensitivityType = None
        """ allergy | intolerance | unknown.
        Type `str`. """
        
        self.status = None
        """ suspected | confirmed | refuted | resolved.
        Type `str`. """
        
        self.subject = None
        """ Who the sensitivity is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.substance = None
        """ The substance that causes the sensitivity.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(AllergyIntolerance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AllergyIntolerance, self).update_with_json(jsondict)
        if 'criticality' in jsondict:
            self.criticality = jsondict['criticality']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'reaction' in jsondict:
            self.reaction = fhirreference.FHIRReference.with_json_and_owner(jsondict['reaction'], self, adversereaction.AdverseReaction)
        if 'recordedDate' in jsondict:
            self.recordedDate = fhirdate.FHIRDate.with_json(jsondict['recordedDate'])
        if 'recorder' in jsondict:
            self.recorder = fhirreference.FHIRReference.with_json_and_owner(jsondict['recorder'], self, practitioner.Practitioner)
        if 'sensitivityTest' in jsondict:
            self.sensitivityTest = fhirreference.FHIRReference.with_json_and_owner(jsondict['sensitivityTest'], self, observation.Observation)
        if 'sensitivityType' in jsondict:
            self.sensitivityType = jsondict['sensitivityType']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'substance' in jsondict:
            self.substance = fhirreference.FHIRReference.with_json_and_owner(jsondict['substance'], self, substance.Substance)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])

