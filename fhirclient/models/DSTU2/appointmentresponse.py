#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2019-10-12.
#  2019, SMART Health IT.


from . import domainresource

class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    
    resource_name = "AppointmentResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ Person, Location/HealthcareService or Device.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON). """
        
        self.appointment = None
        """ Appointment this response relates to.
        Type `FHIRReference` referencing `Appointment` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Additional comments.
        Type `str`. """
        
        self.end = None
        """ Time from appointment, or requested new end time.
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
        """ Time from appointment, or requested new start time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(AppointmentResponse, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, False, None, True),
            ("comment", "comment", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("participantStatus", "participantStatus", str, False, None, True),
            ("participantType", "participantType", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
