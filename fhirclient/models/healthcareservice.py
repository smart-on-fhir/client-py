#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2015-09-24.
#  2015, SMART Health IT.


from . import attachment
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period


class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    
    resource_name = "HealthcareService"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.appointmentRequired = None
        """ If an appointment is required for access to this service.
        Type `bool`. """
        
        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """
        
        self.availableTime = None
        """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
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
        
        self.extraDetails = None
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
        
        self.identifier = None
        """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Location where service may be provided.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
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
        
        self.publicKey = None
        """ PKI Public keys to support secure communications.
        Type `str`. """
        
        self.referralMethod = None
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ Broad category of service being performed or delivered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceName = None
        """ Description of service as presented to a consumer while searching.
        Type `str`. """
        
        self.serviceProvisionCode = None
        """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ Specific service delivered or performed.
        List of `HealthcareServiceServiceType` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("appointmentRequired", "appointmentRequired", bool, False),
            ("availabilityExceptions", "availabilityExceptions", str, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True),
            ("comment", "comment", str, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True),
            ("eligibility", "eligibility", codeableconcept.CodeableConcept, False),
            ("eligibilityNote", "eligibilityNote", str, False),
            ("extraDetails", "extraDetails", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("location", "location", fhirreference.FHIRReference, False),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True),
            ("photo", "photo", attachment.Attachment, False),
            ("programName", "programName", str, True),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False),
            ("publicKey", "publicKey", str, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, False),
            ("serviceName", "serviceName", str, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True),
            ("serviceType", "serviceType", HealthcareServiceServiceType, True),
            ("telecom", "telecom", contactpoint.ContactPoint, True),
        ])
        return js


class HealthcareServiceAvailableTime(fhirelement.FHIRElement):
    """ Times the Service Site is available.
    
    A collection of times that the Service Site is available.
    """
    
    resource_name = "HealthcareServiceAvailableTime"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False),
            ("daysOfWeek", "daysOfWeek", str, True),
        ])
        return js


class HealthcareServiceNotAvailable(fhirelement.FHIRElement):
    """ Not available during this time due to provided reason.
    
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    
    resource_name = "HealthcareServiceNotAvailable"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Reason presented to the user explaining why time not available.
        Type `str`. """
        
        self.during = None
        """ Service not availablefrom this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False),
            ("during", "during", period.Period, False),
        ])
        return js


class HealthcareServiceServiceType(fhirelement.FHIRElement):
    """ Specific service delivered or performed.
    
    A specific type of service that may be delivered or performed.
    """
    
    resource_name = "HealthcareServiceServiceType"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.specialty = None
        """ Specialties handled by the Service Site.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of service delivered or performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(HealthcareServiceServiceType, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(HealthcareServiceServiceType, self).elementProperties()
        js.extend([
            ("specialty", "specialty", codeableconcept.CodeableConcept, True),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

