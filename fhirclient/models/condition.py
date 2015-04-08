#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Condition) on 2015-04-08.
#  2015, SMART Health IT.


import age
import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period
import range


class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.
    
    Use to record detailed information about conditions, problems or diagnoses
    recognized by a clinician. There are many uses including: recording a
    Diagnosis during an Encounter; populating a problem List or a Summary
    Statement, such as a Discharge Summary.
    """
    
    resource_name = "Condition"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.abatementAge = None
        """ If/when in resolution/remission.
        Type `Age` (represented as `dict` in JSON). """
        
        self.abatementBoolean = False
        """ If/when in resolution/remission.
        Type `bool`. """
        
        self.abatementDate = None
        """ If/when in resolution/remission.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.abatementPeriod = None
        """ If/when in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.abatementRange = None
        """ If/when in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """
        
        self.abatementString = None
        """ If/when in resolution/remission.
        Type `str`. """
        
        self.asserter = None
        """ Person who asserts this condition.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. complaint | symptom | finding | diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.clinicalStatus = None
        """ provisional | working | confirmed | refuted | entered-in-error |
        unknown.
        Type `str`. """
        
        self.code = None
        """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dateAsserted = None
        """ When first detected/suspected/entered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dueTo = None
        """ Causes for this Condition.
        List of `ConditionDueTo` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter when condition first asserted.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.evidence = None
        """ Supporting evidence.
        List of `ConditionEvidence` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this condition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Anatomical location, if relevant.
        List of `ConditionLocation` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Additional information about the Condition.
        Type `str`. """
        
        self.occurredFollowing = None
        """ Precedent for this Condition.
        List of `ConditionOccurredFollowing` items (represented as `dict` in JSON). """
        
        self.onsetAge = None
        """ Estimated or actual date,  date-time, or age.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetDateTime = None
        """ Estimated or actual date,  date-time, or age.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onsetPeriod = None
        """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetRange = None
        """ Estimated or actual date,  date-time, or age.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None
        """ Estimated or actual date,  date-time, or age.
        Type `str`. """
        
        self.patient = None
        """ Who has the condition?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.severity = None
        """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stage = None
        """ Stage/grade, usually assessed formally.
        Type `ConditionStage` (represented as `dict` in JSON). """
        
        super(Condition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Condition, self).update_with_json(jsondict)
        if 'abatementAge' in jsondict:
            self.abatementAge = age.Age.with_json_and_owner(jsondict['abatementAge'], self)
        if 'abatementBoolean' in jsondict:
            self.abatementBoolean = jsondict['abatementBoolean']
        if 'abatementDate' in jsondict:
            self.abatementDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['abatementDate'], self)
        if 'abatementPeriod' in jsondict:
            self.abatementPeriod = period.Period.with_json_and_owner(jsondict['abatementPeriod'], self)
        if 'abatementRange' in jsondict:
            self.abatementRange = range.Range.with_json_and_owner(jsondict['abatementRange'], self)
        if 'abatementString' in jsondict:
            self.abatementString = jsondict['abatementString']
        if 'asserter' in jsondict:
            self.asserter = fhirreference.FHIRReference.with_json_and_owner(jsondict['asserter'], self)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'clinicalStatus' in jsondict:
            self.clinicalStatus = jsondict['clinicalStatus']
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'dateAsserted' in jsondict:
            self.dateAsserted = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateAsserted'], self)
        if 'dueTo' in jsondict:
            self.dueTo = ConditionDueTo.with_json_and_owner(jsondict['dueTo'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'evidence' in jsondict:
            self.evidence = ConditionEvidence.with_json_and_owner(jsondict['evidence'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'location' in jsondict:
            self.location = ConditionLocation.with_json_and_owner(jsondict['location'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'occurredFollowing' in jsondict:
            self.occurredFollowing = ConditionOccurredFollowing.with_json_and_owner(jsondict['occurredFollowing'], self)
        if 'onsetAge' in jsondict:
            self.onsetAge = age.Age.with_json_and_owner(jsondict['onsetAge'], self)
        if 'onsetDateTime' in jsondict:
            self.onsetDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['onsetDateTime'], self)
        if 'onsetPeriod' in jsondict:
            self.onsetPeriod = period.Period.with_json_and_owner(jsondict['onsetPeriod'], self)
        if 'onsetRange' in jsondict:
            self.onsetRange = range.Range.with_json_and_owner(jsondict['onsetRange'], self)
        if 'onsetString' in jsondict:
            self.onsetString = jsondict['onsetString']
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'severity' in jsondict:
            self.severity = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['severity'], self)
        if 'stage' in jsondict:
            self.stage = ConditionStage.with_json_and_owner(jsondict['stage'], self)


class ConditionDueTo(fhirelement.FHIRElement):
    """ Causes for this Condition.
    
    Further conditions, problems, diagnoses, procedures or events or the
    substance that caused/triggered this Condition.
    """
    
    resource_name = "ConditionDueTo"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Relationship target by means of a predefined code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Relationship target resource.
        Type `FHIRReference` referencing `Condition, Procedure, MedicationAdministration, Immunization, MedicationStatement` (represented as `dict` in JSON). """
        
        super(ConditionDueTo, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionDueTo, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)


class ConditionEvidence(fhirelement.FHIRElement):
    """ Supporting evidence.
    
    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """
    
    resource_name = "ConditionEvidence"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Manifestation/symptom.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Supporting information found elsewhere.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(ConditionEvidence, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionEvidence, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'detail' in jsondict:
            self.detail = fhirreference.FHIRReference.with_json_and_owner(jsondict['detail'], self)


class ConditionLocation(fhirelement.FHIRElement):
    """ Anatomical location, if relevant.
    
    The anatomical location where this condition manifests itself.
    """
    
    resource_name = "ConditionLocation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.siteCodeableConcept = None
        """ Location - may include laterality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Location - may include laterality.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        super(ConditionLocation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionLocation, self).update_with_json(jsondict)
        if 'siteCodeableConcept' in jsondict:
            self.siteCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['siteCodeableConcept'], self)
        if 'siteReference' in jsondict:
            self.siteReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['siteReference'], self)


class ConditionOccurredFollowing(fhirelement.FHIRElement):
    """ Precedent for this Condition.
    
    Further conditions, problems, diagnoses, procedures or events or the
    substance that preceded this Condition.
    """
    
    resource_name = "ConditionOccurredFollowing"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Relationship target by means of a predefined code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Relationship target resource.
        Type `FHIRReference` referencing `Condition, Procedure, MedicationAdministration, Immunization, MedicationStatement` (represented as `dict` in JSON). """
        
        super(ConditionOccurredFollowing, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionOccurredFollowing, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)


class ConditionStage(fhirelement.FHIRElement):
    """ Stage/grade, usually assessed formally.
    
    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    
    resource_name = "ConditionStage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.assessment = None
        """ Formal record of assessment.
        List of `FHIRReference` items referencing `ClinicalImpression, DiagnosticReport, Observation` (represented as `dict` in JSON). """
        
        self.summary = None
        """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionStage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionStage, self).update_with_json(jsondict)
        if 'assessment' in jsondict:
            self.assessment = fhirreference.FHIRReference.with_json_and_owner(jsondict['assessment'], self)
        if 'summary' in jsondict:
            self.summary = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['summary'], self)

