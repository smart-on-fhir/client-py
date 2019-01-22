#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/SubstancePolymer) on 2019-01-22.
#  2019, SMART Health IT.


from . import domainresource

class SubstancePolymer(domainresource.DomainResource):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstancePolymer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.class_fhir = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.copolymerConnectivity = None
        """ 
        T
        o
        d
        o
        .
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.geometry = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modification = None
        """ 
        T
        o
        d
        o
        .
        List of `str` items. """
        
        self.monomerSet = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstancePolymerMonomerSet` items (represented as `dict` in JSON). """
        
        self.repeat = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstancePolymerRepeat` items (represented as `dict` in JSON). """
        
        super(SubstancePolymer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymer, self).elementProperties()
        js.extend([
            ("class_fhir", "class", codeableconcept.CodeableConcept, False, None, False),
            ("copolymerConnectivity", "copolymerConnectivity", codeableconcept.CodeableConcept, True, None, False),
            ("geometry", "geometry", codeableconcept.CodeableConcept, False, None, False),
            ("modification", "modification", str, True, None, False),
            ("monomerSet", "monomerSet", SubstancePolymerMonomerSet, True, None, False),
            ("repeat", "repeat", SubstancePolymerRepeat, True, None, False),
        ])
        return js


from . import backboneelement

class SubstancePolymerMonomerSet(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstancePolymerMonomerSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ratioType = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startingMaterial = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstancePolymerMonomerSetStartingMaterial` items (represented as `dict` in JSON). """
        
        super(SubstancePolymerMonomerSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerMonomerSet, self).elementProperties()
        js.extend([
            ("ratioType", "ratioType", codeableconcept.CodeableConcept, False, None, False),
            ("startingMaterial", "startingMaterial", SubstancePolymerMonomerSetStartingMaterial, True, None, False),
        ])
        return js


class SubstancePolymerMonomerSetStartingMaterial(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstancePolymerMonomerSetStartingMaterial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        T
        o
        d
        o
        .
        Type `SubstanceAmount` (represented as `dict` in JSON). """
        
        self.isDefining = None
        """ 
        T
        o
        d
        o
        .
        Type `bool`. """
        
        self.material = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstancePolymerMonomerSetStartingMaterial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerMonomerSetStartingMaterial, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstancePolymerRepeat(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstancePolymerRepeat"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.averageMolecularFormula = None
        """ 
        T
        o
        d
        o
        .
        Type `str`. """
        
        self.numberOfUnits = None
        """ 
        T
        o
        d
        o
        .
        Type `int`. """
        
        self.repeatUnit = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstancePolymerRepeatRepeatUnit` items (represented as `dict` in JSON). """
        
        self.repeatUnitAmountType = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstancePolymerRepeat, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeat, self).elementProperties()
        js.extend([
            ("averageMolecularFormula", "averageMolecularFormula", str, False, None, False),
            ("numberOfUnits", "numberOfUnits", int, False, None, False),
            ("repeatUnit", "repeatUnit", SubstancePolymerRepeatRepeatUnit, True, None, False),
            ("repeatUnitAmountType", "repeatUnitAmountType", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstancePolymerRepeatRepeatUnit(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstancePolymerRepeatRepeatUnit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        T
        o
        d
        o
        .
        Type `SubstanceAmount` (represented as `dict` in JSON). """
        
        self.degreeOfPolymerisation = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation` items (represented as `dict` in JSON). """
        
        self.orientationOfPolymerisation = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.repeatUnit = None
        """ 
        T
        o
        d
        o
        .
        Type `str`. """
        
        self.structuralRepresentation = None
        """ 
        T
        o
        d
        o
        .
        List of `SubstancePolymerRepeatRepeatUnitStructuralRepresentation` items (represented as `dict` in JSON). """
        
        super(SubstancePolymerRepeatRepeatUnit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnit, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("degreeOfPolymerisation", "degreeOfPolymerisation", SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, True, None, False),
            ("orientationOfPolymerisation", "orientationOfPolymerisation", codeableconcept.CodeableConcept, False, None, False),
            ("repeatUnit", "repeatUnit", str, False, None, False),
            ("structuralRepresentation", "structuralRepresentation", SubstancePolymerRepeatRepeatUnitStructuralRepresentation, True, None, False),
        ])
        return js


class SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ 
        T
        o
        d
        o
        .
        Type `SubstanceAmount` (represented as `dict` in JSON). """
        
        self.degree = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("degree", "degree", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


class SubstancePolymerRepeatRepeatUnitStructuralRepresentation(backboneelement.BackboneElement):
    """ 
    T
    o
    d
    o
    .
    """
    
    resource_type = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment = None
        """ 
        T
        o
        d
        o
        .
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.representation = None
        """ 
        T
        o
        d
        o
        .
        Type `str`. """
        
        self.type = None
        """ 
        T
        o
        d
        o
        .
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SubstancePolymerRepeatRepeatUnitStructuralRepresentation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitStructuralRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


import sys
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import substanceamount
except ImportError:
    substanceamount = sys.modules[__package__ + '.substanceamount']
