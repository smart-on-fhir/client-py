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
        self._account = None
        """ Primitive extension for account. Type `FHIRPrimitiveExtension` """
        
        self.cancelledReason = None
        """ Reason for cancellation of this Invoice.
        Type `str`. """
        self._cancelledReason = None
        """ Primitive extension for cancelledReason. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Invoice date / posting date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for item.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.issuer = None
        """ Issuing Organization of Invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._issuer = None
        """ Primitive extension for issuer. Type `FHIRPrimitiveExtension` """
        
        self.lineItem = None
        """ Line items of this Invoice.
        List of `InvoiceLineItem` items (represented as `dict` in JSON). """
        self._lineItem = None
        """ Primitive extension for lineItem. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments made about the invoice.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.participant = None
        """ Participant in creation of this Invoice.
        List of `InvoiceParticipant` items (represented as `dict` in JSON). """
        self._participant = None
        """ Primitive extension for participant. Type `FHIRPrimitiveExtension` """
        
        self.paymentTerms = None
        """ Payment details.
        Type `str`. """
        self._paymentTerms = None
        """ Primitive extension for paymentTerms. Type `FHIRPrimitiveExtension` """
        
        self.recipient = None
        """ Recipient of this invoice.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._recipient = None
        """ Primitive extension for recipient. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | issued | balanced | cancelled | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Recipient(s) of goods and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.totalGross = None
        """ Gross total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        self._totalGross = None
        """ Primitive extension for totalGross. Type `FHIRPrimitiveExtension` """
        
        self.totalNet = None
        """ Net total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """
        self._totalNet = None
        """ Primitive extension for totalNet. Type `FHIRPrimitiveExtension` """
        
        self.totalPriceComponent = None
        """ Components of Invoice total.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        self._totalPriceComponent = None
        """ Primitive extension for totalPriceComponent. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Invoice, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Invoice, self).elementProperties()
        js.extend([
            ("account", "account", fhirreference.FHIRReference, False, None, False),
            ("_account", "_account", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("cancelledReason", "cancelledReason", str, False, None, False),
            ("_cancelledReason", "_cancelledReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("_issuer", "_issuer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lineItem", "lineItem", InvoiceLineItem, True, None, False),
            ("_lineItem", "_lineItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("participant", "participant", InvoiceParticipant, True, None, False),
            ("_participant", "_participant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("paymentTerms", "paymentTerms", str, False, None, False),
            ("_paymentTerms", "_paymentTerms", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, False, None, False),
            ("_recipient", "_recipient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("totalGross", "totalGross", money.Money, False, None, False),
            ("_totalGross", "_totalGross", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("totalNet", "totalNet", money.Money, False, None, False),
            ("_totalNet", "_totalNet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("totalPriceComponent", "totalPriceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("_totalPriceComponent", "_totalPriceComponent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._chargeItemCodeableConcept = None
        """ Primitive extension for chargeItemCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.chargeItemReference = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._chargeItemReference = None
        """ Primitive extension for chargeItemReference. Type `FHIRPrimitiveExtension` """
        
        self.priceComponent = None
        """ Components of total line item price.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """
        self._priceComponent = None
        """ Primitive extension for priceComponent. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Sequence number of line item.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        super(InvoiceLineItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend([
            ("chargeItemCodeableConcept", "chargeItemCodeableConcept", codeableconcept.CodeableConcept, False, "chargeItem", True),
            ("_chargeItemCodeableConcept", "_chargeItemCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("chargeItemReference", "chargeItemReference", fhirreference.FHIRReference, False, "chargeItem", True),
            ("_chargeItemReference", "_chargeItemReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priceComponent", "priceComponent", InvoiceLineItemPriceComponent, True, None, False),
            ("_priceComponent", "_priceComponent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code identifying the specific component.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Factor used for calculating this component.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ base | surcharge | deduction | discount | tax | informational.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(InvoiceLineItemPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._actor = None
        """ Primitive extension for actor. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ Type of involvement in creation of this Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        super(InvoiceParticipant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False, None, True),
            ("_actor", "_actor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, False),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money