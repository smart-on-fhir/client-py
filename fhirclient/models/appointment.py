#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Appointment) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Appointment(domainresource.DomainResource):
    """ A booking of a healthcare event among patient(s), practitioner(s), related
    person(s) and/or device(s) for a specific date/time. This may result in one
    or more Encounter(s).
    """
    
    resource_type = "Appointment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appointmentType = None
        """ The style of appointment or patient that has been booked in the
        slot (not service type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.comment = None
        """ Additional comments.
        Type `str`. """
        
        self.created = None
        """ The date that this appointment was initially created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Shown on a subject line in a meeting request, or appointment list.
        Type `str`. """
        
        self.end = None
        """ When appointment is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.incomingReferral = None
        """ The ReferralRequest provided as information to allocate to the
        Encounter.
        List of `FHIRReference` items referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason the appointment is to takes place (resource).
        List of `FHIRReference` items referencing `Condition, Procedure` (represented as `dict` in JSON). """
        
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
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.requestedPeriod = None
        """ Potential date/time interval(s) requested to allocate the
        appointment within.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ A broad categorisation of the service that is to be performed
        during this appointment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ The specific service that is to be performed during this
        appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.slot = None
        """ The slots that this appointment is filling.
        List of `FHIRReference` items referencing `Slot` (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.start = None
        """ When appointment is to take place.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ proposed | pending | booked | arrived | fulfilled | cancelled |
        noshow | entered-in-error.
        Type `str`. """
        
        self.supportingInformation = None
        """ Additional information to support the appointment.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(Appointment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("end", "end", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("incomingReferral", "incomingReferral", fhirreference.FHIRReference, True, None, False),
            ("indication", "indication", fhirreference.FHIRReference, True, None, False),
            ("minutesDuration", "minutesDuration", int, False, None, False),
            ("participant", "participant", AppointmentParticipant, True, None, True),
            ("priority", "priority", int, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("requestedPeriod", "requestedPeriod", period.Period, True, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("slot", "slot", fhirreference.FHIRReference, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("start", "start", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class AppointmentParticipant(backboneelement.BackboneElement):
    """ Participants involved in appointment.
    
    List of participants involved in the appointment.
    """
    
    resource_type = "AppointmentParticipant"
    
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


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
