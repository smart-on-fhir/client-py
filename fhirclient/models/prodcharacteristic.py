# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ProdCharacteristic).
# 2024, SMART Health IT.


from . import backboneelement

class ProdCharacteristic(backboneelement.BackboneElement):
    """ The marketing status describes the date when a medicinal product is
    actually put on the market or the date as of which it is no longer
    available.
    """
    
    resource_type = "ProdCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.color = None
        """ Where applicable, the color can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        List of `str` items. """
        self._color = None
        """ Primitive extension for color. Type `FHIRPrimitiveExtension` """
        
        self.depth = None
        """ Where applicable, the depth can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        self._depth = None
        """ Primitive extension for depth. Type `FHIRPrimitiveExtension` """
        
        self.externalDiameter = None
        """ Where applicable, the external diameter can be specified using a
        numerical value and its unit of measurement The unit of measurement
        shall be specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        self._externalDiameter = None
        """ Primitive extension for externalDiameter. Type `FHIRPrimitiveExtension` """
        
        self.height = None
        """ Where applicable, the height can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        self._height = None
        """ Primitive extension for height. Type `FHIRPrimitiveExtension` """
        
        self.image = None
        """ Where applicable, the image can be provided The format of the image
        attachment shall be specified by regional implementations.
        List of `Attachment` items (represented as `dict` in JSON). """
        self._image = None
        """ Primitive extension for image. Type `FHIRPrimitiveExtension` """
        
        self.imprint = None
        """ Where applicable, the imprint can be specified as text.
        List of `str` items. """
        self._imprint = None
        """ Primitive extension for imprint. Type `FHIRPrimitiveExtension` """
        
        self.nominalVolume = None
        """ Where applicable, the nominal volume can be specified using a
        numerical value and its unit of measurement The unit of measurement
        shall be specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        self._nominalVolume = None
        """ Primitive extension for nominalVolume. Type `FHIRPrimitiveExtension` """
        
        self.scoring = None
        """ Where applicable, the scoring can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._scoring = None
        """ Primitive extension for scoring. Type `FHIRPrimitiveExtension` """
        
        self.shape = None
        """ Where applicable, the shape can be specified An appropriate
        controlled vocabulary shall be used The term and the term
        identifier shall be used.
        Type `str`. """
        self._shape = None
        """ Primitive extension for shape. Type `FHIRPrimitiveExtension` """
        
        self.weight = None
        """ Where applicable, the weight can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        self._weight = None
        """ Primitive extension for weight. Type `FHIRPrimitiveExtension` """
        
        self.width = None
        """ Where applicable, the width can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be
        specified in accordance with ISO 11240 and the resulting
        terminology The symbol and the symbol identifier shall be used.
        Type `Quantity` (represented as `dict` in JSON). """
        self._width = None
        """ Primitive extension for width. Type `FHIRPrimitiveExtension` """
        
        super(ProdCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProdCharacteristic, self).elementProperties()
        js.extend([
            ("color", "color", str, True, None, False),
            ("_color", "_color", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("depth", "depth", quantity.Quantity, False, None, False),
            ("_depth", "_depth", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("externalDiameter", "externalDiameter", quantity.Quantity, False, None, False),
            ("_externalDiameter", "_externalDiameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("height", "height", quantity.Quantity, False, None, False),
            ("_height", "_height", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("image", "image", attachment.Attachment, True, None, False),
            ("_image", "_image", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("imprint", "imprint", str, True, None, False),
            ("_imprint", "_imprint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("nominalVolume", "nominalVolume", quantity.Quantity, False, None, False),
            ("_nominalVolume", "_nominalVolume", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("scoring", "scoring", codeableconcept.CodeableConcept, False, None, False),
            ("_scoring", "_scoring", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("shape", "shape", str, False, None, False),
            ("_shape", "_shape", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("weight", "weight", quantity.Quantity, False, None, False),
            ("_weight", "_weight", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("width", "width", quantity.Quantity, False, None, False),
            ("_width", "_width", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import quantity