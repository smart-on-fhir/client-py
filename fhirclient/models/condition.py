#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Condition) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Condition(domainresource.DomainResource):
    """ Detailed information about conditions, problems or diagnoses.
    
    Use to record detailed information about conditions, problems or diagnoses
    recognized by a clinician. There are many uses including: recording a
    diagnosis during an encounter; populating a problem list or a summary
    statement, such as a discharge summary.
    """
    
    resource_name = "Condition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abatementBoolean = None
        """ If/when in resolution/remission.
        Type `bool`. """
        
        self.abatementDateTime = None
        """ If/when in resolution/remission.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.abatementPeriod = None
        """ If/when in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.abatementQuantity = None
        """ If/when in resolution/remission.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
        self.abatementRange = None
        """ If/when in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """
        
        self.abatementString = None
        """ If/when in resolution/remission.
        Type `str`. """
        
        self.asserter = None
        """ Person who asserts this condition.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Anatomical location, if relevant.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.category = None
        """ complaint | symptom | finding | diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.clinicalStatus = None
        """ active | relapse | remission | resolved.
        Type `str`. """
        
        self.code = None
        """ Identification of the condition, problem or diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.dateRecorded = None
        """ When first entered.
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
        
        self.notes = None
        """ Additional information about the Condition.
        Type `str`. """
        
        self.onsetDateTime = None
        """ Estimated or actual date,  date-time, or age.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onsetPeriod = None
        """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetQuantity = None
        """ Estimated or actual date,  date-time, or age.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
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
        
        self.verificationStatus = None
        """ provisional | differential | confirmed | refuted | entered-in-error
        | unknown.
        Type `str`. """
        
        super(Condition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementBoolean", "abatementBoolean", bool, False, "abatement", False),
            ("abatementDateTime", "abatementDateTime", fhirdate.FHIRDate, False, "abatement", False),
            ("abatementPeriod", "abatementPeriod", period.Period, False, "abatement", False),
            ("abatementQuantity", "abatementQuantity", quantity.Quantity, False, "abatement", False),
            ("abatementRange", "abatementRange", range.Range, False, "abatement", False),
            ("abatementString", "abatementString", str, False, "abatement", False),
            ("asserter", "asserter", fhirreference.FHIRReference, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("clinicalStatus", "clinicalStatus", str, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("dateRecorded", "dateRecorded", fhirdate.FHIRDate, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("evidence", "evidence", ConditionEvidence, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("notes", "notes", str, False, None, False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetQuantity", "onsetQuantity", quantity.Quantity, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("severity", "severity", codeableconcept.CodeableConcept, False, None, False),
            ("stage", "stage", ConditionStage, False, None, False),
            ("verificationStatus", "verificationStatus", str, False, None, True),
        ])
        return js


from . import backboneelement

class ConditionEvidence(backboneelement.BackboneElement):
    """ Supporting evidence.
    
    Supporting Evidence / manifestations that are the basis on which this
    condition is suspected or confirmed.
    """
    
    resource_name = "ConditionEvidence"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Manifestation/symptom.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Supporting information found elsewhere.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(ConditionEvidence, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class ConditionStage(backboneelement.BackboneElement):
    """ Stage/grade, usually assessed formally.
    
    Clinical stage or grade of a condition. May include formal severity
    assessments.
    """
    
    resource_name = "ConditionStage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assessment = None
        """ Formal record of assessment.
        List of `FHIRReference` items referencing `ClinicalImpression, DiagnosticReport, Observation` (represented as `dict` in JSON). """
        
        self.summary = None
        """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionStage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", fhirreference.FHIRReference, True, None, False),
            ("summary", "summary", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
