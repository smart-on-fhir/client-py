#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ImagingManifest) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class ImagingManifest(domainresource.DomainResource):
    """ Key Object Selection.
    
    A text description of the DICOM SOP instances selected in the
    ImagingManifest; or the reason for, or significance of, the selection.
    """
    
    resource_type = "ImagingManifest"
    
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
        """ Time when the selection of instances was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Description text.
        Type `str`. """
        
        self.identifier = None
        """ SOP Instance UID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.study = None
        """ Study identity of the selected instances.
        List of `ImagingManifestStudy` items (represented as `dict` in JSON). """
        
        super(ImagingManifest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifest, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("authoringTime", "authoringTime", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("study", "study", ImagingManifestStudy, True, None, True),
        ])
        return js


from . import backboneelement

class ImagingManifestStudy(backboneelement.BackboneElement):
    """ Study identity of the selected instances.
    
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_type = "ImagingManifestStudy"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        """ Study access service endpoint.
        List of `FHIRReference` items referencing `Endpoint` (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to ImagingStudy.
        Type `FHIRReference` referencing `ImagingStudy` (represented as `dict` in JSON). """
        
        self.series = None
        """ Series identity of the selected instances.
        List of `ImagingManifestStudySeries` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Study instance UID.
        Type `str`. """
        
        super(ImagingManifestStudy, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudy, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, False, None, False),
            ("series", "series", ImagingManifestStudySeries, True, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingManifestStudySeries(backboneelement.BackboneElement):
    """ Series identity of the selected instances.
    
    Series identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_type = "ImagingManifestStudySeries"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        """ Series access endpoint.
        List of `FHIRReference` items referencing `Endpoint` (represented as `dict` in JSON). """
        
        self.instance = None
        """ The selected instance.
        List of `ImagingManifestStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Series instance UID.
        Type `str`. """
        
        super(ImagingManifestStudySeries, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudySeries, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("instance", "instance", ImagingManifestStudySeriesInstance, True, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


class ImagingManifestStudySeriesInstance(backboneelement.BackboneElement):
    """ The selected instance.
    
    Identity and locating information of the selected DICOM SOP instances.
    """
    
    resource_type = "ImagingManifestStudySeriesInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sopClass = None
        """ SOP class UID of instance.
        Type `str`. """
        
        self.uid = None
        """ Selected instance UID.
        Type `str`. """
        
        super(ImagingManifestStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ImagingManifestStudySeriesInstance, self).elementProperties()
        js.extend([
            ("sopClass", "sopClass", str, False, None, True),
            ("uid", "uid", str, False, None, True),
        ])
        return js


import sys
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
