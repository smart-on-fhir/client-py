# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Medication).
# 2024, SMART Health IT.


from . import domainresource

class Medication(domainresource.DomainResource):
    """ Definition of a Medication.
    
    This resource is primarily used for the identification and definition of a
    medication for the purposes of prescribing, dispensing, and administering a
    medication as well as for making statements about medication use.
    """
    
    resource_type = "Medication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Amount of drug in package.
        Type `Ratio` (represented as `dict` in JSON). """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.batch = None
        """ Details about packaged medications.
        Type `MedicationBatch` (represented as `dict` in JSON). """
        self._batch = None
        """ Primitive extension for batch. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Codes that identify this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.form = None
        """ powder | tablets | capsule +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._form = None
        """ Primitive extension for form. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier for this medication.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.ingredient = None
        """ Active or inactive ingredient.
        List of `MedicationIngredient` items (represented as `dict` in JSON). """
        self._ingredient = None
        """ Primitive extension for ingredient. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ Manufacturer of the item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(Medication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("amount", "amount", ratio.Ratio, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("batch", "batch", MedicationBatch, False, None, False),
            ("_batch", "_batch", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("_form", "_form", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("ingredient", "ingredient", MedicationIngredient, True, None, False),
            ("_ingredient", "_ingredient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationBatch(backboneelement.BackboneElement):
    """ Details about packaged medications.
    
    Information that only applies to packages (not products).
    """
    
    resource_type = "MedicationBatch"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expirationDate = None
        """ When batch will expire.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._expirationDate = None
        """ Primitive extension for expirationDate. Type `FHIRPrimitiveExtension` """
        
        self.lotNumber = None
        """ Identifier assigned to batch.
        Type `str`. """
        self._lotNumber = None
        """ Primitive extension for lotNumber. Type `FHIRPrimitiveExtension` """
        
        super(MedicationBatch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationBatch, self).elementProperties()
        js.extend([
            ("expirationDate", "expirationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_expirationDate", "_expirationDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("_lotNumber", "_lotNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicationIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    resource_type = "MedicationIngredient"
    
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
        """ The actual ingredient or content.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._itemCodeableConcept = None
        """ Primitive extension for itemCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.itemReference = None
        """ The actual ingredient or content.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._itemReference = None
        """ Primitive extension for itemReference. Type `FHIRPrimitiveExtension` """
        
        self.strength = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """
        self._strength = None
        """ Primitive extension for strength. Type `FHIRPrimitiveExtension` """
        
        super(MedicationIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationIngredient, self).elementProperties()
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

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import ratio