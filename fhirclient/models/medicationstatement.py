#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (medicationstatement.profile.json) on 2015-01-23.
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


class MedicationStatement(fhirresource.FHIRResource):
    """ Administration of medication to a patient.
    
    A record of medication being taken by a patient, or that the medication has
    been given to a patient where the record is the result of a report from the
    patient or another clinician.
    """
    
    resource_name = "MedicationStatement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.dosage = None
        """ Details of how medication was taken.
        List of `MedicationStatementDosage` items (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ Over what period was medication consumed?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Over what period was medication consumed?.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.informationSource = None
        """ The person who provided the information about the taking of this
        medication..
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.medication = None
        """ What medication was taken?.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who was/is taking medication.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reasonForUseCodeableConcept = None
        """ A reason for why the medication is being/was taken..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonForUseReference = None
        """ A reason for why the medication is being/was taken..
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ True if asserting medication was not given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in progress | completed | entered in error.
        Type `str`. """
        
        self.wasNotGiven = False
        """ True if medication is/was not being taken.
        Type `bool`. """
        
        super(MedicationStatement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationStatement, self).update_with_json(jsondict)
        if 'dosage' in jsondict:
            self.dosage = MedicationStatementDosage.with_json_and_owner(jsondict['dosage'], self)
        if 'effectiveDateTime' in jsondict:
            self.effectiveDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['effectiveDateTime'], self)
        if 'effectivePeriod' in jsondict:
            self.effectivePeriod = period.Period.with_json_and_owner(jsondict['effectivePeriod'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'informationSource' in jsondict:
            self.informationSource = fhirreference.FHIRReference.with_json_and_owner(jsondict['informationSource'], self)
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'reasonForUseCodeableConcept' in jsondict:
            self.reasonForUseCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonForUseCodeableConcept'], self)
        if 'reasonForUseReference' in jsondict:
            self.reasonForUseReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reasonForUseReference'], self)
        if 'reasonNotGiven' in jsondict:
            self.reasonNotGiven = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonNotGiven'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'wasNotGiven' in jsondict:
            self.wasNotGiven = jsondict['wasNotGiven']


class MedicationStatementDosage(fhirelement.FHIRElement):
    """ Details of how medication was taken.
    
    Indicates how the medication is/was used by the patient.
    """
    
    resource_name = "MedicationStatementDosage"
    
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
        
        self.schedule = None
        """ When/how often was medication taken?.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.site = None
        """ Where on body was medication administered?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Dosage Instructions.
        Type `str`. """
        
        super(MedicationStatementDosage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationStatementDosage, self).update_with_json(jsondict)
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
        if 'schedule' in jsondict:
            self.schedule = timing.Timing.with_json_and_owner(jsondict['schedule'], self)
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['site'], self)
        if 'text' in jsondict:
            self.text = jsondict['text']

