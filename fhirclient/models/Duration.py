#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-Duration.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import Quantity


class Duration(Quantity.Quantity):
    """ Profile for Duration on Quantity.
    
    Basic Profile for Duration on Quantity for validation support
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(Duration, self).__init__(jsondict)

