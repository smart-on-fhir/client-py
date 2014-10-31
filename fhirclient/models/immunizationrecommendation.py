#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (immunizationrecommendation.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import immunization
import narrative
import observation
import organization
import patient


class ImmunizationRecommendation(fhirresource.FHIRResource):
    """ Immunization profile.
    
    Scope and Usage The ImmunizationRecommendation resource is intended to
    cover communication of a specified patient's immunization recommendation
    and status across all healthcare disciplines in all care settings and all
    regions.
    
    Additionally, the ImmunizationRecommendation resource is expected to cover
    key concepts related to the querying of a patient's immunization
    recommendation and status. This resource - through consultation with the
    PHER work group - is believed to meet key use cases and information
    requirements as defined in the existing HL7 v3 POIZ domain and Immunization
    Domain Analysis Model.
    """
    
    resource_name = "ImmunizationRecommendation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.recommendation = None
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who this profile is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationRecommendation, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'recommendation' in jsondict:
            self.recommendation = ImmunizationRecommendationRecommendation.with_json(jsondict['recommendation'])
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class ImmunizationRecommendationRecommendation(fhirelement.FHIRElement):
    """ Vaccine administration recommendations.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ Date recommendation created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dateCriterion = None
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        
        self.doseNumber = None
        """ Recommended dose number.
        Type `int`. """
        
        self.forecastStatus = None
        """ Vaccine administration status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.protocol = None
        """ Protocol used by recommendation.
        Type `ImmunizationRecommendationRecommendationProtocol` (represented as `dict` in JSON). """
        
        self.supportingImmunization = None
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items referencing `Immunization` (represented as `dict` in JSON). """
        
        self.supportingPatientInformation = None
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """
        
        self.vaccineType = None
        """ Vaccine recommendation applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationRecommendationRecommendation, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'dateCriterion' in jsondict:
            self.dateCriterion = ImmunizationRecommendationRecommendationDateCriterion.with_json(jsondict['dateCriterion'])
        if 'doseNumber' in jsondict:
            self.doseNumber = jsondict['doseNumber']
        if 'forecastStatus' in jsondict:
            self.forecastStatus = codeableconcept.CodeableConcept.with_json(jsondict['forecastStatus'])
        if 'protocol' in jsondict:
            self.protocol = ImmunizationRecommendationRecommendationProtocol.with_json(jsondict['protocol'])
        if 'supportingImmunization' in jsondict:
            self.supportingImmunization = fhirreference.FHIRReference.with_json_and_owner(jsondict['supportingImmunization'], self, immunization.Immunization)
        if 'supportingPatientInformation' in jsondict:
            self.supportingPatientInformation = fhirreference.FHIRReference.with_json_and_owner(jsondict['supportingPatientInformation'], self, observation.Observation)
        if 'vaccineType' in jsondict:
            self.vaccineType = codeableconcept.CodeableConcept.with_json(jsondict['vaccineType'])


class ImmunizationRecommendationRecommendationDateCriterion(fhirelement.FHIRElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations - e.g. earliest date to administer, latest
    date to administer, etc.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ Recommended date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationRecommendationRecommendationDateCriterion, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'value' in jsondict:
            self.value = fhirdate.FHIRDate.with_json(jsondict['value'])


class ImmunizationRecommendationRecommendationProtocol(fhirelement.FHIRElement):
    """ Protocol used by recommendation.
    
    Contains information about the protocol under which the vaccine was
    administered.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None
        """ Protocol details.
        Type `str`. """
        
        self.doseSequence = None
        """ Number of dose within sequence.
        Type `int`. """
        
        self.series = None
        """ Name of vaccination series.
        Type `str`. """
        
        super(ImmunizationRecommendationRecommendationProtocol, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationRecommendationRecommendationProtocol, self).update_with_json(jsondict)
        if 'authority' in jsondict:
            self.authority = fhirreference.FHIRReference.with_json_and_owner(jsondict['authority'], self, organization.Organization)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'doseSequence' in jsondict:
            self.doseSequence = jsondict['doseSequence']
        if 'series' in jsondict:
            self.series = jsondict['series']

