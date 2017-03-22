#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Goal) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Goal(domainresource.DomainResource):
    """ Describes the intended objective(s) for a patient, group or organization.
    
    Describes the intended objective(s) for a patient, group or organization
    care, for example, weight loss, restoring an activity of daily living,
    obtaining herd immunity via immunization, meeting a process improvement
    objective, etc.
    """
    
    resource_type = "Goal"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addresses = None
        """ Issues addressed by this goal.
        List of `FHIRReference` items referencing `Condition, Observation, MedicationStatement, NutritionOrder, ProcedureRequest, RiskAssessment` (represented as `dict` in JSON). """
        
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
        
        self.outcomeCode = None
        """ What result was achieved regarding the goal?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.outcomeReference = None
        """ Observation that resulted from goal.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """
        
        self.priority = None
        """ high-priority | medium-priority | low-priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startCodeableConcept = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startDate = None
        """ When goal pursuit begins.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ proposed | accepted | planned | in-progress | on-target | ahead-of-
        target | behind-target | sustaining | achieved | on-hold |
        cancelled | entered-in-error | rejected.
        Type `str`. """
        
        self.statusDate = None
        """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.statusReason = None
        """ Reason for current status.
        Type `str`. """
        
        self.subject = None
        """ Who this goal is intended for.
        Type `FHIRReference` referencing `Patient, Group, Organization` (represented as `dict` in JSON). """
        
        self.target = None
        """ Target outcome for the goal.
        Type `GoalTarget` (represented as `dict` in JSON). """
        
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
            ("outcomeCode", "outcomeCode", codeableconcept.CodeableConcept, True, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, False, "start", False),
            ("startDate", "startDate", fhirdate.FHIRDate, False, "start", False),
            ("status", "status", str, False, None, True),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("statusReason", "statusReason", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("target", "target", GoalTarget, False, None, False),
        ])
        return js


from . import backboneelement

class GoalTarget(backboneelement.BackboneElement):
    """ Target outcome for the goal.
    
    Indicates what should be done by when.
    """
    
    resource_type = "GoalTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.detailCodeableConcept = None
        """ The target value to be achieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailQuantity = None
        """ The target value to be achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.detailRange = None
        """ The target value to be achieved.
        Type `Range` (represented as `dict` in JSON). """
        
        self.dueDate = None
        """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dueDuration = None
        """ Reach goal on or before.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.measure = None
        """ The parameter whose value is being tracked.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(GoalTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False),
            ("detailRange", "detailRange", range.Range, False, "detail", False),
            ("dueDate", "dueDate", fhirdate.FHIRDate, False, "due", False),
            ("dueDuration", "dueDuration", duration.Duration, False, "due", False),
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + '.duration']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
