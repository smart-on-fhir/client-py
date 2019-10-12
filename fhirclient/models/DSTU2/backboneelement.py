#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/BackboneElement) on 2019-10-12.
#  2019, SMART Health IT.


from . import element

class BackboneElement(element.Element):
    """ Base for elements defined inside a resource.
    
    Base definition for all elements that are defined inside a resource - but
    not those in a data type.
    """
    
    resource_name = "BackboneElement"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.modifierExtension = None
        """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """
        
        super(BackboneElement, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(BackboneElement, self).elementProperties()
        js.extend([
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False),
        ])
        return js


from . import extension
