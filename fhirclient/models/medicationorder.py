#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.7.0.10061 (http://hl7.org/fhir/StructureDefinition/MedicationOrder) on 2016-10-24.
#  2016, SMART Health IT.


from . import domainresource

class MedicationOrder(domainresource.DomainResource):
    """ Prescription of medication to for patient.
    
    An order for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationOrder" rather than "MedicationPrescription" to generalize the
    use across inpatient and outpatient settings as well as for care plans,
    etc.
    """
    
    resource_name = "MedicationOrder"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items referencing `Request` (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of medication usage.
        Type `str`. """
        
        self.dateWritten = None
        """ When prescription was initially authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.definition = None
        """ Protocol or definition.
        List of `FHIRReference` items referencing `Definition` (represented as `dict` in JSON). """
        
        self.dispenseRequest = None
        """ Medication supply authorization.
        Type `MedicationOrderDispenseRequest` (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ How the medication should be taken.
        List of `DosageInstruction` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter/admission/stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.eventHistory = None
        """ A list of events of interest in the lifecycle.
        List of `FHIRReference` items referencing `Provenance` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ Medication to be taken.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Medication to be taken.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the prescription.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.prescriber = None
        """ Who ordered the initial medication(s).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.priorPrescription = None
        """ An order/prescription that this supersedes.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Reason or indication for writing the prescription.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Condition or Observation that supports why the prescription is
        being written.
        List of `FHIRReference` items referencing `Condition, Observation` (represented as `dict` in JSON). """
        
        self.requisition = None
        """ Identifier of composite.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | on-hold | completed | entered-in-error | stopped | draft.
        Type `str`. """
        
        self.substitution = None
        """ Any restrictions on medication substitution.
        Type `MedicationOrderSubstitution` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Information to support ordering of the medication.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(MedicationOrder, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationOrder, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", str, False, None, False),
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("dispenseRequest", "dispenseRequest", MedicationOrderDispenseRequest, False, None, False),
            ("dosageInstruction", "dosageInstruction", dosageinstruction.DosageInstruction, True, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", annotation.Annotation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, False),
            ("priorPrescription", "priorPrescription", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("requisition", "requisition", identifier.Identifier, False, None, False),
            ("status", "status", str, False, None, False),
            ("substitution", "substitution", MedicationOrderSubstitution, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class MedicationOrderDispenseRequest(backboneelement.BackboneElement):
    """ Medication supply authorization.
    
    Indicates the specific details for the dispense or medication supply part
    of a medication order (also known as a Medication Prescription).  Note that
    this information is NOT always sent with the order.  There may be in some
    settings (e.g. hospitals) institutional or system support for completing
    the dispense details in the pharmacy department.
    """
    
    resource_name = "MedicationOrderDispenseRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expectedSupplyDuration = None
        """ Number of days supply per dispense.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.numberOfRepeatsAllowed = None
        """ Number of refills authorized.
        Type `int`. """
        
        self.quantity = None
        """ Amount of medication to supply per dispense.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationOrderDispenseRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationOrderDispenseRequest, self).elementProperties()
        js.extend([
            ("expectedSupplyDuration", "expectedSupplyDuration", duration.Duration, False, None, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("validityPeriod", "validityPeriod", period.Period, False, None, False),
        ])
        return js


class MedicationOrderSubstitution(backboneelement.BackboneElement):
    """ Any restrictions on medication substitution.
    
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """
    
    resource_name = "MedicationOrderSubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowed = None
        """ Whether substitution is allowed or not.
        Type `bool`. """
        
        self.reason = None
        """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationOrderSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationOrderSubstitution, self).elementProperties()
        js.extend([
            ("allowed", "allowed", bool, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import dosageinstruction
from . import duration
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
