# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ImagingStudy).
# 2024, SMART Health IT.


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
        
        self.basedOn = None
        """ Request fulfilled.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Institution-generated description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter with which this imaging study is associated.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Study access endpoint.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifiers for the whole study.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.interpreter = None
        """ Who interpreted images.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._interpreter = None
        """ Primitive extension for interpreter. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where ImagingStudy occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.modality = None
        """ All series modality if actual acquisition modalities.
        List of `Coding` items (represented as `dict` in JSON). """
        self._modality = None
        """ Primitive extension for modality. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ User-defined comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.numberOfInstances = None
        """ Number of Study Related Instances.
        Type `int`. """
        self._numberOfInstances = None
        """ Primitive extension for numberOfInstances. Type `FHIRPrimitiveExtension` """
        
        self.numberOfSeries = None
        """ Number of Study Related Series.
        Type `int`. """
        self._numberOfSeries = None
        """ Primitive extension for numberOfSeries. Type `FHIRPrimitiveExtension` """
        
        self.procedureCode = None
        """ The performed procedure code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._procedureCode = None
        """ Primitive extension for procedureCode. Type `FHIRPrimitiveExtension` """
        
        self.procedureReference = None
        """ The performed Procedure reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._procedureReference = None
        """ Primitive extension for procedureReference. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Why the study was requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why was study performed.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.referrer = None
        """ Referring physician.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._referrer = None
        """ Primitive extension for referrer. Type `FHIRPrimitiveExtension` """
        
        self.series = None
        """ Each study has one or more series of instances.
        List of `ImagingStudySeries` items (represented as `dict` in JSON). """
        self._series = None
        """ Primitive extension for series. Type `FHIRPrimitiveExtension` """
        
        self.started = None
        """ When the study was started.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._started = None
        """ Primitive extension for started. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ registered | available | cancelled | entered-in-error | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Who or what is the subject of the study.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        super(ImagingStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("interpreter", "interpreter", fhirreference.FHIRReference, True, None, False),
            ("_interpreter", "_interpreter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modality", "modality", coding.Coding, True, None, False),
            ("_modality", "_modality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("_numberOfInstances", "_numberOfInstances", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numberOfSeries", "numberOfSeries", int, False, None, False),
            ("_numberOfSeries", "_numberOfSeries", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedureCode", "procedureCode", codeableconcept.CodeableConcept, True, None, False),
            ("_procedureCode", "_procedureCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, False, None, False),
            ("_procedureReference", "_procedureReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referrer", "referrer", fhirreference.FHIRReference, False, None, False),
            ("_referrer", "_referrer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("series", "series", ImagingStudySeries, True, None, False),
            ("_series", "_series", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("started", "started", fhirdatetime.FHIRDateTime, False, None, False),
            ("_started", "_started", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        
        self.bodySite = None
        """ Body part examined.
        Type `Coding` (represented as `dict` in JSON). """
        self._bodySite = None
        """ Primitive extension for bodySite. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ A short human readable summary of the series.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Series access endpoint.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.instance = None
        """ A single SOP instance from the series.
        List of `ImagingStudySeriesInstance` items (represented as `dict` in JSON). """
        self._instance = None
        """ Primitive extension for instance. Type `FHIRPrimitiveExtension` """
        
        self.laterality = None
        """ Body part laterality.
        Type `Coding` (represented as `dict` in JSON). """
        self._laterality = None
        """ Primitive extension for laterality. Type `FHIRPrimitiveExtension` """
        
        self.modality = None
        """ The modality of the instances in the series.
        Type `Coding` (represented as `dict` in JSON). """
        self._modality = None
        """ Primitive extension for modality. Type `FHIRPrimitiveExtension` """
        
        self.number = None
        """ Numeric identifier of this series.
        Type `int`. """
        self._number = None
        """ Primitive extension for number. Type `FHIRPrimitiveExtension` """
        
        self.numberOfInstances = None
        """ Number of Series Related Instances.
        Type `int`. """
        self._numberOfInstances = None
        """ Primitive extension for numberOfInstances. Type `FHIRPrimitiveExtension` """
        
        self.performer = None
        """ Who performed the series.
        List of `ImagingStudySeriesPerformer` items (represented as `dict` in JSON). """
        self._performer = None
        """ Primitive extension for performer. Type `FHIRPrimitiveExtension` """
        
        self.specimen = None
        """ Specimen imaged.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._specimen = None
        """ Primitive extension for specimen. Type `FHIRPrimitiveExtension` """
        
        self.started = None
        """ When the series started.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._started = None
        """ Primitive extension for started. Type `FHIRPrimitiveExtension` """
        
        self.uid = None
        """ DICOM Series Instance UID for the series.
        Type `str`. """
        self._uid = None
        """ Primitive extension for uid. Type `FHIRPrimitiveExtension` """
        
        super(ImagingStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("_bodySite", "_bodySite", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instance", "instance", ImagingStudySeriesInstance, True, None, False),
            ("_instance", "_instance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("laterality", "laterality", coding.Coding, False, None, False),
            ("_laterality", "_laterality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modality", "modality", coding.Coding, False, None, True),
            ("_modality", "_modality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("number", "number", int, False, None, False),
            ("_number", "_number", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numberOfInstances", "numberOfInstances", int, False, None, False),
            ("_numberOfInstances", "_numberOfInstances", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("performer", "performer", ImagingStudySeriesPerformer, True, None, False),
            ("_performer", "_performer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True, None, False),
            ("_specimen", "_specimen", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("started", "started", fhirdatetime.FHIRDateTime, False, None, False),
            ("_started", "_started", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uid", "uid", str, False, None, True),
            ("_uid", "_uid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._number = None
        """ Primitive extension for number. Type `FHIRPrimitiveExtension` """
        
        self.sopClass = None
        """ DICOM class type.
        Type `Coding` (represented as `dict` in JSON). """
        self._sopClass = None
        """ Primitive extension for sopClass. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Description of instance.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.uid = None
        """ DICOM SOP Instance UID.
        Type `str`. """
        self._uid = None
        """ Primitive extension for uid. Type `FHIRPrimitiveExtension` """
        
        super(ImagingStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("_number", "_number", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sopClass", "sopClass", coding.Coding, False, None, True),
            ("_sopClass", "_sopClass", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("uid", "uid", str, False, None, True),
            ("_uid", "_uid", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """ Who performed the series.
    
    Indicates who or what performed the series and how they were involved.
    """
    
    resource_type = "ImagingStudySeriesPerformer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Who performed the series.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.function = None
        """ Type of performance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._function = None
        """ Primitive extension for function. Type `FHIRPrimitiveExtension` """
        
        super(ImagingStudySeriesPerformer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("function", "function", codeableconcept.CodeableConcept, False, None, False),
            ("_function", "_function", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import coding
from . import fhirdatetime
from . import fhirreference
from . import identifier