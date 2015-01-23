#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (substance.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import quantity
import ratio


class Substance(fhirresource.FHIRResource):
    """ A homogeneous material with a definite composition.
    """
    
    resource_name = "Substance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.description = None
        """ Textual description of the substance, comments.
        Type `str`. """
        
        self.ingredient = None
        """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """
        
        self.instance = None
        """ If this describes a specific package/container of the substance.
        Type `SubstanceInstance` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Substance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Substance, self).update_with_json(jsondict)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'ingredient' in jsondict:
            self.ingredient = SubstanceIngredient.with_json_and_owner(jsondict['ingredient'], self)
        if 'instance' in jsondict:
            self.instance = SubstanceInstance.with_json_and_owner(jsondict['instance'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class SubstanceIngredient(fhirelement.FHIRElement):
    """ Composition information about the substance.
    
    A substance can be composed of other substances.
    """
    
    resource_name = "SubstanceIngredient"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.quantity = None
        """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.substance = None
        """ A component of the substance.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        super(SubstanceIngredient, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SubstanceIngredient, self).update_with_json(jsondict)
        if 'quantity' in jsondict:
            self.quantity = ratio.Ratio.with_json_and_owner(jsondict['quantity'], self)
        if 'substance' in jsondict:
            self.substance = fhirreference.FHIRReference.with_json_and_owner(jsondict['substance'], self)


class SubstanceInstance(fhirelement.FHIRElement):
    """ If this describes a specific package/container of the substance.
    
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    
    resource_name = "SubstanceInstance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.expiry = None
        """ When no longer valid to use.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount of substance in the package.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SubstanceInstance, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SubstanceInstance, self).update_with_json(jsondict)
        if 'expiry' in jsondict:
            self.expiry = fhirdate.FHIRDate.with_json_and_owner(jsondict['expiry'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)

