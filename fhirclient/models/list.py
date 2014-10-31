#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (list.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner


class List(fhirresource.FHIRResource):
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
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'emptyReason' in jsondict:
            self.emptyReason = codeableconcept.CodeableConcept.with_json(jsondict['emptyReason'])
        if 'entry' in jsondict:
            self.entry = ListEntry.with_json(jsondict['entry'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'ordered' in jsondict:
            self.ordered = jsondict['ordered']
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self, practitioner.Practitioner)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class ListEntry(fhirelement.FHIRElement):
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
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'deleted' in jsondict:
            self.deleted = jsondict['deleted']
        if 'flag' in jsondict:
            self.flag = codeableconcept.CodeableConcept.with_json(jsondict['flag'])
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self, fhirresource.FHIRResource)

