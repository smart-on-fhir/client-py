#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/EligibilityResponse) on 2017-03-15.
#  2017, SMART Health IT.


from . import domainresource

class EligibilityResponse(domainresource.DomainResource):
    """ EligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an Eligibility resource.
    """
    
    resource_type = "EligibilityResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.inforce = None
        """ Coverage inforce.
        Type `bool`. """
        
        self.insurance = None
        """ Details by insurance coverage.
        List of `EligibilityResponseInsurance` items (represented as `dict` in JSON). """
        
        self.insurer = None
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.outcome = None
        """ complete | error | partial.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.request = None
        """ Eligibility reference.
        Type `FHIRReference` referencing `EligibilityRequest` (represented as `dict` in JSON). """
        
        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        
        super(EligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("error", "error", EligibilityResponseError, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("inforce", "inforce", bool, False, None, False),
            ("insurance", "insurance", EligibilityResponseInsurance, True, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
        ])
        return js


from . import backboneelement

class EligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Mutually exclusive with Services Provided (Item).
    """
    
    resource_type = "EligibilityResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class EligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Details by insurance coverage.
    
    The insurer may provide both the details for the requested coverage as well
    as details for additional coverages known to the insurer.
    """
    
    resource_type = "EligibilityResponseInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitBalance = None
        """ Benefits by Category.
        List of `EligibilityResponseInsuranceBenefitBalance` items (represented as `dict` in JSON). """
        
        self.contract = None
        """ Contract details.
        Type `FHIRReference` referencing `Contract` (represented as `dict` in JSON). """
        
        self.coverage = None
        """ Updated Coverage details.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        super(EligibilityResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("benefitBalance", "benefitBalance", EligibilityResponseInsuranceBenefitBalance, True, None, False),
            ("contract", "contract", fhirreference.FHIRReference, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class EligibilityResponseInsuranceBenefitBalance(backboneelement.BackboneElement):
    """ Benefits by Category.
    
    Benefits and optionally current balances by Category.
    """
    
    resource_type = "EligibilityResponseInsuranceBenefitBalance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Benefit Category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None
        """ Description of the benefit.
        Type `str`. """
        
        self.excluded = None
        """ Excluded from the plan.
        Type `bool`. """
        
        self.financial = None
        """ Benefit Summary.
        List of `EligibilityResponseInsuranceBenefitBalanceFinancial` items (represented as `dict` in JSON). """
        
        self.name = None
        """ Short name for the benefit.
        Type `str`. """
        
        self.network = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subCategory = None
        """ Benefit SubCategory.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.term = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EligibilityResponseInsuranceBenefitBalance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseInsuranceBenefitBalance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("financial", "financial", EligibilityResponseInsuranceBenefitBalanceFinancial, True, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("subCategory", "subCategory", codeableconcept.CodeableConcept, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class EligibilityResponseInsuranceBenefitBalanceFinancial(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits Used to date.
    """
    
    resource_type = "EligibilityResponseInsuranceBenefitBalanceFinancial"
    
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
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(EligibilityResponseInsuranceBenefitBalanceFinancial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(EligibilityResponseInsuranceBenefitBalanceFinancial, self).elementProperties()
        js.extend([
            ("benefitMoney", "benefitMoney", money.Money, False, "benefit", False),
            ("benefitString", "benefitString", str, False, "benefit", False),
            ("benefitUnsignedInt", "benefitUnsignedInt", int, False, "benefit", False),
            ("benefitUsedMoney", "benefitUsedMoney", money.Money, False, "benefitUsed", False),
            ("benefitUsedUnsignedInt", "benefitUsedUnsignedInt", int, False, "benefitUsed", False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
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
