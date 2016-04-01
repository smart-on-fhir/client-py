#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8139 (http://hl7.org/fhir/StructureDefinition/ImagingExcerpt) on 2016-04-01.
#  2016, SMART Health IT.


from . import domainresource

class ImagingExcerpt(domainresource.DomainResource):
    """ Key Object Selection.
    
    A manifest of a set of DICOM Service-Object Pair Instances (SOP Instances).
    The referenced SOP Instances (images or other content) are for a single
    patient, and may be from one or more studies. The referenced SOP Instances
    have been selected for a purpose, such as quality assurance, conference, or
    consult. Reflecting that range of purposes, typical ImagingExcerpt
    resources may include all SOP Instances in a study (perhaps for sharing
    through a Health Information Exchange); key images from multiple studies
    (for reference by a referring or treating physician); a multi-frame
    ultrasound instance ("cine" video clip) and a set of measurements taken
    from that instance (for inclusion in a teaching file); and so on.
    """
    
    resource_name = "ImagingExcerpt"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ Author (human or machine).
        Type `FHIRReference` referencing `Practitioner, Device, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authoringTime = None
        """ Time when the imaging object selection was created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Description text.
        Type `str`. """
        
        self.patient = None
        """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.study = None
        """ Study identity of the selected instances.
        List of `ImagingExcerptStudy` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Reason for selection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uid = None
        """ Instance UID.
        Type `str`. """
        
        super(ImagingExcerpt, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerpt, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoringTime", "authoringTime", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("study", "study", ImagingExcerptStudy, True, None, True),
            ("title", "title", codeableconcept.CodeableConcept, False, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


from . import backboneelement

class ImagingExcerptStudy(backboneelement.BackboneElement):
    """ Study identity of the selected instances.
    
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingExcerptStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dicom = None
        """ Dicom web access.
        List of `ImagingExcerptStudyDicom` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to ImagingStudy.
        Type `FHIRReference` referencing `ImagingStudy` (represented as `dict` in JSON). """
        
        self.series = None
        """ Series identity of the selected instances.
        List of `ImagingExcerptStudySeries` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Study instance UID.
        Type `str`. """
        
        self.viewable = None
        """ Viewable format.
        List of `ImagingExcerptStudyViewable` items (represented as `dict` in JSON). """
        
        super(ImagingExcerptStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerptStudy, self).elementProperties()
        js.extend([
            ("dicom", "dicom", ImagingExcerptStudyDicom, True, None, False),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingExcerptStudySeries, True, None, True),
            ("uid", "uid", str, False, None, True),
            ("viewable", "viewable", ImagingExcerptStudyViewable, True, None, False),
        ])
        return js


class ImagingExcerptStudyDicom(backboneelement.BackboneElement):
    """ Dicom web access.
    
    Methods of accessing using DICOM web technologies.
    """
    
    resource_name = "ImagingExcerptStudyDicom"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ WADO-RS | WADO-URI | IID | WADO-WS.
        Type `str`. """
        
        self.url = None
        """ Retrieve study URL.
        Type `str`. """
        
        super(ImagingExcerptStudyDicom, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerptStudyDicom, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


class ImagingExcerptStudySeries(backboneelement.BackboneElement):
    """ Series identity of the selected instances.
    
    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingExcerptStudySeries"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dicom = None
        """ Dicom web access.
        List of `ImagingExcerptStudySeriesDicom` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ The selected instance.
        List of `ImagingExcerptStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Series instance UID.
        Type `str`. """
        
        super(ImagingExcerptStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerptStudySeries, self).elementProperties()
        js.extend([
            ("dicom", "dicom", ImagingExcerptStudySeriesDicom, True, None, False),
            ("instance", "instance", ImagingExcerptStudySeriesInstance, True, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingExcerptStudySeriesDicom(backboneelement.BackboneElement):
    """ Dicom web access.
    
    Methods of accessing using DICOM web technologies.
    """
    
    resource_name = "ImagingExcerptStudySeriesDicom"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ WADO-RS | WADO-URI | IID | WADO-WS.
        Type `str`. """
        
        self.url = None
        """ Retrieve study URL.
        Type `str`. """
        
        super(ImagingExcerptStudySeriesDicom, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerptStudySeriesDicom, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


class ImagingExcerptStudySeriesInstance(backboneelement.BackboneElement):
    """ The selected instance.
    
    Identity and locating information of the selected DICOM SOP instances.
    """
    
    resource_name = "ImagingExcerptStudySeriesInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dicom = None
        """ Dicom web access.
        List of `ImagingExcerptStudySeriesInstanceDicom` items (represented as `dict` in JSON). """
        
        self.frameNumbers = None
        """ Frame reference number.
        List of `int` items. """
        
        self.sopClass = None
        """ SOP class UID of instance.
        Type `str`. """
        
        self.uid = None
        """ Selected instance UID.
        Type `str`. """
        
        super(ImagingExcerptStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerptStudySeriesInstance, self).elementProperties()
        js.extend([
            ("dicom", "dicom", ImagingExcerptStudySeriesInstanceDicom, True, None, False),
            ("frameNumbers", "frameNumbers", int, True, None, False),
            ("sopClass", "sopClass", str, False, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingExcerptStudySeriesInstanceDicom(backboneelement.BackboneElement):
    """ Dicom web access.
    
    Methods of accessing using DICOM web technologies.
    """
    
    resource_name = "ImagingExcerptStudySeriesInstanceDicom"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ WADO-RS | WADO-URI | IID | WADO-WS.
        Type `str`. """
        
        self.url = None
        """ Retrieve study URL.
        Type `str`. """
        
        super(ImagingExcerptStudySeriesInstanceDicom, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerptStudySeriesInstanceDicom, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, True),
        ])
        return js


class ImagingExcerptStudyViewable(backboneelement.BackboneElement):
    """ Viewable format.
    
    A set of viewable reference images of various  types.
    """
    
    resource_name = "ImagingExcerptStudyViewable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ Mime type of the content, with charset etc..
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
        
        self.size = None
        """ Number of bytes of content (if url provided).
        Type `int`. """
        
        self.title = None
        """ Label to display in place of the data.
        Type `str`. """
        
        self.url = None
        """ Uri where the data can be found.
        Type `str`. """
        
        self.width = None
        """ Width of the image in pixels (photo/video).
        Type `int`. """
        
        super(ImagingExcerptStudyViewable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingExcerptStudyViewable, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, True),
            ("duration", "duration", int, False, None, False),
            ("frames", "frames", int, False, None, False),
            ("height", "height", int, False, None, False),
            ("size", "size", int, False, None, False),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("width", "width", int, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
