#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (list.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import CodeableConcept
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Narrative
import Patient
import Practitioner


class List(FHIRResource.FHIRResource):
    """ Information summarized from a list of other resources.
    
    Scope and Usage List resources are used in many places, including
    allergies, medications, alerts, medical history, etc.
    """
    
    resource_name = "List"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ What the purpose of this list is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the list was prepared.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.emptyReason = None
        """ Why list is empty.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.entry = None
        """ Entries in the list.
        List of `ListEntry` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.mode = None
        """ working | snapshot | changes.
        Type `str`. """
        
        self.ordered = False
        """ Whether items in the list have a meaningful order.
        Type `bool`. """
        
        self.source = None
        """ Who and/or what defined the list contents.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.subject = None
        """ If all resources have the same subject.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(List, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(List, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = CodeableConcept.CodeableConcept.with_json(jsondict['code'])
        if 'date' in jsondict:
            self.date = FHIRDate.FHIRDate.with_json(jsondict['date'])
        if 'emptyReason' in jsondict:
            self.emptyReason = CodeableConcept.CodeableConcept.with_json(jsondict['emptyReason'])
        if 'entry' in jsondict:
            self.entry = ListEntry.with_json(jsondict['entry'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'ordered' in jsondict:
            self.ordered = jsondict['ordered']
        if 'source' in jsondict:
            self.source = FHIRReference.FHIRReference.with_json_and_owner(jsondict['source'], self, Practitioner.Practitioner)
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])


class ListEntry(FHIRElement.FHIRElement):
    """ Entries in the list.
    
    Entries in this list.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ When item added to list.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deleted = False
        """ If this item is actually marked as deleted.
        Type `bool`. """
        
        self.flag = None
        """ Workflow information about this item.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.item = None
        """ Actual entry.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        super(ListEntry, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ListEntry, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = FHIRDate.FHIRDate.with_json(jsondict['date'])
        if 'deleted' in jsondict:
            self.deleted = jsondict['deleted']
        if 'flag' in jsondict:
            self.flag = CodeableConcept.CodeableConcept.with_json(jsondict['flag'])
        if 'item' in jsondict:
            self.item = FHIRReference.FHIRReference.with_json_and_owner(jsondict['item'], self, FHIRResource.FHIRResource)

