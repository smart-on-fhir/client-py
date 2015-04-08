#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Immunization) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import quantity


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
        
        self.reported = False
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
        
        self.wasNotGiven = False
        """ Was immunization given?.
        Type `bool`. """
        
        super(Immunization, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Immunization, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'doseQuantity' in jsondict:
            self.doseQuantity = quantity.Quantity.with_json_and_owner(jsondict['doseQuantity'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'expirationDate' in jsondict:
            self.expirationDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['expirationDate'], self)
        if 'explanation' in jsondict:
            self.explanation = ImmunizationExplanation.with_json_and_owner(jsondict['explanation'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'lotNumber' in jsondict:
            self.lotNumber = jsondict['lotNumber']
        if 'manufacturer' in jsondict:
            self.manufacturer = fhirreference.FHIRReference.with_json_and_owner(jsondict['manufacturer'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'performer' in jsondict:
            self.performer = fhirreference.FHIRReference.with_json_and_owner(jsondict['performer'], self)
        if 'reaction' in jsondict:
            self.reaction = ImmunizationReaction.with_json_and_owner(jsondict['reaction'], self)
        if 'reported' in jsondict:
            self.reported = jsondict['reported']
        if 'requester' in jsondict:
            self.requester = fhirreference.FHIRReference.with_json_and_owner(jsondict['requester'], self)
        if 'route' in jsondict:
            self.route = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['route'], self)
        if 'site' in jsondict:
            self.site = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['site'], self)
        if 'vaccinationProtocol' in jsondict:
            self.vaccinationProtocol = ImmunizationVaccinationProtocol.with_json_and_owner(jsondict['vaccinationProtocol'], self)
        if 'vaccineType' in jsondict:
            self.vaccineType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['vaccineType'], self)
        if 'wasNotGiven' in jsondict:
            self.wasNotGiven = jsondict['wasNotGiven']


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
    
    def update_with_json(self, jsondict):
        super(ImmunizationExplanation, self).update_with_json(jsondict)
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'reasonNotGiven' in jsondict:
            self.reasonNotGiven = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonNotGiven'], self)


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
        
        self.reported = False
        """ Was reaction self-reported?.
        Type `bool`. """
        
        super(ImmunizationReaction, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationReaction, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'detail' in jsondict:
            self.detail = fhirreference.FHIRReference.with_json_and_owner(jsondict['detail'], self)
        if 'reported' in jsondict:
            self.reported = jsondict['reported']


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
    
    def update_with_json(self, jsondict):
        super(ImmunizationVaccinationProtocol, self).update_with_json(jsondict)
        if 'authority' in jsondict:
            self.authority = fhirreference.FHIRReference.with_json_and_owner(jsondict['authority'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'doseSequence' in jsondict:
            self.doseSequence = jsondict['doseSequence']
        if 'doseStatus' in jsondict:
            self.doseStatus = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['doseStatus'], self)
        if 'doseStatusReason' in jsondict:
            self.doseStatusReason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['doseStatusReason'], self)
        if 'doseTarget' in jsondict:
            self.doseTarget = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['doseTarget'], self)
        if 'series' in jsondict:
            self.series = jsondict['series']
        if 'seriesDoses' in jsondict:
            self.seriesDoses = jsondict['seriesDoses']

