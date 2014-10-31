#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Schedule.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirdate
import fhirelement
import period


class Schedule(fhirelement.FHIRElement):
    """ A schedule that specifies an event that may occur multiple times.
    """
    
    resource_name = "Schedule"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.event = None
        """ When the event occurs.
        List of `Period` items (represented as `dict` in JSON). """
        
        self.repeat = None
        """ Only if there is none or one event.
        Type `ScheduleRepeat` (represented as `dict` in JSON). """
        
        super(Schedule, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Schedule, self).update_with_json(jsondict)
        if 'event' in jsondict:
            self.event = period.Period.with_json(jsondict['event'])
        if 'repeat' in jsondict:
            self.repeat = ScheduleRepeat.with_json(jsondict['repeat'])


class ScheduleRepeat(fhirelement.FHIRElement):
    """ Only if there is none or one event.
    
    Identifies a repeating pattern to the intended time periods.
    """
    
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
        
        super(ScheduleRepeat, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ScheduleRepeat, self).update_with_json(jsondict)
        if 'count' in jsondict:
            self.count = jsondict['count']
        if 'duration' in jsondict:
            self.duration = jsondict['duration']
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json(jsondict['end'])
        if 'frequency' in jsondict:
            self.frequency = jsondict['frequency']
        if 'units' in jsondict:
            self.units = jsondict['units']
        if 'when' in jsondict:
            self.when = jsondict['when']

