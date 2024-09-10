# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Group).
# 2024, SMART Health IT.


from . import domainresource

class Group(domainresource.DomainResource):
    """ Group of multiple entities.
    
    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively, and are
    not formally or legally recognized; i.e. a collection of entities that
    isn't an Organization.
    """
    
    resource_type = "Group"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.active = None
        """ Whether this group's record is in active use.
        Type `bool`. """
        self._active = None
        """ Primitive extension for active. Type `FHIRPrimitiveExtension` """
        
        self.actual = None
        """ Descriptive or actual.
        Type `bool`. """
        self._actual = None
        """ Primitive extension for actual. Type `FHIRPrimitiveExtension` """
        
        self.characteristic = None
        """ Include / Exclude group members by Trait.
        List of `GroupCharacteristic` items (represented as `dict` in JSON). """
        self._characteristic = None
        """ Primitive extension for characteristic. Type `FHIRPrimitiveExtension` """
        
        self.code = None
        """ Kind of Group members.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique id.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.managingEntity = None
        """ Entity that is the custodian of the Group's definition.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._managingEntity = None
        """ Primitive extension for managingEntity. Type `FHIRPrimitiveExtension` """
        
        self.member = None
        """ Who or what is in group.
        List of `GroupMember` items (represented as `dict` in JSON). """
        self._member = None
        """ Primitive extension for member. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Label for Group.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.quantity = None
        """ Number of members.
        Type `int`. """
        self._quantity = None
        """ Primitive extension for quantity. Type `FHIRPrimitiveExtension` """
        
        self.type = None
        """ person | animal | practitioner | device | medication | substance.
        Type `str`. """
        self._type = None
        """ Primitive extension for type. Type `FHIRPrimitiveExtension` """
        
        super(Group, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend([
            ("active", "active", bool, False, None, False),
            ("_active", "_active", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("actual", "actual", bool, False, None, True),
            ("_actual", "_actual", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("characteristic", "characteristic", GroupCharacteristic, True, None, False),
            ("_characteristic", "_characteristic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("managingEntity", "managingEntity", fhirreference.FHIRReference, False, None, False),
            ("_managingEntity", "_managingEntity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("member", "member", GroupMember, True, None, False),
            ("_member", "_member", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("quantity", "quantity", int, False, None, False),
            ("_quantity", "_quantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("type", "type", str, False, None, True),
            ("_type", "_type", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class GroupCharacteristic(backboneelement.BackboneElement):
    """ Include / Exclude group members by Trait.
    
    Identifies traits whose presence r absence is shared by members of the
    group.
    """
    
    resource_type = "GroupCharacteristic"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Kind of characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.exclude = None
        """ Group includes or excludes.
        Type `bool`. """
        self._exclude = None
        """ Primitive extension for exclude. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Period over which characteristic is tested.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        self.valueBoolean = None
        """ Value held by characteristic.
        Type `bool`. """
        self._valueBoolean = None
        """ Primitive extension for valueBoolean. Type `FHIRPrimitiveExtension` """
        
        self.valueCodeableConcept = None
        """ Value held by characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._valueCodeableConcept = None
        """ Primitive extension for valueCodeableConcept. Type `FHIRPrimitiveExtension` """
        
        self.valueQuantity = None
        """ Value held by characteristic.
        Type `Quantity` (represented as `dict` in JSON). """
        self._valueQuantity = None
        """ Primitive extension for valueQuantity. Type `FHIRPrimitiveExtension` """
        
        self.valueRange = None
        """ Value held by characteristic.
        Type `Range` (represented as `dict` in JSON). """
        self._valueRange = None
        """ Primitive extension for valueRange. Type `FHIRPrimitiveExtension` """
        
        self.valueReference = None
        """ Value held by characteristic.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._valueReference = None
        """ Primitive extension for valueReference. Type `FHIRPrimitiveExtension` """
        
        super(GroupCharacteristic, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("exclude", "exclude", bool, False, None, True),
            ("_exclude", "_exclude", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueBoolean", "valueBoolean", bool, False, "value", True),
            ("_valueBoolean", "_valueBoolean", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False, "value", True),
            ("_valueCodeableConcept", "_valueCodeableConcept", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False, "value", True),
            ("_valueQuantity", "_valueQuantity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueRange", "valueRange", range.Range, False, "value", True),
            ("_valueRange", "_valueRange", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("valueReference", "valueReference", fhirreference.FHIRReference, False, "value", True),
            ("_valueReference", "_valueReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class GroupMember(backboneelement.BackboneElement):
    """ Who or what is in group.
    
    Identifies the resource instances that are members of the group.
    """
    
    resource_type = "GroupMember"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.entity = None
        """ Reference to the group member.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._entity = None
        """ Primitive extension for entity. Type `FHIRPrimitiveExtension` """
        
        self.inactive = None
        """ If member is no longer in group.
        Type `bool`. """
        self._inactive = None
        """ Primitive extension for inactive. Type `FHIRPrimitiveExtension` """
        
        self.period = None
        """ Period member belonged to the group.
        Type `Period` (represented as `dict` in JSON). """
        self._period = None
        """ Primitive extension for period. Type `FHIRPrimitiveExtension` """
        
        super(GroupMember, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(GroupMember, self).elementProperties()
        js.extend([
            ("entity", "entity", fhirreference.FHIRReference, False, None, True),
            ("_entity", "_entity", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("inactive", "inactive", bool, False, None, False),
            ("_inactive", "_inactive", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("_period", "_period", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range