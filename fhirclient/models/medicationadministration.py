# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration).
# 2024, SMART Health IT.


from . import domainresource

class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.
    
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    
    resource_type = "MedicationAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Type of medication usage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Encounter or Episode of Care administered as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._device = None
        """ Primitive extension for device. Type `FHIRPrimitiveExtension` """
        
        self.dosage = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        self._dosage = None
        """ Primitive extension for dosage. Type `FHIRPrimitiveExtension` """
        
        self.effectiveDateTime = None
        """ Start and end time of administration.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._effectiveDateTime = None
        """ Primitive extension for effectiveDateTime. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._eventHistory = None
        """ Primitive extension for eventHistory. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instantiates = None
        """ Instantiates protocol or definition.
        List of `str` items. """
        self._instantiates = None
        """ Primitive extension for instantiates. Type `FHIRPrimitiveExtension` """
        
        self.medicationCodeableConcept = None
        """ What was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._medicationCodeableConcept = None
        """ Primitive extension for medicationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.medicationReference = None
        """ What was administered.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._medicationReference = None
        """ Primitive extension for medicationReference. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Information about the administration.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who performed the medication administration and what they did.
        List of `MedicationAdministrationPerformer` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Condition or observation that supports why the medication was
        administered.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Request administration performed against.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ in-progress | not-done | on-hold | completed | entered-in-error |
        stopped | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who received medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.supportingInformation = None
        """ Additional information to support administration.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInformation = None
        """ Primitive extension for supportingInformation. Type `FHIRPrimitiveExtension` """
        
        super(MedicationAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("_device", "_device", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dosage", "dosage", MedicationAdministrationDosage, False, None, False),
            ("_dosage", "_dosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdatetime.FHIRDateTime, False, "effective", True),
            ("_effectiveDateTime", "_effectiveDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", True),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("_eventHistory", "_eventHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("_instantiates", "_instantiates", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("_medicationCodeableConcept", "_medicationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("_medicationReference", "_medicationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", MedicationAdministrationPerformer, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("_supportingInformation", "_supportingInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationAdministrationDosage(backboneelement.BackboneElement):
    """ Details of how medication was taken.
    
    Describes the medication dosage information details e.g. dose, rate, site,
    route, etc.
    """
    
    resource_type = "MedicationAdministrationDosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dose = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        self._dose = None
        """ Primitive extension for dose. Type `FHIRPrimitiveExtension` """
        
        self.method = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._method = None
        """ Primitive extension for method. Type `FHIRPrimitiveExtension` """
        
        self.rateQuantity = None
        """ Dose quantity per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        self._rateQuantity = None
        """ Primitive extension for rateQuantity. Type `FHIRPrimitiveExtension` """
        
        self.rateRatio = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        self._rateRatio = None
        """ Primitive extension for rateRatio. Type `FHIRPrimitiveExtension` """
        
        self.route = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._route = None
        """ Primitive extension for route. Type `FHIRPrimitiveExtension` """
        
        self.site = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._site = None
        """ Primitive extension for site. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Free text dosage instructions e.g. SIG.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("dose", "dose", quantity.Quantity, False, None, False),
            ("_dose", "_dose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("_method", "_method", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("_rateQuantity", "_rateQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("_rateRatio", "_rateRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("_route", "_route", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("site", "site", codeableconcept.CodeableConcept, False, None, False),
            ("_site", "_site", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationAdministrationPerformer(backboneelement.BackboneElement):
    """ Who performed the medication administration and what they did.
    
    Indicates who or what performed the medication administration and how they
    were involved.
    """
    
    resource_type = "MedicationAdministrationPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Who performed the medication administration.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._function = None
        """ Primitive extension for function. Type `FHIRPrimitiveExtension` """
        
        super(MedicationAdministrationPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("_function", "_function", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
from . import ratio