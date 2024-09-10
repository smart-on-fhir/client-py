# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Identifier).
# 2024, SMART Health IT.


from . import element

class Identifier(element.Element):
    """ An identifier intended for computation.
    
    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """
    
    resource_type = "Identifier"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.assigner = None
        """ Organization that issued id (may be just text).
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._assigner = None
        """ Primitive extension for assigner. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Time period when id is/was valid for use.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.system = None
        """ The namespace for the identifier value.
        Type `str`. """
        self._system = None
        """ Primitive extension for system. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Description of identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.use = None
        """ usual | official | temp | secondary | old (If known).
        Type `str`. """
        self._use = None
        """ Primitive extension for use. Type `FHIRPrimitiveExtension` """
        
        self.value = None
        """ The value that is unique.
        Type `str`. """
        self._value = None
        """ Primitive extension for value. Type `FHIRPrimitiveExtension` """
        
        super(Identifier, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Identifier, self).elementProperties()
        js.extend([
            ("assigner", "assigner", fhirreference.FHIRReference, False, None, False),
            ("_assigner", "_assigner", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("system", "system", str, False, None, False),
            ("_system", "_system", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("use", "use", str, False, None, False),
            ("_use", "_use", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("value", "value", str, False, None, False),
            ("_value", "_value", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import period