# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/ProductShelfLife).
# 2024, SMART Health IT.


from . import backboneelement

class ProductShelfLife(backboneelement.BackboneElement):
    """ The shelf-life and storage information for a medicinal product item or
    container can be described using this class.
    """
    
    resource_type = "ProductShelfLife"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None
        """ Unique identifier for the packaged Medicinal Product.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.period = None
        """ The shelf life time period can be specified using a numerical value
        for the period of time and its unit of time measurement The unit of
        measurement shall be specified in accordance with ISO 11240 and the
        resulting terminology The symbol and the symbol identifier shall be
        used.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.specialPrecautionsForStorage = None
        """ Special precautions for storage, if any, can be specified using an
        appropriate controlled vocabulary The controlled term and the
        controlled term identifier shall be specified.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None
        """ This describes the shelf life, taking into account various
        scenarios such as shelf life of the packaged Medicinal Product
        itself, shelf life after transformation where necessary and shelf
        life after the first opening of a bottle, etc. The shelf life type
        shall be specified using an appropriate controlled vocabulary The
        controlled term and the controlled term identifier shall be
        specified.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProductShelfLife, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(ProductShelfLife, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("period", "period", quantity.Quantity, False, None, True),
            ("specialPrecautionsForStorage", "specialPrecautionsForStorage", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import codeableconcept
from . import identifier
from . import quantity
