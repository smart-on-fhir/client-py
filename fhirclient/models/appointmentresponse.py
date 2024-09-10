# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse).
# 2024, SMART Health IT.


from . import domainresource

class AppointmentResponse(domainresource.DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    
    resource_type = "AppointmentResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Person, Location, HealthcareService, or Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.appointment = None
        """ Appointment this response relates to.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._appointment = None
        """ Primitive extension for appointment. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Additional comments.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.end = None
        """ Time from appointment, or requested new end time.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.participantStatus = None
        """ accepted | declined | tentative | needs-action.
        Type `str`. """
        self._participantStatus = None
        """ Primitive extension for participantStatus. Type `FHIRPrimitiveExtension` """
        
        self.participantType = None
        """ Role of participant in the appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._participantType = None
        """ Primitive extension for participantType. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ Time from appointment, or requested new start time.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        super(AppointmentResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(AppointmentResponse, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, False),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("appointment", "appointment", fhirreference.FHIRReference, False, None, True),
            ("_appointment", "_appointment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("end", "end", fhirinstant.FHIRInstant, False, None, False),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantStatus", "participantStatus", str, False, None, True),
            ("_participantStatus", "_participantStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participantType", "participantType", codeableconcept.CodeableConcept, True, None, False),
            ("_participantType", "_participantType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", fhirinstant.FHIRInstant, False, None, False),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirinstant
from . import fhirreference
from . import identifier