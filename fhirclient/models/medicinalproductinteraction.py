# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction).
# 2024, SMART Health IT.


from . import domainresource

class MedicinalProductInteraction(domainresource.DomainResource):
    """ MedicinalProductInteraction.
    
    The interactions of the medicinal product with other medicinal products, or
    other forms of interactions.
    """
    
    resource_type = "MedicinalProductInteraction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None
        """ The interaction described.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.effect = None
        """ The effect of the interaction, for example "reduced gastric
        absorption of primary medication".
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._effect = None
        """ Primitive extension for effect. Type `FHIRPrimitiveExtension` """
        
        self.incidence = None
        """ The incidence of the interaction, e.g. theoretical, observed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._incidence = None
        """ Primitive extension for incidence. Type `FHIRPrimitiveExtension` """
        
        self.interactant = None
        """ The specific medication, food or laboratory test that interacts.
        List of `MedicinalProductInteractionInteractant` items (represented as `dict` in JSON). """
        self._interactant = None
        """ Primitive extension for interactant. Type `FHIRPrimitiveExtension` """
        
        self.management = None
        """ Actions for managing the interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._management = None
        """ Primitive extension for management. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ The medication for which this is a described interaction.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ The type of the interaction e.g. drug-drug interaction, drug-food
        interaction, drug-lab test interaction.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductInteraction, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductInteraction, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("effect", "effect", codeableconcept.CodeableConcept, False, None, False),
            ("_effect", "_effect", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("incidence", "incidence", codeableconcept.CodeableConcept, False, None, False),
            ("_incidence", "_incidence", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("interactant", "interactant", MedicinalProductInteractionInteractant, True, None, False),
            ("_interactant", "_interactant", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("management", "management", codeableconcept.CodeableConcept, False, None, False),
            ("_management", "_management", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, True, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MedicinalProductInteractionInteractant(backboneelement.BackboneElement):
    """ The specific medication, food or laboratory test that interacts.
    """
    
    resource_type = "MedicinalProductInteractionInteractant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.itemCodeableConcept = None
        """ The specific medication, food or laboratory test that interacts.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._itemCodeableConcept = None
        """ Primitive extension for itemCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.itemReference = None
        """ The specific medication, food or laboratory test that interacts.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._itemReference = None
        """ Primitive extension for itemReference. Type `FHIRPrimitiveExtension` """
        
        super(MedicinalProductInteractionInteractant, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MedicinalProductInteractionInteractant, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", True),
            ("_itemCodeableConcept", "_itemCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", True),
            ("_itemReference", "_itemReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference