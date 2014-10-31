#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (media.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import attachment
import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner


class Media(fhirresource.FHIRResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    
    Scope and Usage The Media resource contains photos, videos, and audio
    recordings. It is used with media acquired or used as part of the
    healthcare process. Here are some typical usages:
    
    * Photos of patients and staff for identification purposes
    * Photos and videos of diagnostic or care provision procedures for
    recording purposes
    * Storing scans and faxes of paper documents where not enough metadata
    exists to create a DocumentReference
    * Images on diagnostic reports
    The Media resource may contain medical images in a DICOM format. While such
    images may also be accessible through an ImagingStudy resource, the Media
    resource enables "ready for presentation" access to a specific image. Such
    images would preferentially be made available in a FHIR ecosystem by the
    Media.content.url providing a reference to a WADO-RS service to access the
    image. That WADO-RS service may include rendering the image with
    annotations and display parameters from an associated DICOM presentation
    state. Although the Media resource is allowed to contain images collected
    by a DICOM based system, DICOM images would preferentially be made
    available in a FHIR ecosystem by provision of a resource with references to
    a WADO-RS server.
    """
    
    resource_name = "Media"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.content = None
        """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ When the media was taken/recorded (end).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deviceName = None
        """ Name of the device/manufacturer.
        Type `str`. """
        
        self.frames = None
        """ Number of frames if > 1 (photo).
        Type `int`. """
        
        self.height = None
        """ Height of the image in pixels(photo/video).
        Type `int`. """
        
        self.identifier = None
        """ Identifier(s) for the image.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.length = None
        """ Length in seconds (audio / video).
        Type `int`. """
        
        self.operator = None
        """ The person who generated the image.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who/What this Media is a record of.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.subtype = None
        """ The type of acquisition equipment/process.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ photo | video | audio.
        Type `str`. """
        
        self.view = None
        """ Imaging view e.g Lateral or Antero-posterior.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.width = None
        """ Width of the image in pixels (photo/video).
        Type `int`. """
        
        super(Media, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Media, self).update_with_json(jsondict)
        if 'content' in jsondict:
            self.content = attachment.Attachment.with_json(jsondict['content'])
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json(jsondict['dateTime'])
        if 'deviceName' in jsondict:
            self.deviceName = jsondict['deviceName']
        if 'frames' in jsondict:
            self.frames = jsondict['frames']
        if 'height' in jsondict:
            self.height = jsondict['height']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'length' in jsondict:
            self.length = jsondict['length']
        if 'operator' in jsondict:
            self.operator = fhirreference.FHIRReference.with_json_and_owner(jsondict['operator'], self, practitioner.Practitioner)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'subtype' in jsondict:
            self.subtype = codeableconcept.CodeableConcept.with_json(jsondict['subtype'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'view' in jsondict:
            self.view = codeableconcept.CodeableConcept.with_json(jsondict['view'])
        if 'width' in jsondict:
            self.width = jsondict['width']

