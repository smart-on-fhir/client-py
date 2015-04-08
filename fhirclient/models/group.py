#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Group) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirelement
import fhirreference
import identifier
import quantity
import range


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
        
        self.actual = False
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
    
    def update_with_json(self, jsondict):
        super(Group, self).update_with_json(jsondict)
        if 'actual' in jsondict:
            self.actual = jsondict['actual']
        if 'characteristic' in jsondict:
            self.characteristic = GroupCharacteristic.with_json_and_owner(jsondict['characteristic'], self)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'member' in jsondict:
            self.member = fhirreference.FHIRReference.with_json_and_owner(jsondict['member'], self)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'quantity' in jsondict:
            self.quantity = jsondict['quantity']
        if 'type' in jsondict:
            self.type = jsondict['type']


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
        
        self.exclude = False
        """ Group includes or excludes.
        Type `bool`. """
        
        self.valueBoolean = False
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
    
    def update_with_json(self, jsondict):
        super(GroupCharacteristic, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'exclude' in jsondict:
            self.exclude = jsondict['exclude']
        if 'valueBoolean' in jsondict:
            self.valueBoolean = jsondict['valueBoolean']
        if 'valueCodeableConcept' in jsondict:
            self.valueCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['valueCodeableConcept'], self)
        if 'valueQuantity' in jsondict:
            self.valueQuantity = quantity.Quantity.with_json_and_owner(jsondict['valueQuantity'], self)
        if 'valueRange' in jsondict:
            self.valueRange = range.Range.with_json_and_owner(jsondict['valueRange'], self)

