# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/PaymentNotice).
# 2024, SMART Health IT.


from . import domainresource

class PaymentNotice(domainresource.DomainResource):
    """ PaymentNotice request.
    
    This resource provides the status of the payment for goods and services
    rendered, and the request and response resource references.
    """
    
    resource_type = "PaymentNotice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Monetary amount of the payment.
        Type `Money` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for the payment noctice.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.payee = None
        """ Party being paid.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._payee = None
        """ Primitive extension for payee. Type `FHIRPrimitiveExtension` """
        
        self.payment = None
        """ Payment reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._payment = None
        """ Primitive extension for payment. Type `FHIRPrimitiveExtension` """
        
        self.paymentDate = None
        """ Payment or clearing date.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._paymentDate = None
        """ Primitive extension for paymentDate. Type `FHIRPrimitiveExtension` """
        
        self.paymentStatus = None
        """ Issued or cleared Status of the payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._paymentStatus = None
        """ Primitive extension for paymentStatus. Type `FHIRPrimitiveExtension` """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.recipient = None
        """ Party being notified.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recipient = None
        """ Primitive extension for recipient. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._response = None
        """ Primitive extension for response. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("_payee", "_payee", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payment", "payment", fhirreference.FHIRReference, False, None, True),
            ("_payment", "_payment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("_paymentDate", "_paymentDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentStatus", "paymentStatus", codeableconcept.CodeableConcept, False, None, False),
            ("_paymentStatus", "_paymentStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, True),
            ("_recipient", "_recipient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("_response", "_response", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money