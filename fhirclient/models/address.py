#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Address.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirelement
import period


class Address(fhirelement.FHIRElement):
    """ A postal address.
    """
    
    resource_name = "Address"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.city = None
        """ Name of city, town etc..
        Type `str`. """
        
        self.country = None
        """ Country (can be ISO 3166 3 letter code).
        Type `str`. """
        
        self.line = None
        """ Street name, number, direction & P.O. Box etc.
        List of `str` items. """
        
        self.period = None
        """ Time period when address was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.state = None
        """ Sub-unit of country (abreviations ok).
        Type `str`. """
        
        self.text = None
        """ Text representation of the address.
        Type `str`. """
        
        self.use = None
        """ home | work | temp | old - purpose of this address.
        Type `str`. """
        
        self.zip = None
        """ Postal code for area.
        Type `str`. """
        
        super(Address, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Address, self).update_with_json(jsondict)
        if 'city' in jsondict:
            self.city = jsondict['city']
        if 'country' in jsondict:
            self.country = jsondict['country']
        if 'line' in jsondict:
            self.line = jsondict['line']
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])
        if 'state' in jsondict:
            self.state = jsondict['state']
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'use' in jsondict:
            self.use = jsondict['use']
        if 'zip' in jsondict:
            self.zip = jsondict['zip']

