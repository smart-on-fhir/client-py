# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PaymentReconciliation).
# 2024, SMART Health IT.


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
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Settlement particulars.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.disposition = None
        """ Disposition message.
        Type `str`. """
        self._disposition = None
        """ Primitive extension for disposition. Type `FHIRPrimitiveExtension` """
        
        self.formCode = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._formCode = None
        """ Primitive extension for formCode. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for a payment reconciliation.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `str`. """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.paymentAmount = None
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """
        self._paymentAmount = None
        """ Primitive extension for paymentAmount. Type `FHIRPrimitiveExtension` """
        
        self.paymentDate = None
        """ When payment issued.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._paymentDate = None
        """ Primitive extension for paymentDate. Type `FHIRPrimitiveExtension` """
        
        self.paymentIdentifier = None
        """ Business identifier for the payment.
        Type `Identifier` (represented as `dict` in JSON). """
        self._paymentIdentifier = None
        """ Primitive extension for paymentIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.paymentIssuer = None
        """ Party generating payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._paymentIssuer = None
        """ Primitive extension for paymentIssuer. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.processNote = None
        """ Note concerning processing.
        List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON). """
        self._processNote = None
        """ Primitive extension for processNote. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Reference to requesting resource.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.requestor = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requestor = None
        """ Primitive extension for requestor. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", PaymentReconciliationDetail, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("formCode", "formCode", codeableconcept.CodeableConcept, False, None, False),
            ("_formCode", "_formCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentAmount", "paymentAmount", money.Money, False, None, True),
            ("_paymentAmount", "_paymentAmount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, True),
            ("_paymentDate", "_paymentDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentIdentifier", "paymentIdentifier", identifier.Identifier, False, None, False),
            ("_paymentIdentifier", "_paymentIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentIssuer", "paymentIssuer", fhirreference.FHIRReference, False, None, False),
            ("_paymentIssuer", "_paymentIssuer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("processNote", "processNote", PaymentReconciliationProcessNote, True, None, False),
            ("_processNote", "_processNote", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("_requestor", "_requestor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date of commitment to pay.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier of the payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.payee = None
        """ Recipient of the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._payee = None
        """ Primitive extension for payee. Type `FHIRPrimitiveExtension` """
        
        self.predecessor = None
        """ Business identifier of the prior payment detail.
        Type `Identifier` (represented as `dict` in JSON). """
        self._predecessor = None
        """ Primitive extension for predecessor. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Request giving rise to the payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.response = None
        """ Response committing to a payment.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._response = None
        """ Primitive extension for response. Type `FHIRPrimitiveExtension` """
        
        self.responsible = None
        """ Contact for the response.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._responsible = None
        """ Primitive extension for responsible. Type `FHIRPrimitiveExtension` """
        
        self.submitter = None
        """ Submitter of the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._submitter = None
        """ Primitive extension for submitter. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Category of payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(PaymentReconciliationDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("_payee", "_payee", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("predecessor", "predecessor", identifier.Identifier, False, None, False),
            ("_predecessor", "_predecessor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("_response", "_response", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("_responsible", "_responsible", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("submitter", "submitter", fhirreference.FHIRReference, False, None, False),
            ("_submitter", "_submitter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ display | print | printoper.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(PaymentReconciliationProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
        js.extend([
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period