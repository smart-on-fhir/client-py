#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (clinicalassessment.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource


class ClinicalAssessment(fhirresource.FHIRResource):
    """ A clinical assessment performed when planning treatments and management
    strategies for a patient.
    
    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow.
    """
    
    resource_name = "ClinicalAssessment"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ Actions taken during assessment.
        List of `FHIRReference` items referencing `ReferralRequest, ProcedureRequest, Procedure, MedicationPrescription, DiagnosticOrder, NutritionOrder, Supply, Appointment` (represented as `dict` in JSON). """
        
        self.assessor = None
        """ The clinicial performing the assessment.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.careplan = None
        """ A specific careplan that prompted this assessment.
        Type `FHIRReference` referencing `CarePlan` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the assessment occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Why/how the assessment was performed.
        Type `str`. """
        
        self.diagnosis = None
        """ Possible or likely diagnosis.
        List of `ClinicalAssessmentDiagnosis` items (represented as `dict` in JSON). """
        
        self.investigations = None
        """ One or more sets of investigations (signs, symptions, etc).
        List of `ClinicalAssessmentInvestigations` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient being asssesed.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.plan = None
        """ Plan of action after assessment.
        Type `FHIRReference` referencing `CarePlan` (represented as `dict` in JSON). """
        
        self.previous = None
        """ Reference to last assessment.
        Type `FHIRReference` referencing `ClinicalAssessment` (represented as `dict` in JSON). """
        
        self.problem = None
        """ General assessment of patient state.
        List of `FHIRReference` items referencing `Condition, AllergyIntolerance` (represented as `dict` in JSON). """
        
        self.prognosis = None
        """ Estimate of likely outcome.
        Type `str`. """
        
        self.protocol = None
        """ Clinical Protocol followed.
        Type `str`. """
        
        self.referral = None
        """ A specific referral that lead to this assessment.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.resolved = None
        """ Diagnosies/conditions resolved since previous assessment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.ruledOut = None
        """ Diagnosis considered not possible.
        List of `ClinicalAssessmentRuledOut` items (represented as `dict` in JSON). """
        
        self.summary = None
        """ Summary of the assessment.
        Type `str`. """
        
        super(ClinicalAssessment, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalAssessment, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = fhirreference.FHIRReference.with_json_and_owner(jsondict['action'], self)
        if 'assessor' in jsondict:
            self.assessor = fhirreference.FHIRReference.with_json_and_owner(jsondict['assessor'], self)
        if 'careplan' in jsondict:
            self.careplan = fhirreference.FHIRReference.with_json_and_owner(jsondict['careplan'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'diagnosis' in jsondict:
            self.diagnosis = ClinicalAssessmentDiagnosis.with_json_and_owner(jsondict['diagnosis'], self)
        if 'investigations' in jsondict:
            self.investigations = ClinicalAssessmentInvestigations.with_json_and_owner(jsondict['investigations'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'plan' in jsondict:
            self.plan = fhirreference.FHIRReference.with_json_and_owner(jsondict['plan'], self)
        if 'previous' in jsondict:
            self.previous = fhirreference.FHIRReference.with_json_and_owner(jsondict['previous'], self)
        if 'problem' in jsondict:
            self.problem = fhirreference.FHIRReference.with_json_and_owner(jsondict['problem'], self)
        if 'prognosis' in jsondict:
            self.prognosis = jsondict['prognosis']
        if 'protocol' in jsondict:
            self.protocol = jsondict['protocol']
        if 'referral' in jsondict:
            self.referral = fhirreference.FHIRReference.with_json_and_owner(jsondict['referral'], self)
        if 'resolved' in jsondict:
            self.resolved = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['resolved'], self)
        if 'ruledOut' in jsondict:
            self.ruledOut = ClinicalAssessmentRuledOut.with_json_and_owner(jsondict['ruledOut'], self)
        if 'summary' in jsondict:
            self.summary = jsondict['summary']


class ClinicalAssessmentDiagnosis(fhirelement.FHIRElement):
    """ Possible or likely diagnosis.
    
    An specific diagnosis that was considered likely or relevant to ongoing
    treatment.
    """
    
    resource_name = "ClinicalAssessmentDiagnosis"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.cause = None
        """ Which investigations support diagnosis.
        Type `str`. """
        
        self.item = None
        """ Specific text or code for diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClinicalAssessmentDiagnosis, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalAssessmentDiagnosis, self).update_with_json(jsondict)
        if 'cause' in jsondict:
            self.cause = jsondict['cause']
        if 'item' in jsondict:
            self.item = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['item'], self)


class ClinicalAssessmentInvestigations(fhirelement.FHIRElement):
    """ One or more sets of investigations (signs, symptions, etc).
    
    One or more sets of investigations (signs, symptions, etc). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """
    
    resource_name = "ClinicalAssessmentInvestigations"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ A name/code for the set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        """ Record of a specific investigation.
        List of `FHIRReference` items referencing `Observation, QuestionnaireAnswers, FamilyHistory, DiagnosticReport` (represented as `dict` in JSON). """
        
        super(ClinicalAssessmentInvestigations, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalAssessmentInvestigations, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self)


class ClinicalAssessmentRuledOut(fhirelement.FHIRElement):
    """ Diagnosis considered not possible.
    """
    
    resource_name = "ClinicalAssessmentRuledOut"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.item = None
        """ Specific text of code for diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Grounds for elimination.
        Type `str`. """
        
        super(ClinicalAssessmentRuledOut, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalAssessmentRuledOut, self).update_with_json(jsondict)
        if 'item' in jsondict:
            self.item = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['item'], self)
        if 'reason' in jsondict:
            self.reason = jsondict['reason']

