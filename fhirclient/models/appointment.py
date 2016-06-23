#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Appointment) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """
    
    resource_name = "Appointment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Additional comments.
        Type `str`. """
        
        self.description = None
        """ Shown on a subject line in a meeting request, or appointment list.
        Type `str`. """
        
        self.end = None
        """ When appointment is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.minutesDuration = None
        """ Can be less than start/end (e.g. estimate).
        Type `int`. """
        
        self.participant = None
        """ Participants involved in appointment.
        List of `AppointmentParticipant` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ Used to make informed decisions if needing to re-prioritize.
        Type `int`. """
        
        self.reason = None
        """ Reason this appointment is scheduled.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.slot = None
        """ If provided, then no schedule and start/end values MUST match slot.
        List of `FHIRReference` items referencing `Slot` (represented as `dict` in JSON). """
        
        self.start = None
        """ When appointment is to take place.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ proposed | pending | booked | arrived | fulfilled | cancelled |
        noshow.
        Type `str`. """
        
        self.type = None
        """ The type of appointment that is being booked.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Appointment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("description", "description", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("minutesDuration", "minutesDuration", int, False, None, False),
            ("participant", "participant", AppointmentParticipant, True, None, True),
            ("priority", "priority", int, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("slot", "slot", fhirreference.FHIRReference, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class AppointmentParticipant(backboneelement.BackboneElement):
    """ Participants involved in appointment.
    
    List of participants involved in the appointment.
    """
    
    resource_name = "AppointmentParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Person, Location/HealthcareService or Device.
        Type `FHIRReference` referencing `Patient, Practitioner, RelatedPerson, Device, HealthcareService, Location` (represented as `dict` in JSON). """
        
        self.required = None
        """ required | optional | information-only.
        Type `str`. """
        
        self.status = None
        """ accepted | declined | tentative | needs-action.
        Type `str`. """
        
        self.type = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(AppointmentParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("required", "required", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
