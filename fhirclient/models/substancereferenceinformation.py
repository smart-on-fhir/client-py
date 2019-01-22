#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class SubstanceReferenceInformation(domainresource.DomainResource):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstanceReferenceInformation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstanceReferenceInformationClassification` items (represented as `dict` in JSON). """
        
        self.comment = None
        """ 
        T
        o
        d
        o
        .
        Type `str`. """
        
        self.gene = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstanceReferenceInformationGene` items (represented as `dict` in JSON). """
        
        self.geneElement = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstanceReferenceInformationGeneElement` items (represented as `dict` in JSON). """
        
        self.target = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstanceReferenceInformationTarget` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformation, self).elementProperties()
        js.extend([
            ("classification", "classification", SubstanceReferenceInformationClassification, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("gene", "gene", SubstanceReferenceInformationGene, True, None, False),
            ("geneElement", "geneElement", SubstanceReferenceInformationGeneElement, True, None, False),
            ("target", "target", SubstanceReferenceInformationTarget, True, None, False),
        ])
        return js


from . import backboneelement

class SubstanceReferenceInformationClassification(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstanceReferenceInformationClassification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.classification = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.domain = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        T
        o
        d
        o
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.subtype = None
        """ 
        T
        o
        d
        o
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationClassification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationClassification, self).elementProperties()
        js.extend([
            ("classification", "classification", codeableconcept.CodeableConcept, False, None, False),
            ("domain", "domain", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("subtype", "subtype", codeableconcept.CodeableConcept, True, None, False),
        ])
        return js


class SubstanceReferenceInformationGene(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstanceReferenceInformationGene"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.gene = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.geneSequenceOrigin = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        T
        o
        d
        o
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationGene, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationGene, self).elementProperties()
        js.extend([
            ("gene", "gene", codeableconcept.CodeableConcept, False, None, False),
            ("geneSequenceOrigin", "geneSequenceOrigin", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
        ])
        return js


class SubstanceReferenceInformationGeneElement(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstanceReferenceInformationGeneElement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None
        """ 
        T
        o
        d
        o
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        T
        o
        d
        o
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationGeneElement, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationGeneElement, self).elementProperties()
        js.extend([
            ("element", "element", identifier.Identifier, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstanceReferenceInformationTarget(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstanceReferenceInformationTarget"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amountQuantity = None
        """ 
        T
        o
        d
        o
        .
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.amountRange = None
        """ 
        T
        o
        d
        o
        .
        Type `Range` (represented as `dict` in JSON). """
        
        self.amountString = None
        """ 
        T
        o
        d
        o
        .
        Type `str`. """
        
        self.amountType = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.interaction = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.organism = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.organismType = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ 
        T
        o
        d
        o
        .
        List of `FHIRReference` items (represented as `dict` in JSON). """
        
        self.target = None
        """ 
        T
        o
        d
        o
        .
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstanceReferenceInformationTarget, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstanceReferenceInformationTarget, self).elementProperties()
        js.extend([
            ("amountQuantity", "amountQuantity", quantity.Quantity, False, "amount", False),
            ("amountRange", "amountRange", range.Range, False, "amount", False),
            ("amountString", "amountString", str, False, "amount", False),
            ("amountType", "amountType", codeableconcept.CodeableConcept, False, None, False),
            ("interaction", "interaction", codeableconcept.CodeableConcept, False, None, False),
            ("organism", "organism", codeableconcept.CodeableConcept, False, None, False),
            ("organismType", "organismType", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, True, None, False),
            ("target", "target", identifier.Identifier, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + '.range']
