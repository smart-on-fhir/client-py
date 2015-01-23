#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (reversal.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class Reversal(fhirresource.FHIRResource):
    """ Reversal request.
    
    This resource provides the request and response details for the request for
    which all actions are to be reversed or terminated.
    """
    
    resource_name = "Reversal"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.coverage = None
        """ Insurance or medical plan.
        Type `ReversalCoverage` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.nullify = False
        """ Nullify.
        Type `bool`. """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `ReversalPayee` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `OralHealthClaim, PharmacyClaim, VisionClaim, ProfessionalClaim, InstitutionalClaim, SupportingDocumentation` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` referencing `ClaimResponse, StatusResponse` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.target = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(Reversal, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Reversal, self).update_with_json(jsondict)
        if 'coverage' in jsondict:
            self.coverage = ReversalCoverage.with_json_and_owner(jsondict['coverage'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'nullify' in jsondict:
            self.nullify = jsondict['nullify']
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'payee' in jsondict:
            self.payee = ReversalPayee.with_json_and_owner(jsondict['payee'], self)
        if 'provider' in jsondict:
            self.provider = fhirreference.FHIRReference.with_json_and_owner(jsondict['provider'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'response' in jsondict:
            self.response = fhirreference.FHIRReference.with_json_and_owner(jsondict['response'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)


class ReversalCoverage(fhirelement.FHIRElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_name = "ReversalCoverage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.focal = False
        """ Is the focal Coverage.
        Type `bool`. """
        
        self.relationship = None
        """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        super(ReversalCoverage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ReversalCoverage, self).update_with_json(jsondict)
        if 'businessArrangement' in jsondict:
            self.businessArrangement = jsondict['businessArrangement']
        if 'coverage' in jsondict:
            self.coverage = fhirreference.FHIRReference.with_json_and_owner(jsondict['coverage'], self)
        if 'focal' in jsondict:
            self.focal = jsondict['focal']
        if 'relationship' in jsondict:
            self.relationship = coding.Coding.with_json_and_owner(jsondict['relationship'], self)
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']


class ReversalPayee(fhirelement.FHIRElement):
    """ Payee.
    
    Payee information supplied for matching purposes.
    """
    
    resource_name = "ReversalPayee"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.organization = None
        """ Organization who is the payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.person = None
        """ Other person who is the payee.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Provider who is the payee.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None
        """ Payee Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ReversalPayee, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ReversalPayee, self).update_with_json(jsondict)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'person' in jsondict:
            self.person = fhirreference.FHIRReference.with_json_and_owner(jsondict['person'], self)
        if 'provider' in jsondict:
            self.provider = fhirreference.FHIRReference.with_json_and_owner(jsondict['provider'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

