#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Period.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirdate
import fhirelement


class Period(fhirelement.FHIRElement):
    """ Time range defined by start and end date/time.
    """
    
    resource_name = "Period"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.end = None
        """ End time with inclusive boundary, if not ongoing.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.start = None
        """ Starting time with inclusive boundary.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(Period, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Period, self).update_with_json(jsondict)
        if 'end' in jsondict:
            self.end = fhirdate.FHIRDate.with_json(jsondict['end'])
        if 'start' in jsondict:
            self.start = fhirdate.FHIRDate.with_json(jsondict['start'])

