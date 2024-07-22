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
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier for the payment noctice.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.payee = None
        """ Party being paid.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.payment = None
        """ Payment reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.paymentDate = None
        """ Payment or clearing date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.paymentStatus = None
        """ Issued or cleared Status of the payment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Party being notified.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.request = None
        """ Request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.response = None
        """ Response reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(PaymentNotice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(PaymentNotice, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, True),
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("payee", "payee", fhirreference.FHIRReference, False, None, False),
            ("payment", "payment", fhirreference.FHIRReference, False, None, True),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("paymentStatus", "paymentStatus", codeableconcept.CodeableConcept, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
