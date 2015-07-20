#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Group) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity
from . import range


class Group(domainresource.DomainResource):
    """ Group of multiple entities.
    
    Represents a defined collection of entities that may be discussed or acted
    upon collectively but which are not expected to act collectively and are
    not formally or legally recognized.  I.e. A collection of entities that
    isn't an Organization.
    """
    
    resource_name = "Group"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actual = None
        """ Descriptive or actual.
        Type `bool`. """
        
        self.characteristic = None
        """ Trait of group members.
        List of `GroupCharacteristic` items (represented as `dict` in JSON). """
        
        self.code = None
        """ Kind of Group members.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique id.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.member = None
        """ Who or what is in group.
        List of `FHIRReference` items referencing `Patient, Practitioner, Device, Medication, Substance` (represented as `dict` in JSON). """
        
        self.name = None
        """ Label for Group.
        Type `str`. """
        
        self.quantity = None
        """ Number of members.
        Type `int`. """
        
        self.type = None
        """ person | animal | practitioner | device | medication | substance.
        Type `str`. """
        
        super(Group, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Group, self).elementProperties()
        js.extend([
            ("actual", "actual", bool, False),
            ("characteristic", "characteristic", GroupCharacteristic, True),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("member", "member", fhirreference.FHIRReference, True),
            ("name", "name", str, False),
            ("quantity", "quantity", int, False),
            ("type", "type", str, False),
        ])
        return js


class GroupCharacteristic(fhirelement.FHIRElement):
    """ Trait of group members.
    
    Identifies the traits shared by members of the group.
    """
    
    resource_name = "GroupCharacteristic"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Kind of characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.exclude = None
        """ Group includes or excludes.
        Type `bool`. """
        
        self.valueBoolean = None
        """ Value held by characteristic.
        Type `bool`. """
        
        self.valueCodeableConcept = None
        """ Value held by characteristic.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.valueQuantity = None
        """ Value held by characteristic.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.valueRange = None
        """ Value held by characteristic.
        Type `Range` (represented as `dict` in JSON). """
        
        super(GroupCharacteristic, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(GroupCharacteristic, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("exclude", "exclude", bool, False),
            ("valueBoolean", "valueBoolean", bool, False),
            ("valueCodeableConcept", "valueCodeableConcept", codeableconcept.CodeableConcept, False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, False),
            ("valueRange", "valueRange", range.Range, False),
        ])
        return js

