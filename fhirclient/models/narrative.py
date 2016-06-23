#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Narrative) on 2016-06-23.
#  2016, SMART Health IT.


from . import element

class Narrative(element.Element):
    """ A human-readable formatted text, including images.
    """
    
    resource_name = "Narrative"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.div = None
        """ Limited xhtml content.
        Type `str`. """
        
        self.status = None
        """ generated | extensions | additional | empty.
        Type `str`. """
        
        super(Narrative, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("div", "div", str, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


