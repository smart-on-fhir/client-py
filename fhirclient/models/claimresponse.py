#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ClaimResponse) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import money


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
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentAdjustmentReason = None
        """ Reason for Payment adjustment.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.paymentAmount = None
        """ Payment amount.
        Type `Money` (represented as `dict` in JSON). """
        
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
        Type `Money` (represented as `dict` in JSON). """
        
        self.totalCost = None
        """ Total Cost of service from the Claim.
        Type `Money` (represented as `dict` in JSON). """
        
        self.unallocDeductable = None
        """ Unallocated deductable.
        Type `Money` (represented as `dict` in JSON). """
        
        super(ClaimResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponse, self).update_with_json(jsondict)
        if 'addItem' in jsondict:
            self.addItem = ClaimResponseAddItem.with_json_and_owner(jsondict['addItem'], self)
        if 'coverage' in jsondict:
            self.coverage = ClaimResponseCoverage.with_json_and_owner(jsondict['coverage'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'disposition' in jsondict:
            self.disposition = jsondict['disposition']
        if 'error' in jsondict:
            self.error = ClaimResponseError.with_json_and_owner(jsondict['error'], self)
        if 'form' in jsondict:
            self.form = coding.Coding.with_json_and_owner(jsondict['form'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'item' in jsondict:
            self.item = ClaimResponseItem.with_json_and_owner(jsondict['item'], self)
        if 'note' in jsondict:
            self.note = ClaimResponseNote.with_json_and_owner(jsondict['note'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'payeeType' in jsondict:
            self.payeeType = coding.Coding.with_json_and_owner(jsondict['payeeType'], self)
        if 'paymentAdjustment' in jsondict:
            self.paymentAdjustment = money.Money.with_json_and_owner(jsondict['paymentAdjustment'], self)
        if 'paymentAdjustmentReason' in jsondict:
            self.paymentAdjustmentReason = coding.Coding.with_json_and_owner(jsondict['paymentAdjustmentReason'], self)
        if 'paymentAmount' in jsondict:
            self.paymentAmount = money.Money.with_json_and_owner(jsondict['paymentAmount'], self)
        if 'paymentDate' in jsondict:
            self.paymentDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['paymentDate'], self)
        if 'paymentRef' in jsondict:
            self.paymentRef = identifier.Identifier.with_json_and_owner(jsondict['paymentRef'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'requestOrganization' in jsondict:
            self.requestOrganization = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestOrganization'], self)
        if 'requestProvider' in jsondict:
            self.requestProvider = fhirreference.FHIRReference.with_json_and_owner(jsondict['requestProvider'], self)
        if 'reserved' in jsondict:
            self.reserved = coding.Coding.with_json_and_owner(jsondict['reserved'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)
        if 'totalBenefit' in jsondict:
            self.totalBenefit = money.Money.with_json_and_owner(jsondict['totalBenefit'], self)
        if 'totalCost' in jsondict:
            self.totalCost = money.Money.with_json_and_owner(jsondict['totalCost'], self)
        if 'unallocDeductable' in jsondict:
            self.unallocDeductable = money.Money.with_json_and_owner(jsondict['unallocDeductable'], self)


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
        Type `Money` (represented as `dict` in JSON). """
        
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
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAddItem, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseAddItemAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'detail' in jsondict:
            self.detail = ClaimResponseAddItemDetail.with_json_and_owner(jsondict['detail'], self)
        if 'fee' in jsondict:
            self.fee = money.Money.with_json_and_owner(jsondict['fee'], self)
        if 'noteNumberLinkId' in jsondict:
            self.noteNumberLinkId = jsondict['noteNumberLinkId']
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']
        if 'service' in jsondict:
            self.service = coding.Coding.with_json_and_owner(jsondict['service'], self)


class ClaimResponseAddItemAdjudication(fhirelement.FHIRElement):
    """ Added items adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseAddItemAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monitary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ClaimResponseAddItemAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAddItemAdjudication, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


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
        Type `Money` (represented as `dict` in JSON). """
        
        self.service = None
        """ Service or Product.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimResponseAddItemDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAddItemDetail, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseAddItemDetailAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'fee' in jsondict:
            self.fee = money.Money.with_json_and_owner(jsondict['fee'], self)
        if 'service' in jsondict:
            self.service = coding.Coding.with_json_and_owner(jsondict['service'], self)


class ClaimResponseAddItemDetailAdjudication(fhirelement.FHIRElement):
    """ Added items detail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseAddItemDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monitary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ClaimResponseAddItemDetailAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAddItemDetailAdjudication, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


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
        
        self.focal = False
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
    
    def update_with_json(self, jsondict):
        super(ClaimResponseCoverage, self).update_with_json(jsondict)
        if 'businessArrangement' in jsondict:
            self.businessArrangement = jsondict['businessArrangement']
        if 'claimResponse' in jsondict:
            self.claimResponse = fhirreference.FHIRReference.with_json_and_owner(jsondict['claimResponse'], self)
        if 'coverage' in jsondict:
            self.coverage = fhirreference.FHIRReference.with_json_and_owner(jsondict['coverage'], self)
        if 'focal' in jsondict:
            self.focal = jsondict['focal']
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'preAuthRef' in jsondict:
            self.preAuthRef = jsondict['preAuthRef']
        if 'relationship' in jsondict:
            self.relationship = coding.Coding.with_json_and_owner(jsondict['relationship'], self)
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']


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
    
    def update_with_json(self, jsondict):
        super(ClaimResponseError, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'detailSequenceLinkId' in jsondict:
            self.detailSequenceLinkId = jsondict['detailSequenceLinkId']
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']
        if 'subdetailSequenceLinkId' in jsondict:
            self.subdetailSequenceLinkId = jsondict['subdetailSequenceLinkId']


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
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItem, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseItemAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'detail' in jsondict:
            self.detail = ClaimResponseItemDetail.with_json_and_owner(jsondict['detail'], self)
        if 'noteNumber' in jsondict:
            self.noteNumber = jsondict['noteNumber']
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']


class ClaimResponseItemAdjudication(fhirelement.FHIRElement):
    """ Adjudication details.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseItemAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monitary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ClaimResponseItemAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemAdjudication, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


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
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemDetail, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseItemDetailAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']
        if 'subDetail' in jsondict:
            self.subDetail = ClaimResponseItemDetailSubDetail.with_json_and_owner(jsondict['subDetail'], self)


class ClaimResponseItemDetailAdjudication(fhirelement.FHIRElement):
    """ Detail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseItemDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monitary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ClaimResponseItemDetailAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemDetailAdjudication, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


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
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemDetailSubDetail, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseItemDetailSubDetailAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']


class ClaimResponseItemDetailSubDetailAdjudication(fhirelement.FHIRElement):
    """ Subdetail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseItemDetailSubDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monitary amount.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ClaimResponseItemDetailSubDetailAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemDetailSubDetailAdjudication, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


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
        """ Note explanitory text.
        Type `str`. """
        
        self.type = None
        """ display | print | printoper.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimResponseNote, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseNote, self).update_with_json(jsondict)
        if 'number' in jsondict:
            self.number = jsondict['number']
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

