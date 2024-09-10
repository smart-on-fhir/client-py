# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/SpecimenDefinition).
# 2024, SMART Health IT.


from . import domainresource

class SpecimenDefinition(domainresource.DomainResource):
    """ Kind of specimen.
    
    A kind of specimen with associated set of requirements.
    """
    
    resource_type = "SpecimenDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.collection = None
        """ Specimen collection procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._collection = None
        """ Primitive extension for collection. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Business identifier of a kind of specimen.
        Type `Identifier` (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.patientPreparation = None
        """ Patient preparation for collection.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._patientPreparation = None
        """ Primitive extension for patientPreparation. Type `FHIRPrimitiveExtension` """
        
        self.timeAspect = None
        """ Time aspect for collection.
        Type `str`. """
        self._timeAspect = None
        """ Primitive extension for timeAspect. Type `FHIRPrimitiveExtension` """
        
        self.typeCollected = None
        """ Kind of material to collect.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._typeCollected = None
        """ Primitive extension for typeCollected. Type `FHIRPrimitiveExtension` """
        
        self.typeTested = None
        """ Specimen in container intended for testing by lab.
        List of `SpecimenDefinitionTypeTested` items (represented as `dict` in JSON). """
        self._typeTested = None
        """ Primitive extension for typeTested. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenDefinition, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinition, self).elementProperties()
        js.extend([
            ("collection", "collection", codeableconcept.CodeableConcept, True, None, False),
            ("_collection", "_collection", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("patientPreparation", "patientPreparation", codeableconcept.CodeableConcept, True, None, False),
            ("_patientPreparation", "_patientPreparation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("timeAspect", "timeAspect", str, False, None, False),
            ("_timeAspect", "_timeAspect", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("typeCollected", "typeCollected", codeableconcept.CodeableConcept, False, None, False),
            ("_typeCollected", "_typeCollected", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("typeTested", "typeTested", SpecimenDefinitionTypeTested, True, None, False),
            ("_typeTested", "_typeTested", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class SpecimenDefinitionTypeTested(backboneelement.BackboneElement):
    """ Specimen in container intended for testing by lab.
    
    Specimen conditioned in a container as expected by the testing laboratory.
    """
    
    resource_type = "SpecimenDefinitionTypeTested"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.container = None
        """ The specimen's container.
        Type `SpecimenDefinitionTypeTestedContainer` (represented as `dict` in JSON). """
        self._container = None
        """ Primitive extension for container. Type `FHIRPrimitiveExtension` """
        
        self.handling = None
        """ Specimen handling before testing.
        List of `SpecimenDefinitionTypeTestedHandling` items (represented as `dict` in JSON). """
        self._handling = None
        """ Primitive extension for handling. Type `FHIRPrimitiveExtension` """
        
        self.isDerived = None
        """ Primary or secondary specimen.
        Type `bool`. """
        self._isDerived = None
        """ Primitive extension for isDerived. Type `FHIRPrimitiveExtension` """
        
        self.preference = None
        """ preferred | alternate.
        Type `str`. """
        self._preference = None
        """ Primitive extension for preference. Type `FHIRPrimitiveExtension` """
        
        self.rejectionCriterion = None
        """ Rejection criterion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._rejectionCriterion = None
        """ Primitive extension for rejectionCriterion. Type `FHIRPrimitiveExtension` """
        
        self.requirement = None
        """ Specimen requirements.
        Type `str`. """
        self._requirement = None
        """ Primitive extension for requirement. Type `FHIRPrimitiveExtension` """
        
        self.retentionTime = None
        """ Specimen retention time.
        Type `Duration` (represented as `dict` in JSON). """
        self._retentionTime = None
        """ Primitive extension for retentionTime. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Type of intended specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenDefinitionTypeTested, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTested, self).elementProperties()
        js.extend([
            ("container", "container", SpecimenDefinitionTypeTestedContainer, False, None, False),
            ("_container", "_container", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("handling", "handling", SpecimenDefinitionTypeTestedHandling, True, None, False),
            ("_handling", "_handling", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("isDerived", "isDerived", bool, False, None, False),
            ("_isDerived", "_isDerived", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preference", "preference", str, False, None, True),
            ("_preference", "_preference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("rejectionCriterion", "rejectionCriterion", codeableconcept.CodeableConcept, True, None, False),
            ("_rejectionCriterion", "_rejectionCriterion", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("requirement", "requirement", str, False, None, False),
            ("_requirement", "_requirement", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("retentionTime", "retentionTime", duration.Duration, False, None, False),
            ("_retentionTime", "_retentionTime", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainer(backboneelement.BackboneElement):
    """ The specimen's container.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainer"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additive = None
        """ Additive associated with container.
        List of `SpecimenDefinitionTypeTestedContainerAdditive` items (represented as `dict` in JSON). """
        self._additive = None
        """ Primitive extension for additive. Type `FHIRPrimitiveExtension` """
        
        self.cap = None
        """ Color of container cap.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._cap = None
        """ Primitive extension for cap. Type `FHIRPrimitiveExtension` """
        
        self.capacity = None
        """ Container capacity.
        Type `Quantity` (represented as `dict` in JSON). """
        self._capacity = None
        """ Primitive extension for capacity. Type `FHIRPrimitiveExtension` """
        
        self.description = None
        """ Container description.
        Type `str`. """
        self._description = None
        """ Primitive extension for description. Type `FHIRPrimitiveExtension` """
        
        self.material = None
        """ Container material.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._material = None
        """ Primitive extension for material. Type `FHIRPrimitiveExtension` """
        
        self.minimumVolumeQuantity = None
        """ Minimum volume.
        Type `Quantity` (represented as `dict` in JSON). """
        self._minimumVolumeQuantity = None
        """ Primitive extension for minimumVolumeQuantity. Type `FHIRPrimitiveExtension` """
        
        self.minimumVolumeString = None
        """ Minimum volume.
        Type `str`. """
        self._minimumVolumeString = None
        """ Primitive extension for minimumVolumeString. Type `FHIRPrimitiveExtension` """
        
        self.preparation = None
        """ Specimen container preparation.
        Type `str`. """
        self._preparation = None
        """ Primitive extension for preparation. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ Kind of container associated with the kind of specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenDefinitionTypeTestedContainer, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainer, self).elementProperties()
        js.extend([
            ("additive", "additive", SpecimenDefinitionTypeTestedContainerAdditive, True, None, False),
            ("_additive", "_additive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("cap", "cap", codeableconcept.CodeableConcept, False, None, False),
            ("_cap", "_cap", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("capacity", "capacity", quantity.Quantity, False, None, False),
            ("_capacity", "_capacity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("description", "description", str, False, None, False),
            ("_description", "_description", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("material", "material", codeableconcept.CodeableConcept, False, None, False),
            ("_material", "_material", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minimumVolumeQuantity", "minimumVolumeQuantity", quantity.Quantity, False, "minimumVolume", False),
            ("_minimumVolumeQuantity", "_minimumVolumeQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("minimumVolumeString", "minimumVolumeString", str, False, "minimumVolume", False),
            ("_minimumVolumeString", "_minimumVolumeString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("preparation", "preparation", str, False, None, False),
            ("_preparation", "_preparation", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedContainerAdditive(backboneelement.BackboneElement):
    """ Additive associated with container.
    
    Substance introduced in the kind of container to preserve, maintain or
    enhance the specimen. Examples: Formalin, Citrate, EDTA.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedContainerAdditive"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._additiveCodeableConcept = None
        """ Primitive extension for additiveCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._additiveReference = None
        """ Primitive extension for additiveReference. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenDefinitionTypeTestedContainerAdditive, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedContainerAdditive, self).elementProperties()
        js.extend([
            ("additiveCodeableConcept", "additiveCodeableConcept", codeableconcept.CodeableConcept, False, "additive", True),
            ("_additiveCodeableConcept", "_additiveCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("additiveReference", "additiveReference", fhirreference.FHIRReference, False, "additive", True),
            ("_additiveReference", "_additiveReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class SpecimenDefinitionTypeTestedHandling(backboneelement.BackboneElement):
    """ Specimen handling before testing.
    
    Set of instructions for preservation/transport of the specimen at a defined
    temperature interval, prior the testing process.
    """
    
    resource_type = "SpecimenDefinitionTypeTestedHandling"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.instruction = None
        """ Preservation instruction.
        Type `str`. """
        self._instruction = None
        """ Primitive extension for instruction. Type `FHIRPrimitiveExtension` """
        
        self.maxDuration = None
        """ Maximum preservation time.
        Type `Duration` (represented as `dict` in JSON). """
        self._maxDuration = None
        """ Primitive extension for maxDuration. Type `FHIRPrimitiveExtension` """
        
        self.temperatureQualifier = None
        """ Temperature qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._temperatureQualifier = None
        """ Primitive extension for temperatureQualifier. Type `FHIRPrimitiveExtension` """
        
        self.temperatureRange = None
        """ Temperature range.
        Type `Range` (represented as `dict` in JSON). """
        self._temperatureRange = None
        """ Primitive extension for temperatureRange. Type `FHIRPrimitiveExtension` """
        
        super(SpecimenDefinitionTypeTestedHandling, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SpecimenDefinitionTypeTestedHandling, self).elementProperties()
        js.extend([
            ("instruction", "instruction", str, False, None, False),
            ("_instruction", "_instruction", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("maxDuration", "maxDuration", duration.Duration, False, None, False),
            ("_maxDuration", "_maxDuration", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("temperatureQualifier", "temperatureQualifier", codeableconcept.CodeableConcept, False, None, False),
            ("_temperatureQualifier", "_temperatureQualifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("temperatureRange", "temperatureRange", range.Range, False, None, False),
            ("_temperatureRange", "_temperatureRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import duration
from . import fhirreference
from . import identifier
from . import quantity
from . import range