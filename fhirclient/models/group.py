#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (group.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import quantity
import range


class Group(fhirresource.FHIRResource):
    """ Group of multiple entities.
    
    Scope and Usage Use Cases The group resource is used in one of two ways:
    
    * To define a group of specific people, animals, devices, etc. that is
    being tracked, examined or otherwise referenced as part of healthcare-
    related activities
    * To define a set of *possible* people, animals, devices, etc. that are of
    interest for some intended future healthcare-related activities
    Examples of the former could include group therapy or treatment sessions,
    exposed entities tracked as part of public health, etc. The latter might be
    used to define expected subjects for a clinical study.
    
    Both use cases are handled by a single resource because the data elements
    captured tend to be similar.
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
        """ Who is in group.
        List of `FHIRReference` items referencing `Patient` (represented as `dict` in JSON). """
        
        self.name = None
        """ Label for Group.
        Type `str`. """
        
        self.quantity = None
        """ Number of members.
        Type `int`. """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ person | animal | practitioner | device | medication | substance.
        Type `str`. """
        
        super(Group, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Group, self).update_with_json(jsondict)
        if 'actual' in jsondict:
            self.actual = jsondict['actual']
        if 'characteristic' in jsondict:
            self.characteristic = GroupCharacteristic.with_json(jsondict['characteristic'])
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'member' in jsondict:
            self.member = fhirreference.FHIRReference.with_json_and_owner(jsondict['member'], self, patient.Patient)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'quantity' in jsondict:
            self.quantity = jsondict['quantity']
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = jsondict['type']


class GroupCharacteristic(fhirelement.FHIRElement):
    """ Trait of group members.
    
    Identifies the traits shared by members of the group.
    """
    
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
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'exclude' in jsondict:
            self.exclude = jsondict['exclude']
        if 'valueBoolean' in jsondict:
            self.valueBoolean = jsondict['valueBoolean']
        if 'valueCodeableConcept' in jsondict:
            self.valueCodeableConcept = codeableconcept.CodeableConcept.with_json(jsondict['valueCodeableConcept'])
        if 'valueQuantity' in jsondict:
            self.valueQuantity = quantity.Quantity.with_json(jsondict['valueQuantity'])
        if 'valueRange' in jsondict:
            self.valueRange = range.Range.with_json(jsondict['valueRange'])

