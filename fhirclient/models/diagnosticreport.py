#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (diagnosticreport.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import attachment
import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period


class DiagnosticReport(fhirresource.FHIRResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretation, and formatted representation of diagnostic reports.
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
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        super(DiagnosticReport, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticReport, self).update_with_json(jsondict)
        if 'codedDiagnosis' in jsondict:
            self.codedDiagnosis = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['codedDiagnosis'], self)
        if 'conclusion' in jsondict:
            self.conclusion = jsondict['conclusion']
        if 'diagnosticDateTime' in jsondict:
            self.diagnosticDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['diagnosticDateTime'], self)
        if 'diagnosticPeriod' in jsondict:
            self.diagnosticPeriod = period.Period.with_json_and_owner(jsondict['diagnosticPeriod'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'image' in jsondict:
            self.image = DiagnosticReportImage.with_json_and_owner(jsondict['image'], self)
        if 'imagingStudy' in jsondict:
            self.imagingStudy = fhirreference.FHIRReference.with_json_and_owner(jsondict['imagingStudy'], self)
        if 'issued' in jsondict:
            self.issued = fhirdate.FHIRDate.with_json_and_owner(jsondict['issued'], self)
        if 'name' in jsondict:
            self.name = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['name'], self)
        if 'performer' in jsondict:
            self.performer = fhirreference.FHIRReference.with_json_and_owner(jsondict['performer'], self)
        if 'presentedForm' in jsondict:
            self.presentedForm = attachment.Attachment.with_json_and_owner(jsondict['presentedForm'], self)
        if 'requestDetail' in jsondict:
            self.requestDetail = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestDetail'], self)
        if 'result' in jsondict:
            self.result = fhirreference.FHIRReference.with_json_and_owner(jsondict['result'], self)
        if 'serviceCategory' in jsondict:
            self.serviceCategory = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['serviceCategory'], self)
        if 'specimen' in jsondict:
            self.specimen = fhirreference.FHIRReference.with_json_and_owner(jsondict['specimen'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)


class DiagnosticReportImage(fhirelement.FHIRElement):
    """ Key images associated with this report.
    
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    
    resource_name = "DiagnosticReportImage"
    
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
            self.link = fhirreference.FHIRReference.with_json_and_owner(jsondict['link'], self)

