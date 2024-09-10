# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation).
# 2024, SMART Health IT.


from . import domainresource

class SubstanceReferenceInformation(domainresource.DomainResource):
    """ Todo.
    """
    
    resource_type = "SubstanceReferenceInformation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ Todo.
        List of `SubstanceReferenceInformationClassification` items (represented as `dict` in JSON). """
        self._classification = None
        """ Primitive extension for classification. Type `FHIRPrimitiveExtension` """
        
        self.comment = None
        """ Todo.
        Type `str`. """
        self._comment = None
        """ Primitive extension for comment. Type `FHIRPrimitiveExtension` """
        
        self.gene = None
        """ Todo.
        List of `SubstanceReferenceInformationGene` items (represented as `dict` in JSON). """
        self._gene = None
        """ Primitive extension for gene. Type `FHIRPrimitiveExtension` """
        
        self.geneElement = None
        """ Todo.
        List of `SubstanceReferenceInformationGeneElement` items (represented as `dict` in JSON). """
        self._geneElement = None
        """ Primitive extension for geneElement. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Todo.
        List of `SubstanceReferenceInformationTarget` items (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceReferenceInformation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformation, self).elementProperties()
        js.extend([
            ("classification", "classification", SubstanceReferenceInformationClassification, True, None, False),
            ("_classification", "_classification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("comment", "comment", str, False, None, False),
            ("_comment", "_comment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("gene", "gene", SubstanceReferenceInformationGene, True, None, False),
            ("_gene", "_gene", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("geneElement", "geneElement", SubstanceReferenceInformationGeneElement, True, None, False),
            ("_geneElement", "_geneElement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", SubstanceReferenceInformationTarget, True, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SubstanceReferenceInformationClassification(backboneelement.BackboneElement):
    """ Todo.
    """
    
    resource_type = "SubstanceReferenceInformationClassification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._classification = None
        """ Primitive extension for classification. Type `FHIRPrimitiveExtension` """
        
        self.domain = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._domain = None
        """ Primitive extension for domain. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.subtype = None
        """ Todo.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._subtype = None
        """ Primitive extension for subtype. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceReferenceInformationClassification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("_classification", "_classification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("_domain", "_domain", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False),
            ("_subtype", "_subtype", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """ Todo.
    """
    
    resource_type = "SubstanceReferenceInformationGene"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.gene = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._gene = None
        """ Primitive extension for gene. Type `FHIRPrimitiveExtension` """
        
        self.geneSequenceOrigin = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._geneSequenceOrigin = None
        """ Primitive extension for geneSequenceOrigin. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceReferenceInformationGene, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationGene, self).elementProperties()
        js.extend([
            ("gene", "gene", codeableconcept.CodeableConcept, False, None, False),
            ("_gene", "_gene", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("geneSequenceOrigin", "geneSequenceOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("_geneSequenceOrigin", "_geneSequenceOrigin", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """ Todo.
    """
    
    resource_type = "SubstanceReferenceInformationGeneElement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ Todo.
        Type `Identifier` (represented as `dict` in JSON). """
        self._element = None
        """ Primitive extension for element. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceReferenceInformationGeneElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationGeneElement, self).elementProperties()
        js.extend([
            ("element", "element", identifier.Identifier, False, None, False),
            ("_element", "_element", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """ Todo.
    """
    
    resource_type = "SubstanceReferenceInformationTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ Todo.
        Type `Quantity` (represented as `dict` in JSON). """
        self._amountQuantity = None
        """ Primitive extension for amountQuantity. Type `FHIRPrimitiveExtension` """
        
        self.amountRange = None
        """ Todo.
        Type `Range` (represented as `dict` in JSON). """
        self._amountRange = None
        """ Primitive extension for amountRange. Type `FHIRPrimitiveExtension` """
        
        self.amountString = None
        """ Todo.
        Type `str`. """
        self._amountString = None
        """ Primitive extension for amountString. Type `FHIRPrimitiveExtension` """
        
        self.amountType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._amountType = None
        """ Primitive extension for amountType. Type `FHIRPrimitiveExtension` """
        
        self.interaction = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._interaction = None
        """ Primitive extension for interaction. Type `FHIRPrimitiveExtension` """
        
        self.organism = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._organism = None
        """ Primitive extension for organism. Type `FHIRPrimitiveExtension` """
        
        self.organismType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._organismType = None
        """ Primitive extension for organismType. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Todo.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Todo.
        Type `Identifier` (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstanceReferenceInformationTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationTarget, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("_amountQuantity", "_amountQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("_amountRange", "_amountRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountString", "amountString", str, False, "amount", False),
            ("_amountString", "_amountString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("_amountType", "_amountType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("interaction", "interaction", codeableconcept.CodeableConcept, False, None, False),
            ("_interaction", "_interaction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("organism", "organism", codeableconcept.CodeableConcept, False, None, False),
            ("_organism", "_organism", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("organismType", "organismType", codeableconcept.CodeableConcept, False, None, False),
            ("_organismType", "_organismType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", identifier.Identifier, False, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import quantity
from . import range