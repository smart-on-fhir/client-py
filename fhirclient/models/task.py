#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/Task) on 2016-04-01.
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
        
        self.created = None
        """ Task Creation Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.creator = None
        """ Task Creator.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Task Definition.
        Type `str`. """
        
        self.description = None
        """ Task Description.
        Type `str`. """
        
        self.failureReason = None
        """ Task Failure Reason.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.for_fhir = None
        """ Beneficiary of the Task.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Task Instance Identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.input = None
        """ Task Input.
        List of `TaskInput` items (represented as `dict` in JSON). """
        
        self.lastModified = None
        """ Task Last Modified Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.output = None
        """ Task Output.
        List of `TaskOutput` items (represented as `dict` in JSON). """
        
        self.owner = None
        """ Task Owner.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.parent = None
        """ Composite task.
        Type `FHIRReference` referencing `Task` (represented as `dict` in JSON). """
        
        self.performerType = None
        """ requester | dispatcher | scheduler | performer | monitor | manager
        | acquirer | reviewer.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ low | normal | high.
        Type `str`. """
        
        self.status = None
        """ draft | requested | received | accepted | +.
        Type `str`. """
        
        self.subject = None
        """ Task Subject.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ Task Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Task, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Task, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("creator", "creator", fhirreference.FHIRReference, False, None, True),
            ("definition", "definition", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("failureReason", "failureReason", codeableconcept.CodeableConcept, False, None, False),
            ("for_fhir", "for", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("input", "input", TaskInput, True, None, False),
            ("lastModified", "lastModified", fhirdate.FHIRDate, False, None, True),
            ("output", "output", TaskOutput, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("performerType", "performerType", coding.Coding, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class TaskInput(backboneelement.BackboneElement):
    """ Task Input.
    
    Inputs to the task.
    """
    
    resource_name = "TaskInput"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Input Name.
        Type `str`. """
        
        self.valueAddress = None
        """ Input Value.
        Type `Address` (represented as `dict` in JSON). """
        
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
        
        self.valueDate = None
        """ Input Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Input Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Input Value.
        Type `float`. """
        
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
            ("name", "name", str, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
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
        
        self.name = None
        """ Output Name.
        Type `str`. """
        
        self.valueAddress = None
        """ Output Value.
        Type `Address` (represented as `dict` in JSON). """
        
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
        
        self.valueDate = None
        """ Output Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDateTime = None
        """ Output Value.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.valueDecimal = None
        """ Output Value.
        Type `float`. """
        
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
            ("name", "name", str, False, None, True),
            ("valueAddress", "valueAddress", address.Address, False, "value", True),
            ("valueAnnotation", "valueAnnotation", annotation.Annotation, False, "value", True),
            ("valueAttachment", "valueAttachment", attachment.Attachment, False, "value", True),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCode", "valueCode", str, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueCoding", "valueCoding", coding.Coding, False, "value", True),
            ("valueContactPoint", "valueContactPoint", contactpoint.ContactPoint, False, "value", True),
            ("valueDate", "valueDate", fhirdate.FHIRDate, False, "value", True),
            ("valueDateTime", "valueDateTime", fhirdate.FHIRDate, False, "value", True),
            ("valueDecimal", "valueDecimal", float, False, "value", True),
            ("valueHumanName", "valueHumanName", humanname.HumanName, False, "value", True),
            ("valueId", "valueId", str, False, "value", True),
            ("valueIdentifier", "valueIdentifier", identifier.Identifier, False, "value", True),
            ("valueInstant", "valueInstant", fhirdate.FHIRDate, False, "value", True),
            ("valueInteger", "valueInteger", int, False, "value", True),
            ("valueMarkdown", "valueMarkdown", str, False, "value", True),
            ("valueMeta", "valueMeta", meta.Meta, False, "value", True),
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
from . import annotation
from . import attachment
from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import meta
from . import period
from . import quantity
from . import range
from . import ratio
from . import sampleddata
from . import signature
from . import timing
