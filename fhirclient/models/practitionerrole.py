# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PractitionerRole).
# 2024, SMART Health IT.


from . import domainresource

class PractitionerRole(domainresource.DomainResource):
    """ Roles/organizations the practitioner is associated with.
    
    A specific set of Roles/Locations/specialties/services that a practitioner
    may perform at an organization for a period of time.
    """
    
    resource_type = "PractitionerRole"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this practitioner role record is in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """
        self._availabilityExceptions = None
        """ Primitive extension for availabilityExceptions. Type `FHIRPrimitiveExtension` """
        
        self.availableTime = None
        """ Times the Service Site is available.
        List of `PractitionerRoleAvailableTime` items (represented as `dict` in JSON). """
        self._availableTime = None
        """ Primitive extension for availableTime. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Roles which this practitioner may perform.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        practitioner with this role.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.healthcareService = None
        """ The list of healthcare services that this worker provides for this
        role's Organization/Location(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._healthcareService = None
        """ Primitive extension for healthcareService. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifiers that are specific to a role/location.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ The location(s) at which this practitioner provides care.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.notAvailable = None
        """ Not available during this time due to provided reason.
        List of `PractitionerRoleNotAvailable` items (represented as `dict` in JSON). """
        self._notAvailable = None
        """ Primitive extension for notAvailable. Type `FHIRPrimitiveExtension` """
        
        self.organization = None
        """ Organization where the roles are available.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._organization = None
        """ Primitive extension for organization. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ The period during which the practitioner is authorized to perform
        in these role(s).
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.practitioner = None
        """ Practitioner that is able to provide the defined services for the
        organization.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._practitioner = None
        """ Primitive extension for practitioner. Type `FHIRPrimitiveExtension` """
        
        self.specialty = None
        """ Specific specialty of the practitioner.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._specialty = None
        """ Primitive extension for specialty. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ Contact details that are specific to the role/location/service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        super(PractitionerRole, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRole, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("_availabilityExceptions", "_availabilityExceptions", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("availableTime", "availableTime", PractitionerRoleAvailableTime, True, None, False),
            ("_availableTime", "_availableTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, True, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("healthcareService", "healthcareService", fhirreference.FHIRReference, True, None, False),
            ("_healthcareService", "_healthcareService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("notAvailable", "notAvailable", PractitionerRoleNotAvailable, True, None, False),
            ("_notAvailable", "_notAvailable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("_organization", "_organization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("practitioner", "practitioner", fhirreference.FHIRReference, False, None, False),
            ("_practitioner", "_practitioner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("_specialty", "_specialty", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class PractitionerRoleAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times the practitioner is available or performing this role
    at the location and/or healthcareservice.
    """
    
    resource_type = "PractitionerRoleAvailableTime"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None
        """ Always available? e.g. 24 hour service.
        Type `bool`. """
        self._allDay = None
        """ Primitive extension for allDay. Type `FHIRPrimitiveExtension` """
        
        self.availableEndTime = None
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRTime` (represented as `str` in JSON). """
        self._availableEndTime = None
        """ Primitive extension for availableEndTime. Type `FHIRPrimitiveExtension` """
        
        self.availableStartTime = None
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRTime` (represented as `str` in JSON). """
        self._availableStartTime = None
        """ Primitive extension for availableStartTime. Type `FHIRPrimitiveExtension` """
        
        self.daysOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        self._daysOfWeek = None
        """ Primitive extension for daysOfWeek. Type `FHIRPrimitiveExtension` """
        
        super(PractitionerRoleAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRoleAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("_allDay", "_allDay", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("availableEndTime", "availableEndTime", fhirtime.FHIRTime, False, None, False),
            ("_availableEndTime", "_availableEndTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("availableStartTime", "availableStartTime", fhirtime.FHIRTime, False, None, False),
            ("_availableStartTime", "_availableStartTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
            ("_daysOfWeek", "_daysOfWeek", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class PractitionerRoleNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The practitioner is not available or performing this role during this
    period of time due to the provided reason.
    """
    
    resource_type = "PractitionerRoleNotAvailable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Reason presented to the user explaining why time not available.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.during = None
        """ Service not available from this date.
        Type `Period` (represented as `dict` in JSON). """
        self._during = None
        """ Primitive extension for during. Type `FHIRPrimitiveExtension` """
        
        super(PractitionerRoleNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PractitionerRoleNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("during", "during", period.Period, False, None, False),
            ("_during", "_during", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import fhirtime
from . import identifier
from . import period