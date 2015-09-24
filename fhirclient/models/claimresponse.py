#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2015-09-24.
#  2015, SMART Health IT.


from . import coding
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity


class ClaimResponse(domainresource.DomainResource):
    """ Remittance resource.
    
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    
    resource_name = "ClaimResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.addItem = None
        """ Insurer added line items.
        List of `ClaimResponseAddItem` items (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance or medical plan.
        List of `ClaimResponseCoverage` items (represented as `dict` in JSON). """
        
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
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Response  number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Line items.
        List of `ClaimResponseItem` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Processing notes.
        List of `ClaimResponseNote` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error.
        Type `str`. """
        
        self.payeeType = None
        """ Party to be paid any benefits payable.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.paymentAdjustment = None
        """ Payment adjustment for non-Claim issues.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.paymentAdjustmentReason = None
        """ Reason for Payment adjustment.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.paymentAmount = None
        """ Payment amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.paymentDate = None
        """ Expected data of Payment.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.paymentRef = None
        """ Payment identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
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
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.totalBenefit = None
        """ Total benefit payable for the Claim.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.totalCost = None
        """ Total Cost of service from the Claim.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.unallocDeductable = None
        """ Unallocated deductible.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponse, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponse, self).elementProperties()
        js.extend([
            ("addItem", "addItem", ClaimResponseAddItem, True),
            ("coverage", "coverage", ClaimResponseCoverage, True),
            ("created", "created", fhirdate.FHIRDate, False),
            ("disposition", "disposition", str, False),
            ("error", "error", ClaimResponseError, True),
            ("form", "form", coding.Coding, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("item", "item", ClaimResponseItem, True),
            ("note", "note", ClaimResponseNote, True),
            ("organization", "organization", fhirreference.FHIRReference, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False),
            ("outcome", "outcome", str, False),
            ("payeeType", "payeeType", coding.Coding, False),
            ("paymentAdjustment", "paymentAdjustment", quantity.Quantity, False),
            ("paymentAdjustmentReason", "paymentAdjustmentReason", coding.Coding, False),
            ("paymentAmount", "paymentAmount", quantity.Quantity, False),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False),
            ("paymentRef", "paymentRef", identifier.Identifier, False),
            ("request", "request", fhirreference.FHIRReference, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False),
            ("reserved", "reserved", coding.Coding, False),
            ("ruleset", "ruleset", coding.Coding, False),
            ("totalBenefit", "totalBenefit", quantity.Quantity, False),
            ("totalCost", "totalCost", quantity.Quantity, False),
            ("unallocDeductable", "unallocDeductable", quantity.Quantity, False),
        ])
        return js


class ClaimResponseAddItem(fhirelement.FHIRElement):
    """ Insurer added line items.
    
    The first tier service adjudications for payor added services.
    """
    
    resource_name = "ClaimResponseAddItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ClaimResponseAddItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Added items details.
        List of `ClaimResponseAddItemDetail` items (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.noteNumberLinkId = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.sequenceLinkId = None
        """ Service instances.
        List of `int` items. """
        
        self.service = None
        """ Group, Service or Product.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseAddItemAdjudication, True),
            ("detail", "detail", ClaimResponseAddItemDetail, True),
            ("fee", "fee", quantity.Quantity, False),
            ("noteNumberLinkId", "noteNumberLinkId", int, True),
            ("sequenceLinkId", "sequenceLinkId", int, True),
            ("service", "service", coding.Coding, False),
        ])
        return js


class ClaimResponseAddItemAdjudication(fhirelement.FHIRElement):
    """ Added items adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseAddItemAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monetary value.
        Type `float`. """
        
        super(ClaimResponseAddItemAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("code", "code", coding.Coding, False),
            ("value", "value", float, False),
        ])
        return js


class ClaimResponseAddItemDetail(fhirelement.FHIRElement):
    """ Added items details.
    
    The second tier service adjudications for payor added services.
    """
    
    resource_name = "ClaimResponseAddItemDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Added items detail adjudication.
        List of `ClaimResponseAddItemDetailAdjudication` items (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.service = None
        """ Service or Product.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItemDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseAddItemDetailAdjudication, True),
            ("fee", "fee", quantity.Quantity, False),
            ("service", "service", coding.Coding, False),
        ])
        return js


class ClaimResponseAddItemDetailAdjudication(fhirelement.FHIRElement):
    """ Added items detail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseAddItemDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monetary value.
        Type `float`. """
        
        super(ClaimResponseAddItemDetailAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseAddItemDetailAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("code", "code", coding.Coding, False),
            ("value", "value", float, False),
        ])
        return js


class ClaimResponseCoverage(fhirelement.FHIRElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_name = "ClaimResponseCoverage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.relationship = None
        """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance identifier.
        Type `int`. """
        
        super(ClaimResponseCoverage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseCoverage, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False),
            ("focal", "focal", bool, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False),
            ("preAuthRef", "preAuthRef", str, True),
            ("relationship", "relationship", coding.Coding, False),
            ("sequence", "sequence", int, False),
        ])
        return js


class ClaimResponseError(fhirelement.FHIRElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    resource_name = "ClaimResponseError"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.detailSequenceLinkId = None
        """ Detail sequence number.
        Type `int`. """
        
        self.sequenceLinkId = None
        """ Item sequence number.
        Type `int`. """
        
        self.subdetailSequenceLinkId = None
        """ Subdetail sequence number.
        Type `int`. """
        
        super(ClaimResponseError, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseError, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False),
            ("detailSequenceLinkId", "detailSequenceLinkId", int, False),
            ("sequenceLinkId", "sequenceLinkId", int, False),
            ("subdetailSequenceLinkId", "subdetailSequenceLinkId", int, False),
        ])
        return js


class ClaimResponseItem(fhirelement.FHIRElement):
    """ Line items.
    
    The first tier service adjudications for submitted services.
    """
    
    resource_name = "ClaimResponseItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(ClaimResponseItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemAdjudication, True),
            ("detail", "detail", ClaimResponseItemDetail, True),
            ("noteNumber", "noteNumber", int, True),
            ("sequenceLinkId", "sequenceLinkId", int, False),
        ])
        return js


class ClaimResponseItemAdjudication(fhirelement.FHIRElement):
    """ Adjudication details.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseItemAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monetary value.
        Type `float`. """
        
        super(ClaimResponseItemAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("code", "code", coding.Coding, False),
            ("value", "value", float, False),
        ])
        return js


class ClaimResponseItemDetail(fhirelement.FHIRElement):
    """ Detail line items.
    
    The second tier service adjudications for submitted services.
    """
    
    resource_name = "ClaimResponseItemDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Detail adjudication.
        List of `ClaimResponseItemDetailAdjudication` items (represented as `dict` in JSON). """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        self.subDetail = None
        """ Subdetail line items.
        List of `ClaimResponseItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        super(ClaimResponseItemDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemDetailAdjudication, True),
            ("sequenceLinkId", "sequenceLinkId", int, False),
            ("subDetail", "subDetail", ClaimResponseItemDetailSubDetail, True),
        ])
        return js


class ClaimResponseItemDetailAdjudication(fhirelement.FHIRElement):
    """ Detail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseItemDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monetary value.
        Type `float`. """
        
        super(ClaimResponseItemDetailAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetailAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("code", "code", coding.Coding, False),
            ("value", "value", float, False),
        ])
        return js


class ClaimResponseItemDetailSubDetail(fhirelement.FHIRElement):
    """ Subdetail line items.
    
    The third tier service adjudications for submitted services.
    """
    
    resource_name = "ClaimResponseItemDetailSubDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Subdetail adjudication.
        List of `ClaimResponseItemDetailSubDetailAdjudication` items (represented as `dict` in JSON). """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        super(ClaimResponseItemDetailSubDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ClaimResponseItemDetailSubDetailAdjudication, True),
            ("sequenceLinkId", "sequenceLinkId", int, False),
        ])
        return js


class ClaimResponseItemDetailSubDetailAdjudication(fhirelement.FHIRElement):
    """ Subdetail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseItemDetailSubDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monetary value.
        Type `float`. """
        
        super(ClaimResponseItemDetailSubDetailAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseItemDetailSubDetailAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("code", "code", coding.Coding, False),
            ("value", "value", float, False),
        ])
        return js


class ClaimResponseNote(fhirelement.FHIRElement):
    """ Processing notes.
    
    Note text.
    """
    
    resource_name = "ClaimResponseNote"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.number = None
        """ Note Number for this note.
        Type `int`. """
        
        self.text = None
        """ Note explanatory text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimResponseNote, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ClaimResponseNote, self).elementProperties()
        js.extend([
            ("number", "number", int, False),
            ("text", "text", str, False),
            ("type", "type", coding.Coding, False),
        ])
        return js

