#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.
    
    A patient's point-in-time immunization and recommendation (i.e. forecasting
    a patient's immunization eligibility according to a published schedule)
    with optional supporting justification.
    """
    
    resource_name = "ImmunizationRecommendation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who this profile is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.recommendation = None
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True),
        ])
        return js


class ImmunizationRecommendationRecommendation(fhirelement.FHIRElement):
    """ Vaccine administration recommendations.
    """
    
    resource_name = "ImmunizationRecommendationRecommendation"
    
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
        List of `FHIRReference` items referencing `Observation, AllergyIntolerance` (represented as `dict` in JSON). """
        
        self.vaccineCode = None
        """ Vaccine recommendation applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True),
            ("doseNumber", "doseNumber", int, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False),
            ("protocol", "protocol", ImmunizationRecommendationRecommendationProtocol, False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(fhirelement.FHIRElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    
    resource_name = "ImmunizationRecommendationRecommendationDateCriterion"
    
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
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("value", "value", fhirdate.FHIRDate, False),
        ])
        return js


class ImmunizationRecommendationRecommendationProtocol(fhirelement.FHIRElement):
    """ Protocol used by recommendation.
    
    Contains information about the protocol under which the vaccine was
    administered.
    """
    
    resource_name = "ImmunizationRecommendationRecommendationProtocol"
    
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
        """ Dose number within sequence.
        Type `int`. """
        
        self.series = None
        """ Name of vaccination series.
        Type `str`. """
        
        super(ImmunizationRecommendationRecommendationProtocol, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationProtocol, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False),
            ("description", "description", str, False),
            ("doseSequence", "doseSequence", int, False),
            ("series", "series", str, False),
        ])
        return js

