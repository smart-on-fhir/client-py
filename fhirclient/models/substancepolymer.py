# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SubstancePolymer).
# 2024, SMART Health IT.


from . import domainresource

class SubstancePolymer(domainresource.DomainResource):
    """ Todo.
    """
    
    resource_type = "SubstancePolymer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.class_fhir = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.copolymerConnectivity = None
        """ Todo.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.geometry = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.modification = None
        """ Todo.
        List of `str` items. """
        
        self.monomerSet = None
        """ Todo.
        List of `SubstancePolymerMonomerSet` items (represented as `dict` in JSON). """
        
        self.repeat = None
        """ Todo.
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
    """ Todo.
    """
    
    resource_type = "SubstancePolymerMonomerSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ratioType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.startingMaterial = None
        """ Todo.
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
    """ Todo.
    """
    
    resource_type = "SubstancePolymerMonomerSetStartingMaterial"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Todo.
        Type `SubstanceAmount` (represented as `dict` in JSON). """
        
        self.isDefining = None
        """ Todo.
        Type `bool`. """
        
        self.material = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.type = None
        """ Todo.
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
    """ Todo.
    """
    
    resource_type = "SubstancePolymerRepeat"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.averageMolecularFormula = None
        """ Todo.
        Type `str`. """
        
        self.numberOfUnits = None
        """ Todo.
        Type `int`. """
        
        self.repeatUnit = None
        """ Todo.
        List of `SubstancePolymerRepeatRepeatUnit` items (represented as `dict` in JSON). """
        
        self.repeatUnitAmountType = None
        """ Todo.
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
    """ Todo.
    """
    
    resource_type = "SubstancePolymerRepeatRepeatUnit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Todo.
        Type `SubstanceAmount` (represented as `dict` in JSON). """
        
        self.degreeOfPolymerisation = None
        """ Todo.
        List of `SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation` items (represented as `dict` in JSON). """
        
        self.orientationOfPolymerisation = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.repeatUnit = None
        """ Todo.
        Type `str`. """
        
        self.structuralRepresentation = None
        """ Todo.
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
    """ Todo.
    """
    
    resource_type = "SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Todo.
        Type `SubstanceAmount` (represented as `dict` in JSON). """
        
        self.degree = None
        """ Todo.
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
    """ Todo.
    """
    
    resource_type = "SubstancePolymerRepeatRepeatUnitStructuralRepresentation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.attachment = None
        """ Todo.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.representation = None
        """ Todo.
        Type `str`. """
        
        self.type = None
        """ Todo.
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


from . import attachment
from . import codeableconcept
from . import substanceamount
