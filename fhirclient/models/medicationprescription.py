#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (medicationprescription.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import duration
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period
import quantity
import range
import ratio
import timing


class MedicationPrescription(fhirresource.FHIRResource):
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
        """ active | on hold | completed | entered in error | stopped |
        superceded | draft.
        Type `str`. """
        
        self.substitution = None
        """ Any restrictions on medication substitution?.
        Type `MedicationPrescriptionSubstitution` (represented as `dict` in JSON). """
        
        super(MedicationPrescription, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationPrescription, self).update_with_json(jsondict)
        if 'dateWritten' in jsondict:
            self.dateWritten = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateWritten'], self)
        if 'dispense' in jsondict:
            self.dispense = MedicationPrescriptionDispense.with_json_and_owner(jsondict['dispense'], self)
        if 'dosageInstruction' in jsondict:
            self.dosageInstruction = MedicationPrescriptionDosageInstruction.with_json_and_owner(jsondict['dosageInstruction'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'prescriber' in jsondict:
            self.prescriber = fhirreference.FHIRReference.with_json_and_owner(jsondict['prescriber'], self)
        if 'reasonCodeableConcept' in jsondict:
            self.reasonCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonCodeableConcept'], self)
        if 'reasonReference' in jsondict:
            self.reasonReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reasonReference'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'substitution' in jsondict:
            self.substitution = MedicationPrescriptionSubstitution.with_json_and_owner(jsondict['substitution'], self)


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
    
    def update_with_json(self, jsondict):
        super(MedicationPrescriptionDispense, self).update_with_json(jsondict)
        if 'expectedSupplyDuration' in jsondict:
            self.expectedSupplyDuration = duration.Duration.with_json_and_owner(jsondict['expectedSupplyDuration'], self)
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self)
        if 'numberOfRepeatsAllowed' in jsondict:
            self.numberOfRepeatsAllowed = jsondict['numberOfRepeatsAllowed']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'validityPeriod' in jsondict:
            self.validityPeriod = period.Period.with_json_and_owner(jsondict['validityPeriod'], self)


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
        
        self.asNeededBoolean = False
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
    
    def update_with_json(self, jsondict):
        super(MedicationPrescriptionDosageInstruction, self).update_with_json(jsondict)
        if 'additionalInstructions' in jsondict:
            self.additionalInstructions = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['additionalInstructions'], self)
        if 'asNeededBoolean' in jsondict:
            self.asNeededBoolean = jsondict['asNeededBoolean']
        if 'asNeededCodeableConcept' in jsondict:
            self.asNeededCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['asNeededCodeableConcept'], self)
        if 'doseQuantity' in jsondict:
            self.doseQuantity = quantity.Quantity.with_json_and_owner(jsondict['doseQuantity'], self)
        if 'doseRange' in jsondict:
            self.doseRange = range.Range.with_json_and_owner(jsondict['doseRange'], self)
        if 'maxDosePerPeriod' in jsondict:
            self.maxDosePerPeriod = ratio.Ratio.with_json_and_owner(jsondict['maxDosePerPeriod'], self)
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['method'], self)
        if 'rate' in jsondict:
            self.rate = ratio.Ratio.with_json_and_owner(jsondict['rate'], self)
        if 'route' in jsondict:
            self.route = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['route'], self)
        if 'scheduledDateTime' in jsondict:
            self.scheduledDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['scheduledDateTime'], self)
        if 'scheduledPeriod' in jsondict:
            self.scheduledPeriod = period.Period.with_json_and_owner(jsondict['scheduledPeriod'], self)
        if 'scheduledTiming' in jsondict:
            self.scheduledTiming = timing.Timing.with_json_and_owner(jsondict['scheduledTiming'], self)
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['site'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']


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
    
    def update_with_json(self, jsondict):
        super(MedicationPrescriptionSubstitution, self).update_with_json(jsondict)
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

