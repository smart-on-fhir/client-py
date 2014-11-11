#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (condition.profile.json) on 2014-11-11.
#  2014, SMART Platforms.


import age
import codeableconcept
import encounter
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner


class Condition(fhirresource.FHIRResource):
    """ Detailed information about conditions, problems or diagnoses.
    
    Scope and Usage This resource is used to record detailed information about
    a specific aspect of or issue with the health state of a patient. It is
    intended for use for issues that have been identified as relevant for
    tracking and reporting purposes or where there's a need to capture a
    concrete diagnosis or the gathering of data such as signs and symptoms.
    There are situations where the same information might appear as both an
    observation as well as a condition. For example, the appearance of a rash
    or an instance of a fever are signs and symptoms that would typically be
    captured using the Observation resource. However, a pattern of ongoing
    fevers or a persistent or severe rash requiring treatment might be captured
    as a condition. The Condition resource specifically excludes
    AdverseReactions and AllergyIntolerances as those are handled with their
    own resources.
    
    The Condition resource may be used to record positive aspects of the health
    state of a patient (e.g. pregnancy) as well as the major use, which is for
    problems/concerns (e.g. hypertension).
    
    Conditions are frequently referenced by other resources as "reasons" for an
    action (Prescription, Procedure, DiagnosticOrder, etc.)
    
    The conditions represented in this resources are sometimes described as
    "Problems", and kept as part of a problem list.
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
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
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
        
        self.onsetAge = None
        """ Estimated or actual date, or age.
        Type `Age` (represented as `dict` in JSON). """
        
        self.onsetDate = None
        """ Estimated or actual date, or age.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.relatedItem = None
        """ Causes or precedents for this Condition.
        List of `ConditionRelatedItem` items (represented as `dict` in JSON). """
        
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
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
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
            self.asserter = fhirreference.FHIRReference.with_json_and_owner(jsondict['asserter'], self, practitioner.Practitioner)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'certainty' in jsondict:
            self.certainty = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['certainty'], self)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'dateAsserted' in jsondict:
            self.dateAsserted = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateAsserted'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, encounter.Encounter)
        if 'evidence' in jsondict:
            self.evidence = ConditionEvidence.with_json_and_owner(jsondict['evidence'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'location' in jsondict:
            self.location = ConditionLocation.with_json_and_owner(jsondict['location'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'onsetAge' in jsondict:
            self.onsetAge = age.Age.with_json_and_owner(jsondict['onsetAge'], self)
        if 'onsetDate' in jsondict:
            self.onsetDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['onsetDate'], self)
        if 'relatedItem' in jsondict:
            self.relatedItem = ConditionRelatedItem.with_json_and_owner(jsondict['relatedItem'], self)
        if 'severity' in jsondict:
            self.severity = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['severity'], self)
        if 'stage' in jsondict:
            self.stage = ConditionStage.with_json_and_owner(jsondict['stage'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json_and_owner(jsondict['text'], self)


class ConditionStage(fhirelement.FHIRElement):
    """ Stage/grade, usually assessed formally.
    
    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    
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
            self.assessment = fhirreference.FHIRReference.with_json_and_owner(jsondict['assessment'], self, fhirresource.FHIRResource)
        if 'summary' in jsondict:
            self.summary = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['summary'], self)


class ConditionEvidence(fhirelement.FHIRElement):
    """ Supporting evidence.
    
    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """
    
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
            self.detail = fhirreference.FHIRReference.with_json_and_owner(jsondict['detail'], self, fhirresource.FHIRResource)


class ConditionLocation(fhirelement.FHIRElement):
    """ Anatomical location, if relevant.
    
    The anatomical location where this condition manifests itself.
    """
    
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


class ConditionRelatedItem(fhirelement.FHIRElement):
    """ Causes or precedents for this Condition.
    
    Further conditions, problems, diagnoses, procedures or events that are
    related in some way to this condition, or the substance that
    caused/triggered this Condition.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Relationship target by means of a predefined code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Relationship target resource.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.type = None
        """ due-to | following.
        Type `str`. """
        
        super(ConditionRelatedItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ConditionRelatedItem, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self, Condition)
        if 'type' in jsondict:
            self.type = jsondict['type']

