#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import timing


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
    
    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("activity", "activity", CarePlanActivity, True),
            ("author", "author", fhirreference.FHIRReference, True),
            ("category", "category", codeableconcept.CodeableConcept, True),
            ("concern", "concern", fhirreference.FHIRReference, True),
            ("goal", "goal", fhirreference.FHIRReference, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("modified", "modified", fhirdate.FHIRDate, False),
            ("notes", "notes", str, False),
            ("participant", "participant", CarePlanParticipant, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("status", "status", str, False),
            ("support", "support", fhirreference.FHIRReference, True),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("actionResulting", "actionResulting", fhirreference.FHIRReference, True),
            ("detail", "detail", CarePlanActivityDetail, False),
            ("notes", "notes", str, False),
            ("reference", "reference", fhirreference.FHIRReference, False),
        ])
        return js


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
        
        self.prohibited = None
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
    
    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("category", "category", str, False),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("dailyAmount", "dailyAmount", quantity.Quantity, False),
            ("goal", "goal", fhirreference.FHIRReference, True),
            ("location", "location", fhirreference.FHIRReference, False),
            ("note", "note", str, False),
            ("performer", "performer", fhirreference.FHIRReference, True),
            ("product", "product", fhirreference.FHIRReference, False),
            ("prohibited", "prohibited", bool, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False),
            ("scheduledString", "scheduledString", str, False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False),
            ("status", "status", str, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(CarePlanParticipant, self).elementProperties()
        js.extend([
            ("member", "member", fhirreference.FHIRReference, False),
            ("role", "role", codeableconcept.CodeableConcept, False),
        ])
        return js

