#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).
    
    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """
    
    resource_name = "ImagingStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.accession = None
        """ Related workflow identifier ("Accession Number").
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.availability = None
        """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE (0008,0056).
        Type `str`. """
        
        self.description = None
        """ Institution-generated description.
        Type `str`. """
        
        self.identifier = None
        """ Other identifiers for the study.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpreter = None
        """ Who interpreted images.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.modalityList = None
        """ All series modality if actual acquisition modalities.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.numberOfInstances = None
        """ Number of Study Related Instances.
        Type `int`. """
        
        self.numberOfSeries = None
        """ Number of Study Related Series.
        Type `int`. """
        
        self.order = None
        """ Order(s) that caused this study to be performed.
        List of `FHIRReference` items referencing `DiagnosticOrder` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who the images are of.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.procedure = None
        """ Type of procedure performed.
        List of `FHIRReference` items referencing `Procedure` (represented as `dict` in JSON). """
        
        self.referrer = None
        """ Referring physician (0008,0090).
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.series = None
        """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """
        
        self.started = None
        """ When the study was started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.uid = None
        """ Formal identifier for the study.
        Type `str`. """
        
        self.url = None
        """ Retrieve URI.
        Type `str`. """
        
        super(ImagingStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("accession", "accession", identifier.Identifier, False, None, False),
            ("availability", "availability", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpreter", "interpreter", fhirreference.FHIRReference, False, None, False),
            ("modalityList", "modalityList", coding.Coding, True, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, True),
            ("numberOfSeries", "numberOfSeries", int, False, None, True),
            ("order", "order", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("procedure", "procedure", fhirreference.FHIRReference, True, None, False),
            ("referrer", "referrer", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingStudySeries, True, None, False),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("uid", "uid", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


from . import backboneelement

class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.
    
    Each study has one or more series of images or other content.
    """
    
    resource_name = "ImagingStudySeries"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.availability = None
        """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE.
        Type `str`. """
        
        self.bodySite = None
        """ Body part examined.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.description = None
        """ A description of the series.
        Type `str`. """
        
        self.instance = None
        """ A single SOP instance from the series.
        List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.laterality = None
        """ Body part laterality.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.modality = None
        """ The modality of the instances in the series.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.number = None
        """ Numeric identifier of this series.
        Type `int`. """
        
        self.numberOfInstances = None
        """ Number of Series Related Instances.
        Type `int`. """
        
        self.started = None
        """ When the series started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.uid = None
        """ Formal identifier for this series.
        Type `str`. """
        
        self.url = None
        """ Location of the referenced instance(s).
        Type `str`. """
        
        super(ImagingStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("availability", "availability", str, False, None, False),
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("description", "description", str, False, None, False),
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False),
            ("laterality", "laterality", coding.Coding, False, None, False),
            ("modality", "modality", coding.Coding, False, None, True),
            ("number", "number", int, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, True),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("uid", "uid", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.
    
    A single SOP Instance within the series, e.g. an image, or presentation
    state.
    """
    
    resource_name = "ImagingStudySeriesInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.content = None
        """ Content of the instance.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.number = None
        """ The number of this instance in the series.
        Type `int`. """
        
        self.sopClass = None
        """ DICOM class type.
        Type `str`. """
        
        self.title = None
        """ Description of instance.
        Type `str`. """
        
        self.type = None
        """ Type of instance (image etc.).
        Type `str`. """
        
        self.uid = None
        """ Formal identifier for this instance.
        Type `str`. """
        
        super(ImagingStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("content", "content", attachment.Attachment, True, None, False),
            ("number", "number", int, False, None, False),
            ("sopClass", "sopClass", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("type", "type", str, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


from . import attachment
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
