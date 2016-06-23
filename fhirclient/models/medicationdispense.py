#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.
    
    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """
    
    resource_name = "MedicationDispense"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorizingPrescription = None
        """ Medication order that authorizes the dispense.
        List of `FHIRReference` items referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.daysSupply = None
        """ Days Supply.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.destination = None
        """ Where the medication was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.dispenser = None
        """ Practitioner responsible for dispensing medication.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.dosageInstruction = None
        """ Medicine administration instructions to the patient/caregiver.
        List of `MedicationDispenseDosageInstruction` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.medicationCodeableConcept = None
        """ What medication was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.medicationReference = None
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
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
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
        """ When product was given out.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whenPrepared = None
        """ Dispense processing time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(MedicationDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, True, None, False),
            ("daysSupply", "daysSupply", quantity.Quantity, False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("dispenser", "dispenser", fhirreference.FHIRReference, False, None, False),
            ("dosageInstruction", "dosageInstruction", MedicationDispenseDosageInstruction, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, False, "medication", True),
            ("note", "note", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("whenHandedOver", "whenHandedOver", fhirdate.FHIRDate, False, None, False),
            ("whenPrepared", "whenPrepared", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationDispenseDosageInstruction(backboneelement.BackboneElement):
    """ Medicine administration instructions to the patient/caregiver.
    
    Indicates how the medication is to be used by the patient.
    """
    
    resource_name = "MedicationDispenseDosageInstruction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.doseRange = None
        """ Amount of medication per dose.
        Type `Range` (represented as `dict` in JSON). """
        
        self.maxDosePerPeriod = None
        """ Upper limit on medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.method = None
        """ Technique for administering medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.rateRange = None
        """ Amount of medication per unit of time.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Amount of medication per unit of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.route = None
        """ How drug should enter body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteCodeableConcept = None
        """ Body site to administer to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Body site to administer to.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        self.text = None
        """ Dosage Instructions.
        Type `str`. """
        
        self.timing = None
        """ When medication should be administered.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(MedicationDispenseDosageInstruction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispenseDosageInstruction, self).elementProperties()
        js.extend([
            ("additionalInstructions", "additionalInstructions", codeableconcept.CodeableConcept, False, None, False),
            ("asNeededBoolean", "asNeededBoolean", bool, False, "asNeeded", False),
            ("asNeededCodeableConcept", "asNeededCodeableConcept", codeableconcept.CodeableConcept, False, "asNeeded", False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False, "dose", False),
            ("doseRange", "doseRange", range.Range, False, "dose", False),
            ("maxDosePerPeriod", "maxDosePerPeriod", ratio.Ratio, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("rateRange", "rateRange", range.Range, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("route", "route", codeableconcept.CodeableConcept, False, None, False),
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False, "site", False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False, "site", False),
            ("text", "text", str, False, None, False),
            ("timing", "timing", timing.Timing, False, None, False),
        ])
        return js


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Deals with substitution of one medicine for another.
    
    Indicates whether or not substitution was made as part of the dispense.  In
    some cases substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.
    """
    
    resource_name = "MedicationDispenseSubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reason = None
        """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.responsibleParty = None
        """ Who is responsible for the substitution.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of substitution.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationDispenseSubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import range
from . import ratio
from . import timing
