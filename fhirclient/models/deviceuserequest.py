#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (deviceuserequest.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier
import period
import timing


class DeviceUseRequest(fhirresource.FHIRResource):
    """ Request for device use.
    
    Represents a request for the use of a device.
    """
    
    resource_name = "DeviceUseRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Target body site.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        """ proposed | planned | requested | received | accepted | in progress
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
        if 'bodySite' in jsondict:
            self.bodySite = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySite'], self)
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

