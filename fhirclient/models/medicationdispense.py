#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
from . import ratio
from . import timing


class MedicationDispense(domainresource.DomainResource):
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
        
        self.note = None
        """ Information about the dispense.
        Type `str`. """
        
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
        """ in-progress | on-hold | completed | entered-in-error | stopped.
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
    
    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, True),
            ("daysSupply", "daysSupply", quantity.Quantity, False),
            ("destination", "destination", fhirreference.FHIRReference, False),
            ("dispenser", "dispenser", fhirreference.FHIRReference, False),
            ("dosageInstruction", "dosageInstruction", MedicationDispenseDosageInstruction, True),
            ("identifier", "identifier", identifier.Identifier, False),
            ("medication", "medication", fhirreference.FHIRReference, False),
            ("note", "note", str, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
            ("whenHandedOver", "whenHandedOver", fhirdate.FHIRDate, False),
            ("whenPrepared", "whenPrepared", fhirdate.FHIRDate, False),
        ])
        return js


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
        
        self.asNeededBoolean = None
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
    
    def elementProperties(self):
        js = super(MedicationDispenseDosageInstruction, self).elementProperties()
        js.extend([
            ("additionalInstructions", "additionalInstructions", codeableconcept.CodeableConcept, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False),
            ("doseRange", "doseRange", range.Range, False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False),
            ("method", "method", codeableconcept.CodeableConcept, False),
            ("rate", "rate", ratio.Ratio, False),
            ("route", "route", codeableconcept.CodeableConcept, False),
            ("scheduleDateTime", "scheduleDateTime", fhirdate.FHIRDate, False),
            ("schedulePeriod", "schedulePeriod", period.Period, False),
            ("scheduleTiming", "scheduleTiming", timing.Timing, False),
            ("site", "site", codeableconcept.CodeableConcept, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, True),
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, True),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

