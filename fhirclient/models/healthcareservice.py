#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2017-03-22.
#  2017, SMART Health IT.


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
        """ Whether this healthcareservice is in active use.
        Type `bool`. """
        
        self.appointmentRequired = None
        """ If an appointment is required for access to this service.
        Type `bool`. """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """
        
        self.availableTime = None
        """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Broad category of service being performed or delivered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.comment = None
        """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `str`. """
        
        self.coverageArea = None
        """ Location(s) service is inteded for/available to.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.eligibility = None
        """ Specific eligibility requirements required to use the service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.eligibilityNote = None
        """ Describes the eligibility conditions for the service.
        Type `str`. """
        
        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        location.
        List of `FHIRReference` items referencing `Endpoint` (represented as `dict` in JSON). """
        
        self.extraDetails = None
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
        
        self.identifier = None
        """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Location(s) where service may be provided.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.name = None
        """ Description of service as presented to a consumer while searching.
        Type `str`. """
        
        self.notAvailable = None
        """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.programName = None
        """ Program Names that categorize the service.
        List of `str` items. """
        
        self.providedBy = None
        """ Organization that provides this service.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.referralMethod = None
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceProvisionCode = None
        """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ Specialties handled by the HealthcareService.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of service that may be delivered or performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("eligibility", "eligibility", codeableconcept.CodeableConcept, False, None, False),
            ("eligibilityNote", "eligibilityNote", str, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, True, None, False),
            ("name", "name", str, False, None, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("programName", "programName", str, True, None, False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False),
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
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
        
        self.availableEndTime = None
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.availableStartTime = None
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
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
        
        self.during = None
        """ Service not availablefrom this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
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
