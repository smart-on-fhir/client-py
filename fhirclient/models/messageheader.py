#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import coding
import contactpoint
import domainresource
import fhirdate
import fhirelement
import fhirreference


class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.
    
    The header for a message exchange that is either requesting or responding
    to an action.  The Reference(s) that are the subject of the action as well
    as other Information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    
    resource_name = "MessageHeader"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ The source of the decision.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.data = None
        """ The actual content of the message.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.destination = None
        """ Message Destination Application(s).
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """
        
        self.enterer = None
        """ The source of the data entry.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.event = None
        """ Code for the event this message represents.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Id of this message.
        Type `str`. """
        
        self.reason = None
        """ Cause of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ Intended "real-world" recipient for the data.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.response = None
        """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Final responsibility for event.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.source = None
        """ Message Source Application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
        
        self.timestamp = None
        """ Time that the message was sent.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(MessageHeader, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MessageHeader, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = fhirreference.FHIRReference.with_json_and_owner(jsondict['author'], self)
        if 'data' in jsondict:
            self.data = fhirreference.FHIRReference.with_json_and_owner(jsondict['data'], self)
        if 'destination' in jsondict:
            self.destination = MessageHeaderDestination.with_json_and_owner(jsondict['destination'], self)
        if 'enterer' in jsondict:
            self.enterer = fhirreference.FHIRReference.with_json_and_owner(jsondict['enterer'], self)
        if 'event' in jsondict:
            self.event = coding.Coding.with_json_and_owner(jsondict['event'], self)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'receiver' in jsondict:
            self.receiver = fhirreference.FHIRReference.with_json_and_owner(jsondict['receiver'], self)
        if 'response' in jsondict:
            self.response = MessageHeaderResponse.with_json_and_owner(jsondict['response'], self)
        if 'responsible' in jsondict:
            self.responsible = fhirreference.FHIRReference.with_json_and_owner(jsondict['responsible'], self)
        if 'source' in jsondict:
            self.source = MessageHeaderSource.with_json_and_owner(jsondict['source'], self)
        if 'timestamp' in jsondict:
            self.timestamp = fhirdate.FHIRDate.with_json_and_owner(jsondict['timestamp'], self)


class MessageHeaderDestination(fhirelement.FHIRElement):
    """ Message Destination Application(s).
    
    The destination application which the message is intended for.
    """
    
    resource_name = "MessageHeaderDestination"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.endpoint = None
        """ Actual destination address or id.
        Type `str`. """
        
        self.name = None
        """ Name of system.
        Type `str`. """
        
        self.target = None
        """ Particular delivery destination within the destination.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        super(MessageHeaderDestination, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MessageHeaderDestination, self).update_with_json(jsondict)
        if 'endpoint' in jsondict:
            self.endpoint = jsondict['endpoint']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)


class MessageHeaderResponse(fhirelement.FHIRElement):
    """ If this is a reply to prior message.
    
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    
    resource_name = "MessageHeaderResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ ok | transient-error | fatal-error.
        Type `str`. """
        
        self.details = None
        """ Specific list of hints/warnings/errors.
        Type `FHIRReference` referencing `OperationOutcome` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Id of original message.
        Type `str`. """
        
        super(MessageHeaderResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MessageHeaderResponse, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'details' in jsondict:
            self.details = fhirreference.FHIRReference.with_json_and_owner(jsondict['details'], self)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']


class MessageHeaderSource(fhirelement.FHIRElement):
    """ Message Source Application.
    
    The source application from which this message originated.
    """
    
    resource_name = "MessageHeaderSource"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contact = None
        """ Human contact for problems.
        Type `ContactPoint` (represented as `dict` in JSON). """
        
        self.endpoint = None
        """ Actual message source address or id.
        Type `str`. """
        
        self.name = None
        """ Name of system.
        Type `str`. """
        
        self.software = None
        """ Name of software running the system.
        Type `str`. """
        
        self.version = None
        """ Version of software running.
        Type `str`. """
        
        super(MessageHeaderSource, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MessageHeaderSource, self).update_with_json(jsondict)
        if 'contact' in jsondict:
            self.contact = contactpoint.ContactPoint.with_json_and_owner(jsondict['contact'], self)
        if 'endpoint' in jsondict:
            self.endpoint = jsondict['endpoint']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'software' in jsondict:
            self.software = jsondict['software']
        if 'version' in jsondict:
            self.version = jsondict['version']

