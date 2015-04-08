#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Goal) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) of patient care.
    
    Describes the intended objective(s) of patient care, for example, weight
    loss, restoring an activity of daily living, etc.
    """
    
    resource_name = "Goal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who's responsible for creating Goal?.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.concern = None
        """ Health issues this goal addresses.
        List of `FHIRReference` items referencing `Condition, Observation, MedicationStatement, NutritionOrder, ProcedureRequest, RiskAssessment` (represented as `dict` in JSON). """
        
        self.description = None
        """ What's the desired outcome?.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Comments about the goal.
        Type `str`. """
        
        self.outcome = None
        """ What was end result of goal?.
        List of `GoalOutcome` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient for whom this goal is intended for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.priority = None
        """ high | medium |low.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | planned | in-progress | achieved | sustaining |
        cancelled | accepted | rejected.
        Type `str`. """
        
        self.statusDate = None
        """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.targetDate = None
        """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Goal, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Goal, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'concern' in jsondict:
            self.concern = fhirreference.FHIRReference.with_json_and_owner(jsondict['concern'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'outcome' in jsondict:
            self.outcome = GoalOutcome.with_json_and_owner(jsondict['outcome'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'priority' in jsondict:
            self.priority = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['priority'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'statusDate' in jsondict:
            self.statusDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['statusDate'], self)
        if 'targetDate' in jsondict:
            self.targetDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['targetDate'], self)


class GoalOutcome(fhirelement.FHIRElement):
    """ What was end result of goal?.
    
    Identifies the change (or lack of change) at the point where the goal was
    deepmed to be cancelled or achieved.
    """
    
    resource_name = "GoalOutcome"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.resultCodeableConcept = None
        """ Code or observation that resulted from gual.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.resultReference = None
        """ Code or observation that resulted from gual.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        super(GoalOutcome, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(GoalOutcome, self).update_with_json(jsondict)
        if 'resultCodeableConcept' in jsondict:
            self.resultCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['resultCodeableConcept'], self)
        if 'resultReference' in jsondict:
            self.resultReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['resultReference'], self)

