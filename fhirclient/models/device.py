#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Device) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Device(domainresource.DomainResource):
    """ Item used in healthcare.
    
    This resource identifies an instance or a type of a manufactured item that
    is used in the provision of healthcare without being substantially changed
    through that activity. The device may be a medical or non-medical device.
    Medical devices include durable (reusable) medical equipment, implantable
    devices, as well as disposable equipment used for diagnostic, treatment,
    and research for healthcare and public health.  Non-medical devices may
    include items such as a machine, cellphone, computer, application, etc.
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
        
        self.expirationDate = None
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the resource is found.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Lot number of manufacture.
        Type `str`. """
        
        self.manufactureDate = None
        """ Date when the device was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.manufacturer = None
        """ Name of device manufacturer.
        Type `str`. """
        
        self.model = None
        """ Model id assigned by the manufacturer.
        Type `str`. """
        
        self.note = None
        """ Device notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient to whom Device is affixed.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.safety = None
        """ Safety Characteristics of Device.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.status = None
        """ active | inactive | entered-in-error | unknown.
        Type `str`. """
        
        self.type = None
        """ What kind of device this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udi = None
        """ Unique Device Identifier (UDI) Barcode string.
        Type `DeviceUdi` (represented as `dict` in JSON). """
        
        self.url = None
        """ Network address to contact device.
        Type `str`. """
        
        self.version = None
        """ Version number (i.e. software).
        Type `str`. """
        
        super(Device, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, True, None, False),
            ("expirationDate", "expirationDate", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("lotNumber", "lotNumber", str, False, None, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False, None, False),
            ("manufacturer", "manufacturer", str, False, None, False),
            ("model", "model", str, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("owner", "owner", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("safety", "safety", codeableconcept.CodeableConcept, True, None, False),
            ("status", "status", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("udi", "udi", DeviceUdi, False, None, False),
            ("url", "url", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceUdi(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.
    
    [Unique device identifier (UDI)](device.html#5.11.3.2.2) assigned to device
    label or package.
    """
    
    resource_type = "DeviceUdi"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.carrierAIDC = None
        """ UDI Machine Readable Barcode String.
        Type `str`. """
        
        self.carrierHRF = None
        """ UDI Human Readable Barcode String.
        Type `str`. """
        
        self.deviceIdentifier = None
        """ Mandatory fixed portion of UDI.
        Type `str`. """
        
        self.entryType = None
        """ barcode | rfid | manual +.
        Type `str`. """
        
        self.issuer = None
        """ UDI Issuing Organization.
        Type `str`. """
        
        self.jurisdiction = None
        """ Regional UDI authority.
        Type `str`. """
        
        self.name = None
        """ Device Name as appears on UDI label.
        Type `str`. """
        
        super(DeviceUdi, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceUdi, self).elementProperties()
        js.extend([
            ("carrierAIDC", "carrierAIDC", str, False, None, False),
            ("carrierHRF", "carrierHRF", str, False, None, False),
            ("deviceIdentifier", "deviceIdentifier", str, False, None, False),
            ("entryType", "entryType", str, False, None, False),
            ("issuer", "issuer", str, False, None, False),
            ("jurisdiction", "jurisdiction", str, False, None, False),
            ("name", "name", str, False, None, False),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + '.contactpoint']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
