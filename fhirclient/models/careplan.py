#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (careplan.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import condition
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import location
import medication
import narrative
import patient
import period
import practitioner
import procedure
import quantity
import schedule


class CarePlan(fhirresource.FHIRResource):
    """ Healthcare plan for patient.
    
    Scope and Usage Care Plans are used in many of areas of healthcare with a
    variety of scopes. They can be as simple as a general practitioner keeping
    track of when their patient is next due for a tetanus immunization through
    to a detailed plan for an oncology patient covering diet, chemotherapy,
    radiation, lab work and counseling with detailed timing relationships, pre-
    conditions and goals.
    
    This resource takes an intermediate approach. It captures basic details
    about who is involved and what actions are intended without dealing in
    discrete data about dependencies and timing relationships. These can be
    supported where necessary using the extension mechanisms.
    
    Comments are welcome about the appropriateness of the proposed level of
    granularity, whether it's too much detail for what most systems need, or
    not sufficient for common essential use cases.
    """
    
    resource_name = "CarePlan"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.activity = None
        """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
        
        self.concern = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.goal = None
        """ Desired outcome of plan.
        List of `CarePlanGoal` items (represented as `dict` in JSON). """
        
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
        List of `CarePlanParticipant` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who care plan is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.status = None
        """ planned | active | completed.
        Type `str`. """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(CarePlan, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlan, self).update_with_json(jsondict)
        if 'activity' in jsondict:
            self.activity = CarePlanActivity.with_json(jsondict['activity'])
        if 'concern' in jsondict:
            self.concern = fhirreference.FHIRReference.with_json_and_owner(jsondict['concern'], self, condition.Condition)
        if 'goal' in jsondict:
            self.goal = CarePlanGoal.with_json(jsondict['goal'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'modified' in jsondict:
            self.modified = fhirdate.FHIRDate.with_json(jsondict['modified'])
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'participant' in jsondict:
            self.participant = CarePlanParticipant.with_json(jsondict['participant'])
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self, patient.Patient)
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class CarePlanParticipant(fhirelement.FHIRElement):
    """ Who's involved in plan?.
    
    Identifies all people and organizations who are expected to be involved in
    the care envisioned by this plan.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.member = None
        """ Who is involved.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of involvement.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CarePlanParticipant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlanParticipant, self).update_with_json(jsondict)
        if 'member' in jsondict:
            self.member = fhirreference.FHIRReference.with_json_and_owner(jsondict['member'], self, practitioner.Practitioner)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json(jsondict['role'])


class CarePlanGoal(fhirelement.FHIRElement):
    """ Desired outcome of plan.
    
    Describes the intended objective(s) of carrying out the Care Plan.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.concern = None
        """ Health issues this goal addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.description = None
        """ What's the desired outcome?.
        Type `str`. """
        
        self.notes = None
        """ Comments about the goal.
        Type `str`. """
        
        self.status = None
        """ in progress | achieved | sustaining | cancelled.
        Type `str`. """
        
        super(CarePlanGoal, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlanGoal, self).update_with_json(jsondict)
        if 'concern' in jsondict:
            self.concern = fhirreference.FHIRReference.with_json_and_owner(jsondict['concern'], self, condition.Condition)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'status' in jsondict:
            self.status = jsondict['status']


class CarePlanActivity(fhirelement.FHIRElement):
    """ Action to occur as part of plan.
    
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actionResulting = None
        """ Appointments, orders, etc..
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Activity details defined in specific resource.
        Type `FHIRReference` referencing `Procedure` (represented as `dict` in JSON). """
        
        self.goal = None
        """ Goals this activity relates to.
        List of `str` items. """
        
        self.notes = None
        """ Comments about the activity.
        Type `str`. """
        
        self.prohibited = False
        """ Do NOT do.
        Type `bool`. """
        
        self.simple = None
        """ Activity details summarised here.
        Type `CarePlanActivitySimple` (represented as `dict` in JSON). """
        
        self.status = None
        """ not started | scheduled | in progress | on hold | completed |
        cancelled.
        Type `str`. """
        
        super(CarePlanActivity, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlanActivity, self).update_with_json(jsondict)
        if 'actionResulting' in jsondict:
            self.actionResulting = fhirreference.FHIRReference.with_json_and_owner(jsondict['actionResulting'], self, fhirresource.FHIRResource)
        if 'detail' in jsondict:
            self.detail = fhirreference.FHIRReference.with_json_and_owner(jsondict['detail'], self, procedure.Procedure)
        if 'goal' in jsondict:
            self.goal = jsondict['goal']
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'prohibited' in jsondict:
            self.prohibited = jsondict['prohibited']
        if 'simple' in jsondict:
            self.simple = CarePlanActivitySimple.with_json(jsondict['simple'])
        if 'status' in jsondict:
            self.status = jsondict['status']


class CarePlanActivitySimple(fhirelement.FHIRElement):
    """ Activity details summarised here.
    
    A simple summary of details suitable for a general care plan system (e.g.
    form driven) that doesn't know about specific resources such as procedure
    etc.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ diet | drug | encounter | observation | procedure | supply | other.
        Type `str`. """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dailyAmount = None
        """ How much consumed/day?.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.details = None
        """ Extra info on activity occurrence.
        Type `str`. """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who's responsible?.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.product = None
        """ What's administered/supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ How much is administered/supplied/consumed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.timingPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingSchedule = None
        """ When activity is to occur.
        Type `Schedule` (represented as `dict` in JSON). """
        
        self.timingString = None
        """ When activity is to occur.
        Type `str`. """
        
        super(CarePlanActivitySimple, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlanActivitySimple, self).update_with_json(jsondict)
        if 'category' in jsondict:
            self.category = jsondict['category']
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'dailyAmount' in jsondict:
            self.dailyAmount = quantity.Quantity.with_json(jsondict['dailyAmount'])
        if 'details' in jsondict:
            self.details = jsondict['details']
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self, location.Location)
        if 'performer' in jsondict:
            self.performer = fhirreference.FHIRReference.with_json_and_owner(jsondict['performer'], self, practitioner.Practitioner)
        if 'product' in jsondict:
            self.product = fhirreference.FHIRReference.with_json_and_owner(jsondict['product'], self, medication.Medication)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json(jsondict['quantity'])
        if 'timingPeriod' in jsondict:
            self.timingPeriod = period.Period.with_json(jsondict['timingPeriod'])
        if 'timingSchedule' in jsondict:
            self.timingSchedule = schedule.Schedule.with_json(jsondict['timingSchedule'])
        if 'timingString' in jsondict:
            self.timingString = jsondict['timingString']

