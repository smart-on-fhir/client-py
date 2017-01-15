#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.8.0.10521 (http://hl7.org/fhir/StructureDefinition/NutritionRequest) on 2017-01-15.
#  2017, SMART Health IT.


from . import domainresource

class NutritionRequest(domainresource.DomainResource):
    """ Diet, formula or nutritional supplement request.
    
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    
    resource_type = "NutritionRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergyIntolerance = None
        """ List of the patient's food and nutrition-related allergies and
        intolerances.
        List of `FHIRReference` items referencing `AllergyIntolerance` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ Date and time the nutrition order was requested.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ The encounter associated with this nutrition order.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.enteralFormula = None
        """ Enteral formula components.
        Type `NutritionRequestEnteralFormula` (represented as `dict` in JSON). """
        
        self.excludeFoodModifier = None
        """ Order-specific modifier about the type of food that should not be
        given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.foodPreferenceModifier = None
        """ Order-specific modifier about the type of food that should be given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.oralDiet = None
        """ Oral diet components.
        Type `NutritionRequestOralDiet` (represented as `dict` in JSON). """
        
        self.orderer = None
        """ Who ordered the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The person who requires the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | draft | planned | requested | active | on-hold |
        completed | cancelled | entered-in-error.
        Type `str`. """
        
        self.supplement = None
        """ Supplement components.
        List of `NutritionRequestSupplement` items (represented as `dict` in JSON). """
        
        super(NutritionRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionRequest, self).elementProperties()
        js.extend([
            ("allergyIntolerance", "allergyIntolerance", fhirreference.FHIRReference, True, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("enteralFormula", "enteralFormula", NutritionRequestEnteralFormula, False, None, False),
            ("excludeFoodModifier", "excludeFoodModifier", codeableconcept.CodeableConcept, True, None, False),
            ("foodPreferenceModifier", "foodPreferenceModifier", codeableconcept.CodeableConcept, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("oralDiet", "oralDiet", NutritionRequestOralDiet, False, None, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("status", "status", str, False, None, False),
            ("supplement", "supplement", NutritionRequestSupplement, True, None, False),
        ])
        return js


from . import backboneelement

class NutritionRequestEnteralFormula(backboneelement.BackboneElement):
    """ Enteral formula components.
    
    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """
    
    resource_type = "NutritionRequestEnteralFormula"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveProductName = None
        """ Product or brand name of the modular additive.
        Type `str`. """
        
        self.additiveType = None
        """ Type of modular component to add to the feeding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.administration = None
        """ Formula feeding instruction as structured data.
        List of `NutritionRequestEnteralFormulaAdministration` items (represented as `dict` in JSON). """
        
        self.administrationInstruction = None
        """ Formula feeding instructions expressed as text.
        Type `str`. """
        
        self.baseFormulaProductName = None
        """ Product or brand name of the enteral or infant formula.
        Type `str`. """
        
        self.baseFormulaType = None
        """ Type of enteral or infant formula.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.caloricDensity = None
        """ Amount of energy per specified volume that is required.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.maxVolumeToDeliver = None
        """ Upper limit on formula volume per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.routeofAdministration = None
        """ How the formula should enter the patient's gastrointestinal tract.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionRequestEnteralFormula, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionRequestEnteralFormula, self).elementProperties()
        js.extend([
            ("additiveProductName", "additiveProductName", str, False, None, False),
            ("additiveType", "additiveType", codeableconcept.CodeableConcept, False, None, False),
            ("administration", "administration", NutritionRequestEnteralFormulaAdministration, True, None, False),
            ("administrationInstruction", "administrationInstruction", str, False, None, False),
            ("baseFormulaProductName", "baseFormulaProductName", str, False, None, False),
            ("baseFormulaType", "baseFormulaType", codeableconcept.CodeableConcept, False, None, False),
            ("caloricDensity", "caloricDensity", quantity.Quantity, False, None, False),
            ("maxVolumeToDeliver", "maxVolumeToDeliver", quantity.Quantity, False, None, False),
            ("routeofAdministration", "routeofAdministration", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class NutritionRequestEnteralFormulaAdministration(backboneelement.BackboneElement):
    """ Formula feeding instruction as structured data.
    
    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """
    
    resource_type = "NutritionRequestEnteralFormulaAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None
        """ The volume of formula to provide.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateQuantity = None
        """ Speed with which the formula is provided per period of time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rateRatio = None
        """ Speed with which the formula is provided per period of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ Scheduled frequency of enteral feeding.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(NutritionRequestEnteralFormulaAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionRequestEnteralFormulaAdministration, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("schedule", "schedule", timing.Timing, False, None, False),
        ])
        return js


class NutritionRequestOralDiet(backboneelement.BackboneElement):
    """ Oral diet components.
    
    Diet given orally in contrast to enteral (tube) feeding.
    """
    
    resource_type = "NutritionRequestOralDiet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.fluidConsistencyType = None
        """ The required consistency of fluids and liquids provided to the
        patient.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.instruction = None
        """ Instructions or additional information about the oral diet.
        Type `str`. """
        
        self.nutrient = None
        """ Required  nutrient modifications.
        List of `NutritionRequestOralDietNutrient` items (represented as `dict` in JSON). """
        
        self.schedule = None
        """ Scheduled frequency of diet.
        List of `Timing` items (represented as `dict` in JSON). """
        
        self.texture = None
        """ Required  texture modifications.
        List of `NutritionRequestOralDietTexture` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of oral diet or diet restrictions that describe what can be
        consumed orally.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(NutritionRequestOralDiet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionRequestOralDiet, self).elementProperties()
        js.extend([
            ("fluidConsistencyType", "fluidConsistencyType", codeableconcept.CodeableConcept, True, None, False),
            ("instruction", "instruction", str, False, None, False),
            ("nutrient", "nutrient", NutritionRequestOralDietNutrient, True, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("texture", "texture", NutritionRequestOralDietTexture, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class NutritionRequestOralDietNutrient(backboneelement.BackboneElement):
    """ Required  nutrient modifications.
    
    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """
    
    resource_type = "NutritionRequestOralDietNutrient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Quantity of the specified nutrient.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Type of nutrient that is being modified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionRequestOralDietNutrient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionRequestOralDietNutrient, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class NutritionRequestOralDietTexture(backboneelement.BackboneElement):
    """ Required  texture modifications.
    
    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    
    resource_type = "NutritionRequestOralDietTexture"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.foodType = None
        """ Concepts that are used to identify an entity that is ingested for
        nutritional purposes.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modifier = None
        """ Code to indicate how to alter the texture of the foods, e.g. pureed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionRequestOralDietTexture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionRequestOralDietTexture, self).elementProperties()
        js.extend([
            ("foodType", "foodType", codeableconcept.CodeableConcept, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class NutritionRequestSupplement(backboneelement.BackboneElement):
    """ Supplement components.
    
    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """
    
    resource_type = "NutritionRequestSupplement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instruction = None
        """ Instructions or additional information about the oral supplement.
        Type `str`. """
        
        self.productName = None
        """ Product or brand name of the nutritional supplement.
        Type `str`. """
        
        self.quantity = None
        """ Amount of the nutritional supplement.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ Scheduled frequency of supplement.
        List of `Timing` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of supplement product requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionRequestSupplement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionRequestSupplement, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("productName", "productName", str, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio
from . import timing
