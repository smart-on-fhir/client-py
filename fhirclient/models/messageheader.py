# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/MessageHeader).
# 2024, SMART Health IT.


from . import domainresource

class MessageHeader(domainresource.DomainResource):
    """ A resource that describes a message that is exchanged between systems.
    
    The header for a message exchange that is either requesting or responding
    to an action.  The reference(s) that are the subject of the action as well
    as other information related to the action are typically transmitted in a
    bundle in which the MessageHeader resource instance is the first resource
    in the bundle.
    """
    
    resource_type = "MessageHeader"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None
        """ The source of the decision.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._author = None
        """ Primitive extension for author. Type `FHIRPrimitiveExtension` """
        
        self.definition = None
        """ Link to the definition for this message.
        Type `str`. """
        self._definition = None
        """ Primitive extension for definition. Type `FHIRPrimitiveExtension` """
        
        self.destination = None
        """ Message destination application(s).
        List of `MessageHeaderDestination` items (represented as `dict` in JSON). """
        self._destination = None
        """ Primitive extension for destination. Type `FHIRPrimitiveExtension` """
        
        self.enterer = None
        """ The source of the data entry.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._enterer = None
        """ Primitive extension for enterer. Type `FHIRPrimitiveExtension` """
        
        self.eventCoding = None
        """ Code for the event this message represents or link to event
        definition.
        Type `Coding` (represented as `dict` in JSON). """
        self._eventCoding = None
        """ Primitive extension for eventCoding. Type `FHIRPrimitiveExtension` """
        
        self.eventUri = None
        """ Code for the event this message represents or link to event
        definition.
        Type `str`. """
        self._eventUri = None
        """ Primitive extension for eventUri. Type `FHIRPrimitiveExtension` """
        
        self.focus = None
        """ The actual content of the message.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._focus = None
        """ Primitive extension for focus. Type `FHIRPrimitiveExtension` """
        
        self.reason = None
        """ Cause of event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._reason = None
        """ Primitive extension for reason. Type `FHIRPrimitiveExtension` """
        
        self.response = None
        """ If this is a reply to prior message.
        Type `MessageHeaderResponse` (represented as `dict` in JSON). """
        self._response = None
        """ Primitive extension for response. Type `FHIRPrimitiveExtension` """
        
        self.responsible = None
        """ Final responsibility for event.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._responsible = None
        """ Primitive extension for responsible. Type `FHIRPrimitiveExtension` """
        
        self.sender = None
        """ Real world sender of the message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._sender = None
        """ Primitive extension for sender. Type `FHIRPrimitiveExtension` """
        
        self.source = None
        """ Message source application.
        Type `MessageHeaderSource` (represented as `dict` in JSON). """
        self._source = None
        """ Primitive extension for source. Type `FHIRPrimitiveExtension` """
        
        super(MessageHeader, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeader, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("_author", "_author", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("definition", "definition", str, False, None, False),
            ("_definition", "_definition", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("destination", "destination", MessageHeaderDestination, True, None, False),
            ("_destination", "_destination", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("enterer", "enterer", fhirreference.FHIRReference, False, None, False),
            ("_enterer", "_enterer", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("eventCoding", "eventCoding", coding.Coding, False, "event", True),
            ("_eventCoding", "_eventCoding", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("eventUri", "eventUri", str, False, "event", True),
            ("_eventUri", "_eventUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("focus", "focus", fhirreference.FHIRReference, True, None, False),
            ("_focus", "_focus", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, False, None, False),
            ("_reason", "_reason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("response", "response", MessageHeaderResponse, False, None, False),
            ("_response", "_response", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("responsible", "responsible", fhirreference.FHIRReference, False, None, False),
            ("_responsible", "_responsible", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("_sender", "_sender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("source", "source", MessageHeaderSource, False, None, True),
            ("_source", "_source", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class MessageHeaderDestination(backboneelement.BackboneElement):
    """ Message destination application(s).
    
    The destination application which the message is intended for.
    """
    
    resource_type = "MessageHeaderDestination"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.endpoint = None
        """ Actual destination address or id.
        Type `str`. """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name of system.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.receiver = None
        """ Intended "real-world" recipient for the data.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._receiver = None
        """ Primitive extension for receiver. Type `FHIRPrimitiveExtension` """
        
        self.target = None
        """ Particular delivery destination within the destination.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._target = None
        """ Primitive extension for target. Type `FHIRPrimitiveExtension` """
        
        super(MessageHeaderDestination, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderDestination, self).elementProperties()
        js.extend([
            ("endpoint", "endpoint", str, False, None, True),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, False, None, False),
            ("_receiver", "_receiver", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
            ("_target", "_target", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MessageHeaderResponse(backboneelement.BackboneElement):
    """ If this is a reply to prior message.
    
    Information about the message that this message is a response to.  Only
    present if this message is a response.
    """
    
    resource_type = "MessageHeaderResponse"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ ok | transient-error | fatal-error.
        Type `str`. """
        self._code = None
        """ Primitive extension for code. Type `FHIRPrimitiveExtension` """
        
        self.details = None
        """ Specific list of hints/warnings/errors.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._details = None
        """ Primitive extension for details. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Id of original message.
        Type `str`. """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        super(MessageHeaderResponse, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderResponse, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("_code", "_code", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("details", "details", fhirreference.FHIRReference, False, None, False),
            ("_details", "_details", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", str, False, None, True),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


class MessageHeaderSource(backboneelement.BackboneElement):
    """ Message source application.
    
    The source application from which this message originated.
    """
    
    resource_type = "MessageHeaderSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contact = None
        """ Human contact for problems.
        Type `ContactPoint` (represented as `dict` in JSON). """
        self._contact = None
        """ Primitive extension for contact. Type `FHIRPrimitiveExtension` """
        
        self.endpoint = None
        """ Actual message source address or id.
        Type `str`. """
        self._endpoint = None
        """ Primitive extension for endpoint. Type `FHIRPrimitiveExtension` """
        
        self.name = None
        """ Name of system.
        Type `str`. """
        self._name = None
        """ Primitive extension for name. Type `FHIRPrimitiveExtension` """
        
        self.software = None
        """ Name of software running the system.
        Type `str`. """
        self._software = None
        """ Primitive extension for software. Type `FHIRPrimitiveExtension` """
        
        self.version = None
        """ Version of software running.
        Type `str`. """
        self._version = None
        """ Primitive extension for version. Type `FHIRPrimitiveExtension` """
        
        super(MessageHeaderSource, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(MessageHeaderSource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactpoint.ContactPoint, False, None, False),
            ("_contact", "_contact", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("endpoint", "endpoint", str, False, None, True),
            ("_endpoint", "_endpoint", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("name", "name", str, False, None, False),
            ("_name", "_name", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("software", "software", str, False, None, False),
            ("_software", "_software", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("version", "version", str, False, None, False),
            ("_version", "_version", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirreference