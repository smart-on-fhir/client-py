#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DeviceUseRequest) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing


class DeviceUseRequest(domainresource.DomainResource):
    """ A request for a patient to use or be given a medical device.
    
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    
    resource_name = "DeviceUseRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySiteCodeableConcept = None
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySiteReference = None
        """ Target body site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        self.device = None
        """ Device requested.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter motivating request.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Notes or comments.
        List of `str` items. """
        
        self.orderedOn = None
        """ When ordered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        self.prnReason = None
        """ PRN.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recordedOn = None
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | aborted.
        Type `str`. """
        
        self.subject = None
        """ Focus of request.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None
        """ Schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None
        """ Schedule for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None
        """ Schedule for use.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(DeviceUseRequest, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DeviceUseRequest, self).elementProperties()
        js.extend([
            ("bodySiteCodeableConcept", "bodySiteCodeableConcept", codeableconcept.CodeableConcept, False),
            ("bodySiteReference", "bodySiteReference", fhirreference.FHIRReference, False),
            ("device", "device", fhirreference.FHIRReference, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("indication", "indication", codeableconcept.CodeableConcept, True),
            ("notes", "notes", str, True),
            ("orderedOn", "orderedOn", fhirdate.FHIRDate, False),
            ("priority", "priority", str, False),
            ("prnReason", "prnReason", codeableconcept.CodeableConcept, True),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False),
            ("timingPeriod", "timingPeriod", period.Period, False),
            ("timingTiming", "timingTiming", timing.Timing, False),
        ])
        return js

