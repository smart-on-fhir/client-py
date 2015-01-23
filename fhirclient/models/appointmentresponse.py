#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (appointmentresponse.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier


class AppointmentResponse(fhirresource.FHIRResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    
    resource_name = "AppointmentResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.appointment = None
        """ Parent appointment that this response is replying to.
        Type `FHIRReference` referencing `Appointment` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Additional comments about the appointment.
        Type `str`. """
        
        self.end = None
        """ Date/Time that the appointment is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.individual = None
        """ A Person of device that is participating in the appointment,
        usually Practitioner, Patient, RelatedPerson or Device.
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.lastModified = None
        """ Date when the response was recorded or last updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lastModifiedBy = None
        """ Who recorded the appointment response.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.participantStatus = None
        """ accepted | declined | tentative | in-process | completed | needs-
        action.
        Type `str`. """
        
        self.participantType = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.start = None
        """ Date/Time that the appointment is to take place.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(AppointmentResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AppointmentResponse, self).update_with_json(jsondict)
        if 'appointment' in jsondict:
            self.appointment = fhirreference.FHIRReference.with_json_and_owner(jsondict['appointment'], self)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json_and_owner(jsondict['end'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'individual' in jsondict:
            self.individual = fhirreference.FHIRReference.with_json_and_owner(jsondict['individual'], self)
        if 'lastModified' in jsondict:
            self.lastModified = fhirdate.FHIRDate.with_json_and_owner(jsondict['lastModified'], self)
        if 'lastModifiedBy' in jsondict:
            self.lastModifiedBy = fhirreference.FHIRReference.with_json_and_owner(jsondict['lastModifiedBy'], self)
        if 'participantStatus' in jsondict:
            self.participantStatus = jsondict['participantStatus']
        if 'participantType' in jsondict:
            self.participantType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['participantType'], self)
        if 'start' in jsondict:
            self.start = fhirdate.FHIRDate.with_json_and_owner(jsondict['start'], self)

