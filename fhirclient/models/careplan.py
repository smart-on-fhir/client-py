#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period
import quantity
import timing


class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient.
    
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient for a period of time, possibly limited to
    care for a specific condition or set of conditions.
    """
    
    resource_name = "CarePlan"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.activity = None
        """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
        
        self.author = None
        """ Who is responsible for plan.
        List of `FHIRReference` items referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.concern = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.goal = None
        """ Desired outcome of plan.
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
        
        self.support = None
        """ Information considered as part of plan.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(CarePlan, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlan, self).update_with_json(jsondict)
        if 'activity' in jsondict:
            self.activity = CarePlanActivity.with_json_and_owner(jsondict['activity'], self)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
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
            self.participant = CarePlanParticipant.with_json_and_owner(jsondict['participant'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'support' in jsondict:
            self.support = fhirreference.FHIRReference.with_json_and_owner(jsondict['support'], self)


class CarePlanActivity(fhirelement.FHIRElement):
    """ Action to occur as part of plan.
    
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    
    resource_name = "CarePlanActivity"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actionResulting = None
        """ Appointments, orders, etc..
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.detail = None
        """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """
        
        self.notes = None
        """ Comments about the activity.
        Type `str`. """
        
        self.reference = None
        """ Activity details defined in specific resource.
        Type `FHIRReference` referencing `Appointment, CommunicationRequest, DeviceUseRequest, DiagnosticOrder, MedicationPrescription, NutritionOrder, Order, ProcedureRequest, ProcessRequest, ReferralRequest, Supply, VisionPrescription` (represented as `dict` in JSON). """
        
        super(CarePlanActivity, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlanActivity, self).update_with_json(jsondict)
        if 'actionResulting' in jsondict:
            self.actionResulting = fhirreference.FHIRReference.with_json_and_owner(jsondict['actionResulting'], self)
        if 'detail' in jsondict:
            self.detail = CarePlanActivityDetail.with_json_and_owner(jsondict['detail'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'reference' in jsondict:
            self.reference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reference'], self)


class CarePlanActivityDetail(fhirelement.FHIRElement):
    """ In-line definition of activity.
    
    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    
    resource_name = "CarePlanActivityDetail"
    
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
        """ How to consume/day?.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.goal = None
        """ Goals this activity relates to.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.note = None
        """ Extra info on activity occurrence.
        Type `str`. """
        
        self.performer = None
        """ Who will be responsible?.
        List of `FHIRReference` items referencing `Practitioner, Organization, RelatedPerson, Patient` (represented as `dict` in JSON). """
        
        self.product = None
        """ What is to be administered/supplied.
        Type `FHIRReference` referencing `Medication, Substance` (represented as `dict` in JSON). """
        
        self.prohibited = False
        """ Do NOT do.
        Type `bool`. """
        
        self.quantity = None
        """ How much to administer/supply/consume.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Why activity should be done.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why activity should be done.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.scheduledPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledString = None
        """ When activity is to occur.
        Type `str`. """
        
        self.scheduledTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.status = None
        """ not-started | scheduled | in-progress | on-hold | completed |
        cancelled.
        Type `str`. """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CarePlanActivityDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlanActivityDetail, self).update_with_json(jsondict)
        if 'category' in jsondict:
            self.category = jsondict['category']
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'dailyAmount' in jsondict:
            self.dailyAmount = quantity.Quantity.with_json_and_owner(jsondict['dailyAmount'], self)
        if 'goal' in jsondict:
            self.goal = fhirreference.FHIRReference.with_json_and_owner(jsondict['goal'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'performer' in jsondict:
            self.performer = fhirreference.FHIRReference.with_json_and_owner(jsondict['performer'], self)
        if 'product' in jsondict:
            self.product = fhirreference.FHIRReference.with_json_and_owner(jsondict['product'], self)
        if 'prohibited' in jsondict:
            self.prohibited = jsondict['prohibited']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'reasonCodeableConcept' in jsondict:
            self.reasonCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonCodeableConcept'], self)
        if 'reasonReference' in jsondict:
            self.reasonReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reasonReference'], self)
        if 'scheduledPeriod' in jsondict:
            self.scheduledPeriod = period.Period.with_json_and_owner(jsondict['scheduledPeriod'], self)
        if 'scheduledString' in jsondict:
            self.scheduledString = jsondict['scheduledString']
        if 'scheduledTiming' in jsondict:
            self.scheduledTiming = timing.Timing.with_json_and_owner(jsondict['scheduledTiming'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'statusReason' in jsondict:
            self.statusReason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['statusReason'], self)


class CarePlanParticipant(fhirelement.FHIRElement):
    """ Who's involved in plan?.
    
    Identifies all people and organizations who are expected to be involved in
    the care envisioned by this plan.
    """
    
    resource_name = "CarePlanParticipant"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.member = None
        """ Who is involved.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Organization` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of involvement.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CarePlanParticipant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CarePlanParticipant, self).update_with_json(jsondict)
        if 'member' in jsondict:
            self.member = fhirreference.FHIRReference.with_json_and_owner(jsondict['member'], self)
        if 'role' in jsondict:
            self.role = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['role'], self)

