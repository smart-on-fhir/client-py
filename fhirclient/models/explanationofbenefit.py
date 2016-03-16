#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Explanation of Benefit resource.
    
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    
    resource_name = "ExplanationOfBenefit"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.accidentDate = None
        """ Accident Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.accidentLocationAddress = None
        """ Accident Place.
        Type `Address` (represented as `dict` in JSON). """
        
        self.accidentLocationReference = None
        """ Accident Place.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.accidentLocationString = None
        """ Accident Place.
        Type `str`. """
        
        self.accidentType = None
        """ Accident Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.addItem = None
        """ Insurer added line items.
        List of `ExplanationOfBenefitAddItem` items (represented as `dict` in JSON). """
        
        self.benefitBalance = None
        """ Balance by Benefit Category.
        List of `ExplanationOfBenefitBenefitBalance` items (represented as `dict` in JSON). """
        
        self.billablePeriod = None
        """ Period for charge submission.
        Type `Period` (represented as `dict` in JSON). """
        
        self.claim = None
        """ Claim reference.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.claimResponse = None
        """ Claim response reference.
        Type `FHIRReference` referencing `ClaimResponse` (represented as `dict` in JSON). """
        
        self.claimTotal = None
        """ Total claim cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Insurance or medical plan.
        Type `ExplanationOfBenefitCoverage` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosis = None
        """ Diagnosis.
        List of `ExplanationOfBenefitDiagnosis` items (represented as `dict` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.employmentImpacted = None
        """ Period unable to work.
        Type `Period` (represented as `dict` in JSON). """
        
        self.exception = None
        """ Eligibility exceptions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.facility = None
        """ Servicing Facility.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.hospitalization = None
        """ Period in hospital.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.interventionException = None
        """ Intervention and exception code (Pharma).
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Goods and Services.
        List of `ExplanationOfBenefitItem` items (represented as `dict` in JSON). """
        
        self.missingTeeth = None
        """ Only if type = oral.
        List of `ExplanationOfBenefitMissingTeeth` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Processing notes.
        List of `ExplanationOfBenefitNote` items (represented as `dict` in JSON). """
        
        self.onsetDate = None
        """ Illness, injury or treatable condition date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.onsetPeriod = None
        """ Illness, injury or treatable condition date.
        Type `Period` (represented as `dict` in JSON). """
        
        self.organization = None
        """ Responsible organization for the claim.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalPrescription = None
        """ Original Prescription.
        Type `FHIRReference` referencing `MedicationOrder` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.payee = None
        """ Payee.
        Type `ExplanationOfBenefitPayee` (represented as `dict` in JSON). """
        
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
        
        self.precedence = None
        """ Precedence (primary, secondary, etc.).
        Type `int`. """
        
        self.prescription = None
        """ Prescription.
        Type `FHIRReference` referencing `MedicationOrder, VisionPrescription` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible provider for the claim.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.referral = None
        """ Treatment Referral.
        Type `FHIRReference` referencing `ReferralRequest` (represented as `dict` in JSON). """
        
        self.relatedClaim = None
        """ Related Claims.
        List of `FHIRReference` items referencing `Claim` (represented as `dict` in JSON). """
        
        self.reserved = None
        """ Funds reserved status.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Current specification followed.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.school = None
        """ Name of School.
        Type `str`. """
        
        self.specialCondition = None
        """ List of special Conditions.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.totalBenefit = None
        """ Total benefit payable for the Claim.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.unallocDeductable = None
        """ Unallocated deductable.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefit, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("accidentDate", "accidentDate", fhirdate.FHIRDate, False, None, False),
            ("accidentLocationAddress", "accidentLocationAddress", address.Address, False, "accidentLocation", False),
            ("accidentLocationReference", "accidentLocationReference", fhirreference.FHIRReference, False, "accidentLocation", False),
            ("accidentLocationString", "accidentLocationString", str, False, "accidentLocation", False),
            ("accidentType", "accidentType", coding.Coding, False, None, False),
            ("addItem", "addItem", ExplanationOfBenefitAddItem, True, None, False),
            ("benefitBalance", "benefitBalance", ExplanationOfBenefitBenefitBalance, True, None, False),
            ("billablePeriod", "billablePeriod", period.Period, False, None, False),
            ("claim", "claim", fhirreference.FHIRReference, False, None, False),
            ("claimResponse", "claimResponse", fhirreference.FHIRReference, False, None, False),
            ("claimTotal", "claimTotal", quantity.Quantity, False, None, False),
            ("coverage", "coverage", ExplanationOfBenefitCoverage, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("diagnosis", "diagnosis", ExplanationOfBenefitDiagnosis, True, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("employmentImpacted", "employmentImpacted", period.Period, False, None, False),
            ("exception", "exception", coding.Coding, True, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("form", "form", coding.Coding, False, None, False),
            ("hospitalization", "hospitalization", period.Period, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("interventionException", "interventionException", coding.Coding, True, None, False),
            ("item", "item", ExplanationOfBenefitItem, True, None, False),
            ("missingTeeth", "missingTeeth", ExplanationOfBenefitMissingTeeth, True, None, False),
            ("note", "note", ExplanationOfBenefitNote, True, None, False),
            ("onsetDate", "onsetDate", fhirdate.FHIRDate, False, "onset", False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalPrescription", "originalPrescription", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("payee", "payee", ExplanationOfBenefitPayee, False, None, False),
            ("paymentAdjustment", "paymentAdjustment", quantity.Quantity, False, None, False),
            ("paymentAdjustmentReason", "paymentAdjustmentReason", coding.Coding, False, None, False),
            ("paymentAmount", "paymentAmount", quantity.Quantity, False, None, False),
            ("paymentDate", "paymentDate", fhirdate.FHIRDate, False, None, False),
            ("paymentRef", "paymentRef", identifier.Identifier, False, None, False),
            ("precedence", "precedence", int, False, None, False),
            ("prescription", "prescription", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("referral", "referral", fhirreference.FHIRReference, False, None, False),
            ("relatedClaim", "relatedClaim", fhirreference.FHIRReference, True, None, False),
            ("reserved", "reserved", coding.Coding, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("school", "school", str, False, None, False),
            ("specialCondition", "specialCondition", coding.Coding, True, None, False),
            ("totalBenefit", "totalBenefit", quantity.Quantity, False, None, False),
            ("unallocDeductable", "unallocDeductable", quantity.Quantity, False, None, False),
        ])
        return js


from . import backboneelement

class ExplanationOfBenefitAddItem(backboneelement.BackboneElement):
    """ Insurer added line items.
    
    The first tier service adjudications for payor added services.
    """
    
    resource_name = "ExplanationOfBenefitAddItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Added items adjudication.
        List of `ExplanationOfBenefitAddItemAdjudication` items (represented as `dict` in JSON). """
        
        self.detail = None
        """ Added items details.
        List of `ExplanationOfBenefitAddItemDetail` items (represented as `dict` in JSON). """
        
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
        
        super(ExplanationOfBenefitAddItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitAddItemAdjudication, True, None, False),
            ("detail", "detail", ExplanationOfBenefitAddItemDetail, True, None, False),
            ("fee", "fee", quantity.Quantity, False, None, False),
            ("noteNumberLinkId", "noteNumberLinkId", int, True, None, False),
            ("sequenceLinkId", "sequenceLinkId", int, True, None, False),
            ("service", "service", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitAddItemAdjudication(backboneelement.BackboneElement):
    """ Added items adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ExplanationOfBenefitAddItemAdjudication"
    
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
        """ Non-monitory value.
        Type `float`. """
        
        super(ExplanationOfBenefitAddItemAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("code", "code", coding.Coding, False, None, True),
            ("value", "value", float, False, None, False),
        ])
        return js


class ExplanationOfBenefitAddItemDetail(backboneelement.BackboneElement):
    """ Added items details.
    
    The second tier service adjudications for payor added services.
    """
    
    resource_name = "ExplanationOfBenefitAddItemDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Added items detail adjudication.
        List of `ExplanationOfBenefitAddItemDetailAdjudication` items (represented as `dict` in JSON). """
        
        self.fee = None
        """ Professional fee or Product charge.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.service = None
        """ Service or Product.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitAddItemDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitAddItemDetailAdjudication, True, None, False),
            ("fee", "fee", quantity.Quantity, False, None, False),
            ("service", "service", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitAddItemDetailAdjudication(backboneelement.BackboneElement):
    """ Added items detail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ExplanationOfBenefitAddItemDetailAdjudication"
    
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
        """ Non-monitory value.
        Type `float`. """
        
        super(ExplanationOfBenefitAddItemDetailAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitAddItemDetailAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("code", "code", coding.Coding, False, None, True),
            ("value", "value", float, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalance(backboneelement.BackboneElement):
    """ Balance by Benefit Category.
    """
    
    resource_name = "ExplanationOfBenefitBenefitBalance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ Benefit Category.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.financial = None
        """ Benefit Summary.
        List of `ExplanationOfBenefitBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
        self.network = None
        """ In or out of network.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subCategory = None
        """ Benefit SubCategory.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.term = None
        """ Annual or lifetime.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Individual or family.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitBenefitBalance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, False, None, True),
            ("financial", "financial", ExplanationOfBenefitBenefitBalanceFinancial, True, None, False),
            ("network", "network", coding.Coding, False, None, False),
            ("subCategory", "subCategory", coding.Coding, False, None, False),
            ("term", "term", coding.Coding, False, None, False),
            ("unit", "unit", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    resource_name = "ExplanationOfBenefitBenefitBalanceFinancial"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.benefitQuantity = None
        """ Benefits allowed.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.benefitUnsignedInt = None
        """ Benefits allowed.
        Type `int`. """
        
        self.benefitUsedQuantity = None
        """ Benefits used.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.benefitUsedUnsignedInt = None
        """ Benefits used.
        Type `int`. """
        
        self.type = None
        """ Deductable, visits, benefit amount.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitBenefitBalanceFinancial, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("benefitQuantity", "benefitQuantity", quantity.Quantity, False, "benefit", False),
            ("benefitUnsignedInt", "benefitUnsignedInt", int, False, "benefit", False),
            ("benefitUsedQuantity", "benefitUsedQuantity", quantity.Quantity, False, "benefitUsed", False),
            ("benefitUsedUnsignedInt", "benefitUsedUnsignedInt", int, False, "benefitUsed", False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitCoverage(backboneelement.BackboneElement):
    """ Insurance or medical plan.
    
    Financial instrument by which payment information for health care.
    """
    
    resource_name = "ExplanationOfBenefitCoverage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.preAuthRef = None
        """ Pre-Authorization/Determination Reference.
        List of `str` items. """
        
        self.relationship = None
        """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitCoverage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitCoverage, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("preAuthRef", "preAuthRef", str, True, None, False),
            ("relationship", "relationship", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitDiagnosis(backboneelement.BackboneElement):
    """ Diagnosis.
    
    Ordered list of patient diagnosis for which care is sought.
    """
    
    resource_name = "ExplanationOfBenefitDiagnosis"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.diagnosis = None
        """ Patient's list of diagnosis.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Sequence of diagnosis.
        Type `int`. """
        
        super(ExplanationOfBenefitDiagnosis, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosis", "diagnosis", coding.Coding, False, None, True),
            ("sequence", "sequence", int, False, None, True),
        ])
        return js


class ExplanationOfBenefitItem(backboneelement.BackboneElement):
    """ Goods and Services.
    
    First tier of goods and services.
    """
    
    resource_name = "ExplanationOfBenefitItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Adjudication details.
        List of `ExplanationOfBenefitItemAdjudication` items (represented as `dict` in JSON). """
        
        self.bodySite = None
        """ Service Location.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.detail = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetail` items (represented as `dict` in JSON). """
        
        self.diagnosisLinkId = None
        """ Diagnosis Link.
        List of `int` items. """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.modifier = None
        """ Service/Product billing modifiers.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.net = None
        """ Total item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.noteNumber = None
        """ List of note numbers which apply.
        List of `int` items. """
        
        self.place = None
        """ Place of service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.prosthesis = None
        """ Prosthetic details.
        Type `ExplanationOfBenefitItemProsthesis` (represented as `dict` in JSON). """
        
        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Item Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.servicedDate = None
        """ Date or dates of Service.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.servicedPeriod = None
        """ Date or dates of Service.
        Type `Period` (represented as `dict` in JSON). """
        
        self.subSite = None
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
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItem, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemAdjudication, True, None, False),
            ("bodySite", "bodySite", coding.Coding, False, None, False),
            ("detail", "detail", ExplanationOfBenefitItemDetail, True, None, False),
            ("diagnosisLinkId", "diagnosisLinkId", int, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("modifier", "modifier", coding.Coding, True, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("noteNumber", "noteNumber", int, True, None, False),
            ("place", "place", coding.Coding, False, None, False),
            ("points", "points", float, False, None, False),
            ("prosthesis", "prosthesis", ExplanationOfBenefitItemProsthesis, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("subSite", "subSite", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", coding.Coding, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemAdjudication(backboneelement.BackboneElement):
    """ Adjudication details.
    
    The adjudications results.
    """
    
    resource_name = "ExplanationOfBenefitItemAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.category = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Adjudication reason.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ExplanationOfBenefitItemAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("category", "category", coding.Coding, False, None, True),
            ("reason", "reason", coding.Coding, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Second tier of goods and services.
    """
    
    resource_name = "ExplanationOfBenefitItemDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ Detail adjudication.
        List of `ExplanationOfBenefitItemDetailAdjudication` items (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Total additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.sequence = None
        """ Service instance.
        Type `int`. """
        
        self.service = None
        """ Additional item codes.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subDetail = None
        """ Additional items.
        List of `ExplanationOfBenefitItemDetailSubDetail` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Group or type of product or service.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.unitPrice = None
        """ Fee, charge or cost per point.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemDetailAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("subDetail", "subDetail", ExplanationOfBenefitItemDetailSubDetail, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", coding.Coding, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetailAdjudication(backboneelement.BackboneElement):
    """ Detail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ExplanationOfBenefitItemDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Adjudication reason.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ExplanationOfBenefitItemDetailAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("code", "code", coding.Coding, False, None, True),
            ("reason", "reason", coding.Coding, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetailSubDetail(backboneelement.BackboneElement):
    """ Additional items.
    
    Third tier of goods and services.
    """
    
    resource_name = "ExplanationOfBenefitItemDetailSubDetail"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.adjudication = None
        """ SubDetail adjudication.
        List of `ExplanationOfBenefitItemDetailSubDetailAdjudication` items (represented as `dict` in JSON). """
        
        self.factor = None
        """ Price scaling factor.
        Type `float`. """
        
        self.net = None
        """ Net additional item cost.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.points = None
        """ Difficulty scaling factor.
        Type `float`. """
        
        self.quantity = None
        """ Count of Products or Services.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
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
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemDetailSubDetail, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetail, self).elementProperties()
        js.extend([
            ("adjudication", "adjudication", ExplanationOfBenefitItemDetailSubDetailAdjudication, True, None, False),
            ("factor", "factor", float, False, None, False),
            ("net", "net", quantity.Quantity, False, None, False),
            ("points", "points", float, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("service", "service", coding.Coding, False, None, True),
            ("type", "type", coding.Coding, False, None, True),
            ("udi", "udi", coding.Coding, False, None, False),
            ("unitPrice", "unitPrice", quantity.Quantity, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemDetailSubDetailAdjudication(backboneelement.BackboneElement):
    """ SubDetail adjudication.
    
    The adjudications results.
    """
    
    resource_name = "ExplanationOfBenefitItemDetailSubDetailAdjudication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Monetary amount.
        Type `Quantity` referencing `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Adjudication category such as co-pay, eligible, benefit, etc..
        Type `Coding` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Adjudication reason.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None
        """ Non-monitory value.
        Type `float`. """
        
        super(ExplanationOfBenefitItemDetailSubDetailAdjudication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemDetailSubDetailAdjudication, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("code", "code", coding.Coding, False, None, True),
            ("reason", "reason", coding.Coding, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


class ExplanationOfBenefitItemProsthesis(backboneelement.BackboneElement):
    """ Prosthetic details.
    
    The materials and placement date of prior fixed prosthesis.
    """
    
    resource_name = "ExplanationOfBenefitItemProsthesis"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.initial = None
        """ Is this the initial service.
        Type `bool`. """
        
        self.priorDate = None
        """ Initial service Date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priorMaterial = None
        """ Prosthetic Material.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitItemProsthesis, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitItemProsthesis, self).elementProperties()
        js.extend([
            ("initial", "initial", bool, False, None, False),
            ("priorDate", "priorDate", fhirdate.FHIRDate, False, None, False),
            ("priorMaterial", "priorMaterial", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitMissingTeeth(backboneelement.BackboneElement):
    """ Only if type = oral.
    
    A list of teeth which would be expected but are not found due to having
    been previously  extracted or for other reasons.
    """
    
    resource_name = "ExplanationOfBenefitMissingTeeth"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.extractionDate = None
        """ Date of Extraction.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.reason = None
        """ Reason for missing.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.tooth = None
        """ Tooth Code.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefitMissingTeeth, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitMissingTeeth, self).elementProperties()
        js.extend([
            ("extractionDate", "extractionDate", fhirdate.FHIRDate, False, None, False),
            ("reason", "reason", coding.Coding, False, None, False),
            ("tooth", "tooth", coding.Coding, False, None, True),
        ])
        return js


class ExplanationOfBenefitNote(backboneelement.BackboneElement):
    """ Processing notes.
    
    Note text.
    """
    
    resource_name = "ExplanationOfBenefitNote"
    
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
        
        super(ExplanationOfBenefitNote, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitNote, self).elementProperties()
        js.extend([
            ("number", "number", int, False, None, False),
            ("text", "text", str, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class ExplanationOfBenefitPayee(backboneelement.BackboneElement):
    """ Payee.
    
    The party to be reimbursed for the services.
    """
    
    resource_name = "ExplanationOfBenefitPayee"
    
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
        
        super(ExplanationOfBenefitPayee, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ExplanationOfBenefitPayee, self).elementProperties()
        js.extend([
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("person", "person", fhirreference.FHIRReference, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import address
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
