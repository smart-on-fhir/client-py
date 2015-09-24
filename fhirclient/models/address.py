#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Address) on 2015-09-24.
#  2015, SMART Health IT.


from . import fhirelement
from . import period


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
        
        self.district = None
        """ District name (aka county).
        Type `str`. """
        
        self.line = None
        """ Street name, number, direction & P.O. Box etc..
        List of `str` items. """
        
        self.period = None
        """ Time period when address was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.postalCode = None
        """ Postal code for area.
        Type `str`. """
        
        self.state = None
        """ Sub-unit of country (abbreviations ok).
        Type `str`. """
        
        self.text = None
        """ Text representation of the address.
        Type `str`. """
        
        self.type = None
        """ postal | physical | both.
        Type `str`. """
        
        self.use = None
        """ home | work | temp | old - purpose of this address.
        Type `str`. """
        
        super(Address, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("city", "city", str, False),
            ("country", "country", str, False),
            ("district", "district", str, False),
            ("line", "line", str, True),
            ("period", "period", period.Period, False),
            ("postalCode", "postalCode", str, False),
            ("state", "state", str, False),
            ("text", "text", str, False),
            ("type", "type", str, False),
            ("use", "use", str, False),
        ])
        return js

