# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ServiceRequest).
# 2024, SMART Health IT.


from . import domainresource

class ServiceRequest(domainresource.DomainResource):
    """ A request for a service to be performed.
    
    A record of a request for service such as diagnostic investigations,
    treatments, or operations to be performed.
    """
    
    resource_type = "ServiceRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.asNeededBoolean = None
        """ Preconditions for service.
        Type `bool`. """
        self._asNeededBoolean = None
        """ Primitive extension for asNeededBoolean. Type `FHIRPrimitiveExtension` """
        
        self.asNeededCodeableConcept = None
        """ Preconditions for service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._asNeededCodeableConcept = None
        """ Primitive extension for asNeededCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.authoredOn = None
        """ Date request signed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._authoredOn = None
        """ Primitive extension for authoredOn. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Location on Body.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Classification of service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ What is being requested/ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.doNotPerform = None
        """ True if service/procedure should not be performed.
        Type `bool`. """
        self._doNotPerform = None
        """ Primitive extension for doNotPerform. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter in which the request was created.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifiers assigned to this order.
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
        
        self.locationCode = None
        """ Requested location.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._locationCode = None
        """ Primitive extension for locationCode. Type `FHIRPrimitiveExtension` """
        
        self.locationReference = None
        """ Requested location.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._locationReference = None
        """ Primitive extension for locationReference. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceDateTime = None
        """ When service should occur.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._occurrenceDateTime = None
        """ Primitive extension for occurrenceDateTime. Type `FHIRPrimitiveExtension` """
        
        self.occurrencePeriod = None
        """ When service should occur.
        Type `Period` (represented as `dict` in JSON). """
        self._occurrencePeriod = None
        """ Primitive extension for occurrencePeriod. Type `FHIRPrimitiveExtension` """
        
        self.occurrenceTiming = None
        """ When service should occur.
        Type `Timing` (represented as `dict` in JSON). """
        self._occurrenceTiming = None
        """ Primitive extension for occurrenceTiming. Type `FHIRPrimitiveExtension` """
        
        self.orderDetail = None
        """ Additional order information.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._orderDetail = None
        """ Primitive extension for orderDetail. Type `FHIRPrimitiveExtension` """
        
        self.patientInstruction = None
        """ Patient or consumer-oriented instructions.
        Type `str`. """
        self._patientInstruction = None
        """ Primitive extension for patientInstruction. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Requested performer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.performerType = None
        """ Performer role.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._performerType = None
        """ Primitive extension for performerType. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.quantityQuantity = None
        """ Service amount.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantityQuantity = None
        """ Primitive extension for quantityQuantity. Type `FHIRPrimitiveExtension` """
        
        self.quantityRange = None
        """ Service amount.
        Type `Range` (represented as `dict` in JSON). """
        self._quantityRange = None
        """ Primitive extension for quantityRange. Type `FHIRPrimitiveExtension` """
        
        self.quantityRatio = None
        """ Service amount.
        Type `Ratio` (represented as `dict` in JSON). """
        self._quantityRatio = None
        """ Primitive extension for quantityRatio. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Explanation/Justification for procedure or service.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Explanation/Justification for service or service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._relevantHistory = None
        """ Primitive extension for relevantHistory. Type `FHIRPrimitiveExtension` """
        
        self.replaces = None
        """ What request replaces.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._replaces = None
        """ Primitive extension for replaces. Type `FHIRPrimitiveExtension` """
        
        self.requester = None
        """ Who/what is requesting service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requester = None
        """ Primitive extension for requester. Type `FHIRPrimitiveExtension` """
        
        self.requisition = None
        """ Composite Request ID.
        Type `Identifier` (represented as `dict` in JSON). """
        self._requisition = None
        """ Primitive extension for requisition. Type `FHIRPrimitiveExtension` """
        
        self.specimen = None
        """ Procedure Samples.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._specimen = None
        """ Primitive extension for specimen. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Individual or Entity the service is ordered for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInfo = None
        """ Primitive extension for supportingInfo. Type `FHIRPrimitiveExtension` """
        
        super(ServiceRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ServiceRequest, self).elementProperties()
        js.extend([
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("_asNeededBoolean", "_asNeededBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("_asNeededCodeableConcept", "_asNeededCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("_authoredOn", "_authoredOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("_doNotPerform", "_doNotPerform", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
            ("locationCode", "locationCode", codeableconcept.CodeableConcept, True, None, False),
            ("_locationCode", "_locationCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("locationReference", "locationReference", fhirreference.FHIRReference, True, None, False),
            ("_locationReference", "_locationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdatetime.FHIRDateTime, False, "occurrence", False),
            ("_occurrenceDateTime", "_occurrenceDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("_occurrencePeriod", "_occurrencePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("_occurrenceTiming", "_occurrenceTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orderDetail", "orderDetail", codeableconcept.CodeableConcept, True, None, False),
            ("_orderDetail", "_orderDetail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("_patientInstruction", "_patientInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("_performerType", "_performerType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantityQuantity", "quantityQuantity", quantity.Quantity, False, "quantity", False),
            ("_quantityQuantity", "_quantityQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantityRange", "quantityRange", range.Range, False, "quantity", False),
            ("_quantityRange", "_quantityRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantityRatio", "quantityRatio", ratio.Ratio, False, "quantity", False),
            ("_quantityRatio", "_quantityRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relevantHistory", "relevantHistory", fhirreference.FHIRReference, True, None, False),
            ("_relevantHistory", "_relevantHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("_replaces", "_replaces", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("_requester", "_requester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("_requisition", "_requisition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("_specimen", "_specimen", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("_supportingInfo", "_supportingInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
from . import ratio
from . import timing