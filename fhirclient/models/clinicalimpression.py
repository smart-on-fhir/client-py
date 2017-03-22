#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression) on 2017-03-22.
#  2017, SMART Health IT.


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
    
    resource_type = "ClinicalImpression"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None
        """ Action taken as part of assessment procedure.
        List of `FHIRReference` items referencing `ReferralRequest, ProcedureRequest, Procedure, MedicationRequest, Appointment` (represented as `dict` in JSON). """
        
        self.assessor = None
        """ The clinician performing the assessment.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.code = None
        """ Kind of assessment performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or Episode created from.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the assessment was documented.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Why/how the assessment was performed.
        Type `str`. """
        
        self.effectiveDateTime = None
        """ Time of assessment.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Time of assessment.
        Type `Period` (represented as `dict` in JSON). """
        
        self.finding = None
        """ Possible or likely findings and diagnoses.
        List of `ClinicalImpressionFinding` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.investigation = None
        """ One or more sets of investigations (signs, symptions, etc.).
        List of `ClinicalImpressionInvestigation` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the ClinicalImpression.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.previous = None
        """ Reference to last assessment.
        Type `FHIRReference` referencing `ClinicalImpression` (represented as `dict` in JSON). """
        
        self.problem = None
        """ Relevant impressions of patient state.
        List of `FHIRReference` items referencing `Condition, AllergyIntolerance` (represented as `dict` in JSON). """
        
        self.prognosisCodeableConcept = None
        """ Estimate of likely outcome.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.prognosisReference = None
        """ RiskAssessment expressing likely outcome.
        List of `FHIRReference` items referencing `RiskAssessment` (represented as `dict` in JSON). """
        
        self.protocol = None
        """ Clinical Protocol followed.
        List of `str` items. """
        
        self.status = None
        """ draft | completed | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Patient or group assessed.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.summary = None
        """ Summary of the assessment.
        Type `str`. """
        
        super(ClinicalImpression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpression, self).elementProperties()
        js.extend([
            ("action", "action", fhirreference.FHIRReference, True, None, False),
            ("assessor", "assessor", fhirreference.FHIRReference, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("finding", "finding", ClinicalImpressionFinding, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("investigation", "investigation", ClinicalImpressionInvestigation, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("previous", "previous", fhirreference.FHIRReference, False, None, False),
            ("problem", "problem", fhirreference.FHIRReference, True, None, False),
            ("prognosisCodeableConcept", "prognosisCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("prognosisReference", "prognosisReference", fhirreference.FHIRReference, True, None, False),
            ("protocol", "protocol", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("summary", "summary", str, False, None, False),
        ])
        return js


from . import backboneelement

class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """ Possible or likely findings and diagnoses.
    
    Specific findings or diagnoses that was considered likely or relevant to
    ongoing treatment.
    """
    
    resource_type = "ClinicalImpressionFinding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basis = None
        """ Which investigations support finding.
        Type `str`. """
        
        self.itemCodeableConcept = None
        """ What was found.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ What was found.
        Type `FHIRReference` referencing `Condition, Observation` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionFinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionFinding, self).elementProperties()
        js.extend([
            ("basis", "basis", str, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
        ])
        return js


class ClinicalImpressionInvestigation(backboneelement.BackboneElement):
    """ One or more sets of investigations (signs, symptions, etc.).
    
    One or more sets of investigations (signs, symptions, etc.). The actual
    grouping of investigations vary greatly depending on the type and context
    of the assessment. These investigations may include data generated during
    the assessment process, or data previously generated and recorded that is
    pertinent to the outcomes.
    """
    
    resource_type = "ClinicalImpressionInvestigation"
    
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
        List of `FHIRReference` items referencing `Observation, QuestionnaireResponse, FamilyMemberHistory, DiagnosticReport, RiskAssessment, ImagingStudy` (represented as `dict` in JSON). """
        
        super(ClinicalImpressionInvestigation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionInvestigation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("item", "item", fhirreference.FHIRReference, True, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
