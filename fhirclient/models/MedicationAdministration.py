#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medicationadministration.profile.json) on 2014-10-17.
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
import Device
import Encounter
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Medication
import MedicationPrescription
import Narrative
import Patient
import Period
import Practitioner
import Quantity
import Ratio


class MedicationAdministration(FHIRResource.FHIRResource):
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
            self.device = FHIRReference.FHIRReference.with_json_and_owner(jsondict['device'], self, Device.Device)
        if 'dosage' in jsondict:
            self.dosage = MedicationAdministrationDosage.with_json(jsondict['dosage'])
        if 'encounter' in jsondict:
            self.encounter = FHIRReference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, Encounter.Encounter)
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'medication' in jsondict:
            self.medication = FHIRReference.FHIRReference.with_json_and_owner(jsondict['medication'], self, Medication.Medication)
        if 'patient' in jsondict:
            self.patient = FHIRReference.FHIRReference.with_json_and_owner(jsondict['patient'], self, Patient.Patient)
        if 'practitioner' in jsondict:
            self.practitioner = FHIRReference.FHIRReference.with_json_and_owner(jsondict['practitioner'], self, Practitioner.Practitioner)
        if 'prescription' in jsondict:
            self.prescription = FHIRReference.FHIRReference.with_json_and_owner(jsondict['prescription'], self, MedicationPrescription.MedicationPrescription)
        if 'reasonNotGiven' in jsondict:
            self.reasonNotGiven = CodeableConcept.CodeableConcept.with_json(jsondict['reasonNotGiven'])
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'wasNotGiven' in jsondict:
            self.wasNotGiven = jsondict['wasNotGiven']
        if 'whenGiven' in jsondict:
            self.whenGiven = Period.Period.with_json(jsondict['whenGiven'])


class MedicationAdministrationDosage(FHIRElement.FHIRElement):
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

