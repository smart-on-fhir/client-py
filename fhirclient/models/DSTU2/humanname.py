#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/HumanName) on 2019-10-12.
#  2019, SMART Health IT.


from . import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.
    
    A human's name with the ability to identify parts and usage.
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
    
    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("family", "family", str, True, None, False),
            ("given", "given", str, True, None, False),
            ("period", "period", period.Period, False, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("text", "text", str, False, None, False),
            ("use", "use", str, False, None, False),
        ])
        return js


from . import period
