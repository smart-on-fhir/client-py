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
        
        self.bodySite = None
        """ Observed body part.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.createdDateTime = None
        """ When Media was collected.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.createdPeriod = None
        """ When Media was collected.
        Type `Period` (represented as `dict` in JSON). """
        
        self.device = None
        """ Observing Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.deviceName = None
        """ Name of the device/manufacturer.
        Type `str`. """
        
        self.duration = None
        """ Length in seconds (audio / video).
        Type `float`. """
        
        self.encounter = None
        """ Encounter associated with media.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.frames = None
        """ Number of frames if > 1 (photo).
        Type `int`. """
        
        self.height = None
        """ Height of the image in pixels (photo/video).
        Type `int`. """
        
        self.identifier = None
        """ Identifier(s) for the image.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issued = None
        """ Date/Time this version was made available.
        Type `FHIRInstant` (represented as `str` in JSON). """
        
        self.modality = None
        """ The type of acquisition equipment/process.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the media.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.operator = None
        """ The person who generated the image.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why was event performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """
        
        self.subject = None
        """ Who/What this Media is a record of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Classification of media as image, video, or audio.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
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
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("content", "content", attachment.Attachment, False, None, True),
            ("createdDateTime", "createdDateTime", fhirdatetime.FHIRDateTime, False, "created", False),
            ("createdPeriod", "createdPeriod", period.Period, False, "created", False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("deviceName", "deviceName", str, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("height", "height", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issued", "issued", fhirinstant.FHIRInstant, False, None, False),
            ("modality", "modality", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("operator", "operator", fhirreference.FHIRReference, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("view", "view", codeableconcept.CodeableConcept, False, None, False),
            ("width", "width", int, False, None, False),
        ])
        return js


from . import annotation
from . import attachment
from . import codeableconcept
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import period
