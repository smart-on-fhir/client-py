# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ClinicalImpression).
# 2024, SMART Health IT.


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
        
        self.assessor = None
        """ The clinician performing the assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._assessor = None
        """ Primitive extension for assessor. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Kind of assessment performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ When the assessment was documented.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Why/how the assessment was performed.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.effectiveDateTime = None
        """ Time of assessment.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._effectiveDateTime = None
        """ Primitive extension for effectiveDateTime. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ Time of assessment.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.finding = None
        """ Possible or likely findings and diagnoses.
        List of `ClinicalImpressionFinding` items (represented as `dict` in JSON). """
        self._finding = None
        """ Primitive extension for finding. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.investigation = None
        """ One or more sets of investigations (signs, symptoms, etc.).
        List of `ClinicalImpressionInvestigation` items (represented as `dict` in JSON). """
        self._investigation = None
        """ Primitive extension for investigation. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments made about the ClinicalImpression.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.previous = None
        """ Reference to last assessment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._previous = None
        """ Primitive extension for previous. Type `FHIRPrimitiveExtension` """
        
        self.problem = None
        """ Relevant impressions of patient state.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._problem = None
        """ Primitive extension for problem. Type `FHIRPrimitiveExtension` """
        
        self.prognosisCodeableConcept = None
        """ Estimate of likely outcome.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._prognosisCodeableConcept = None
        """ Primitive extension for prognosisCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.prognosisReference = None
        """ RiskAssessment expressing likely outcome.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._prognosisReference = None
        """ Primitive extension for prognosisReference. Type `FHIRPrimitiveExtension` """
        
        self.protocol = None
        """ Clinical Protocol followed.
        List of `str` items. """
        self._protocol = None
        """ Primitive extension for protocol. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ in-progress | completed | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Patient or group assessed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.summary = None
        """ Summary of the assessment.
        Type `str`. """
        self._summary = None
        """ Primitive extension for summary. Type `FHIRPrimitiveExtension` """
        
        self.supportingInfo = None
        """ Information supporting the clinical impression.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInfo = None
        """ Primitive extension for supportingInfo. Type `FHIRPrimitiveExtension` """
        
        super(ClinicalImpression, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpression, self).elementProperties()
        js.extend([
            ("assessor", "assessor", fhirreference.FHIRReference, False, None, False),
            ("_assessor", "_assessor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdatetime.FHIRDateTime, False, "effective", False),
            ("_effectiveDateTime", "_effectiveDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("finding", "finding", ClinicalImpressionFinding, True, None, False),
            ("_finding", "_finding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("investigation", "investigation", ClinicalImpressionInvestigation, True, None, False),
            ("_investigation", "_investigation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("previous", "previous", fhirreference.FHIRReference, False, None, False),
            ("_previous", "_previous", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("problem", "problem", fhirreference.FHIRReference, True, None, False),
            ("_problem", "_problem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prognosisCodeableConcept", "prognosisCodeableConcept", codeableconcept.CodeableConcept, True, None, False),
            ("_prognosisCodeableConcept", "_prognosisCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prognosisReference", "prognosisReference", fhirreference.FHIRReference, True, None, False),
            ("_prognosisReference", "_prognosisReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("protocol", "protocol", str, True, None, False),
            ("_protocol", "_protocol", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("summary", "summary", str, False, None, False),
            ("_summary", "_summary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfo", "supportingInfo", fhirreference.FHIRReference, True, None, False),
            ("_supportingInfo", "_supportingInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ClinicalImpressionFinding(backboneelement.BackboneElement):
    """ Possible or likely findings and diagnoses.
    
    Specific findings or diagnoses that were considered likely or relevant to
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
        self._basis = None
        """ Primitive extension for basis. Type `FHIRPrimitiveExtension` """
        
        self.itemCodeableConcept = None
        """ What was found.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._itemCodeableConcept = None
        """ Primitive extension for itemCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.itemReference = None
        """ What was found.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._itemReference = None
        """ Primitive extension for itemReference. Type `FHIRPrimitiveExtension` """
        
        super(ClinicalImpressionFinding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionFinding, self).elementProperties()
        js.extend([
            ("basis", "basis", str, False, None, False),
            ("_basis", "_basis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, None, False),
            ("_itemCodeableConcept", "_itemCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, None, False),
            ("_itemReference", "_itemReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ClinicalImpressionInvestigation(backboneelement.BackboneElement):
    """ One or more sets of investigations (signs, symptoms, etc.).
    
    One or more sets of investigations (signs, symptoms, etc.). The actual
    grouping of investigations varies greatly depending on the type and context
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
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Record of a specific investigation.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        super(ClinicalImpressionInvestigation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClinicalImpressionInvestigation, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", fhirreference.FHIRReference, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period