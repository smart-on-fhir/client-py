# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest).
# 2024, SMART Health IT.


from . import domainresource

class CoverageEligibilityRequest(domainresource.DomainResource):
    """ CoverageEligibilityRequest resource.
    
    The CoverageEligibilityRequest provides patient and insurance coverage
    information to an insurer for them to respond, in the form of an
    CoverageEligibilityResponse, with information regarding whether the stated
    coverage is valid and in-force and optionally to provide the insurance
    details of the policy.
    """
    
    resource_type = "CoverageEligibilityRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ Creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.enterer = None
        """ Author.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._enterer = None
        """ Primitive extension for enterer. Type `FHIRPrimitiveExtension` """
        
        self.facility = None
        """ Servicing facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._facility = None
        """ Primitive extension for facility. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for coverage eligiblity request.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.insurance = None
        """ Patient insurance information.
        List of `CoverageEligibilityRequestInsurance` items (represented as `dict` in JSON). """
        self._insurance = None
        """ Primitive extension for insurance. Type `FHIRPrimitiveExtension` """
        
        self.insurer = None
        """ Coverage issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._insurer = None
        """ Primitive extension for insurer. Type `FHIRPrimitiveExtension` """
        
        self.item = None
        """ Item to be evaluated for eligibiity.
        List of `CoverageEligibilityRequestItem` items (represented as `dict` in JSON). """
        self._item = None
        """ Primitive extension for item. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Intended recipient of products and services.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ Desired processing priority.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.provider = None
        """ Party responsible for the request.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ auth-requirements | benefits | discovery | validation.
        List of `str` items. """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
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
        
        self.supportingInfo = None
        """ Supporting information.
        List of `CoverageEligibilityRequestSupportingInfo` items (represented as `dict` in JSON). """
        self._supportingInfo = None
        """ Primitive extension for supportingInfo. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequest, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("_enterer", "_enterer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("_facility", "_facility", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurance", "insurance", CoverageEligibilityRequestInsurance, True, None, False),
            ("_insurance", "_insurance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("insurer", "insurer", fhirreference.FHIRReference, False, None, True),
            ("_insurer", "_insurer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("item", "item", CoverageEligibilityRequestItem, True, None, False),
            ("_item", "_item", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", str, True, None, True),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedDate", "servicedDate", fhirdate.FHIRDate, False, "serviced", False),
            ("_servicedDate", "_servicedDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("servicedPeriod", "servicedPeriod", period.Period, False, "serviced", False),
            ("_servicedPeriod", "_servicedPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfo", "supportingInfo", CoverageEligibilityRequestSupportingInfo, True, None, False),
            ("_supportingInfo", "_supportingInfo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class CoverageEligibilityRequestInsurance(backboneelement.BackboneElement):
    """ Patient insurance information.
    
    Financial instruments for reimbursement for the health care products and
    services.
    """
    
    resource_type = "CoverageEligibilityRequestInsurance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.businessArrangement = None
        """ Additional provider contract number.
        Type `str`. """
        self._businessArrangement = None
        """ Primitive extension for businessArrangement. Type `FHIRPrimitiveExtension` """
        
        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._coverage = None
        """ Primitive extension for coverage. Type `FHIRPrimitiveExtension` """
        
        self.focal = None
        """ Applicable coverage.
        Type `bool`. """
        self._focal = None
        """ Primitive extension for focal. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityRequestInsurance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestInsurance, self).elementProperties()
        js.extend([
            ("businessArrangement", "businessArrangement", str, False, None, False),
            ("_businessArrangement", "_businessArrangement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focal", "focal", bool, False, None, False),
            ("_focal", "_focal", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItem(backboneelement.BackboneElement):
    """ Item to be evaluated for eligibiity.
    
    Service categories or billable services for which benefit details and/or an
    authorization prior to service delivery may be required by the payor.
    """
    
    resource_type = "CoverageEligibilityRequestItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ Benefit classification.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.detail = None
        """ Product or service details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._detail = None
        """ Primitive extension for detail. Type `FHIRPrimitiveExtension` """
        
        self.diagnosis = None
        """ Applicable diagnosis.
        List of `CoverageEligibilityRequestItemDiagnosis` items (represented as `dict` in JSON). """
        self._diagnosis = None
        """ Primitive extension for diagnosis. Type `FHIRPrimitiveExtension` """
        
        self.facility = None
        """ Servicing facility.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._facility = None
        """ Primitive extension for facility. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Product or service billing modifiers.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        self.productOrService = None
        """ Billing, service, product, or drug code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._productOrService = None
        """ Primitive extension for productOrService. Type `FHIRPrimitiveExtension` """
        
        self.provider = None
        """ Perfoming practitioner.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._provider = None
        """ Primitive extension for provider. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Count of products or services.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.supportingInfoSequence = None
        """ Applicable exception or supporting information.
        List of `int` items. """
        self._supportingInfoSequence = None
        """ Primitive extension for supportingInfoSequence. Type `FHIRPrimitiveExtension` """
        
        self.unitPrice = None
        """ Fee, charge or cost per item.
        Type `Money` (represented as `dict` in JSON). """
        self._unitPrice = None
        """ Primitive extension for unitPrice. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityRequestItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestItem, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("detail", "detail", fhirreference.FHIRReference, True, None, False),
            ("_detail", "_detail", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnosis", "diagnosis", CoverageEligibilityRequestItemDiagnosis, True, None, False),
            ("_diagnosis", "_diagnosis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("facility", "facility", fhirreference.FHIRReference, False, None, False),
            ("_facility", "_facility", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, True, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productOrService", "productOrService", codeableconcept.CodeableConcept, False, None, False),
            ("_productOrService", "_productOrService", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("_provider", "_provider", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supportingInfoSequence", "supportingInfoSequence", int, True, None, False),
            ("_supportingInfoSequence", "_supportingInfoSequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unitPrice", "unitPrice", money.Money, False, None, False),
            ("_unitPrice", "_unitPrice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageEligibilityRequestItemDiagnosis(backboneelement.BackboneElement):
    """ Applicable diagnosis.
    
    Patient diagnosis for which care is sought.
    """
    
    resource_type = "CoverageEligibilityRequestItemDiagnosis"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.diagnosisCodeableConcept = None
        """ Nature of illness or problem.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._diagnosisCodeableConcept = None
        """ Primitive extension for diagnosisCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.diagnosisReference = None
        """ Nature of illness or problem.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._diagnosisReference = None
        """ Primitive extension for diagnosisReference. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityRequestItemDiagnosis, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestItemDiagnosis, self).elementProperties()
        js.extend([
            ("diagnosisCodeableConcept", "diagnosisCodeableConcept", codeableconcept.CodeableConcept, False, "diagnosis", False),
            ("_diagnosisCodeableConcept", "_diagnosisCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diagnosisReference", "diagnosisReference", fhirreference.FHIRReference, False, "diagnosis", False),
            ("_diagnosisReference", "_diagnosisReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageEligibilityRequestSupportingInfo(backboneelement.BackboneElement):
    """ Supporting information.
    
    Additional information codes regarding exceptions, special considerations,
    the condition, situation, prior or concurrent issues.
    """
    
    resource_type = "CoverageEligibilityRequestSupportingInfo"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appliesToAll = None
        """ Applies to all items.
        Type `bool`. """
        self._appliesToAll = None
        """ Primitive extension for appliesToAll. Type `FHIRPrimitiveExtension` """
        
        self.information = None
        """ Data to be provided.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._information = None
        """ Primitive extension for information. Type `FHIRPrimitiveExtension` """
        
        self.sequence = None
        """ Information instance identifier.
        Type `int`. """
        self._sequence = None
        """ Primitive extension for sequence. Type `FHIRPrimitiveExtension` """
        
        super(CoverageEligibilityRequestSupportingInfo, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageEligibilityRequestSupportingInfo, self).elementProperties()
        js.extend([
            ("appliesToAll", "appliesToAll", bool, False, None, False),
            ("_appliesToAll", "_appliesToAll", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("information", "information", fhirreference.FHIRReference, False, None, True),
            ("_information", "_information", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sequence", "sequence", int, False, None, True),
            ("_sequence", "_sequence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
from . import quantity