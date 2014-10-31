#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-HumanName.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirelement
import period


class HumanName(fhirelement.FHIRElement):
    """ Name of a human - parts and usage.
    """
    
    resource_name = "HumanName"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.family = None
        """ Family name (often called 'Surname').
        List of `str` items. """
        
        self.given = None
        """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """
        
        self.period = None
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.prefix = None
        """ Parts that come before the name.
        List of `str` items. """
        
        self.suffix = None
        """ Parts that come after the name.
        List of `str` items. """
        
        self.text = None
        """ Text representation of the full name.
        Type `str`. """
        
        self.use = None
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """
        
        super(HumanName, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(HumanName, self).update_with_json(jsondict)
        if 'family' in jsondict:
            self.family = jsondict['family']
        if 'given' in jsondict:
            self.given = jsondict['given']
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])
        if 'prefix' in jsondict:
            self.prefix = jsondict['prefix']
        if 'suffix' in jsondict:
            self.suffix = jsondict['suffix']
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'use' in jsondict:
            self.use = jsondict['use']

