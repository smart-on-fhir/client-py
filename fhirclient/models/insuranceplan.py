# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/InsurancePlan).
# 2024, SMART Health IT.


from . import domainresource

class InsurancePlan(domainresource.DomainResource):
    """ Details of a Health Insurance product/plan provided by an organization.
    """
    
    resource_type = "InsurancePlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administeredBy = None
        """ Product administrator.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._administeredBy = None
        """ Primitive extension for administeredBy. Type `FHIRPrimitiveExtension` """
        
        self.alias = None
        """ Alternate names.
        List of `str` items. """
        self._alias = None
        """ Primitive extension for alias. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact for the product.
        List of `InsurancePlanContact` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.coverage = None
        """ Coverage details.
        List of `InsurancePlanCoverage` items (represented as `dict` in JSON). """
        self._coverage = None
        """ Primitive extension for coverage. Type `FHIRPrimitiveExtension` """
        
        self.coverageArea = None
        """ Where product applies.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._coverageArea = None
        """ Primitive extension for coverageArea. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Technical endpoint.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for Product.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Official name.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.network = None
        """ What networks are Included.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._network = None
        """ Primitive extension for network. Type `FHIRPrimitiveExtension` """
        
        self.ownedBy = None
        """ Plan issuer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._ownedBy = None
        """ Primitive extension for ownedBy. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ When the product is available.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.plan = None
        """ Plan details.
        List of `InsurancePlanPlan` items (represented as `dict` in JSON). """
        self._plan = None
        """ Primitive extension for plan. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of product.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlan, self).elementProperties()
        js.extend([
            ("administeredBy", "administeredBy", fhirreference.FHIRReference, False, None, False),
            ("_administeredBy", "_administeredBy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("alias", "alias", str, True, None, False),
            ("_alias", "_alias", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", InsurancePlanContact, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("coverage", "coverage", InsurancePlanCoverage, True, None, False),
            ("_coverage", "_coverage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("_coverageArea", "_coverageArea", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, True, None, False),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("_network", "_network", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ownedBy", "ownedBy", fhirreference.FHIRReference, False, None, False),
            ("_ownedBy", "_ownedBy", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("plan", "plan", InsurancePlanPlan, True, None, False),
            ("_plan", "_plan", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class InsurancePlanContact(backboneelement.BackboneElement):
    """ Contact for the product.
    
    The contact for the health insurance product for a certain purpose.
    """
    
    resource_type = "InsurancePlanContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        self._address = None
        """ Primitive extension for address. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._purpose = None
        """ Primitive extension for purpose. Type `FHIRPrimitiveExtension` """
        
        self.telecom = None
        """ Contact details (telephone, email, etc.)  for a contact.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._telecom = None
        """ Primitive extension for telecom. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanContact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanContact, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("_address", "_address", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", humanname.HumanName, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("purpose", "purpose", codeableconcept.CodeableConcept, False, None, False),
            ("_purpose", "_purpose", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("_telecom", "_telecom", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanCoverage(backboneelement.BackboneElement):
    """ Coverage details.
    
    Details about the coverage offered by the insurance product.
    """
    
    resource_type = "InsurancePlanCoverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit = None
        """ List of benefits.
        List of `InsurancePlanCoverageBenefit` items (represented as `dict` in JSON). """
        self._benefit = None
        """ Primitive extension for benefit. Type `FHIRPrimitiveExtension` """
        
        self.network = None
        """ What networks provide coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._network = None
        """ Primitive extension for network. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of coverage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanCoverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanCoverage, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanCoverageBenefit, True, None, True),
            ("_benefit", "_benefit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("_network", "_network", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanCoverageBenefit(backboneelement.BackboneElement):
    """ List of benefits.
    
    Specific benefits under this type of coverage.
    """
    
    resource_type = "InsurancePlanCoverageBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.limit = None
        """ Benefit limits.
        List of `InsurancePlanCoverageBenefitLimit` items (represented as `dict` in JSON). """
        self._limit = None
        """ Primitive extension for limit. Type `FHIRPrimitiveExtension` """
        
        self.requirement = None
        """ Referral requirements.
        Type `str`. """
        self._requirement = None
        """ Primitive extension for requirement. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of benefit.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanCoverageBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefit, self).elementProperties()
        js.extend([
            ("limit", "limit", InsurancePlanCoverageBenefitLimit, True, None, False),
            ("_limit", "_limit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("_requirement", "_requirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanCoverageBenefitLimit(backboneelement.BackboneElement):
    """ Benefit limits.
    
    The specific limits on the benefit.
    """
    
    resource_type = "InsurancePlanCoverageBenefitLimit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Benefit limit details.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ Maximum value allowed.
        Type `Quantity` (represented as `dict` in JSON). """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanCoverageBenefitLimit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanCoverageBenefitLimit, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", quantity.Quantity, False, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanPlan(backboneelement.BackboneElement):
    """ Plan details.
    
    Details about an insurance plan.
    """
    
    resource_type = "InsurancePlanPlan"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverageArea = None
        """ Where product applies.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._coverageArea = None
        """ Primitive extension for coverageArea. Type `FHIRPrimitiveExtension` """
        
        self.generalCost = None
        """ Overall costs.
        List of `InsurancePlanPlanGeneralCost` items (represented as `dict` in JSON). """
        self._generalCost = None
        """ Primitive extension for generalCost. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for Product.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.network = None
        """ What networks provide coverage.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._network = None
        """ Primitive extension for network. Type `FHIRPrimitiveExtension` """
        
        self.specificCost = None
        """ Specific costs.
        List of `InsurancePlanPlanSpecificCost` items (represented as `dict` in JSON). """
        self._specificCost = None
        """ Primitive extension for specificCost. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of plan.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanPlan, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlan, self).elementProperties()
        js.extend([
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("_coverageArea", "_coverageArea", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("generalCost", "generalCost", InsurancePlanPlanGeneralCost, True, None, False),
            ("_generalCost", "_generalCost", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("network", "network", fhirreference.FHIRReference, True, None, False),
            ("_network", "_network", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specificCost", "specificCost", InsurancePlanPlanSpecificCost, True, None, False),
            ("_specificCost", "_specificCost", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanPlanGeneralCost(backboneelement.BackboneElement):
    """ Overall costs.
    
    Overall costs associated with the plan.
    """
    
    resource_type = "InsurancePlanPlanGeneralCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comment = None
        """ Additional cost information.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.cost = None
        """ Cost value.
        Type `Money` (represented as `dict` in JSON). """
        self._cost = None
        """ Primitive extension for cost. Type `FHIRPrimitiveExtension` """
        
        self.groupSize = None
        """ Number of enrollees.
        Type `int`. """
        self._groupSize = None
        """ Primitive extension for groupSize. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of cost.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanPlanGeneralCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanGeneralCost, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("cost", "cost", money.Money, False, None, False),
            ("_cost", "_cost", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("groupSize", "groupSize", int, False, None, False),
            ("_groupSize", "_groupSize", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanPlanSpecificCost(backboneelement.BackboneElement):
    """ Specific costs.
    
    Costs associated with the coverage provided by the product.
    """
    
    resource_type = "InsurancePlanPlanSpecificCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.benefit = None
        """ Benefits list.
        List of `InsurancePlanPlanSpecificCostBenefit` items (represented as `dict` in JSON). """
        self._benefit = None
        """ Primitive extension for benefit. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ General category of benefit.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanPlanSpecificCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCost, self).elementProperties()
        js.extend([
            ("benefit", "benefit", InsurancePlanPlanSpecificCostBenefit, True, None, False),
            ("_benefit", "_benefit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanPlanSpecificCostBenefit(backboneelement.BackboneElement):
    """ Benefits list.
    
    List of the specific benefits under this category of benefit.
    """
    
    resource_type = "InsurancePlanPlanSpecificCostBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cost = None
        """ List of the costs.
        List of `InsurancePlanPlanSpecificCostBenefitCost` items (represented as `dict` in JSON). """
        self._cost = None
        """ Primitive extension for cost. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of specific benefit.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanPlanSpecificCostBenefit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefit, self).elementProperties()
        js.extend([
            ("cost", "cost", InsurancePlanPlanSpecificCostBenefitCost, True, None, False),
            ("_cost", "_cost", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class InsurancePlanPlanSpecificCostBenefitCost(backboneelement.BackboneElement):
    """ List of the costs.
    
    List of the costs associated with a specific benefit.
    """
    
    resource_type = "InsurancePlanPlanSpecificCostBenefitCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
        """ in-network | out-of-network | other.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._applicability = None
        """ Primitive extension for applicability. Type `FHIRPrimitiveExtension` """
        
        self.qualifiers = None
        """ Additional information about the cost.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._qualifiers = None
        """ Primitive extension for qualifiers. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of cost.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The actual cost value.
        Type `Quantity` (represented as `dict` in JSON). """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(InsurancePlanPlanSpecificCostBenefitCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(InsurancePlanPlanSpecificCostBenefitCost, self).elementProperties()
        js.extend([
            ("applicability", "applicability", codeableconcept.CodeableConcept, False, None, False),
            ("_applicability", "_applicability", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("qualifiers", "qualifiers", codeableconcept.CodeableConcept, True, None, False),
            ("_qualifiers", "_qualifiers", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", quantity.Quantity, False, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import address
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import humanname
from . import identifier
from . import money
from . import period
from . import quantity