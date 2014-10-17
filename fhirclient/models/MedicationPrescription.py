#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medicationprescription.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import CodeableConcept
import Condition
import Duration
import Encounter
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Medication
import Narrative
import Patient
import Period
import Practitioner
import Quantity
import Ratio
import Schedule


class MedicationPrescription(FHIRResource.FHIRResource):
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
            self.dateWritten = FHIRDate.FHIRDate.with_json(jsondict['dateWritten'])
        if 'dispense' in jsondict:
            self.dispense = MedicationPrescriptionDispense.with_json(jsondict['dispense'])
        if 'dosageInstruction' in jsondict:
            self.dosageInstruction = MedicationPrescriptionDosageInstruction.with_json(jsondict['dosageInstruction'])
        if 'encounter' in jsondict:
            self.encounter = FHIRReference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, Encounter.Encounter)
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'medication' in jsondict:
            self.medication = FHIRReference.FHIRReference.with_json_and_owner(jsondict['medication'], self, Medication.Medication)
        if 'patient' in jsondict:
            self.patient = FHIRReference.FHIRReference.with_json_and_owner(jsondict['patient'], self, Patient.Patient)
        if 'prescriber' in jsondict:
            self.prescriber = FHIRReference.FHIRReference.with_json_and_owner(jsondict['prescriber'], self, Practitioner.Practitioner)
        if 'reasonCodeableConcept' in jsondict:
            self.reasonCodeableConcept = CodeableConcept.CodeableConcept.with_json(jsondict['reasonCodeableConcept'])
        if 'reasonResource' in jsondict:
            self.reasonResource = FHIRReference.FHIRReference.with_json_and_owner(jsondict['reasonResource'], self, Condition.Condition)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'substitution' in jsondict:
            self.substitution = MedicationPrescriptionSubstitution.with_json(jsondict['substitution'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])


class MedicationPrescriptionDosageInstruction(FHIRElement.FHIRElement):
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
            self.additionalInstructions = CodeableConcept.CodeableConcept.with_json(jsondict['additionalInstructions'])
        if 'asNeededBoolean' in jsondict:
            self.asNeededBoolean = jsondict['asNeededBoolean']
        if 'asNeededCodeableConcept' in jsondict:
            self.asNeededCodeableConcept = CodeableConcept.CodeableConcept.with_json(jsondict['asNeededCodeableConcept'])
        if 'doseQuantity' in jsondict:
            self.doseQuantity = Quantity.Quantity.with_json(jsondict['doseQuantity'])
        if 'maxDosePerPeriod' in jsondict:
            self.maxDosePerPeriod = Ratio.Ratio.with_json(jsondict['maxDosePerPeriod'])
        if 'method' in jsondict:
            self.method = CodeableConcept.CodeableConcept.with_json(jsondict['method'])
        if 'rate' in jsondict:
            self.rate = Ratio.Ratio.with_json(jsondict['rate'])
        if 'route' in jsondict:
            self.route = CodeableConcept.CodeableConcept.with_json(jsondict['route'])
        if 'site' in jsondict:
            self.site = CodeableConcept.CodeableConcept.with_json(jsondict['site'])
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'timingDateTime' in jsondict:
            self.timingDateTime = FHIRDate.FHIRDate.with_json(jsondict['timingDateTime'])
        if 'timingPeriod' in jsondict:
            self.timingPeriod = Period.Period.with_json(jsondict['timingPeriod'])
        if 'timingSchedule' in jsondict:
            self.timingSchedule = Schedule.Schedule.with_json(jsondict['timingSchedule'])


class MedicationPrescriptionDispense(FHIRElement.FHIRElement):
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
            self.expectedSupplyDuration = Duration.Duration.with_json(jsondict['expectedSupplyDuration'])
        if 'medication' in jsondict:
            self.medication = FHIRReference.FHIRReference.with_json_and_owner(jsondict['medication'], self, Medication.Medication)
        if 'numberOfRepeatsAllowed' in jsondict:
            self.numberOfRepeatsAllowed = jsondict['numberOfRepeatsAllowed']
        if 'quantity' in jsondict:
            self.quantity = Quantity.Quantity.with_json(jsondict['quantity'])
        if 'validityPeriod' in jsondict:
            self.validityPeriod = Period.Period.with_json(jsondict['validityPeriod'])


class MedicationPrescriptionSubstitution(FHIRElement.FHIRElement):
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
            self.reason = CodeableConcept.CodeableConcept.with_json(jsondict['reason'])
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])

