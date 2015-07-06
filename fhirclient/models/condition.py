#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Condition) on 2015-07-06.
#  2015, SMART Health IT.


from . import age
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import range


class Condition(domainresource.DomainResource):
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
        
        self.abatementBoolean = None
        """ If/when in resolution/remission.
        Type `bool`. """
        
        self.abatementDate = None
        """ If/when in resolution/remission.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.abatementPeriod = None
        """ If/when in resolution/remission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.abatementRange = None
        """ If/when in resolution/remission.
        Type `Range` (represented as `dict` in JSON). """
        
        self.abatementString = None
        """ If/when in resolution/remission.
        Type `str`. """
        
        self.asserter = None
        """ Person who asserts this condition.
        Type `FHIRReference` referencing `Practitioner, Patient` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. complaint | symptom | finding | diagnosis.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.clinicalStatus = None
        """ provisional | working | confirmed | refuted | entered-in-error |
        unknown.
        Type `str`. """
        
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
        
        self.onsetPeriod = None
        """ Estimated or actual date,  date-time, or age.
        Type `Period` (represented as `dict` in JSON). """
        
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
        
        super(Condition, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Condition, self).elementProperties()
        js.extend([
            ("abatementAge", "abatementAge", age.Age, False),
            ("abatementBoolean", "abatementBoolean", bool, False),
            ("abatementDate", "abatementDate", fhirdate.FHIRDate, False),
            ("abatementPeriod", "abatementPeriod", period.Period, False),
            ("abatementRange", "abatementRange", range.Range, False),
            ("abatementString", "abatementString", str, False),
            ("asserter", "asserter", fhirreference.FHIRReference, False),
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("clinicalStatus", "clinicalStatus", str, False),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("dateAsserted", "dateAsserted", fhirdate.FHIRDate, False),
            ("dueTo", "dueTo", ConditionDueTo, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("evidence", "evidence", ConditionEvidence, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("location", "location", ConditionLocation, True),
            ("notes", "notes", str, False),
            ("occurredFollowing", "occurredFollowing", ConditionOccurredFollowing, True),
            ("onsetAge", "onsetAge", age.Age, False),
            ("onsetDateTime", "onsetDateTime", fhirdate.FHIRDate, False),
            ("onsetPeriod", "onsetPeriod", period.Period, False),
            ("onsetRange", "onsetRange", range.Range, False),
            ("onsetString", "onsetString", str, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("severity", "severity", codeableconcept.CodeableConcept, False),
            ("stage", "stage", ConditionStage, False),
        ])
        return js


class ConditionDueTo(fhirelement.FHIRElement):
    """ Causes for this Condition.
    
    Further conditions, problems, diagnoses, procedures or events or the
    substance that caused/triggered this Condition.
    """
    
    resource_name = "ConditionDueTo"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Relationship target by means of a predefined code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Relationship target resource.
        Type `FHIRReference` referencing `Condition, Procedure, MedicationAdministration, Immunization, MedicationStatement` (represented as `dict` in JSON). """
        
        super(ConditionDueTo, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConditionDueTo, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("target", "target", fhirreference.FHIRReference, False),
        ])
        return js


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
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(ConditionEvidence, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConditionEvidence, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("detail", "detail", fhirreference.FHIRReference, True),
        ])
        return js


class ConditionLocation(fhirelement.FHIRElement):
    """ Anatomical location, if relevant.
    
    The anatomical location where this condition manifests itself.
    """
    
    resource_name = "ConditionLocation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.siteCodeableConcept = None
        """ Location - may include laterality.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.siteReference = None
        """ Location - may include laterality.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        super(ConditionLocation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConditionLocation, self).elementProperties()
        js.extend([
            ("siteCodeableConcept", "siteCodeableConcept", codeableconcept.CodeableConcept, False),
            ("siteReference", "siteReference", fhirreference.FHIRReference, False),
        ])
        return js


class ConditionOccurredFollowing(fhirelement.FHIRElement):
    """ Precedent for this Condition.
    
    Further conditions, problems, diagnoses, procedures or events or the
    substance that preceded this Condition.
    """
    
    resource_name = "ConditionOccurredFollowing"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Relationship target by means of a predefined code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.target = None
        """ Relationship target resource.
        Type `FHIRReference` referencing `Condition, Procedure, MedicationAdministration, Immunization, MedicationStatement` (represented as `dict` in JSON). """
        
        super(ConditionOccurredFollowing, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConditionOccurredFollowing, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("target", "target", fhirreference.FHIRReference, False),
        ])
        return js


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
        List of `FHIRReference` items referencing `ClinicalImpression, DiagnosticReport, Observation` (represented as `dict` in JSON). """
        
        self.summary = None
        """ Simple summary (disease specific).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ConditionStage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ConditionStage, self).elementProperties()
        js.extend([
            ("assessment", "assessment", fhirreference.FHIRReference, True),
            ("summary", "summary", codeableconcept.CodeableConcept, False),
        ])
        return js

