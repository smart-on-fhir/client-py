#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (BackboneElement.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import fhirelement


class BackboneElement(fhirelement.FHIRElement):
    """ Base for elements defined inside a resource.
    
    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """
    
    resource_name = "BackboneElement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(BackboneElement, self).__init__(jsondict)

