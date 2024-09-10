# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Device).
# 2024, SMART Health IT.


from . import domainresource

class Device(domainresource.DomainResource):
    """ Item used in healthcare.
    
    A type of a manufactured item that is used in the provision of healthcare
    without being substantially changed through that activity. The device may
    be a medical or non-medical device.
    """
    
    resource_type = "Device"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.definition = None
        """ The reference to the definition for the device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.deviceName = None
        """ The name of the device as given by the manufacturer.
        List of `DeviceDeviceName` items (represented as `dict` in JSON). """
        self._deviceName = None
        """ Primitive extension for deviceName. Type `FHIRPrimitiveExtension` """
        
        self.distinctIdentifier = None
        """ The distinct identification string.
        Type `str`. """
        self._distinctIdentifier = None
        """ Primitive extension for distinctIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.expirationDate = None
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._expirationDate = None
        """ Primitive extension for expirationDate. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.location = None
        """ Where the device is found.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._location = None
        """ Primitive extension for location. Type `FHIRPrimitiveExtension` """
        
        self.lotNumber = None
        """ Lot number of manufacture.
        Type `str`. """
        self._lotNumber = None
        """ Primitive extension for lotNumber. Type `FHIRPrimitiveExtension` """
        
        self.manufactureDate = None
        """ Date when the device was made.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._manufactureDate = None
        """ Primitive extension for manufactureDate. Type `FHIRPrimitiveExtension` """
        
        self.manufacturer = None
        """ Name of device manufacturer.
        Type `str`. """
        self._manufacturer = None
        """ Primitive extension for manufacturer. Type `FHIRPrimitiveExtension` """
        
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
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._owner = None
        """ Primitive extension for owner. Type `FHIRPrimitiveExtension` """
        
        self.parent = None
        """ The parent device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._parent = None
        """ Primitive extension for parent. Type `FHIRPrimitiveExtension` """
        
        self.partNumber = None
        """ The part number of the device.
        Type `str`. """
        self._partNumber = None
        """ Primitive extension for partNumber. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Patient to whom Device is affixed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.property = None
        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
        List of `DeviceProperty` items (represented as `dict` in JSON). """
        self._property = None
        """ Primitive extension for property. Type `FHIRPrimitiveExtension` """
        
        self.safety = None
        """ Safety Characteristics of Device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._safety = None
        """ Primitive extension for safety. Type `FHIRPrimitiveExtension` """
        
        self.serialNumber = None
        """ Serial number assigned by the manufacturer.
        Type `str`. """
        self._serialNumber = None
        """ Primitive extension for serialNumber. Type `FHIRPrimitiveExtension` """
        
        self.specialization = None
        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
        List of `DeviceSpecialization` items (represented as `dict` in JSON). """
        self._specialization = None
        """ Primitive extension for specialization. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | inactive | entered-in-error | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ online | paused | standby | offline | not-ready | transduc-discon |
        hw-discon | off.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The kind or type of device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.udiCarrier = None
        """ Unique Device Identifier (UDI) Barcode string.
        List of `DeviceUdiCarrier` items (represented as `dict` in JSON). """
        self._udiCarrier = None
        """ Primitive extension for udiCarrier. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Network address to contact device.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ The actual design of the device or software version running on the
        device.
        List of `DeviceVersion` items (represented as `dict` in JSON). """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(Device, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, False, None, False),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deviceName", "deviceName", DeviceDeviceName, True, None, False),
            ("_deviceName", "_deviceName", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("distinctIdentifier", "distinctIdentifier", str, False, None, False),
            ("_distinctIdentifier", "_distinctIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("expirationDate", "expirationDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_expirationDate", "_expirationDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("_location", "_location", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("_lotNumber", "_lotNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdatetime.FHIRDateTime, False, None, False),
            ("_manufactureDate", "_manufactureDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("_manufacturer", "_manufacturer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modelNumber", "modelNumber", str, False, None, False),
            ("_modelNumber", "_modelNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("_owner", "_owner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("_parent", "_parent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partNumber", "partNumber", str, False, None, False),
            ("_partNumber", "_partNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("property", "property", DeviceProperty, True, None, False),
            ("_property", "_property", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("_safety", "_safety", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("serialNumber", "serialNumber", str, False, None, False),
            ("_serialNumber", "_serialNumber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("specialization", "specialization", DeviceSpecialization, True, None, False),
            ("_specialization", "_specialization", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, False),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, True, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("udiCarrier", "udiCarrier", DeviceUdiCarrier, True, None, False),
            ("_udiCarrier", "_udiCarrier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", DeviceVersion, True, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceDeviceName(backboneelement.BackboneElement):
    """ The name of the device as given by the manufacturer.
    
    This represents the manufacturer's name of the device as provided by the
    device, from a UDI label, or by a person describing the Device.  This
    typically would be used when a person provides the name(s) or when the
    device represents one of the names available from DeviceDefinition.
    """
    
    resource_type = "DeviceDeviceName"
    
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
        
        super(DeviceDeviceName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    
    resource_type = "DeviceProperty"
    
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
        
        super(DeviceProperty, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, True, None, False),
            ("_valueCode", "_valueCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, True, None, False),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    
    resource_type = "DeviceSpecialization"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.systemType = None
        """ The standard that is used to operate and communicate.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._systemType = None
        """ Primitive extension for systemType. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ The version of the standard that is used to operate and communicate.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(DeviceSpecialization, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", codeableconcept.CodeableConcept, False, None, True),
            ("_systemType", "_systemType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceUdiCarrier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    
    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    
    resource_type = "DeviceUdiCarrier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.carrierAIDC = None
        """ UDI Machine Readable Barcode String.
        Type `str`. """
        self._carrierAIDC = None
        """ Primitive extension for carrierAIDC. Type `FHIRPrimitiveExtension` """
        
        self.carrierHRF = None
        """ UDI Human Readable Barcode String.
        Type `str`. """
        self._carrierHRF = None
        """ Primitive extension for carrierHRF. Type `FHIRPrimitiveExtension` """
        
        self.deviceIdentifier = None
        """ Mandatory fixed portion of UDI.
        Type `str`. """
        self._deviceIdentifier = None
        """ Primitive extension for deviceIdentifier. Type `FHIRPrimitiveExtension` """
        
        self.entryType = None
        """ barcode | rfid | manual +.
        Type `str`. """
        self._entryType = None
        """ Primitive extension for entryType. Type `FHIRPrimitiveExtension` """
        
        self.issuer = None
        """ UDI Issuing Organization.
        Type `str`. """
        self._issuer = None
        """ Primitive extension for issuer. Type `FHIRPrimitiveExtension` """
        
        self.jurisdiction = None
        """ Regional UDI authority.
        Type `str`. """
        self._jurisdiction = None
        """ Primitive extension for jurisdiction. Type `FHIRPrimitiveExtension` """
        
        super(DeviceUdiCarrier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUdiCarrier, self).elementProperties()
        js.extend([
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("_carrierAIDC", "_carrierAIDC", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("_carrierHRF", "_carrierHRF", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("deviceIdentifier", "deviceIdentifier", str, False, None, False),
            ("_deviceIdentifier", "_deviceIdentifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("entryType", "entryType", str, False, None, False),
            ("_entryType", "_entryType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("issuer", "issuer", str, False, None, False),
            ("_issuer", "_issuer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, False),
            ("_jurisdiction", "_jurisdiction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class DeviceVersion(backboneelement.BackboneElement):
    """ The actual design of the device or software version running on the device.
    """
    
    resource_type = "DeviceVersion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.component = None
        """ A single component of the device version.
        Type `Identifier` (represented as `dict` in JSON). """
        self._component = None
        """ Primitive extension for component. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of the device version.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The version text.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(DeviceVersion, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceVersion, self).elementProperties()
        js.extend([
            ("component", "component", identifier.Identifier, False, None, False),
            ("_component", "_component", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, True),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity