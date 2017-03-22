#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class ClaimResponse(domainresource.DomainResource):
    """ Remittance resource.
    
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    
    resource_type = "ClaimResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.addItem = None
        """ Insurer added line items.
        List of `ClaimResponseAddItem` items (represented as `dict` in JSON). """
        
        self.communicationRequest = None
        """ Request for additional information.
        List of `FHIRReference` items referencing `CommunicationRequest` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.error = None
        """ Processing errors.
        List of `ClaimResponseError` items (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Response  number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.insurance = None
        """ Insurance or medical plan.
        List of `ClaimResponseInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ Insurance issuing organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.item = None
        """ Line items.
        List of `ClaimResponseItem` items (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error | partial.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.payeeType = None
        """ Party to be paid any benefits payable.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.payment = None
        """ Payment details, if paid.
        Type `ClaimResponsePayment` (represented as `dict` in JSON). """
        
        self.processNote = None
        """ Processing notes.
        List of `ClaimResponseProcessNote` items (represented as `dict` in JSON). """
        
        self.request = None
        """ Id of resource triggering adjudication.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reserved = None
        """ Funds reserved status.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        self.totalBenefit = None
        """ Total benefit payable for the Claim.
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalCost = None
        """ Total Cost of service from the Claim.
        Type `Money` (represented as `dict` in JSON). """
        
        self.unallocDeductable = None
        """ Unallocated deductible.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("addItem", "addItem", ClaimResponseAddItem, True, None, False),
            ("communicationRequest", "communicationRequest", fhirreference.FHIRReference, True, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", ClaimResponseError, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("insurance", "insurance", ClaimResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("item", "item", ClaimResponseItem, True, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("payeeType", "payeeType", codeableconcept.CodeableConcept, False, None, False),
            ("payment", "payment", ClaimResponsePayment, False, None, False),
            ("processNote", "processNote", ClaimResponseProcessNote, True, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("reserved", "reserved", coding.Coding, False, None, False),
            ("status", "status", str, False, None, False),
            ("totalBenefit", "totalBenefit", money.Money, False, None, False),
            ("totalCost", "totalCost", money.Money, False, None, False),
            ("unallocDeductable", "unallocDeductable", money.Money, False, None, False),
        ])
        return js


from . import backboneelement

class ClaimResponseAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first tier service adjudications for payor added services.
    """
    
    resource_type = "ClaimResponseAddItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Added items details.
        List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Money` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.noteNumber = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.sequenceLinkId = None
        """ Service instances.
        List of `int` items. """
        
        self.service = None
        """ Group, Service or Product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("detail", "detail", ClaimResponseAddItemDetail, True, None, False),
            ("fee", "fee", money.Money, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("sequenceLinkId", "sequenceLinkId", int, True, None, False),
            ("service", "service", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimResponseAddItemDetail(backboneelement.BackboneElement):
    """ Added items details.
    
    The second tier service adjudications for payor added services.
    """
    
    resource_type = "ClaimResponseAddItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Added items detail adjudication.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.category = None
        """ Type of service or product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Money` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.noteNumber = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.revenue = None
        """ Revenue or cost center code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.service = None
        """ Service or Product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("fee", "fee", money.Money, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("revenue", "revenue", codeableconcept.CodeableConcept, False, None, False),
            ("service", "service", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    resource_type = "ClaimResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.detailSequenceLinkId = None
        """ Detail sequence number.
        Type `int`. """
        
        self.sequenceLinkId = None
        """ Item sequence number.
        Type `int`. """
        
        self.subdetailSequenceLinkId = None
        """ Subdetail sequence number.
        Type `int`. """
        
        super(ClaimResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("detailSequenceLinkId", "detailSequenceLinkId", int, False, None, False),
            ("sequenceLinkId", "sequenceLinkId", int, False, None, False),
            ("subdetailSequenceLinkId", "subdetailSequenceLinkId", int, False, None, False),
        ])
        return js


class ClaimResponseInsurance(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_type = "ClaimResponseInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
        """ Business agreement.
        Type `str`. """
        
        self.claimResponse = None
        """ Adjudication results.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.focal = None
        """ Is the focal Coverage.
        Type `bool`. """
        
        self.preAuthRef = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.sequence = None
        """ Service instance identifier.
        Type `int`. """
        
        super(ClaimResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("focal", "focal", bool, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ClaimResponseItem(backboneelement.BackboneElement):
    """ Line items.
    
    The first tier service adjudications for submitted services.
    """
    
    resource_type = "ClaimResponseItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Detail line items.
        List of `ClaimResponseItemDetail` items (represented as `dict` in JSON). """
        
        self.noteNumber = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        super(ClaimResponseItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("detail", "detail", ClaimResponseItemDetail, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("sequenceLinkId", "sequenceLinkId", int, False, None, True),
        ])
        return js


class ClaimResponseItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    The adjudication results.
    """
    
    resource_type = "ClaimResponseItemAdjudication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.category = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Explanation of Adjudication outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monetary value.
        Type `float`. """
        
        super(ClaimResponseItemAdjudication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class ClaimResponseItemDetail(backboneelement.BackboneElement):
    """ Detail line items.
    
    The second tier service adjudications for submitted services.
    """
    
    resource_type = "ClaimResponseItemDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Detail level adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.noteNumber = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        self.subDetail = None
        """ Subdetail line items.
        List of `ClaimResponseItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        super(ClaimResponseItemDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("sequenceLinkId", "sequenceLinkId", int, False, None, True),
            ("subDetail", "subDetail", ClaimResponseItemDetailSubDetail, True, None, False),
        ])
        return js


class ClaimResponseItemDetailSubDetail(backboneelement.BackboneElement):
    """ Subdetail line items.
    
    The third tier service adjudications for submitted services.
    """
    
    resource_type = "ClaimResponseItemDetailSubDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjudication = None
        """ Subdetail level adjudication details.
        List of `ClaimResponseItemAdjudication` items (represented as `dict` in JSON). """
        
        self.noteNumber = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        super(ClaimResponseItemDetailSubDetail, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("sequenceLinkId", "sequenceLinkId", int, False, None, True),
        ])
        return js


class ClaimResponsePayment(backboneelement.BackboneElement):
    """ Payment details, if paid.
    
    Payment details for the claim if the claim has been paid.
    """
    
    resource_type = "ClaimResponsePayment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.adjustment = None
        """ Payment adjustment for non-Claim issues.
        Type `Money` (represented as `dict` in JSON). """
        
        self.adjustmentReason = None
        """ Explanation for the non-claim adjustment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.amount = None
        """ Payable amount after adjustment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.date = None
        """ Expected data of Payment.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Identifier of the payment instrument.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ Partial or Complete.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponsePayment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponsePayment, self).elementProperties()
        js.extend([
            ("adjustment", "adjustment", money.Money, False, None, False),
            ("adjustmentReason", "adjustmentReason", codeableconcept.CodeableConcept, False, None, False),
            ("amount", "amount", money.Money, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class ClaimResponseProcessNote(backboneelement.BackboneElement):
    """ Processing notes.
    
    Note text.
    """
    
    resource_type = "ClaimResponseProcessNote"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None
        """ Language if different from the resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.number = None
        """ Sequence Number for this note.
        Type `int`. """
        
        self.text = None
        """ Note explanatory text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ClaimResponseProcessNote, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ClaimResponseProcessNote, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, False, None, False),
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + '.coding']
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
