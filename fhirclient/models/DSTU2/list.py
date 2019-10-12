#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/List) on 2019-10-12.
#  2019, SMART Health IT.


from . import domainresource

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
        
        self.encounter = None
        """ Context in which list created.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
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
        """ Comments about the list.
        Type `str`. """
        
        self.orderedBy = None
        """ What order the list has.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who and/or what defined the list contents (aka Author).
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
    
    def elementProperties(self):
        js = super(List, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("emptyReason", "emptyReason", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("entry", "entry", ListEntry, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("mode", "mode", str, False, None, True),
            ("note", "note", str, False, None, False),
            ("orderedBy", "orderedBy", codeableconcept.CodeableConcept, False, None, False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("title", "title", str, False, None, False),
        ])
        return js


from . import backboneelement

class ListEntry(backboneelement.BackboneElement):
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
        
        self.deleted = None
        """ If this item is actually marked as deleted.
        Type `bool`. """
        
        self.flag = None
        """ Status/Workflow information about this item.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.item = None
        """ Actual entry.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        super(ListEntry, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ListEntry, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deleted", "deleted", bool, False, None, False),
            ("flag", "flag", codeableconcept.CodeableConcept, False, None, False),
            ("item", "item", fhirreference.FHIRReference, False, None, True),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
