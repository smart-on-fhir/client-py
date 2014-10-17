#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (diagnosticreport.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import Attachment
import CodeableConcept
import DiagnosticOrder
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import ImagingStudy
import Media
import Narrative
import Observation
import Patient
import Period
import Practitioner
import Specimen


class DiagnosticReport(FHIRResource.FHIRResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    
    Scope and Usage A diagnostic report is the set of information that is
    typically provided by a diagnostic service when investigations are
    complete. The information includes a mix of atomic results, text reports,
    images, and codes. The mix varies depending on the nature of the diagnostic
    procedure, and sometimes on the nature of the outcomes for a particular
    investigation.
    
    The Diagnostic Report Resource is suitable for the following kinds of
    Diagnostic Reports:
    
    * Laboratory (Clinical Chemistry, Hematology, Microbiology, etc.)
    * Pathology / Histopathology / related disciplines
    * Imaging Investigations (x-ray, CT, MRI etc.)
    * Other diagnostics - Cardiology, Gastroenterology etc.
    The Diagnostic Report resource is not intended to support cumulative result
    presentation (tabular presentation of past and present results in the
    resource). The Diagnostic Report resource does not yet provide full support
    for detailed structured reports of sequencing; this is planned for a future
    release.
    """
    
    resource_name = "DiagnosticReport"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.codedDiagnosis = None
        """ Codes for the conclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.conclusion = None
        """ Clinical Interpretation of test results.
        Type `str`. """
        
        self.diagnosticDateTime = None
        """ Physiologically Relevant time/time-period for report.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosticPeriod = None
        """ Physiologically Relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Id for external references to this report.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.image = None
        """ Key images associated with this report.
        List of `DiagnosticReportImage` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items referencing `ImagingStudy` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Date this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Responsible Diagnostic Service.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.presentedForm = None
        """ Entire Report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.requestDetail = None
        """ What was requested.
        List of `FHIRReference` items referencing `DiagnosticOrder` (represented as `dict` in JSON). """
        
        self.result = None
        """ Observations - simple, or complex nested groups.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ Biochemistry, Hematology etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimens this report is based on.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | partial | final | corrected +.
        Type `str`. """
        
        self.subject = None
        """ The subject of the report, usually, but not always, the patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(DiagnosticReport, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticReport, self).update_with_json(jsondict)
        if 'codedDiagnosis' in jsondict:
            self.codedDiagnosis = CodeableConcept.CodeableConcept.with_json(jsondict['codedDiagnosis'])
        if 'conclusion' in jsondict:
            self.conclusion = jsondict['conclusion']
        if 'diagnosticDateTime' in jsondict:
            self.diagnosticDateTime = FHIRDate.FHIRDate.with_json(jsondict['diagnosticDateTime'])
        if 'diagnosticPeriod' in jsondict:
            self.diagnosticPeriod = Period.Period.with_json(jsondict['diagnosticPeriod'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'image' in jsondict:
            self.image = DiagnosticReportImage.with_json(jsondict['image'])
        if 'imagingStudy' in jsondict:
            self.imagingStudy = FHIRReference.FHIRReference.with_json_and_owner(jsondict['imagingStudy'], self, ImagingStudy.ImagingStudy)
        if 'issued' in jsondict:
            self.issued = FHIRDate.FHIRDate.with_json(jsondict['issued'])
        if 'name' in jsondict:
            self.name = CodeableConcept.CodeableConcept.with_json(jsondict['name'])
        if 'performer' in jsondict:
            self.performer = FHIRReference.FHIRReference.with_json_and_owner(jsondict['performer'], self, Practitioner.Practitioner)
        if 'presentedForm' in jsondict:
            self.presentedForm = Attachment.Attachment.with_json(jsondict['presentedForm'])
        if 'requestDetail' in jsondict:
            self.requestDetail = FHIRReference.FHIRReference.with_json_and_owner(jsondict['requestDetail'], self, DiagnosticOrder.DiagnosticOrder)
        if 'result' in jsondict:
            self.result = FHIRReference.FHIRReference.with_json_and_owner(jsondict['result'], self, Observation.Observation)
        if 'serviceCategory' in jsondict:
            self.serviceCategory = CodeableConcept.CodeableConcept.with_json(jsondict['serviceCategory'])
        if 'specimen' in jsondict:
            self.specimen = FHIRReference.FHIRReference.with_json_and_owner(jsondict['specimen'], self, Specimen.Specimen)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])


class DiagnosticReportImage(FHIRElement.FHIRElement):
    """ Key images associated with this report.
    
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comment = None
        """ Comment about the image (e.g. explanation).
        Type `str`. """
        
        self.link = None
        """ Reference to the image source.
        Type `FHIRReference` referencing `Media` (represented as `dict` in JSON). """
        
        super(DiagnosticReportImage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticReportImage, self).update_with_json(jsondict)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'link' in jsondict:
            self.link = FHIRReference.FHIRReference.with_json_and_owner(jsondict['link'], self, Media.Media)

