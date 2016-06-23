#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

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
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(ClinicalImpression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpression, self).elementProperties()
        js.extend([
            ("action", "action", fhirreference.FHIRReference, True, None, False),
            ("assessor", "assessor", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("finding", "finding", ClinicalImpressionFinding, True, None, False),
            ("investigations", "investigations", ClinicalImpressionInvestigations, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("plan", "plan", fhirreference.FHIRReference, True, None, False),
            ("previous", "previous", fhirreference.FHIRReference, False, None, False),
            ("problem", "problem", fhirreference.FHIRReference, True, None, False),
            ("prognosis", "prognosis", str, False, None, False),
            ("protocol", "protocol", str, False, None, False),
            ("resolved", "resolved", codeableconcept.CodeableConcept, True, None, False),
            ("ruledOut", "ruledOut", ClinicalImpressionRuledOut, True, None, False),
            ("status", "status", str, False, None, True),
            ("summary", "summary", str, False, None, False),
            ("triggerCodeableConcept", "triggerCodeableConcept", codeableconcept.CodeableConcept, False, "trigger", False),
            ("triggerReference", "triggerReference", fhirreference.FHIRReference, False, "trigger", False),
        ])
        return js


from . import backboneelement

class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """ Possible or likely findings and diagnoses.
    
    Specific findings or diagnoses that was considered likely or relevant to
    ongoing treatment.
    """
    
    resource_name = "ClinicalImpressionFinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cause = None
        """ Which investigations support finding.
        Type `str`. """
        
        self.item = None
        """ Specific text or code for finding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionFinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionFinding, self).elementProperties()
        js.extend([
            ("cause", "cause", str, False, None, False),
            ("item", "item", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ClinicalImpressionInvestigations(backboneelement.BackboneElement):
    """ One or more sets of investigations (signs, symptions, etc.).
    
    One or more sets of investigations (signs, symptions, etc.). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """
    
    resource_name = "ClinicalImpressionInvestigations"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ A name/code for the set.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        """ Record of a specific investigation.
        List of `FHIRReference` items referencing `Observation, QuestionnaireResponse, FamilyMemberHistory, DiagnosticReport` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionInvestigations, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionInvestigations, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("item", "item", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ClinicalImpressionRuledOut(backboneelement.BackboneElement):
    """ Diagnosis considered not possible.
    """
    
    resource_name = "ClinicalImpressionRuledOut"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.item = None
        """ Specific text of code for diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Grounds for elimination.
        Type `str`. """
        
        super(ClinicalImpressionRuledOut, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionRuledOut, self).elementProperties()
        js.extend([
            ("item", "item", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
