#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (medicationdispense.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period
import quantity
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
        
        super(MedicationDispense, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispense, self).update_with_json(jsondict)
        if 'authorizingPrescription' in jsondict:
            self.authorizingPrescription = fhirreference.FHIRReference.with_json_and_owner(jsondict['authorizingPrescription'], self)
        if 'dispense' in jsondict:
            self.dispense = MedicationDispenseDispense.with_json_and_owner(jsondict['dispense'], self)
        if 'dispenser' in jsondict:
            self.dispenser = fhirreference.FHIRReference.with_json_and_owner(jsondict['dispenser'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'substitution' in jsondict:
            self.substitution = MedicationDispenseSubstitution.with_json_and_owner(jsondict['substitution'], self)


class MedicationDispenseDispense(fhirelement.FHIRElement):
    """ Details for individual dispensed medicationdetails.
    
    Indicates the details of the dispense event such as the days supply and
    quantity of medication dispensed.
    """
    
    resource_name = "MedicationDispenseDispense"
    
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
        List of `FHIRReference` items referencing `Patient, Practitioner` (represented as `dict` in JSON). """
        
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
            self.destination = fhirreference.FHIRReference.with_json_and_owner(jsondict['destination'], self)
        if 'dosage' in jsondict:
            self.dosage = MedicationDispenseDispenseDosage.with_json_and_owner(jsondict['dosage'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'receiver' in jsondict:
            self.receiver = fhirreference.FHIRReference.with_json_and_owner(jsondict['receiver'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'whenHandedOver' in jsondict:
            self.whenHandedOver = fhirdate.FHIRDate.with_json_and_owner(jsondict['whenHandedOver'], self)
        if 'whenPrepared' in jsondict:
            self.whenPrepared = fhirdate.FHIRDate.with_json_and_owner(jsondict['whenPrepared'], self)


class MedicationDispenseDispenseDosage(fhirelement.FHIRElement):
    """ Medicine administration instructions to the patient/carer.
    
    Indicates how the medication is to be used by the patient.
    """
    
    resource_name = "MedicationDispenseDispenseDosage"
    
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
        
        super(MedicationDispenseDispenseDosage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationDispenseDispenseDosage, self).update_with_json(jsondict)
        if 'additionalInstructions' in jsondict:
            self.additionalInstructions = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['additionalInstructions'], self)
        if 'asNeededBoolean' in jsondict:
            self.asNeededBoolean = jsondict['asNeededBoolean']
        if 'asNeededCodeableConcept' in jsondict:
            self.asNeededCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['asNeededCodeableConcept'], self)
        if 'maxDosePerPeriod' in jsondict:
            self.maxDosePerPeriod = ratio.Ratio.with_json_and_owner(jsondict['maxDosePerPeriod'], self)
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['method'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
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

