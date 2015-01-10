#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (paymentreconciliation.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import money
import period


class PaymentReconciliation(fhirresource.FHIRResource):
    """ PaymentReconciliation resource.
    
    This resource provides payment details and claim references supporting a
    bulk payment.
    """
    
    resource_name = "PaymentReconciliation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Details.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Note text.
        List of `PaymentReconciliationNote` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error.
        Type `str`. """
        
        self.period = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` referencing `PendedRequest` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.total = None
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """
        
        super(PaymentReconciliation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PaymentReconciliation, self).update_with_json(jsondict)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'detail' in jsondict:
            self.detail = PaymentReconciliationDetail.with_json_and_owner(jsondict['detail'], self)
        if 'disposition' in jsondict:
            self.disposition = jsondict['disposition']
        if 'form' in jsondict:
            self.form = coding.Coding.with_json_and_owner(jsondict['form'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'note' in jsondict:
            self.note = PaymentReconciliationNote.with_json_and_owner(jsondict['note'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'requestOrganization' in jsondict:
            self.requestOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestOrganization'], self)
        if 'requestProvider' in jsondict:
            self.requestProvider = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestProvider'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)
        if 'total' in jsondict:
            self.total = money.Money.with_json_and_owner(jsondict['total'], self)


class PaymentReconciliationDetail(fhirelement.FHIRElement):
    """ Details.
    
    List of individual settlement amounts and the corresponding transaction.
    """
    
    resource_name = "PaymentReconciliationDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Detail amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.request = None
        """ Claim.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.responce = None
        """ Claim Response.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.submitter = None
        """ Submitter.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PaymentReconciliationDetail, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'payee' in jsondict:
            self.payee = fhirreference.FHIRReference.with_json_and_owner(jsondict['payee'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'responce' in jsondict:
            self.responce = fhirreference.FHIRReference.with_json_and_owner(jsondict['responce'], self)
        if 'submitter' in jsondict:
            self.submitter = fhirreference.FHIRReference.with_json_and_owner(jsondict['submitter'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)


class PaymentReconciliationNote(fhirelement.FHIRElement):
    """ Note text.
    
    Suite of notes.
    """
    
    resource_name = "PaymentReconciliationNote"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.text = None
        """ Notes text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationNote, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(PaymentReconciliationNote, self).update_with_json(jsondict)
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

