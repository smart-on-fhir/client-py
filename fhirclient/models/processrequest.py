#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ProcessRequest) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period


class ProcessRequest(domainresource.DomainResource):
    """ Process request.
    
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """
    
    resource_name = "ProcessRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ cancel | poll | reprocess | status.
        Type `str`. """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exclude = None
        """ Resource type(s) to exclude.
        List of `str` items. """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.include = None
        """ Resource type(s) to include.
        List of `str` items. """
        
        self.item = None
        """ Items to re-adjudicate.
        List of `ProcessRequestItem` items (represented as `dict` in JSON). """
        
        self.nullify = False
        """ Nullify.
        Type `bool`. """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period.
        Type `Period` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Reference number/string.
        Type `str`. """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.target = None
        """ Target of the request.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(ProcessRequest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProcessRequest, self).update_with_json(jsondict)
        if 'action' in jsondict:
            self.action = jsondict['action']
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'exclude' in jsondict:
            self.exclude = jsondict['exclude']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'include' in jsondict:
            self.include = jsondict['include']
        if 'item' in jsondict:
            self.item = ProcessRequestItem.with_json_and_owner(jsondict['item'], self)
        if 'nullify' in jsondict:
            self.nullify = jsondict['nullify']
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
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


class ProcessRequestItem(fhirelement.FHIRElement):
    """ Items to re-adjudicate.
    
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """
    
    resource_name = "ProcessRequestItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        super(ProcessRequestItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProcessRequestItem, self).update_with_json(jsondict)
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']

