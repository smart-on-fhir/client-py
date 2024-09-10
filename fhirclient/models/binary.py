# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Binary).
# 2024, SMART Health IT.


from . import resource

class Binary(resource.Resource):
    """ Pure binary content defined by a format other than FHIR.
    
    A resource that represents the data of a single raw artifact as digital
    content accessible in its native format.  A Binary resource can contain any
    content, whether text, image, pdf, zip archive, etc.
    """
    
    resource_type = "Binary"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ MimeType of the binary content.
        Type `str`. """
        self._contentType = None
        """ Primitive extension for contentType. Type `FHIRPrimitiveExtension` """
        
        self.data = None
        """ The actual content.
        Type `str`. """
        self._data = None
        """ Primitive extension for data. Type `FHIRPrimitiveExtension` """
        
        self.securityContext = None
        """ Identifies another resource to use as proxy when enforcing access
        control.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._securityContext = None
        """ Primitive extension for securityContext. Type `FHIRPrimitiveExtension` """
        
        super(Binary, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Binary, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, True),
            ("_contentType", "_contentType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("data", "data", str, False, None, False),
            ("_data", "_data", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("securityContext", "securityContext", fhirreference.FHIRReference, False, None, False),
            ("_securityContext", "_securityContext", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirreference