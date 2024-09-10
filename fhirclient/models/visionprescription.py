# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/VisionPrescription).
# 2024, SMART Health IT.


from . import domainresource

class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.
    
    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """
    
    resource_type = "VisionPrescription"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None
        """ Response creation date.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._created = None
        """ Primitive extension for created. Type `FHIRPrimitiveExtension` """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._dateWritten = None
        """ Primitive extension for dateWritten. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business Identifier for vision prescription.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.lensSpecification = None
        """ Vision lens authorization.
        List of `VisionPrescriptionLensSpecification` items (represented as `dict` in JSON). """
        self._lensSpecification = None
        """ Primitive extension for lensSpecification. Type `FHIRPrimitiveExtension` """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._patient = None
        """ Primitive extension for patient. Type `FHIRPrimitiveExtension` """
        
        self.prescriber = None
        """ Who authorized the vision prescription.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._prescriber = None
        """ Primitive extension for prescriber. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("created", "created", fhirdatetime.FHIRDateTime, False, None, True),
            ("_created", "_created", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("dateWritten", "dateWritten", fhirdatetime.FHIRDateTime, False, None, True),
            ("_dateWritten", "_dateWritten", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("lensSpecification", "lensSpecification", VisionPrescriptionLensSpecification, True, None, True),
            ("_lensSpecification", "_lensSpecification", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("_patient", "_patient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False, None, True),
            ("_prescriber", "_prescriber", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """ Vision lens authorization.
    
    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """
    
    resource_type = "VisionPrescriptionLensSpecification"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.add = None
        """ Added power for multifocal levels.
        Type `float`. """
        self._add = None
        """ Primitive extension for add. Type `FHIRPrimitiveExtension` """
        
        self.axis = None
        """ Lens meridian which contain no power for astigmatism.
        Type `int`. """
        self._axis = None
        """ Primitive extension for axis. Type `FHIRPrimitiveExtension` """
        
        self.backCurve = None
        """ Contact lens back curvature.
        Type `float`. """
        self._backCurve = None
        """ Primitive extension for backCurve. Type `FHIRPrimitiveExtension` """
        
        self.brand = None
        """ Brand required.
        Type `str`. """
        self._brand = None
        """ Primitive extension for brand. Type `FHIRPrimitiveExtension` """
        
        self.color = None
        """ Color required.
        Type `str`. """
        self._color = None
        """ Primitive extension for color. Type `FHIRPrimitiveExtension` """
        
        self.cylinder = None
        """ Lens power for astigmatism.
        Type `float`. """
        self._cylinder = None
        """ Primitive extension for cylinder. Type `FHIRPrimitiveExtension` """
        
        self.diameter = None
        """ Contact lens diameter.
        Type `float`. """
        self._diameter = None
        """ Primitive extension for diameter. Type `FHIRPrimitiveExtension` """
        
        self.duration = None
        """ Lens wear duration.
        Type `Quantity` (represented as `dict` in JSON). """
        self._duration = None
        """ Primitive extension for duration. Type `FHIRPrimitiveExtension` """
        
        self.eye = None
        """ right | left.
        Type `str`. """
        self._eye = None
        """ Primitive extension for eye. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Notes for coatings.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.power = None
        """ Contact lens power.
        Type `float`. """
        self._power = None
        """ Primitive extension for power. Type `FHIRPrimitiveExtension` """
        
        self.prism = None
        """ Eye alignment compensation.
        List of `VisionPrescriptionLensSpecificationPrism` items (represented as `dict` in JSON). """
        self._prism = None
        """ Primitive extension for prism. Type `FHIRPrimitiveExtension` """
        
        self.product = None
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._product = None
        """ Primitive extension for product. Type `FHIRPrimitiveExtension` """
        
        self.sphere = None
        """ Power of the lens.
        Type `float`. """
        self._sphere = None
        """ Primitive extension for sphere. Type `FHIRPrimitiveExtension` """
        
        super(VisionPrescriptionLensSpecification, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecification, self).elementProperties()
        js.extend([
            ("add", "add", float, False, None, False),
            ("_add", "_add", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("axis", "axis", int, False, None, False),
            ("_axis", "_axis", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("backCurve", "backCurve", float, False, None, False),
            ("_backCurve", "_backCurve", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("brand", "brand", str, False, None, False),
            ("_brand", "_brand", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("color", "color", str, False, None, False),
            ("_color", "_color", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("cylinder", "cylinder", float, False, None, False),
            ("_cylinder", "_cylinder", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("diameter", "diameter", float, False, None, False),
            ("_diameter", "_diameter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("duration", "duration", quantity.Quantity, False, None, False),
            ("_duration", "_duration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("eye", "eye", str, False, None, True),
            ("_eye", "_eye", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("power", "power", float, False, None, False),
            ("_power", "_power", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("prism", "prism", VisionPrescriptionLensSpecificationPrism, True, None, False),
            ("_prism", "_prism", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("product", "product", codeableconcept.CodeableConcept, False, None, True),
            ("_product", "_product", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sphere", "sphere", float, False, None, False),
            ("_sphere", "_sphere", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """ Eye alignment compensation.
    
    Allows for adjustment on two axis.
    """
    
    resource_type = "VisionPrescriptionLensSpecificationPrism"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.amount = None
        """ Amount of adjustment.
        Type `float`. """
        self._amount = None
        """ Primitive extension for amount. Type `FHIRPrimitiveExtension` """
        
        self.base = None
        """ up | down | in | out.
        Type `str`. """
        self._base = None
        """ Primitive extension for base. Type `FHIRPrimitiveExtension` """
        
        super(VisionPrescriptionLensSpecificationPrism, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecificationPrism, self).elementProperties()
        js.extend([
            ("amount", "amount", float, False, None, True),
            ("_amount", "_amount", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("base", "base", str, False, None, True),
            ("_base", "_base", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier
from . import quantity