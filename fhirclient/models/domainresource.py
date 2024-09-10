# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/DomainResource).
# 2024, SMART Health IT.


from . import resource

class DomainResource(resource.Resource):
    """ A resource with narrative, extensions, and contained resources.
    
    A resource that includes narrative, extensions, and contained resources.
    """
    
    resource_type = "DomainResource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contained = None
        """ Contained, inline Resources.
        List of `Resource` items (represented as `dict` in JSON). """
        self._contained = None
        """ Primitive extension for contained. Type `FHIRPrimitiveExtension` """
        
        self.extension = None
        """ Additional content defined by implementations.
        List of `Extension` items (represented as `dict` in JSON). """
        self._extension = None
        """ Primitive extension for extension. Type `FHIRPrimitiveExtension` """
        
        self.modifierExtension = None
        """ Extensions that cannot be ignored.
        List of `Extension` items (represented as `dict` in JSON). """
        self._modifierExtension = None
        """ Primitive extension for modifierExtension. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        super(DomainResource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(DomainResource, self).elementProperties()
        js.extend([
            ("contained", "contained", resource.Resource, True, None, False),
            ("_contained", "_contained", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("extension", "extension", extension.Extension, True, None, False),
            ("_extension", "_extension", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modifierExtension", "modifierExtension", extension.Extension, True, None, False),
            ("_modifierExtension", "_modifierExtension", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", narrative.Narrative, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import extension
from . import narrative