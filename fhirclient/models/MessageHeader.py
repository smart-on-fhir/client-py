#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (messageheader.profile.json) on 2014-10-17.
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
import Coding
import Contact
import Device
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Narrative
import OperationOutcome
import Practitioner


class MessageHeader(FHIRResource.FHIRResource):
    """ A resource that describes a message that is exchanged between systems.
    
    Scope and Usage The MessageHeader resource is defined in order to support
    Messaging using FHIR resources. The principle usage of the MessageHeader
    resource is when messages are exchanged. However, as a resource that can be
    used with the RESTful framework, the MessageHeader resource has the normal
    resource end-point ([base-url]/Message), which is used to manage a set of
    static messages resources. This could be used to make an archive of past
    messages available. Creating or updating Message resources in this fashion
    does not represent the actual occurrence of any event, nor can it trigger
    any logic associated with the actual event. It is just for managing a set
    of message resources.
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
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
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
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.response = None
        """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
        
        self.responsible = None
        """ Final responsibility for event.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.source = None
        """ Message Source Application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.timestamp = None
        """ Time that the message was sent.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(MessageHeader, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(MessageHeader, self).update_with_json(jsondict)
        if 'author' in jsondict:
            self.author = FHIRReference.FHIRReference.with_json_and_owner(jsondict['author'], self, Practitioner.Practitioner)
        if 'data' in jsondict:
            self.data = FHIRReference.FHIRReference.with_json_and_owner(jsondict['data'], self, FHIRResource.FHIRResource)
        if 'destination' in jsondict:
            self.destination = MessageHeaderDestination.with_json(jsondict['destination'])
        if 'enterer' in jsondict:
            self.enterer = FHIRReference.FHIRReference.with_json_and_owner(jsondict['enterer'], self, Practitioner.Practitioner)
        if 'event' in jsondict:
            self.event = Coding.Coding.with_json(jsondict['event'])
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']
        if 'reason' in jsondict:
            self.reason = CodeableConcept.CodeableConcept.with_json(jsondict['reason'])
        if 'receiver' in jsondict:
            self.receiver = FHIRReference.FHIRReference.with_json_and_owner(jsondict['receiver'], self, Practitioner.Practitioner)
        if 'response' in jsondict:
            self.response = MessageHeaderResponse.with_json(jsondict['response'])
        if 'responsible' in jsondict:
            self.responsible = FHIRReference.FHIRReference.with_json_and_owner(jsondict['responsible'], self, Practitioner.Practitioner)
        if 'source' in jsondict:
            self.source = MessageHeaderSource.with_json(jsondict['source'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'timestamp' in jsondict:
            self.timestamp = FHIRDate.FHIRDate.with_json(jsondict['timestamp'])


class MessageHeaderResponse(FHIRElement.FHIRElement):
    """ If this is a reply to prior message.
    
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    
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
            self.details = FHIRReference.FHIRReference.with_json_and_owner(jsondict['details'], self, OperationOutcome.OperationOutcome)
        if 'identifier' in jsondict:
            self.identifier = jsondict['identifier']


class MessageHeaderSource(FHIRElement.FHIRElement):
    """ Message Source Application.
    
    The source application from which this message originated.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contact = None
        """ Human contact for problems.
        Type `Contact` (represented as `dict` in JSON). """
        
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
            self.contact = Contact.Contact.with_json(jsondict['contact'])
        if 'endpoint' in jsondict:
            self.endpoint = jsondict['endpoint']
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'software' in jsondict:
            self.software = jsondict['software']
        if 'version' in jsondict:
            self.version = jsondict['version']


class MessageHeaderDestination(FHIRElement.FHIRElement):
    """ Message Destination Application(s).
    
    The destination application which the message is intended for.
    """
    
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
            self.target = FHIRReference.FHIRReference.with_json_and_owner(jsondict['target'], self, Device.Device)

