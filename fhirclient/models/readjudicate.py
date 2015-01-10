#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (readjudicate.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class Readjudicate(fhirresource.FHIRResource):
    """ Readjudicate request.
    
    This resource provides the request and line items details for the claim
    which is to be re-adjudicated.
    """
    
    resource_name = "Readjudicate"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Items to re-adjudicate.
        List of `ReadjudicateItem` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Reference number/string.
        Type `str`. """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.target = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(Readjudicate, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Readjudicate, self).update_with_json(jsondict)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'item' in jsondict:
            self.item = ReadjudicateItem.with_json_and_owner(jsondict['item'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'provider' in jsondict:
            self.provider = fhirreference.FHIRReference.with_json_and_owner(jsondict['provider'], self)
        if 'reference' in jsondict:
            self.reference = jsondict['reference']
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'response' in jsondict:
            self.response = fhirreference.FHIRReference.with_json_and_owner(jsondict['response'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)


class ReadjudicateItem(fhirelement.FHIRElement):
    """ Items to re-adjudicate.
    
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """
    
    resource_name = "ReadjudicateItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        super(ReadjudicateItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ReadjudicateItem, self).update_with_json(jsondict)
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']

