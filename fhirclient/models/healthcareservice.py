#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2015-04-08.
#  2015, SMART Health IT.


import attachment
import codeableconcept
import contactpoint
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period


class HealthcareService(domainresource.DomainResource):
    """ The details of a Healthcare Service available at a location.
    """
    
    resource_name = "HealthcareService"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.appointmentRequired = False
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
    
    def update_with_json(self, jsondict):
        super(HealthcareService, self).update_with_json(jsondict)
        if 'appointmentRequired' in jsondict:
            self.appointmentRequired = jsondict['appointmentRequired']
        if 'availabilityExceptions' in jsondict:
            self.availabilityExceptions = jsondict['availabilityExceptions']
        if 'availableTime' in jsondict:
            self.availableTime = HealthcareServiceAvailableTime.with_json_and_owner(jsondict['availableTime'], self)
        if 'characteristic' in jsondict:
            self.characteristic = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['characteristic'], self)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'coverageArea' in jsondict:
            self.coverageArea = fhirreference.FHIRReference.with_json_and_owner(jsondict['coverageArea'], self)
        if 'eligibility' in jsondict:
            self.eligibility = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['eligibility'], self)
        if 'eligibilityNote' in jsondict:
            self.eligibilityNote = jsondict['eligibilityNote']
        if 'extraDetails' in jsondict:
            self.extraDetails = jsondict['extraDetails']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'notAvailable' in jsondict:
            self.notAvailable = HealthcareServiceNotAvailable.with_json_and_owner(jsondict['notAvailable'], self)
        if 'photo' in jsondict:
            self.photo = attachment.Attachment.with_json_and_owner(jsondict['photo'], self)
        if 'programName' in jsondict:
            self.programName = jsondict['programName']
        if 'providedBy' in jsondict:
            self.providedBy = fhirreference.FHIRReference.with_json_and_owner(jsondict['providedBy'], self)
        if 'publicKey' in jsondict:
            self.publicKey = jsondict['publicKey']
        if 'referralMethod' in jsondict:
            self.referralMethod = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['referralMethod'], self)
        if 'serviceCategory' in jsondict:
            self.serviceCategory = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['serviceCategory'], self)
        if 'serviceName' in jsondict:
            self.serviceName = jsondict['serviceName']
        if 'serviceProvisionCode' in jsondict:
            self.serviceProvisionCode = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['serviceProvisionCode'], self)
        if 'serviceType' in jsondict:
            self.serviceType = HealthcareServiceServiceType.with_json_and_owner(jsondict['serviceType'], self)
        if 'telecom' in jsondict:
            self.telecom = contactpoint.ContactPoint.with_json_and_owner(jsondict['telecom'], self)


class HealthcareServiceAvailableTime(fhirelement.FHIRElement):
    """ A Collection of times that the Service Site is available.
    """
    
    resource_name = "HealthcareServiceAvailableTime"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.allDay = False
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
    
    def update_with_json(self, jsondict):
        super(HealthcareServiceAvailableTime, self).update_with_json(jsondict)
        if 'allDay' in jsondict:
            self.allDay = jsondict['allDay']
        if 'availableEndTime' in jsondict:
            self.availableEndTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['availableEndTime'], self)
        if 'availableStartTime' in jsondict:
            self.availableStartTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['availableStartTime'], self)
        if 'daysOfWeek' in jsondict:
            self.daysOfWeek = jsondict['daysOfWeek']


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
    
    def update_with_json(self, jsondict):
        super(HealthcareServiceNotAvailable, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'during' in jsondict:
            self.during = period.Period.with_json_and_owner(jsondict['during'], self)


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
    
    def update_with_json(self, jsondict):
        super(HealthcareServiceServiceType, self).update_with_json(jsondict)
        if 'specialty' in jsondict:
            self.specialty = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['specialty'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

