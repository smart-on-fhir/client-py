#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/PaymentNotice) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import domainresource
import fhirdate
import fhirreference
import identifier


class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.
    
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    
    resource_name = "PaymentNotice"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.paymentStatus = None
        """ Status of the payment.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
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
        """ Insurer or Regulatory body.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(PaymentNotice, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PaymentNotice, self).update_with_json(jsondict)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'paymentStatus' in jsondict:
            self.paymentStatus = coding.Coding.with_json_and_owner(jsondict['paymentStatus'], self)
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

