#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation) on 2019-05-07.
#  2019, SMART Health IT.


from . import domainresource

class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.
    
    This resource provides the details including amount of a payment and
    allocates the payment items being paid.
    """
    
    resource_type = "PaymentReconciliation"
    
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
        """ Settlement particulars.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        
        self.disposition = None
        """ Disposition message.
        Type `str`. """
        
        self.formCode = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier for a payment reconciliation.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `str`. """
        
        self.paymentAmount = None
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentDate = None
        """ When payment issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.paymentIdentifier = None
        """ Business identifier for the payment.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.paymentIssuer = None
        """ Party generating payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.period = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        
        self.processNote = None
        """ Note concerning processing.
        List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON). """
        
        self.request = None
        """ Reference to requesting resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.requestor = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, True),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("paymentAmount", "paymentAmount", money.Money, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, True),
            ("paymentIdentifier", "paymentIdentifier", identifier.Identifier, False, None, False),
            ("paymentIssuer", "paymentIssuer", fhirreference.FHIRReference, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ Settlement particulars.
    
    Distribution of the payment amount for a previously acknowledged payable.
    """
    
    resource_type = "PaymentReconciliationDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Amount allocated to this payable.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date of commitment to pay.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business identifier of the payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Recipient of the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.predecessor = None
        """ Business identifier of the prior payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request giving rise to the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response committing to a payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Contact for the response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.submitter = None
        """ Submitter of the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.type = None
        """ Category of payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("predecessor", "predecessor", identifier.Identifier, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Note concerning processing.
    
    A note that describes or explains the processing in a human readable form.
    """
    
    resource_type = "PaymentReconciliationProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.text = None
        """ Note explanatory text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `str`. """
        
        super(PaymentReconciliationProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + '.money']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
