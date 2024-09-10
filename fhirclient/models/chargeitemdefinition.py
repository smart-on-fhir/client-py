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
        self._applicability = None
        """ Primitive extension for applicability. Type `FHIRPrimitiveExtension` """
        
        self.approvalDate = None
        """ When the charge item definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._approvalDate = None
        """ Primitive extension for approvalDate. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Billing codes or product types this definition applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """
        self._copyright = None
        """ Primitive extension for copyright. Type `FHIRPrimitiveExtension` """
        
        self.date = None
        """ Date last changed.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._date = None
        """ Primitive extension for date. Type `FHIRPrimitiveExtension` """
        
        self.derivedFromUri = None
        """ Underlying externally-defined charge item definition.
        List of `str` items. """
        self._derivedFromUri = None
        """ Primitive extension for derivedFromUri. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Natural language description of the charge item definition.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.effectivePeriod = None
        """ When the charge item definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """
        self._effectivePeriod = None
        """ Primitive extension for effectivePeriod. Type `FHIRPrimitiveExtension` """
        
        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """
        self._experimental = None
        """ Primitive extension for experimental. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Additional identifier for the charge item definition.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instance = None
        """ Instances this definition applies to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._instance = None
        """ Primitive extension for instance. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Intended jurisdiction for charge item definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        self.lastReviewDate = None
        """ When the charge item definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._lastReviewDate = None
        """ Primitive extension for lastReviewDate. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ A larger definition of which this particular definition is a
        component or step.
        List of `str` items. """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.propertyGroup = None
        """ Group of properties which are applicable under the same conditions.
        List of `ChargeItemDefinitionPropertyGroup` items (represented as `dict` in JSON). """
        self._propertyGroup = None
        """ Primitive extension for propertyGroup. Type `FHIRPrimitiveExtension` """
        
        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """
        self._publisher = None
        """ Primitive extension for publisher. Type `FHIRPrimitiveExtension` """
        
        self.replaces = None
        """ Completed or terminated request(s) whose function is taken by this
        new request.
        List of `str` items. """
        self._replaces = None
        """ Primitive extension for replaces. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Name for this charge item definition (human friendly).
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Canonical identifier for this charge item definition, represented
        as a URI (globally unique).
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """
        self._useContext = None
        """ Primitive extension for useContext. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Business version of the charge item definition.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(ChargeItemDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinition, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("_applicability", "_applicability", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("approvalDate", "approvalDate", fhirdate.FHIRDate, False, None, False),
            ("_approvalDate", "_approvalDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactdetail.ContactDetail, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("_copyright", "_copyright", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("date", "date", fhirdatetime.FHIRDateTime, False, None, False),
            ("_date", "_date", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("derivedFromUri", "derivedFromUri", str, True, None, False),
            ("_derivedFromUri", "_derivedFromUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effectivePeriod", "effectivePeriod", period.Period, False, None, False),
            ("_effectivePeriod", "_effectivePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("_experimental", "_experimental", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instance", "instance", fhirreference.FHIRReference, True, None, False),
            ("_instance", "_instance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, True, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lastReviewDate", "lastReviewDate", fhirdate.FHIRDate, False, None, False),
            ("_lastReviewDate", "_lastReviewDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", str, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("propertyGroup", "propertyGroup", ChargeItemDefinitionPropertyGroup, True, None, False),
            ("_propertyGroup", "_propertyGroup", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("_publisher", "_publisher", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("_replaces", "_replaces", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, True),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("useContext", "useContext", usagecontext.UsageContext, True, None, False),
            ("_useContext", "_useContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.expression = None
        """ Boolean-valued expression.
        Type `str`. """
        self._expression = None
        """ Primitive extension for expression. Type `FHIRPrimitiveExtension` """
        
        self.language = None
        """ Language of the expression.
        Type `str`. """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        super(ChargeItemDefinitionApplicability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionApplicability, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expression", "expression", str, False, None, False),
            ("_expression", "_expression", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("language", "language", str, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._applicability = None
        """ Primitive extension for applicability. Type `FHIRPrimitiveExtension` """
        
        self.priceComponent = None
        """ Components of total line item price.
        List of `ChargeItemDefinitionPropertyGroupPriceComponent` items (represented as `dict` in JSON). """
        self._priceComponent = None
        """ Primitive extension for priceComponent. Type `FHIRPrimitiveExtension` """
        
        super(ChargeItemDefinitionPropertyGroup, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroup, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("_applicability", "_applicability", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priceComponent", "priceComponent", ChargeItemDefinitionPropertyGroupPriceComponent, True, None, False),
            ("_priceComponent", "_priceComponent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code identifying the specific component.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Factor used for calculating this component.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ base | surcharge | deduction | discount | tax | informational.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(ChargeItemDefinitionPropertyGroupPriceComponent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroupPriceComponent, self).elementProperties()
        js.extend([
            ("amount", "amount", money.Money, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import contactdetail
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import money
from . import period
from . import usagecontext