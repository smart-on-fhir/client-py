#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Media) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Media(domainresource.DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    
    resource_name = "Media"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(Media, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("content", "content", attachment.Attachment, False, None, True),
            ("deviceName", "deviceName", str, False, None, False),
            ("duration", "duration", int, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("height", "height", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("operator", "operator", fhirreference.FHIRReference, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
            ("view", "view", codeableconcept.CodeableConcept, False, None, False),
            ("width", "width", int, False, None, False),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import fhirreference
from . import identifier
