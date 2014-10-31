#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medicationprescription.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import condition
import duration
import encounter
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import medication
import narrative
import patient
import period
import practitioner
import quantity
import ratio
import schedule


class MedicationPrescription(fhirresource.FHIRResource):
    """ Prescription of medication to for patient.
    
    Scope and Usage This resource covers all orders for medications for a
    patient. This includes in-patient medication orders as well as community
    orders (whether filled by the prescriber or by a pharmacy). It also
    includes orders for over-the-counter medications (e.g. Aspirin) and dietary
    supplements. It may be used to support the order of medication-related
    devices. It is not intended for use in prescribing particular diets, or for
    ordering non-medication-related items (eye-glasses, supplies, etc.)
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
        
        self.reasonResource = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | on hold | completed | entered in error | stopped |
        superceded.
        Type `str`. """
        
        self.substitution = None
        """ Any restrictions on medication substitution?.
        Type `MedicationPrescriptionSubstitution` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(MedicationPrescription, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationPrescription, self).update_with_json(jsondict)
        if 'dateWritten' in jsondict:
            self.dateWritten = fhirdate.FHIRDate.with_json(jsondict['dateWritten'])
        if 'dispense' in jsondict:
            self.dispense = MedicationPrescriptionDispense.with_json(jsondict['dispense'])
        if 'dosageInstruction' in jsondict:
            self.dosageInstruction = MedicationPrescriptionDosageInstruction.with_json(jsondict['dosageInstruction'])
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, encounter.Encounter)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self, medication.Medication)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self, patient.Patient)
        if 'prescriber' in jsondict:
            self.prescriber = fhirreference.FHIRReference.with_json_and_owner(jsondict['prescriber'], self, practitioner.Practitioner)
        if 'reasonCodeableConcept' in jsondict:
            self.reasonCodeableConcept = codeableconcept.CodeableConcept.with_json(jsondict['reasonCodeableConcept'])
        if 'reasonResource' in jsondict:
            self.reasonResource = fhirreference.FHIRReference.with_json_and_owner(jsondict['reasonResource'], self, condition.Condition)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'substitution' in jsondict:
            self.substitution = MedicationPrescriptionSubstitution.with_json(jsondict['substitution'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class MedicationPrescriptionDosageInstruction(fhirelement.FHIRElement):
    """ How medication should be taken.
    
    Indicates how the medication is to be used by the patient.
    """
    
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
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Dosage instructions expressed as text.
        Type `str`. """
        
        self.timingDateTime = None
        """ When medication should be administered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ When medication should be administered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingSchedule = None
        """ When medication should be administered.
        Type `Schedule` (represented as `dict` in JSON). """
        
        super(MedicationPrescriptionDosageInstruction, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationPrescriptionDosageInstruction, self).update_with_json(jsondict)
        if 'additionalInstructions' in jsondict:
            self.additionalInstructions = codeableconcept.CodeableConcept.with_json(jsondict['additionalInstructions'])
        if 'asNeededBoolean' in jsondict:
            self.asNeededBoolean = jsondict['asNeededBoolean']
        if 'asNeededCodeableConcept' in jsondict:
            self.asNeededCodeableConcept = codeableconcept.CodeableConcept.with_json(jsondict['asNeededCodeableConcept'])
        if 'doseQuantity' in jsondict:
            self.doseQuantity = quantity.Quantity.with_json(jsondict['doseQuantity'])
        if 'maxDosePerPeriod' in jsondict:
            self.maxDosePerPeriod = ratio.Ratio.with_json(jsondict['maxDosePerPeriod'])
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json(jsondict['method'])
        if 'rate' in jsondict:
            self.rate = ratio.Ratio.with_json(jsondict['rate'])
        if 'route' in jsondict:
            self.route = codeableconcept.CodeableConcept.with_json(jsondict['route'])
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json(jsondict['site'])
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'timingDateTime' in jsondict:
            self.timingDateTime = fhirdate.FHIRDate.with_json(jsondict['timingDateTime'])
        if 'timingPeriod' in jsondict:
            self.timingPeriod = period.Period.with_json(jsondict['timingPeriod'])
        if 'timingSchedule' in jsondict:
            self.timingSchedule = schedule.Schedule.with_json(jsondict['timingSchedule'])


class MedicationPrescriptionDispense(fhirelement.FHIRElement):
    """ Medication supply authorization.
    
    Deals with details of the dispense part of the order.
    """
    
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
            self.expectedSupplyDuration = duration.Duration.with_json(jsondict['expectedSupplyDuration'])
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self, medication.Medication)
        if 'numberOfRepeatsAllowed' in jsondict:
            self.numberOfRepeatsAllowed = jsondict['numberOfRepeatsAllowed']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json(jsondict['quantity'])
        if 'validityPeriod' in jsondict:
            self.validityPeriod = period.Period.with_json(jsondict['validityPeriod'])


class MedicationPrescriptionSubstitution(fhirelement.FHIRElement):
    """ Any restrictions on medication substitution?.
    
    Indicates whether or not substitution can or should be part of the
    dispense. In some cases substitution must happen, in other cases
    substitution must not happen, and in others it does not matter. This block
    explains the prescriber's intent. If nothing is specified substitution may
    be done.
    """
    
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
            self.reason = codeableconcept.CodeableConcept.with_json(jsondict['reason'])
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])

