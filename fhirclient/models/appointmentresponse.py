#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirreference
import identifier


class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    
    resource_name = "AppointmentResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ A Person, Location/HealthcareService or Device that is
        participating in the appointment.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON). """
        
        self.appointment = None
        """ Parent appointment that this response is replying to.
        Type `FHIRReference` referencing `Appointment` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Additional comments about the appointment.
        Type `str`. """
        
        self.end = None
        """ Date/Time that the appointment is to conclude, or requested new end
        time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.participantStatus = None
        """ accepted | declined | tentative | in-process | completed | needs-
        action.
        Type `str`. """
        
        self.participantType = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.start = None
        """ Date/Time that the appointment is to take place, or requested new
        start time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(AppointmentResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(AppointmentResponse, self).update_with_json(jsondict)
        if 'actor' in jsondict:
            self.actor = fhirreference.FHIRReference.with_json_and_owner(jsondict['actor'], self)
        if 'appointment' in jsondict:
            self.appointment = fhirreference.FHIRReference.with_json_and_owner(jsondict['appointment'], self)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json_and_owner(jsondict['end'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'participantStatus' in jsondict:
            self.participantStatus = jsondict['participantStatus']
        if 'participantType' in jsondict:
            self.participantType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['participantType'], self)
        if 'start' in jsondict:
            self.start = fhirdate.FHIRDate.with_json_and_owner(jsondict['start'], self)

