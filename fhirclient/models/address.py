#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Address) on 2015-04-08.
#  2015, SMART Health IT.


import fhirelement
import period


class Address(fhirelement.FHIRElement):
    """ A postal address.
    
    There is a variety of postal address formats defined around the world. This
    format defines a superset that is the basis for all addresses around the
    world.
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
        
        self.postalCode = None
        """ Postal code for area.
        Type `str`. """
        
        self.state = None
        """ Sub-unit of country (abreviations ok).
        Type `str`. """
        
        self.text = None
        """ Text representation of the address.
        Type `str`. """
        
        self.use = None
        """ home | work | temp | old - purpose of this address.
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
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'postalCode' in jsondict:
            self.postalCode = jsondict['postalCode']
        if 'state' in jsondict:
            self.state = jsondict['state']
        if 'text' in jsondict:
            self.text = jsondict['text']
        if 'use' in jsondict:
            self.use = jsondict['use']

