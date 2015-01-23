#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (appointment.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class Appointment(fhirresource.FHIRResource):
    """ A scheduled healthcare event for a patient and/or practitioner(s) where a
    service may take place at a specific date/time.
    """
    
    resource_name = "Appointment"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comment = None
        """ Additional comments about the appointment.
        Type `str`. """
        
        self.description = None
        """ The brief description of the appointment as would be shown on a
        subject line in a meeting request, or appointment list. Detailed or
        expanded information should be put in the comment field.
        Type `str`. """
        
        self.end = None
        """ Date/Time that the appointment is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.lastModified = None
        """ Date when the appointment was recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastModifiedBy = None
        """ Who recorded the appointment.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.location = None
        """ The primary location that this appointment is to take place.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.order = None
        """ An Order that lead to the creation of this appointment.
        Type `FHIRReference` referencing `Order` (represented as `dict` in JSON). """
        
        self.participant = None
        """ List of participants involved in the appointment.
        List of `AppointmentParticipant` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ The priority of the appointment. Can be used to make informed
        decisions if needing to re-prioritize appointments. (The iCal
        Standard specifies 0 as undefined, 1 as highest, 9 as lowest
        priority) (Need to change back to CodeableConcept).
        Type `int`. """
        
        self.reason = None
        """ The reason that this appointment is being scheduled, this is more
        clinical than administrative.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.slot = None
        """ The slot that this appointment is filling. If provided then the
        schedule will not be provided as slots are not recursive, and the
        start/end values MUST be the same as from the slot.
        List of `FHIRReference` items referencing `Slot` (represented as `dict` in JSON). """
        
        self.start = None
        """ Date/Time that the appointment is to take place.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ pending | booked | arrived | fulfilled | cancelled | noshow.
        Type `str`. """
        
        self.type = None
        """ The type of appointments that is being booked (ideally this would
        be an identifiable service - which is at a location, rather than
        the location itself).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Appointment, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Appointment, self).update_with_json(jsondict)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json_and_owner(jsondict['end'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'lastModified' in jsondict:
            self.lastModified = fhirdate.FHIRDate.with_json_and_owner(jsondict['lastModified'], self)
        if 'lastModifiedBy' in jsondict:
            self.lastModifiedBy = fhirreference.FHIRReference.with_json_and_owner(jsondict['lastModifiedBy'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'order' in jsondict:
            self.order = fhirreference.FHIRReference.with_json_and_owner(jsondict['order'], self)
        if 'participant' in jsondict:
            self.participant = AppointmentParticipant.with_json_and_owner(jsondict['participant'], self)
        if 'priority' in jsondict:
            self.priority = jsondict['priority']
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'slot' in jsondict:
            self.slot = fhirreference.FHIRReference.with_json_and_owner(jsondict['slot'], self)
        if 'start' in jsondict:
            self.start = fhirdate.FHIRDate.with_json_and_owner(jsondict['start'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class AppointmentParticipant(fhirelement.FHIRElement):
    """ List of participants involved in the appointment.
    """
    
    resource_name = "AppointmentParticipant"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ A Person of device that is participating in the appointment,
        usually Practitioner, Patient, RelatedPerson or Device.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.required = None
        """ required | optional | information-only.
        Type `str`. """
        
        self.status = None
        """ accepted | declined | tentative | in-process | completed | needs-
        action.
        Type `str`. """
        
        self.type = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(AppointmentParticipant, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AppointmentParticipant, self).update_with_json(jsondict)
        if 'actor' in jsondict:
            self.actor = fhirreference.FHIRReference.with_json_and_owner(jsondict['actor'], self)
        if 'required' in jsondict:
            self.required = jsondict['required']
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

