#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/EligibilityResponse) on 2016-08-31.
#  2016, SMART Health IT.


from . import domainresource

class EligibilityResponse(domainresource.DomainResource):
    """ EligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """
    
    resource_name = "EligibilityResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        self.organizationIdentifier = None
        """ Insurer.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.organizationReference = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error | partial.
        Type `str`. """
        
        self.requestIdentifier = None
        """ Claim reference.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationIdentifier = None
        """ Responsible organization.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestOrganizationReference = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProviderIdentifier = None
        """ Responsible practitioner.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.requestProviderReference = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.requestReference = None
        """ Claim reference.
        Type `FHIRReference` referencing `EligibilityRequest` (represented as `dict` in JSON). """
        
        self.ruleset = None
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(EligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)
    
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
            ("organizationIdentifier", "organizationIdentifier", identifier.Identifier, False, "organization", False),
            ("organizationReference", "organizationReference", fhirreference.FHIRReference, False, "organization", False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("requestIdentifier", "requestIdentifier", identifier.Identifier, False, "request", False),
            ("requestOrganizationIdentifier", "requestOrganizationIdentifier", identifier.Identifier, False, "requestOrganization", False),
            ("requestOrganizationReference", "requestOrganizationReference", fhirreference.FHIRReference, False, "requestOrganization", False),
            ("requestProviderIdentifier", "requestProviderIdentifier", identifier.Identifier, False, "requestProvider", False),
            ("requestProviderReference", "requestProviderReference", fhirreference.FHIRReference, False, "requestProvider", False),
            ("requestReference", "requestReference", fhirreference.FHIRReference, False, "request", False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class EligibilityResponseBenefitBalance(backboneelement.BackboneElement):
    """ Benefits by Category.
    
    Benefits and optionally current balances by Category.
    """
    
    resource_name = "EligibilityResponseBenefitBalance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Benefit Category.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.description = None
        """ Description of the benefit.
        Type `str`. """
        
        self.financial = None
        """ Benefit Summary.
        List of `EligibilityResponseBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Short name for the benefit.
        Type `str`. """
        
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
        
        super(EligibilityResponseBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", coding.Coding, False, None, True),
            ("description", "description", str, False, None, False),
            ("financial", "financial", EligibilityResponseBenefitBalanceFinancial, True, None, False),
            ("name", "name", str, False, None, False),
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
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitMoney = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        
        self.benefitString = None
        """ Benefits allowed.
        Type `str`. """
        
        self.benefitUnsignedInt = None
        """ Benefits allowed.
        Type `int`. """
        
        self.benefitUsedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        
        self.benefitUsedUnsignedInt = None
        """ Benefits used.
        Type `int`. """
        
        self.type = None
        """ Deductable, visits, benefit amount.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(EligibilityResponseBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("benefitMoney", "benefitMoney", money.Money, False, "benefit", False),
            ("benefitString", "benefitString", str, False, "benefit", False),
            ("benefitUnsignedInt", "benefitUnsignedInt", int, False, "benefit", False),
            ("benefitUsedMoney", "benefitUsedMoney", money.Money, False, "benefitUsed", False),
            ("benefitUsedUnsignedInt", "benefitUsedUnsignedInt", int, False, "benefitUsed", False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class EligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    resource_name = "EligibilityResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(EligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
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
from . import money
