#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CarePlan) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class CarePlan(domainresource.DomainResource):
    """ Healthcare plan for patient or group.
    
    Describes the intention of how one or more practitioners intend to deliver
    care for a particular patient, group or community for a period of time,
    possibly limited to care for a specific condition or set of conditions.
    """
    
    resource_name = "CarePlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activity = None
        """ Action to occur as part of plan.
        List of `CarePlanActivity` items (represented as `dict` in JSON). """
        
        self.addresses = None
        """ Health issues this plan addresses.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
        self.author = None
        """ Who is responsible for contents of the plan.
        List of `FHIRReference` items referencing `Patient, Practitioner, RelatedPerson, Organization` (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of plan.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Created in context of.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.description = None
        """ Summary of nature of plan.
        Type `str`. """
        
        self.goal = None
        """ Desired outcome of plan.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this plan.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.modified = None
        """ When last updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.note = None
        """ Comments about the plan.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.participant = None
        """ Who's involved in plan?.
        List of `CarePlanParticipant` items (represented as `dict` in JSON). """
        
        self.period = None
        """ Time period plan covers.
        Type `Period` (represented as `dict` in JSON). """
        
        self.relatedPlan = None
        """ Plans related to this one.
        List of `CarePlanRelatedPlan` items (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | draft | active | completed | cancelled.
        Type `str`. """
        
        self.subject = None
        """ Who care plan is for.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.support = None
        """ Information considered as part of plan.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(CarePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlan, self).elementProperties()
        js.extend([
            ("activity", "activity", CarePlanActivity, True, None, False),
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("author", "author", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("modified", "modified", fhirdate.FHIRDate, False, None, False),
            ("note", "note", annotation.Annotation, False, None, False),
            ("participant", "participant", CarePlanParticipant, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("relatedPlan", "relatedPlan", CarePlanRelatedPlan, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("support", "support", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class CarePlanActivity(backboneelement.BackboneElement):
    """ Action to occur as part of plan.
    
    Identifies a planned action to occur as part of the plan.  For example, a
    medication to be used, lab tests to perform, self-monitoring, education,
    etc.
    """
    
    resource_name = "CarePlanActivity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actionResulting = None
        """ Appointments, orders, etc..
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.detail = None
        """ In-line definition of activity.
        Type `CarePlanActivityDetail` (represented as `dict` in JSON). """
        
        self.progress = None
        """ Comments about the activity status/progress.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.reference = None
        """ Activity details defined in specific resource.
        Type `FHIRReference` referencing `Appointment, CommunicationRequest, DeviceUseRequest, DiagnosticOrder, MedicationOrder, NutritionOrder, Order, ProcedureRequest, ProcessRequest, ReferralRequest, SupplyRequest, VisionPrescription` (represented as `dict` in JSON). """
        
        super(CarePlanActivity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivity, self).elementProperties()
        js.extend([
            ("actionResulting", "actionResulting", fhirreference.FHIRReference, True, None, False),
            ("detail", "detail", CarePlanActivityDetail, False, None, False),
            ("progress", "progress", annotation.Annotation, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class CarePlanActivityDetail(backboneelement.BackboneElement):
    """ In-line definition of activity.
    
    A simple summary of a planned activity suitable for a general care plan
    system (e.g. form driven) that doesn't know about specific resources such
    as procedure etc.
    """
    
    resource_name = "CarePlanActivityDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ diet | drug | encounter | observation | procedure | supply | other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dailyAmount = None
        """ How to consume/day?.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.description = None
        """ Extra info describing activity to perform.
        Type `str`. """
        
        self.goal = None
        """ Goals this activity relates to.
        List of `FHIRReference` items referencing `Goal` (represented as `dict` in JSON). """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who will be responsible?.
        List of `FHIRReference` items referencing `Practitioner, Organization, RelatedPerson, Patient` (represented as `dict` in JSON). """
        
        self.productCodeableConcept = None
        """ What is to be administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.productReference = None
        """ What is to be administered/supplied.
        Type `FHIRReference` referencing `Medication, Substance` (represented as `dict` in JSON). """
        
        self.prohibited = None
        """ Do NOT do.
        Type `bool`. """
        
        self.quantity = None
        """ How much to administer/supply/consume.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why activity should be done.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Condition triggering need for activity.
        List of `FHIRReference` items referencing `Condition` (represented as `dict` in JSON). """
        
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
        
        super(CarePlanActivityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanActivityDetail, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("dailyAmount", "dailyAmount", quantity.Quantity, False, None, False),
            ("description", "description", str, False, None, False),
            ("goal", "goal", fhirreference.FHIRReference, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("productCodeableConcept", "productCodeableConcept", codeableconcept.CodeableConcept, False, "product", False),
            ("productReference", "productReference", fhirreference.FHIRReference, False, "product", False),
            ("prohibited", "prohibited", bool, False, None, True),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False),
            ("scheduledString", "scheduledString", str, False, "scheduled", False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False, "scheduled", False),
            ("status", "status", str, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class CarePlanParticipant(backboneelement.BackboneElement):
    """ Who's involved in plan?.
    
    Identifies all people and organizations who are expected to be involved in
    the care envisioned by this plan.
    """
    
    resource_name = "CarePlanParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.member = None
        """ Who is involved.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Organization` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of involvement.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(CarePlanParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanParticipant, self).elementProperties()
        js.extend([
            ("member", "member", fhirreference.FHIRReference, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class CarePlanRelatedPlan(backboneelement.BackboneElement):
    """ Plans related to this one.
    
    Identifies CarePlans with some sort of formal relationship to the current
    plan.
    """
    
    resource_name = "CarePlanRelatedPlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ includes | replaces | fulfills.
        Type `str`. """
        
        self.plan = None
        """ Plan relationship exists with.
        Type `FHIRReference` referencing `CarePlan` (represented as `dict` in JSON). """
        
        super(CarePlanRelatedPlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CarePlanRelatedPlan, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("plan", "plan", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import timing
