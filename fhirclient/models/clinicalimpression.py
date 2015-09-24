#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference


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
        List of `FHIRReference` items referencing `ReferralRequest, ProcedureRequest, Procedure, MedicationOrder, DiagnosticOrder, NutritionOrder, SupplyRequest, Appointment` (represented as `dict` in JSON). """
        
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
        """ One or more sets of investigations (signs, symptions, etc.).
        List of `ClinicalImpressionInvestigations` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ The patient being assessed.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.plan = None
        """ Plan of action after assessment.
        List of `FHIRReference` items referencing `CarePlan, Appointment, CommunicationRequest, DeviceUseRequest, DiagnosticOrder, MedicationOrder, NutritionOrder, Order, ProcedureRequest, ProcessRequest, ReferralRequest, SupplyRequest, VisionPrescription` (represented as `dict` in JSON). """
        
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
        """ Diagnoses/conditions resolved since previous assessment.
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
    
    def elementProperties(self):
        js = super(ClinicalImpression, self).elementProperties()
        js.extend([
            ("action", "action", fhirreference.FHIRReference, True),
            ("assessor", "assessor", fhirreference.FHIRReference, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("finding", "finding", ClinicalImpressionFinding, True),
            ("investigations", "investigations", ClinicalImpressionInvestigations, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("plan", "plan", fhirreference.FHIRReference, True),
            ("previous", "previous", fhirreference.FHIRReference, False),
            ("problem", "problem", fhirreference.FHIRReference, True),
            ("prognosis", "prognosis", str, False),
            ("protocol", "protocol", str, False),
            ("resolved", "resolved", codeableconcept.CodeableConcept, True),
            ("ruledOut", "ruledOut", ClinicalImpressionRuledOut, True),
            ("status", "status", str, False),
            ("summary", "summary", str, False),
            ("triggerCodeableConcept", "triggerCodeableConcept", codeableconcept.CodeableConcept, False),
            ("triggerReference", "triggerReference", fhirreference.FHIRReference, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(ClinicalImpressionFinding, self).elementProperties()
        js.extend([
            ("cause", "cause", str, False),
            ("item", "item", codeableconcept.CodeableConcept, False),
        ])
        return js


class ClinicalImpressionInvestigations(fhirelement.FHIRElement):
    """ One or more sets of investigations (signs, symptions, etc.).
    
    One or more sets of investigations (signs, symptions, etc.). The actual
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
        List of `FHIRReference` items referencing `Observation, QuestionnaireResponse, FamilyMemberHistory, DiagnosticReport` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionInvestigations, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionInvestigations, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("item", "item", fhirreference.FHIRReference, True),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(ClinicalImpressionRuledOut, self).elementProperties()
        js.extend([
            ("item", "item", codeableconcept.CodeableConcept, False),
            ("reason", "reason", str, False),
        ])
        return js

