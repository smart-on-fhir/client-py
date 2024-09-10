# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProductPackaged(domainresource.DomainResource):
    """ A medicinal product in a container or package.
    """
    
    resource_type = "MedicinalProductPackaged"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.batchIdentifier = None
        """ Batch numbering.
        List of `MedicinalProductPackagedBatchIdentifier` items (represented as `dict` in JSON). """
        self._batchIdentifier = None
        """ Primitive extension for batchIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Textual description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.legalStatusOfSupply = None
        """ The legal status of supply of the medicinal product as classified
        by the regulator.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._legalStatusOfSupply = None
        """ Primitive extension for legalStatusOfSupply. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ Manufacturer of this Package Item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
        self.marketingAuthorization = None
        """ Manufacturer of this Package Item.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._marketingAuthorization = None
        """ Primitive extension for marketingAuthorization. Type `FHIRPrimitiveExtension` """
        
        self.marketingStatus = None
        """ Marketing information.
        List of `MarketingStatus` items (represented as `dict` in JSON). """
        self._marketingStatus = None
        """ Primitive extension for marketingStatus. Type `FHIRPrimitiveExtension` """
        
        self.packageItem = None
        """ A packaging item, as a contained for medicine, possibly with other
        packaging items within.
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """
        self._packageItem = None
        """ Primitive extension for packageItem. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ The product with this is a pack for.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPackaged, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackaged, self).elementProperties()
        js.extend([
            ("batchIdentifier", "batchIdentifier", MedicinalProductPackagedBatchIdentifier, True, None, False),
            ("_batchIdentifier", "_batchIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("legalStatusOfSupply", "legalStatusOfSupply", codeableconcept.CodeableConcept, False, None, False),
            ("_legalStatusOfSupply", "_legalStatusOfSupply", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("marketingAuthorization", "marketingAuthorization", fhirreference.FHIRReference, False, None, False),
            ("_marketingAuthorization", "_marketingAuthorization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("marketingStatus", "marketingStatus", marketingstatus.MarketingStatus, True, None, False),
            ("_marketingStatus", "_marketingStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, True),
            ("_packageItem", "_packageItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductPackagedBatchIdentifier(backboneelement.BackboneElement):
    """ Batch numbering.
    """
    
    resource_type = "MedicinalProductPackagedBatchIdentifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.immediatePackaging = None
        """ A number appearing on the immediate packaging (and not the outer
        packaging).
        Type `Identifier` (represented as `dict` in JSON). """
        self._immediatePackaging = None
        """ Primitive extension for immediatePackaging. Type `FHIRPrimitiveExtension` """
        
        self.outerPackaging = None
        """ A number appearing on the outer packaging of a specific batch.
        Type `Identifier` (represented as `dict` in JSON). """
        self._outerPackaging = None
        """ Primitive extension for outerPackaging. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPackagedBatchIdentifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackagedBatchIdentifier, self).elementProperties()
        js.extend([
            ("immediatePackaging", "immediatePackaging", identifier.Identifier, False, None, False),
            ("_immediatePackaging", "_immediatePackaging", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("outerPackaging", "outerPackaging", identifier.Identifier, False, None, True),
            ("_outerPackaging", "_outerPackaging", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MedicinalProductPackagedPackageItem(backboneelement.BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """
    
    resource_type = "MedicinalProductPackagedPackageItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.alternateMaterial = None
        """ A possible alternate material for the packaging.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._alternateMaterial = None
        """ Primitive extension for alternateMaterial. Type `FHIRPrimitiveExtension` """
        
        self.device = None
        """ A device accompanying a medicinal product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._device = None
        """ Primitive extension for device. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Including possibly Data Carrier Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.manufacturedItem = None
        """ The manufactured item as contained in the packaged medicinal
        product.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._manufacturedItem = None
        """ Primitive extension for manufacturedItem. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ Manufacturer of this Package Item.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
        self.material = None
        """ Material type of the package item.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._material = None
        """ Primitive extension for material. Type `FHIRPrimitiveExtension` """
        
        self.otherCharacteristics = None
        """ Other codeable characteristics.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._otherCharacteristics = None
        """ Primitive extension for otherCharacteristics. Type `FHIRPrimitiveExtension` """
        
        self.packageItem = None
        """ Allows containers within containers.
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """
        self._packageItem = None
        """ Primitive extension for packageItem. Type `FHIRPrimitiveExtension` """
        
        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        self._physicalCharacteristics = None
        """ Primitive extension for physicalCharacteristics. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ The quantity of this package in the medicinal product, at the
        current level of packaging. The outermost is always 1.
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.shelfLifeStorage = None
        """ Shelf Life and storage information.
        List of `ProductShelfLife` items (represented as `dict` in JSON). """
        self._shelfLifeStorage = None
        """ Primitive extension for shelfLifeStorage. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The physical type of the container of the medicine.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductPackagedPackageItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductPackagedPackageItem, self).elementProperties()
        js.extend([
            ("alternateMaterial", "alternateMaterial", codeableconcept.CodeableConcept, True, None, False),
            ("_alternateMaterial", "_alternateMaterial", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("device", "device", fhirreference.FHIRReference, True, None, False),
            ("_device", "_device", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturedItem", "manufacturedItem", fhirreference.FHIRReference, True, None, False),
            ("_manufacturedItem", "_manufacturedItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", fhirreference.FHIRReference, True, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, True, None, False),
            ("_material", "_material", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("otherCharacteristics", "otherCharacteristics", codeableconcept.CodeableConcept, True, None, False),
            ("_otherCharacteristics", "_otherCharacteristics", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("packageItem", "packageItem", MedicinalProductPackagedPackageItem, True, None, False),
            ("_packageItem", "_packageItem", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("_physicalCharacteristics", "_physicalCharacteristics", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, True),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False),
            ("_shelfLifeStorage", "_shelfLifeStorage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import marketingstatus
from . import prodcharacteristic
from . import productshelflife
from . import quantity