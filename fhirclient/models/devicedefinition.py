# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceDefinition).
# 2024, SMART Health IT.


from . import domainresource

class DeviceDefinition(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.
    
    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    
    resource_type = "DeviceDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.capability = None
        """ Device capabilities.
        List of `DeviceDefinitionCapability` items (represented as `dict` in JSON). """
        self._capability = None
        """ Primitive extension for capability. Type `FHIRPrimitiveExtension` """
        
        self.contact = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.deviceName = None
        """ A name given to the device to identify it.
        List of `DeviceDefinitionDeviceName` items (represented as `dict` in JSON). """
        self._deviceName = None
        """ Primitive extension for deviceName. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.languageCode = None
        """ Language code for the human-readable text strings produced by the
        device (all supported).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._languageCode = None
        """ Primitive extension for languageCode. Type `FHIRPrimitiveExtension` """
        
        self.manufacturerReference = None
        """ Name of device manufacturer.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._manufacturerReference = None
        """ Primitive extension for manufacturerReference. Type `FHIRPrimitiveExtension` """
        
        self.manufacturerString = None
        """ Name of device manufacturer.
        Type `str`. """
        self._manufacturerString = None
        """ Primitive extension for manufacturerString. Type `FHIRPrimitiveExtension` """
        
        self.material = None
        """ A substance used to create the material(s) of which the device is
        made.
        List of `DeviceDefinitionMaterial` items (represented as `dict` in JSON). """
        self._material = None
        """ Primitive extension for material. Type `FHIRPrimitiveExtension` """
        
        self.modelNumber = None
        """ The model number for the device.
        Type `str`. """
        self._modelNumber = None
        """ Primitive extension for modelNumber. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.onlineInformation = None
        """ Access to on-line information.
        Type `str`. """
        self._onlineInformation = None
        """ Primitive extension for onlineInformation. Type `FHIRPrimitiveExtension` """
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._owner = None
        """ Primitive extension for owner. Type `FHIRPrimitiveExtension` """
        
        self.parentDevice = None
        """ The parent device it can be part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._parentDevice = None
        """ Primitive extension for parentDevice. Type `FHIRPrimitiveExtension` """
        
        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """
        self._physicalCharacteristics = None
        """ Primitive extension for physicalCharacteristics. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
        List of `DeviceDefinitionProperty` items (represented as `dict` in JSON). """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ The quantity of the device present in the packaging (e.g. the
        number of devices present in a pack, or the number of devices in
        the same package of the medicinal product).
        Type `Quantity` (represented as `dict` in JSON). """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.safety = None
        """ Safety characteristics of the device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._safety = None
        """ Primitive extension for safety. Type `FHIRPrimitiveExtension` """
        
        self.shelfLifeStorage = None
        """ Shelf Life and storage information.
        List of `ProductShelfLife` items (represented as `dict` in JSON). """
        self._shelfLifeStorage = None
        """ Primitive extension for shelfLifeStorage. Type `FHIRPrimitiveExtension` """
        
        self.specialization = None
        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
        List of `DeviceDefinitionSpecialization` items (represented as `dict` in JSON). """
        self._specialization = None
        """ Primitive extension for specialization. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ What kind of device or device system this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.udiDeviceIdentifier = None
        """ Unique Device Identifier (UDI) Barcode string.
        List of `DeviceDefinitionUdiDeviceIdentifier` items (represented as `dict` in JSON). """
        self._udiDeviceIdentifier = None
        """ Primitive extension for udiDeviceIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Network address to contact device.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Available versions.
        List of `str` items. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(DeviceDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinition, self).elementProperties()
        js.extend([
            ("capability", "capability", DeviceDefinitionCapability, True, None, False),
            ("_capability", "_capability", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deviceName", "deviceName", DeviceDefinitionDeviceName, True, None, False),
            ("_deviceName", "_deviceName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, True, None, False),
            ("_languageCode", "_languageCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturerReference", "manufacturerReference", fhirreference.FHIRReference, False, "manufacturer", False),
            ("_manufacturerReference", "_manufacturerReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturerString", "manufacturerString", str, False, "manufacturer", False),
            ("_manufacturerString", "_manufacturerString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("material", "material", DeviceDefinitionMaterial, True, None, False),
            ("_material", "_material", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("_modelNumber", "_modelNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onlineInformation", "onlineInformation", str, False, None, False),
            ("_onlineInformation", "_onlineInformation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("_owner", "_owner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parentDevice", "parentDevice", fhirreference.FHIRReference, False, None, False),
            ("_parentDevice", "_parentDevice", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, False, None, False),
            ("_physicalCharacteristics", "_physicalCharacteristics", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", DeviceDefinitionProperty, True, None, False),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("_safety", "_safety", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, True, None, False),
            ("_shelfLifeStorage", "_shelfLifeStorage", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialization", "specialization", DeviceDefinitionSpecialization, True, None, False),
            ("_specialization", "_specialization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("udiDeviceIdentifier", "udiDeviceIdentifier", DeviceDefinitionUdiDeviceIdentifier, True, None, False),
            ("_udiDeviceIdentifier", "_udiDeviceIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, True, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """ Device capabilities.
    """
    
    resource_type = "DeviceDefinitionCapability"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ Description of capability.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of capability.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(DeviceDefinitionCapability, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionCapability, self).elementProperties()
        js.extend([
            ("description", "description", codeableconcept.CodeableConcept, True, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """ A name given to the device to identify it.
    """
    
    resource_type = "DeviceDefinitionDeviceName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None
        """ The name of the device.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ udi-label-name | user-friendly-name | patient-reported-name |
        manufacturer-name | model-name | other.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(DeviceDefinitionDeviceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """ A substance used to create the material(s) of which the device is made.
    """
    
    resource_type = "DeviceDefinitionMaterial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allergenicIndicator = None
        """ Whether the substance is a known or suspected allergen.
        Type `bool`. """
        self._allergenicIndicator = None
        """ Primitive extension for allergenicIndicator. Type `FHIRPrimitiveExtension` """
        
        self.alternate = None
        """ Indicates an alternative material of the device.
        Type `bool`. """
        self._alternate = None
        """ Primitive extension for alternate. Type `FHIRPrimitiveExtension` """
        
        self.substance = None
        """ The substance.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._substance = None
        """ Primitive extension for substance. Type `FHIRPrimitiveExtension` """
        
        super(DeviceDefinitionMaterial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionMaterial, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, False, None, False),
            ("_allergenicIndicator", "_allergenicIndicator", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("alternate", "alternate", bool, False, None, False),
            ("_alternate", "_alternate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("substance", "substance", codeableconcept.CodeableConcept, False, None, True),
            ("_substance", "_substance", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    
    resource_type = "DeviceDefinitionProperty"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None
        """ Code that specifies the property DeviceDefinitionPropetyCode
        (Extensible).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.valueCode = None
        """ Property value as a code, e.g., NTP4 (synced to NTP).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._valueCode = None
        """ Primitive extension for valueCode. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Property value as a quantity.
        List of `Quantity` items (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        super(DeviceDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    
    resource_type = "DeviceDefinitionSpecialization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.systemType = None
        """ The standard that is used to operate and communicate.
        Type `str`. """
        self._systemType = None
        """ Primitive extension for systemType. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ The version of the standard that is used to operate and communicate.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(DeviceDefinitionSpecialization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", str, False, None, True),
            ("_systemType", "_systemType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    
    resource_type = "DeviceDefinitionUdiDeviceIdentifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.deviceIdentifier = None
        """ The identifier that is to be associated with every Device that
        references this DeviceDefintiion for the issuer and jurisdication
        porvided in the DeviceDefinition.udiDeviceIdentifier.
        Type `str`. """
        self._deviceIdentifier = None
        """ Primitive extension for deviceIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.issuer = None
        """ The organization that assigns the identifier algorithm.
        Type `str`. """
        self._issuer = None
        """ Primitive extension for issuer. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ The jurisdiction to which the deviceIdentifier applies.
        Type `str`. """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        super(DeviceDefinitionUdiDeviceIdentifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDefinitionUdiDeviceIdentifier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", str, False, None, True),
            ("_deviceIdentifier", "_deviceIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issuer", "issuer", str, False, None, True),
            ("_issuer", "_issuer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, True),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity