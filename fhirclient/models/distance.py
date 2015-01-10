#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (Distance.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import quantity


class Distance(quantity.Quantity):
    """ A measure of distance.
    
    There SHALL be a code if there is a value and it SHALL be an expression of
    length.  If system is present, it SHALL be UCUM.
    """
    
    resource_name = "Distance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Distance, self).__init__(jsondict)

