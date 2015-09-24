#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/BackboneElement) on 2015-09-24.
#  2015, SMART Health IT.


from . import fhirelement


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

