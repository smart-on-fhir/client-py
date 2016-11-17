#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 (http://hl7.org/fhir/StructureDefinition/Goal) on 2016-10-24.
#  2016, SMART Health IT.


from . import domainresource

class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.
    
    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    
    resource_name = "Goal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addresses = None
        """ Issues addressed by this goal.
        List of `FHIRReference` items referencing `Condition, Observation, MedicationStatement, NutritionRequest, ProcedureRequest, RiskAssessment` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. Treatment, dietary, behavioral, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Code or text describing goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.expressedBy = None
        """ Who's responsible for creating Goal?.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments about the goal.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ What was end result of goal?.
        List of `GoalOutcome` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ high | medium |low.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startCodeableConcept = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startDate = None
        """ When goal pursuit begins.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ proposed | planned | accepted | rejected | in-progress | achieved |
        sustaining | on-hold | cancelled | on-target | ahead-of-target |
        behind-target.
        Type `str`. """
        
        self.statusDate = None
        """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who this goal is intended for.
        Type `FHIRReference` referencing `Patient, Group, Organization` (represented as `dict` in JSON). """
        
        self.targetDate = None
        """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.targetDuration = None
        """ Reach goal on or before.
        Type `Duration` (represented as `dict` in JSON). """
        
        super(Goal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("description", "description", codeableconcept.CodeableConcept, False, None, True),
            ("expressedBy", "expressedBy", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("outcome", "outcome", GoalOutcome, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, False, "start", False),
            ("startDate", "startDate", fhirdate.FHIRDate, False, "start", False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("targetDate", "targetDate", fhirdate.FHIRDate, False, "target", False),
            ("targetDuration", "targetDuration", duration.Duration, False, "target", False),
        ])
        return js


from . import backboneelement

class GoalOutcome(backboneelement.BackboneElement):
    """ What was end result of goal?.
    
    Identifies the change (or lack of change) at the point where the goal was
    deemed to be cancelled or achieved.
    """
    
    resource_name = "GoalOutcome"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.resultCodeableConcept = None
        """ Code or observation that resulted from goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.resultReference = None
        """ Code or observation that resulted from goal.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        super(GoalOutcome, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GoalOutcome, self).elementProperties()
        js.extend([
            ("resultCodeableConcept", "resultCodeableConcept", codeableconcept.CodeableConcept, False, "result", False),
            ("resultReference", "resultReference", fhirreference.FHIRReference, False, "result", False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
