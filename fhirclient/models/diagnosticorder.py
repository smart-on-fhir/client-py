#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (diagnosticorder.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class DiagnosticOrder(fhirresource.FHIRResource):
    """ A request for a diagnostic service.
    
    A request for a diagnostic investigation service to be performed.
    """
    
    resource_name = "DiagnosticOrder"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.clinicalNotes = None
        """ Explanation/Justification for test.
        Type `str`. """
        
        self.encounter = None
        """ The encounter that this diagnostic order is associated with.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.event = None
        """ A list of events of interest in the lifecycle.
        List of `DiagnosticOrderEvent` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.item = None
        """ The items the orderer requested.
        List of `DiagnosticOrderItem` items (represented as `dict` in JSON). """
        
        self.orderer = None
        """ Who ordered the test.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        self.specimen = None
        """ If the whole order relates to specific specimens.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | received | accepted | in progress | review | completed
        | suspended | rejected | failed.
        Type `str`. """
        
        self.subject = None
        """ Who and/or what test is about.
        Type `FHIRReference` referencing `Patient, Group, Location, Device` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Supporting observations or conditions for this request.
        List of `FHIRReference` items referencing `Observation, Condition` (represented as `dict` in JSON). """
        
        super(DiagnosticOrder, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticOrder, self).update_with_json(jsondict)
        if 'clinicalNotes' in jsondict:
            self.clinicalNotes = jsondict['clinicalNotes']
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'event' in jsondict:
            self.event = DiagnosticOrderEvent.with_json_and_owner(jsondict['event'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'item' in jsondict:
            self.item = DiagnosticOrderItem.with_json_and_owner(jsondict['item'], self)
        if 'orderer' in jsondict:
            self.orderer = fhirreference.FHIRReference.with_json_and_owner(jsondict['orderer'], self)
        if 'priority' in jsondict:
            self.priority = jsondict['priority']
        if 'specimen' in jsondict:
            self.specimen = fhirreference.FHIRReference.with_json_and_owner(jsondict['specimen'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'supportingInformation' in jsondict:
            self.supportingInformation = fhirreference.FHIRReference.with_json_and_owner(jsondict['supportingInformation'], self)


class DiagnosticOrderEvent(fhirelement.FHIRElement):
    """ A list of events of interest in the lifecycle.
    
    A summary of the events of interest that have occurred as the request is
    processed. E.g. when the order was made, various processing steps
    (specimens received), when it was completed.
    """
    
    resource_name = "DiagnosticOrderEvent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ Who recorded or did this.
        Type `FHIRReference` referencing `Practitioner, Device` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ The date at which the event happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ More information about the event and its context.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | received | accepted | in progress | review | completed
        | suspended | rejected | failed.
        Type `str`. """
        
        super(DiagnosticOrderEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticOrderEvent, self).update_with_json(jsondict)
        if 'actor' in jsondict:
            self.actor = fhirreference.FHIRReference.with_json_and_owner(jsondict['actor'], self)
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateTime'], self)
        if 'description' in jsondict:
            self.description = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['description'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']


class DiagnosticOrderItem(fhirelement.FHIRElement):
    """ The items the orderer requested.
    
    The specific diagnostic investigations that are requested as part of this
    request. Sometimes, there can only be one item per request, but in most
    contexts, more than one investigation can be requested.
    """
    
    resource_name = "DiagnosticOrderItem"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Location of requested test (if applicable).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.code = None
        """ Code to indicate the item (test or panel) being ordered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.event = None
        """ A list of events of interest in the lifecycle.
        List of `DiagnosticOrderEvent` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ If this item relates to specific specimens.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | received | accepted | in progress | review | completed
        | suspended | rejected | failed.
        Type `str`. """
        
        super(DiagnosticOrderItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticOrderItem, self).update_with_json(jsondict)
        if 'bodySite' in jsondict:
            self.bodySite = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['bodySite'], self)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'event' in jsondict:
            self.event = DiagnosticOrderEvent.with_json_and_owner(jsondict['event'], self)
        if 'specimen' in jsondict:
            self.specimen = fhirreference.FHIRReference.with_json_and_owner(jsondict['specimen'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']

