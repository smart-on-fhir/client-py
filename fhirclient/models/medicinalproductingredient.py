# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProductIngredient(domainresource.DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    """
    
    resource_type = "MedicinalProductIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergenicIndicator = None
        """ If the ingredient is a known or suspected allergen.
        Type `bool`. """
        self._allergenicIndicator = None
        """ Primitive extension for allergenicIndicator. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifier for the ingredient.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ Manufacturer of this Ingredient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
        self.role = None
        """ Ingredient role e.g. Active ingredient, excipient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._role = None
        """ Primitive extension for role. Type `FHIRPrimitiveExtension` """
        
        self.specifiedSubstance = None
        """ A specified substance that comprises this ingredient.
        List of `MedicinalProductIngredientSpecifiedSubstance` items (represented as `dict` in JSON). """
        self._specifiedSubstance = None
        """ Primitive extension for specifiedSubstance. Type `FHIRPrimitiveExtension` """
        
        self.substance = None
        """ The ingredient substance.
        Type `MedicinalProductIngredientSubstance` (represented as `dict` in JSON). """
        self._substance = None
        """ Primitive extension for substance. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredient, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("_allergenicIndicator", "_allergenicIndicator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("role", "role", codeableconcept.CodeableConcept, False, None, True),
            ("_role", "_role", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specifiedSubstance", "specifiedSubstance", MedicinalProductIngredientSpecifiedSubstance, True, None, False),
            ("_specifiedSubstance", "_specifiedSubstance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substance", "substance", MedicinalProductIngredientSubstance, False, None, False),
            ("_substance", "_substance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductIngredientSpecifiedSubstance(backboneelement.BackboneElement):
    """ A specified substance that comprises this ingredient.
    """
    
    resource_type = "MedicinalProductIngredientSpecifiedSubstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ The specified substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.confidentiality = None
        """ Confidentiality level of the specified substance as the ingredient.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._confidentiality = None
        """ Primitive extension for confidentiality. Type `FHIRPrimitiveExtension` """
        
        self.group = None
        """ The group of specified substance, e.g. group 1 to 4.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._group = None
        """ Primitive extension for group. Type `FHIRPrimitiveExtension` """
        
        self.strength = None
        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """
        self._strength = None
        """ Primitive extension for strength. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductIngredientSpecifiedSubstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("confidentiality", "confidentiality", codeableconcept.CodeableConcept, False, None, False),
            ("_confidentiality", "_confidentiality", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("group", "group", codeableconcept.CodeableConcept, False, None, True),
            ("_group", "_group", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
            ("_strength", "_strength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductIngredientSpecifiedSubstanceStrength(backboneelement.BackboneElement):
    """ Quantity of the substance or specified substance present in the
    manufactured item or pharmaceutical product.
    """
    
    resource_type = "MedicinalProductIngredientSpecifiedSubstanceStrength"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.concentration = None
        """ The strength per unitary volume (or mass).
        Type `Ratio` (represented as `dict` in JSON). """
        self._concentration = None
        """ Primitive extension for concentration. Type `FHIRPrimitiveExtension` """
        
        self.concentrationLowLimit = None
        """ A lower limit for the strength per unitary volume (or mass), for
        when there is a range. The concentration attribute then becomes the
        upper limit.
        Type `Ratio` (represented as `dict` in JSON). """
        self._concentrationLowLimit = None
        """ Primitive extension for concentrationLowLimit. Type `FHIRPrimitiveExtension` """
        
        self.country = None
        """ The country or countries for which the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._country = None
        """ Primitive extension for country. Type `FHIRPrimitiveExtension` """
        
        self.measurementPoint = None
        """ For when strength is measured at a particular point or distance.
        Type `str`. """
        self._measurementPoint = None
        """ Primitive extension for measurementPoint. Type `FHIRPrimitiveExtension` """
        
        self.presentation = None
        """ The quantity of substance in the unit of presentation, or in the
        volume (or mass) of the single pharmaceutical product or
        manufactured item.
        Type `Ratio` (represented as `dict` in JSON). """
        self._presentation = None
        """ Primitive extension for presentation. Type `FHIRPrimitiveExtension` """
        
        self.presentationLowLimit = None
        """ A lower limit for the quantity of substance in the unit of
        presentation. For use when there is a range of strengths, this is
        the lower limit, with the presentation attribute becoming the upper
        limit.
        Type `Ratio` (represented as `dict` in JSON). """
        self._presentationLowLimit = None
        """ Primitive extension for presentationLowLimit. Type `FHIRPrimitiveExtension` """
        
        self.referenceStrength = None
        """ Strength expressed in terms of a reference substance.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength` items (represented as `dict` in JSON). """
        self._referenceStrength = None
        """ Primitive extension for referenceStrength. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrength, self).elementProperties()
        js.extend([
            ("concentration", "concentration", ratio.Ratio, False, None, False),
            ("_concentration", "_concentration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("concentrationLowLimit", "concentrationLowLimit", ratio.Ratio, False, None, False),
            ("_concentrationLowLimit", "_concentrationLowLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("_country", "_country", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("_measurementPoint", "_measurementPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("presentation", "presentation", ratio.Ratio, False, None, True),
            ("_presentation", "_presentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("presentationLowLimit", "presentationLowLimit", ratio.Ratio, False, None, False),
            ("_presentationLowLimit", "_presentationLowLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceStrength", "referenceStrength", MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, True, None, False),
            ("_referenceStrength", "_referenceStrength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength(backboneelement.BackboneElement):
    """ Strength expressed in terms of a reference substance.
    """
    
    resource_type = "MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.country = None
        """ The country or countries for which the strength range applies.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._country = None
        """ Primitive extension for country. Type `FHIRPrimitiveExtension` """
        
        self.measurementPoint = None
        """ For when strength is measured at a particular point or distance.
        Type `str`. """
        self._measurementPoint = None
        """ Primitive extension for measurementPoint. Type `FHIRPrimitiveExtension` """
        
        self.strength = None
        """ Strength expressed in terms of a reference substance.
        Type `Ratio` (represented as `dict` in JSON). """
        self._strength = None
        """ Primitive extension for strength. Type `FHIRPrimitiveExtension` """
        
        self.strengthLowLimit = None
        """ Strength expressed in terms of a reference substance.
        Type `Ratio` (represented as `dict` in JSON). """
        self._strengthLowLimit = None
        """ Primitive extension for strengthLowLimit. Type `FHIRPrimitiveExtension` """
        
        self.substance = None
        """ Relevant reference substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._substance = None
        """ Primitive extension for substance. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSpecifiedSubstanceStrengthReferenceStrength, self).elementProperties()
        js.extend([
            ("country", "country", codeableconcept.CodeableConcept, True, None, False),
            ("_country", "_country", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measurementPoint", "measurementPoint", str, False, None, False),
            ("_measurementPoint", "_measurementPoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("strength", "strength", ratio.Ratio, False, None, True),
            ("_strength", "_strength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("strengthLowLimit", "strengthLowLimit", ratio.Ratio, False, None, False),
            ("_strengthLowLimit", "_strengthLowLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, False),
            ("_substance", "_substance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductIngredientSubstance(backboneelement.BackboneElement):
    """ The ingredient substance.
    """
    
    resource_type = "MedicinalProductIngredientSubstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ The ingredient substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.strength = None
        """ Quantity of the substance or specified substance present in the
        manufactured item or pharmaceutical product.
        List of `MedicinalProductIngredientSpecifiedSubstanceStrength` items (represented as `dict` in JSON). """
        self._strength = None
        """ Primitive extension for strength. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductIngredientSubstance, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductIngredientSubstance, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("strength", "strength", MedicinalProductIngredientSpecifiedSubstanceStrength, True, None, False),
            ("_strength", "_strength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import ratio