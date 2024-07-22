# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProductManufactured(domainresource.DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    """
    
    resource_type = "MedicinalProductManufactured"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ingredient = None
        """ Ingredient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.manufacturedDoseForm = None
        """ Dose form as manufactured and before any transformation into the
        pharmaceutical product.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.manufacturer = None
        """ Manufacturer of the item (Note that this should be named
        "manufacturer" but it currently causes technical issues).
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.otherCharacteristics = None
        """ Other codeable characteristics.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ The quantity or "count number" of the manufactured item.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.unitOfPresentation = None
        """ The “real world” units in which the quantity of the manufactured
        item is described.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(MedicinalProductManufactured, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductManufactured, self).elementProperties()
        js.extend([
            ("ingredient", "ingredient", fhirreference.FHIRReference, True, None, False),
            ("manufacturedDoseForm", "manufacturedDoseForm", codeableconcept.CodeableConcept, False, None, True),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("unitOfPresentation", "unitOfPresentation", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirreference
from . import prodcharacteristic
from . import quantity
