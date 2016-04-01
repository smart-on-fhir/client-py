#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/Protocol) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class Protocol(domainresource.DomainResource):
    """ Contextual set of behaviors.
    
    A definition of behaviors to be taken in particular circumstances, often
    including conditions, options and other decision points.
    """
    
    resource_name = "Protocol"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ Who wrote protocol?.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.group = None
        """ To whom does Protocol apply?.
        Type `FHIRReference` referencing `Group` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique Id for this particular protocol.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.purpose = None
        """ When is protocol to be used?.
        Type `str`. """
        
        self.status = None
        """ draft | testing | review | active | withdrawn | superseded.
        Type `str`. """
        
        self.step = None
        """ What's done as part of protocol.
        List of `ProtocolStep` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ What does protocol deal with?.
        Type `FHIRReference` referencing `Condition, Device, Medication` (represented as `dict` in JSON). """
        
        self.title = None
        """ Name of protocol.
        Type `str`. """
        
        self.type = None
        """ condition | device | drug | study.
        Type `str`. """
        
        super(Protocol, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Protocol, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("group", "group", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("purpose", "purpose", str, False, None, True),
            ("status", "status", str, False, None, True),
            ("step", "step", ProtocolStep, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import backboneelement

class ProtocolStep(backboneelement.BackboneElement):
    """ What's done as part of protocol.
    """
    
    resource_name = "ProtocolStep"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activity = None
        """ Activities that occur within timepoint.
        List of `ProtocolStepActivity` items (represented as `dict` in JSON). """
        
        self.description = None
        """ Human description of activity.
        Type `str`. """
        
        self.duration = None
        """ How long does step last?.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
        
        self.exit = None
        """ Rules prior to completion.
        Type `ProtocolStepPrecondition` (represented as `dict` in JSON). """
        
        self.firstActivity = None
        """ First activity within timepoint.
        Type `str`. """
        
        self.name = None
        """ Label for step.
        Type `str`. """
        
        self.next = None
        """ What happens next?.
        List of `ProtocolStepNext` items (represented as `dict` in JSON). """
        
        self.precondition = None
        """ Rules prior to execution.
        Type `ProtocolStepPrecondition` (represented as `dict` in JSON). """
        
        super(ProtocolStep, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProtocolStep, self).elementProperties()
        js.extend([
            ("activity", "activity", ProtocolStepActivity, True, None, False),
            ("description", "description", str, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("exit", "exit", ProtocolStepPrecondition, False, None, False),
            ("firstActivity", "firstActivity", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("next", "next", ProtocolStepNext, True, None, False),
            ("precondition", "precondition", ProtocolStepPrecondition, False, None, False),
        ])
        return js


class ProtocolStepActivity(backboneelement.BackboneElement):
    """ Activities that occur within timepoint.
    """
    
    resource_name = "ProtocolStepActivity"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alternative = None
        """ What can be done instead?.
        List of `str` items. """
        
        self.component = None
        """ Activities that are part of this activity.
        List of `ProtocolStepActivityComponent` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Details of activity.
        Type `ProtocolStepActivityDetail` (represented as `dict` in JSON). """
        
        self.following = None
        """ What happens next.
        List of `str` items. """
        
        self.wait = None
        """ Pause before start.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
        
        super(ProtocolStepActivity, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProtocolStepActivity, self).elementProperties()
        js.extend([
            ("alternative", "alternative", str, True, None, False),
            ("component", "component", ProtocolStepActivityComponent, True, None, False),
            ("detail", "detail", ProtocolStepActivityDetail, False, None, True),
            ("following", "following", str, True, None, False),
            ("wait", "wait", quantity.Quantity, False, None, False),
        ])
        return js


class ProtocolStepActivityComponent(backboneelement.BackboneElement):
    """ Activities that are part of this activity.
    """
    
    resource_name = "ProtocolStepActivityComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.activity = None
        """ Component activity.
        Type `str`. """
        
        self.sequence = None
        """ Order of occurrence.
        Type `int`. """
        
        super(ProtocolStepActivityComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProtocolStepActivityComponent, self).elementProperties()
        js.extend([
            ("activity", "activity", str, False, None, True),
            ("sequence", "sequence", int, False, None, False),
        ])
        return js


class ProtocolStepActivityDetail(backboneelement.BackboneElement):
    """ Details of activity.
    
    Information about the nature of the activity, including type, timing and
    other qualifiers.
    """
    
    resource_name = "ProtocolStepActivityDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ diet | drug | encounter | observation +.
        Type `str`. """
        
        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Extra info on activity occurrence.
        Type `str`. """
        
        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who's responsible?.
        List of `FHIRReference` items referencing `Practitioner, Organization, RelatedPerson, Patient` (represented as `dict` in JSON). """
        
        self.product = None
        """ What's administered/supplied.
        Type `FHIRReference` referencing `Medication, Substance` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ How much is administered/consumed/supplied.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.timingCodeableConcept = None
        """ When activity is to occur.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(ProtocolStepActivityDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProtocolStepActivityDetail, self).elementProperties()
        js.extend([
            ("category", "category", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("description", "description", str, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("product", "product", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("timingCodeableConcept", "timingCodeableConcept", codeableconcept.CodeableConcept, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
        ])
        return js


class ProtocolStepNext(backboneelement.BackboneElement):
    """ What happens next?.
    
    What happens next?
    """
    
    resource_name = "ProtocolStepNext"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ Condition in which next step is executed.
        Type `ProtocolStepPrecondition` (represented as `dict` in JSON). """
        
        self.description = None
        """ Description of what happens next.
        Type `str`. """
        
        self.reference = None
        """ Id of following step.
        Type `str`. """
        
        super(ProtocolStepNext, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProtocolStepNext, self).elementProperties()
        js.extend([
            ("condition", "condition", ProtocolStepPrecondition, False, None, False),
            ("description", "description", str, False, None, False),
            ("reference", "reference", str, False, None, False),
        ])
        return js


class ProtocolStepPrecondition(backboneelement.BackboneElement):
    """ Rules prior to execution.
    """
    
    resource_name = "ProtocolStepPrecondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ Condition evaluated.
        Type `ProtocolStepPreconditionCondition` (represented as `dict` in JSON). """
        
        self.description = None
        """ Description of condition.
        Type `str`. """
        
        self.exclude = None
        """ Not conditions.
        List of `ProtocolStepPrecondition` items (represented as `dict` in JSON). """
        
        self.intersection = None
        """ And conditions.
        List of `ProtocolStepPrecondition` items (represented as `dict` in JSON). """
        
        self.union = None
        """ Or conditions.
        List of `ProtocolStepPrecondition` items (represented as `dict` in JSON). """
        
        super(ProtocolStepPrecondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProtocolStepPrecondition, self).elementProperties()
        js.extend([
            ("condition", "condition", ProtocolStepPreconditionCondition, False, None, False),
            ("description", "description", str, False, None, False),
            ("exclude", "exclude", ProtocolStepPrecondition, True, None, False),
            ("intersection", "intersection", ProtocolStepPrecondition, True, None, False),
            ("union", "union", ProtocolStepPrecondition, True, None, False),
        ])
        return js


class ProtocolStepPreconditionCondition(backboneelement.BackboneElement):
    """ Condition evaluated.
    
    Defines the name/value pair that must hold for the condition to be met.
    """
    
    resource_name = "ProtocolStepPreconditionCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Observation / test / assertion.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueBoolean = None
        """ Value needed to satisfy condition.
        Type `bool`. """
        
        self.valueCodeableConcept = None
        """ Value needed to satisfy condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value needed to satisfy condition.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value needed to satisfy condition.
        Type `Range` (represented as `dict` in JSON). """
        
        super(ProtocolStepPreconditionCondition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProtocolStepPreconditionCondition, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("valueRange", "valueRange", range.Range, False, "value", True),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import timing
