# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SampledData).
# 2024, SMART Health IT.


from . import element

class SampledData(element.Element):
    """ A series of measurements taken by a device.
    
    A series of measurements taken by a device, with upper and lower limits.
    There may be more than one dimension in the data.
    """
    
    resource_type = "SampledData"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.data = None
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """
        self._data = None
        """ Primitive extension for data. Type `FHIRPrimitiveExtension` """
        
        self.dimensions = None
        """ Number of sample points at each time point.
        Type `int`. """
        self._dimensions = None
        """ Primitive extension for dimensions. Type `FHIRPrimitiveExtension` """
        
        self.factor = None
        """ Multiply data by this before adding to origin.
        Type `float`. """
        self._factor = None
        """ Primitive extension for factor. Type `FHIRPrimitiveExtension` """
        
        self.lowerLimit = None
        """ Lower limit of detection.
        Type `float`. """
        self._lowerLimit = None
        """ Primitive extension for lowerLimit. Type `FHIRPrimitiveExtension` """
        
        self.origin = None
        """ Zero value and units.
        Type `Quantity` (represented as `dict` in JSON). """
        self._origin = None
        """ Primitive extension for origin. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Number of milliseconds between samples.
        Type `float`. """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.upperLimit = None
        """ Upper limit of detection.
        Type `float`. """
        self._upperLimit = None
        """ Primitive extension for upperLimit. Type `FHIRPrimitiveExtension` """
        
        super(SampledData, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SampledData, self).elementProperties()
        js.extend([
            ("data", "data", str, False, None, False),
            ("_data", "_data", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dimensions", "dimensions", int, False, None, True),
            ("_dimensions", "_dimensions", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("_factor", "_factor", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lowerLimit", "lowerLimit", float, False, None, False),
            ("_lowerLimit", "_lowerLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("origin", "origin", quantity.Quantity, False, None, True),
            ("_origin", "_origin", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", float, False, None, True),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("upperLimit", "upperLimit", float, False, None, False),
            ("_upperLimit", "_upperLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import quantity