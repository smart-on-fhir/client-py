#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (devicecomponent.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class DeviceComponent(fhirresource.FHIRResource):
    """ An instance of a medical-related component of a medical device.
    
    Describes the characteristics, operational status and capabilities of a
    medical-related component of a medical device.
    """
    
    resource_name = "DeviceComponent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ Instance id assigned by the software stack.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.languageCode = None
        """ Language code for the human-readable text strings produced by the
        device.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.lastSystemChange = None
        """ Recent system change timestamp.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.measurementPrinciple = None
        """ other | chemical | electrical | impedance | nuclear | optical |
        thermal | biological | mechanical | acoustical | manual+.
        Type `str`. """
        
        self.operationalStatus = None
        """ Component operational status.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.parameterGroup = None
        """ Current supported parameter group.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.parent = None
        """ Parent resource link.
        Type `FHIRReference` referencing `DeviceComponent` (represented as `dict` in JSON). """
        
        self.productionSpecification = None
        """ Production specification of the component.
        List of `DeviceComponentProductionSpecification` items (represented as `dict` in JSON). """
        
        self.source = None
        """ A source device of this component.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of component it is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceComponent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceComponent, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'languageCode' in jsondict:
            self.languageCode = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['languageCode'], self)
        if 'lastSystemChange' in jsondict:
            self.lastSystemChange = fhirdate.FHIRDate.with_json_and_owner(jsondict['lastSystemChange'], self)
        if 'measurementPrinciple' in jsondict:
            self.measurementPrinciple = jsondict['measurementPrinciple']
        if 'operationalStatus' in jsondict:
            self.operationalStatus = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['operationalStatus'], self)
        if 'parameterGroup' in jsondict:
            self.parameterGroup = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['parameterGroup'], self)
        if 'parent' in jsondict:
            self.parent = fhirreference.FHIRReference.with_json_and_owner(jsondict['parent'], self)
        if 'productionSpecification' in jsondict:
            self.productionSpecification = DeviceComponentProductionSpecification.with_json_and_owner(jsondict['productionSpecification'], self)
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)


class DeviceComponentProductionSpecification(fhirelement.FHIRElement):
    """ Production specification of the component.
    
    Describes the production specification such as component revision, serial
    number, etc.
    """
    
    resource_name = "DeviceComponentProductionSpecification"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.componentId = None
        """ Internal component unique identification.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.productionSpec = None
        """ A printable string defining the component.
        Type `str`. """
        
        self.specType = None
        """ Specification type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceComponentProductionSpecification, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceComponentProductionSpecification, self).update_with_json(jsondict)
        if 'componentId' in jsondict:
            self.componentId = identifier.Identifier.with_json_and_owner(jsondict['componentId'], self)
        if 'productionSpec' in jsondict:
            self.productionSpec = jsondict['productionSpec']
        if 'specType' in jsondict:
            self.specType = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['specType'], self)

