# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Coding).
# 2024, SMART Health IT.


from . import element

class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """
    
    resource_type = "Coding"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Symbol in syntax defined by the system.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.display = None
        """ Representation defined by the system.
        Type `str`. """
        self._display = None
        """ Primitive extension for display. Type `FHIRPrimitiveExtension` """
        
        self.system = None
        """ Identity of the terminology system.
        Type `str`. """
        self._system = None
        """ Primitive extension for system. Type `FHIRPrimitiveExtension` """
        
        self.userSelected = None
        """ If this coding was chosen directly by the user.
        Type `bool`. """
        self._userSelected = None
        """ Primitive extension for userSelected. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Version of the system - if relevant.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(Coding, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("display", "display", str, False, None, False),
            ("_display", "_display", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("userSelected", "userSelected", bool, False, None, False),
            ("_userSelected", "_userSelected", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension
