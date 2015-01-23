#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (claimresponse.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import money


class ClaimResponse(fhirresource.FHIRResource):
    """ Remittance resource.
    
    This resource provides the adjudication details from the processing of a
    Claim resource.
    """
    
    resource_name = "ClaimResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additem = None
        """ Insurer added line items.
        List of `ClaimResponseAdditem` items (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `OralHealthClaim, PharmacyClaim, VisionClaim, ProfessionalClaim, InstitutionalClaim` (represented as `dict` in JSON). """
        
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
        if 'additem' in jsondict:
            self.additem = ClaimResponseAdditem.with_json_and_owner(jsondict['additem'], self)
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


class ClaimResponseAdditem(fhirelement.FHIRElement):
    """ Insurer added line items.
    
    The first tier service adjudications for payor added services.
    """
    
    resource_name = "ClaimResponseAdditem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ClaimResponseAdditemAdjudication` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Added items details.
        List of `ClaimResponseAdditemDetail` items (represented as `dict` in JSON). """
        
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
        
        super(ClaimResponseAdditem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAdditem, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseAdditemAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'detail' in jsondict:
            self.detail = ClaimResponseAdditemDetail.with_json_and_owner(jsondict['detail'], self)
        if 'fee' in jsondict:
            self.fee = money.Money.with_json_and_owner(jsondict['fee'], self)
        if 'noteNumberLinkId' in jsondict:
            self.noteNumberLinkId = jsondict['noteNumberLinkId']
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']
        if 'service' in jsondict:
            self.service = coding.Coding.with_json_and_owner(jsondict['service'], self)


class ClaimResponseAdditemAdjudication(fhirelement.FHIRElement):
    """ Added items adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseAdditemAdjudication"
    
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
        
        super(ClaimResponseAdditemAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAdditemAdjudication, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


class ClaimResponseAdditemDetail(fhirelement.FHIRElement):
    """ Added items details.
    
    The second tier service adjudications for payor added services.
    """
    
    resource_name = "ClaimResponseAdditemDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Added items detail adjudication.
        List of `ClaimResponseAdditemDetailAdjudication` items (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Money` (represented as `dict` in JSON). """
        
        self.service = None
        """ Service or Product.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ClaimResponseAdditemDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAdditemDetail, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseAdditemDetailAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'fee' in jsondict:
            self.fee = money.Money.with_json_and_owner(jsondict['fee'], self)
        if 'service' in jsondict:
            self.service = coding.Coding.with_json_and_owner(jsondict['service'], self)


class ClaimResponseAdditemDetailAdjudication(fhirelement.FHIRElement):
    """ Added items detail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseAdditemDetailAdjudication"
    
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
        
        super(ClaimResponseAdditemDetailAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseAdditemDetailAdjudication, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = money.Money.with_json_and_owner(jsondict['amount'], self)
        if 'code' in jsondict:
            self.code = coding.Coding.with_json_and_owner(jsondict['code'], self)
        if 'value' in jsondict:
            self.value = jsondict['value']


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
        
        self.subdetail = None
        """ Subdetail line items.
        List of `ClaimResponseItemDetailSubdetail` items (represented as `dict` in JSON). """
        
        super(ClaimResponseItemDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemDetail, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseItemDetailAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']
        if 'subdetail' in jsondict:
            self.subdetail = ClaimResponseItemDetailSubdetail.with_json_and_owner(jsondict['subdetail'], self)


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


class ClaimResponseItemDetailSubdetail(fhirelement.FHIRElement):
    """ Subdetail line items.
    
    The third tier service adjudications for submitted services.
    """
    
    resource_name = "ClaimResponseItemDetailSubdetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Subdetail adjudication.
        List of `ClaimResponseItemDetailSubdetailAdjudication` items (represented as `dict` in JSON). """
        
        self.sequenceLinkId = None
        """ Service instance.
        Type `int`. """
        
        super(ClaimResponseItemDetailSubdetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemDetailSubdetail, self).update_with_json(jsondict)
        if 'adjudication' in jsondict:
            self.adjudication = ClaimResponseItemDetailSubdetailAdjudication.with_json_and_owner(jsondict['adjudication'], self)
        if 'sequenceLinkId' in jsondict:
            self.sequenceLinkId = jsondict['sequenceLinkId']


class ClaimResponseItemDetailSubdetailAdjudication(fhirelement.FHIRElement):
    """ Subdetail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ClaimResponseItemDetailSubdetailAdjudication"
    
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
        
        super(ClaimResponseItemDetailSubdetailAdjudication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ClaimResponseItemDetailSubdetailAdjudication, self).update_with_json(jsondict)
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

