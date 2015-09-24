#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2015-09-24.
#  2015, SMART Health IT.


from . import coding
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity


class PaymentReconciliation(domainresource.DomainResource):
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
        Type `FHIRReference` referencing `ProcessRequest` (represented as `dict` in JSON). """
        
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
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(PaymentReconciliation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False),
            ("detail", "detail", PaymentReconciliationDetail, True),
            ("disposition", "disposition", str, False),
            ("form", "form", coding.Coding, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("note", "note", PaymentReconciliationNote, True),
            ("organization", "organization", fhirreference.FHIRReference, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False),
            ("outcome", "outcome", str, False),
            ("period", "period", period.Period, False),
            ("request", "request", fhirreference.FHIRReference, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False),
            ("ruleset", "ruleset", coding.Coding, False),
            ("total", "total", quantity.Quantity, False),
        ])
        return js


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
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.request = None
        """ Claim.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.responce = None
        """ Claim Response.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.submitter = None
        """ Submitter.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("payee", "payee", fhirreference.FHIRReference, False),
            ("request", "request", fhirreference.FHIRReference, False),
            ("responce", "responce", fhirreference.FHIRReference, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False),
            ("type", "type", coding.Coding, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(PaymentReconciliationNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False),
            ("type", "type", coding.Coding, False),
        ])
        return js

