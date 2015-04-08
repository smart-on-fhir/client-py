#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference


class ClinicalImpression(domainresource.DomainResource):
    """ A clinical assessment performed when planning treatments and management
    strategies for a patient.
    
    A record of a clinical assessment performed to determine what problem(s)
    may affect the patient and before planning the treatments or management
    strategies that are best to manage a patient's condition. Assessments are
    often 1:1 with a clinical consultation / encounter,  but this varies
    greatly depending on the clinical workflow. This resource is called
    "ClinicalImpression" rather than "ClinicalAssessment" to avoid confusion
    with the recording of assessment tools such as Apgar score.
    """
    
    resource_name = "ClinicalImpression"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ Actions taken during assessment.
        List of `FHIRReference` items referencing `ReferralRequest, ProcedureRequest, Procedure, MedicationPrescription, DiagnosticOrder, NutritionOrder, Supply, Appointment` (represented as `dict` in JSON). """
        
        self.assessor = None
        """ The clinician performing the assessment.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the assessment occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Why/how the assessment was performed.
        Type `str`. """
        
        self.finding = None
        """ Possible or likely findings and diagnoses.
        List of `ClinicalImpressionFinding` items (represented as `dict` in JSON). """
        
        self.investigations = None
        """ One or more sets of investigations (signs, symptions, etc).
        List of `ClinicalImpressionInvestigations` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient being asssesed.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.plan = None
        """ Plan of action after assessment.
        List of `FHIRReference` items referencing `CarePlan, Appointment, CommunicationRequest, DeviceUseRequest, DiagnosticOrder, MedicationPrescription, NutritionOrder, Order, ProcedureRequest, ProcessRequest, ReferralRequest, Supply, VisionPrescription` (represented as `dict` in JSON). """
        
        self.previous = None
        """ Reference to last assessment.
        Type `FHIRReference` referencing `ClinicalImpression` (represented as `dict` in JSON). """
        
        self.problem = None
        """ General assessment of patient state.
        List of `FHIRReference` items referencing `Condition, AllergyIntolerance` (represented as `dict` in JSON). """
        
        self.prognosis = None
        """ Estimate of likely outcome.
        Type `str`. """
        
        self.protocol = None
        """ Clinical Protocol followed.
        Type `str`. """
        
        self.resolved = None
        """ Diagnosies/conditions resolved since previous assessment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.ruledOut = None
        """ Diagnosis considered not possible.
        List of `ClinicalImpressionRuledOut` items (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | completed | entered-in-error.
        Type `str`. """
        
        self.summary = None
        """ Summary of the assessment.
        Type `str`. """
        
        self.triggerCodeableConcept = None
        """ Request or event that necessitated this assessment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.triggerReference = None
        """ Request or event that necessitated this assessment.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(ClinicalImpression, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalImpression, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = fhirreference.FHIRReference.with_json_and_owner(jsondict['action'], self)
        if 'assessor' in jsondict:
            self.assessor = fhirreference.FHIRReference.with_json_and_owner(jsondict['assessor'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'finding' in jsondict:
            self.finding = ClinicalImpressionFinding.with_json_and_owner(jsondict['finding'], self)
        if 'investigations' in jsondict:
            self.investigations = ClinicalImpressionInvestigations.with_json_and_owner(jsondict['investigations'], self)
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
        if 'resolved' in jsondict:
            self.resolved = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['resolved'], self)
        if 'ruledOut' in jsondict:
            self.ruledOut = ClinicalImpressionRuledOut.with_json_and_owner(jsondict['ruledOut'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'summary' in jsondict:
            self.summary = jsondict['summary']
        if 'triggerCodeableConcept' in jsondict:
            self.triggerCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['triggerCodeableConcept'], self)
        if 'triggerReference' in jsondict:
            self.triggerReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['triggerReference'], self)


class ClinicalImpressionFinding(fhirelement.FHIRElement):
    """ Possible or likely findings and diagnoses.
    
    Specific findings or diagnoses that was considered likely or relevant to
    ongoing treatment.
    """
    
    resource_name = "ClinicalImpressionFinding"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.cause = None
        """ Which investigations support finding.
        Type `str`. """
        
        self.item = None
        """ Specific text or code for finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionFinding, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalImpressionFinding, self).update_with_json(jsondict)
        if 'cause' in jsondict:
            self.cause = jsondict['cause']
        if 'item' in jsondict:
            self.item = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['item'], self)


class ClinicalImpressionInvestigations(fhirelement.FHIRElement):
    """ One or more sets of investigations (signs, symptions, etc).
    
    One or more sets of investigations (signs, symptions, etc). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """
    
    resource_name = "ClinicalImpressionInvestigations"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ A name/code for the set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        """ Record of a specific investigation.
        List of `FHIRReference` items referencing `Observation, QuestionnaireAnswers, FamilyMemberHistory, DiagnosticReport` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionInvestigations, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalImpressionInvestigations, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self)


class ClinicalImpressionRuledOut(fhirelement.FHIRElement):
    """ Diagnosis considered not possible.
    """
    
    resource_name = "ClinicalImpressionRuledOut"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.item = None
        """ Specific text of code for diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Grounds for elimination.
        Type `str`. """
        
        super(ClinicalImpressionRuledOut, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClinicalImpressionRuledOut, self).update_with_json(jsondict)
        if 'item' in jsondict:
            self.item = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['item'], self)
        if 'reason' in jsondict:
            self.reason = jsondict['reason']

