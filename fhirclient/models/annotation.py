# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Annotation).
# 2024, SMART Health IT.


from . import element

class Annotation(element.Element):
    """ Text node with attribution.
    
    A  text note which also  contains information about who made the statement
    and when.
    """
    
    resource_type = "Annotation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authorReference = None
        """ Individual responsible for the annotation.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._authorReference = None
        """ Primitive extension for authorReference. Type `FHIRPrimitiveExtension` """
        
        self.authorString = None
        """ Individual responsible for the annotation.
        Type `str`. """
        self._authorString = None
        """ Primitive extension for authorString. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ The annotation  - text content (as markdown).
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.time = None
        """ When the annotation was made.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._time = None
        """ Primitive extension for time. Type `FHIRPrimitiveExtension` """
        
        super(Annotation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Annotation, self).elementProperties()
        js.extend([
            ("authorReference", "authorReference", fhirreference.FHIRReference, False, "author", False),
            ("_authorReference", "_authorReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("authorString", "authorString", str, False, "author", False),
            ("_authorString", "_authorString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, True),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("time", "time", fhirdatetime.FHIRDateTime, False, None, False),
            ("_time", "_time", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import fhirdatetime
from . import fhirreference