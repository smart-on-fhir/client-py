#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Appointment) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
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
        priority).
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
        """ The type of appointment that is being booked.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Appointment, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False),
            ("description", "description", str, False),
            ("end", "end", fhirdate.FHIRDate, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("order", "order", fhirreference.FHIRReference, False),
            ("participant", "participant", AppointmentParticipant, True),
            ("priority", "priority", int, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False),
            ("slot", "slot", fhirreference.FHIRReference, True),
            ("start", "start", fhirdate.FHIRDate, False),
            ("status", "status", str, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


class AppointmentParticipant(fhirelement.FHIRElement):
    """ List of participants involved in the appointment.
    """
    
    resource_name = "AppointmentParticipant"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ A Person, Location/HealthcareService or Device that is
        participating in the appointment.
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
        
        super(AppointmentParticipant, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False),
            ("required", "required", str, False),
            ("status", "status", str, False),
            ("type", "type", codeableconcept.CodeableConcept, True),
        ])
        return js

