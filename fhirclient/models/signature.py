# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Signature).
# 2024, SMART Health IT.


from . import element

class Signature(element.Element):
    """ A Signature - XML DigSig, JWS, Graphical image of signature, etc..
    
    A signature along with supporting context. The signature may be a digital
    signature that is cryptographic in nature, or some other signature
    acceptable to the domain. This other signature may be as simple as a
    graphical image representing a hand-written signature, or a signature
    ceremony Different signature approaches have different utilities.
    """
    
    resource_type = "Signature"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.data = None
        """ The actual signature content (XML DigSig. JWS, picture, etc.).
        Type `str`. """
        self._data = None
        """ Primitive extension for data. Type `FHIRPrimitiveExtension` """
        
        self.onBehalfOf = None
        """ The party represented.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._onBehalfOf = None
        """ Primitive extension for onBehalfOf. Type `FHIRPrimitiveExtension` """
        
        self.sigFormat = None
        """ The technical format of the signature.
        Type `str`. """
        self._sigFormat = None
        """ Primitive extension for sigFormat. Type `FHIRPrimitiveExtension` """
        
        self.targetFormat = None
        """ The technical format of the signed resources.
        Type `str`. """
        self._targetFormat = None
        """ Primitive extension for targetFormat. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        self.when = None
        """ When the signature was created.
        Type `FHIRInstant` (represented as `str` in JSON). """
        self._when = None
        """ Primitive extension for when. Type `FHIRPrimitiveExtension` """
        
        self.who = None
        """ Who signed.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._who = None
        """ Primitive extension for who. Type `FHIRPrimitiveExtension` """
        
        super(Signature, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("_data", "_data", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
            ("_onBehalfOf", "_onBehalfOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sigFormat", "sigFormat", str, False, None, False),
            ("_sigFormat", "_sigFormat", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("targetFormat", "targetFormat", str, False, None, False),
            ("_targetFormat", "_targetFormat", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", coding.Coding, True, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("when", "when", fhirinstant.FHIRInstant, False, None, True),
            ("_when", "_when", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("who", "who", fhirreference.FHIRReference, False, None, True),
            ("_who", "_who", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import coding
from . import fhirinstant
from . import fhirreference