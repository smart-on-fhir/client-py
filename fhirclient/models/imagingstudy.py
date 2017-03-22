#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2017-03-22.
#  2017, SMART Health IT.


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
    
    resource_type = "ImagingStudy"
    
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
        """ ONLINE | OFFLINE | NEARLINE | UNAVAILABLE.
        Type `str`. """
        
        self.basedOn = None
        """ Request fulfilled.
        List of `FHIRReference` items referencing `ReferralRequest, CarePlan, ProcedureRequest` (represented as `dict` in JSON). """
        
        self.context = None
        """ Originating context.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.description = None
        """ Institution-generated description.
        Type `str`. """
        
        self.endpoint = None
        """ Study access endpoint.
        List of `FHIRReference` items referencing `Endpoint` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Other identifiers for the study.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interpreter = None
        """ Who interpreted images.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.modalityList = None
        """ All series modality if actual acquisition modalities.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.numberOfInstances = None
        """ Number of Study Related Instances.
        Type `int`. """
        
        self.numberOfSeries = None
        """ Number of Study Related Series.
        Type `int`. """
        
        self.patient = None
        """ Who the images are of.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.procedureCode = None
        """ The performed procedure code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.procedureReference = None
        """ The performed Procedure reference.
        List of `FHIRReference` items referencing `Procedure` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Why the study was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.referrer = None
        """ Referring physician.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.series = None
        """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """
        
        self.started = None
        """ When the study was started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.uid = None
        """ Formal DICOM identifier for the study.
        Type `str`. """
        
        super(ImagingStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("accession", "accession", identifier.Identifier, False, None, False),
            ("availability", "availability", str, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interpreter", "interpreter", fhirreference.FHIRReference, True, None, False),
            ("modalityList", "modalityList", coding.Coding, True, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("numberOfSeries", "numberOfSeries", int, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("procedureCode", "procedureCode", codeableconcept.CodeableConcept, True, None, False),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, True, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("referrer", "referrer", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingStudySeries, True, None, False),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


from . import backboneelement

class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.
    
    Each study has one or more series of images or other content.
    """
    
    resource_type = "ImagingStudySeries"
    
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
        """ A short human readable summary of the series.
        Type `str`. """
        
        self.endpoint = None
        """ Series access endpoint.
        List of `FHIRReference` items referencing `Endpoint` (represented as `dict` in JSON). """
        
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
        
        self.performer = None
        """ Who performed the series.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.started = None
        """ When the series started.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.uid = None
        """ Formal DICOM identifier for this series.
        Type `str`. """
        
        super(ImagingStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("availability", "availability", str, False, None, False),
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("description", "description", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False),
            ("laterality", "laterality", coding.Coding, False, None, False),
            ("modality", "modality", coding.Coding, False, None, True),
            ("number", "number", int, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, True, None, False),
            ("started", "started", fhirdate.FHIRDate, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.
    
    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """
    
    resource_type = "ImagingStudySeriesInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.number = None
        """ The number of this instance in the series.
        Type `int`. """
        
        self.sopClass = None
        """ DICOM class type.
        Type `str`. """
        
        self.title = None
        """ Description of instance.
        Type `str`. """
        
        self.uid = None
        """ Formal DICOM identifier for this instance.
        Type `str`. """
        
        super(ImagingStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("sopClass", "sopClass", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("uid", "uid", str, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
