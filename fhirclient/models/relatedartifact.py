# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/RelatedArtifact).
# 2024, SMART Health IT.


from . import element

class RelatedArtifact(element.Element):
    """ Related artifacts for a knowledge resource.
    
    Related artifacts such as additional documentation, justification, or
    bibliographic references.
    """
    
    resource_type = "RelatedArtifact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.citation = None
        """ Bibliographic citation for the artifact.
        Type `str`. """
        self._citation = None
        """ Primitive extension for citation. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ Brief description of the related artifact.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.document = None
        """ What document is being referenced.
        Type `Attachment` (represented as `dict` in JSON). """
        self._document = None
        """ Primitive extension for document. Type `FHIRPrimitiveExtension` """
        
        self.label = None
        """ Short label.
        Type `str`. """
        self._label = None
        """ Primitive extension for label. Type `FHIRPrimitiveExtension` """
        
        self.resource = None
        """ What resource is being referenced.
        Type `str`. """
        self._resource = None
        """ Primitive extension for resource. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ documentation | justification | citation | predecessor | successor
        | derived-from | depends-on | composed-of.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Where the artifact can be accessed.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(RelatedArtifact, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(RelatedArtifact, self).elementProperties()
        js.extend([
            ("citation", "citation", str, False, None, False),
            ("_citation", "_citation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("document", "document", attachment.Attachment, False, None, False),
            ("_document", "_document", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("label", "label", str, False, None, False),
            ("_label", "_label", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("resource", "resource", str, False, None, False),
            ("_resource", "_resource", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment