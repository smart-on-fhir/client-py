# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse).
# 2024, SMART Health IT.


from . import domainresource

class CoverageEligibilityResponse(domainresource.DomainResource):
    """ CoverageEligibilityResponse resource.
    
    This resource provides eligibility and plan details from the processing of
    an CoverageEligibilityRequest resource.
    """
    
    resource_type = "CoverageEligibilityResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.disposition = None
        """ Disposition Message.
        Type `str`. """
        self._disposition = None
        """ Primitive extension for disposition. Type `FHIRPrimitiveExtension` """
        
        self.error = None
        """ Processing errors.
        List of `CoverageEligibilityResponseError` items (represented as `dict` in JSON). """
        self._error = None
        """ Primitive extension for error. Type `FHIRPrimitiveExtension` """
        
        self.form = None
        """ Printed form identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._form = None
        """ Primitive extension for form. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for coverage eligiblity request.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.insurance = None
        """ Patient insurance information.
        List of `CoverageEligibilityResponseInsurance` items (represented as `dict` in JSON). """
        self._insurance = None
        """ Primitive extension for insurance. Type `FHIRPrimitiveExtension` """
        
        self.insurer = None
        """ Coverage issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._insurer = None
        """ Primitive extension for insurer. Type `FHIRPrimitiveExtension` """
        
        self.outcome = None
        """ queued | complete | error | partial.
        Type `str`. """
        self._outcome = None
        """ Primitive extension for outcome. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Intended recipient of products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.preAuthRef = None
        """ Preauthorization reference.
        Type `str`. """
        self._preAuthRef = None
        """ Primitive extension for preAuthRef. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.request = None
        """ Eligibility request reference.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._request = None
        """ Primitive extension for request. Type `FHIRPrimitiveExtension` """
        
        self.requestor = None
        """ Party responsible for the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._requestor = None
        """ Primitive extension for requestor. Type `FHIRPrimitiveExtension` """
        
        self.servicedDate = None
        """ Estimated date or dates of service.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._servicedDate = None
        """ Primitive extension for servicedDate. Type `FHIRPrimitiveExtension` """
        
        self.servicedPeriod = None
        """ Estimated date or dates of service.
        Type `Period` (represented as `dict` in JSON). """
        self._servicedPeriod = None
        """ Primitive extension for servicedPeriod. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponse, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("_disposition", "_disposition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("error", "error", CoverageEligibilityResponseError, True, None, False),
            ("_error", "_error", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("_form", "_form", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurance", "insurance", CoverageEligibilityResponseInsurance, True, None, False),
            ("_insurance", "_insurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("_insurer", "_insurer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outcome", "outcome", str, False, None, True),
            ("_outcome", "_outcome", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preAuthRef", "preAuthRef", str, False, None, False),
            ("_preAuthRef", "_preAuthRef", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, True),
            ("_request", "_request", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requestor", "requestor", fhirreference.FHIRReference, False, None, False),
            ("_requestor", "_requestor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("_servicedDate", "_servicedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("_servicedPeriod", "_servicedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class CoverageEligibilityResponseError(backboneelement.BackboneElement):
    """ Processing errors.
    
    Errors encountered during the processing of the request.
    """
    
    resource_type = "CoverageEligibilityResponseError"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Error code detailing processing issues.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityResponseError, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseError, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageEligibilityResponseInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services.
    """
    
    resource_type = "CoverageEligibilityResponseInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefitPeriod = None
        """ When the benefits are applicable.
        Type `Period` (represented as `dict` in JSON). """
        self._benefitPeriod = None
        """ Primitive extension for benefitPeriod. Type `FHIRPrimitiveExtension` """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._coverage = None
        """ Primitive extension for coverage. Type `FHIRPrimitiveExtension` """
        
        self.inforce = None
        """ Coverage inforce indicator.
        Type `bool`. """
        self._inforce = None
        """ Primitive extension for inforce. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Benefits and authorization details.
        List of `CoverageEligibilityResponseInsuranceItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityResponseInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsurance, self).elementProperties()
        js.extend([
            ("benefitPeriod", "benefitPeriod", period.Period, False, None, False),
            ("_benefitPeriod", "_benefitPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("inforce", "inforce", bool, False, None, False),
            ("_inforce", "_inforce", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", CoverageEligibilityResponseInsuranceItem, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItem(backboneelement.BackboneElement):
    """ Benefits and authorization details.
    
    Benefits and optionally current balances, and authorization details by
    category or service.
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorizationRequired = None
        """ Authorization required flag.
        Type `bool`. """
        self._authorizationRequired = None
        """ Primitive extension for authorizationRequired. Type `FHIRPrimitiveExtension` """
        
        self.authorizationSupporting = None
        """ Type of required supporting materials.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._authorizationSupporting = None
        """ Primitive extension for authorizationSupporting. Type `FHIRPrimitiveExtension` """
        
        self.authorizationUrl = None
        """ Preauthorization requirements endpoint.
        Type `str`. """
        self._authorizationUrl = None
        """ Primitive extension for authorizationUrl. Type `FHIRPrimitiveExtension` """
        
        self.benefit = None
        """ Benefit Summary.
        List of `CoverageEligibilityResponseInsuranceItemBenefit` items (represented as `dict` in JSON). """
        self._benefit = None
        """ Primitive extension for benefit. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Description of the benefit or services covered.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.excluded = None
        """ Excluded from the plan.
        Type `bool`. """
        self._excluded = None
        """ Primitive extension for excluded. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Short name for the benefit.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.network = None
        """ In or out of network.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._network = None
        """ Primitive extension for network. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.provider = None
        """ Performing practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.term = None
        """ Annual or lifetime.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._term = None
        """ Primitive extension for term. Type `FHIRPrimitiveExtension` """
        
        self.unit = None
        """ Individual or family.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._unit = None
        """ Primitive extension for unit. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityResponseInsuranceItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItem, self).elementProperties()
        js.extend([
            ("authorizationRequired", "authorizationRequired", bool, False, None, False),
            ("_authorizationRequired", "_authorizationRequired", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("authorizationSupporting", "authorizationSupporting", codeableconcept.CodeableConcept, True, None, False),
            ("_authorizationSupporting", "_authorizationSupporting", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("authorizationUrl", "authorizationUrl", str, False, None, False),
            ("_authorizationUrl", "_authorizationUrl", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("benefit", "benefit", CoverageEligibilityResponseInsuranceItemBenefit, True, None, False),
            ("_benefit", "_benefit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("excluded", "excluded", bool, False, None, False),
            ("_excluded", "_excluded", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("network", "network", codeableconcept.CodeableConcept, False, None, False),
            ("_network", "_network", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("term", "term", codeableconcept.CodeableConcept, False, None, False),
            ("_term", "_term", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
            ("_unit", "_unit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageEligibilityResponseInsuranceItemBenefit(backboneelement.BackboneElement):
    """ Benefit Summary.
    
    Benefits used to date.
    """
    
    resource_type = "CoverageEligibilityResponseInsuranceItemBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowedMoney = None
        """ Benefits allowed.
        Type `Money` (represented as `dict` in JSON). """
        self._allowedMoney = None
        """ Primitive extension for allowedMoney. Type `FHIRPrimitiveExtension` """
        
        self.allowedString = None
        """ Benefits allowed.
        Type `str`. """
        self._allowedString = None
        """ Primitive extension for allowedString. Type `FHIRPrimitiveExtension` """
        
        self.allowedUnsignedInt = None
        """ Benefits allowed.
        Type `int`. """
        self._allowedUnsignedInt = None
        """ Primitive extension for allowedUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.usedMoney = None
        """ Benefits used.
        Type `Money` (represented as `dict` in JSON). """
        self._usedMoney = None
        """ Primitive extension for usedMoney. Type `FHIRPrimitiveExtension` """
        
        self.usedString = None
        """ Benefits used.
        Type `str`. """
        self._usedString = None
        """ Primitive extension for usedString. Type `FHIRPrimitiveExtension` """
        
        self.usedUnsignedInt = None
        """ Benefits used.
        Type `int`. """
        self._usedUnsignedInt = None
        """ Primitive extension for usedUnsignedInt. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityResponseInsuranceItemBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityResponseInsuranceItemBenefit, self).elementProperties()
        js.extend([
            ("allowedMoney", "allowedMoney", money.Money, False, "allowed", False),
            ("_allowedMoney", "_allowedMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("allowedString", "allowedString", str, False, "allowed", False),
            ("_allowedString", "_allowedString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("allowedUnsignedInt", "allowedUnsignedInt", int, False, "allowed", False),
            ("_allowedUnsignedInt", "_allowedUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usedMoney", "usedMoney", money.Money, False, "used", False),
            ("_usedMoney", "_usedMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usedString", "usedString", str, False, "used", False),
            ("_usedString", "_usedString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("usedUnsignedInt", "usedUnsignedInt", int, False, "used", False),
            ("_usedUnsignedInt", "_usedUnsignedInt", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period