# Generated from FHIR 4.0.1-9346c8cc45 (http://hl7.org/fhir/StructureDefinition/Communication).
# 2024, SMART Health IT.


from . import domainresource

class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.
    
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency that was notified about a
    reportable condition.
    """
    
    resource_type = "Communication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.about = None
        """ Resources that pertain to this communication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._about = None
        """ Primitive extension for about. Type `FHIRPrimitiveExtension` """
        
        self.basedOn = None
        """ Request fulfilled by this communication.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._basedOn = None
        """ Primitive extension for basedOn. Type `FHIRPrimitiveExtension` """
        
        self.category = None
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._category = None
        """ Primitive extension for category. Type `FHIRPrimitiveExtension` """
        
        self.encounter = None
        """ Encounter created as part of.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._encounter = None
        """ Primitive extension for encounter. Type `FHIRPrimitiveExtension` """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        self._identifier = None
        """ Primitive extension for identifier. Type `FHIRPrimitiveExtension` """
        
        self.inResponseTo = None
        """ Reply to.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._inResponseTo = None
        """ Primitive extension for inResponseTo. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items. """
        self._instantiatesCanonical = None
        """ Primitive extension for instantiatesCanonical. Type `FHIRPrimitiveExtension` """
        
        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """
        self._instantiatesUri = None
        """ Primitive extension for instantiatesUri. Type `FHIRPrimitiveExtension` """
        
        self.medium = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._medium = None
        """ Primitive extension for medium. Type `FHIRPrimitiveExtension` """
        
        self.note = None
        """ Comments made about the communication.
        List of `Annotation` items (represented as `dict` in JSON). """
        self._note = None
        """ Primitive extension for note. Type `FHIRPrimitiveExtension` """
        
        self.partOf = None
        """ Part of this action.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._partOf = None
        """ Primitive extension for partOf. Type `FHIRPrimitiveExtension` """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationPayload` items (represented as `dict` in JSON). """
        self._payload = None
        """ Primitive extension for payload. Type `FHIRPrimitiveExtension` """
        
        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """
        self._priority = None
        """ Primitive extension for priority. Type `FHIRPrimitiveExtension` """
        
        self.reasonCode = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        self._reasonCode = None
        """ Primitive extension for reasonCode. Type `FHIRPrimitiveExtension` """
        
        self.reasonReference = None
        """ Why was communication done?.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._reasonReference = None
        """ Primitive extension for reasonReference. Type `FHIRPrimitiveExtension` """
        
        self.received = None
        """ When received.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._received = None
        """ Primitive extension for received. Type `FHIRPrimitiveExtension` """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items (represented as `dict` in JSON). """
        self._recipient = None
        """ Primitive extension for recipient. Type `FHIRPrimitiveExtension` """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._sender = None
        """ Primitive extension for sender. Type `FHIRPrimitiveExtension` """
        
        self.sent = None
        """ When sent.
        Type `FHIRDateTime` (represented as `str` in JSON). """
        self._sent = None
        """ Primitive extension for sent. Type `FHIRPrimitiveExtension` """
        
        self.status = None
        """ preparation | in-progress | not-done | on-hold | stopped |
        completed | entered-in-error | unknown.
        Type `str`. """
        self._status = None
        """ Primitive extension for status. Type `FHIRPrimitiveExtension` """
        
        self.statusReason = None
        """ Reason for current status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._statusReason = None
        """ Primitive extension for statusReason. Type `FHIRPrimitiveExtension` """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._subject = None
        """ Primitive extension for subject. Type `FHIRPrimitiveExtension` """
        
        self.topic = None
        """ Description of the purpose/content.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        self._topic = None
        """ Primitive extension for topic. Type `FHIRPrimitiveExtension` """
        
        super(Communication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Communication, self).elementProperties()
        js.extend([
            ("about", "about", fhirreference.FHIRReference, True, None, False),
            ("_about", "_about", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("_basedOn", "_basedOn", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("_category", "_category", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("_encounter", "_encounter", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("_identifier", "_identifier", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("inResponseTo", "inResponseTo", fhirreference.FHIRReference, True, None, False),
            ("_inResponseTo", "_inResponseTo", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesCanonical", "instantiatesCanonical", str, True, None, False),
            ("_instantiatesCanonical", "_instantiatesCanonical", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("instantiatesUri", "instantiatesUri", str, True, None, False),
            ("_instantiatesUri", "_instantiatesUri", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("_medium", "_medium", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("_note", "_note", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("_partOf", "_partOf", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("payload", "payload", CommunicationPayload, True, None, False),
            ("_payload", "_payload", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("_priority", "_priority", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("_reasonCode", "_reasonCode", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("_reasonReference", "_reasonReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("received", "received", fhirdatetime.FHIRDateTime, False, None, False),
            ("_received", "_received", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("_recipient", "_recipient", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("_sender", "_sender", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("sent", "sent", fhirdatetime.FHIRDateTime, False, None, False),
            ("_sent", "_sent", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("status", "status", str, False, None, True),
            ("_status", "_status", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("statusReason", "statusReason", codeableconcept.CodeableConcept, False, None, False),
            ("_statusReason", "_statusReason", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("_subject", "_subject", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("topic", "topic", codeableconcept.CodeableConcept, False, None, False),
            ("_topic", "_topic", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js


from . import backboneelement

class CommunicationPayload(backboneelement.BackboneElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """
    
    resource_type = "CommunicationPayload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """
        self._contentAttachment = None
        """ Primitive extension for contentAttachment. Type `FHIRPrimitiveExtension` """
        
        self.contentReference = None
        """ Message part content.
        Type `FHIRReference` (represented as `dict` in JSON). """
        self._contentReference = None
        """ Primitive extension for contentReference. Type `FHIRPrimitiveExtension` """
        
        self.contentString = None
        """ Message part content.
        Type `str`. """
        self._contentString = None
        """ Primitive extension for contentString. Type `FHIRPrimitiveExtension` """
        
        super(CommunicationPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("_contentAttachment", "_contentAttachment", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("_contentReference", "_contentReference", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
            ("contentString", "contentString", str, False, "content", True),
            ("_contentString", "_contentString", fhirprimitiveextension.FHIRPrimitiveExtension, False, None, False),
        ])
        return js

from . import fhirprimitiveextension

from . import annotation
from . import attachment
from . import codeableconcept
from . import fhirdatetime
from . import fhirreference
from . import identifier