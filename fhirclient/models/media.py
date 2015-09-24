#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Media) on 2015-09-24.
#  2015, SMART Health IT.


from . import attachment
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import identifier


class Media(domainresource.DomainResource):
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
        """ Height of the image in pixels (photo/video).
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
        """ Imaging view, e.g. Lateral or Antero-posterior.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.width = None
        """ Width of the image in pixels (photo/video).
        Type `int`. """
        
        super(Media, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("content", "content", attachment.Attachment, False),
            ("deviceName", "deviceName", str, False),
            ("duration", "duration", int, False),
            ("frames", "frames", int, False),
            ("height", "height", int, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("operator", "operator", fhirreference.FHIRReference, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, False),
            ("type", "type", str, False),
            ("view", "view", codeableconcept.CodeableConcept, False),
            ("width", "width", int, False),
        ])
        return js

