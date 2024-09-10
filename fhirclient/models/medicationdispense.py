# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationDispense).
# 2024, SMART Health IT.


from . import domainresource

class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.
    
    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """
    
    resource_type = "MedicationDispense"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorizingPrescription = None
        """ Medication order that authorizes the dispense.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._authorizingPrescription = None
        """ Primitive extension for authorizingPrescription. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Type of medication dispense.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.context = None
        """ Encounter / Episode associated with event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._context = None
        """ Primitive extension for context. Type `FHIRPrimitiveExtension` """
        
        self.daysSupply = None
        """ Amount of medication expressed as a timing amount.
        Type `Quantity` (represented as `dict` in JSON). """
        self._daysSupply = None
        """ Primitive extension for daysSupply. Type `FHIRPrimitiveExtension` """
        
        self.destination = None
        """ Where the medication was sent.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._destination = None
        """ Primitive extension for destination. Type `FHIRPrimitiveExtension` """
        
        self.detectedIssue = None
        """ Clinical issue with action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._detectedIssue = None
        """ Primitive extension for detectedIssue. Type `FHIRPrimitiveExtension` """
        
        self.dosageInstruction = None
        """ How the medication is to be used by the patient or administered by
        the caregiver.
        List of `Dosage` items (represented as `dict` in JSON). """
        self._dosageInstruction = None
        """ Primitive extension for dosageInstruction. Type `FHIRPrimitiveExtension` """
        
        self.eventHistory = None
        """ A list of relevant lifecycle events.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._eventHistory = None
        """ Primitive extension for eventHistory. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where the dispense occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.medicationCodeableConcept = None
        """ What medication was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._medicationCodeableConcept = None
        """ Primitive extension for medicationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.medicationReference = None
        """ What medication was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._medicationReference = None
        """ Primitive extension for medicationReference. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Information about the dispense.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Event that dispense is part of.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who performed event.
        List of `MedicationDispensePerformer` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.receiver = None
        """ Who collected the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._receiver = None
        """ Primitive extension for receiver. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ preparation | in-progress | cancelled | on-hold | completed |
        entered-in-error | stopped | declined | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReasonCodeableConcept = None
        """ Why a dispense was not performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._statusReasonCodeableConcept = None
        """ Primitive extension for statusReasonCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.statusReasonReference = None
        """ Why a dispense was not performed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._statusReasonReference = None
        """ Primitive extension for statusReasonReference. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who the dispense is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.substitution = None
        """ Whether a substitution was performed on the dispense.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """
        self._substitution = None
        """ Primitive extension for substitution. Type `FHIRPrimitiveExtension` """
        
        self.supportingInformation = None
        """ Information that supports the dispensing of the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInformation = None
        """ Primitive extension for supportingInformation. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.whenHandedOver = None
        """ When product was given out.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._whenHandedOver = None
        """ Primitive extension for whenHandedOver. Type `FHIRPrimitiveExtension` """
        
        self.whenPrepared = None
        """ When product was packaged and reviewed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._whenPrepared = None
        """ Primitive extension for whenPrepared. Type `FHIRPrimitiveExtension` """
        
        super(MedicationDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, True, None, False),
            ("_authorizingPrescription", "_authorizingPrescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("_context", "_context", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("daysSupply", "daysSupply", quantity.Quantity, False, None, False),
            ("_daysSupply", "_daysSupply", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("_destination", "_destination", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("_detectedIssue", "_detectedIssue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("_dosageInstruction", "_dosageInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("_eventHistory", "_eventHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("_medicationCodeableConcept", "_medicationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("_medicationReference", "_medicationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", MedicationDispensePerformer, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("_receiver", "_receiver", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReasonCodeableConcept", "statusReasonCodeableConcept", codeableconcept.CodeableConcept, False, "statusReason", False),
            ("_statusReasonCodeableConcept", "_statusReasonCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReasonReference", "statusReasonReference", fhirreference.FHIRReference, False, "statusReason", False),
            ("_statusReasonReference", "_statusReasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, False, None, False),
            ("_substitution", "_substitution", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("_supportingInformation", "_supportingInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("whenHandedOver", "whenHandedOver", fhirdatetime.FHIRDateTime, False, None, False),
            ("_whenHandedOver", "_whenHandedOver", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("whenPrepared", "whenPrepared", fhirdatetime.FHIRDateTime, False, None, False),
            ("_whenPrepared", "_whenPrepared", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationDispensePerformer(backboneelement.BackboneElement):
    """ Who performed event.
    
    Indicates who or what performed the event.
    """
    
    resource_type = "MedicationDispensePerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.function = None
        """ Who performed the dispense and what they did.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._function = None
        """ Primitive extension for function. Type `FHIRPrimitiveExtension` """
        
        super(MedicationDispensePerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispensePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("_function", "_function", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Whether a substitution was performed on the dispense.
    
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """
    
    resource_type = "MedicationDispenseSubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reason = None
        """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.responsibleParty = None
        """ Who is responsible for the substitution.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._responsibleParty = None
        """ Primitive extension for responsibleParty. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Code signifying whether a different drug was dispensed from what
        was prescribed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.wasSubstituted = None
        """ Whether a substitution was or was not performed on the dispense.
        Type `bool`. """
        self._wasSubstituted = None
        """ Primitive extension for wasSubstituted. Type `FHIRPrimitiveExtension` """
        
        super(MedicationDispenseSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, True, None, False),
            ("_responsibleParty", "_responsibleParty", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("wasSubstituted", "wasSubstituted", bool, False, None, True),
            ("_wasSubstituted", "_wasSubstituted", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import dosage
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity