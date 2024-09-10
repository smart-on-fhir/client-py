# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/TriggerDefinition).
# 2024, SMART Health IT.


from . import element

class TriggerDefinition(element.Element):
    """ Defines an expected trigger for a module.
    
    A description of a triggering event. Triggering events can be named events,
    data events, or periodic, as determined by the type element.
    """
    
    resource_type = "TriggerDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.condition = None
        """ Whether the event triggers (boolean expression).
        Type `Expression` (represented as `dict` in JSON). """
        self._condition = None
        """ Primitive extension for condition. Type `FHIRPrimitiveExtension` """
        
        self.data = None
        """ Triggering data of the event (multiple = 'and').
        List of `DataRequirement` items (represented as `dict` in JSON). """
        self._data = None
        """ Primitive extension for data. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name or URI that identifies the event.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.timingDate = None
        """ Timing of the event.
        Type `FHIRDate` (represented as `str` in JSON). """
        self._timingDate = None
        """ Primitive extension for timingDate. Type `FHIRPrimitiveExtension` """
        
        self.timingDateTime = None
        """ Timing of the event.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._timingDateTime = None
        """ Primitive extension for timingDateTime. Type `FHIRPrimitiveExtension` """
        
        self.timingReference = None
        """ Timing of the event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._timingReference = None
        """ Primitive extension for timingReference. Type `FHIRPrimitiveExtension` """
        
        self.timingTiming = None
        """ Timing of the event.
        Type `Timing` (represented as `dict` in JSON). """
        self._timingTiming = None
        """ Primitive extension for timingTiming. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ named-event | periodic | data-changed | data-added | data-modified
        | data-removed | data-accessed | data-access-ended.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(TriggerDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TriggerDefinition, self).elementProperties()
        js.extend([
            ("condition", "condition", expression.Expression, False, None, False),
            ("_condition", "_condition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("data", "data", datarequirement.DataRequirement, True, None, False),
            ("_data", "_data", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDate", "timingDate", fhirdate.FHIRDate, False, "timing", False),
            ("_timingDate", "_timingDate", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingDateTime", "timingDateTime", fhirdatetime.FHIRDateTime, False, "timing", False),
            ("_timingDateTime", "_timingDateTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingReference", "timingReference", fhirreference.FHIRReference, False, "timing", False),
            ("_timingReference", "_timingReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("_timingTiming", "_timingTiming", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import datarequirement
from . import expression
from . import fhirdate
from . import fhirdatetime
from . import fhirreference
from . import timing