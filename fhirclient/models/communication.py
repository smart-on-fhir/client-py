#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/Communication) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.
    
    An occurrence of information being transmitted; e.g. an alert that was sent
    to a responsible provider, a public health agency was notified about a
    reportable condition.
    """
    
    resource_type = "Communication"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ Request fulfilled by this communication.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.category = None
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or episode leading to message.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.definition = None
        """ Instantiates protocol or definition.
        List of `FHIRReference` items referencing `PlanDefinition, ActivityDefinition` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medium = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notDone = None
        """ Communication did not occur.
        Type `bool`. """
        
        self.notDoneReason = None
        """ Why communication did not occur.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about the communication.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of this action.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationPayload` items (represented as `dict` in JSON). """
        
        self.reasonCode = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why was communication done?.
        List of `FHIRReference` items referencing `Condition, Observation` (represented as `dict` in JSON). """
        
        self.received = None
        """ When received.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items referencing `Device, Organization, Patient, Practitioner, RelatedPerson, Group` (represented as `dict` in JSON). """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.sent = None
        """ When sent.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ preparation | in-progress | suspended | aborted | completed |
        entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.topic = None
        """ Focal resources.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(Communication, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Communication, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("definition", "definition", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("notDone", "notDone", bool, False, None, False),
            ("notDoneReason", "notDoneReason", codeableconcept.CodeableConcept, False, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("payload", "payload", CommunicationPayload, True, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("received", "received", fhirdate.FHIRDate, False, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("sent", "sent", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, True, None, False),
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
        
        self.contentReference = None
        """ Message part content.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.contentString = None
        """ Message part content.
        Type `str`. """
        
        super(CommunicationPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + '.attachment']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
