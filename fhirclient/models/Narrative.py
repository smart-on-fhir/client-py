#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Narrative.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import fhirelement


class Narrative(fhirelement.FHIRElement):
    """ A human-readable formatted text, including images.
    """
    
    resource_name = "Narrative"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.div = None
        """ Limited xhtml content.
        Type `str`. """
        
        self.status = None
        """ generated | extensions | additional.
        Type `str`. """
        
        super(Narrative, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Narrative, self).update_with_json(jsondict)
        if 'div' in jsondict:
            self.div = jsondict['div']
        if 'status' in jsondict:
            self.status = jsondict['status']

