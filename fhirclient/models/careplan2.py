#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (careplan2.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period


class CarePlan2(fhirresource.FHIRResource):
    """ Healthcare plan for patient.
    
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient for a period of time, possibly limited to
    care for a specific condition or set of conditions.
    """
    
    resource_name = "CarePlan2"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.activity = None
        """ CarePlan Activity.
        List of `FHIRReference` items referencing `ProcedureRequest, MedicationPrescription, DiagnosticOrder, ReferralRequest, CommunicationRequest, NutritionOrder` (represented as `dict` in JSON). """
        
        self.concern = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.goal = None
        """ CarePlan Goal.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.modified = None
        """ When last updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.notes = None
        """ Comments about the plan.
        Type `str`. """
        
        self.participant = None
        """ Who's involved in plan?.
        List of `CarePlan2Participant` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who care plan is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | active | completed.
        Type `str`. """
        
        super(CarePlan2, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlan2, self).update_with_json(jsondict)
        if 'activity' in jsondict:
            self.activity = fhirreference.FHIRReference.with_json_and_owner(jsondict['activity'], self)
        if 'concern' in jsondict:
            self.concern = fhirreference.FHIRReference.with_json_and_owner(jsondict['concern'], self)
        if 'goal' in jsondict:
            self.goal = fhirreference.FHIRReference.with_json_and_owner(jsondict['goal'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'modified' in jsondict:
            self.modified = fhirdate.FHIRDate.with_json_and_owner(jsondict['modified'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'participant' in jsondict:
            self.participant = CarePlan2Participant.with_json_and_owner(jsondict['participant'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']


class CarePlan2Participant(fhirelement.FHIRElement):
    """ Who's involved in plan?.
    
    Identifies all people and organizations who are expected to be involved in
    the care envisioned by this plan.
    """
    
    resource_name = "CarePlan2Participant"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.member = None
        """ Who is involved.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Organization` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of involvement.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CarePlan2Participant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlan2Participant, self).update_with_json(jsondict)
        if 'member' in jsondict:
            self.member = fhirreference.FHIRReference.with_json_and_owner(jsondict['member'], self)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)

