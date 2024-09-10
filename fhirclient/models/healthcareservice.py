# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/HealthcareService).
# 2024, SMART Health IT.


from . import domainresource

class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    
    resource_type = "HealthcareService"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this HealthcareService record is in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.appointmentRequired = None
        """ If an appointment is required for access to this service.
        Type `bool`. """
        self._appointmentRequired = None
        """ Primitive extension for appointmentRequired. Type `FHIRPrimitiveExtension` """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """
        self._availabilityExceptions = None
        """ Primitive extension for availabilityExceptions. Type `FHIRPrimitiveExtension` """
        
        self.availableTime = None
        """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        self._availableTime = None
        """ Primitive extension for availableTime. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Broad category of service being performed or delivered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.characteristic = None
        """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._characteristic = None
        """ Primitive extension for characteristic. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.communication = None
        """ The language that this service is offered in.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._communication = None
        """ Primitive extension for communication. Type `FHIRPrimitiveExtension` """
        
        self.coverageArea = None
        """ Location(s) service is intended for/available to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._coverageArea = None
        """ Primitive extension for coverageArea. Type `FHIRPrimitiveExtension` """
        
        self.eligibility = None
        """ Specific eligibility requirements required to use the service.
        List of `HealthcareServiceEligibility` items (represented as `dict` in JSON). """
        self._eligibility = None
        """ Primitive extension for eligibility. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Technical endpoints providing access to electronic services
        operated for the healthcare service.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.extraDetails = None
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
        self._extraDetails = None
        """ Primitive extension for extraDetails. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Location(s) where service may be provided.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Description of service as presented to a consumer while searching.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.notAvailable = None
        """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        self._notAvailable = None
        """ Primitive extension for notAvailable. Type `FHIRPrimitiveExtension` """
        
        self.photo = None
        """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """
        self._photo = None
        """ Primitive extension for photo. Type `FHIRPrimitiveExtension` """
        
        self.program = None
        """ Programs that this service is applicable to.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._program = None
        """ Primitive extension for program. Type `FHIRPrimitiveExtension` """
        
        self.providedBy = None
        """ Organization that provides this service.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._providedBy = None
        """ Primitive extension for providedBy. Type `FHIRPrimitiveExtension` """
        
        self.referralMethod = None
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._referralMethod = None
        """ Primitive extension for referralMethod. Type `FHIRPrimitiveExtension` """
        
        self.serviceProvisionCode = None
        """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._serviceProvisionCode = None
        """ Primitive extension for serviceProvisionCode. Type `FHIRPrimitiveExtension` """
        
        self.specialty = None
        """ Specialties handled by the HealthcareService.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._specialty = None
        """ Primitive extension for specialty. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of service that may be delivered or performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("_appointmentRequired", "_appointmentRequired", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("_availabilityExceptions", "_availabilityExceptions", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("_availableTime", "_availableTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("_characteristic", "_characteristic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("communication", "communication", codeableconcept.CodeableConcept, True, None, False),
            ("_communication", "_communication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("_coverageArea", "_coverageArea", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("eligibility", "eligibility", HealthcareServiceEligibility, True, None, False),
            ("_eligibility", "_eligibility", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("_extraDetails", "_extraDetails", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("_notAvailable", "_notAvailable", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("_photo", "_photo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("program", "program", codeableconcept.CodeableConcept, True, None, False),
            ("_program", "_program", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False),
            ("_providedBy", "_providedBy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False),
            ("_referralMethod", "_referralMethod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False),
            ("_serviceProvisionCode", "_serviceProvisionCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("_specialty", "_specialty", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times that the Service Site is available.
    """
    
    resource_type = "HealthcareServiceAvailableTime"
    
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
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
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


class HealthcareServiceEligibility(backboneelement.BackboneElement):
    """ Specific eligibility requirements required to use the service.
    
    Does this service have specific eligibility requirements that need to be
    met in order to use the service?
    """
    
    resource_type = "HealthcareServiceEligibility"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Coded value for the eligibility.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Describes the eligibility conditions for the service.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        super(HealthcareServiceEligibility, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceEligibility, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    
    resource_type = "HealthcareServiceNotAvailable"
    
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
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("during", "during", period.Period, False, None, False),
            ("_during", "_during", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import fhirtime
from . import identifier
from . import period