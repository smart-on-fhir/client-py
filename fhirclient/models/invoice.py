# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Invoice).
# 2024, SMART Health IT.


from . import domainresource

class Invoice(domainresource.DomainResource):
    """ Invoice containing ChargeItems from an Account.
    
    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """
    
    resource_type = "Invoice"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.account = None
        """ Account that is being balanced.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.cancelledReason = None
        """ Reason for cancellation of this Invoice.
        Type `str`. """
        
        self.date = None
        """ Invoice date / posting date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Business Identifier for item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issuer = None
        """ Issuing Organization of Invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.lineItem = None
        """ Line items of this Invoice.
        List of `InvoiceLineItem` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the invoice.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.participant = None
        """ Participant in creation of this Invoice.
        List of `InvoiceParticipant` items (represented as `dict` in JSON). """
        
        self.paymentTerms = None
        """ Payment details.
        Type `str`. """
        
        self.recipient = None
        """ Recipient of this invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | issued | balanced | cancelled | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Recipient(s) of goods and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.totalGross = None
        """ Gross total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalNet = None
        """ Net total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalPriceComponent = None
        """ Components of Invoice total.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Invoice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Invoice, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, False, None, False),
            ("cancelledReason", "cancelledReason", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("lineItem", "lineItem", InvoiceLineItem, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("participant", "participant", InvoiceParticipant, True, None, False),
            ("paymentTerms", "paymentTerms", str, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("totalGross", "totalGross", money.Money, False, None, False),
            ("totalNet", "totalNet", money.Money, False, None, False),
            ("totalPriceComponent", "totalPriceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class InvoiceLineItem(backboneelement.BackboneElement):
    """ Line items of this Invoice.
    
    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """
    
    resource_type = "InvoiceLineItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.chargeItemCodeableConcept = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.chargeItemReference = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.priceComponent = None
        """ Components of total line item price.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Sequence number of line item.
        Type `int`. """
        
        super(InvoiceLineItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend([
            ("chargeItemCodeableConcept", "chargeItemCodeableConcept", codeableconcept.CodeableConcept, False, "chargeItem", True),
            ("chargeItemReference", "chargeItemReference", fhirreference.FHIRReference, False, "chargeItem", True),
            ("priceComponent", "priceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("sequence", "sequence", int, False, None, False),
        ])
        return js


class InvoiceLineItemPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.
    
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
    """
    
    resource_type = "InvoiceLineItemPriceComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Monetary amount associated with this component.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Code identifying the specific component.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Factor used for calculating this component.
        Type `float`. """
        
        self.type = None
        """ base | surcharge | deduction | discount | tax | informational.
        Type `str`. """
        
        super(InvoiceLineItemPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


class InvoiceParticipant(backboneelement.BackboneElement):
    """ Participant in creation of this Invoice.
    
    Indicates who or what performed or participated in the charged service.
    """
    
    resource_type = "InvoiceParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.actor = None
        """ Individual who was involved.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.role = None
        """ Type of involvement in creation of this Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(InvoiceParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
