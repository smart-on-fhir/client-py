#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (ContactPoint.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import fhirelement
import period


class ContactPoint(fhirelement.FHIRElement):
    """ Details of a Technology mediated contact point (phone, fax, email, etc).
    
    Details for All kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    
    resource_name = "ContactPoint"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ Time period when the contact point was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ phone | fax | email | url.
        Type `str`. """
        
        self.use = None
        """ home | work | temp | old | mobile - purpose of this contact point.
        Type `str`. """
        
        self.value = None
        """ The actual contact point details.
        Type `str`. """
        
        super(ContactPoint, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ContactPoint, self).update_with_json(jsondict)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'use' in jsondict:
            self.use = jsondict['use']
        if 'value' in jsondict:
            self.value = jsondict['value']

