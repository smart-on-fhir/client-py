#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (Timing.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import fhirdate
import fhirelement
import period


class Timing(fhirelement.FHIRElement):
    """ A timing schedule that specifies an event that may occur multiple times.
    
    Specifies an event that may occur multiple times. Timing schedules are used
    for to record when things are expected or requested to occur.
    """
    
    resource_name = "Timing"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.event = None
        """ When the event occurs.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.repeat = None
        """ Only if there is none or one event.
        Type `TimingRepeat` (represented as `dict` in JSON). """
        
        super(Timing, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Timing, self).update_with_json(jsondict)
        if 'event' in jsondict:
            self.event = period.Period.with_json_and_owner(jsondict['event'], self)
        if 'repeat' in jsondict:
            self.repeat = TimingRepeat.with_json_and_owner(jsondict['repeat'], self)


class TimingRepeat(fhirelement.FHIRElement):
    """ Only if there is none or one event.
    
    Identifies a repeating pattern to the intended time periods.
    """
    
    resource_name = "TimingRepeat"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.count = None
        """ Number of times to repeat.
        Type `int`. """
        
        self.duration = None
        """ Repeating or event-related duration.
        Type `float`. """
        
        self.end = None
        """ When to stop repeats.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.frequency = None
        """ Event occurs frequency times per duration.
        Type `int`. """
        
        self.units = None
        """ s | min | h | d | wk | mo | a - unit of time (UCUM).
        Type `str`. """
        
        self.when = None
        """ HS | WAKE | AC | ACM | ACD | ACV | PC | PCM | PCD | PCV - common
        life events.
        Type `str`. """
        
        super(TimingRepeat, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(TimingRepeat, self).update_with_json(jsondict)
        if 'count' in jsondict:
            self.count = jsondict['count']
        if 'duration' in jsondict:
            self.duration = jsondict['duration']
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json_and_owner(jsondict['end'], self)
        if 'frequency' in jsondict:
            self.frequency = jsondict['frequency']
        if 'units' in jsondict:
            self.units = jsondict['units']
        if 'when' in jsondict:
            self.when = jsondict['when']

