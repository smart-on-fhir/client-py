# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceRequest).
# 2024, SMART Health IT.


from . import domainresource

class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.
    
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    
    resource_type = "DeviceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ When recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._authoredOn = None
        """ Primitive extension for authoredOn. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.codeCodeableConcept = None
        """ Device requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._codeCodeableConcept = None
        """ Primitive extension for codeCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.codeReference = None
        """ Device requested.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._codeReference = None
        """ Primitive extension for codeReference. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter motivating request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.groupIdentifier = None
        """ Identifier of composite request.
        Type `Identifier` (represented as `dict` in JSON). """
        self._groupIdentifier = None
        """ Primitive extension for groupIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._insurance = None
        """ Primitive extension for insurance. Type `FHIRPrimitiveExtension` """
        
        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """
        self._intent = None
        """ Primitive extension for intent. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Notes or comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ Desired time or schedule for use.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurrencePeriod = None
        """ Desired time or schedule for use.
        Type `Period` (represented as `dict` in JSON). """
        self._occurrencePeriod = None
        """ Primitive extension for occurrencePeriod. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceTiming = None
        """ Desired time or schedule for use.
        Type `Timing` (represented as `dict` in JSON). """
        self._occurrenceTiming = None
        """ Primitive extension for occurrenceTiming. Type `FHIRPrimitiveExtension` """
        
        self.parameter = None
        """ Device details.
        List of `DeviceRequestParameter` items (represented as `dict` in JSON). """
        self._parameter = None
        """ Primitive extension for parameter. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Requested Filler.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.performerType = None
        """ Filler role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._performerType = None
        """ Primitive extension for performerType. Type `FHIRPrimitiveExtension` """
        
        self.priorRequest = None
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._priorRequest = None
        """ Primitive extension for priorRequest. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Coded Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Linked Reason for request.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._relevantHistory = None
        """ Primitive extension for relevantHistory. Type `FHIRPrimitiveExtension` """
        
        self.requester = None
        """ Who/what is requesting diagnostics.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requester = None
        """ Primitive extension for requester. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Focus of request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInfo = None
        """ Primitive extension for supportingInfo. Type `FHIRPrimitiveExtension` """
        
        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("_authoredOn", "_authoredOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("codeCodeableConcept", "codeCodeableConcept", codeableconcept.CodeableConcept, False, "code", True),
            ("_codeCodeableConcept", "_codeCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("codeReference", "codeReference", fhirreference.FHIRReference, False, "code", True),
            ("_codeReference", "_codeReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("_groupIdentifier", "_groupIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurance", "insurance", fhirreference.FHIRReference, True, None, False),
            ("_insurance", "_insurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("_occurrencePeriod", "_occurrencePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("_occurrenceTiming", "_occurrenceTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parameter", "parameter", DeviceRequestParameter, True, None, False),
            ("_parameter", "_parameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("_performerType", "_performerType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priorRequest", "priorRequest", fhirreference.FHIRReference, True, None, False),
            ("_priorRequest", "_priorRequest", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("_relevantHistory", "_relevantHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("_requester", "_requester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("_supportingInfo", "_supportingInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceRequestParameter(backboneelement.BackboneElement):
    """ Device details.
    
    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """
    
    resource_type = "DeviceRequestParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Device detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Value of detail.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Value of detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Value of detail.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Value of detail.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        super(DeviceRequestParameter, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", False),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import timing