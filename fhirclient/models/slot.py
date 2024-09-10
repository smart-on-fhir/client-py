# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Slot).
# 2024, SMART Health IT.


from . import domainresource

class Slot(domainresource.DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    
    resource_type = "Slot"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appointmentType = None
        """ The style of appointment or patient that may be booked in the slot
        (not service type).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._appointmentType = None
        """ Primitive extension for appointmentType. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.end = None
        """ Date/Time that the slot is to conclude.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._end = None
        """ Primitive extension for end. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.overbooked = None
        """ This slot has already been overbooked, appointments are unlikely to
        be accepted for this time.
        Type `bool`. """
        self._overbooked = None
        """ Primitive extension for overbooked. Type `FHIRPrimitiveExtension` """
        
        self.schedule = None
        """ The schedule resource that this slot defines an interval of status
        information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._schedule = None
        """ Primitive extension for schedule. Type `FHIRPrimitiveExtension` """
        
        self.serviceCategory = None
        """ A broad categorization of the service that is to be performed
        during this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._serviceCategory = None
        """ Primitive extension for serviceCategory. Type `FHIRPrimitiveExtension` """
        
        self.serviceType = None
        """ The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location,
        rather than the location itself). If provided then this overrides
        the value provided on the availability resource.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._serviceType = None
        """ Primitive extension for serviceType. Type `FHIRPrimitiveExtension` """
        
        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._specialty = None
        """ Primitive extension for specialty. Type `FHIRPrimitiveExtension` """
        
        self.start = None
        """ Date/Time that the slot is to begin.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._start = None
        """ Primitive extension for start. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ busy | free | busy-unavailable | busy-tentative | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(Slot, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend([
            ("appointmentType", "appointmentType", codeableconcept.CodeableConcept, False, None, False),
            ("_appointmentType", "_appointmentType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("end", "end", fhirinstant.FHIRInstant, False, None, True),
            ("_end", "_end", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("overbooked", "overbooked", bool, False, None, False),
            ("_overbooked", "_overbooked", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("schedule", "schedule", fhirreference.FHIRReference, False, None, True),
            ("_schedule", "_schedule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, True, None, False),
            ("_serviceCategory", "_serviceCategory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceType", "serviceType", codeableconcept.CodeableConcept, True, None, False),
            ("_serviceType", "_serviceType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("_specialty", "_specialty", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("start", "start", fhirinstant.FHIRInstant, False, None, True),
            ("_start", "_start", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirinstant
from . import fhirreference
from . import identifier