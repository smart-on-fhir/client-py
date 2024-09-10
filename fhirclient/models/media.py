# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Media).
# 2024, SMART Health IT.


from . import domainresource

class Media(domainresource.DomainResource):
    """ A photo, video, or audio recording acquired or used in healthcare. The
    actual content may be inline or provided by direct reference.
    """
    
    resource_type = "Media"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ Procedure that caused this media to be created.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.bodySite = None
        """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.content = None
        """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """
        self._content = None
        """ Primitive extension for content. Type `FHIRPrimitiveExtension` """
        
        self.createdDateTime = None
        """ When Media was collected.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._createdDateTime = None
        """ Primitive extension for createdDateTime. Type `FHIRPrimitiveExtension` """
        
        self.createdPeriod = None
        """ When Media was collected.
        Type `Period` (represented as `dict` in JSON). """
        self._createdPeriod = None
        """ Primitive extension for createdPeriod. Type `FHIRPrimitiveExtension` """
        
        self.device = None
        """ Observing Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._device = None
        """ Primitive extension for device. Type `FHIRPrimitiveExtension` """
        
        self.deviceName = None
        """ Name of the device/manufacturer.
        Type `str`. """
        self._deviceName = None
        """ Primitive extension for deviceName. Type `FHIRPrimitiveExtension` """
        
        self.duration = None
        """ Length in seconds (audio / video).
        Type `float`. """
        self._duration = None
        """ Primitive extension for duration. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter associated with media.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.frames = None
        """ Number of frames if > 1 (photo).
        Type `int`. """
        self._frames = None
        """ Primitive extension for frames. Type `FHIRPrimitiveExtension` """
        
        self.height = None
        """ Height of the image in pixels (photo/video).
        Type `int`. """
        self._height = None
        """ Primitive extension for height. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier(s) for the image.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.issued = None
        """ Date/Time this version was made available.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._issued = None
        """ Primitive extension for issued. Type `FHIRPrimitiveExtension` """
        
        self.modality = None
        """ The type of acquisition equipment/process.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._modality = None
        """ Primitive extension for modality. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments made about the media.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.operator = None
        """ The person who generated the image.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._operator = None
        """ Primitive extension for operator. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why was event performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who/What this Media is a record of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Classification of media as image, video, or audio.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.view = None
        """ Imaging view, e.g. Lateral or Antero-posterior.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._view = None
        """ Primitive extension for view. Type `FHIRPrimitiveExtension` """
        
        self.width = None
        """ Width of the image in pixels (photo/video).
        Type `int`. """
        self._width = None
        """ Primitive extension for width. Type `FHIRPrimitiveExtension` """
        
        super(Media, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Media, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("content", "content", attachment.Attachment, False, None, True),
            ("_content", "_content", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("createdDateTime", "createdDateTime", fhirdatetime.FHIRDateTime, False, "created", False),
            ("_createdDateTime", "_createdDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("createdPeriod", "createdPeriod", period.Period, False, "created", False),
            ("_createdPeriod", "_createdPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("_device", "_device", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deviceName", "deviceName", str, False, None, False),
            ("_deviceName", "_deviceName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("_duration", "_duration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("_frames", "_frames", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("height", "height", int, False, None, False),
            ("_height", "_height", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issued", "issued", fhirinstant.FHIRInstant, False, None, False),
            ("_issued", "_issued", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modality", "modality", codeableconcept.CodeableConcept, False, None, False),
            ("_modality", "_modality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operator", "operator", fhirreference.FHIRReference, False, None, False),
            ("_operator", "_operator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("view", "view", codeableconcept.CodeableConcept, False, None, False),
            ("_view", "_view", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("width", "width", int, False, None, False),
            ("_width", "_width", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import attachment
from . import codeableconcept
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import period