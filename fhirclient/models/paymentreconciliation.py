#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8522 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2016-06-16.
#  2016, SMART Health IT.


from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    
    This resource provides payment details and claim references supporting a
    bulk payment.
    """
    
    resource_name = "PaymentReconciliation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        self.organizationIdentifier = None
        """ Insurer.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error | partial.
        Type `str`. """
        
        self.period = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.requestIdentifier = None
        """ Claim reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationIdentifier = None
        """ Responsible organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationReference = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProviderIdentifier = None
        """ Responsible practitioner.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestProviderReference = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.requestReference = None
        """ Claim reference.
        Type `FHIRReference` referencing `ProcessRequest` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.total = None
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("form", "form", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("note", "note", PaymentReconciliationNote, True, None, False),
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, "request", False),
            ("requestOrganizationIdentifier", "requestOrganizationIdentifier", identifier.Identifier, False, "requestOrganization", False),
            ("requestOrganizationReference", "requestOrganizationReference", fhirreference.FHIRReference, False, "requestOrganization", False),
            ("requestProviderIdentifier", "requestProviderIdentifier", identifier.Identifier, False, "requestProvider", False),
            ("requestProviderReference", "requestProviderReference", fhirreference.FHIRReference, False, "requestProvider", False),
            ("requestReference", "requestReference", fhirreference.FHIRReference, False, "request", False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("total", "total", money.Money, False, None, True),
        ])
        return js


from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Details.
    
    List of individual settlement amounts and the corresponding transaction.
    """
    
    resource_name = "PaymentReconciliationDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Detail amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payeeIdentifier = None
        """ Payee.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.payeeReference = None
        """ Payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestIdentifier = None
        """ Claim.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestReference = None
        """ Claim.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.responceIdentifier = None
        """ Claim Response.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.responceReference = None
        """ Claim Response.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.submitterIdentifier = None
        """ Submitter.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.submitterReference = None
        """ Submitter.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("payeeIdentifier", "payeeIdentifier", identifier.Identifier, False, "payee", False),
            ("payeeReference", "payeeReference", fhirreference.FHIRReference, False, "payee", False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, "request", False),
            ("requestReference", "requestReference", fhirreference.FHIRReference, False, "request", False),
            ("responceIdentifier", "responceIdentifier", identifier.Identifier, False, "responce", False),
            ("responceReference", "responceReference", fhirreference.FHIRReference, False, "responce", False),
            ("submitterIdentifier", "submitterIdentifier", identifier.Identifier, False, "submitter", False),
            ("submitterReference", "submitterReference", fhirreference.FHIRReference, False, "submitter", False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class PaymentReconciliationNote(backboneelement.BackboneElement):
    """ Note text.
    
    Suite of notes.
    """
    
    resource_name = "PaymentReconciliationNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ Notes text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import money
from . import period
