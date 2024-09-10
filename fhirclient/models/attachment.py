# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Attachment).
# 2024, SMART Health IT.


from . import element

class Attachment(element.Element):
    """ Content in a format defined elsewhere.
    
    For referring to data content defined in other formats.
    """
    
    resource_type = "Attachment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentType = None
        """ Mime type of the content, with charset etc..
        Type `str`. """
        self._contentType = None
        """ Primitive extension for contentType. Type `FHIRPrimitiveExtension` """
        
        self.creation = None
        """ Date attachment was first created.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._creation = None
        """ Primitive extension for creation. Type `FHIRPrimitiveExtension` """
        
        self.data = None
        """ Data inline, base64ed.
        Type `str`. """
        self._data = None
        """ Primitive extension for data. Type `FHIRPrimitiveExtension` """
        
        self.hash = None
        """ Hash of the data (sha-1, base64ed).
        Type `str`. """
        self._hash = None
        """ Primitive extension for hash. Type `FHIRPrimitiveExtension` """
        
        self.language = None
        """ Human language of the content (BCP-47).
        Type `str`. """
        self._language = None
        """ Primitive extension for language. Type `FHIRPrimitiveExtension` """
        
        self.size = None
        """ Number of bytes of content (if url provided).
        Type `int`. """
        self._size = None
        """ Primitive extension for size. Type `FHIRPrimitiveExtension` """
        
        self.title = None
        """ Label to display in place of the data.
        Type `str`. """
        self._title = None
        """ Primitive extension for title. Type `FHIRPrimitiveExtension` """
        
        self.url = None
        """ Uri where the data can be found.
        Type `str`. """
        self._url = None
        """ Primitive extension for url. Type `FHIRPrimitiveExtension` """
        
        super(Attachment, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False, None, False),
            ("_contentType", "_contentType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("creation", "creation", fhirdatetime.FHIRDateTime, False, None, False),
            ("_creation", "_creation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("data", "data", str, False, None, False),
            ("_data", "_data", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("hash", "hash", str, False, None, False),
            ("_hash", "_hash", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("language", "language", str, False, None, False),
            ("_language", "_language", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("size", "size", int, False, None, False),
            ("_size", "_size", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("title", "title", str, False, None, False),
            ("_title", "_title", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("url", "url", str, False, None, False),
            ("_url", "_url", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirdatetime