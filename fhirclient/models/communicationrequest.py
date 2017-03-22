#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.
    
    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """
    
    resource_type = "CommunicationRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authoredOn = None
        """ When request transitioned to being actionable.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.basedOn = None
        """ Fulfills plan or proposal.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.category = None
        """ Message category.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.context = None
        """ Encounter or episode leading to message.
        Type `FHIRReference` referencing `Encounter, EpisodeOfCare` (represented as `dict` in JSON). """
        
        self.groupIdentifier = None
        """ Composite request this is part of.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medium = None
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.note = None
        """ Comments made about communication request.
        List of `Annotation` items (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When scheduled.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When scheduled.
        Type `Period` (represented as `dict` in JSON). """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ Message urgency.
        Type `str`. """
        
        self.reasonCode = None
        """ Why is communication needed?.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why is communication needed?.
        List of `FHIRReference` items referencing `Condition, Observation` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items referencing `Device, Organization, Patient, Practitioner, RelatedPerson, Group, CareTeam` (represented as `dict` in JSON). """
        
        self.replaces = None
        """ Request(s) replaced by this request.
        List of `FHIRReference` items referencing `CommunicationRequest` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Who/what is requesting service.
        Type `CommunicationRequestRequester` (represented as `dict` in JSON). """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | active | suspended | cancelled | completed | entered-in-
        error | unknown.
        Type `str`. """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        self.topic = None
        """ Focal resources.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(CommunicationRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("authoredOn", "authoredOn", fhirdate.FHIRDate, False, None, False),
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("context", "context", fhirreference.FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", identifier.Identifier, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("note", "note", annotation.Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("payload", "payload", CommunicationRequestPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("replaces", "replaces", fhirreference.FHIRReference, True, None, False),
            ("requester", "requester", CommunicationRequestRequester, False, None, False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
            ("topic", "topic", fhirreference.FHIRReference, True, None, False),
        ])
        return js


from . import backboneelement

class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    
    resource_type = "CommunicationRequestPayload"
    
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
        
        super(CommunicationRequestPayload, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
        ])
        return js


class CommunicationRequestRequester(backboneelement.BackboneElement):
    """ Who/what is requesting service.
    
    The individual who initiated the request and has responsibility for its
    activation.
    """
    
    resource_type = "CommunicationRequestRequester"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.agent = None
        """ Individual making the request.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient, RelatedPerson, Device` (represented as `dict` in JSON). """
        
        self.onBehalfOf = None
        """ Organization agent is acting for.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(CommunicationRequestRequester, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(CommunicationRequestRequester, self).elementProperties()
        js.extend([
            ("agent", "agent", fhirreference.FHIRReference, False, None, True),
            ("onBehalfOf", "onBehalfOf", fhirreference.FHIRReference, False, None, False),
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
