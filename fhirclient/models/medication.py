#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Medication) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Medication(domainresource.DomainResource):
    """ Definition of a Medication.
    
    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """
    
    resource_name = "Medication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Codes that identify this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.isBrand = None
        """ True if a brand.
        Type `bool`. """
        
        self.manufacturer = None
        """ Manufacturer of the item.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.package = None
        """ Details about packaged medications.
        Type `MedicationPackage` (represented as `dict` in JSON). """
        
        self.product = None
        """ Administrable medication details.
        Type `MedicationProduct` (represented as `dict` in JSON). """
        
        super(Medication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("isBrand", "isBrand", bool, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False, None, False),
            ("package", "package", MedicationPackage, False, None, False),
            ("product", "product", MedicationProduct, False, None, False),
        ])
        return js


from . import backboneelement

class MedicationPackage(backboneelement.BackboneElement):
    """ Details about packaged medications.
    
    Information that only applies to packages (not products).
    """
    
    resource_name = "MedicationPackage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.container = None
        """ E.g. box, vial, blister-pack.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ What is  in the package.
        List of `MedicationPackageContent` items (represented as `dict` in JSON). """
        
        super(MedicationPackage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationPackage, self).elementProperties()
        js.extend([
            ("container", "container", codeableconcept.CodeableConcept, False, None, False),
            ("content", "content", MedicationPackageContent, True, None, False),
        ])
        return js


class MedicationPackageContent(backboneelement.BackboneElement):
    """ What is  in the package.
    
    A set of components that go to make up the described item.
    """
    
    resource_name = "MedicationPackageContent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Quantity present in the package.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.item = None
        """ A product in the package.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        super(MedicationPackageContent, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationPackageContent, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class MedicationProduct(backboneelement.BackboneElement):
    """ Administrable medication details.
    
    Information that only applies to products (not packages).
    """
    
    resource_name = "MedicationProduct"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.batch = None
        """ None.
        List of `MedicationProductBatch` items (represented as `dict` in JSON). """
        
        self.form = None
        """ powder | tablets | carton +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ Active or inactive ingredient.
        List of `MedicationProductIngredient` items (represented as `dict` in JSON). """
        
        super(MedicationProduct, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationProduct, self).elementProperties()
        js.extend([
            ("batch", "batch", MedicationProductBatch, True, None, False),
            ("form", "form", codeableconcept.CodeableConcept, False, None, False),
            ("ingredient", "ingredient", MedicationProductIngredient, True, None, False),
        ])
        return js


class MedicationProductBatch(backboneelement.BackboneElement):
    """ None.
    
    Information about a group of medication produced or packaged from one
    production run.
    """
    
    resource_name = "MedicationProductBatch"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expirationDate = None
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lotNumber = None
        """ None.
        Type `str`. """
        
        super(MedicationProductBatch, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationProductBatch, self).elementProperties()
        js.extend([
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
        ])
        return js


class MedicationProductIngredient(backboneelement.BackboneElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    resource_name = "MedicationProductIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.item = None
        """ The product contained.
        Type `FHIRReference` referencing `Substance, Medication` (represented as `dict` in JSON). """
        
        super(MedicationProductIngredient, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicationProductIngredient, self).elementProperties()
        js.extend([
            ("amount", "amount", ratio.Ratio, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import quantity
from . import ratio
