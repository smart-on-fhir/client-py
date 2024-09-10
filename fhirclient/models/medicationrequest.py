# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationRequest).
# 2024, SMART Health IT.


from . import domainresource

class MedicationRequest(domainresource.DomainResource):
    """ Ordering of medication for patient or group.
    
    An order or request for both supply of the medication and the instructions
    for administration of the medication to a patient. The resource is called
    "MedicationRequest" rather than "MedicationPrescription" or
    "MedicationOrder" to generalize the use across inpatient and outpatient
    settings, including care plans, etc., and to harmonize with workflow
    patterns.
    """
    
    resource_type = "MedicationRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ When request was initially authored.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._authoredOn = None
        """ Primitive extension for authoredOn. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Type of medication usage.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.courseOfTherapyType = None
        """ Overall pattern of medication administration.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._courseOfTherapyType = None
        """ Primitive extension for courseOfTherapyType. Type `FHIRPrimitiveExtension` """
        
        self.detectedIssue = None
        """ Clinical Issue with action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._detectedIssue = None
        """ Primitive extension for detectedIssue. Type `FHIRPrimitiveExtension` """
        
        self.dispenseRequest = None
        """ Medication supply authorization.
        Type `MedicationRequestDispenseRequest` (represented as `dict` in JSON). """
        self._dispenseRequest = None
        """ Primitive extension for dispenseRequest. Type `FHIRPrimitiveExtension` """
        
        self.doNotPerform = None
        """ True if request is prohibiting action.
        Type `bool`. """
        self._doNotPerform = None
        """ Primitive extension for doNotPerform. Type `FHIRPrimitiveExtension` """
        
        self.dosageInstruction = None
        """ How the medication should be taken.
        List of `Dosage` items (represented as `dict` in JSON). """
        self._dosageInstruction = None
        """ Primitive extension for dosageInstruction. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter created as part of encounter/admission/stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._eventHistory = None
        """ Primitive extension for eventHistory. Type `FHIRPrimitiveExtension` """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        self._groupIdentifier = None
        """ Primitive extension for groupIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External ids for this request.
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
        """ proposal | plan | order | original-order | reflex-order | filler-
        order | instance-order | option.
        Type `str`. """
        self._intent = None
        """ Primitive extension for intent. Type `FHIRPrimitiveExtension` """
        
        self.medicationCodeableConcept = None
        """ Medication to be taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._medicationCodeableConcept = None
        """ Primitive extension for medicationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.medicationReference = None
        """ Medication to be taken.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._medicationReference = None
        """ Primitive extension for medicationReference. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Information about the prescription.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Intended performer of administration.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.performerType = None
        """ Desired kind of performer of the medication administration.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._performerType = None
        """ Primitive extension for performerType. Type `FHIRPrimitiveExtension` """
        
        self.priorPrescription = None
        """ An order/prescription that is being replaced.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._priorPrescription = None
        """ Primitive extension for priorPrescription. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Reason or indication for ordering or not ordering the medication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Condition or observation that supports why the prescription is
        being written.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.recorder = None
        """ Person who entered the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recorder = None
        """ Primitive extension for recorder. Type `FHIRPrimitiveExtension` """
        
        self.reportedBoolean = None
        """ Reported rather than primary record.
        Type `bool`. """
        self._reportedBoolean = None
        """ Primitive extension for reportedBoolean. Type `FHIRPrimitiveExtension` """
        
        self.reportedReference = None
        """ Reported rather than primary record.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._reportedReference = None
        """ Primitive extension for reportedReference. Type `FHIRPrimitiveExtension` """
        
        self.requester = None
        """ Who/What requested the Request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requester = None
        """ Primitive extension for requester. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | on-hold | cancelled | completed | entered-in-error |
        stopped | draft | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who or group medication request is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.substitution = None
        """ Any restrictions on medication substitution.
        Type `MedicationRequestSubstitution` (represented as `dict` in JSON). """
        self._substitution = None
        """ Primitive extension for substitution. Type `FHIRPrimitiveExtension` """
        
        self.supportingInformation = None
        """ Information to support ordering of the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInformation = None
        """ Primitive extension for supportingInformation. Type `FHIRPrimitiveExtension` """
        
        super(MedicationRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdatetime.FHIRDateTime, False, None, False),
            ("_authoredOn", "_authoredOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("courseOfTherapyType", "courseOfTherapyType", codeableconcept.CodeableConcept, False, None, False),
            ("_courseOfTherapyType", "_courseOfTherapyType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, True, None, False),
            ("_detectedIssue", "_detectedIssue", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dispenseRequest", "dispenseRequest", MedicationRequestDispenseRequest, False, None, False),
            ("_dispenseRequest", "_dispenseRequest", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("_doNotPerform", "_doNotPerform", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, True, None, False),
            ("_dosageInstruction", "_dosageInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("_eventHistory", "_eventHistory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("_medicationCodeableConcept", "_medicationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("_medicationReference", "_medicationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performerType", "performerType", codeableconcept.CodeableConcept, False, None, False),
            ("_performerType", "_performerType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priorPrescription", "priorPrescription", fhirreference.FHIRReference, False, None, False),
            ("_priorPrescription", "_priorPrescription", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("_recorder", "_recorder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reportedBoolean", "reportedBoolean", bool, False, "reported", False),
            ("_reportedBoolean", "_reportedBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reportedReference", "reportedReference", fhirreference.FHIRReference, False, "reported", False),
            ("_reportedReference", "_reportedReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("_requester", "_requester", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substitution", "substitution", MedicationRequestSubstitution, False, None, False),
            ("_substitution", "_substitution", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("_supportingInformation", "_supportingInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationRequestDispenseRequest(backboneelement.BackboneElement):
    """ Medication supply authorization.
    
    Indicates the specific details for the dispense or medication supply part
    of a medication request (also known as a Medication Prescription or
    Medication Order).  Note that this information is not always sent with the
    order.  There may be in some settings (e.g. hospitals) institutional or
    system support for completing the dispense details in the pharmacy
    department.
    """
    
    resource_type = "MedicationRequestDispenseRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dispenseInterval = None
        """ Minimum period of time between dispenses.
        Type `Duration` (represented as `dict` in JSON). """
        self._dispenseInterval = None
        """ Primitive extension for dispenseInterval. Type `FHIRPrimitiveExtension` """
        
        self.expectedSupplyDuration = None
        """ Number of days supply per dispense.
        Type `Duration` (represented as `dict` in JSON). """
        self._expectedSupplyDuration = None
        """ Primitive extension for expectedSupplyDuration. Type `FHIRPrimitiveExtension` """
        
        self.initialFill = None
        """ First fill details.
        Type `MedicationRequestDispenseRequestInitialFill` (represented as `dict` in JSON). """
        self._initialFill = None
        """ Primitive extension for initialFill. Type `FHIRPrimitiveExtension` """
        
        self.numberOfRepeatsAllowed = None
        """ Number of refills authorized.
        Type `int`. """
        self._numberOfRepeatsAllowed = None
        """ Primitive extension for numberOfRepeatsAllowed. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Intended dispenser.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Amount of medication to supply per dispense.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.validityPeriod = None
        """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """
        self._validityPeriod = None
        """ Primitive extension for validityPeriod. Type `FHIRPrimitiveExtension` """
        
        super(MedicationRequestDispenseRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestDispenseRequest, self).elementProperties()
        js.extend([
            ("dispenseInterval", "dispenseInterval", duration.Duration, False, None, False),
            ("_dispenseInterval", "_dispenseInterval", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expectedSupplyDuration", "expectedSupplyDuration", duration.Duration, False, None, False),
            ("_expectedSupplyDuration", "_expectedSupplyDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("initialFill", "initialFill", MedicationRequestDispenseRequestInitialFill, False, None, False),
            ("_initialFill", "_initialFill", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False, None, False),
            ("_numberOfRepeatsAllowed", "_numberOfRepeatsAllowed", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
            ("_validityPeriod", "_validityPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationRequestDispenseRequestInitialFill(backboneelement.BackboneElement):
    """ First fill details.
    
    Indicates the quantity or duration for the first dispense of the
    medication.
    """
    
    resource_type = "MedicationRequestDispenseRequestInitialFill"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.duration = None
        """ First fill duration.
        Type `Duration` (represented as `dict` in JSON). """
        self._duration = None
        """ Primitive extension for duration. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ First fill quantity.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        super(MedicationRequestDispenseRequestInitialFill, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestDispenseRequestInitialFill, self).elementProperties()
        js.extend([
            ("duration", "duration", duration.Duration, False, None, False),
            ("_duration", "_duration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationRequestSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.
    
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases, substitution must happen, in other cases
    substitution must not happen. This block explains the prescriber's intent.
    If nothing is specified substitution may be done.
    """
    
    resource_type = "MedicationRequestSubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedBoolean = None
        """ Whether substitution is allowed or not.
        Type `bool`. """
        self._allowedBoolean = None
        """ Primitive extension for allowedBoolean. Type `FHIRPrimitiveExtension` """
        
        self.allowedCodeableConcept = None
        """ Whether substitution is allowed or not.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._allowedCodeableConcept = None
        """ Primitive extension for allowedCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        super(MedicationRequestSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationRequestSubstitution, self).elementProperties()
        js.extend([
            ("allowedBoolean", "allowedBoolean", bool, False, "allowed", True),
            ("_allowedBoolean", "_allowedBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("allowedCodeableConcept", "allowedCodeableConcept", codeableconcept.CodeableConcept, False, "allowed", True),
            ("_allowedCodeableConcept", "_allowedCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import dosage
from . import duration
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import quantity