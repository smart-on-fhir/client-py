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
        self._class_fhir = None
        """ Primitive extension for class_fhir. Type `FHIRPrimitiveExtension` """
        
        self.copolymerConnectivity = None
        """ Todo.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._copolymerConnectivity = None
        """ Primitive extension for copolymerConnectivity. Type `FHIRPrimitiveExtension` """
        
        self.geometry = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._geometry = None
        """ Primitive extension for geometry. Type `FHIRPrimitiveExtension` """
        
        self.modification = None
        """ Todo.
        List of `str` items. """
        self._modification = None
        """ Primitive extension for modification. Type `FHIRPrimitiveExtension` """
        
        self.monomerSet = None
        """ Todo.
        List of `SubstancePolymerMonomerSet` items (represented as `dict` in JSON). """
        self._monomerSet = None
        """ Primitive extension for monomerSet. Type `FHIRPrimitiveExtension` """
        
        self.repeat = None
        """ Todo.
        List of `SubstancePolymerRepeat` items (represented as `dict` in JSON). """
        self._repeat = None
        """ Primitive extension for repeat. Type `FHIRPrimitiveExtension` """
        
        super(SubstancePolymer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymer, self).elementProperties()
        js.extend([
            ("class_fhir", "class", codeableconcept.CodeableConcept, False, None, False),
            ("_class_fhir", "_class_fhir", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("copolymerConnectivity", "copolymerConnectivity", codeableconcept.CodeableConcept, True, None, False),
            ("_copolymerConnectivity", "_copolymerConnectivity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("geometry", "geometry", codeableconcept.CodeableConcept, False, None, False),
            ("_geometry", "_geometry", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("modification", "modification", str, True, None, False),
            ("_modification", "_modification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("monomerSet", "monomerSet", SubstancePolymerMonomerSet, True, None, False),
            ("_monomerSet", "_monomerSet", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repeat", "repeat", SubstancePolymerRepeat, True, None, False),
            ("_repeat", "_repeat", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._ratioType = None
        """ Primitive extension for ratioType. Type `FHIRPrimitiveExtension` """
        
        self.startingMaterial = None
        """ Todo.
        List of `SubstancePolymerMonomerSetStartingMaterial` items (represented as `dict` in JSON). """
        self._startingMaterial = None
        """ Primitive extension for startingMaterial. Type `FHIRPrimitiveExtension` """
        
        super(SubstancePolymerMonomerSet, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerMonomerSet, self).elementProperties()
        js.extend([
            ("ratioType", "ratioType", codeableconcept.CodeableConcept, False, None, False),
            ("_ratioType", "_ratioType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("startingMaterial", "startingMaterial", SubstancePolymerMonomerSetStartingMaterial, True, None, False),
            ("_startingMaterial", "_startingMaterial", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.isDefining = None
        """ Todo.
        Type `bool`. """
        self._isDefining = None
        """ Primitive extension for isDefining. Type `FHIRPrimitiveExtension` """
        
        self.material = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._material = None
        """ Primitive extension for material. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstancePolymerMonomerSetStartingMaterial, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerMonomerSetStartingMaterial, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isDefining", "isDefining", bool, False, None, False),
            ("_isDefining", "_isDefining", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("_material", "_material", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._averageMolecularFormula = None
        """ Primitive extension for averageMolecularFormula. Type `FHIRPrimitiveExtension` """
        
        self.numberOfUnits = None
        """ Todo.
        Type `int`. """
        self._numberOfUnits = None
        """ Primitive extension for numberOfUnits. Type `FHIRPrimitiveExtension` """
        
        self.repeatUnit = None
        """ Todo.
        List of `SubstancePolymerRepeatRepeatUnit` items (represented as `dict` in JSON). """
        self._repeatUnit = None
        """ Primitive extension for repeatUnit. Type `FHIRPrimitiveExtension` """
        
        self.repeatUnitAmountType = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._repeatUnitAmountType = None
        """ Primitive extension for repeatUnitAmountType. Type `FHIRPrimitiveExtension` """
        
        super(SubstancePolymerRepeat, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeat, self).elementProperties()
        js.extend([
            ("averageMolecularFormula", "averageMolecularFormula", str, False, None, False),
            ("_averageMolecularFormula", "_averageMolecularFormula", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("numberOfUnits", "numberOfUnits", int, False, None, False),
            ("_numberOfUnits", "_numberOfUnits", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repeatUnit", "repeatUnit", SubstancePolymerRepeatRepeatUnit, True, None, False),
            ("_repeatUnit", "_repeatUnit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repeatUnitAmountType", "repeatUnitAmountType", codeableconcept.CodeableConcept, False, None, False),
            ("_repeatUnitAmountType", "_repeatUnitAmountType", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.degreeOfPolymerisation = None
        """ Todo.
        List of `SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation` items (represented as `dict` in JSON). """
        self._degreeOfPolymerisation = None
        """ Primitive extension for degreeOfPolymerisation. Type `FHIRPrimitiveExtension` """
        
        self.orientationOfPolymerisation = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._orientationOfPolymerisation = None
        """ Primitive extension for orientationOfPolymerisation. Type `FHIRPrimitiveExtension` """
        
        self.repeatUnit = None
        """ Todo.
        Type `str`. """
        self._repeatUnit = None
        """ Primitive extension for repeatUnit. Type `FHIRPrimitiveExtension` """
        
        self.structuralRepresentation = None
        """ Todo.
        List of `SubstancePolymerRepeatRepeatUnitStructuralRepresentation` items (represented as `dict` in JSON). """
        self._structuralRepresentation = None
        """ Primitive extension for structuralRepresentation. Type `FHIRPrimitiveExtension` """
        
        super(SubstancePolymerRepeatRepeatUnit, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnit, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("degreeOfPolymerisation", "degreeOfPolymerisation", SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, True, None, False),
            ("_degreeOfPolymerisation", "_degreeOfPolymerisation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("orientationOfPolymerisation", "orientationOfPolymerisation", codeableconcept.CodeableConcept, False, None, False),
            ("_orientationOfPolymerisation", "_orientationOfPolymerisation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("repeatUnit", "repeatUnit", str, False, None, False),
            ("_repeatUnit", "_repeatUnit", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("structuralRepresentation", "structuralRepresentation", SubstancePolymerRepeatRepeatUnitStructuralRepresentation, True, None, False),
            ("_structuralRepresentation", "_structuralRepresentation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.degree = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._degree = None
        """ Primitive extension for degree. Type `FHIRPrimitiveExtension` """
        
        super(SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitDegreeOfPolymerisation, self).elementProperties()
        js.extend([
            ("amount", "amount", substanceamount.SubstanceAmount, False, None, False),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("degree", "degree", codeableconcept.CodeableConcept, False, None, False),
            ("_degree", "_degree", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
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
        self._attachment = None
        """ Primitive extension for attachment. Type `FHIRPrimitiveExtension` """
        
        self.representation = None
        """ Todo.
        Type `str`. """
        self._representation = None
        """ Primitive extension for representation. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Todo.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SubstancePolymerRepeatRepeatUnitStructuralRepresentation, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SubstancePolymerRepeatRepeatUnitStructuralRepresentation, self).elementProperties()
        js.extend([
            ("attachment", "attachment", attachment.Attachment, False, None, False),
            ("_attachment", "_attachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("representation", "representation", str, False, None, False),
            ("_representation", "_representation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import attachment
from . import codeableconcept
from . import substanceamount