#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (nutritionorder.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import period
import quantity
import range
import ratio
import timing


class NutritionOrder(fhirresource.FHIRResource):
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
        
        self.item = None
        """ Set of nutrition items or components that comprise the nutrition
        order.
        List of `NutritionOrderItem` items (represented as `dict` in JSON). """
        
        self.orderer = None
        """ Who ordered the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | active | inactive | held | cancelled.
        Type `str`. """
        
        self.subject = None
        """ The person who requires the diet, formula or nutritional supplement.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(NutritionOrder, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NutritionOrder, self).update_with_json(jsondict)
        if 'allergyIntolerance' in jsondict:
            self.allergyIntolerance = fhirreference.FHIRReference.with_json_and_owner(jsondict['allergyIntolerance'], self)
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateTime'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'excludeFoodModifier' in jsondict:
            self.excludeFoodModifier = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['excludeFoodModifier'], self)
        if 'foodPreferenceModifier' in jsondict:
            self.foodPreferenceModifier = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['foodPreferenceModifier'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'item' in jsondict:
            self.item = NutritionOrderItem.with_json_and_owner(jsondict['item'], self)
        if 'orderer' in jsondict:
            self.orderer = fhirreference.FHIRReference.with_json_and_owner(jsondict['orderer'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)


class NutritionOrderItem(fhirelement.FHIRElement):
    """ Set of nutrition items or components that comprise the nutrition order.
    
    Different items that combine to make a complete description of the
    nutrition to be provided via oral diet, nutritional supplement and/or
    formula order.
    """
    
    resource_name = "NutritionOrderItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.enteralFormula = None
        """ Enteral formula components.
        Type `NutritionOrderItemEnteralFormula` (represented as `dict` in JSON). """
        
        self.isInEffect = False
        """ Indicates whether the nutrition item is  currently in effect.
        Type `bool`. """
        
        self.oralDiet = None
        """ Oral diet components.
        Type `NutritionOrderItemOralDiet` (represented as `dict` in JSON). """
        
        self.scheduledPeriod = None
        """ Frequency to offer nutrition item.
        Type `Period` (represented as `dict` in JSON). """
        
        self.scheduledTiming = None
        """ Frequency to offer nutrition item.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.supplement = None
        """ Supplement components.
        Type `NutritionOrderItemSupplement` (represented as `dict` in JSON). """
        
        super(NutritionOrderItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NutritionOrderItem, self).update_with_json(jsondict)
        if 'enteralFormula' in jsondict:
            self.enteralFormula = NutritionOrderItemEnteralFormula.with_json_and_owner(jsondict['enteralFormula'], self)
        if 'isInEffect' in jsondict:
            self.isInEffect = jsondict['isInEffect']
        if 'oralDiet' in jsondict:
            self.oralDiet = NutritionOrderItemOralDiet.with_json_and_owner(jsondict['oralDiet'], self)
        if 'scheduledPeriod' in jsondict:
            self.scheduledPeriod = period.Period.with_json_and_owner(jsondict['scheduledPeriod'], self)
        if 'scheduledTiming' in jsondict:
            self.scheduledTiming = timing.Timing.with_json_and_owner(jsondict['scheduledTiming'], self)
        if 'supplement' in jsondict:
            self.supplement = NutritionOrderItemSupplement.with_json_and_owner(jsondict['supplement'], self)


class NutritionOrderItemEnteralFormula(fhirelement.FHIRElement):
    """ Enteral formula components.
    
    Class that defines the components of an enteral formula order for the
    patient.
    """
    
    resource_name = "NutritionOrderItemEnteralFormula"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.additiveName = None
        """ Product or brand name of the modular additive.
        Type `str`. """
        
        self.additiveType = None
        """ Type of modular component to add to the feeding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.administrationInstructions = None
        """ Formula feeding instructions expressed as text.
        Type `str`. """
        
        self.baseFormulaName = None
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
        
        super(NutritionOrderItemEnteralFormula, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NutritionOrderItemEnteralFormula, self).update_with_json(jsondict)
        if 'additiveName' in jsondict:
            self.additiveName = jsondict['additiveName']
        if 'additiveType' in jsondict:
            self.additiveType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['additiveType'], self)
        if 'administrationInstructions' in jsondict:
            self.administrationInstructions = jsondict['administrationInstructions']
        if 'baseFormulaName' in jsondict:
            self.baseFormulaName = jsondict['baseFormulaName']
        if 'baseFormulaType' in jsondict:
            self.baseFormulaType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['baseFormulaType'], self)
        if 'caloricDensity' in jsondict:
            self.caloricDensity = quantity.Quantity.with_json_and_owner(jsondict['caloricDensity'], self)
        if 'maxVolumeToDeliver' in jsondict:
            self.maxVolumeToDeliver = quantity.Quantity.with_json_and_owner(jsondict['maxVolumeToDeliver'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'rate' in jsondict:
            self.rate = ratio.Ratio.with_json_and_owner(jsondict['rate'], self)
        if 'rateAdjustment' in jsondict:
            self.rateAdjustment = quantity.Quantity.with_json_and_owner(jsondict['rateAdjustment'], self)
        if 'routeofAdministration' in jsondict:
            self.routeofAdministration = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['routeofAdministration'], self)


class NutritionOrderItemOralDiet(fhirelement.FHIRElement):
    """ Oral diet components.
    
    Class that defines the components of an oral diet order for the patient.
    """
    
    resource_name = "NutritionOrderItemOralDiet"
    
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
        
        self.nutrients = None
        """ Required  nutrient modifications.
        List of `NutritionOrderItemOralDietNutrients` items (represented as `dict` in JSON). """
        
        self.texture = None
        """ Required  texture modifications.
        List of `NutritionOrderItemOralDietTexture` items (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of oral diet or diet restrictions that describe what can be
        consumed orally.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(NutritionOrderItemOralDiet, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NutritionOrderItemOralDiet, self).update_with_json(jsondict)
        if 'fluidConsistencyType' in jsondict:
            self.fluidConsistencyType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['fluidConsistencyType'], self)
        if 'instruction' in jsondict:
            self.instruction = jsondict['instruction']
        if 'nutrients' in jsondict:
            self.nutrients = NutritionOrderItemOralDietNutrients.with_json_and_owner(jsondict['nutrients'], self)
        if 'texture' in jsondict:
            self.texture = NutritionOrderItemOralDietTexture.with_json_and_owner(jsondict['texture'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class NutritionOrderItemOralDietNutrients(fhirelement.FHIRElement):
    """ Required  nutrient modifications.
    
    Class that defines the details of any nutrient modifications required for
    the oral diet.
    """
    
    resource_name = "NutritionOrderItemOralDietNutrients"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amountQuantity = None
        """ Quantity of the specified nutrient.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.amountRange = None
        """ Quantity of the specified nutrient.
        Type `Range` (represented as `dict` in JSON). """
        
        self.mod = None
        """ Type of nutrient that is being modified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderItemOralDietNutrients, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NutritionOrderItemOralDietNutrients, self).update_with_json(jsondict)
        if 'amountQuantity' in jsondict:
            self.amountQuantity = quantity.Quantity.with_json_and_owner(jsondict['amountQuantity'], self)
        if 'amountRange' in jsondict:
            self.amountRange = range.Range.with_json_and_owner(jsondict['amountRange'], self)
        if 'mod' in jsondict:
            self.mod = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['mod'], self)


class NutritionOrderItemOralDietTexture(fhirelement.FHIRElement):
    """ Required  texture modifications.
    
    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    
    resource_name = "NutritionOrderItemOralDietTexture"
    
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
        
        super(NutritionOrderItemOralDietTexture, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NutritionOrderItemOralDietTexture, self).update_with_json(jsondict)
        if 'foodType' in jsondict:
            self.foodType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['foodType'], self)
        if 'mod' in jsondict:
            self.mod = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['mod'], self)


class NutritionOrderItemSupplement(fhirelement.FHIRElement):
    """ Supplement components.
    
    Class that defines the components of a supplement order for the patient.
    """
    
    resource_name = "NutritionOrderItemSupplement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.name = None
        """ Product or brand name of the nutritional supplement.
        Type `str`. """
        
        self.quantity = None
        """ Amount of the nutritional supplement.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of supplement product requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(NutritionOrderItemSupplement, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(NutritionOrderItemSupplement, self).update_with_json(jsondict)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

