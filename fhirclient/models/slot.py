#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (slot.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier


class Slot(fhirresource.FHIRResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    
    resource_name = "Slot"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comment = None
        """ Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.
        Type `str`. """
        
        self.end = None
        """ Date/Time that the slot is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.freeBusyType = None
        """ BUSY | FREE | BUSY-UNAVAILABLE | BUSY-TENTATIVE.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastModified = None
        """ When this slot was created, or last revised.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.overbooked = False
        """ This slot has already been overbooked, appointments are unlikely to
        be accepted for this time.
        Type `bool`. """
        
        self.schedule = None
        """ The schedule resource that this slot defines an interval of status
        information.
        Type `FHIRReference` referencing `Schedule` (represented as `dict` in JSON). """
        
        self.start = None
        """ Date/Time that the slot is to begin.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.type = None
        """ The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location,
        rather than the location itself). If provided then this overrides
        the value provided on the availability resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Slot, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Slot, self).update_with_json(jsondict)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json_and_owner(jsondict['end'], self)
        if 'freeBusyType' in jsondict:
            self.freeBusyType = jsondict['freeBusyType']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'lastModified' in jsondict:
            self.lastModified = fhirdate.FHIRDate.with_json_and_owner(jsondict['lastModified'], self)
        if 'overbooked' in jsondict:
            self.overbooked = jsondict['overbooked']
        if 'schedule' in jsondict:
            self.schedule = fhirreference.FHIRReference.with_json_and_owner(jsondict['schedule'], self)
        if 'start' in jsondict:
            self.start = fhirdate.FHIRDate.with_json_and_owner(jsondict['start'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

