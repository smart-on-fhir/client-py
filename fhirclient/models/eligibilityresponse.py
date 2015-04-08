#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/EligibilityResponse) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import domainresource
import fhirdate
import fhirreference
import identifier


class EligibilityResponse(domainresource.DomainResource):
    """ EligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """
    
    resource_name = "EligibilityResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error.
        Type `str`. """
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` referencing `EligibilityRequest` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(EligibilityResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(EligibilityResponse, self).update_with_json(jsondict)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'disposition' in jsondict:
            self.disposition = jsondict['disposition']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'requestOrganization' in jsondict:
            self.requestOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestOrganization'], self)
        if 'requestProvider' in jsondict:
            self.requestProvider = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestProvider'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)

