#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 (http://hl7.org/fhir/StructureDefinition/EligibilityResponse) on 2016-03-16.
#  2016, SMART Health IT.


from . import domainresource

class EligibilityResponse(domainresource.DomainResource):
    """ EligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """
    
    resource_name = "EligibilityResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.benefitBalance = None
        """ Benefits by Category.
        List of `EligibilityResponseBenefitBalance` items (represented as `dict` in JSON). """
        
        self.contract = None
        """ Contract details.
        Type `FHIRReference` referencing `Contract` (represented as `dict` in JSON). """
        
        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        
        self.error = None
        """ Processing errors.
        List of `EligibilityResponseError` items (represented as `dict` in JSON). """
        
        self.form = None
        """ Printed Form Identifier.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.inforce = None
        """ Coverage inforce.
        Type `bool`. """
        
        self.organization = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error.
        Type `str`. """
        
        self.request = None
        """ Claim reference.
        Type `FHIRReference` referencing `EligibilityRequest` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(EligibilityResponse, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EligibilityResponse, self).elementProperties()
        js.extend([
            ("benefitBalance", "benefitBalance", EligibilityResponseBenefitBalance, True, None, False),
            ("contract", "contract", fhirreference.FHIRReference, False, None, False),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", EligibilityResponseError, True, None, False),
            ("form", "form", coding.Coding, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("inforce", "inforce", bool, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
        ])
        return js


from . import backboneelement

class EligibilityResponseBenefitBalance(backboneelement.BackboneElement):
    """ Benefits by Category.
    
    Benefits and optionally current balances by Category.
    """
    
    resource_name = "EligibilityResponseBenefitBalance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ Benefit Category.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.financial = None
        """ Benefit Summary.
        List of `EligibilityResponseBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
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
        
        super(EligibilityResponseBenefitBalance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EligibilityResponseBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, False, None, True),
            ("financial", "financial", EligibilityResponseBenefitBalanceFinancial, True, None, False),
            ("network", "network", coding.Coding, False, None, False),
            ("subCategory", "subCategory", coding.Coding, False, None, False),
            ("term", "term", coding.Coding, False, None, False),
            ("unit", "unit", coding.Coding, False, None, False),
        ])
        return js


class EligibilityResponseBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    resource_name = "EligibilityResponseBenefitBalanceFinancial"
    
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
        
        super(EligibilityResponseBenefitBalanceFinancial, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EligibilityResponseBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("benefitQuantity", "benefitQuantity", quantity.Quantity, False, "benefit", False),
            ("benefitUnsignedInt", "benefitUnsignedInt", int, False, "benefit", False),
            ("benefitUsedQuantity", "benefitUsedQuantity", quantity.Quantity, False, "benefitUsed", False),
            ("benefitUsedUnsignedInt", "benefitUsedUnsignedInt", int, False, "benefitUsed", False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class EligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    resource_name = "EligibilityResponseError"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(EligibilityResponseError, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(EligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", coding.Coding, False, None, True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
