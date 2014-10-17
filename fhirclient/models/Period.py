#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Period.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


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

