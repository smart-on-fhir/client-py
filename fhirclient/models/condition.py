#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (condition.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import age
import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class Condition(fhirresource.FHIRResource):
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
        
        self.asserter = None
        """ Person who asserts this condition.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. complaint | symptom | finding | diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.certainty = None
        """ Degree of confidence.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
        
        self.severity = None
        """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.stage = None
        """ Stage/grade, usually assessed formally.
        Type `ConditionStage` (represented as `dict` in JSON). """
        
        self.status = None
        """ provisional | working | confirmed | refuted.
        Type `str`. """
        
        self.subject = None
        """ Who has the condition?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(Condition, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Condition, self).update_with_json(jsondict)
        if 'abatementAge' in jsondict:
            self.abatementAge = age.Age.with_json_and_owner(jsondict['abatementAge'], self)
        if 'abatementBoolean' in jsondict:
            self.abatementBoolean = jsondict['abatementBoolean']
        if 'abatementDate' in jsondict:
            self.abatementDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['abatementDate'], self)
        if 'asserter' in jsondict:
            self.asserter = fhirreference.FHIRReference.with_json_and_owner(jsondict['asserter'], self)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'certainty' in jsondict:
            self.certainty = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['certainty'], self)
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
        if 'severity' in jsondict:
            self.severity = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['severity'], self)
        if 'stage' in jsondict:
            self.stage = ConditionStage.with_json_and_owner(jsondict['stage'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)


class ConditionDueTo(fhirelement.FHIRElement):
    """ Causes for this Condition.
    
    Further conditions, problems, diagnoses, procedures or events or the
    substance that caused/triggered this Condition.
    """
    
    resource_name = "ConditionDueTo"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.codeableConcept = None
        """ Relationship target by means of a predefined code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Relationship target resource.
        Type `FHIRReference` referencing `Condition, Procedure, MedicationAdministration, Immunization, MedicationStatement` (represented as `dict` in JSON). """
        
        super(ConditionDueTo, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionDueTo, self).update_with_json(jsondict)
        if 'codeableConcept' in jsondict:
            self.codeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['codeableConcept'], self)
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
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
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
        
        self.code = None
        """ Location - may include laterality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Precise location details.
        Type `str`. """
        
        super(ConditionLocation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionLocation, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'detail' in jsondict:
            self.detail = jsondict['detail']


class ConditionOccurredFollowing(fhirelement.FHIRElement):
    """ Precedent for this Condition.
    
    Further conditions, problems, diagnoses, procedures or events or the
    substance that preceded this Condition.
    """
    
    resource_name = "ConditionOccurredFollowing"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.codeableConcept = None
        """ Relationship target by means of a predefined code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Relationship target resource.
        Type `FHIRReference` referencing `Condition, Procedure, MedicationAdministration, Immunization, MedicationStatement` (represented as `dict` in JSON). """
        
        super(ConditionOccurredFollowing, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionOccurredFollowing, self).update_with_json(jsondict)
        if 'codeableConcept' in jsondict:
            self.codeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['codeableConcept'], self)
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
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
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

