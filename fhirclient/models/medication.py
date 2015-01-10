#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (medication.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirelement
import fhirreference
import fhirresource
import quantity
import ratio


class Medication(fhirresource.FHIRResource):
    """ Definition of a Medication.
    
    Primarily used for identification and definition of Medication, but also
    covers ingredients and packaging.
    """
    
    resource_name = "Medication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Codes that identify this medication.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.isBrand = False
        """ True if a brand.
        Type `bool`. """
        
        self.kind = None
        """ product | package.
        Type `str`. """
        
        self.manufacturer = None
        """ Manufacturer of the item.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.name = None
        """ Common / Commercial name.
        Type `str`. """
        
        self.package = None
        """ Details about packaged medications.
        Type `MedicationPackage` (represented as `dict` in JSON). """
        
        self.product = None
        """ Administrable medication details.
        Type `MedicationProduct` (represented as `dict` in JSON). """
        
        super(Medication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Medication, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'isBrand' in jsondict:
            self.isBrand = jsondict['isBrand']
        if 'kind' in jsondict:
            self.kind = jsondict['kind']
        if 'manufacturer' in jsondict:
            self.manufacturer = fhirreference.FHIRReference.with_json_and_owner(jsondict['manufacturer'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'package' in jsondict:
            self.package = MedicationPackage.with_json_and_owner(jsondict['package'], self)
        if 'product' in jsondict:
            self.product = MedicationProduct.with_json_and_owner(jsondict['product'], self)


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
        """ What is  in the package?.
        List of `MedicationPackageContent` items (represented as `dict` in JSON). """
        
        super(MedicationPackage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationPackage, self).update_with_json(jsondict)
        if 'container' in jsondict:
            self.container = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['container'], self)
        if 'content' in jsondict:
            self.content = MedicationPackageContent.with_json_and_owner(jsondict['content'], self)


class MedicationPackageContent(fhirelement.FHIRElement):
    """ What is  in the package?.
    
    A set of components that go to make up the described item.
    """
    
    resource_name = "MedicationPackageContent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ How many are in the package?.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.item = None
        """ A product in the package.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        super(MedicationPackageContent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationPackageContent, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = quantity.Quantity.with_json_and_owner(jsondict['amount'], self)
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self)


class MedicationProduct(fhirelement.FHIRElement):
    """ Administrable medication details.
    
    Information that only applies to products (not packages).
    """
    
    resource_name = "MedicationProduct"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.form = None
        """ powder | tablets | carton +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.ingredient = None
        """ Active or inactive ingredient.
        List of `MedicationProductIngredient` items (represented as `dict` in JSON). """
        
        super(MedicationProduct, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationProduct, self).update_with_json(jsondict)
        if 'form' in jsondict:
            self.form = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['form'], self)
        if 'ingredient' in jsondict:
            self.ingredient = MedicationProductIngredient.with_json_and_owner(jsondict['ingredient'], self)


class MedicationProductIngredient(fhirelement.FHIRElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    resource_name = "MedicationProductIngredient"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ How much ingredient in product.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.item = None
        """ The product contained.
        Type `FHIRReference` referencing `Substance, Medication` (represented as `dict` in JSON). """
        
        super(MedicationProductIngredient, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationProductIngredient, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = ratio.Ratio.with_json_and_owner(jsondict['amount'], self)
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self)

