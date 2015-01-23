#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3969 (Duration.profile.json) on 2015-01-23.
#  2015, SMART Platforms.


import quantity


class Duration(quantity.Quantity):
    """ A length of time.
    
    There SHALL be a code if there is a value and it SHALL be an expression of
    time.  If system is present, it SHALL be UCUM.
    """
    
    resource_name = "Duration"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Duration, self).__init__(jsondict)

