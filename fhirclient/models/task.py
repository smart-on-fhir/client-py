#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10210 (http://hl7.org/fhir/StructureDefinition/Task) on 2016-11-17.
#  2016, SMART Health IT.


from . import domainresource

class Task(domainresource.DomainResource):
    """ A task to be performed.
    """
    
    resource_name = "Task"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ Request fulfilled by this task.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.businessStatus = None
        """ E.g. "Specimen collected", "IV prepped".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Task Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
        """ Healthcare event during which this task originated.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.created = None
        """ Task Creation Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.definition = None
        """ Task Definition.
        Type `str`. """
        
        self.description = None
        """ Human-readable explanation of task.
        Type `str`. """
        
        self.focus = None
        """ What task is acting on.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.for_fhir = None
        """ Beneficiary of the Task.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.fulfillment = None
        """ Constraints on fulfillment tasks.
        Type `TaskFulfillment` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Task Instance Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.input = None
        """ Supporting information.
        List of `TaskInput` items (represented as `dict` in JSON). """
        
        self.lastModified = None
        """ Task Last Modified Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.note = None
        """ Comments made about the task.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.output = None
        """ Task Output.
        List of `TaskOutput` items (represented as `dict` in JSON). """
        
        self.owner = None
        """ Task Owner.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.parent = None
        """ Composite task.
        List of `FHIRReference` items referencing `Task` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ requester | dispatcher | scheduler | performer | monitor | manager
        | acquirer | reviewer.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ low | normal | high.
        Type `str`. """
        
        self.reason = None
        """ Why task is needed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Task Creator.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.requisition = None
        """ Requisition or grouper id.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.stage = None
        """ proposed | planned | actionable +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | requested | received | accepted | +.
        Type `str`. """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Task, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("businessStatus", "businessStatus", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("definition", "definition", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("fulfillment", "fulfillment", TaskFulfillment, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("output", "output", TaskOutput, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, True, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, True),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("stage", "stage", codeableconcept.CodeableConcept, False, None, True),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class TaskFulfillment(backboneelement.BackboneElement):
    """ Constraints on fulfillment tasks.
    
    Identifies any limitations on what part of a referenced task subject
    request should be actioned.
    """
    
    resource_name = "TaskFulfillment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ Over what time-period is fulfillment sought.
        Type `Period` (represented as `dict` in JSON). """
        
        self.recipients = None
        """ For whom is fulfillment sought?.
        List of `FHIRReference` items referencing `Patient, Practitioner, RelatedPerson, Group, Organization` (represented as `dict` in JSON). """
        
        self.repetitions = None
        """ How many times to repeat.
        Type `int`. """
        
        super(TaskFulfillment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskFulfillment, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("recipients", "recipients", fhirreference.FHIRReference, True, None, False),
            ("repetitions", "repetitions", int, False, None, False),
        ])
        return js


class TaskInput(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information that may be needed in the execution of the task.
    """
    
    resource_name = "TaskInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Label for the input.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ Input Value.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ Input Value.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ Input Value.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Input Value.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ Input Value.
        Type `str`. """
        
        self.valueBoolean = None
        """ Input Value.
        Type `bool`. """
        
        self.valueCode = None
        """ Input Value.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Input Value.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Input Value.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Input Value.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ Input Value.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ Input Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Input Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Input Value.
        Type `float`. """
        
        self.valueDistance = None
        """ Input Value.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ Input Value.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ Input Value.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        """ Input Value.
        Type `str`. """
        
        self.valueIdentifier = None
        """ Input Value.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ Input Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Input Value.
        Type `int`. """
        
        self.valueMarkdown = None
        """ Input Value.
        Type `str`. """
        
        self.valueMeta = None
        """ Input Value.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ Input Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        """ Input Value.
        Type `str`. """
        
        self.valuePeriod = None
        """ Input Value.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        """ Input Value.
        Type `int`. """
        
        self.valueQuantity = None
        """ Input Value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Input Value.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Input Value.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Input Value.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Input Value.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Input Value.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Input Value.
        Type `str`. """
        
        self.valueTime = None
        """ Input Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ Input Value.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        """ Input Value.
        Type `int`. """
        
        self.valueUri = None
        """ Input Value.
        Type `str`. """
        
        super(TaskInput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskInput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
        ])
        return js


class TaskOutput(backboneelement.BackboneElement):
    """ Task Output.
    
    Outputs produced by the Task.
    """
    
    resource_name = "TaskOutput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Output Name.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueAddress = None
        """ Output Value.
        Type `Address` (represented as `dict` in JSON). """
        
        self.valueAge = None
        """ Output Value.
        Type `Age` (represented as `dict` in JSON). """
        
        self.valueAnnotation = None
        """ Output Value.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.valueAttachment = None
        """ Output Value.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.valueBase64Binary = None
        """ Output Value.
        Type `str`. """
        
        self.valueBoolean = None
        """ Output Value.
        Type `bool`. """
        
        self.valueCode = None
        """ Output Value.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Output Value.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueCoding = None
        """ Output Value.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.valueContactPoint = None
        """ Output Value.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.valueCount = None
        """ Output Value.
        Type `Count` (represented as `dict` in JSON). """
        
        self.valueDate = None
        """ Output Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Output Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Output Value.
        Type `float`. """
        
        self.valueDistance = None
        """ Output Value.
        Type `Distance` (represented as `dict` in JSON). """
        
        self.valueDuration = None
        """ Output Value.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.valueHumanName = None
        """ Output Value.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.valueId = None
        """ Output Value.
        Type `str`. """
        
        self.valueIdentifier = None
        """ Output Value.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.valueInstant = None
        """ Output Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueInteger = None
        """ Output Value.
        Type `int`. """
        
        self.valueMarkdown = None
        """ Output Value.
        Type `str`. """
        
        self.valueMeta = None
        """ Output Value.
        Type `Meta` (represented as `dict` in JSON). """
        
        self.valueMoney = None
        """ Output Value.
        Type `Money` (represented as `dict` in JSON). """
        
        self.valueOid = None
        """ Output Value.
        Type `str`. """
        
        self.valuePeriod = None
        """ Output Value.
        Type `Period` (represented as `dict` in JSON). """
        
        self.valuePositiveInt = None
        """ Output Value.
        Type `int`. """
        
        self.valueQuantity = None
        """ Output Value.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Output Value.
        Type `Range` (represented as `dict` in JSON). """
        
        self.valueRatio = None
        """ Output Value.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.valueReference = None
        """ Output Value.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.valueSampledData = None
        """ Output Value.
        Type `SampledData` (represented as `dict` in JSON). """
        
        self.valueSignature = None
        """ Output Value.
        Type `Signature` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Output Value.
        Type `str`. """
        
        self.valueTime = None
        """ Output Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueTiming = None
        """ Output Value.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.valueUnsignedInt = None
        """ Output Value.
        Type `int`. """
        
        self.valueUri = None
        """ Output Value.
        Type `str`. """
        
        super(TaskOutput, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TaskOutput, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAge", "valueAge", age.Age, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueCount", "valueCount", count.Count, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueDistance", "valueDistance", distance.Distance, False, "value", True),
            ("valueDuration", "valueDuration", duration.Duration, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("valueOid", "valueOid", str, False, "value", True),
            ("valuePeriod", "valuePeriod", period.Period, False, "value", True),
            ("valuePositiveInt", "valuePositiveInt", int, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("valueRatio", "valueRatio", ratio.Ratio, False, "value", True),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("valueSampledData", "valueSampledData", sampleddata.SampledData, False, "value", True),
            ("valueSignature", "valueSignature", signature.Signature, False, "value", True),
            ("valueString", "valueString", str, False, "value", True),
            ("valueTime", "valueTime", fhirdate.FHIRDate, False, "value", True),
            ("valueTiming", "valueTiming", timing.Timing, False, "value", True),
            ("valueUnsignedInt", "valueUnsignedInt", int, False, "value", True),
            ("valueUri", "valueUri", str, False, "value", True),
        ])
        return js


from . import address
from . import age
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import count
from . import distance
from . import duration
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import meta
from . import money
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import signature
from . import timing
