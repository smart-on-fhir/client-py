#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medicationstatement.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import device
import fhirelement
import fhirreference
import fhirresource
import identifier
import medication
import narrative
import patient
import period
import quantity
import ratio
import schedule


class MedicationStatement(fhirresource.FHIRResource):
    """ Administration of medication to a patient.
    
    Scope and Usage Common usage includes:
    
    * the recording of non-prescription and/or recreational drugs
    * the recording of an intake medication list upon admission to hospital
    * the summarization of a patient's "active medications" in a patient
    profile
    """
    
    resource_name = "MedicationStatement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.device = None
        """ E.g. infusion pump.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        List of `MedicationStatementDosage` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medication = None
        """ What medication was taken?.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who was/is taking medication.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ True if asserting medication was not given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.wasNotGiven = False
        """ True if medication is/was not being taken.
        Type `bool`. """
        
        self.whenGiven = None
        """ Over what period was medication consumed?.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationStatement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationStatement, self).update_with_json(jsondict)
        if 'device' in jsondict:
            self.device = fhirreference.FHIRReference.with_json_and_owner(jsondict['device'], self, device.Device)
        if 'dosage' in jsondict:
            self.dosage = MedicationStatementDosage.with_json(jsondict['dosage'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self, medication.Medication)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self, patient.Patient)
        if 'reasonNotGiven' in jsondict:
            self.reasonNotGiven = codeableconcept.CodeableConcept.with_json(jsondict['reasonNotGiven'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'wasNotGiven' in jsondict:
            self.wasNotGiven = jsondict['wasNotGiven']
        if 'whenGiven' in jsondict:
            self.whenGiven = period.Period.with_json(jsondict['whenGiven'])


class MedicationStatementDosage(fhirelement.FHIRElement):
    """ Details of how medication was taken.
    
    Indicates how the medication is/was used by the patient.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.asNeededBoolean = False
        """ Take "as needed" f(or x).
        Type `bool`. """
        
        self.asNeededCodeableConcept = None
        """ Take "as needed" f(or x).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Maximum dose that was consumed per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique used to administer medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount administered in one dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rate = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ How did the medication enter the body?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Where on body was medication administered?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timing = None
        """ When/how often was medication taken?.
        Type `Schedule` (represented as `dict` in JSON). """
        
        super(MedicationStatementDosage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationStatementDosage, self).update_with_json(jsondict)
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
        if 'timing' in jsondict:
            self.timing = schedule.Schedule.with_json(jsondict['timing'])

