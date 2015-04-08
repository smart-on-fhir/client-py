#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ProcessResponse) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class ProcessResponse(domainresource.DomainResource):
    """ ProcessResponse resource.
    
    This resource provides processing status, errors and notes from the
    processing of a resource.
    """
    
    resource_name = "ProcessResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.error = None
        """ Error code.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Notes.
        List of `ProcessResponseNotes` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Authoring Organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ Processing outcome.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible Practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProcessResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProcessResponse, self).update_with_json(jsondict)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'disposition' in jsondict:
            self.disposition = jsondict['disposition']
        if 'error' in jsondict:
            self.error = coding.Coding.with_json_and_owner(jsondict['error'], self)
        if 'form' in jsondict:
            self.form = coding.Coding.with_json_and_owner(jsondict['form'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'notes' in jsondict:
            self.notes = ProcessResponseNotes.with_json_and_owner(jsondict['notes'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'outcome' in jsondict:
            self.outcome = coding.Coding.with_json_and_owner(jsondict['outcome'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'requestOrganization' in jsondict:
            self.requestOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestOrganization'], self)
        if 'requestProvider' in jsondict:
            self.requestProvider = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestProvider'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)


class ProcessResponseNotes(fhirelement.FHIRElement):
    """ Notes.
    
    Suite of processing note or additional requirements is the processing has
    been held.
    """
    
    resource_name = "ProcessResponseNotes"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.text = None
        """ Notes text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProcessResponseNotes, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProcessResponseNotes, self).update_with_json(jsondict)
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

