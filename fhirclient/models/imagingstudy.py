#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (imagingstudy.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import coding
import diagnosticorder
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner


class ImagingStudy(fhirresource.FHIRResource):
    """ A set of images produced in single study (one or more series of references
    images).
    
    Scope and Usage This resource summarizes a series of images or other
    instances generated as part of an imaging study, and provides references to
    where the images are available using WADO-RS. This resource is used to make
    information concerning images etc. that are available in other clinical
    contexts such as diagnostic reports, Care Plans, etc. Also, see the use
    case description below.
    
    This resources has been specifically designed with use in DICOM contexts in
    mind. The content is closely based on the definitions of the equivalent
    DICOM constructs, and informed by usage patterns already established
    through DICOM implementation practices, including XDS-I. It is not,
    however, necessary to use DICOM infrastructure in order to use this
    resource.
    """
    
    resource_name = "ImagingStudy"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accessionNo = None
        """ Accession Number (0008,0050).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.availability = None
        """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE (0008,0056).
        Type `str`. """
        
        self.clinicalInformation = None
        """ Diagnoses etc with request (0040,1002).
        Type `str`. """
        
        self.dateTime = None
        """ When the study was performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Institution-generated description (0008,1030).
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the study (0020,0010).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpreter = None
        """ Who interpreted images (0008,1060).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.modality = None
        """ All series.modality if actual acquisition modalities.
        List of `str` items. """
        
        self.numberOfInstances = None
        """ Number of Study Related Instances (0020,1208).
        Type `int`. """
        
        self.numberOfSeries = None
        """ Number of Study Related Series (0020,1206).
        Type `int`. """
        
        self.order = None
        """ Order(s) that caused this study to be performed.
        List of `FHIRReference` items referencing `DiagnosticOrder` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Type of procedure performed (0008,1032).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.referrer = None
        """ Referring physician (0008,0090).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.series = None
        """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who the images are of.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.uid = None
        """ Formal identifier for the study (0020,000D).
        Type `str`. """
        
        self.url = None
        """ Retrieve URI (0008,1190).
        Type `str`. """
        
        super(ImagingStudy, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingStudy, self).update_with_json(jsondict)
        if 'accessionNo' in jsondict:
            self.accessionNo = identifier.Identifier.with_json(jsondict['accessionNo'])
        if 'availability' in jsondict:
            self.availability = jsondict['availability']
        if 'clinicalInformation' in jsondict:
            self.clinicalInformation = jsondict['clinicalInformation']
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json(jsondict['dateTime'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'interpreter' in jsondict:
            self.interpreter = fhirreference.FHIRReference.with_json_and_owner(jsondict['interpreter'], self, practitioner.Practitioner)
        if 'modality' in jsondict:
            self.modality = jsondict['modality']
        if 'numberOfInstances' in jsondict:
            self.numberOfInstances = jsondict['numberOfInstances']
        if 'numberOfSeries' in jsondict:
            self.numberOfSeries = jsondict['numberOfSeries']
        if 'order' in jsondict:
            self.order = fhirreference.FHIRReference.with_json_and_owner(jsondict['order'], self, diagnosticorder.DiagnosticOrder)
        if 'procedure' in jsondict:
            self.procedure = coding.Coding.with_json(jsondict['procedure'])
        if 'referrer' in jsondict:
            self.referrer = fhirreference.FHIRReference.with_json_and_owner(jsondict['referrer'], self, practitioner.Practitioner)
        if 'series' in jsondict:
            self.series = ImagingStudySeries.with_json(jsondict['series'])
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'uid' in jsondict:
            self.uid = jsondict['uid']
        if 'url' in jsondict:
            self.url = jsondict['url']


class ImagingStudySeries(fhirelement.FHIRElement):
    """ Each study has one or more series of instances.
    
    Each study has one or more series of image instances.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.availability = None
        """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE (0008,0056).
        Type `str`. """
        
        self.bodySite = None
        """ Body part examined (Map from 0018,0015).
        Type `Coding` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ When the series started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ A description of the series (0008,103E).
        Type `str`. """
        
        self.instance = None
        """ A single instance taken from a patient (image or other).
        List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.modality = None
        """ The modality of the instances in the series (0008,0060).
        Type `str`. """
        
        self.number = None
        """ Number of this series in overall sequence (0020,0011).
        Type `int`. """
        
        self.numberOfInstances = None
        """ Number of Series Related Instances (0020,1209).
        Type `int`. """
        
        self.uid = None
        """ Formal identifier for this series (0020,000E).
        Type `str`. """
        
        self.url = None
        """ Retrieve URI (0008,1115 > 0008,1190).
        Type `str`. """
        
        super(ImagingStudySeries, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingStudySeries, self).update_with_json(jsondict)
        if 'availability' in jsondict:
            self.availability = jsondict['availability']
        if 'bodySite' in jsondict:
            self.bodySite = coding.Coding.with_json(jsondict['bodySite'])
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json(jsondict['dateTime'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'instance' in jsondict:
            self.instance = ImagingStudySeriesInstance.with_json(jsondict['instance'])
        if 'modality' in jsondict:
            self.modality = jsondict['modality']
        if 'number' in jsondict:
            self.number = jsondict['number']
        if 'numberOfInstances' in jsondict:
            self.numberOfInstances = jsondict['numberOfInstances']
        if 'uid' in jsondict:
            self.uid = jsondict['uid']
        if 'url' in jsondict:
            self.url = jsondict['url']


class ImagingStudySeriesInstance(fhirelement.FHIRElement):
    """ A single instance taken from a patient (image or other).
    
    A single image taken from a patient.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.attachment = None
        """ A FHIR resource with content for this instance.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.number = None
        """ The number of this instance in the series (0020,0013).
        Type `int`. """
        
        self.sopclass = None
        """ DICOM class type (0008,0016).
        Type `str`. """
        
        self.title = None
        """ Description (0070,0080 | 0040,A043 > 0008,0104 | 0042,0010 |
        0008,0008).
        Type `str`. """
        
        self.type = None
        """ Type of instance (image etc) (0004,1430).
        Type `str`. """
        
        self.uid = None
        """ Formal identifier for this instance (0008,0018).
        Type `str`. """
        
        self.url = None
        """ WADO-RS service where instance is available  (0008,1199 >
        0008,1190).
        Type `str`. """
        
        super(ImagingStudySeriesInstance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingStudySeriesInstance, self).update_with_json(jsondict)
        if 'attachment' in jsondict:
            self.attachment = fhirreference.FHIRReference.with_json_and_owner(jsondict['attachment'], self, fhirresource.FHIRResource)
        if 'number' in jsondict:
            self.number = jsondict['number']
        if 'sopclass' in jsondict:
            self.sopclass = jsondict['sopclass']
        if 'title' in jsondict:
            self.title = jsondict['title']
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'uid' in jsondict:
            self.uid = jsondict['uid']
        if 'url' in jsondict:
            self.url = jsondict['url']

