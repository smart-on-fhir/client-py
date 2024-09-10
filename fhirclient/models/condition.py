# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Condition).
# 2024, SMART Health IT.


from . import domainresource

class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.
    
    A clinical condition, problem, diagnosis, or other event, situation, issue,
    or clinical concept that has risen to a level of concern.
    """
    
    resource_type = "Condition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abatementAge = None
        """ When in resolution/remission.
        Type `Age` (represented as `dict` in JSON). """
        self._abatementAge = None
        """ Primitive extension for abatementAge. Type `FHIRPrimitiveExtension` """
        
        self.abatementDateTime = None
        """ When in resolution/remission.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._abatementDateTime = None
        """ Primitive extension for abatementDateTime. Type `FHIRPrimitiveExtension` """
        
        self.abatementPeriod = None
        """ When in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """
        self._abatementPeriod = None
        """ Primitive extension for abatementPeriod. Type `FHIRPrimitiveExtension` """
        
        self.abatementRange = None
        """ When in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """
        self._abatementRange = None
        """ Primitive extension for abatementRange. Type `FHIRPrimitiveExtension` """
        
        self.abatementString = None
        """ When in resolution/remission.
        Type `str`. """
        self._abatementString = None
        """ Primitive extension for abatementString. Type `FHIRPrimitiveExtension` """
        
        self.asserter = None
        """ Person who asserts this condition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._asserter = None
        """ Primitive extension for asserter. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ problem-list-item | encounter-diagnosis.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.clinicalStatus = None
        """ active | recurrence | relapse | inactive | remission | resolved.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._clinicalStatus = None
        """ Primitive extension for clinicalStatus. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.evidence = None
        """ Supporting evidence.
        List of `ConditionEvidence` items (represented as `dict` in JSON). """
        self._evidence = None
        """ Primitive extension for evidence. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Ids for this condition.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Additional information about the Condition.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.onsetAge = None
        """ Estimated or actual date,  date-time, or age.
        Type `Age` (represented as `dict` in JSON). """
        self._onsetAge = None
        """ Primitive extension for onsetAge. Type `FHIRPrimitiveExtension` """
        
        self.onsetDateTime = None
        """ Estimated or actual date,  date-time, or age.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._onsetDateTime = None
        """ Primitive extension for onsetDateTime. Type `FHIRPrimitiveExtension` """
        
        self.onsetPeriod = None
        """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """
        self._onsetPeriod = None
        """ Primitive extension for onsetPeriod. Type `FHIRPrimitiveExtension` """
        
        self.onsetRange = None
        """ Estimated or actual date,  date-time, or age.
        Type `Range` (represented as `dict` in JSON). """
        self._onsetRange = None
        """ Primitive extension for onsetRange. Type `FHIRPrimitiveExtension` """
        
        self.onsetString = None
        """ Estimated or actual date,  date-time, or age.
        Type `str`. """
        self._onsetString = None
        """ Primitive extension for onsetString. Type `FHIRPrimitiveExtension` """
        
        self.recordedDate = None
        """ Date record was first recorded.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._recordedDate = None
        """ Primitive extension for recordedDate. Type `FHIRPrimitiveExtension` """
        
        self.recorder = None
        """ Who recorded the condition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recorder = None
        """ Primitive extension for recorder. Type `FHIRPrimitiveExtension` """
        
        self.severity = None
        """ Subjective severity of condition.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._severity = None
        """ Primitive extension for severity. Type `FHIRPrimitiveExtension` """
        
        self.stage = None
        """ Stage/grade, usually assessed formally.
        List of `ConditionStage` items (represented as `dict` in JSON). """
        self._stage = None
        """ Primitive extension for stage. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who has the condition?.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.verificationStatus = None
        """ unconfirmed | provisional | differential | confirmed | refuted |
        entered-in-error.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._verificationStatus = None
        """ Primitive extension for verificationStatus. Type `FHIRPrimitiveExtension` """
        
        super(Condition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementAge", "abatementAge", age.Age, False, "abatement", False),
            ("_abatementAge", "_abatementAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("abatementDateTime", "abatementDateTime", fhirdatetime.FHIRDateTime, False, "abatement", False),
            ("_abatementDateTime", "_abatementDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("abatementPeriod", "abatementPeriod", period.Period, False, "abatement", False),
            ("_abatementPeriod", "_abatementPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("abatementRange", "abatementRange", range.Range, False, "abatement", False),
            ("_abatementRange", "_abatementRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("abatementString", "abatementString", str, False, "abatement", False),
            ("_abatementString", "_abatementString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("_asserter", "_asserter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("clinicalStatus", "clinicalStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_clinicalStatus", "_clinicalStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("evidence", "evidence", ConditionEvidence, True, None, False),
            ("_evidence", "_evidence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetAge", "onsetAge", age.Age, False, "onset", False),
            ("_onsetAge", "_onsetAge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetDateTime", "onsetDateTime", fhirdatetime.FHIRDateTime, False, "onset", False),
            ("_onsetDateTime", "_onsetDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("_onsetPeriod", "_onsetPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("_onsetRange", "_onsetRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("_onsetString", "_onsetString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recordedDate", "recordedDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_recordedDate", "_recordedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recorder", "recorder", fhirreference.FHIRReference, False, None, False),
            ("_recorder", "_recorder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("_severity", "_severity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("stage", "stage", ConditionStage, True, None, False),
            ("_stage", "_stage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("verificationStatus", "verificationStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_verificationStatus", "_verificationStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.
    
    Supporting evidence / manifestations that are the basis of the Condition's
    verification status, such as evidence that confirmed or refuted the
    condition.
    """
    
    resource_type = "ConditionEvidence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Manifestation/symptom.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Supporting information found elsewhere.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        super(ConditionEvidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.
    
    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    
    resource_type = "ConditionStage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment = None
        """ Formal record of assessment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._assessment = None
        """ Primitive extension for assessment. Type `FHIRPrimitiveExtension` """
        
        self.summary = None
        """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._summary = None
        """ Primitive extension for summary. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of staging.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ConditionStage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", fhirreference.FHIRReference, True, None, False),
            ("_assessment", "_assessment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("summary", "summary", codeableconcept.CodeableConcept, False, None, False),
            ("_summary", "_summary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import age
from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import period
from . import range