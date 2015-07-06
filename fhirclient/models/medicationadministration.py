#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/MedicationAdministration) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import ratio


class MedicationAdministration(domainresource.DomainResource):
    """ Administration of medication to a patient.
    
    Describes the event of a patient consuming or otherwise being administered
    a medication.  This may be as simple as swallowing a tablet or it may be a
    long running infusion.Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """
    
    resource_name = "MedicationAdministration"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.device = None
        """ Device used to administer.
        List of `FHIRReference` items referencing `Device` (represented as `dict` in JSON). """
        
        self.dosage = None
        """ Details of how medication was taken.
        Type `MedicationAdministrationDosage` (represented as `dict` in JSON). """
        
        self.effectiveTimeDateTime = None
        """ Start and end time of administration.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectiveTimePeriod = None
        """ Start and end time of administration.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medication = None
        """ What was administered?.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.note = None
        """ Information about the administration.
        Type `str`. """
        
        self.patient = None
        """ Who received medication?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.practitioner = None
        """ Who administered substance?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.prescription = None
        """ Order administration performed against.
        Type `FHIRReference` referencing `MedicationPrescription` (represented as `dict` in JSON). """
        
        self.reasonGiven = None
        """ Reason administration performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ Reason administration not performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
        
        self.wasNotGiven = None
        """ True if medication not administered.
        Type `bool`. """
        
        super(MedicationAdministration, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationAdministration, self).elementProperties()
        js.extend([
            ("device", "device", fhirreference.FHIRReference, True),
            ("dosage", "dosage", MedicationAdministrationDosage, False),
            ("effectiveTimeDateTime", "effectiveTimeDateTime", fhirdate.FHIRDate, False),
            ("effectiveTimePeriod", "effectiveTimePeriod", period.Period, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("medication", "medication", fhirreference.FHIRReference, False),
            ("note", "note", str, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("practitioner", "practitioner", fhirreference.FHIRReference, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False),
            ("reasonGiven", "reasonGiven", codeableconcept.CodeableConcept, True),
            ("reasonNotGiven", "reasonNotGiven", codeableconcept.CodeableConcept, True),
            ("status", "status", str, False),
            ("wasNotGiven", "wasNotGiven", bool, False),
        ])
        return js


class MedicationAdministrationDosage(fhirelement.FHIRElement):
    """ Details of how medication was taken.
    
    Indicates how the medication is/was used by the patient.
    """
    
    resource_name = "MedicationAdministrationDosage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
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
        
        self.text = None
        """ Dosage Instructions.
        Type `str`. """
        
        super(MedicationAdministrationDosage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationAdministrationDosage, self).elementProperties()
        js.extend([
            ("method", "method", codeableconcept.CodeableConcept, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("rate", "rate", ratio.Ratio, False),
            ("route", "route", codeableconcept.CodeableConcept, False),
            ("site", "site", codeableconcept.CodeableConcept, False),
            ("text", "text", str, False),
        ])
        return js

