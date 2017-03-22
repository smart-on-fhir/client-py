#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Media) on 2017-03-22.
#  2017, SMART Health IT.


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
        List of `FHIRReference` items referencing `ProcedureRequest` (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Body part in media.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ Actual Media - reference or data.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter / Episode associated with media.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.device = None
        """ Observing Device.
        Type `FHIRReference` referencing `Device, DeviceMetric` (represented as `dict` in JSON). """
        
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
        
        self.note = None
        """ Comments made about the media.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When Media was collected.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When Media was collected.
        Type `Period` (represented as `dict` in JSON). """
        
        self.operator = None
        """ The person who generated the image.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Why was event performed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False, None, False),
            ("content", "content", attachment.Attachment, False, None, True),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("device", "device", fhirreference.FHIRReference, False, None, False),
            ("duration", "duration", int, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("height", "height", int, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("operator", "operator", fhirreference.FHIRReference, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", str, False, None, True),
            ("view", "view", codeableconcept.CodeableConcept, False, None, False),
            ("width", "width", int, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
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
