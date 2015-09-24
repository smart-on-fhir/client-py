#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/DiagnosticOrder) on 2015-09-24.
#  2015, SMART Health IT.


from . import annotation
from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier


class DiagnosticOrder(domainresource.DomainResource):
    """ A request for a diagnostic service.
    
    A record of a request for a diagnostic investigation service to be
    performed.
    """
    
    resource_name = "DiagnosticOrder"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
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
        
        self.note = None
        """ Other notes and comments.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.orderer = None
        """ Who ordered the test.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.priority = None
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        self.reason = None
        """ Explanation/Justification for test.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ If the whole order relates to specific specimens.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | draft | planned | requested | received | accepted | in-
        progress | review | completed | cancelled | suspended | rejected |
        failed.
        Type `str`. """
        
        self.subject = None
        """ Who and/or what test is about.
        Type `FHIRReference` referencing `Patient, Group, Location, Device` (represented as `dict` in JSON). """
        
        self.supportingInformation = None
        """ Additional clinical information.
        List of `FHIRReference` items referencing `Observation, Condition, DocumentReference` (represented as `dict` in JSON). """
        
        super(DiagnosticOrder, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DiagnosticOrder, self).elementProperties()
        js.extend([
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("event", "event", DiagnosticOrderEvent, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("item", "item", DiagnosticOrderItem, True),
            ("note", "note", annotation.Annotation, True),
            ("orderer", "orderer", fhirreference.FHIRReference, False),
            ("priority", "priority", str, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True),
            ("specimen", "specimen", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, True),
        ])
        return js


class DiagnosticOrderEvent(fhirelement.FHIRElement):
    """ A list of events of interest in the lifecycle.
    
    A summary of the events of interest that have occurred as the request is
    processed; e.g. when the order was made, various processing steps
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
        """ proposed | draft | planned | requested | received | accepted | in-
        progress | review | completed | cancelled | suspended | rejected |
        failed.
        Type `str`. """
        
        super(DiagnosticOrderEvent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DiagnosticOrderEvent, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False),
            ("description", "description", codeableconcept.CodeableConcept, False),
            ("status", "status", str, False),
        ])
        return js


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
        """ Events specific to this item.
        List of `DiagnosticOrderEvent` items (represented as `dict` in JSON). """
        
        self.specimen = None
        """ If this item relates to specific specimens.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | draft | planned | requested | received | accepted | in-
        progress | review | completed | cancelled | suspended | rejected |
        failed.
        Type `str`. """
        
        super(DiagnosticOrderItem, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DiagnosticOrderItem, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", codeableconcept.CodeableConcept, False),
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("event", "event", DiagnosticOrderEvent, True),
            ("specimen", "specimen", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
        ])
        return js

