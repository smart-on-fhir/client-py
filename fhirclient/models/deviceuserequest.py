#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DeviceUseRequest) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirreference
import identifier
import period
import timing


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
    
    def update_with_json(self, jsondict):
        super(DeviceUseRequest, self).update_with_json(jsondict)
        if 'bodySiteCodeableConcept' in jsondict:
            self.bodySiteCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySiteCodeableConcept'], self)
        if 'bodySiteReference' in jsondict:
            self.bodySiteReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['bodySiteReference'], self)
        if 'device' in jsondict:
            self.device = fhirreference.FHIRReference.with_json_and_owner(jsondict['device'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'indication' in jsondict:
            self.indication = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['indication'], self)
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'orderedOn' in jsondict:
            self.orderedOn = fhirdate.FHIRDate.with_json_and_owner(jsondict['orderedOn'], self)
        if 'priority' in jsondict:
            self.priority = jsondict['priority']
        if 'prnReason' in jsondict:
            self.prnReason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['prnReason'], self)
        if 'recordedOn' in jsondict:
            self.recordedOn = fhirdate.FHIRDate.with_json_and_owner(jsondict['recordedOn'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'timingDateTime' in jsondict:
            self.timingDateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['timingDateTime'], self)
        if 'timingPeriod' in jsondict:
            self.timingPeriod = period.Period.with_json_and_owner(jsondict['timingPeriod'], self)
        if 'timingTiming' in jsondict:
            self.timingTiming = timing.Timing.with_json_and_owner(jsondict['timingTiming'], self)

