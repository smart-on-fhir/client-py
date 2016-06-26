#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.4.0.8595 (http://hl7.org/fhir/StructureDefinition/RelatedResource) on 2016-06-26.
#  2016, SMART Health IT.


from . import element

class RelatedResource(element.Element):
    """ Related resources for the module.
    
    Related resources such as additional documentation, justification, or
    bibliographic references.
    """
    
    resource_name = "RelatedResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.document = None
        """ The related document.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.resource = None
        """ The related resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ documentation | justification | citation | predecessor | successor
        | derived-from.
        Type `str`. """
        
        super(RelatedResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedResource, self).elementProperties()
        js.extend([
            ("document", "document", attachment.Attachment, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
        ])
        return js


from . import attachment
from . import fhirreference
