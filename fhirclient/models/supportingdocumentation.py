#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (supportingdocumentation.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import attachment
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class SupportingDocumentation(fhirresource.FHIRResource):
    """ Documentation submission.
    
    This resource provides the supporting information for a process, for
    example clinical or financial  information related to a claim or pre-
    authorization.
    """
    
    resource_name = "SupportingDocumentation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Supporting Files.
        List of `SupportingDocumentationDetail` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.target = None
        """ Insurer or Provider.
        Type `FHIRReference` referencing `Organization, Practitioner` (represented as `dict` in JSON). """
        
        super(SupportingDocumentation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SupportingDocumentation, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'detail' in jsondict:
            self.detail = SupportingDocumentationDetail.with_json_and_owner(jsondict['detail'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'provider' in jsondict:
            self.provider = fhirreference.FHIRReference.with_json_and_owner(jsondict['provider'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'response' in jsondict:
            self.response = fhirreference.FHIRReference.with_json_and_owner(jsondict['response'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)


class SupportingDocumentationDetail(fhirelement.FHIRElement):
    """ Supporting Files.
    """
    
    resource_name = "SupportingDocumentationDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentAttachment = None
        """ Content.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Content.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ Creation date and time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.linkId = None
        """ LinkId.
        Type `int`. """
        
        super(SupportingDocumentationDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SupportingDocumentationDetail, self).update_with_json(jsondict)
        if 'contentAttachment' in jsondict:
            self.contentAttachment = attachment.Attachment.with_json_and_owner(jsondict['contentAttachment'], self)
        if 'contentReference' in jsondict:
            self.contentReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['contentReference'], self)
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateTime'], self)
        if 'linkId' in jsondict:
            self.linkId = jsondict['linkId']

