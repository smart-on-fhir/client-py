# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/NutritionOrder).
# 2024, SMART Health IT.


from . import domainresource

class NutritionOrder(domainresource.DomainResource):
    """ Diet, formula or nutritional supplement request.
    
    A request to supply a diet, formula feeding (enteral) or oral nutritional
    supplement to a patient/resident.
    """
    
    resource_type = "NutritionOrder"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergyIntolerance = None
        """ List of the patient's food and nutrition-related allergies and
        intolerances.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._allergyIntolerance = None
        """ Primitive extension for allergyIntolerance. Type `FHIRPrimitiveExtension` """
        
        self.dateTime = None
        """ Date and time the nutrition order was requested.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._dateTime = None
        """ Primitive extension for dateTime. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ The encounter associated with this nutrition order.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.enteralFormula = None
        """ Enteral formula components.
        Type `NutritionOrderEnteralFormula` (represented as `dict` in JSON). """
        self._enteralFormula = None
        """ Primitive extension for enteralFormula. Type `FHIRPrimitiveExtension` """
        
        self.excludeFoodModifier = None
        """ Order-specific modifier about the type of food that should not be
        given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._excludeFoodModifier = None
        """ Primitive extension for excludeFoodModifier. Type `FHIRPrimitiveExtension` """
        
        self.foodPreferenceModifier = None
        """ Order-specific modifier about the type of food that should be given.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._foodPreferenceModifier = None
        """ Primitive extension for foodPreferenceModifier. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.instantiates = None
        """ Instantiates protocol or definition.
        List of `str` items. """
        self._instantiates = None
        """ Primitive extension for instantiates. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """
        self._intent = None
        """ Primitive extension for intent. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.oralDiet = None
        """ Oral diet components.
        Type `NutritionOrderOralDiet` (represented as `dict` in JSON). """
        self._oralDiet = None
        """ Primitive extension for oralDiet. Type `FHIRPrimitiveExtension` """
        
        self.orderer = None
        """ Who ordered the diet, formula or nutritional supplement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._orderer = None
        """ Primitive extension for orderer. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ The person who requires the diet, formula or nutritional supplement.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.supplement = None
        """ Supplement components.
        List of `NutritionOrderSupplement` items (represented as `dict` in JSON). """
        self._supplement = None
        """ Primitive extension for supplement. Type `FHIRPrimitiveExtension` """
        
        super(NutritionOrder, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrder, self).elementProperties()
        js.extend([
            ("allergyIntolerance", "allergyIntolerance", fhirreference.FHIRReference, True, None, False),
            ("_allergyIntolerance", "_allergyIntolerance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateTime", "dateTime", fhirdatetime.FHIRDateTime, False, None, True),
            ("_dateTime", "_dateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enteralFormula", "enteralFormula", NutritionOrderEnteralFormula, False, None, False),
            ("_enteralFormula", "_enteralFormula", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("excludeFoodModifier", "excludeFoodModifier", codeableconcept.CodeableConcept, True, None, False),
            ("_excludeFoodModifier", "_excludeFoodModifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("foodPreferenceModifier", "foodPreferenceModifier", codeableconcept.CodeableConcept, True, None, False),
            ("_foodPreferenceModifier", "_foodPreferenceModifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiates", "instantiates", str, True, None, False),
            ("_instantiates", "_instantiates", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intent", "intent", str, False, None, True),
            ("_intent", "_intent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("oralDiet", "oralDiet", NutritionOrderOralDiet, False, None, False),
            ("_oralDiet", "_oralDiet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orderer", "orderer", fhirreference.FHIRReference, False, None, False),
            ("_orderer", "_orderer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("supplement", "supplement", NutritionOrderSupplement, True, None, False),
            ("_supplement", "_supplement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class NutritionOrderEnteralFormula(backboneelement.BackboneElement):
    """ Enteral formula components.
    
    Feeding provided through the gastrointestinal tract via a tube, catheter,
    or stoma that delivers nutrition distal to the oral cavity.
    """
    
    resource_type = "NutritionOrderEnteralFormula"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveProductName = None
        """ Product or brand name of the modular additive.
        Type `str`. """
        self._additiveProductName = None
        """ Primitive extension for additiveProductName. Type `FHIRPrimitiveExtension` """
        
        self.additiveType = None
        """ Type of modular component to add to the feeding.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._additiveType = None
        """ Primitive extension for additiveType. Type `FHIRPrimitiveExtension` """
        
        self.administration = None
        """ Formula feeding instruction as structured data.
        List of `NutritionOrderEnteralFormulaAdministration` items (represented as `dict` in JSON). """
        self._administration = None
        """ Primitive extension for administration. Type `FHIRPrimitiveExtension` """
        
        self.administrationInstruction = None
        """ Formula feeding instructions expressed as text.
        Type `str`. """
        self._administrationInstruction = None
        """ Primitive extension for administrationInstruction. Type `FHIRPrimitiveExtension` """
        
        self.baseFormulaProductName = None
        """ Product or brand name of the enteral or infant formula.
        Type `str`. """
        self._baseFormulaProductName = None
        """ Primitive extension for baseFormulaProductName. Type `FHIRPrimitiveExtension` """
        
        self.baseFormulaType = None
        """ Type of enteral or infant formula.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._baseFormulaType = None
        """ Primitive extension for baseFormulaType. Type `FHIRPrimitiveExtension` """
        
        self.caloricDensity = None
        """ Amount of energy per specified volume that is required.
        Type `Quantity` (represented as `dict` in JSON). """
        self._caloricDensity = None
        """ Primitive extension for caloricDensity. Type `FHIRPrimitiveExtension` """
        
        self.maxVolumeToDeliver = None
        """ Upper limit on formula volume per unit of time.
        Type `Quantity` (represented as `dict` in JSON). """
        self._maxVolumeToDeliver = None
        """ Primitive extension for maxVolumeToDeliver. Type `FHIRPrimitiveExtension` """
        
        self.routeofAdministration = None
        """ How the formula should enter the patient's gastrointestinal tract.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._routeofAdministration = None
        """ Primitive extension for routeofAdministration. Type `FHIRPrimitiveExtension` """
        
        super(NutritionOrderEnteralFormula, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderEnteralFormula, self).elementProperties()
        js.extend([
            ("additiveProductName", "additiveProductName", str, False, None, False),
            ("_additiveProductName", "_additiveProductName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("additiveType", "additiveType", codeableconcept.CodeableConcept, False, None, False),
            ("_additiveType", "_additiveType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("administration", "administration", NutritionOrderEnteralFormulaAdministration, True, None, False),
            ("_administration", "_administration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("administrationInstruction", "administrationInstruction", str, False, None, False),
            ("_administrationInstruction", "_administrationInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("baseFormulaProductName", "baseFormulaProductName", str, False, None, False),
            ("_baseFormulaProductName", "_baseFormulaProductName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("baseFormulaType", "baseFormulaType", codeableconcept.CodeableConcept, False, None, False),
            ("_baseFormulaType", "_baseFormulaType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("caloricDensity", "caloricDensity", quantity.Quantity, False, None, False),
            ("_caloricDensity", "_caloricDensity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxVolumeToDeliver", "maxVolumeToDeliver", quantity.Quantity, False, None, False),
            ("_maxVolumeToDeliver", "_maxVolumeToDeliver", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("routeofAdministration", "routeofAdministration", codeableconcept.CodeableConcept, False, None, False),
            ("_routeofAdministration", "_routeofAdministration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class NutritionOrderEnteralFormulaAdministration(backboneelement.BackboneElement):
    """ Formula feeding instruction as structured data.
    
    Formula administration instructions as structured data.  This repeating
    structure allows for changing the administration rate or volume over time
    for both bolus and continuous feeding.  An example of this would be an
    instruction to increase the rate of continuous feeding every 2 hours.
    """
    
    resource_type = "NutritionOrderEnteralFormulaAdministration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None
        """ The volume of formula to provide.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.rateQuantity = None
        """ Speed with which the formula is provided per period of time.
        Type `Quantity` (represented as `dict` in JSON). """
        self._rateQuantity = None
        """ Primitive extension for rateQuantity. Type `FHIRPrimitiveExtension` """
        
        self.rateRatio = None
        """ Speed with which the formula is provided per period of time.
        Type `Ratio` (represented as `dict` in JSON). """
        self._rateRatio = None
        """ Primitive extension for rateRatio. Type `FHIRPrimitiveExtension` """
        
        self.schedule = None
        """ Scheduled frequency of enteral feeding.
        Type `Timing` (represented as `dict` in JSON). """
        self._schedule = None
        """ Primitive extension for schedule. Type `FHIRPrimitiveExtension` """
        
        super(NutritionOrderEnteralFormulaAdministration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderEnteralFormulaAdministration, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rateQuantity", "rateQuantity", quantity.Quantity, False, "rate", False),
            ("_rateQuantity", "_rateQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rateRatio", "rateRatio", ratio.Ratio, False, "rate", False),
            ("_rateRatio", "_rateRatio", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("schedule", "schedule", timing.Timing, False, None, False),
            ("_schedule", "_schedule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class NutritionOrderOralDiet(backboneelement.BackboneElement):
    """ Oral diet components.
    
    Diet given orally in contrast to enteral (tube) feeding.
    """
    
    resource_type = "NutritionOrderOralDiet"
    
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
        self._fluidConsistencyType = None
        """ Primitive extension for fluidConsistencyType. Type `FHIRPrimitiveExtension` """
        
        self.instruction = None
        """ Instructions or additional information about the oral diet.
        Type `str`. """
        self._instruction = None
        """ Primitive extension for instruction. Type `FHIRPrimitiveExtension` """
        
        self.nutrient = None
        """ Required  nutrient modifications.
        List of `NutritionOrderOralDietNutrient` items (represented as `dict` in JSON). """
        self._nutrient = None
        """ Primitive extension for nutrient. Type `FHIRPrimitiveExtension` """
        
        self.schedule = None
        """ Scheduled frequency of diet.
        List of `Timing` items (represented as `dict` in JSON). """
        self._schedule = None
        """ Primitive extension for schedule. Type `FHIRPrimitiveExtension` """
        
        self.texture = None
        """ Required  texture modifications.
        List of `NutritionOrderOralDietTexture` items (represented as `dict` in JSON). """
        self._texture = None
        """ Primitive extension for texture. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of oral diet or diet restrictions that describe what can be
        consumed orally.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(NutritionOrderOralDiet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDiet, self).elementProperties()
        js.extend([
            ("fluidConsistencyType", "fluidConsistencyType", codeableconcept.CodeableConcept, True, None, False),
            ("_fluidConsistencyType", "_fluidConsistencyType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instruction", "instruction", str, False, None, False),
            ("_instruction", "_instruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("nutrient", "nutrient", NutritionOrderOralDietNutrient, True, None, False),
            ("_nutrient", "_nutrient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("_schedule", "_schedule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("texture", "texture", NutritionOrderOralDietTexture, True, None, False),
            ("_texture", "_texture", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, True, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class NutritionOrderOralDietNutrient(backboneelement.BackboneElement):
    """ Required  nutrient modifications.
    
    Class that defines the quantity and type of nutrient modifications (for
    example carbohydrate, fiber or sodium) required for the oral diet.
    """
    
    resource_type = "NutritionOrderOralDietNutrient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Quantity of the specified nutrient.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Type of nutrient that is being modified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        super(NutritionOrderOralDietNutrient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDietNutrient, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class NutritionOrderOralDietTexture(backboneelement.BackboneElement):
    """ Required  texture modifications.
    
    Class that describes any texture modifications required for the patient to
    safely consume various types of solid foods.
    """
    
    resource_type = "NutritionOrderOralDietTexture"
    
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
        self._foodType = None
        """ Primitive extension for foodType. Type `FHIRPrimitiveExtension` """
        
        self.modifier = None
        """ Code to indicate how to alter the texture of the foods, e.g. pureed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._modifier = None
        """ Primitive extension for modifier. Type `FHIRPrimitiveExtension` """
        
        super(NutritionOrderOralDietTexture, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderOralDietTexture, self).elementProperties()
        js.extend([
            ("foodType", "foodType", codeableconcept.CodeableConcept, False, None, False),
            ("_foodType", "_foodType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifier", "modifier", codeableconcept.CodeableConcept, False, None, False),
            ("_modifier", "_modifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class NutritionOrderSupplement(backboneelement.BackboneElement):
    """ Supplement components.
    
    Oral nutritional products given in order to add further nutritional value
    to the patient's diet.
    """
    
    resource_type = "NutritionOrderSupplement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instruction = None
        """ Instructions or additional information about the oral supplement.
        Type `str`. """
        self._instruction = None
        """ Primitive extension for instruction. Type `FHIRPrimitiveExtension` """
        
        self.productName = None
        """ Product or brand name of the nutritional supplement.
        Type `str`. """
        self._productName = None
        """ Primitive extension for productName. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Amount of the nutritional supplement.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.schedule = None
        """ Scheduled frequency of supplement.
        List of `Timing` items (represented as `dict` in JSON). """
        self._schedule = None
        """ Primitive extension for schedule. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of supplement product requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(NutritionOrderSupplement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(NutritionOrderSupplement, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("_instruction", "_instruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productName", "productName", str, False, None, False),
            ("_productName", "_productName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("schedule", "schedule", timing.Timing, True, None, False),
            ("_schedule", "_schedule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio
from . import timing