#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/NutritionOrder) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio
from . import timing


class NutritionOrder(domainresource.DomainResource):
    """ A request for a diet, formula or nutritional supplement.
    
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    
    resource_name = "NutritionOrder"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.allergyIntolerance = None
        """ List of the patient's food and nutrition-related allergies and
        intolerances.
        List of `FHIRReference` items referencing `AllergyIntolerance` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ Date and time the nutrition order was requested.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None
        """ The encounter associated with that this nutrition order.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.enteralFormula = None
        """ Enteral formula components.
        Type `NutritionOrderEnteralFormula` (represented as `dict` in JSON). """
        
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
        Type `NutritionOrderOralDiet` (represented as `dict` in JSON). """
        
        self.orderer = None
        """ Who ordered the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.patient = None
        """ The person who requires the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | draft | planned | requested | active | on-hold |
        completed | cancelled.
        Type `str`. """
        
        self.supplement = None
        """ Supplement components.
        List of `NutritionOrderSupplement` items (represented as `dict` in JSON). """
        
        super(NutritionOrder, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NutritionOrder, self).elementProperties()
        js.extend([
            ("allergyIntolerance", "allergyIntolerance", fhirreference.FHIRReference, True),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("enteralFormula", "enteralFormula", NutritionOrderEnteralFormula, False),
            ("excludeFoodModifier", "excludeFoodModifier", codeableconcept.CodeableConcept, True),
            ("foodPreferenceModifier", "foodPreferenceModifier", codeableconcept.CodeableConcept, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("oralDiet", "oralDiet", NutritionOrderOralDiet, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("supplement", "supplement", NutritionOrderSupplement, True),
        ])
        return js


class NutritionOrderEnteralFormula(fhirelement.FHIRElement):
    """ Enteral formula components.
    
    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """
    
    resource_name = "NutritionOrderEnteralFormula"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additiveProductName = None
        """ Product or brand name of the modular additive.
        Type `str`. """
        
        self.additiveType = None
        """ Type of modular component to add to the feeding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.administrationInstructions = None
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
        
        self.quantity = None
        """ The volume of formula to provide.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.rate = None
        """ Speed with which the formula is provided per period of time.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.rateAdjustment = None
        """ Change in the rate of administration over a given time.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.routeofAdministration = None
        """ How the formula should enter the patient's gastrointestinal tract.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.scheduled = None
        """ Scheduled frequency of enteral feeding.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(NutritionOrderEnteralFormula, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NutritionOrderEnteralFormula, self).elementProperties()
        js.extend([
            ("additiveProductName", "additiveProductName", str, False),
            ("additiveType", "additiveType", codeableconcept.CodeableConcept, False),
            ("administrationInstructions", "administrationInstructions", str, False),
            ("baseFormulaProductName", "baseFormulaProductName", str, False),
            ("baseFormulaType", "baseFormulaType", codeableconcept.CodeableConcept, False),
            ("caloricDensity", "caloricDensity", quantity.Quantity, False),
            ("maxVolumeToDeliver", "maxVolumeToDeliver", quantity.Quantity, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("rate", "rate", ratio.Ratio, False),
            ("rateAdjustment", "rateAdjustment", quantity.Quantity, False),
            ("routeofAdministration", "routeofAdministration", codeableconcept.CodeableConcept, False),
            ("scheduled", "scheduled", timing.Timing, False),
        ])
        return js


class NutritionOrderOralDiet(fhirelement.FHIRElement):
    """ Oral diet components.
    
    Diet given orally in contrast to enteral (tube) feeding.
    """
    
    resource_name = "NutritionOrderOralDiet"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        List of `NutritionOrderOralDietNutrient` items (represented as `dict` in JSON). """
        
        self.scheduled = None
        """ Scheduled frequency of diet.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.texture = None
        """ Required  texture modifications.
        List of `NutritionOrderOralDietTexture` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of oral diet or diet restrictions that describe what can be
        consumed orally.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(NutritionOrderOralDiet, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDiet, self).elementProperties()
        js.extend([
            ("fluidConsistencyType", "fluidConsistencyType", codeableconcept.CodeableConcept, True),
            ("instruction", "instruction", str, False),
            ("nutrient", "nutrient", NutritionOrderOralDietNutrient, True),
            ("scheduled", "scheduled", timing.Timing, False),
            ("texture", "texture", NutritionOrderOralDietTexture, True),
            ("type", "type", codeableconcept.CodeableConcept, True),
        ])
        return js


class NutritionOrderOralDietNutrient(fhirelement.FHIRElement):
    """ Required  nutrient modifications.
    
    Class that defines the quantity and type of nutrient modifications required
    for the oral diet.
    """
    
    resource_name = "NutritionOrderOralDietNutrient"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Quantity of the specified nutrient.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.mod = None
        """ Type of nutrient that is being modified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderOralDietNutrient, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDietNutrient, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("mod", "modifier", codeableconcept.CodeableConcept, False),
        ])
        return js


class NutritionOrderOralDietTexture(fhirelement.FHIRElement):
    """ Required  texture modifications.
    
    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    
    resource_name = "NutritionOrderOralDietTexture"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.foodType = None
        """ Concepts that are used to identify an entity that is ingested for
        nutritional purposes.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.mod = None
        """ Code to indicate how to alter the texture of the foods, e.g.,
        pureed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderOralDietTexture, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDietTexture, self).elementProperties()
        js.extend([
            ("foodType", "foodType", codeableconcept.CodeableConcept, False),
            ("mod", "modifier", codeableconcept.CodeableConcept, False),
        ])
        return js


class NutritionOrderSupplement(fhirelement.FHIRElement):
    """ Supplement components.
    
    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """
    
    resource_name = "NutritionOrderSupplement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        self.scheduled = None
        """ Scheduled frequency of supplement.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of supplement product requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderSupplement, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(NutritionOrderSupplement, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False),
            ("productName", "productName", str, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("scheduled", "scheduled", timing.Timing, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

