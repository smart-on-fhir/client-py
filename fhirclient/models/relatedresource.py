#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 (http://hl7.org/fhir/StructureDefinition/RelatedResource) on 2016-08-31.
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
        
        self.citation = None
        """ Bibliographic citation for the resource.
        Type `str`. """
        
        self.display = None
        """ Brief description of the related resource.
        Type `str`. """
        
        self.document = None
        """ The related document.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.resource = None
        """ The related resource.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ documentation | justification | citation | predecessor | successor
        | derived-from | depends-on | composed-of.
        Type `str`. """
        
        self.url = None
        """ Url for the related resource.
        Type `str`. """
        
        super(RelatedResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedResource, self).elementProperties()
        js.extend([
            ("citation", "citation", str, False, None, False),
            ("display", "display", str, False, None, False),
            ("document", "document", attachment.Attachment, False, None, False),
            ("resource", "resource", fhirreference.FHIRReference, False, None, False),
            ("type", "type", str, False, None, True),
            ("url", "url", str, False, None, False),
        ])
        return js


from . import attachment
from . import fhirreference
