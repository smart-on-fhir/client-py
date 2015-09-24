#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2015-09-24.
#  2015, SMART Health IT.


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity


class Immunization(domainresource.DomainResource):
    """ Immunization event information.
    
    Describes the event of a patient being administered a vaccination or a
    record of a vaccination as reported by a patient, a clinician or another
    party and may include vaccine reaction information and what vaccination
    protocol was followed.
    """
    
    resource_name = "Immunization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ Vaccination administration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.doseQuantity = None
        """ Amount of vaccine administered.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.expirationDate = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.explanation = None
        """ Administration/non-administration reasons.
        Type `ImmunizationExplanation` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where vaccination occurred.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Vaccine lot number.
        Type `str`. """
        
        self.manufacturer = None
        """ Vaccine manufacturer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.note = None
        """ Vaccination notes.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who was immunized.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who administered vaccine.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reaction = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.reported = None
        """ Indicates a self-reported record.
        Type `bool`. """
        
        self.requester = None
        """ Who ordered vaccination.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.route = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | on-hold | completed | entered-in-error | stopped.
        Type `str`. """
        
        self.vaccinationProtocol = None
        """ What protocol was followed.
        List of `ImmunizationVaccinationProtocol` items (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.wasNotGiven = None
        """ Flag for whether immunization was given.
        Type `bool`. """
        
        super(Immunization, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Immunization, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False),
            ("doseQuantity", "doseQuantity", quantity.Quantity, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False),
            ("explanation", "explanation", ImmunizationExplanation, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("location", "location", fhirreference.FHIRReference, False),
            ("lotNumber", "lotNumber", str, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False),
            ("note", "note", annotation.Annotation, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("performer", "performer", fhirreference.FHIRReference, False),
            ("reaction", "reaction", ImmunizationReaction, True),
            ("reported", "reported", bool, False),
            ("requester", "requester", fhirreference.FHIRReference, False),
            ("route", "route", codeableconcept.CodeableConcept, False),
            ("site", "site", codeableconcept.CodeableConcept, False),
            ("status", "status", str, False),
            ("vaccinationProtocol", "vaccinationProtocol", ImmunizationVaccinationProtocol, True),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False),
            ("wasNotGiven", "wasNotGiven", bool, False),
        ])
        return js


class ImmunizationExplanation(fhirelement.FHIRElement):
    """ Administration/non-administration reasons.
    
    Reasons why a vaccine was or was not administered.
    """
    
    resource_name = "ImmunizationExplanation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.reason = None
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonNotGiven = None
        """ Why immunization did not occur.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationExplanation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImmunizationExplanation, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, True),
            ("reasonNotGiven", "reasonNotGiven", codeableconcept.CodeableConcept, True),
        ])
        return js


class ImmunizationReaction(fhirelement.FHIRElement):
    """ Details of a reaction that follows immunization.
    
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    
    resource_name = "ImmunizationReaction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ When reaction started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Additional information on reaction.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        self.reported = None
        """ Indicates self-reported reaction.
        Type `bool`. """
        
        super(ImmunizationReaction, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImmunizationReaction, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False),
            ("detail", "detail", fhirreference.FHIRReference, False),
            ("reported", "reported", bool, False),
        ])
        return js


class ImmunizationVaccinationProtocol(fhirelement.FHIRElement):
    """ What protocol was followed.
    
    Contains information about the protocol(s) under which the vaccine was
    administered.
    """
    
    resource_name = "ImmunizationVaccinationProtocol"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None
        """ Details of vaccine protocol.
        Type `str`. """
        
        self.doseSequence = None
        """ Dose number within series.
        Type `int`. """
        
        self.doseStatus = None
        """ Indicates if dose counts towards immunity.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseStatusReason = None
        """ Why dose does (not) count.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.series = None
        """ Name of vaccine series.
        Type `str`. """
        
        self.seriesDoses = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        self.targetDisease = None
        """ Disease immunized against.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationVaccinationProtocol, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImmunizationVaccinationProtocol, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False),
            ("description", "description", str, False),
            ("doseSequence", "doseSequence", int, False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, False),
            ("series", "series", str, False),
            ("seriesDoses", "seriesDoses", int, False),
            ("targetDisease", "targetDisease", codeableconcept.CodeableConcept, True),
        ])
        return js

