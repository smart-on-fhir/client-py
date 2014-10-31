#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (diagnosticorder.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import encounter
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import narrative
import patient
import practitioner
import specimen


class DiagnosticOrder(fhirresource.FHIRResource):
    """ A request for a diagnostic service.
    
    Scope and Usage A Diagnostic Order is a record of a request for a set of
    diagnostic investigations to be performed. The investigation will lead to a
    Diagnostic Report that summarizes the outcome of the investigation, and
    includes any useful data and/or images that are relevant to the
    treatment/management of the subject.
    
    The principal intention of the Diagnostic Order is to support ordering
    diagnostic investigations on patients (which includes non-human patients in
    veterinary medicine). However in many contexts, healthcare related
    processes include performing diagnostic investigations on groups of
    subjects, devices involved in the provision of healthcare, and even
    environmental locations such as ducts, bodies of water, etc. The Diagnostic
    Order supports all these usages.
    
    The general work flow that this resource facilitates is that a clinical
    system creates a diagnostic order. The diagnostic order is then exchanged,
    perhaps via intermediaries, with a system that represents a diagnostic
    service that can perform the investigation as a request to do so. The
    diagnostic service will update the request as the work is performed, and
    then finally issue a report that references the requests that it fulfills.
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
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(DiagnosticOrder, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticOrder, self).update_with_json(jsondict)
        if 'clinicalNotes' in jsondict:
            self.clinicalNotes = jsondict['clinicalNotes']
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, encounter.Encounter)
        if 'event' in jsondict:
            self.event = DiagnosticOrderEvent.with_json(jsondict['event'])
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'item' in jsondict:
            self.item = DiagnosticOrderItem.with_json(jsondict['item'])
        if 'orderer' in jsondict:
            self.orderer = fhirreference.FHIRReference.with_json_and_owner(jsondict['orderer'], self, practitioner.Practitioner)
        if 'priority' in jsondict:
            self.priority = jsondict['priority']
        if 'specimen' in jsondict:
            self.specimen = fhirreference.FHIRReference.with_json_and_owner(jsondict['specimen'], self, specimen.Specimen)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self, patient.Patient)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])


class DiagnosticOrderEvent(fhirelement.FHIRElement):
    """ A list of events of interest in the lifecycle.
    
    A summary of the events of interest that have occurred as the request is
    processed. E.g. when the order was made, various processing steps
    (specimens received), when it was completed.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.actor = None
        """ Who recorded or did this.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.dateTime = None
        """ The date at which the event happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ More information about the event and it's context.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | received | accepted | in progress | review | completed
        | suspended | rejected | failed.
        Type `str`. """
        
        super(DiagnosticOrderEvent, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(DiagnosticOrderEvent, self).update_with_json(jsondict)
        if 'actor' in jsondict:
            self.actor = fhirreference.FHIRReference.with_json_and_owner(jsondict['actor'], self, practitioner.Practitioner)
        if 'dateTime' in jsondict:
            self.dateTime = fhirdate.FHIRDate.with_json(jsondict['dateTime'])
        if 'description' in jsondict:
            self.description = codeableconcept.CodeableConcept.with_json(jsondict['description'])
        if 'status' in jsondict:
            self.status = jsondict['status']


class DiagnosticOrderItem(fhirelement.FHIRElement):
    """ The items the orderer requested.
    
    The specific diagnostic investigations that are requested as part of this
    request. Sometimes, there can only be one item per request, but in most
    contexts, more than one investigation can be requested.
    """
    
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
        """ Events specific to this item.
        List of `DiagnosticOrderItemEvent` items (represented as `dict` in JSON). """
        
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
            self.bodySite = codeableconcept.CodeableConcept.with_json(jsondict['bodySite'])
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json(jsondict['code'])
        if 'event' in jsondict:
            self.event = DiagnosticOrderItemEvent.with_json(jsondict['event'])
        if 'specimen' in jsondict:
            self.specimen = fhirreference.FHIRReference.with_json_and_owner(jsondict['specimen'], self, specimen.Specimen)
        if 'status' in jsondict:
            self.status = jsondict['status']


class DiagnosticOrderItemEvent(fhirelement.FHIRElement):
    """ Events specific to this item.
    
    A summary of the events of interest that have occurred as this item of the
    request is processed.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        super(DiagnosticOrderItemEvent, self).__init__(jsondict)

