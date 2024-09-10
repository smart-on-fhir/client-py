# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Address).
# 2024, SMART Health IT.


from . import element

class Address(element.Element):
    """ An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).
    
    An address expressed using postal conventions (as opposed to GPS or other
    location definition formats).  This data type may be used to convey
    addresses for use in delivering mail as well as for visiting locations
    which might not be valid for mail delivery.  There are a variety of postal
    address formats defined around the world.
    """
    
    resource_type = "Address"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.city = None
        """ Name of city, town etc..
        Type `str`. """
        self._city = None
        """ Primitive extension for city. Type `FHIRPrimitiveExtension` """
        
        self.country = None
        """ Country (e.g. can be ISO 3166 2 or 3 letter code).
        Type `str`. """
        self._country = None
        """ Primitive extension for country. Type `FHIRPrimitiveExtension` """
        
        self.district = None
        """ District name (aka county).
        Type `str`. """
        self._district = None
        """ Primitive extension for district. Type `FHIRPrimitiveExtension` """
        
        self.line = None
        """ Street name, number, direction & P.O. Box etc..
        List of `str` items. """
        self._line = None
        """ Primitive extension for line. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Time period when address was/is in use.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.postalCode = None
        """ Postal code for area.
        Type `str`. """
        self._postalCode = None
        """ Primitive extension for postalCode. Type `FHIRPrimitiveExtension` """
        
        self.state = None
        """ Sub-unit of country (abbreviations ok).
        Type `str`. """
        self._state = None
        """ Primitive extension for state. Type `FHIRPrimitiveExtension` """
        
        self.text = None
        """ Text representation of the address.
        Type `str`. """
        self._text = None
        """ Primitive extension for text. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ postal | physical | both.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ home | work | temp | old | billing - purpose of this address.
        Type `str`. """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        super(Address, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Address, self).elementProperties()
        js.extend([
            ("city", "city", str, False, None, False),
            ("_city", "_city", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("country", "country", str, False, None, False),
            ("_country", "_country", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("district", "district", str, False, None, False),
            ("_district", "_district", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("line", "line", str, True, None, False),
            ("_line", "_line", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("postalCode", "postalCode", str, False, None, False),
            ("_postalCode", "_postalCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("state", "state", str, False, None, False),
            ("_state", "_state", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("text", "text", str, False, None, False),
            ("_text", "_text", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import period