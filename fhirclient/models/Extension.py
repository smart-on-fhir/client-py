#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Extension.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import FHIRElement


class Extension(FHIRElement.FHIRElement):
    """ Optional Extensions Element - found in all resources..
    """
    
    resource_name = "Extension"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.url = None
        """ identifies the meaning of the extension.
        Type `str`. """
        
        self.value = None
        """ Value of extension.
        Type `FHIRElement` (represented as `dict` in JSON). """
        
        super(Extension, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Extension, self).update_with_json(jsondict)
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'value' in jsondict:
            self.value = FHIRElement.FHIRElement.with_json(jsondict['value'])

