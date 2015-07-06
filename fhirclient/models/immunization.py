#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity


class Immunization(domainresource.DomainResource):
    """ Immunization event information.
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
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter administered as part of.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.expirationDate = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.explanation = None
        """ Administration / non-administration reasons.
        Type `ImmunizationExplanation` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where did vaccination occur?.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Vaccine lot number.
        Type `str`. """
        
        self.manufacturer = None
        """ Vaccine manufacturer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who was immunized?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who administered vaccine?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reaction = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.reported = None
        """ Is this a self-reported record?.
        Type `bool`. """
        
        self.requester = None
        """ Who ordered vaccination?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.route = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.vaccinationProtocol = None
        """ What protocol was followed.
        List of `ImmunizationVaccinationProtocol` items (represented as `dict` in JSON). """
        
        self.vaccineType = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.wasNotGiven = None
        """ Was immunization given?.
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
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("performer", "performer", fhirreference.FHIRReference, False),
            ("reaction", "reaction", ImmunizationReaction, True),
            ("reported", "reported", bool, False),
            ("requester", "requester", fhirreference.FHIRReference, False),
            ("route", "route", codeableconcept.CodeableConcept, False),
            ("site", "site", codeableconcept.CodeableConcept, False),
            ("vaccinationProtocol", "vaccinationProtocol", ImmunizationVaccinationProtocol, True),
            ("vaccineType", "vaccineType", codeableconcept.CodeableConcept, False),
            ("wasNotGiven", "wasNotGiven", bool, False),
        ])
        return js


class ImmunizationExplanation(fhirelement.FHIRElement):
    """ Administration / non-administration reasons.
    
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
        """ When did reaction start?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Additional information on reaction.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        self.reported = None
        """ Was reaction self-reported?.
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
        """ What dose number within series?.
        Type `int`. """
        
        self.doseStatus = None
        """ Does dose count towards immunity?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseStatusReason = None
        """ Why does does count/not count?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseTarget = None
        """ Disease immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.series = None
        """ Name of vaccine series.
        Type `str`. """
        
        self.seriesDoses = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        super(ImmunizationVaccinationProtocol, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImmunizationVaccinationProtocol, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False),
            ("description", "description", str, False),
            ("doseSequence", "doseSequence", int, False),
            ("doseStatus", "doseStatus", codeableconcept.CodeableConcept, False),
            ("doseStatusReason", "doseStatusReason", codeableconcept.CodeableConcept, False),
            ("doseTarget", "doseTarget", codeableconcept.CodeableConcept, False),
            ("series", "series", str, False),
            ("seriesDoses", "seriesDoses", int, False),
        ])
        return js

