#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Timing) on 2016-06-23.
#  2016, SMART Health IT.


from . import element

class Timing(element.Element):
    """ A timing schedule that specifies an event that may occur multiple times.
    
    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are expected or requested to occur. The most common
    usage is in dosage instructions for medications. They are also used when
    planning care of various kinds.
    """
    
    resource_name = "Timing"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ QD | QOD | Q4H | Q6H | BID | TID | QID | AM | PM +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.event = None
        """ When the event occurs.
        List of `FHIRDate` items (represented as `str` in JSON). """
        
        self.repeat = None
        """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """
        
        super(Timing, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("event", "event", fhirdate.FHIRDate, True, None, False),
            ("repeat", "repeat", TimingRepeat, False, None, False),
        ])
        return js


class TimingRepeat(element.Element):
    """ When the event is to occur.
    
    A set of rules that describe when the event should occur.
    """
    
    resource_name = "TimingRepeat"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.boundsPeriod = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Period` (represented as `dict` in JSON). """
        
        self.boundsQuantity = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Quantity` referencing `Duration` (represented as `dict` in JSON). """
        
        self.boundsRange = None
        """ Length/Range of lengths, or (Start and/or end) limits.
        Type `Range` (represented as `dict` in JSON). """
        
        self.count = None
        """ Number of times to repeat.
        Type `int`. """
        
        self.duration = None
        """ How long when it happens.
        Type `float`. """
        
        self.durationMax = None
        """ How long when it happens (Max).
        Type `float`. """
        
        self.durationUnits = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self.frequency = None
        """ Event occurs frequency times per period.
        Type `int`. """
        
        self.frequencyMax = None
        """ Event occurs up to frequencyMax times per period.
        Type `int`. """
        
        self.period = None
        """ Event occurs frequency times per period.
        Type `float`. """
        
        self.periodMax = None
        """ Upper limit of period (3-4 hours).
        Type `float`. """
        
        self.periodUnits = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self.when = None
        """ Regular life events the event is tied to.
        Type `str`. """
        
        super(TimingRepeat, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("boundsPeriod", "boundsPeriod", period.Period, False, "bounds", False),
            ("boundsQuantity", "boundsQuantity", quantity.Quantity, False, "bounds", False),
            ("boundsRange", "boundsRange", range.Range, False, "bounds", False),
            ("count", "count", int, False, None, False),
            ("duration", "duration", float, False, None, False),
            ("durationMax", "durationMax", float, False, None, False),
            ("durationUnits", "durationUnits", str, False, None, False),
            ("frequency", "frequency", int, False, None, False),
            ("frequencyMax", "frequencyMax", int, False, None, False),
            ("period", "period", float, False, None, False),
            ("periodMax", "periodMax", float, False, None, False),
            ("periodUnits", "periodUnits", str, False, None, False),
            ("when", "when", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import period
from . import quantity
from . import range
