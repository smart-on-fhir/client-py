#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (deviceobservationreport.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import device
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import observation
import patient


class DeviceObservationReport(fhirresource.FHIRResource):
    """ Describes the data produced by a device at a point in time.
    
    Scope and Usage This resource carries a set of data from a device that is
    observing a subject. Most commonly, the subject is a patient, and the
    device is something like a vital signs monitor, or a glucose measurement
    device, but other kinds of subjects and devices are expected as well.
    
    This resource does not cater for:
    
    * Supporting real-time analytics and in particular, alarms that might be
    raised as a result of such analysis
    * Sending commands to a device
    This capability is expected to be subject of additional resources that are
    yet to be developed, and implmenter input on this is welcome.
    """
    
    resource_name = "DeviceObservationReport"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.identifier = None
        """ As assigned by the source device.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.instant = None
        """ When the data values are reported.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.source = None
        """ Identifies/describes where the data came from.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Subject of the measurement.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.virtualDevice = None
        """ A medical-related subsystem of a medical device.
        List of `DeviceObservationReportVirtualDevice` items (represented as `dict` in JSON). """
        
        super(DeviceObservationReport, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceObservationReport, self).update_with_json(jsondict)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'instant' in jsondict:
            self.instant = fhirdate.FHIRDate.with_json(jsondict['instant'])
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self, device.Device)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'virtualDevice' in jsondict:
            self.virtualDevice = DeviceObservationReportVirtualDevice.with_json(jsondict['virtualDevice'])


class DeviceObservationReportVirtualDevice(fhirelement.FHIRElement):
    """ A medical-related subsystem of a medical device.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.channel = None
        """ Groups related data items.
        List of `DeviceObservationReportVirtualDeviceChannel` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Describes the compartment.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(DeviceObservationReportVirtualDevice, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceObservationReportVirtualDevice, self).update_with_json(jsondict)
        if 'channel' in jsondict:
            self.channel = DeviceObservationReportVirtualDeviceChannel.with_json(jsondict['channel'])
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])


class DeviceObservationReportVirtualDeviceChannel(fhirelement.FHIRElement):
    """ Groups related data items.
    
    Groups together physiological measurement data and derived data.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Describes the channel.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.metric = None
        """ Piece of data reported by device.
        List of `DeviceObservationReportVirtualDeviceChannelMetric` items (represented as `dict` in JSON). """
        
        super(DeviceObservationReportVirtualDeviceChannel, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceObservationReportVirtualDeviceChannel, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'metric' in jsondict:
            self.metric = DeviceObservationReportVirtualDeviceChannelMetric.with_json(jsondict['metric'])


class DeviceObservationReportVirtualDeviceChannelMetric(fhirelement.FHIRElement):
    """ Piece of data reported by device.
    
    A piece of measured or derived data that is reported by the machine.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.observation = None
        """ The data for the metric.
        Type `FHIRReference` referencing `Observation` (represented as `dict` in JSON). """
        
        super(DeviceObservationReportVirtualDeviceChannelMetric, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DeviceObservationReportVirtualDeviceChannelMetric, self).update_with_json(jsondict)
        if 'observation' in jsondict:
            self.observation = fhirreference.FHIRReference.with_json_and_owner(jsondict['observation'], self, observation.Observation)

