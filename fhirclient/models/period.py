#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Period) on 2015-09-24.
#  2015, SMART Health IT.


from . import fhirdate
from . import fhirelement


class Period(fhirelement.FHIRElement):
    """ Time range defined by start and end date/time.
    
    A time period defined by a start and end date and optionally time.
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
    
    def elementProperties(self):
        js = super(Period, self).elementProperties()
        js.extend([
            ("end", "end", fhirdate.FHIRDate, False),
            ("start", "start", fhirdate.FHIRDate, False),
        ])
        return js

