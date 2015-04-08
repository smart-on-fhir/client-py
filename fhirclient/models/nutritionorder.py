#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/NutritionOrder) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import quantity
import ratio
import timing


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
    
    def update_with_json(self, jsondict):
        super(NutritionOrder, self).update_with_json(jsondict)
        if 'allergyIntolerance' in jsondict:
            self.allergyIntolerance = fhirreference.FHIRReference.with_json_and_owner(jsondict['allergyIntolerance'], self)
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateTime'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'enteralFormula' in jsondict:
            self.enteralFormula = NutritionOrderEnteralFormula.with_json_and_owner(jsondict['enteralFormula'], self)
        if 'excludeFoodModifier' in jsondict:
            self.excludeFoodModifier = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['excludeFoodModifier'], self)
        if 'foodPreferenceModifier' in jsondict:
            self.foodPreferenceModifier = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['foodPreferenceModifier'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'oralDiet' in jsondict:
            self.oralDiet = NutritionOrderOralDiet.with_json_and_owner(jsondict['oralDiet'], self)
        if 'orderer' in jsondict:
            self.orderer = fhirreference.FHIRReference.with_json_and_owner(jsondict['orderer'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'supplement' in jsondict:
            self.supplement = NutritionOrderSupplement.with_json_and_owner(jsondict['supplement'], self)


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
    
    def update_with_json(self, jsondict):
        super(NutritionOrderEnteralFormula, self).update_with_json(jsondict)
        if 'additiveProductName' in jsondict:
            self.additiveProductName = jsondict['additiveProductName']
        if 'additiveType' in jsondict:
            self.additiveType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['additiveType'], self)
        if 'administrationInstructions' in jsondict:
            self.administrationInstructions = jsondict['administrationInstructions']
        if 'baseFormulaProductName' in jsondict:
            self.baseFormulaProductName = jsondict['baseFormulaProductName']
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
        if 'scheduled' in jsondict:
            self.scheduled = timing.Timing.with_json_and_owner(jsondict['scheduled'], self)


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
    
    def update_with_json(self, jsondict):
        super(NutritionOrderOralDiet, self).update_with_json(jsondict)
        if 'fluidConsistencyType' in jsondict:
            self.fluidConsistencyType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['fluidConsistencyType'], self)
        if 'instruction' in jsondict:
            self.instruction = jsondict['instruction']
        if 'nutrient' in jsondict:
            self.nutrient = NutritionOrderOralDietNutrient.with_json_and_owner(jsondict['nutrient'], self)
        if 'scheduled' in jsondict:
            self.scheduled = timing.Timing.with_json_and_owner(jsondict['scheduled'], self)
        if 'texture' in jsondict:
            self.texture = NutritionOrderOralDietTexture.with_json_and_owner(jsondict['texture'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


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
    
    def update_with_json(self, jsondict):
        super(NutritionOrderOralDietNutrient, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = quantity.Quantity.with_json_and_owner(jsondict['amount'], self)
        if 'modifier' in jsondict:
            self.mod = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['modifier'], self)


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
    
    def update_with_json(self, jsondict):
        super(NutritionOrderOralDietTexture, self).update_with_json(jsondict)
        if 'foodType' in jsondict:
            self.foodType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['foodType'], self)
        if 'modifier' in jsondict:
            self.mod = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['modifier'], self)


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
    
    def update_with_json(self, jsondict):
        super(NutritionOrderSupplement, self).update_with_json(jsondict)
        if 'instruction' in jsondict:
            self.instruction = jsondict['instruction']
        if 'productName' in jsondict:
            self.productName = jsondict['productName']
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'scheduled' in jsondict:
            self.scheduled = timing.Timing.with_json_and_owner(jsondict['scheduled'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

