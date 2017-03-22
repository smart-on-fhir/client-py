#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Element) on 2017-03-22.
#  2017, SMART Health IT.


from . import fhirabstractbase

class Element(fhirabstractbase.FHIRAbstractBase):
    """ Base for all elements.
    
    Base definition for all elements in a resource.
    """
    
    resource_type = "Element"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.extension = None
        """ Additional Content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """
        
        self.id = None
        """ xml:id (or equivalent in JSON).
        Type `str`. """
        
        super(Element, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Element, self).elementProperties()
        from . import extension
        js.extend([
            ("extension", "extension", extension.Extension, True, None, False),
            ("id", "id", str, False, None, False),
        ])
        return js


