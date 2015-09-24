#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Medication) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import quantity
from . import ratio


class Medication(domainresource.DomainResource):
    """ Definition of a Medication.
    
    This resource is primarily used for the identification and definition of a
    medication. It covers the ingredients and the packaging for a medication.
    """
    
    resource_name = "Medication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(Medication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Medication, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("isBrand", "isBrand", bool, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, False),
            ("package", "package", MedicationPackage, False),
            ("product", "product", MedicationProduct, False),
        ])
        return js


class MedicationPackage(fhirelement.FHIRElement):
    """ Details about packaged medications.
    
    Information that only applies to packages (not products).
    """
    
    resource_name = "MedicationPackage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.container = None
        """ E.g. box, vial, blister-pack.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.content = None
        """ What is  in the package.
        List of `MedicationPackageContent` items (represented as `dict` in JSON). """
        
        super(MedicationPackage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationPackage, self).elementProperties()
        js.extend([
            ("container", "container", codeableconcept.CodeableConcept, False),
            ("content", "content", MedicationPackageContent, True),
        ])
        return js


class MedicationPackageContent(fhirelement.FHIRElement):
    """ What is  in the package.
    
    A set of components that go to make up the described item.
    """
    
    resource_name = "MedicationPackageContent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Quantity present in the package.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.item = None
        """ A product in the package.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        super(MedicationPackageContent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationPackageContent, self).elementProperties()
        js.extend([
            ("amount", "amount", quantity.Quantity, False),
            ("item", "item", fhirreference.FHIRReference, False),
        ])
        return js


class MedicationProduct(fhirelement.FHIRElement):
    """ Administrable medication details.
    
    Information that only applies to products (not packages).
    """
    
    resource_name = "MedicationProduct"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(MedicationProduct, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationProduct, self).elementProperties()
        js.extend([
            ("batch", "batch", MedicationProductBatch, True),
            ("form", "form", codeableconcept.CodeableConcept, False),
            ("ingredient", "ingredient", MedicationProductIngredient, True),
        ])
        return js


class MedicationProductBatch(fhirelement.FHIRElement):
    """ None.
    
    Information about a group of medication produced or packaged from one
    production run.
    """
    
    resource_name = "MedicationProductBatch"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.expirationDate = None
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.lotNumber = None
        """ None.
        Type `str`. """
        
        super(MedicationProductBatch, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationProductBatch, self).elementProperties()
        js.extend([
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False),
            ("lotNumber", "lotNumber", str, False),
        ])
        return js


class MedicationProductIngredient(fhirelement.FHIRElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    resource_name = "MedicationProductIngredient"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ Quantity of ingredient present.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.item = None
        """ The product contained.
        Type `FHIRReference` referencing `Substance, Medication` (represented as `dict` in JSON). """
        
        super(MedicationProductIngredient, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(MedicationProductIngredient, self).elementProperties()
        js.extend([
            ("amount", "amount", ratio.Ratio, False),
            ("item", "item", fhirreference.FHIRReference, False),
        ])
        return js

