# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Substance).
# 2024, SMART Health IT.


from . import domainresource

class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """
    
    resource_type = "Substance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None
        """ What class/type of substance this is.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ What substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Textual description of the substance, comments.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.ingredient = None
        """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """
        self._ingredient = None
        """ Primitive extension for ingredient. Type `FHIRPrimitiveExtension` """
        
        self.instance = None
        """ If this describes a specific package/container of the substance.
        List of `SubstanceInstance` items (represented as `dict` in JSON). """
        self._instance = None
        """ Primitive extension for instance. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(Substance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False),
            ("_ingredient", "_ingredient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instance", "instance", SubstanceInstance, True, None, False),
            ("_instance", "_instance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.
    
    A substance can be composed of other substances.
    """
    
    resource_type = "SubstanceIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None
        """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.substanceCodeableConcept = None
        """ A component of the substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._substanceCodeableConcept = None
        """ Primitive extension for substanceCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.substanceReference = None
        """ A component of the substance.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._substanceReference = None
        """ Primitive extension for substanceReference. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substanceCodeableConcept", "substanceCodeableConcept", codeableconcept.CodeableConcept, False, "substance", True),
            ("_substanceCodeableConcept", "_substanceCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substanceReference", "substanceReference", fhirreference.FHIRReference, False, "substance", True),
            ("_substanceReference", "_substanceReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.
    
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    
    resource_type = "SubstanceInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expiry = None
        """ When no longer valid to use.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._expiry = None
        """ Primitive extension for expiry. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Amount of substance in the package.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceInstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("expiry", "expiry", fhirdatetime.FHIRDateTime, False, None, False),
            ("_expiry", "_expiry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio