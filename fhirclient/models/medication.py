#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (medication.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirelement
import fhirreference
import fhirresource
import narrative
import organization
import quantity
import ratio
import substance


class Medication(fhirresource.FHIRResource):
    """ Definition of a Medication.
    
    Scope and Usage Representing Medication in the majority of healthcare
    settings is a matter of identifying an item from a list and then conveying
    a reference for the item selected either into a patient related resource or
    to other applications. Additional information about the medication is
    frequently provided for human verification but a full representation of the
    details of composition and efficacy of the medicine is conveyed by
    referring to drug dictionaries by means of the codes they define. There are
    some occasions where it is necessary to identify slightly more detail, such
    as when dispensing a package containing a particular medicine requires
    identification both of the medicine and the package at once. There are also
    some occasions (e.g. custom formulations) where the composition of a
    medicine must be represented. In these cases the ingredients of the
    medicine have to be specified together with the amount contained, though
    the medication resource does not provide full details.
    
    The medication resource allows for medications to be characterised as
    either a product or a package; this classification is important because it
    affects the interpretation of a prescribed amount. For instance, is the
    prescribed amount 20 tablets, or 20 packages of 50 tablets each? However
    the kind element is not required because not all contexts of use are
    involved with prescription (medication statements, for instance).
    Typically, however, profiles describing the use of the medication resource
    in a prescribing environment will make the kind element required.
    
    Depending on whether the medication is a product or a package, further
    details about the composition can be provided. A product has a form
    (tablet, suspension, etc.) and a list of ingredients with quantities. The
    ingredients may be other medications or substances. A package has a
    container (vacuum packed box, jar, etc.) and a list of the products or
    other packages that are in the package.
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
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Medication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Medication, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'isBrand' in jsondict:
            self.isBrand = jsondict['isBrand']
        if 'kind' in jsondict:
            self.kind = jsondict['kind']
        if 'manufacturer' in jsondict:
            self.manufacturer = fhirreference.FHIRReference.with_json_and_owner(jsondict['manufacturer'], self, organization.Organization)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'package' in jsondict:
            self.package = MedicationPackage.with_json(jsondict['package'])
        if 'product' in jsondict:
            self.product = MedicationProduct.with_json(jsondict['product'])
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class MedicationProduct(fhirelement.FHIRElement):
    """ Administrable medication details.
    
    Information that only applies to products (not packages).
    """
    
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
            self.form = codeableconcept.CodeableConcept.with_json(jsondict['form'])
        if 'ingredient' in jsondict:
            self.ingredient = MedicationProductIngredient.with_json(jsondict['ingredient'])


class MedicationProductIngredient(fhirelement.FHIRElement):
    """ Active or inactive ingredient.
    
    Identifies a particular constituent of interest in the product.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.amount = None
        """ How much ingredient in product.
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.item = None
        """ The product contained.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        super(MedicationProductIngredient, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MedicationProductIngredient, self).update_with_json(jsondict)
        if 'amount' in jsondict:
            self.amount = ratio.Ratio.with_json(jsondict['amount'])
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self, substance.Substance)


class MedicationPackage(fhirelement.FHIRElement):
    """ Details about packaged medications.
    
    Information that only applies to packages (not products).
    """
    
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
            self.container = codeableconcept.CodeableConcept.with_json(jsondict['container'])
        if 'content' in jsondict:
            self.content = MedicationPackageContent.with_json(jsondict['content'])


class MedicationPackageContent(fhirelement.FHIRElement):
    """ What is  in the package?.
    
    A set of components that go to make up the described item.
    """
    
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
            self.amount = quantity.Quantity.with_json(jsondict['amount'])
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self, Medication)

