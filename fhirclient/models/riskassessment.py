#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/RiskAssessment) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period
import range


class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.
    
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    
    resource_name = "RiskAssessment"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.basis = None
        """ Information used in assessment.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.condition = None
        """ Condition assessed.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.date = None
        """ When was assessment made?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Unique identifier for the assessment.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.method = None
        """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.mitigation = None
        """ How to reduce risk.
        Type `str`. """
        
        self.performer = None
        """ Who did assessment?.
        Type `FHIRReference` referencing `Practitioner, Device` (represented as `dict` in JSON). """
        
        self.prediction = None
        """ Outcome predicted.
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who/what does assessment apply to?.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        super(RiskAssessment, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(RiskAssessment, self).update_with_json(jsondict)
        if 'basis' in jsondict:
            self.basis = fhirreference.FHIRReference.with_json_and_owner(jsondict['basis'], self)
        if 'condition' in jsondict:
            self.condition = fhirreference.FHIRReference.with_json_and_owner(jsondict['condition'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'method' in jsondict:
            self.method = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['method'], self)
        if 'mitigation' in jsondict:
            self.mitigation = jsondict['mitigation']
        if 'performer' in jsondict:
            self.performer = fhirreference.FHIRReference.with_json_and_owner(jsondict['performer'], self)
        if 'prediction' in jsondict:
            self.prediction = RiskAssessmentPrediction.with_json_and_owner(jsondict['prediction'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)


class RiskAssessmentPrediction(fhirelement.FHIRElement):
    """ Outcome predicted.
    
    Describes the expected outcome for the subject.
    """
    
    resource_name = "RiskAssessmentPrediction"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.outcome = None
        """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.probabilityCodeableConcept = None
        """ Likelihood of specified outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.probabilityDecimal = None
        """ Likelihood of specified outcome.
        Type `float`. """
        
        self.probabilityRange = None
        """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rationale = None
        """ Explanation of prediction.
        Type `str`. """
        
        self.relativeRisk = None
        """ Relative likelihood.
        Type `float`. """
        
        self.whenPeriod = None
        """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """
        
        self.whenRange = None
        """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """
        
        super(RiskAssessmentPrediction, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(RiskAssessmentPrediction, self).update_with_json(jsondict)
        if 'outcome' in jsondict:
            self.outcome = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['outcome'], self)
        if 'probabilityCodeableConcept' in jsondict:
            self.probabilityCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['probabilityCodeableConcept'], self)
        if 'probabilityDecimal' in jsondict:
            self.probabilityDecimal = jsondict['probabilityDecimal']
        if 'probabilityRange' in jsondict:
            self.probabilityRange = range.Range.with_json_and_owner(jsondict['probabilityRange'], self)
        if 'rationale' in jsondict:
            self.rationale = jsondict['rationale']
        if 'relativeRisk' in jsondict:
            self.relativeRisk = jsondict['relativeRisk']
        if 'whenPeriod' in jsondict:
            self.whenPeriod = period.Period.with_json_and_owner(jsondict['whenPeriod'], self)
        if 'whenRange' in jsondict:
            self.whenRange = range.Range.with_json_and_owner(jsondict['whenRange'], self)

