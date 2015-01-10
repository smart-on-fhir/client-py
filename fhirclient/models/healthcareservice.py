#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (healthcareservice.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import contactpoint
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class HealthcareService(fhirresource.FHIRResource):
    """ The details of a Healthcare Service available at a location.
    """
    
    resource_name = "HealthcareService"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.appointmentRequired = None
        """ Indicates whether or not a prospective consumer will require an
        appointment for a particular service at a Site to be provided by
        the Organization. Indicates if an appointment is required for
        access to this service. If this flag is 'NotDefined', then this
        flag is overridden by the Site's availability flag.
        (ConditionalIndicator Enum).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.availabilityExceptions = None
        """ A description of Site availability exceptions, e.g., public holiday
        availability. Succinctly describing all possible exceptions to
        normal Site availability as details in the Available Times and Not
        Available Times.
        Type `str`. """
        
        self.availableTime = None
        """ A Collection of times that the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.catchmentArea = None
        """ Need better description.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.characteristic = None
        """ Collection of Characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.comment = None
        """ Additional description of the  or any specific issues not covered
        by the other attributes, which can be displayed as further detail
        under the serviceName.
        Type `str`. """
        
        self.contactPoint = None
        """ List of contacts related to this specific healthcare service. If
        this is empty, then refer to the location's contacts.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.coverageArea = None
        """ Need better description.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
        
        self.freeProvisionCode = None
        """ The free provision code provides a link to the Free Provision
        reference entity to enable the selection of one free provision type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.imageURI = None
        """ If there is an image associated with this Service Site, its URI can
        be included here.
        Type `str`. """
        
        self.location = None
        """ The location where this healthcare service may be provided.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.notAvailableTime = None
        """ Not avail times - need better description.
        List of `HealthcareServiceNotAvailableTime` items (represented as `dict` in JSON). """
        
        self.programName = None
        """ Program Names that can be used to categorize the service.
        List of `str` items. """
        
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
        
        self.serviceCode = None
        """ List of the specific.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceName = None
        """ Further description of the service as it would be presented to a
        consumer while searching.
        Type `str`. """
        
        self.serviceType = None
        """ A specific type of service that may be delivered or performed.
        List of `HealthcareServiceServiceType` items (represented as `dict` in JSON). """
        
        self.setting = None
        """ The setting where this service can be provided, such is in home, or
        at location in organisation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.targetGroup = None
        """ Collection of Target Groups for the Service Site (The target
        audience that this service is for).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(HealthcareService, self).update_with_json(jsondict)
        if 'appointmentRequired' in jsondict:
            self.appointmentRequired = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['appointmentRequired'], self)
        if 'availabilityExceptions' in jsondict:
            self.availabilityExceptions = jsondict['availabilityExceptions']
        if 'availableTime' in jsondict:
            self.availableTime = HealthcareServiceAvailableTime.with_json_and_owner(jsondict['availableTime'], self)
        if 'catchmentArea' in jsondict:
            self.catchmentArea = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['catchmentArea'], self)
        if 'characteristic' in jsondict:
            self.characteristic = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['characteristic'], self)
        if 'comment' in jsondict:
            self.comment = jsondict['comment']
        if 'contactPoint' in jsondict:
            self.contactPoint = contactpoint.ContactPoint.with_json_and_owner(jsondict['contactPoint'], self)
        if 'coverageArea' in jsondict:
            self.coverageArea = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['coverageArea'], self)
        if 'eligibility' in jsondict:
            self.eligibility = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['eligibility'], self)
        if 'eligibilityNote' in jsondict:
            self.eligibilityNote = jsondict['eligibilityNote']
        if 'extraDetails' in jsondict:
            self.extraDetails = jsondict['extraDetails']
        if 'freeProvisionCode' in jsondict:
            self.freeProvisionCode = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['freeProvisionCode'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'imageURI' in jsondict:
            self.imageURI = jsondict['imageURI']
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'notAvailableTime' in jsondict:
            self.notAvailableTime = HealthcareServiceNotAvailableTime.with_json_and_owner(jsondict['notAvailableTime'], self)
        if 'programName' in jsondict:
            self.programName = jsondict['programName']
        if 'publicKey' in jsondict:
            self.publicKey = jsondict['publicKey']
        if 'referralMethod' in jsondict:
            self.referralMethod = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['referralMethod'], self)
        if 'serviceCategory' in jsondict:
            self.serviceCategory = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['serviceCategory'], self)
        if 'serviceCode' in jsondict:
            self.serviceCode = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['serviceCode'], self)
        if 'serviceName' in jsondict:
            self.serviceName = jsondict['serviceName']
        if 'serviceType' in jsondict:
            self.serviceType = HealthcareServiceServiceType.with_json_and_owner(jsondict['serviceType'], self)
        if 'setting' in jsondict:
            self.setting = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['setting'], self)
        if 'targetGroup' in jsondict:
            self.targetGroup = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['targetGroup'], self)


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
        """ The closing time of day (the date is not included). Note: If the
        AllDay flag is set, then this time is ignored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.availableStartTime = None
        """ The opening time of day (the date is not included). Note: If the
        AllDay flag is set, then this time is ignored.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None
        """ Indicates which Days of the week are available between the Start
        and End Times.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
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
            self.daysOfWeek = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['daysOfWeek'], self)


class HealthcareServiceNotAvailableTime(fhirelement.FHIRElement):
    """ Not avail times - need better description.
    """
    
    resource_name = "HealthcareServiceNotAvailableTime"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ The reason that can be presented to the user as to why this time is
        not available.
        Type `str`. """
        
        self.endDate = None
        """ Service is not available (seasonally or for a public holiday) until
        this date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.startDate = None
        """ Service is not available (seasonally or for a public holiday) from
        this date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(HealthcareServiceNotAvailableTime, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(HealthcareServiceNotAvailableTime, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'endDate' in jsondict:
            self.endDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['endDate'], self)
        if 'startDate' in jsondict:
            self.startDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['startDate'], self)


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

