#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ImagingObjectSelection) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference


class ImagingObjectSelection(domainresource.DomainResource):
    """ Key Object Selection.
    
    A set of DICOM SOP Instances of a patient, selected for some application
    purpose, e.g., quality assurance, teaching, conference, consulting, etc.
    Objects selected can be from different studies, but must be of the same
    patient.
    """
    
    resource_name = "ImagingObjectSelection"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Author (human or machine).
        Type `FHIRReference` referencing `Practitioner, Device, Organization, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.authoringTime = None
        """ Authoring time of the selection.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Description text.
        Type `str`. """
        
        self.patient = None
        """ Patient of the selected objects.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.study = None
        """ Study identity of the selected instances.
        List of `ImagingObjectSelectionStudy` items (represented as `dict` in JSON). """
        
        self.title = None
        """ Reason for selection.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.uid = None
        """ Instance UID.
        Type `str`. """
        
        super(ImagingObjectSelection, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingObjectSelection, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'authoringTime' in jsondict:
            self.authoringTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['authoringTime'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'study' in jsondict:
            self.study = ImagingObjectSelectionStudy.with_json_and_owner(jsondict['study'], self)
        if 'title' in jsondict:
            self.title = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['title'], self)
        if 'uid' in jsondict:
            self.uid = jsondict['uid']


class ImagingObjectSelectionStudy(fhirelement.FHIRElement):
    """ Study identity of the selected instances.
    
    Study identity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingObjectSelectionStudy"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.series = None
        """ Series identity of the selected instances.
        List of `ImagingObjectSelectionStudySeries` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Study instance uid.
        Type `str`. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudy, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingObjectSelectionStudy, self).update_with_json(jsondict)
        if 'series' in jsondict:
            self.series = ImagingObjectSelectionStudySeries.with_json_and_owner(jsondict['series'], self)
        if 'uid' in jsondict:
            self.uid = jsondict['uid']
        if 'url' in jsondict:
            self.url = jsondict['url']


class ImagingObjectSelectionStudySeries(fhirelement.FHIRElement):
    """ Series identity of the selected instances.
    
    Series indetity and locating information of the DICOM SOP instances in the
    selection.
    """
    
    resource_name = "ImagingObjectSelectionStudySeries"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.instance = None
        """ The selected instance.
        List of `ImagingObjectSelectionStudySeriesInstance` items (represented as `dict` in JSON). """
        
        self.uid = None
        """ Series instance uid.
        Type `str`. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeries, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingObjectSelectionStudySeries, self).update_with_json(jsondict)
        if 'instance' in jsondict:
            self.instance = ImagingObjectSelectionStudySeriesInstance.with_json_and_owner(jsondict['instance'], self)
        if 'uid' in jsondict:
            self.uid = jsondict['uid']
        if 'url' in jsondict:
            self.url = jsondict['url']


class ImagingObjectSelectionStudySeriesInstance(fhirelement.FHIRElement):
    """ The selected instance.
    
    Identity and locating information of the selected DICOM SOP instances.
    """
    
    resource_name = "ImagingObjectSelectionStudySeriesInstance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.frames = None
        """ The frame set.
        List of `ImagingObjectSelectionStudySeriesInstanceFrames` items (represented as `dict` in JSON). """
        
        self.sopClass = None
        """ SOP class uid of instance.
        Type `str`. """
        
        self.uid = None
        """ Uid of the selected instance.
        Type `str`. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeriesInstance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingObjectSelectionStudySeriesInstance, self).update_with_json(jsondict)
        if 'frames' in jsondict:
            self.frames = ImagingObjectSelectionStudySeriesInstanceFrames.with_json_and_owner(jsondict['frames'], self)
        if 'sopClass' in jsondict:
            self.sopClass = jsondict['sopClass']
        if 'uid' in jsondict:
            self.uid = jsondict['uid']
        if 'url' in jsondict:
            self.url = jsondict['url']


class ImagingObjectSelectionStudySeriesInstanceFrames(fhirelement.FHIRElement):
    """ The frame set.
    
    Identity and location information of the frames in the selected instance.
    """
    
    resource_name = "ImagingObjectSelectionStudySeriesInstanceFrames"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.frameNumbers = None
        """ Frame numbers.
        List of `int` items. """
        
        self.url = None
        """ Retrieve URL.
        Type `str`. """
        
        super(ImagingObjectSelectionStudySeriesInstanceFrames, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImagingObjectSelectionStudySeriesInstanceFrames, self).update_with_json(jsondict)
        if 'frameNumbers' in jsondict:
            self.frameNumbers = jsondict['frameNumbers']
        if 'url' in jsondict:
            self.url = jsondict['url']

