# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/HumanName).
# 2024, SMART Health IT.


from . import element

class HumanName(element.Element):
    """ Name of a human - parts and usage.
    
    A human's name with the ability to identify parts and usage.
    """
    
    resource_type = "HumanName"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.family = None
        """ Family name (often called 'Surname').
        Type `str`. """
        self._family = None
        """ Primitive extension for family. Type `FHIRPrimitiveExtension` """
        
        self.given = None
        """ Given names (not always 'first'). Includes middle names.
        List of `str` items. """
        self._given = None
        """ Primitive extension for given. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Time period when name was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.prefix = None
        """ Parts that come before the name.
        List of `str` items. """
        self._prefix = None
        """ Primitive extension for prefix. Type `FHIRPrimitiveExtension` """
        
        self.suffix = None
        """ Parts that come after the name.
        List of `str` items. """
        self._suffix = None
        """ Primitive extension for suffix. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Text representation of the full name.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ usual | official | temp | nickname | anonymous | old | maiden.
        Type `str`. """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        super(HumanName, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(HumanName, self).elementProperties()
        js.extend([
            ("family", "family", str, False, None, False),
            ("_family", "_family", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("given", "given", str, True, None, False),
            ("_given", "_given", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prefix", "prefix", str, True, None, False),
            ("_prefix", "_prefix", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("suffix", "suffix", str, True, None, False),
            ("_suffix", "_suffix", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import period