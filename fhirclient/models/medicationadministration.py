#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medicationadministration.profile.json) on 2014-11-11.
#  2014, SMART Platforms.


import codeableconcept
import device
import encounter
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import medication
import medicationprescription
import narrative
import patient
import period
import practitioner
import quantity
import ratio


class MedicationAdministration(fhirresource.FHIRResource):
    """ Administration of medication to a patient.
    
    Scope and Usage This resource covers the administration of all medications
    with the exception of vaccines. It will principally be used within
    inpatient settings to record the capture of medication administrations
    including self-administrations of oral medications, injections, intra-
    venous adjustments, etc. It can also be used in out-patient settings to
    record allergy shots and other non-immunization administrations. In some
    cases it might be used for home-health reporting, such as recording self-
    administered or even device-administered insulin.
    """
    
    resource_name = "MedicationAdministration"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Medicine administration instructions to the patient/carer.
        List of `MedicationAdministrationDosage` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medication = None
        """ What was administered?.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who received medication?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.practitioner = None
        """ Who administered substance?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Order administration performed against.
        Type `FHIRReference` referencing `MedicationPrescription` (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in progress | on hold | completed | entered in error | stopped.
        Type `str`. """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.wasNotGiven = False
        """ True if medication not administered.
        Type `bool`. """
        
        self.whenGiven = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationAdministration, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationAdministration, self).update_with_json(jsondict)
        if 'device' in jsondict:
            self.device = fhirreference.FHIRReference.with_json_and_owner(jsondict['device'], self, device.Device)
        if 'dosage' in jsondict:
            self.dosage = MedicationAdministrationDosage.with_json_and_owner(jsondict['dosage'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, encounter.Encounter)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'medication' in jsondict:
            self.medication = fhirreference.FHIRReference.with_json_and_owner(jsondict['medication'], self, medication.Medication)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self, patient.Patient)
        if 'practitioner' in jsondict:
            self.practitioner = fhirreference.FHIRReference.with_json_and_owner(jsondict['practitioner'], self, practitioner.Practitioner)
        if 'prescription' in jsondict:
            self.prescription = fhirreference.FHIRReference.with_json_and_owner(jsondict['prescription'], self, medicationprescription.MedicationPrescription)
        if 'reasonNotGiven' in jsondict:
            self.reasonNotGiven = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonNotGiven'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json_and_owner(jsondict['text'], self)
        if 'wasNotGiven' in jsondict:
            self.wasNotGiven = jsondict['wasNotGiven']
        if 'whenGiven' in jsondict:
            self.whenGiven = period.Period.with_json_and_owner(jsondict['whenGiven'], self)


class MedicationAdministrationDosage(fhirelement.FHIRElement):
    """ Medicine administration instructions to the patient/carer.
    
    Provides details of how much of the medication was administered.
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
        """ Total dose that was consumed per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ How drug was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount administered in one dose.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rate = None
        """ Dose quantity per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ Path of substance into body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site administered to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ When dose(s) were given.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ When dose(s) were given.
        Type `Period` (represented as `dict` in JSON). """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationAdministrationDosage, self).update_with_json(jsondict)
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
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['site'], self)
        if 'timingDateTime' in jsondict:
            self.timingDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['timingDateTime'], self)
        if 'timingPeriod' in jsondict:
            self.timingPeriod = period.Period.with_json_and_owner(jsondict['timingPeriod'], self)

