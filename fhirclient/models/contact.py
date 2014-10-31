#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Contact.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import fhirelement
import period


class Contact(fhirelement.FHIRElement):
    """ Technology mediated contact details (phone, fax, email, etc).
    """
    
    resource_name = "Contact"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.period = None
        """ Time period when the contact was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.system = None
        """ phone | fax | email | url.
        Type `str`. """
        
        self.use = None
        """ home | work | temp | old | mobile - purpose of this address.
        Type `str`. """
        
        self.value = None
        """ The actual contact details.
        Type `str`. """
        
        super(Contact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Contact, self).update_with_json(jsondict)
        if 'period' in jsondict:
            self.period = period.Period.with_json(jsondict['period'])
        if 'system' in jsondict:
            self.system = jsondict['system']
        if 'use' in jsondict:
            self.use = jsondict['use']
        if 'value' in jsondict:
            self.value = jsondict['value']

