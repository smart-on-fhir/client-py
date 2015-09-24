#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DeviceComponent) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class DeviceComponent(domainresource.DomainResource):
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
    
    def elementProperties(self):
        js = super(DeviceComponent, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, False),
            ("lastSystemChange", "lastSystemChange", fhirdate.FHIRDate, False),
            ("measurementPrinciple", "measurementPrinciple", str, False),
            ("operationalStatus", "operationalStatus", codeableconcept.CodeableConcept, True),
            ("parameterGroup", "parameterGroup", codeableconcept.CodeableConcept, False),
            ("parent", "parent", fhirreference.FHIRReference, False),
            ("productionSpecification", "productionSpecification", DeviceComponentProductionSpecification, True),
            ("source", "source", fhirreference.FHIRReference, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js


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
    
    def elementProperties(self):
        js = super(DeviceComponentProductionSpecification, self).elementProperties()
        js.extend([
            ("componentId", "componentId", identifier.Identifier, False),
            ("productionSpec", "productionSpec", str, False),
            ("specType", "specType", codeableconcept.CodeableConcept, False),
        ])
        return js

