#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Device) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


class Device(domainresource.DomainResource):
    """ An instance of a manufactured thing that is used in the provision of
    healthcare.
    
    This resource identifies an instance of a manufactured thing that is used
    in the provision of healthcare without being substantially changed through
    that activity. The device may be a machine, an insert, a computer, an
    application, etc. This includes durable (reusable) medical equipment as
    well as disposable equipment used for diagnostic, treatment, and research
    for healthcare and public health.
    """
    
    resource_name = "Device"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contact = None
        """ Details for human/organization for support.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.expiry = None
        """ Date and time of expiry of this device (if applicable).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Instance id from manufacturer, owner, and others.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the resource is found.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Lot number of manufacture.
        Type `str`. """
        
        self.manufactureDate = None
        """ Manufacture date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.manufacturer = None
        """ Name of device manufacturer.
        Type `str`. """
        
        self.model = None
        """ Model id assigned by the manufacturer.
        Type `str`. """
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ If the resource is affixed to a person.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ available | not-available | entered-in-error.
        Type `str`. """
        
        self.type = None
        """ What kind of device this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udi = None
        """ FDA Mandated Unique Device Identifier.
        Type `str`. """
        
        self.url = None
        """ Network address to contact device.
        Type `str`. """
        
        self.version = None
        """ Version number (i.e. software).
        Type `str`. """
        
        super(Device, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Device, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, True),
            ("expiry", "expiry", fhirdate.FHIRDate, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("location", "location", fhirreference.FHIRReference, False),
            ("lotNumber", "lotNumber", str, False),
            ("manufactureDate", "manufactureDate", fhirdate.FHIRDate, False),
            ("manufacturer", "manufacturer", str, False),
            ("model", "model", str, False),
            ("owner", "owner", fhirreference.FHIRReference, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
            ("udi", "udi", str, False),
            ("url", "url", str, False),
            ("version", "version", str, False),
        ])
        return js

