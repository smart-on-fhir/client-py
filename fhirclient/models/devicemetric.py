# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DeviceMetric).
# 2024, SMART Health IT.


from . import domainresource

class DeviceMetric(domainresource.DomainResource):
    """ Measurement, calculation or setting capability of a medical device.
    
    Describes a measurement, calculation or setting capability of a medical
    device.
    """
    
    resource_type = "DeviceMetric"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.calibration = None
        """ Describes the calibrations that have been performed or that are
        required to be performed.
        List of `DeviceMetricCalibration` items (represented as `dict` in JSON). """
        self._calibration = None
        """ Primitive extension for calibration. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ measurement | setting | calculation | unspecified.
        Type `str`. """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.color = None
        """ black | red | green | yellow | blue | magenta | cyan | white.
        Type `str`. """
        self._color = None
        """ Primitive extension for color. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Instance identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.measurementPeriod = None
        """ Describes the measurement repetition time.
        Type `Timing` (represented as `dict` in JSON). """
        self._measurementPeriod = None
        """ Primitive extension for measurementPeriod. Type `FHIRPrimitiveExtension` """
        
        self.operationalStatus = None
        """ on | off | standby | entered-in-error.
        Type `str`. """
        self._operationalStatus = None
        """ Primitive extension for operationalStatus. Type `FHIRPrimitiveExtension` """
        
        self.parent = None
        """ Describes the link to the parent Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._parent = None
        """ Primitive extension for parent. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Describes the link to the source Device.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Identity of metric, for example Heart Rate or PEEP Setting.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.unit = None
        """ Unit of Measure for the Metric.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._unit = None
        """ Primitive extension for unit. Type `FHIRPrimitiveExtension` """
        
        super(DeviceMetric, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceMetric, self).elementProperties()
        js.extend([
            ("calibration", "calibration", DeviceMetricCalibration, True, None, False),
            ("_calibration", "_calibration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", str, False, None, True),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("color", "color", str, False, None, False),
            ("_color", "_color", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("measurementPeriod", "measurementPeriod", timing.Timing, False, None, False),
            ("_measurementPeriod", "_measurementPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("operationalStatus", "operationalStatus", str, False, None, False),
            ("_operationalStatus", "_operationalStatus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("parent", "parent", fhirreference.FHIRReference, False, None, False),
            ("_parent", "_parent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("unit", "unit", codeableconcept.CodeableConcept, False, None, False),
            ("_unit", "_unit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class DeviceMetricCalibration(backboneelement.BackboneElement):
    """ Describes the calibrations that have been performed or that are required to
    be performed.
    """
    
    resource_type = "DeviceMetricCalibration"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.state = None
        """ not-calibrated | calibration-required | calibrated | unspecified.
        Type `str`. """
        self._state = None
        """ Primitive extension for state. Type `FHIRPrimitiveExtension` """
        
        self.time = None
        """ Describes the time last calibration has been performed.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._time = None
        """ Primitive extension for time. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ unspecified | offset | gain | two-point.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(DeviceMetricCalibration, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DeviceMetricCalibration, self).elementProperties()
        js.extend([
            ("state", "state", str, False, None, False),
            ("_state", "_state", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("time", "time", fhirinstant.FHIRInstant, False, None, False),
            ("_time", "_time", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirinstant
from . import fhirreference
from . import identifier
from . import timing