#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/MedicationPrescription) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import duration
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import timing


class MedicationPrescription(domainresource.DomainResource):
    """ Prescription of medication to for patient.
    
    An order for both supply of the medication and the instructions for
    administration of the medicine to a patient.
    """
    
    resource_name = "MedicationPrescription"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dispense = None
        """ Medication supply authorization.
        Type `MedicationPrescriptionDispense` (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ How medication should be taken.
        List of `MedicationPrescriptionDosageInstruction` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medication = None
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
        
        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | on-hold | completed | entered-in-error | stopped |
        superceded | draft.
        Type `str`. """
        
        self.substitution = None
        """ Any restrictions on medication substitution?.
        Type `MedicationPrescriptionSubstitution` (represented as `dict` in JSON). """
        
        super(MedicationPrescription, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationPrescription, self).elementProperties()
        js.extend([
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False),
            ("dispense", "dispense", MedicationPrescriptionDispense, False),
            ("dosageInstruction", "dosageInstruction", MedicationPrescriptionDosageInstruction, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("medication", "medication", fhirreference.FHIRReference, False),
            ("note", "note", str, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("substitution", "substitution", MedicationPrescriptionSubstitution, False),
        ])
        return js


class MedicationPrescriptionDispense(fhirelement.FHIRElement):
    """ Medication supply authorization.
    
    Deals with details of the dispense part of the order.
    """
    
    resource_name = "MedicationPrescriptionDispense"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.expectedSupplyDuration = None
        """ Days supply per dispense.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.medication = None
        """ Product to be supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.numberOfRepeatsAllowed = None
        """ # of refills authorized.
        Type `int`. """
        
        self.quantity = None
        """ Amount of medication to supply per dispense.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.validityPeriod = None
        """ Time period supply is authorized for.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationPrescriptionDispense, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationPrescriptionDispense, self).elementProperties()
        js.extend([
            ("expectedSupplyDuration", "expectedSupplyDuration", duration.Duration, False),
            ("medication", "medication", fhirreference.FHIRReference, False),
            ("numberOfRepeatsAllowed", "numberOfRepeatsAllowed", int, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("validityPeriod", "validityPeriod", period.Period, False),
        ])
        return js


class MedicationPrescriptionDosageInstruction(fhirelement.FHIRElement):
    """ How medication should be taken.
    
    Indicates how the medication is to be used by the patient.
    """
    
    resource_name = "MedicationPrescriptionDosageInstruction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additionalInstructions = None
        """ Supplemental instructions - e.g. "with meals".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = None
        """ Take "as needed" f(or x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" f(or x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseQuantity = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rate = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.scheduledDateTime = None
        """ When medication should be administered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.scheduledPeriod = None
        """ When medication should be administered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledTiming = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Dosage instructions expressed as text.
        Type `str`. """
        
        super(MedicationPrescriptionDosageInstruction, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationPrescriptionDosageInstruction, self).elementProperties()
        js.extend([
            ("additionalInstructions", "additionalInstructions", codeableconcept.CodeableConcept, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False),
            ("doseRange", "doseRange", range.Range, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False),
            ("method", "method", codeableconcept.CodeableConcept, False),
            ("rate", "rate", ratio.Ratio, False),
            ("route", "route", codeableconcept.CodeableConcept, False),
            ("scheduledDateTime", "scheduledDateTime", fhirdate.FHIRDate, False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False),
            ("scheduledTiming", "scheduledTiming", timing.Timing, False),
            ("site", "site", codeableconcept.CodeableConcept, False),
            ("text", "text", str, False),
        ])
        return js


class MedicationPrescriptionSubstitution(fhirelement.FHIRElement):
    """ Any restrictions on medication substitution?.
    
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """
    
    resource_name = "MedicationPrescriptionSubstitution"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.reason = None
        """ Why should substitution (not) be made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ generic | formulary +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationPrescriptionSubstitution, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationPrescriptionSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

