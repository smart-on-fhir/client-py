#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/BackboneElement) on 2015-07-06.
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

