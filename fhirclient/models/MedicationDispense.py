#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medicationdispense.profile.json) on 2014-10-17.
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
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Location
import Medication
import MedicationPrescription
import Narrative
import Patient
import Period
import Practitioner
import Quantity
import Ratio
import Schedule


class MedicationDispense(FHIRResource.FHIRResource):
    """ Dispensing a medication to a named patient.
    
    Scope and Usage This resource covers the supply of all medications to a
    patient. Examples include dispensing and pick-up from an out-patient
    pharmacy, dispensing patient-specific medications from in-patient pharmacy
    to ward as well as issuing a single dose from ward stock to a patient for
    consumption.
    """
    
    resource_name = "MedicationDispense"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authorizingPrescription = None
        """ Medication order that authorizes the dispense.
        List of `FHIRReference` items referencing `MedicationPrescription` (represented as `dict` in JSON). """
        
        self.dispense = None
        """ Details for individual dispensed medicationdetails.
        List of `MedicationDispenseDispense` items (represented as `dict` in JSON). """
        
        self.dispenser = None
        """ Practitioner responsible for dispensing medication.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who the dispense is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ in progress | on hold | completed | entered in error | stopped.
        Type `str`. """
        
        self.substitution = None
        """ Deals with substitution of one medicine for another.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(MedicationDispense, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispense, self).update_with_json(jsondict)
        if 'authorizingPrescription' in jsondict:
            self.authorizingPrescription = FHIRReference.FHIRReference.with_json_and_owner(jsondict['authorizingPrescription'], self, MedicationPrescription.MedicationPrescription)
        if 'dispense' in jsondict:
            self.dispense = MedicationDispenseDispense.with_json(jsondict['dispense'])
        if 'dispenser' in jsondict:
            self.dispenser = FHIRReference.FHIRReference.with_json_and_owner(jsondict['dispenser'], self, Practitioner.Practitioner)
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'patient' in jsondict:
            self.patient = FHIRReference.FHIRReference.with_json_and_owner(jsondict['patient'], self, Patient.Patient)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'substitution' in jsondict:
            self.substitution = MedicationDispenseSubstitution.with_json(jsondict['substitution'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])


class MedicationDispenseDispense(FHIRElement.FHIRElement):
    """ Details for individual dispensed medicationdetails.
    
    Indicates the details of the dispense event such as the days supply and
    quantity of medication dispensed.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.destination = None
        """ Where the medication was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Medicine administration instructions to the patient/carer.
        List of `MedicationDispenseDispenseDosage` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier for individual item.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.medication = None
        """ What medication was supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ Who collected the medication.
        List of `FHIRReference` items referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ in progress | on hold | completed | entered in error | stopped.
        Type `str`. """
        
        self.type = None
        """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.whenHandedOver = None
        """ Handover time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whenPrepared = None
        """ Dispense processing time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(MedicationDispenseDispense, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispenseDispense, self).update_with_json(jsondict)
        if 'destination' in jsondict:
            self.destination = FHIRReference.FHIRReference.with_json_and_owner(jsondict['destination'], self, Location.Location)
        if 'dosage' in jsondict:
            self.dosage = MedicationDispenseDispenseDosage.with_json(jsondict['dosage'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'medication' in jsondict:
            self.medication = FHIRReference.FHIRReference.with_json_and_owner(jsondict['medication'], self, Medication.Medication)
        if 'quantity' in jsondict:
            self.quantity = Quantity.Quantity.with_json(jsondict['quantity'])
        if 'receiver' in jsondict:
            self.receiver = FHIRReference.FHIRReference.with_json_and_owner(jsondict['receiver'], self, Patient.Patient)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])
        if 'whenHandedOver' in jsondict:
            self.whenHandedOver = FHIRDate.FHIRDate.with_json(jsondict['whenHandedOver'])
        if 'whenPrepared' in jsondict:
            self.whenPrepared = FHIRDate.FHIRDate.with_json(jsondict['whenPrepared'])


class MedicationDispenseDispenseDosage(FHIRElement.FHIRElement):
    """ Medicine administration instructions to the patient/carer.
    
    Indicates how the medication is to be used by the patient.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additionalInstructions = None
        """ E.g. "Take with food".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.asNeededBoolean = False
        """ Take "as needed" f(or x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" f(or x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount of medication per dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rate = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ When medication should be administered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ When medication should be administered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingSchedule = None
        """ When medication should be administered.
        Type `Schedule` (represented as `dict` in JSON). """
        
        super(MedicationDispenseDispenseDosage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispenseDispenseDosage, self).update_with_json(jsondict)
        if 'additionalInstructions' in jsondict:
            self.additionalInstructions = CodeableConcept.CodeableConcept.with_json(jsondict['additionalInstructions'])
        if 'asNeededBoolean' in jsondict:
            self.asNeededBoolean = jsondict['asNeededBoolean']
        if 'asNeededCodeableConcept' in jsondict:
            self.asNeededCodeableConcept = CodeableConcept.CodeableConcept.with_json(jsondict['asNeededCodeableConcept'])
        if 'maxDosePerPeriod' in jsondict:
            self.maxDosePerPeriod = Ratio.Ratio.with_json(jsondict['maxDosePerPeriod'])
        if 'method' in jsondict:
            self.method = CodeableConcept.CodeableConcept.with_json(jsondict['method'])
        if 'quantity' in jsondict:
            self.quantity = Quantity.Quantity.with_json(jsondict['quantity'])
        if 'rate' in jsondict:
            self.rate = Ratio.Ratio.with_json(jsondict['rate'])
        if 'route' in jsondict:
            self.route = CodeableConcept.CodeableConcept.with_json(jsondict['route'])
        if 'site' in jsondict:
            self.site = CodeableConcept.CodeableConcept.with_json(jsondict['site'])
        if 'timingDateTime' in jsondict:
            self.timingDateTime = FHIRDate.FHIRDate.with_json(jsondict['timingDateTime'])
        if 'timingPeriod' in jsondict:
            self.timingPeriod = Period.Period.with_json(jsondict['timingPeriod'])
        if 'timingSchedule' in jsondict:
            self.timingSchedule = Schedule.Schedule.with_json(jsondict['timingSchedule'])


class MedicationDispenseSubstitution(FHIRElement.FHIRElement):
    """ Deals with substitution of one medicine for another.
    
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases substitution will be expected but doesn't happen, in other cases
    substitution is not expected but does happen.  This block explains what
    substitition did or did not happen and why.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.reason = None
        """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.responsibleParty = None
        """ Who is responsible for the substitution.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of substitiution.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationDispenseSubstitution, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispenseSubstitution, self).update_with_json(jsondict)
        if 'reason' in jsondict:
            self.reason = CodeableConcept.CodeableConcept.with_json(jsondict['reason'])
        if 'responsibleParty' in jsondict:
            self.responsibleParty = FHIRReference.FHIRReference.with_json_and_owner(jsondict['responsibleParty'], self, Practitioner.Practitioner)
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])

