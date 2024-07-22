# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition).
# 2024, SMART Health IT.


from . import domainresource

class ChargeItemDefinition(domainresource.DomainResource):
    """ Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.
    
    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """
    
    resource_type = "ChargeItemDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
        """ Whether or not the billing code is applicable.
        List of `ChargeItemDefinitionApplicability` items (represented as `dict` in JSON). """
        
        self.approvalDate = None
        """ When the charge item definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.code = None
        """ Billing codes or product types this definition applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        
        self.derivedFromUri = None
        """ Underlying externally-defined charge item definition.
        List of `str` items. """
        
        self.description = None
        """ Natural language description of the charge item definition.
        Type `str`. """
        
        self.effectivePeriod = None
        """ When the charge item definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        
        self.identifier = None
        """ Additional identifier for the charge item definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ Instances this definition applies to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.jurisdiction = None
        """ Intended jurisdiction for charge item definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.lastReviewDate = None
        """ When the charge item definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.partOf = None
        """ A larger definition of which this particular definition is a
        component or step.
        List of `str` items. """
        
        self.propertyGroup = None
        """ Group of properties which are applicable under the same conditions.
        List of `ChargeItemDefinitionPropertyGroup` items (represented as `dict` in JSON). """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.replaces = None
        """ Completed or terminated request(s) whose function is taken by this
        new request.
        List of `str` items. """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        
        self.title = None
        """ Name for this charge item definition (human friendly).
        Type `str`. """
        
        self.url = None
        """ Canonical identifier for this charge item definition, represented
        as a URI (globally unique).
        Type `str`. """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        
        self.version = None
        """ Business version of the charge item definition.
        Type `str`. """
        
        super(ChargeItemDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinition, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("derivedFromUri", "derivedFromUri", str, True, None, False),
            ("description", "description", str, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("instance", "instance", fhirreference.FHIRReference, True, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("partOf", "partOf", str, True, None, False),
            ("propertyGroup", "propertyGroup", ChargeItemDefinitionPropertyGroup, True, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("title", "title", str, False, None, False),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ChargeItemDefinitionApplicability(backboneelement.BackboneElement):
    """ Whether or not the billing code is applicable.
    
    Expressions that describe applicability criteria for the billing code.
    """
    
    resource_type = "ChargeItemDefinitionApplicability"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Natural language description of the condition.
        Type `str`. """
        
        self.expression = None
        """ Boolean-valued expression.
        Type `str`. """
        
        self.language = None
        """ Language of the expression.
        Type `str`. """
        
        super(ChargeItemDefinitionApplicability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionApplicability, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("language", "language", str, False, None, False),
        ])
        return js


class ChargeItemDefinitionPropertyGroup(backboneelement.BackboneElement):
    """ Group of properties which are applicable under the same conditions.
    
    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """
    
    resource_type = "ChargeItemDefinitionPropertyGroup"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.applicability = None
        """ Conditions under which the priceComponent is applicable.
        List of `ChargeItemDefinitionApplicability` items (represented as `dict` in JSON). """
        
        self.priceComponent = None
        """ Components of total line item price.
        List of `ChargeItemDefinitionPropertyGroupPriceComponent` items (represented as `dict` in JSON). """
        
        super(ChargeItemDefinitionPropertyGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroup, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("priceComponent", "priceComponent", ChargeItemDefinitionPropertyGroupPriceComponent, True, None, False),
        ])
        return js


class ChargeItemDefinitionPropertyGroupPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.
    
    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """
    
    resource_type = "ChargeItemDefinitionPropertyGroupPriceComponent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Monetary amount associated with this component.
        Type `Money` (represented as `dict` in JSON). """
        
        self.code = None
        """ Code identifying the specific component.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.factor = None
        """ Factor used for calculating this component.
        Type `float`. """
        
        self.type = None
        """ base | surcharge | deduction | discount | tax | informational.
        Type `str`. """
        
        super(ChargeItemDefinitionPropertyGroupPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroupPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import usagecontext
