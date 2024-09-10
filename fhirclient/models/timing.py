# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Timing).
# 2024, SMART Health IT.


from . import backboneelement

class Timing(backboneelement.BackboneElement):
    """ A timing schedule that specifies an event that may occur multiple times.
    
    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are planned, expected or requested to occur. The most
    common usage is in dosage instructions for medications. They are also used
    when planning care of various kinds, and may be used for reporting the
    schedule to which past regular activities were carried out.
    """
    
    resource_type = "Timing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ BID | TID | QID | AM | PM | QD | QOD | +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.event = None
        """ When the event occurs.
        List of `FHIRDateTime` items (represented as `str` in JSON). """
        self._event = None
        """ Primitive extension for event. Type `FHIRPrimitiveExtension` """
        
        self.repeat = None
        """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """
        self._repeat = None
        """ Primitive extension for repeat. Type `FHIRPrimitiveExtension` """
        
        super(Timing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("event", "event", fhirdatetime.FHIRDateTime, True, None, False),
            ("_event", "_event", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repeat", "repeat", TimingRepeat, False, None, False),
            ("_repeat", "_repeat", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import element

class TimingRepeat(element.Element):
    """ When the event is to occur.
    
    A set of rules that describe when the event is scheduled.
    """
    
    resource_type = "TimingRepeat"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.boundsDuration = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Duration` (represented as `dict` in JSON). """
        self._boundsDuration = None
        """ Primitive extension for boundsDuration. Type `FHIRPrimitiveExtension` """
        
        self.boundsPeriod = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Period` (represented as `dict` in JSON). """
        self._boundsPeriod = None
        """ Primitive extension for boundsPeriod. Type `FHIRPrimitiveExtension` """
        
        self.boundsRange = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Range` (represented as `dict` in JSON). """
        self._boundsRange = None
        """ Primitive extension for boundsRange. Type `FHIRPrimitiveExtension` """
        
        self.count = None
        """ Number of times to repeat.
        Type `int`. """
        self._count = None
        """ Primitive extension for count. Type `FHIRPrimitiveExtension` """
        
        self.countMax = None
        """ Maximum number of times to repeat.
        Type `int`. """
        self._countMax = None
        """ Primitive extension for countMax. Type `FHIRPrimitiveExtension` """
        
        self.dayOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        self._dayOfWeek = None
        """ Primitive extension for dayOfWeek. Type `FHIRPrimitiveExtension` """
        
        self.duration = None
        """ How long when it happens.
        Type `float`. """
        self._duration = None
        """ Primitive extension for duration. Type `FHIRPrimitiveExtension` """
        
        self.durationMax = None
        """ How long when it happens (Max).
        Type `float`. """
        self._durationMax = None
        """ Primitive extension for durationMax. Type `FHIRPrimitiveExtension` """
        
        self.durationUnit = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        self._durationUnit = None
        """ Primitive extension for durationUnit. Type `FHIRPrimitiveExtension` """
        
        self.frequency = None
        """ Event occurs frequency times per period.
        Type `int`. """
        self._frequency = None
        """ Primitive extension for frequency. Type `FHIRPrimitiveExtension` """
        
        self.frequencyMax = None
        """ Event occurs up to frequencyMax times per period.
        Type `int`. """
        self._frequencyMax = None
        """ Primitive extension for frequencyMax. Type `FHIRPrimitiveExtension` """
        
        self.offset = None
        """ Minutes from event (before or after).
        Type `int`. """
        self._offset = None
        """ Primitive extension for offset. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Event occurs frequency times per period.
        Type `float`. """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.periodMax = None
        """ Upper limit of period (3-4 hours).
        Type `float`. """
        self._periodMax = None
        """ Primitive extension for periodMax. Type `FHIRPrimitiveExtension` """
        
        self.periodUnit = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        self._periodUnit = None
        """ Primitive extension for periodUnit. Type `FHIRPrimitiveExtension` """
        
        self.timeOfDay = None
        """ Time of day for action.
        List of `FHIRTime` items (represented as `str` in JSON). """
        self._timeOfDay = None
        """ Primitive extension for timeOfDay. Type `FHIRPrimitiveExtension` """
        
        self.when = None
        """ Code for time period of occurrence.
        List of `str` items. """
        self._when = None
        """ Primitive extension for when. Type `FHIRPrimitiveExtension` """
        
        super(TimingRepeat, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("boundsDuration", "boundsDuration", duration.Duration, False, "bounds", False),
            ("_boundsDuration", "_boundsDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("boundsPeriod", "boundsPeriod", period.Period, False, "bounds", False),
            ("_boundsPeriod", "_boundsPeriod", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("boundsRange", "boundsRange", range.Range, False, "bounds", False),
            ("_boundsRange", "_boundsRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("count", "count", int, False, None, False),
            ("_count", "_count", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("countMax", "countMax", int, False, None, False),
            ("_countMax", "_countMax", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dayOfWeek", "dayOfWeek", str, True, None, False),
            ("_dayOfWeek", "_dayOfWeek", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("_duration", "_duration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("durationMax", "durationMax", float, False, None, False),
            ("_durationMax", "_durationMax", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("durationUnit", "durationUnit", str, False, None, False),
            ("_durationUnit", "_durationUnit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("frequency", "frequency", int, False, None, False),
            ("_frequency", "_frequency", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("frequencyMax", "frequencyMax", int, False, None, False),
            ("_frequencyMax", "_frequencyMax", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("offset", "offset", int, False, None, False),
            ("_offset", "_offset", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", float, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("periodMax", "periodMax", float, False, None, False),
            ("_periodMax", "_periodMax", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("periodUnit", "periodUnit", str, False, None, False),
            ("_periodUnit", "_periodUnit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timeOfDay", "timeOfDay", fhirtime.FHIRTime, True, None, False),
            ("_timeOfDay", "_timeOfDay", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("when", "when", str, True, None, False),
            ("_when", "_when", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import duration
from . import fhirdatetime
from . import fhirtime
from . import period
from . import range