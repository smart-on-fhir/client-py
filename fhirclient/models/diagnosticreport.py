#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class DiagnosticReport(domainresource.DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretations, and formatted representation of diagnostic reports.
    """
    
    resource_type = "DiagnosticReport"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ What was requested.
        List of `FHIRReference` items referencing `CarePlan, ImmunizationRecommendation, MedicationRequest, NutritionOrder, ProcedureRequest, ReferralRequest` (represented as `dict` in JSON). """
        
        self.category = None
        """ Service category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.codedDiagnosis = None
        """ Codes for the conclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.conclusion = None
        """ Clinical Interpretation of test results.
        Type `str`. """
        
        self.context = None
        """ Health care event when test ordered.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.effectiveDateTime = None
        """ Clinically relevant time/time-period for report.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.effectivePeriod = None
        """ Clinically relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier for report.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.image = None
        """ Key images associated with this report.
        List of `DiagnosticReportImage` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items referencing `ImagingStudy, ImagingManifest` (represented as `dict` in JSON). """
        
        self.issued = None
        """ DateTime this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.performer = None
        """ Participants in producing the report.
        List of `DiagnosticReportPerformer` items (represented as `dict` in JSON). """
        
        self.presentedForm = None
        """ Entire report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.result = None
        """ Observations - simple, or complex nested groups.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimens this report is based on.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | partial | preliminary | final +.
        Type `str`. """
        
        self.subject = None
        """ The subject of the report - usually, but not always, the patient.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        super(DiagnosticReport, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("codedDiagnosis", "codedDiagnosis", codeableconcept.CodeableConcept, True, None, False),
            ("conclusion", "conclusion", str, False, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("effectiveDateTime", "effectiveDateTime", fhirdate.FHIRDate, False, "effective", False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, "effective", False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("image", "image", DiagnosticReportImage, True, None, False),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, True, None, False),
            ("issued", "issued", fhirdate.FHIRDate, False, None, False),
            ("performer", "performer", DiagnosticReportPerformer, True, None, False),
            ("presentedForm", "presentedForm", attachment.Attachment, True, None, False),
            ("result", "result", fhirreference.FHIRReference, True, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class DiagnosticReportImage(backboneelement.BackboneElement):
    """ Key images associated with this report.
    
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    
    resource_type = "DiagnosticReportImage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Comment about the image (e.g. explanation).
        Type `str`. """
        
        self.link = None
        """ Reference to the image source.
        Type `FHIRReference` referencing `Media` (represented as `dict` in JSON). """
        
        super(DiagnosticReportImage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReportImage, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("link", "link", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class DiagnosticReportPerformer(backboneelement.BackboneElement):
    """ Participants in producing the report.
    
    Indicates who or what participated in producing the report.
    """
    
    resource_type = "DiagnosticReportPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Practitioner or Organization  participant.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of performer.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DiagnosticReportPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DiagnosticReportPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
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
