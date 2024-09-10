# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Appointment).
# 2024, SMART Health IT.


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
        self._appointmentType = None
        """ Primitive extension for appointmentType. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ The service request this appointment is allocated to assess.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.cancelationReason = None
        """ The coded reason for the appointment being cancelled.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._cancelationReason = None
        """ Primitive extension for cancelationReason. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Additional comments.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.created = None
        """ The date that this appointment was initially created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Shown on a subject line in a meeting request, or appointment list.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.end = None
        """ When appointment is to conclude.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.minutesDuration = None
        """ Can be less than start/end (e.g. estimate).
        Type `int`. """
        self._minutesDuration = None
        """ Primitive extension for minutesDuration. Type `FHIRPrimitiveExtension` """
        
        self.participant = None
        """ Participants involved in appointment.
        List of `AppointmentParticipant` items (represented as `dict` in JSON). """
        self._participant = None
        """ Primitive extension for participant. Type `FHIRPrimitiveExtension` """
        
        self.patientInstruction = None
        """ Detailed information and instructions for the patient.
        Type `str`. """
        self._patientInstruction = None
        """ Primitive extension for patientInstruction. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ Used to make informed decisions if needing to re-prioritize.
        Type `int`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Coded reason this appointment is scheduled.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Reason the appointment is to take place (resource).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.requestedPeriod = None
        """ Potential date/time interval(s) requested to allocate the
        appointment within.
        List of `Period` items (represented as `dict` in JSON). """
        self._requestedPeriod = None
        """ Primitive extension for requestedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.serviceCategory = None
        """ A broad categorization of the service that is to be performed
        during this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._serviceCategory = None
        """ Primitive extension for serviceCategory. Type `FHIRPrimitiveExtension` """
        
        self.serviceType = None
        """ The specific service that is to be performed during this
        appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._serviceType = None
        """ Primitive extension for serviceType. Type `FHIRPrimitiveExtension` """
        
        self.slot = None
        """ The slots that this appointment is filling.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._slot = None
        """ Primitive extension for slot. Type `FHIRPrimitiveExtension` """
        
        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._specialty = None
        """ Primitive extension for specialty. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ When appointment is to take place.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ proposed | pending | booked | arrived | fulfilled | cancelled |
        noshow | entered-in-error | checked-in | waitlist.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.supportingInformation = None
        """ Additional information to support the appointment.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._supportingInformation = None
        """ Primitive extension for supportingInformation. Type `FHIRPrimitiveExtension` """
        
        super(Appointment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Appointment, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False),
            ("_appointmentType", "_appointmentType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("cancelationReason", "cancelationReason", codeableconcept.CodeableConcept, False, None, False),
            ("_cancelationReason", "_cancelationReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, False),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("end", "end", fhirinstant.FHIRInstant, False, None, False),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minutesDuration", "minutesDuration", int, False, None, False),
            ("_minutesDuration", "_minutesDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participant", "participant", AppointmentParticipant, True, None, True),
            ("_participant", "_participant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patientInstruction", "patientInstruction", str, False, None, False),
            ("_patientInstruction", "_patientInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", int, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestedPeriod", "requestedPeriod", period.Period, True, None, False),
            ("_requestedPeriod", "_requestedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("_serviceCategory", "_serviceCategory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("_serviceType", "_serviceType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("slot", "slot", fhirreference.FHIRReference, True, None, False),
            ("_slot", "_slot", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("_specialty", "_specialty", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", fhirinstant.FHIRInstant, False, None, False),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True, None, False),
            ("_supportingInformation", "_supportingInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Participation period of the actor.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.required = None
        """ required | optional | information-only.
        Type `str`. """
        self._required = None
        """ Primitive extension for required. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ accepted | declined | tentative | needs-action.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(AppointmentParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AppointmentParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("required", "required", str, False, None, False),
            ("_required", "_required", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import period