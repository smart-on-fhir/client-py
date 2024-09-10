# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceAmount).
# 2024, SMART Health IT.


from . import backboneelement

class SubstanceAmount(backboneelement.BackboneElement):
    """ Chemical substances are a single substance type whose primary defining
    element is the molecular structure. Chemical substances shall be defined on
    the basis of their complete covalent molecular structure; the presence of a
    salt (counter-ion) and/or solvates (water, alcohols) is also captured.
    Purity, grade, physical form or particle size are not taken into account in
    the definition of a chemical substance or in the assignment of a Substance
    ID.
    """
    
    resource_type = "SubstanceAmount"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amountQuantity = None
        """ Primitive extension for amountQuantity. Type `FHIRPrimitiveExtension` """
        
        self.amountRange = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `Range` (represented as `dict` in JSON). """
        self._amountRange = None
        """ Primitive extension for amountRange. Type `FHIRPrimitiveExtension` """
        
        self.amountString = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `str`. """
        self._amountString = None
        """ Primitive extension for amountString. Type `FHIRPrimitiveExtension` """
        
        self.amountText = None
        """ A textual comment on a numeric value.
        Type `str`. """
        self._amountText = None
        """ Primitive extension for amountText. Type `FHIRPrimitiveExtension` """
        
        self.amountType = None
        """ Most elements that require a quantitative value will also have a
        field called amount type. Amount type should always be specified
        because the actual value of the amount is often dependent on it.
        EXAMPLE: In capturing the actual relative amounts of substances or
        molecular fragments it is essential to indicate whether the amount
        refers to a mole ratio or weight ratio. For any given element an
        effort should be made to use same the amount type for all related
        definitional elements.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._amountType = None
        """ Primitive extension for amountType. Type `FHIRPrimitiveExtension` """
        
        self.referenceRange = None
        """ Reference range of possible or expected values.
        Type `SubstanceAmountReferenceRange` (represented as `dict` in JSON). """
        self._referenceRange = None
        """ Primitive extension for referenceRange. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceAmount, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceAmount, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("_amountQuantity", "_amountQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("_amountRange", "_amountRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("_amountString", "_amountString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountText", "amountText", str, False, None, False),
            ("_amountText", "_amountText", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("_amountType", "_amountType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("referenceRange", "referenceRange", SubstanceAmountReferenceRange, False, None, False),
            ("_referenceRange", "_referenceRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import element

class SubstanceAmountReferenceRange(element.Element):
    """ Reference range of possible or expected values.
    """
    
    resource_type = "SubstanceAmountReferenceRange"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.highLimit = None
        """ Upper limit possible or expected.
        Type `Quantity` (represented as `dict` in JSON). """
        self._highLimit = None
        """ Primitive extension for highLimit. Type `FHIRPrimitiveExtension` """
        
        self.lowLimit = None
        """ Lower limit possible or expected.
        Type `Quantity` (represented as `dict` in JSON). """
        self._lowLimit = None
        """ Primitive extension for lowLimit. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceAmountReferenceRange, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceAmountReferenceRange, self).elementProperties()
        js.extend([
            ("highLimit", "highLimit", quantity.Quantity, False, None, False),
            ("_highLimit", "_highLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lowLimit", "lowLimit", quantity.Quantity, False, None, False),
            ("_lowLimit", "_lowLimit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import quantity
from . import range