# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicationKnowledge).
# 2024, SMART Health IT.


from . import domainresource

class MedicationKnowledge(domainresource.DomainResource):
    """ Definition of Medication Knowledge.
    
    Information about a medication that is used to support knowledge.
    """
    
    resource_type = "MedicationKnowledge"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.administrationGuidelines = None
        """ Guidelines for administration of the medication.
        List of `MedicationKnowledgeAdministrationGuidelines` items (represented as `dict` in JSON). """
        self._administrationGuidelines = None
        """ Primitive extension for administrationGuidelines. Type `FHIRPrimitiveExtension` """
        
        self.amount = None
        """ Amount of drug in package.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.associatedMedication = None
        """ A medication resource that is associated with this medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._associatedMedication = None
        """ Primitive extension for associatedMedication. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Code that identifies this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.contraindication = None
        """ Potential clinical issue with or between medication(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._contraindication = None
        """ Primitive extension for contraindication. Type `FHIRPrimitiveExtension` """
        
        self.cost = None
        """ The pricing of the medication.
        List of `MedicationKnowledgeCost` items (represented as `dict` in JSON). """
        self._cost = None
        """ Primitive extension for cost. Type `FHIRPrimitiveExtension` """
        
        self.doseForm = None
        """ powder | tablets | capsule +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._doseForm = None
        """ Primitive extension for doseForm. Type `FHIRPrimitiveExtension` """
        
        self.drugCharacteristic = None
        """ Specifies descriptive properties of the medicine.
        List of `MedicationKnowledgeDrugCharacteristic` items (represented as `dict` in JSON). """
        self._drugCharacteristic = None
        """ Primitive extension for drugCharacteristic. Type `FHIRPrimitiveExtension` """
        
        self.ingredient = None
        """ Active or inactive ingredient.
        List of `MedicationKnowledgeIngredient` items (represented as `dict` in JSON). """
        self._ingredient = None
        """ Primitive extension for ingredient. Type `FHIRPrimitiveExtension` """
        
        self.intendedRoute = None
        """ The intended or approved route of administration.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._intendedRoute = None
        """ Primitive extension for intendedRoute. Type `FHIRPrimitiveExtension` """
        
        self.kinetics = None
        """ The time course of drug absorption, distribution, metabolism and
        excretion of a medication from the body.
        List of `MedicationKnowledgeKinetics` items (represented as `dict` in JSON). """
        self._kinetics = None
        """ Primitive extension for kinetics. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ Manufacturer of the item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
        self.medicineClassification = None
        """ Categorization of the medication within a formulary or
        classification system.
        List of `MedicationKnowledgeMedicineClassification` items (represented as `dict` in JSON). """
        self._medicineClassification = None
        """ Primitive extension for medicineClassification. Type `FHIRPrimitiveExtension` """
        
        self.monitoringProgram = None
        """ Program under which a medication is reviewed.
        List of `MedicationKnowledgeMonitoringProgram` items (represented as `dict` in JSON). """
        self._monitoringProgram = None
        """ Primitive extension for monitoringProgram. Type `FHIRPrimitiveExtension` """
        
        self.monograph = None
        """ Associated documentation about the medication.
        List of `MedicationKnowledgeMonograph` items (represented as `dict` in JSON). """
        self._monograph = None
        """ Primitive extension for monograph. Type `FHIRPrimitiveExtension` """
        
        self.packaging = None
        """ Details about packaged medications.
        Type `MedicationKnowledgePackaging` (represented as `dict` in JSON). """
        self._packaging = None
        """ Primitive extension for packaging. Type `FHIRPrimitiveExtension` """
        
        self.preparationInstruction = None
        """ The instructions for preparing the medication.
        Type `str`. """
        self._preparationInstruction = None
        """ Primitive extension for preparationInstruction. Type `FHIRPrimitiveExtension` """
        
        self.productType = None
        """ Category of the medication or product.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._productType = None
        """ Primitive extension for productType. Type `FHIRPrimitiveExtension` """
        
        self.regulatory = None
        """ Regulatory information about a medication.
        List of `MedicationKnowledgeRegulatory` items (represented as `dict` in JSON). """
        self._regulatory = None
        """ Primitive extension for regulatory. Type `FHIRPrimitiveExtension` """
        
        self.relatedMedicationKnowledge = None
        """ Associated or related medication information.
        List of `MedicationKnowledgeRelatedMedicationKnowledge` items (represented as `dict` in JSON). """
        self._relatedMedicationKnowledge = None
        """ Primitive extension for relatedMedicationKnowledge. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.synonym = None
        """ Additional names for a medication.
        List of `str` items. """
        self._synonym = None
        """ Primitive extension for synonym. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledge, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledge, self).elementProperties()
        js.extend([
            ("administrationGuidelines", "administrationGuidelines", MedicationKnowledgeAdministrationGuidelines, True, None, False),
            ("_administrationGuidelines", "_administrationGuidelines", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("associatedMedication", "associatedMedication", fhirreference.FHIRReference, True, None, False),
            ("_associatedMedication", "_associatedMedication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contraindication", "contraindication", fhirreference.FHIRReference, True, None, False),
            ("_contraindication", "_contraindication", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("cost", "cost", MedicationKnowledgeCost, True, None, False),
            ("_cost", "_cost", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("doseForm", "doseForm", codeableconcept.CodeableConcept, False, None, False),
            ("_doseForm", "_doseForm", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("drugCharacteristic", "drugCharacteristic", MedicationKnowledgeDrugCharacteristic, True, None, False),
            ("_drugCharacteristic", "_drugCharacteristic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ingredient", "ingredient", MedicationKnowledgeIngredient, True, None, False),
            ("_ingredient", "_ingredient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("intendedRoute", "intendedRoute", codeableconcept.CodeableConcept, True, None, False),
            ("_intendedRoute", "_intendedRoute", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("kinetics", "kinetics", MedicationKnowledgeKinetics, True, None, False),
            ("_kinetics", "_kinetics", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medicineClassification", "medicineClassification", MedicationKnowledgeMedicineClassification, True, None, False),
            ("_medicineClassification", "_medicineClassification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("monitoringProgram", "monitoringProgram", MedicationKnowledgeMonitoringProgram, True, None, False),
            ("_monitoringProgram", "_monitoringProgram", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("monograph", "monograph", MedicationKnowledgeMonograph, True, None, False),
            ("_monograph", "_monograph", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("packaging", "packaging", MedicationKnowledgePackaging, False, None, False),
            ("_packaging", "_packaging", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preparationInstruction", "preparationInstruction", str, False, None, False),
            ("_preparationInstruction", "_preparationInstruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("productType", "productType", codeableconcept.CodeableConcept, True, None, False),
            ("_productType", "_productType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("regulatory", "regulatory", MedicationKnowledgeRegulatory, True, None, False),
            ("_regulatory", "_regulatory", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("relatedMedicationKnowledge", "relatedMedicationKnowledge", MedicationKnowledgeRelatedMedicationKnowledge, True, None, False),
            ("_relatedMedicationKnowledge", "_relatedMedicationKnowledge", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("synonym", "synonym", str, True, None, False),
            ("_synonym", "_synonym", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationKnowledgeAdministrationGuidelines(backboneelement.BackboneElement):
    """ Guidelines for administration of the medication.
    
    Guidelines for the administration of the medication.
    """
    
    resource_type = "MedicationKnowledgeAdministrationGuidelines"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dosage = None
        """ Dosage for the medication for the specific guidelines.
        List of `MedicationKnowledgeAdministrationGuidelinesDosage` items (represented as `dict` in JSON). """
        self._dosage = None
        """ Primitive extension for dosage. Type `FHIRPrimitiveExtension` """
        
        self.indicationCodeableConcept = None
        """ Indication for use that apply to the specific administration
        guidelines.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._indicationCodeableConcept = None
        """ Primitive extension for indicationCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.indicationReference = None
        """ Indication for use that apply to the specific administration
        guidelines.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._indicationReference = None
        """ Primitive extension for indicationReference. Type `FHIRPrimitiveExtension` """
        
        self.patientCharacteristics = None
        """ Characteristics of the patient that are relevant to the
        administration guidelines.
        List of `MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics` items (represented as `dict` in JSON). """
        self._patientCharacteristics = None
        """ Primitive extension for patientCharacteristics. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeAdministrationGuidelines, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelines, self).elementProperties()
        js.extend([
            ("dosage", "dosage", MedicationKnowledgeAdministrationGuidelinesDosage, True, None, False),
            ("_dosage", "_dosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("_indicationCodeableConcept", "_indicationCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("_indicationReference", "_indicationReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patientCharacteristics", "patientCharacteristics", MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, True, None, False),
            ("_patientCharacteristics", "_patientCharacteristics", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeAdministrationGuidelinesDosage(backboneelement.BackboneElement):
    """ Dosage for the medication for the specific guidelines.
    """
    
    resource_type = "MedicationKnowledgeAdministrationGuidelinesDosage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.dosage = None
        """ Dosage for the medication for the specific guidelines.
        List of `Dosage` items (represented as `dict` in JSON). """
        self._dosage = None
        """ Primitive extension for dosage. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of dosage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeAdministrationGuidelinesDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesDosage, self).elementProperties()
        js.extend([
            ("dosage", "dosage", dosage.Dosage, True, None, True),
            ("_dosage", "_dosage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics(backboneelement.BackboneElement):
    """ Characteristics of the patient that are relevant to the administration
    guidelines.
    
    Characteristics of the patient that are relevant to the administration
    guidelines (for example, height, weight, gender, etc.).
    """
    
    resource_type = "MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.characteristicCodeableConcept = None
        """ Specific characteristic that is relevant to the administration
        guideline.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._characteristicCodeableConcept = None
        """ Primitive extension for characteristicCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.characteristicQuantity = None
        """ Specific characteristic that is relevant to the administration
        guideline.
        Type `Quantity` (represented as `dict` in JSON). """
        self._characteristicQuantity = None
        """ Primitive extension for characteristicQuantity. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The specific characteristic.
        List of `str` items. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).elementProperties()
        js.extend([
            ("characteristicCodeableConcept", "characteristicCodeableConcept", codeableconcept.CodeableConcept, False, "characteristic", True),
            ("_characteristicCodeableConcept", "_characteristicCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("characteristicQuantity", "characteristicQuantity", quantity.Quantity, False, "characteristic", True),
            ("_characteristicQuantity", "_characteristicQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, True, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeCost(backboneelement.BackboneElement):
    """ The pricing of the medication.
    
    The price of the medication.
    """
    
    resource_type = "MedicationKnowledgeCost"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.cost = None
        """ The price of the medication.
        Type `Money` (represented as `dict` in JSON). """
        self._cost = None
        """ Primitive extension for cost. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ The source or owner for the price information.
        Type `str`. """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The category of the cost information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeCost, self).elementProperties()
        js.extend([
            ("cost", "cost", money.Money, False, None, True),
            ("_cost", "_cost", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", str, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeDrugCharacteristic(backboneelement.BackboneElement):
    """ Specifies descriptive properties of the medicine.
    
    Specifies descriptive properties of the medicine, such as color, shape,
    imprints, etc.
    """
    
    resource_type = "MedicationKnowledgeDrugCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Code specifying the type of characteristic of medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.valueBase64Binary = None
        """ Description of the characteristic.
        Type `str`. """
        self._valueBase64Binary = None
        """ Primitive extension for valueBase64Binary. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Description of the characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Description of the characteristic.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueString = None
        """ Description of the characteristic.
        Type `str`. """
        self._valueString = None
        """ Primitive extension for valueString. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeDrugCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeDrugCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("_valueBase64Binary", "_valueBase64Binary", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueString", "valueString", str, False, "value", False),
            ("_valueString", "_valueString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    resource_type = "MedicationKnowledgeIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.isActive = None
        """ Active ingredient indicator.
        Type `bool`. """
        self._isActive = None
        """ Primitive extension for isActive. Type `FHIRPrimitiveExtension` """
        
        self.itemCodeableConcept = None
        """ Medication(s) or substance(s) contained in the medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._itemCodeableConcept = None
        """ Primitive extension for itemCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.itemReference = None
        """ Medication(s) or substance(s) contained in the medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._itemReference = None
        """ Primitive extension for itemReference. Type `FHIRPrimitiveExtension` """
        
        self.strength = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """
        self._strength = None
        """ Primitive extension for strength. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("_isActive", "_isActive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("_itemCodeableConcept", "_itemCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("_itemReference", "_itemReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("strength", "strength", ratio.Ratio, False, None, False),
            ("_strength", "_strength", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeKinetics(backboneelement.BackboneElement):
    """ The time course of drug absorption, distribution, metabolism and excretion
    of a medication from the body.
    """
    
    resource_type = "MedicationKnowledgeKinetics"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.areaUnderCurve = None
        """ The drug concentration measured at certain discrete points in time.
        List of `Quantity` items (represented as `dict` in JSON). """
        self._areaUnderCurve = None
        """ Primitive extension for areaUnderCurve. Type `FHIRPrimitiveExtension` """
        
        self.halfLifePeriod = None
        """ Time required for concentration in the body to decrease by half.
        Type `Duration` (represented as `dict` in JSON). """
        self._halfLifePeriod = None
        """ Primitive extension for halfLifePeriod. Type `FHIRPrimitiveExtension` """
        
        self.lethalDose50 = None
        """ The median lethal dose of a drug.
        List of `Quantity` items (represented as `dict` in JSON). """
        self._lethalDose50 = None
        """ Primitive extension for lethalDose50. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeKinetics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeKinetics, self).elementProperties()
        js.extend([
            ("areaUnderCurve", "areaUnderCurve", quantity.Quantity, True, None, False),
            ("_areaUnderCurve", "_areaUnderCurve", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("halfLifePeriod", "halfLifePeriod", duration.Duration, False, None, False),
            ("_halfLifePeriod", "_halfLifePeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lethalDose50", "lethalDose50", quantity.Quantity, True, None, False),
            ("_lethalDose50", "_lethalDose50", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeMedicineClassification(backboneelement.BackboneElement):
    """ Categorization of the medication within a formulary or classification
    system.
    """
    
    resource_type = "MedicationKnowledgeMedicineClassification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ Specific category assigned to the medication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._classification = None
        """ Primitive extension for classification. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of category for the medication (for example, therapeutic
        classification, therapeutic sub-classification).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeMedicineClassification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMedicineClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("_classification", "_classification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeMonitoringProgram(backboneelement.BackboneElement):
    """ Program under which a medication is reviewed.
    
    The program under which the medication is reviewed.
    """
    
    resource_type = "MedicationKnowledgeMonitoringProgram"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ Name of the reviewing program.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of program under which the medication is monitored.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeMonitoringProgram, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMonitoringProgram, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeMonograph(backboneelement.BackboneElement):
    """ Associated documentation about the medication.
    """
    
    resource_type = "MedicationKnowledgeMonograph"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.source = None
        """ Associated documentation about the medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The category of medication document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeMonograph, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMonograph, self).elementProperties()
        js.extend([
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgePackaging(backboneelement.BackboneElement):
    """ Details about packaged medications.
    
    Information that only applies to packages (not products).
    """
    
    resource_type = "MedicationKnowledgePackaging"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None
        """ The number of product units the package would contain if fully
        loaded.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ A code that defines the specific type of packaging that the
        medication can be found in.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgePackaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgePackaging, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeRegulatory(backboneelement.BackboneElement):
    """ Regulatory information about a medication.
    """
    
    resource_type = "MedicationKnowledgeRegulatory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.maxDispense = None
        """ The maximum number of units of the medication that can be dispensed
        in a period.
        Type `MedicationKnowledgeRegulatoryMaxDispense` (represented as `dict` in JSON). """
        self._maxDispense = None
        """ Primitive extension for maxDispense. Type `FHIRPrimitiveExtension` """
        
        self.regulatoryAuthority = None
        """ Specifies the authority of the regulation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._regulatoryAuthority = None
        """ Primitive extension for regulatoryAuthority. Type `FHIRPrimitiveExtension` """
        
        self.schedule = None
        """ Specifies the schedule of a medication in jurisdiction.
        List of `MedicationKnowledgeRegulatorySchedule` items (represented as `dict` in JSON). """
        self._schedule = None
        """ Primitive extension for schedule. Type `FHIRPrimitiveExtension` """
        
        self.substitution = None
        """ Specifies if changes are allowed when dispensing a medication from
        a regulatory perspective.
        List of `MedicationKnowledgeRegulatorySubstitution` items (represented as `dict` in JSON). """
        self._substitution = None
        """ Primitive extension for substitution. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeRegulatory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatory, self).elementProperties()
        js.extend([
            ("maxDispense", "maxDispense", MedicationKnowledgeRegulatoryMaxDispense, False, None, False),
            ("_maxDispense", "_maxDispense", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("regulatoryAuthority", "regulatoryAuthority", fhirreference.FHIRReference, False, None, True),
            ("_regulatoryAuthority", "_regulatoryAuthority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("schedule", "schedule", MedicationKnowledgeRegulatorySchedule, True, None, False),
            ("_schedule", "_schedule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substitution", "substitution", MedicationKnowledgeRegulatorySubstitution, True, None, False),
            ("_substitution", "_substitution", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeRegulatoryMaxDispense(backboneelement.BackboneElement):
    """ The maximum number of units of the medication that can be dispensed in a
    period.
    """
    
    resource_type = "MedicationKnowledgeRegulatoryMaxDispense"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.period = None
        """ The period that applies to the maximum number of units.
        Type `Duration` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ The maximum number of units of the medication that can be dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeRegulatoryMaxDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatoryMaxDispense, self).elementProperties()
        js.extend([
            ("period", "period", duration.Duration, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeRegulatorySchedule(backboneelement.BackboneElement):
    """ Specifies the schedule of a medication in jurisdiction.
    """
    
    resource_type = "MedicationKnowledgeRegulatorySchedule"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.schedule = None
        """ Specifies the specific drug schedule.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._schedule = None
        """ Primitive extension for schedule. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeRegulatorySchedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySchedule, self).elementProperties()
        js.extend([
            ("schedule", "schedule", codeableconcept.CodeableConcept, False, None, True),
            ("_schedule", "_schedule", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeRegulatorySubstitution(backboneelement.BackboneElement):
    """ Specifies if changes are allowed when dispensing a medication from a
    regulatory perspective.
    """
    
    resource_type = "MedicationKnowledgeRegulatorySubstitution"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allowed = None
        """ Specifies if regulation allows for changes in the medication when
        dispensing.
        Type `bool`. """
        self._allowed = None
        """ Primitive extension for allowed. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Specifies the type of substitution allowed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeRegulatorySubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySubstitution, self).elementProperties()
        js.extend([
            ("allowed", "allowed", bool, False, None, True),
            ("_allowed", "_allowed", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationKnowledgeRelatedMedicationKnowledge(backboneelement.BackboneElement):
    """ Associated or related medication information.
    
    Associated or related knowledge about a medication.
    """
    
    resource_type = "MedicationKnowledgeRelatedMedicationKnowledge"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.reference = None
        """ Associated documentation about the associated medication knowledge.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reference = None
        """ Primitive extension for reference. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Category of medicationKnowledge.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicationKnowledgeRelatedMedicationKnowledge, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRelatedMedicationKnowledge, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("_reference", "_reference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import dosage
from . import duration
from . import fhirreference
from . import money
from . import quantity
from . import ratio