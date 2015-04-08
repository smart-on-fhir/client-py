#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Timing) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import fhirdate
import fhirelement
import period


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
    
    def update_with_json(self, jsondict):
        super(Timing, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'event' in jsondict:
            self.event = fhirdate.FHIRDate.with_json_and_owner(jsondict['event'], self)
        if 'repeat' in jsondict:
            self.repeat = TimingRepeat.with_json_and_owner(jsondict['repeat'], self)


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
    
    def update_with_json(self, jsondict):
        super(TimingRepeat, self).update_with_json(jsondict)
        if 'bounds' in jsondict:
            self.bounds = period.Period.with_json_and_owner(jsondict['bounds'], self)
        if 'count' in jsondict:
            self.count = jsondict['count']
        if 'duration' in jsondict:
            self.duration = jsondict['duration']
        if 'durationUnits' in jsondict:
            self.durationUnits = jsondict['durationUnits']
        if 'frequency' in jsondict:
            self.frequency = jsondict['frequency']
        if 'frequencyMax' in jsondict:
            self.frequencyMax = jsondict['frequencyMax']
        if 'period' in jsondict:
            self.period = jsondict['period']
        if 'periodMax' in jsondict:
            self.periodMax = jsondict['periodMax']
        if 'periodUnits' in jsondict:
            self.periodUnits = jsondict['periodUnits']
        if 'when' in jsondict:
            self.when = jsondict['when']

