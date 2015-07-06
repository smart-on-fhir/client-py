#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2015-07-06.
#  2015, SMART Health IT.


from . import attachment
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).
    
    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of Series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A Series is of only one modality (e.g., X-ray, CT,
    MR, ultrasound), but a Study may have multiple Series of different
    modalities.
    """
    
    resource_name = "ImagingStudy"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accession = None
        """ Accession Number (0008,0050).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.availability = None
        """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE (0008,0056).
        Type `str`. """
        
        self.clinicalInformation = None
        """ Diagnoses etc with request (0040,1002).
        Type `str`. """
        
        self.description = None
        """ Institution-generated description (0008,1030).
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the study (0020,0010).
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpreter = None
        """ Who interpreted images (0008,1060).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.modalityList = None
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
        
        self.patient = None
        """ Who the images are of.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Type of procedure performed (0008,1032).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.referrer = None
        """ Referring physician (0008,0090).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.series = None
        """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """
        
        self.started = None
        """ When the study was started (0008,0020)+(0008,0030).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.uid = None
        """ Formal identifier for the study (0020,000D).
        Type `str`. """
        
        self.url = None
        """ Retrieve URI (0008,1190).
        Type `str`. """
        
        super(ImagingStudy, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("accession", "accession", identifier.Identifier, False),
            ("availability", "availability", str, False),
            ("clinicalInformation", "clinicalInformation", str, False),
            ("description", "description", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("interpreter", "interpreter", fhirreference.FHIRReference, False),
            ("modalityList", "modalityList", str, True),
            ("numberOfInstances", "numberOfInstances", int, False),
            ("numberOfSeries", "numberOfSeries", int, False),
            ("order", "order", fhirreference.FHIRReference, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("procedure", "procedure", coding.Coding, True),
            ("referrer", "referrer", fhirreference.FHIRReference, False),
            ("series", "series", ImagingStudySeries, True),
            ("started", "started", fhirdate.FHIRDate, False),
            ("uid", "uid", str, False),
            ("url", "url", str, False),
        ])
        return js


class ImagingStudySeries(fhirelement.FHIRElement):
    """ Each study has one or more series of instances.
    
    Each study has one or more series of image instances.
    """
    
    resource_name = "ImagingStudySeries"
    
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
        
        self.laterality = None
        """ Body part laterality.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.modality = None
        """ The modality of the instances in the series (0008,0060).
        Type `str`. """
        
        self.number = None
        """ Numeric identifier of this series (0020,0011).
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
    
    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("availability", "availability", str, False),
            ("bodySite", "bodySite", coding.Coding, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("instance", "instance", ImagingStudySeriesInstance, True),
            ("laterality", "laterality", coding.Coding, False),
            ("modality", "modality", str, False),
            ("number", "number", int, False),
            ("numberOfInstances", "numberOfInstances", int, False),
            ("uid", "uid", str, False),
            ("url", "url", str, False),
        ])
        return js


class ImagingStudySeriesInstance(fhirelement.FHIRElement):
    """ A single instance taken from a patient (image or other).
    
    A single SOP Instance within the series, e.g., an image, or presentation
    state.
    """
    
    resource_name = "ImagingStudySeriesInstance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.content = None
        """ Content of the instance.
        List of `Attachment` items (represented as `dict` in JSON). """
        
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
        
        super(ImagingStudySeriesInstance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("content", "content", attachment.Attachment, True),
            ("number", "number", int, False),
            ("sopclass", "sopclass", str, False),
            ("title", "title", str, False),
            ("type", "type", str, False),
            ("uid", "uid", str, False),
        ])
        return js

