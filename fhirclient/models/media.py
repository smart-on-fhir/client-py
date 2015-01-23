#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (media.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import attachment
import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier


class Media(fhirresource.FHIRResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    
    resource_name = "Media"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.content = None
        """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.created = None
        """ When the media was taken/recorded (start).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deviceName = None
        """ Name of the device/manufacturer.
        Type `str`. """
        
        self.duration = None
        """ Length in seconds (audio / video).
        Type `int`. """
        
        self.frames = None
        """ Number of frames if > 1 (photo).
        Type `int`. """
        
        self.height = None
        """ Height of the image in pixels(photo/video).
        Type `int`. """
        
        self.identifier = None
        """ Identifier(s) for the image.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.operator = None
        """ The person who generated the image.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who/What this Media is a record of.
        Type `FHIRReference` referencing `Patient, Practitioner, Group, Device, Specimen` (represented as `dict` in JSON). """
        
        self.subtype = None
        """ The type of acquisition equipment/process.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
            self.content = attachment.Attachment.with_json_and_owner(jsondict['content'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'deviceName' in jsondict:
            self.deviceName = jsondict['deviceName']
        if 'duration' in jsondict:
            self.duration = jsondict['duration']
        if 'frames' in jsondict:
            self.frames = jsondict['frames']
        if 'height' in jsondict:
            self.height = jsondict['height']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'operator' in jsondict:
            self.operator = fhirreference.FHIRReference.with_json_and_owner(jsondict['operator'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'subtype' in jsondict:
            self.subtype = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['subtype'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']
        if 'view' in jsondict:
            self.view = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['view'], self)
        if 'width' in jsondict:
            self.width = jsondict['width']

