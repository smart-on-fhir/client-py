#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (oralhealthclaim.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import money
import quantity


class OralHealthClaim(fhirresource.FHIRResource):
    """ Claim, Pre-determination or Pre-authorization.
    
    A provider issued list of services and products provided, or to be
    provided, to a patient which is provided to an insurer for payment
    recovery.
    """
    
    resource_name = "OralHealthClaim"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accident = None
        """ Accident Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.accidentType = None
        """ Accident Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.additionalMaterials = None
        """ Additional materials, documents, etc..
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.condition = None
        """ List of presenting Conditions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance or medical plan.
        List of `OralHealthClaimCoverage` items (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        """ Diagnosis.
        List of `OralHealthClaimDiagnosis` items (represented as `dict` in JSON). """
        
        self.enterer = None
        """ Author.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.exception = None
        """ Eligibility exceptions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.fundsReserve = None
        """ Funds requested to be reserved.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Claim number.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interventionException = None
        """ Intervention and exception code (Pharma).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Goods and Services.
        List of `OralHealthClaimItem` items (represented as `dict` in JSON). """
        
        self.missingteeth = None
        """ Missing Teeth.
        List of `OralHealthClaimMissingteeth` items (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.orthoPlan = None
        """ Orthodontic Treatment Plan.
        Type `OralHealthClaimOrthoPlan` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `OralHealthClaimPayee` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Desired processing priority.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible provider.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.referral = None
        """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.school = None
        """ Name of School.
        Type `str`. """
        
        self.target = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.use = None
        """ complete | proposed | exploratory | other.
        Type `str`. """
        
        super(OralHealthClaim, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaim, self).update_with_json(jsondict)
        if 'accident' in jsondict:
            self.accident = fhirdate.FHIRDate.with_json_and_owner(jsondict['accident'], self)
        if 'accidentType' in jsondict:
            self.accidentType = coding.Coding.with_json_and_owner(jsondict['accidentType'], self)
        if 'additionalMaterials' in jsondict:
            self.additionalMaterials = coding.Coding.with_json_and_owner(jsondict['additionalMaterials'], self)
        if 'condition' in jsondict:
            self.condition = coding.Coding.with_json_and_owner(jsondict['condition'], self)
        if 'coverage' in jsondict:
            self.coverage = OralHealthClaimCoverage.with_json_and_owner(jsondict['coverage'], self)
        if 'created' in jsondict:
            self.created = fhirdate.FHIRDate.with_json_and_owner(jsondict['created'], self)
        if 'diagnosis' in jsondict:
            self.diagnosis = OralHealthClaimDiagnosis.with_json_and_owner(jsondict['diagnosis'], self)
        if 'enterer' in jsondict:
            self.enterer = fhirreference.FHIRReference.with_json_and_owner(jsondict['enterer'], self)
        if 'exception' in jsondict:
            self.exception = coding.Coding.with_json_and_owner(jsondict['exception'], self)
        if 'facility' in jsondict:
            self.facility = fhirreference.FHIRReference.with_json_and_owner(jsondict['facility'], self)
        if 'fundsReserve' in jsondict:
            self.fundsReserve = coding.Coding.with_json_and_owner(jsondict['fundsReserve'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'interventionException' in jsondict:
            self.interventionException = coding.Coding.with_json_and_owner(jsondict['interventionException'], self)
        if 'item' in jsondict:
            self.item = OralHealthClaimItem.with_json_and_owner(jsondict['item'], self)
        if 'missingteeth' in jsondict:
            self.missingteeth = OralHealthClaimMissingteeth.with_json_and_owner(jsondict['missingteeth'], self)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'originalRuleset' in jsondict:
            self.originalRuleset = coding.Coding.with_json_and_owner(jsondict['originalRuleset'], self)
        if 'orthoPlan' in jsondict:
            self.orthoPlan = OralHealthClaimOrthoPlan.with_json_and_owner(jsondict['orthoPlan'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'payee' in jsondict:
            self.payee = OralHealthClaimPayee.with_json_and_owner(jsondict['payee'], self)
        if 'priority' in jsondict:
            self.priority = coding.Coding.with_json_and_owner(jsondict['priority'], self)
        if 'provider' in jsondict:
            self.provider = fhirreference.FHIRReference.with_json_and_owner(jsondict['provider'], self)
        if 'referral' in jsondict:
            self.referral = fhirreference.FHIRReference.with_json_and_owner(jsondict['referral'], self)
        if 'ruleset' in jsondict:
            self.ruleset = coding.Coding.with_json_and_owner(jsondict['ruleset'], self)
        if 'school' in jsondict:
            self.school = jsondict['school']
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)
        if 'use' in jsondict:
            self.use = jsondict['use']


class OralHealthClaimCoverage(fhirelement.FHIRElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_name = "OralHealthClaimCoverage"
    
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
        
        self.preauthref = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.relationship = None
        """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance identifier.
        Type `int`. """
        
        super(OralHealthClaimCoverage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimCoverage, self).update_with_json(jsondict)
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
        if 'preauthref' in jsondict:
            self.preauthref = jsondict['preauthref']
        if 'relationship' in jsondict:
            self.relationship = coding.Coding.with_json_and_owner(jsondict['relationship'], self)
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']


class OralHealthClaimDiagnosis(fhirelement.FHIRElement):
    """ Diagnosis.
    
    Ordered list of patient diagnosis for which care is sought.
    """
    
    resource_name = "OralHealthClaimDiagnosis"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.diagnosis = None
        """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Sequence of diagnosis.
        Type `int`. """
        
        super(OralHealthClaimDiagnosis, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimDiagnosis, self).update_with_json(jsondict)
        if 'diagnosis' in jsondict:
            self.diagnosis = coding.Coding.with_json_and_owner(jsondict['diagnosis'], self)
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']


class OralHealthClaimItem(fhirelement.FHIRElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    resource_name = "OralHealthClaimItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Additional items.
        List of `OralHealthClaimItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisLinkId = None
        """ Diagnosis Link.
        List of `int` items. """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.mod = None
        """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.net = None
        """ Total item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.prosthesis = None
        """ Prosthetic details.
        Type `OralHealthClaimItemProsthesis` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.serviceDate = None
        """ Date of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subsite = None
        """ Service Sub-location.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(OralHealthClaimItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimItem, self).update_with_json(jsondict)
        if 'bodySite' in jsondict:
            self.bodySite = coding.Coding.with_json_and_owner(jsondict['bodySite'], self)
        if 'detail' in jsondict:
            self.detail = OralHealthClaimItemDetail.with_json_and_owner(jsondict['detail'], self)
        if 'diagnosisLinkId' in jsondict:
            self.diagnosisLinkId = jsondict['diagnosisLinkId']
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'mod' in jsondict:
            self.mod = coding.Coding.with_json_and_owner(jsondict['mod'], self)
        if 'net' in jsondict:
            self.net = money.Money.with_json_and_owner(jsondict['net'], self)
        if 'points' in jsondict:
            self.points = jsondict['points']
        if 'prosthesis' in jsondict:
            self.prosthesis = OralHealthClaimItemProsthesis.with_json_and_owner(jsondict['prosthesis'], self)
        if 'provider' in jsondict:
            self.provider = fhirreference.FHIRReference.with_json_and_owner(jsondict['provider'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']
        if 'service' in jsondict:
            self.service = coding.Coding.with_json_and_owner(jsondict['service'], self)
        if 'serviceDate' in jsondict:
            self.serviceDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['serviceDate'], self)
        if 'subsite' in jsondict:
            self.subsite = coding.Coding.with_json_and_owner(jsondict['subsite'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)
        if 'udi' in jsondict:
            self.udi = coding.Coding.with_json_and_owner(jsondict['udi'], self)
        if 'unitPrice' in jsondict:
            self.unitPrice = money.Money.with_json_and_owner(jsondict['unitPrice'], self)


class OralHealthClaimItemDetail(fhirelement.FHIRElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    resource_name = "OralHealthClaimItemDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ Additional items.
        List of `OralHealthClaimItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(OralHealthClaimItemDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimItemDetail, self).update_with_json(jsondict)
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'net' in jsondict:
            self.net = money.Money.with_json_and_owner(jsondict['net'], self)
        if 'points' in jsondict:
            self.points = jsondict['points']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']
        if 'service' in jsondict:
            self.service = coding.Coding.with_json_and_owner(jsondict['service'], self)
        if 'subDetail' in jsondict:
            self.subDetail = OralHealthClaimItemDetailSubDetail.with_json_and_owner(jsondict['subDetail'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)
        if 'udi' in jsondict:
            self.udi = coding.Coding.with_json_and_owner(jsondict['udi'], self)
        if 'unitPrice' in jsondict:
            self.unitPrice = money.Money.with_json_and_owner(jsondict['unitPrice'], self)


class OralHealthClaimItemDetailSubDetail(fhirelement.FHIRElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    resource_name = "OralHealthClaimItemDetailSubDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Net additional item cost.
        Type `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Money` (represented as `dict` in JSON). """
        
        super(OralHealthClaimItemDetailSubDetail, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimItemDetailSubDetail, self).update_with_json(jsondict)
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'net' in jsondict:
            self.net = money.Money.with_json_and_owner(jsondict['net'], self)
        if 'points' in jsondict:
            self.points = jsondict['points']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']
        if 'service' in jsondict:
            self.service = coding.Coding.with_json_and_owner(jsondict['service'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)
        if 'udi' in jsondict:
            self.udi = coding.Coding.with_json_and_owner(jsondict['udi'], self)
        if 'unitPrice' in jsondict:
            self.unitPrice = money.Money.with_json_and_owner(jsondict['unitPrice'], self)


class OralHealthClaimItemProsthesis(fhirelement.FHIRElement):
    """ Prosthetic details.
    
    The materials and placement date of prior fixed prosthesis.
    """
    
    resource_name = "OralHealthClaimItemProsthesis"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.initial = False
        """ Is this the initial service.
        Type `bool`. """
        
        self.priorDate = None
        """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priorMaterial = None
        """ Prosthetic Material.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(OralHealthClaimItemProsthesis, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimItemProsthesis, self).update_with_json(jsondict)
        if 'initial' in jsondict:
            self.initial = jsondict['initial']
        if 'priorDate' in jsondict:
            self.priorDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['priorDate'], self)
        if 'priorMaterial' in jsondict:
            self.priorMaterial = coding.Coding.with_json_and_owner(jsondict['priorMaterial'], self)


class OralHealthClaimMissingteeth(fhirelement.FHIRElement):
    """ Missing Teeth.
    
    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """
    
    resource_name = "OralHealthClaimMissingteeth"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.extractiondate = None
        """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reason = None
        """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.tooth = None
        """ Tooth Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(OralHealthClaimMissingteeth, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimMissingteeth, self).update_with_json(jsondict)
        if 'extractiondate' in jsondict:
            self.extractiondate = fhirdate.FHIRDate.with_json_and_owner(jsondict['extractiondate'], self)
        if 'reason' in jsondict:
            self.reason = coding.Coding.with_json_and_owner(jsondict['reason'], self)
        if 'tooth' in jsondict:
            self.tooth = coding.Coding.with_json_and_owner(jsondict['tooth'], self)


class OralHealthClaimOrthoPlan(fhirelement.FHIRElement):
    """ Orthodontic Treatment Plan.
    
    The high-level details of an Orthodontic Treatment Plan.
    """
    
    resource_name = "OralHealthClaimOrthoPlan"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.diagnosticFee = None
        """ Diagnostic phase fee.
        Type `Money` (represented as `dict` in JSON). """
        
        self.durationMonths = None
        """ Duration in months.
        Type `int`. """
        
        self.examFee = None
        """ First exam fee.
        Type `Money` (represented as `dict` in JSON). """
        
        self.initialPayment = None
        """ Initial payment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.paymentCount = None
        """ Anticipated number of payments.
        Type `int`. """
        
        self.periodicPayment = None
        """ Anticipated payment.
        Type `Money` (represented as `dict` in JSON). """
        
        self.start = None
        """ Start date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(OralHealthClaimOrthoPlan, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimOrthoPlan, self).update_with_json(jsondict)
        if 'diagnosticFee' in jsondict:
            self.diagnosticFee = money.Money.with_json_and_owner(jsondict['diagnosticFee'], self)
        if 'durationMonths' in jsondict:
            self.durationMonths = jsondict['durationMonths']
        if 'examFee' in jsondict:
            self.examFee = money.Money.with_json_and_owner(jsondict['examFee'], self)
        if 'initialPayment' in jsondict:
            self.initialPayment = money.Money.with_json_and_owner(jsondict['initialPayment'], self)
        if 'paymentCount' in jsondict:
            self.paymentCount = jsondict['paymentCount']
        if 'periodicPayment' in jsondict:
            self.periodicPayment = money.Money.with_json_and_owner(jsondict['periodicPayment'], self)
        if 'start' in jsondict:
            self.start = fhirdate.FHIRDate.with_json_and_owner(jsondict['start'], self)


class OralHealthClaimPayee(fhirelement.FHIRElement):
    """ Payee.
    
    The party to be reimbursed for the services.
    """
    
    resource_name = "OralHealthClaimPayee"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.organization = None
        """ Organization who is the payee.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.person = None
        """ Other person who is the payee.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Provider who is the payee.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None
        """ Party to be paid any benefits payable.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(OralHealthClaimPayee, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OralHealthClaimPayee, self).update_with_json(jsondict)
        if 'organization' in jsondict:
            self.organization = fhirreference.FHIRReference.with_json_and_owner(jsondict['organization'], self)
        if 'person' in jsondict:
            self.person = fhirreference.FHIRReference.with_json_and_owner(jsondict['person'], self)
        if 'provider' in jsondict:
            self.provider = fhirreference.FHIRReference.with_json_and_owner(jsondict['provider'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

