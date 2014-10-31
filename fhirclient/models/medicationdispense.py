#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medicationdispense.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import location
import medication
import medicationprescription
import narrative
import patient
import period
import practitioner
import quantity
import ratio
import schedule


class MedicationDispense(fhirresource.FHIRResource):
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
            self.authorizingPrescription = fhirreference.FHIRReference.with_json_and_owner(jsondict['authorizingPrescription'], self, medicationprescription.MedicationPrescription)
        if 'dispense' in jsondict:
            self.dispense = MedicationDispenseDispense.with_json(jsondict['dispense'])
        if 'dispenser' in jsondict:
            self.dispenser = fhirreference.FHIRReference.with_json_and_owner(jsondict['dispenser'], self, practitioner.Practitioner)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self, patient.Patient)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'substitution' in jsondict:
            self.substitution = MedicationDispenseSubstitution.with_json(jsondict['substitution'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class MedicationDispenseDispense(fhirelement.FHIRElement):
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
            self.destination = fhirreference.FHIRReference.with_json_and_owner(jsondict['destination'], self, location.Location)
        if 'dosage' in jsondict:
            self.dosage = MedicationDispenseDispenseDosage.with_json(jsondict['dosage'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self, medication.Medication)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json(jsondict['quantity'])
        if 'receiver' in jsondict:
            self.receiver = fhirreference.FHIRReference.with_json_and_owner(jsondict['receiver'], self, patient.Patient)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])
        if 'whenHandedOver' in jsondict:
            self.whenHandedOver = fhirdate.FHIRDate.with_json(jsondict['whenHandedOver'])
        if 'whenPrepared' in jsondict:
            self.whenPrepared = fhirdate.FHIRDate.with_json(jsondict['whenPrepared'])


class MedicationDispenseDispenseDosage(fhirelement.FHIRElement):
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
            self.additionalInstructions = codeableconcept.CodeableConcept.with_json(jsondict['additionalInstructions'])
        if 'asNeededBoolean' in jsondict:
            self.asNeededBoolean = jsondict['asNeededBoolean']
        if 'asNeededCodeableConcept' in jsondict:
            self.asNeededCodeableConcept = codeableconcept.CodeableConcept.with_json(jsondict['asNeededCodeableConcept'])
        if 'maxDosePerPeriod' in jsondict:
            self.maxDosePerPeriod = ratio.Ratio.with_json(jsondict['maxDosePerPeriod'])
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json(jsondict['method'])
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json(jsondict['quantity'])
        if 'rate' in jsondict:
            self.rate = ratio.Ratio.with_json(jsondict['rate'])
        if 'route' in jsondict:
            self.route = codeableconcept.CodeableConcept.with_json(jsondict['route'])
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json(jsondict['site'])
        if 'timingDateTime' in jsondict:
            self.timingDateTime = fhirdate.FHIRDate.with_json(jsondict['timingDateTime'])
        if 'timingPeriod' in jsondict:
            self.timingPeriod = period.Period.with_json(jsondict['timingPeriod'])
        if 'timingSchedule' in jsondict:
            self.timingSchedule = schedule.Schedule.with_json(jsondict['timingSchedule'])


class MedicationDispenseSubstitution(fhirelement.FHIRElement):
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
            self.reason = codeableconcept.CodeableConcept.with_json(jsondict['reason'])
        if 'responsibleParty' in jsondict:
            self.responsibleParty = fhirreference.FHIRReference.with_json_and_owner(jsondict['responsibleParty'], self, practitioner.Practitioner)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json(jsondict['type'])

