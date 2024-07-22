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
        
        self.amount = None
        """ Amount of drug in package.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.associatedMedication = None
        """ A medication resource that is associated with this medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Code that identifies this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.contraindication = None
        """ Potential clinical issue with or between medication(s).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.cost = None
        """ The pricing of the medication.
        List of `MedicationKnowledgeCost` items (represented as `dict` in JSON). """
        
        self.doseForm = None
        """ powder | tablets | capsule +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.drugCharacteristic = None
        """ Specifies descriptive properties of the medicine.
        List of `MedicationKnowledgeDrugCharacteristic` items (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ Active or inactive ingredient.
        List of `MedicationKnowledgeIngredient` items (represented as `dict` in JSON). """
        
        self.intendedRoute = None
        """ The intended or approved route of administration.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.kinetics = None
        """ The time course of drug absorption, distribution, metabolism and
        excretion of a medication from the body.
        List of `MedicationKnowledgeKinetics` items (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ Manufacturer of the item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.medicineClassification = None
        """ Categorization of the medication within a formulary or
        classification system.
        List of `MedicationKnowledgeMedicineClassification` items (represented as `dict` in JSON). """
        
        self.monitoringProgram = None
        """ Program under which a medication is reviewed.
        List of `MedicationKnowledgeMonitoringProgram` items (represented as `dict` in JSON). """
        
        self.monograph = None
        """ Associated documentation about the medication.
        List of `MedicationKnowledgeMonograph` items (represented as `dict` in JSON). """
        
        self.packaging = None
        """ Details about packaged medications.
        Type `MedicationKnowledgePackaging` (represented as `dict` in JSON). """
        
        self.preparationInstruction = None
        """ The instructions for preparing the medication.
        Type `str`. """
        
        self.productType = None
        """ Category of the medication or product.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.regulatory = None
        """ Regulatory information about a medication.
        List of `MedicationKnowledgeRegulatory` items (represented as `dict` in JSON). """
        
        self.relatedMedicationKnowledge = None
        """ Associated or related medication information.
        List of `MedicationKnowledgeRelatedMedicationKnowledge` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """
        
        self.synonym = None
        """ Additional names for a medication.
        List of `str` items. """
        
        super(MedicationKnowledge, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledge, self).elementProperties()
        js.extend([
            ("administrationGuidelines", "administrationGuidelines", MedicationKnowledgeAdministrationGuidelines, True, None, False),
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("associatedMedication", "associatedMedication", fhirreference.FHIRReference, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("contraindication", "contraindication", fhirreference.FHIRReference, True, None, False),
            ("cost", "cost", MedicationKnowledgeCost, True, None, False),
            ("doseForm", "doseForm", codeableconcept.CodeableConcept, False, None, False),
            ("drugCharacteristic", "drugCharacteristic", MedicationKnowledgeDrugCharacteristic, True, None, False),
            ("ingredient", "ingredient", MedicationKnowledgeIngredient, True, None, False),
            ("intendedRoute", "intendedRoute", codeableconcept.CodeableConcept, True, None, False),
            ("kinetics", "kinetics", MedicationKnowledgeKinetics, True, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("medicineClassification", "medicineClassification", MedicationKnowledgeMedicineClassification, True, None, False),
            ("monitoringProgram", "monitoringProgram", MedicationKnowledgeMonitoringProgram, True, None, False),
            ("monograph", "monograph", MedicationKnowledgeMonograph, True, None, False),
            ("packaging", "packaging", MedicationKnowledgePackaging, False, None, False),
            ("preparationInstruction", "preparationInstruction", str, False, None, False),
            ("productType", "productType", codeableconcept.CodeableConcept, True, None, False),
            ("regulatory", "regulatory", MedicationKnowledgeRegulatory, True, None, False),
            ("relatedMedicationKnowledge", "relatedMedicationKnowledge", MedicationKnowledgeRelatedMedicationKnowledge, True, None, False),
            ("status", "status", str, False, None, False),
            ("synonym", "synonym", str, True, None, False),
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
        
        self.indicationCodeableConcept = None
        """ Indication for use that apply to the specific administration
        guidelines.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.indicationReference = None
        """ Indication for use that apply to the specific administration
        guidelines.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.patientCharacteristics = None
        """ Characteristics of the patient that are relevant to the
        administration guidelines.
        List of `MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics` items (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeAdministrationGuidelines, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelines, self).elementProperties()
        js.extend([
            ("dosage", "dosage", MedicationKnowledgeAdministrationGuidelinesDosage, True, None, False),
            ("indicationCodeableConcept", "indicationCodeableConcept", codeableconcept.CodeableConcept, False, "indication", False),
            ("indicationReference", "indicationReference", fhirreference.FHIRReference, False, "indication", False),
            ("patientCharacteristics", "patientCharacteristics", MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, True, None, False),
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
        
        self.type = None
        """ Type of dosage.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeAdministrationGuidelinesDosage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesDosage, self).elementProperties()
        js.extend([
            ("dosage", "dosage", dosage.Dosage, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
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
        
        self.characteristicQuantity = None
        """ Specific characteristic that is relevant to the administration
        guideline.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.value = None
        """ The specific characteristic.
        List of `str` items. """
        
        super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeAdministrationGuidelinesPatientCharacteristics, self).elementProperties()
        js.extend([
            ("characteristicCodeableConcept", "characteristicCodeableConcept", codeableconcept.CodeableConcept, False, "characteristic", True),
            ("characteristicQuantity", "characteristicQuantity", quantity.Quantity, False, "characteristic", True),
            ("value", "value", str, True, None, False),
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
        
        self.source = None
        """ The source or owner for the price information.
        Type `str`. """
        
        self.type = None
        """ The category of the cost information.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeCost, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeCost, self).elementProperties()
        js.extend([
            ("cost", "cost", money.Money, False, None, True),
            ("source", "source", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
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
        
        self.valueBase64Binary = None
        """ Description of the characteristic.
        Type `str`. """
        
        self.valueCodeableConcept = None
        """ Description of the characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Description of the characteristic.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueString = None
        """ Description of the characteristic.
        Type `str`. """
        
        super(MedicationKnowledgeDrugCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeDrugCharacteristic, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("valueBase64Binary", "valueBase64Binary", str, False, "value", False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
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
        
        self.itemCodeableConcept = None
        """ Medication(s) or substance(s) contained in the medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ Medication(s) or substance(s) contained in the medication.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.strength = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeIngredient, self).elementProperties()
        js.extend([
            ("isActive", "isActive", bool, False, None, False),
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("strength", "strength", ratio.Ratio, False, None, False),
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
        
        self.halfLifePeriod = None
        """ Time required for concentration in the body to decrease by half.
        Type `Duration` (represented as `dict` in JSON). """
        
        self.lethalDose50 = None
        """ The median lethal dose of a drug.
        List of `Quantity` items (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeKinetics, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeKinetics, self).elementProperties()
        js.extend([
            ("areaUnderCurve", "areaUnderCurve", quantity.Quantity, True, None, False),
            ("halfLifePeriod", "halfLifePeriod", duration.Duration, False, None, False),
            ("lethalDose50", "lethalDose50", quantity.Quantity, True, None, False),
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
        
        self.type = None
        """ The type of category for the medication (for example, therapeutic
        classification, therapeutic sub-classification).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeMedicineClassification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMedicineClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
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
        
        self.type = None
        """ Type of program under which the medication is monitored.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeMonitoringProgram, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMonitoringProgram, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.type = None
        """ The category of medication document.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeMonograph, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeMonograph, self).elementProperties()
        js.extend([
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.type = None
        """ A code that defines the specific type of packaging that the
        medication can be found in.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgePackaging, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgePackaging, self).elementProperties()
        js.extend([
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
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
        
        self.regulatoryAuthority = None
        """ Specifies the authority of the regulation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ Specifies the schedule of a medication in jurisdiction.
        List of `MedicationKnowledgeRegulatorySchedule` items (represented as `dict` in JSON). """
        
        self.substitution = None
        """ Specifies if changes are allowed when dispensing a medication from
        a regulatory perspective.
        List of `MedicationKnowledgeRegulatorySubstitution` items (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRegulatory, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatory, self).elementProperties()
        js.extend([
            ("maxDispense", "maxDispense", MedicationKnowledgeRegulatoryMaxDispense, False, None, False),
            ("regulatoryAuthority", "regulatoryAuthority", fhirreference.FHIRReference, False, None, True),
            ("schedule", "schedule", MedicationKnowledgeRegulatorySchedule, True, None, False),
            ("substitution", "substitution", MedicationKnowledgeRegulatorySubstitution, True, None, False),
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
        
        self.quantity = None
        """ The maximum number of units of the medication that can be dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRegulatoryMaxDispense, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatoryMaxDispense, self).elementProperties()
        js.extend([
            ("period", "period", duration.Duration, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
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
        
        super(MedicationKnowledgeRegulatorySchedule, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySchedule, self).elementProperties()
        js.extend([
            ("schedule", "schedule", codeableconcept.CodeableConcept, False, None, True),
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
        
        self.type = None
        """ Specifies the type of substitution allowed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRegulatorySubstitution, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRegulatorySubstitution, self).elementProperties()
        js.extend([
            ("allowed", "allowed", bool, False, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
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
        
        self.type = None
        """ Category of medicationKnowledge.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicationKnowledgeRelatedMedicationKnowledge, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationKnowledgeRelatedMedicationKnowledge, self).elementProperties()
        js.extend([
            ("reference", "reference", fhirreference.FHIRReference, True, None, True),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import dosage
from . import duration
from . import fhirreference
from . import money
from . import quantity
from . import ratio
