#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Device) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import contactpoint
import domainresource
import fhirdate
import fhirreference
import identifier


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
    
    def update_with_json(self, jsondict):
        super(Device, self).update_with_json(jsondict)
        if 'contact' in jsondict:
            self.contact = contactpoint.ContactPoint.with_json_and_owner(jsondict['contact'], self)
        if 'expiry' in jsondict:
            self.expiry = fhirdate.FHIRDate.with_json_and_owner(jsondict['expiry'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'location' in jsondict:
            self.location = fhirreference.FHIRReference.with_json_and_owner(jsondict['location'], self)
        if 'lotNumber' in jsondict:
            self.lotNumber = jsondict['lotNumber']
        if 'manufactureDate' in jsondict:
            self.manufactureDate = fhirdate.FHIRDate.with_json_and_owner(jsondict['manufactureDate'], self)
        if 'manufacturer' in jsondict:
            self.manufacturer = jsondict['manufacturer']
        if 'model' in jsondict:
            self.model = jsondict['model']
        if 'owner' in jsondict:
            self.owner = fhirreference.FHIRReference.with_json_and_owner(jsondict['owner'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'udi' in jsondict:
            self.udi = jsondict['udi']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'version' in jsondict:
            self.version = jsondict['version']

