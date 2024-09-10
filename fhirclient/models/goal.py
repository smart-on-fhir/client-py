# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Goal).
# 2024, SMART Health IT.


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
        
        self.achievementStatus = None
        """ in-progress | improving | worsening | no-change | achieved |
        sustaining | not-achieved | no-progress | not-attainable.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._achievementStatus = None
        """ Primitive extension for achievementStatus. Type `FHIRPrimitiveExtension` """
        
        self.addresses = None
        """ Issues addressed by this goal.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._addresses = None
        """ Primitive extension for addresses. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ E.g. Treatment, dietary, behavioral, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Code or text describing goal.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.expressedBy = None
        """ Who's responsible for creating Goal?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._expressedBy = None
        """ Primitive extension for expressedBy. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Ids for this goal.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.lifecycleStatus = None
        """ proposed | planned | accepted | active | on-hold | completed |
        cancelled | entered-in-error | rejected.
        Type `str`. """
        self._lifecycleStatus = None
        """ Primitive extension for lifecycleStatus. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments about the goal.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.outcomeCode = None
        """ What result was achieved regarding the goal?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._outcomeCode = None
        """ Primitive extension for outcomeCode. Type `FHIRPrimitiveExtension` """
        
        self.outcomeReference = None
        """ Observation that resulted from goal.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._outcomeReference = None
        """ Primitive extension for outcomeReference. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ high-priority | medium-priority | low-priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.startCodeableConcept = None
        """ When goal pursuit begins.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._startCodeableConcept = None
        """ Primitive extension for startCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.startDate = None
        """ When goal pursuit begins.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._startDate = None
        """ Primitive extension for startDate. Type `FHIRPrimitiveExtension` """
        
        self.statusDate = None
        """ When goal status took effect.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._statusDate = None
        """ Primitive extension for statusDate. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason for current status.
        Type `str`. """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who this goal is intended for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Target outcome for the goal.
        List of `GoalTarget` items (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(Goal, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Goal, self).elementProperties()
        js.extend([
            ("achievementStatus", "achievementStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_achievementStatus", "_achievementStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("addresses", "addresses", fhirreference.FHIRReference, True, None, False),
            ("_addresses", "_addresses", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", codeableconcept.CodeableConcept, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expressedBy", "expressedBy", fhirreference.FHIRReference, False, None, False),
            ("_expressedBy", "_expressedBy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lifecycleStatus", "lifecycleStatus", str, False, None, True),
            ("_lifecycleStatus", "_lifecycleStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcomeCode", "outcomeCode", codeableconcept.CodeableConcept, True, None, False),
            ("_outcomeCode", "_outcomeCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcomeReference", "outcomeReference", fhirreference.FHIRReference, True, None, False),
            ("_outcomeReference", "_outcomeReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("startCodeableConcept", "startCodeableConcept", codeableconcept.CodeableConcept, False, "start", False),
            ("_startCodeableConcept", "_startCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("startDate", "startDate", fhirdate.FHIRDate, False, "start", False),
            ("_startDate", "_startDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusDate", "statusDate", fhirdate.FHIRDate, False, None, False),
            ("_statusDate", "_statusDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", str, False, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", GoalTarget, True, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.detailBoolean = None
        """ The target value to be achieved.
        Type `bool`. """
        self._detailBoolean = None
        """ Primitive extension for detailBoolean. Type `FHIRPrimitiveExtension` """
        
        self.detailCodeableConcept = None
        """ The target value to be achieved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._detailCodeableConcept = None
        """ Primitive extension for detailCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.detailInteger = None
        """ The target value to be achieved.
        Type `int`. """
        self._detailInteger = None
        """ Primitive extension for detailInteger. Type `FHIRPrimitiveExtension` """
        
        self.detailQuantity = None
        """ The target value to be achieved.
        Type `Quantity` (represented as `dict` in JSON). """
        self._detailQuantity = None
        """ Primitive extension for detailQuantity. Type `FHIRPrimitiveExtension` """
        
        self.detailRange = None
        """ The target value to be achieved.
        Type `Range` (represented as `dict` in JSON). """
        self._detailRange = None
        """ Primitive extension for detailRange. Type `FHIRPrimitiveExtension` """
        
        self.detailRatio = None
        """ The target value to be achieved.
        Type `Ratio` (represented as `dict` in JSON). """
        self._detailRatio = None
        """ Primitive extension for detailRatio. Type `FHIRPrimitiveExtension` """
        
        self.detailString = None
        """ The target value to be achieved.
        Type `str`. """
        self._detailString = None
        """ Primitive extension for detailString. Type `FHIRPrimitiveExtension` """
        
        self.dueDate = None
        """ Reach goal on or before.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._dueDate = None
        """ Primitive extension for dueDate. Type `FHIRPrimitiveExtension` """
        
        self.dueDuration = None
        """ Reach goal on or before.
        Type `Duration` (represented as `dict` in JSON). """
        self._dueDuration = None
        """ Primitive extension for dueDuration. Type `FHIRPrimitiveExtension` """
        
        self.measure = None
        """ The parameter whose value is being tracked.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._measure = None
        """ Primitive extension for measure. Type `FHIRPrimitiveExtension` """
        
        super(GoalTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GoalTarget, self).elementProperties()
        js.extend([
            ("detailBoolean", "detailBoolean", bool, False, "detail", False),
            ("_detailBoolean", "_detailBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailCodeableConcept", "detailCodeableConcept", codeableconcept.CodeableConcept, False, "detail", False),
            ("_detailCodeableConcept", "_detailCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailInteger", "detailInteger", int, False, "detail", False),
            ("_detailInteger", "_detailInteger", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailQuantity", "detailQuantity", quantity.Quantity, False, "detail", False),
            ("_detailQuantity", "_detailQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailRange", "detailRange", range.Range, False, "detail", False),
            ("_detailRange", "_detailRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailRatio", "detailRatio", ratio.Ratio, False, "detail", False),
            ("_detailRatio", "_detailRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detailString", "detailString", str, False, "detail", False),
            ("_detailString", "_detailString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dueDate", "dueDate", fhirdate.FHIRDate, False, "due", False),
            ("_dueDate", "_dueDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dueDuration", "dueDuration", duration.Duration, False, "due", False),
            ("_dueDuration", "_dueDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measure", "measure", codeableconcept.CodeableConcept, False, None, False),
            ("_measure", "_measure", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio