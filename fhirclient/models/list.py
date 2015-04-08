#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/List) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class List(domainresource.DomainResource):
    """ Information summarized from a list of other resources.
    
    A set of information summarized from a list of other resources.
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
        
        self.note = None
        """ Comments about the note.
        Type `str`. """
        
        self.orderedBy = None
        """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who and/or what defined the list contents.
        Type `FHIRReference` referencing `Practitioner, Patient, Device` (represented as `dict` in JSON). """
        
        self.status = None
        """ current | retired | entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ If all resources have the same subject.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        self.title = None
        """ Descriptive name for the list.
        Type `str`. """
        
        super(List, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(List, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'emptyReason' in jsondict:
            self.emptyReason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['emptyReason'], self)
        if 'entry' in jsondict:
            self.entry = ListEntry.with_json_and_owner(jsondict['entry'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'mode' in jsondict:
            self.mode = jsondict['mode']
        if 'note' in jsondict:
            self.note = jsondict['note']
        if 'orderedBy' in jsondict:
            self.orderedBy = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['orderedBy'], self)
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'title' in jsondict:
            self.title = jsondict['title']


class ListEntry(fhirelement.FHIRElement):
    """ Entries in the list.
    
    Entries in this list.
    """
    
    resource_name = "ListEntry"
    
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
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(ListEntry, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ListEntry, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'deleted' in jsondict:
            self.deleted = jsondict['deleted']
        if 'flag' in jsondict:
            self.flag = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['flag'], self)
        if 'item' in jsondict:
            self.item = fhirreference.FHIRReference.with_json_and_owner(jsondict['item'], self)

