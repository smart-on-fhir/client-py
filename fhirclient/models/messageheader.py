#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/MessageHeader) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.
    
    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    
    resource_name = "MessageHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("data", "data", fhirreference.FHIRReference, True, None, False),
            ("destination", "destination", MessageHeaderDestination, True, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("event", "event", coding.Coding, False, None, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, False, None, False),
            ("response", "response", MessageHeaderResponse, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("source", "source", MessageHeaderSource, False, None, True),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, True),
        ])
        return js


from . import backboneelement

class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message Destination Application(s).
    
    The destination application which the message is intended for.
    """
    
    resource_name = "MessageHeaderDestination"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.
    
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    
    resource_name = "MessageHeaderResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("details", "details", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", str, False, None, True),
        ])
        return js


class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message Source Application.
    
    The source application from which this message originated.
    """
    
    resource_name = "MessageHeaderSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("software", "software", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import fhirreference
