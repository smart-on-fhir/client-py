#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (medicationdispense.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
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


class MedicationDispense(fhirresource.FHIRResource):
    """ Dispensing a medication to a named patient.
    
    Dispensing a medication to a named patient.  This includes a description of
    the supply provided and the instructions for administering the medication.
    """
    
    resource_name = "MedicationDispense"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authorizingPrescription = None
        """ Medication order that authorizes the dispense.
        List of `FHIRReference` items referencing `MedicationPrescription` (represented as `dict` in JSON). """
        
        self.daysSupply = None
        """ Days Supply.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.destination = None
        """ Where the medication was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.dispenser = None
        """ Practitioner responsible for dispensing medication.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ Medicine administration instructions to the patient/carer.
        List of `MedicationDispenseDosageInstruction` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.medication = None
        """ What medication was supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who the dispense is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ Who collected the medication.
        List of `FHIRReference` items referencing `Patient, Practitioner` (represented as `dict` in JSON). """
        
        self.status = None
        """ in progress | on hold | completed | entered in error | stopped.
        Type `str`. """
        
        self.substitution = None
        """ Deals with substitution of one medicine for another.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """
        
        self.type = None
        """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.whenHandedOver = None
        """ Handover time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whenPrepared = None
        """ Dispense processing time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(MedicationDispense, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispense, self).update_with_json(jsondict)
        if 'authorizingPrescription' in jsondict:
            self.authorizingPrescription = fhirreference.FHIRReference.with_json_and_owner(jsondict['authorizingPrescription'], self)
        if 'daysSupply' in jsondict:
            self.daysSupply = quantity.Quantity.with_json_and_owner(jsondict['daysSupply'], self)
        if 'destination' in jsondict:
            self.destination = fhirreference.FHIRReference.with_json_and_owner(jsondict['destination'], self)
        if 'dispenser' in jsondict:
            self.dispenser = fhirreference.FHIRReference.with_json_and_owner(jsondict['dispenser'], self)
        if 'dosageInstruction' in jsondict:
            self.dosageInstruction = MedicationDispenseDosageInstruction.with_json_and_owner(jsondict['dosageInstruction'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'receiver' in jsondict:
            self.receiver = fhirreference.FHIRReference.with_json_and_owner(jsondict['receiver'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'substitution' in jsondict:
            self.substitution = MedicationDispenseSubstitution.with_json_and_owner(jsondict['substitution'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'whenHandedOver' in jsondict:
            self.whenHandedOver = fhirdate.FHIRDate.with_json_and_owner(jsondict['whenHandedOver'], self)
        if 'whenPrepared' in jsondict:
            self.whenPrepared = fhirdate.FHIRDate.with_json_and_owner(jsondict['whenPrepared'], self)


class MedicationDispenseDosageInstruction(fhirelement.FHIRElement):
    """ Medicine administration instructions to the patient/carer.
    
    Indicates how the medication is to be used by the patient.
    """
    
    resource_name = "MedicationDispenseDosageInstruction"
    
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
        
        self.scheduleDateTime = None
        """ When medication should be administered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.schedulePeriod = None
        """ When medication should be administered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduleTiming = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationDispenseDosageInstruction, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispenseDosageInstruction, self).update_with_json(jsondict)
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
        if 'scheduleDateTime' in jsondict:
            self.scheduleDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['scheduleDateTime'], self)
        if 'schedulePeriod' in jsondict:
            self.schedulePeriod = period.Period.with_json_and_owner(jsondict['schedulePeriod'], self)
        if 'scheduleTiming' in jsondict:
            self.scheduleTiming = timing.Timing.with_json_and_owner(jsondict['scheduleTiming'], self)
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['site'], self)


class MedicationDispenseSubstitution(fhirelement.FHIRElement):
    """ Deals with substitution of one medicine for another.
    
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases substitution will be expected but doesn't happen, in other cases
    substitution is not expected but does happen.  This block explains what
    substitition did or did not happen and why.
    """
    
    resource_name = "MedicationDispenseSubstitution"
    
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
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'responsibleParty' in jsondict:
            self.responsibleParty = fhirreference.FHIRReference.with_json_and_owner(jsondict['responsibleParty'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

