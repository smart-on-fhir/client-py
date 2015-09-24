#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/MedicationOrder) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import timing


class MedicationOrder(domainresource.DomainResource):
    """ Prescription of medication to for patient.
    
    An order for both supply of the medication and the instructions for
    administration of the medication to a patient. The resource is called
    "MedicationOrder" rather than "MedicationPrescription" to generalize the
    use across inpatient and outpatient settings as well as for care plans,
    etc.
    """
    
    resource_name = "MedicationOrder"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.dateEnded = None
        """ When prescription was stopped.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dispenseRequest = None
        """ Medication supply authorization.
        Type `MedicationOrderDispenseRequest` (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ How medication should be taken.
        List of `MedicationOrderDosageInstruction` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter/admission/stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
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
        Type `str`. """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.prescriber = None
        """ Who ordered the medication(s).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.priorPrescription = None
        """ An order/prescription that this supersedes.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonEnded = None
        """ Why prescription was stopped.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | on-hold | completed | entered-in-error | stopped | draft.
        Type `str`. """
        
        self.substitution = None
        """ Any restrictions on medication substitution.
        Type `MedicationOrderSubstitution` (represented as `dict` in JSON). """
        
        super(MedicationOrder, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationOrder, self).elementProperties()
        js.extend([
            ("dateEnded", "dateEnded", fhirdate.FHIRDate, False),
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False),
            ("dispenseRequest", "dispenseRequest", MedicationOrderDispenseRequest, False),
            ("dosageInstruction", "dosageInstruction", MedicationOrderDosageInstruction, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False),
            ("note", "note", str, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False),
            ("priorPrescription", "priorPrescription", fhirreference.FHIRReference, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False),
            ("reasonEnded", "reasonEnded", codeableconcept.CodeableConcept, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("substitution", "substitution", MedicationOrderSubstitution, False),
        ])
        return js


class MedicationOrderDispenseRequest(fhirelement.FHIRElement):
    """ Medication supply authorization.
    
    Indicates the specific details for the dispense or medication supply part
    of a medication order (also known as a Medication Prescription).  Note that
    this information is NOT always sent with the order.  There may be in some
    settings (e.g. hospitals) institutional or system support for completing
    the dispense details in the pharmacy department.
    """
    
    resource_name = "MedicationOrderDispenseRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.expectedSupplyDuration = None
        """ Number of days supply per dispense.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
        """ Product to be supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.numberOfRepeatsAllowed = None
        """ Number of refills authorized.
        Type `int`. """
        
        self.quantity = None
        """ Amount of medication to supply per dispense.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationOrderDispenseRequest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationOrderDispenseRequest, self).elementProperties()
        js.extend([
            ("expectedSupplyDuration", "expectedSupplyDuration", quantity.Quantity, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("validityPeriod", "validityPeriod", period.Period, False),
        ])
        return js


class MedicationOrderDosageInstruction(fhirelement.FHIRElement):
    """ How medication should be taken.
    
    Indicates how the medication is to be used by the patient.
    """
    
    resource_name = "MedicationOrderDosageInstruction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additionalInstructions = None
        """ Supplemental instructions - e.g. "with meals".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Take "as needed" (for x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" (for x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseQuantity = None
        """ Amount of medication per dose.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteCodeableConcept = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Body site to administer to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        self.text = None
        """ Dosage instructions expressed as text.
        Type `str`. """
        
        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(MedicationOrderDosageInstruction, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationOrderDosageInstruction, self).elementProperties()
        js.extend([
            ("additionalInstructions", "additionalInstructions", codeableconcept.CodeableConcept, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False),
            ("doseRange", "doseRange", range.Range, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False),
            ("method", "method", codeableconcept.CodeableConcept, False),
            ("rateRange", "rateRange", range.Range, False),
            ("rateRatio", "rateRatio", ratio.Ratio, False),
            ("route", "route", codeableconcept.CodeableConcept, False),
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False),
            ("text", "text", str, False),
            ("timing", "timing", timing.Timing, False),
        ])
        return js


class MedicationOrderSubstitution(fhirelement.FHIRElement):
    """ Any restrictions on medication substitution.
    
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """
    
    resource_name = "MedicationOrderSubstitution"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.reason = None
        """ Why should (not) substitution be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ generic | formulary +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationOrderSubstitution, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationOrderSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

