#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (uuid.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import fhirelement


class str(fhirelement.FHIRElement):
    """ Primitive Type base64Binary.
    
    A stream of bytes
    """
    
    resource_name = "base64Binary"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(str, self).__init__(jsondict)

