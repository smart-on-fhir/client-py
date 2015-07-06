#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2015-07-06.
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
    """ The details of a Healthcare Service available at a location.
    """
    
    resource_name = "HealthcareService"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.appointmentRequired = None
        """ Indicates if an appointment is required for access to this service.
        Type `bool`. """
        
        self.availabilityExceptions = None
        """ A description of Site availability exceptions, e.g., public holiday
        availability. Succinctly describing all possible exceptions to
        normal Site availability as details in the Available Times and Not
        Available Times.
        Type `str`. """
        
        self.availableTime = None
        """ A Collection of times that the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ Collection of Characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.comment = None
        """ Any additional description of the service and/or any specific
        issues not covered by the other attributes, which can be displayed
        as further detail under the serviceName.
        Type `str`. """
        
        self.coverageArea = None
        """ The location(s) that this service is available to (not where the
        service is provided).
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.eligibility = None
        """ Does this service have specific eligibility requirements that need
        to be met in order to use the service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.eligibilityNote = None
        """ Describes the eligibility conditions for the service.
        Type `str`. """
        
        self.extraDetails = None
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
        
        self.identifier = None
        """ External Identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ The location where this healthcare service may be provided.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.notAvailable = None
        """ The HealthcareService is not available during this period of time
        due to the provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        
        self.photo = None
        """ If there is a photo/symbol associated with this HealthcareService,
        it may be included here to facilitate quick identification of the
        service in a list.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.programName = None
        """ Program Names that can be used to categorize the service.
        List of `str` items. """
        
        self.providedBy = None
        """ The organization that provides this Healthcare Service.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.publicKey = None
        """ The public part of the 'keys' allocated to an Organization by an
        accredited body to support secure exchange of data over the
        internet. To be provided by the Organization, where available.
        Type `str`. """
        
        self.referralMethod = None
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ Identifies the broad category of service being performed or
        delivered. Selecting a Service Category then determines the list of
        relevant service types that can be selected in the Primary Service
        Type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceName = None
        """ Further description of the service as it would be presented to a
        consumer while searching.
        Type `str`. """
        
        self.serviceProvisionCode = None
        """ The code(s) that detail the conditions under which the healthcare
        service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None
        """ A specific type of service that may be delivered or performed.
        List of `HealthcareServiceServiceType` items (represented as `dict` in JSON). """
        
        self.telecom = None
        """ List of contacts related to this specific healthcare service. If
        this is empty, then refer to the location's contacts.
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
    """ A Collection of times that the Service Site is available.
    """
    
    resource_name = "HealthcareServiceAvailableTime"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.allDay = None
        """ Is this always available? (hence times are irrelevant) e.g. 24 hour
        service.
        Type `bool`. """
        
        self.availableEndTime = None
        """ The closing time of day. Note: If the AllDay flag is set, then this
        time is ignored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.availableStartTime = None
        """ The opening time of day. Note: If the AllDay flag is set, then this
        time is ignored.
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
    """ The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    
    resource_name = "HealthcareServiceNotAvailable"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ The reason that can be presented to the user as to why this time is
        not available.
        Type `str`. """
        
        self.during = None
        """ Service is not available (seasonally or for a public holiday) from
        this date.
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
    """ A specific type of service that may be delivered or performed.
    """
    
    resource_name = "HealthcareServiceServiceType"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.specialty = None
        """ Collection of Specialties handled by the Service Site. This is more
        of a Medical Term.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ The specific type of service being delivered or performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(HealthcareServiceServiceType, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(HealthcareServiceServiceType, self).elementProperties()
        js.extend([
            ("specialty", "specialty", codeableconcept.CodeableConcept, True),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

