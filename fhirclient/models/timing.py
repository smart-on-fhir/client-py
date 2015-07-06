#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Timing) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import fhirdate
from . import fhirelement
from . import period


class Timing(fhirelement.FHIRElement):
    """ A timing schedule that specifies an event that may occur multiple times.
    
    Specifies an event that may occur multiple times. Timing schedules are used
    to record when things are expected or requested to occur. The most common
    usage is in dosage instructions for medications. They are also used when
    planning care of various kinds.
    """
    
    resource_name = "Timing"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ BID | TID | QID | AM | PM +.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.event = None
        """ When the event occurs.
        List of `FHIRDate` items (represented as `str` in JSON). """
        
        self.repeat = None
        """ When the event is to occur.
        Type `TimingRepeat` (represented as `dict` in JSON). """
        
        super(Timing, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Timing, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("event", "event", fhirdate.FHIRDate, True),
            ("repeat", "repeat", TimingRepeat, False),
        ])
        return js


class TimingRepeat(fhirelement.FHIRElement):
    """ When the event is to occur.
    
    A set of rules that describe when the event should occur.
    """
    
    resource_name = "TimingRepeat"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bounds = None
        """ Start and/or end limits.
        Type `Period` (represented as `dict` in JSON). """
        
        self.count = None
        """ Number of times to repeat.
        Type `int`. """
        
        self.duration = None
        """ How long when it happens.
        Type `float`. """
        
        self.durationUnits = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self.frequency = None
        """ Event occurs frequency times per duration.
        Type `int`. """
        
        self.frequencyMax = None
        """ Event occurs frequency times per duration.
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
        
        super(TimingRepeat, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(TimingRepeat, self).elementProperties()
        js.extend([
            ("bounds", "bounds", period.Period, False),
            ("count", "count", int, False),
            ("duration", "duration", float, False),
            ("durationUnits", "durationUnits", str, False),
            ("frequency", "frequency", int, False),
            ("frequencyMax", "frequencyMax", int, False),
            ("period", "period", float, False),
            ("periodMax", "periodMax", float, False),
            ("periodUnits", "periodUnits", str, False),
            ("when", "when", str, False),
        ])
        return js

