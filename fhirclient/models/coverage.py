# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Coverage).
# 2024, SMART Health IT.


from . import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.
    
    Financial instrument which may be used to reimburse or pay for health care
    products and services. Includes both insurance and self-payment.
    """
    
    resource_type = "Coverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.beneficiary = None
        """ Plan beneficiary.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._beneficiary = None
        """ Primitive extension for beneficiary. Type `FHIRPrimitiveExtension` """
        
        self.class_fhir = None
        """ Additional coverage classifications.
        List of `CoverageClass` items (represented as `dict` in JSON). """
        self._class_fhir = None
        """ Primitive extension for class_fhir. Type `FHIRPrimitiveExtension` """
        
        self.contract = None
        """ Contract details.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._contract = None
        """ Primitive extension for contract. Type `FHIRPrimitiveExtension` """
        
        self.costToBeneficiary = None
        """ Patient payments for services/products.
        List of `CoverageCostToBeneficiary` items (represented as `dict` in JSON). """
        self._costToBeneficiary = None
        """ Primitive extension for costToBeneficiary. Type `FHIRPrimitiveExtension` """
        
        self.dependent = None
        """ Dependent number.
        Type `str`. """
        self._dependent = None
        """ Primitive extension for dependent. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for the coverage.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.network = None
        """ Insurer network.
        Type `str`. """
        self._network = None
        """ Primitive extension for network. Type `FHIRPrimitiveExtension` """
        
        self.order = None
        """ Relative order of the coverage.
        Type `int`. """
        self._order = None
        """ Primitive extension for order. Type `FHIRPrimitiveExtension` """
        
        self.payor = None
        """ Issuer of the policy.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._payor = None
        """ Primitive extension for payor. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.policyHolder = None
        """ Owner of the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._policyHolder = None
        """ Primitive extension for policyHolder. Type `FHIRPrimitiveExtension` """
        
        self.relationship = None
        """ Beneficiary relationship to the subscriber.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._relationship = None
        """ Primitive extension for relationship. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.subrogation = None
        """ Reimbursement to insurer.
        Type `bool`. """
        self._subrogation = None
        """ Primitive extension for subrogation. Type `FHIRPrimitiveExtension` """
        
        self.subscriber = None
        """ Subscriber to the policy.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subscriber = None
        """ Primitive extension for subscriber. Type `FHIRPrimitiveExtension` """
        
        self.subscriberId = None
        """ ID assigned to the subscriber.
        Type `str`. """
        self._subscriberId = None
        """ Primitive extension for subscriberId. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Coverage category such as medical or accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("beneficiary", "beneficiary", fhirreference.FHIRReference, False, None, True),
            ("_beneficiary", "_beneficiary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("class_fhir", "class", CoverageClass, True, None, False),
            ("_class_fhir", "_class_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("_contract", "_contract", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("costToBeneficiary", "costToBeneficiary", CoverageCostToBeneficiary, True, None, False),
            ("_costToBeneficiary", "_costToBeneficiary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dependent", "dependent", str, False, None, False),
            ("_dependent", "_dependent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("network", "network", str, False, None, False),
            ("_network", "_network", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("order", "order", int, False, None, False),
            ("_order", "_order", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payor", "payor", fhirreference.FHIRReference, True, None, True),
            ("_payor", "_payor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("policyHolder", "policyHolder", fhirreference.FHIRReference, False, None, False),
            ("_policyHolder", "_policyHolder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, False),
            ("_relationship", "_relationship", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subrogation", "subrogation", bool, False, None, False),
            ("_subrogation", "_subrogation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False),
            ("_subscriber", "_subscriber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subscriberId", "subscriberId", str, False, None, False),
            ("_subscriberId", "_subscriberId", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class CoverageClass(backboneelement.BackboneElement):
    """ Additional coverage classifications.
    
    A suite of underwriter specific classifiers.
    """
    
    resource_type = "CoverageClass"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Human readable description of the type and value.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of class such as 'group' or 'plan'.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Value associated with the type.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(CoverageClass, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageClass, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageCostToBeneficiary(backboneelement.BackboneElement):
    """ Patient payments for services/products.
    
    A suite of codes indicating the cost category and associated amount which
    have been detailed in the policy and may have been  included on the health
    card.
    """
    
    resource_type = "CoverageCostToBeneficiary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exception = None
        """ Exceptions for patient payments.
        List of `CoverageCostToBeneficiaryException` items (represented as `dict` in JSON). """
        self._exception = None
        """ Primitive extension for exception. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Cost category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.valueMoney = None
        """ The amount or percentage due from the beneficiary.
        Type `Money` (represented as `dict` in JSON). """
        self._valueMoney = None
        """ Primitive extension for valueMoney. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ The amount or percentage due from the beneficiary.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        super(CoverageCostToBeneficiary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageCostToBeneficiary, self).elementProperties()
        js.extend([
            ("exception", "exception", CoverageCostToBeneficiaryException, True, None, False),
            ("_exception", "_exception", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueMoney", "valueMoney", money.Money, False, "value", True),
            ("_valueMoney", "_valueMoney", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class CoverageCostToBeneficiaryException(backboneelement.BackboneElement):
    """ Exceptions for patient payments.
    
    A suite of codes indicating exceptions or reductions to patient costs and
    their effective periods.
    """
    
    resource_type = "CoverageCostToBeneficiaryException"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ The effective period of the exception.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Exception category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(CoverageCostToBeneficiaryException, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CoverageCostToBeneficiaryException, self).elementProperties()
        js.extend([
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import quantity