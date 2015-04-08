#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DeviceMetric) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import timing


class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.
    
    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    
    resource_name = "DeviceMetric"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.calibration = None
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """
        
        self.category = None
        """ measurement | setting | calculation | unspecified.
        Type `str`. """
        
        self.color = None
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """
        
        self.identifier = None
        """ Unique identifier of this DeviceMetric.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.measurementPeriod = None
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.operationalStatus = None
        """ on | off | standby.
        Type `str`. """
        
        self.parent = None
        """ Describes the link to the parent DeviceComponent.
        Type `FHIRReference` referencing `DeviceComponent` (represented as `dict` in JSON). """
        
        self.source = None
        """ Describes the link to the source Device.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.unit = None
        """ Unit of metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceMetric, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceMetric, self).update_with_json(jsondict)
        if 'calibration' in jsondict:
            self.calibration = DeviceMetricCalibration.with_json_and_owner(jsondict['calibration'], self)
        if 'category' in jsondict:
            self.category = jsondict['category']
        if 'color' in jsondict:
            self.color = jsondict['color']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'measurementPeriod' in jsondict:
            self.measurementPeriod = timing.Timing.with_json_and_owner(jsondict['measurementPeriod'], self)
        if 'operationalStatus' in jsondict:
            self.operationalStatus = jsondict['operationalStatus']
        if 'parent' in jsondict:
            self.parent = fhirreference.FHIRReference.with_json_and_owner(jsondict['parent'], self)
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'unit' in jsondict:
            self.unit = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['unit'], self)


class DeviceMetricCalibration(fhirelement.FHIRElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    
    resource_name = "DeviceMetricCalibration"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.state = None
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """
        
        self.time = None
        """ Describes the time last calibration has been performed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.type = None
        """ unspecified | offset | gain | two-point.
        Type `str`. """
        
        super(DeviceMetricCalibration, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceMetricCalibration, self).update_with_json(jsondict)
        if 'state' in jsondict:
            self.state = jsondict['state']
        if 'time' in jsondict:
            self.time = fhirdate.FHIRDate.with_json_and_owner(jsondict['time'], self)
        if 'type' in jsondict:
            self.type = jsondict['type']

