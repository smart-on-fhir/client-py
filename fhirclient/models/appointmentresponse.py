#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


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
    
    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False),
            ("appointment", "appointment", fhirreference.FHIRReference, False),
            ("comment", "comment", str, False),
            ("end", "end", fhirdate.FHIRDate, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("participantStatus", "participantStatus", str, False),
            ("participantType", "participantType", codeableconcept.CodeableConcept, True),
            ("start", "start", fhirdate.FHIRDate, False),
        ])
        return js

