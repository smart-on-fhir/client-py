#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Communication) on 2015-04-08.
#  2015, SMART Health IT.


import attachment
import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class Communication(domainresource.DomainResource):
    """ A record of information transmitted from a sender to a receiver.
    
    An occurrence of information being transmitted. E.g., an alert that was
    sent to a responsible provider, a public health agency was notified about a
    reportable condition.
    """
    
    resource_name = "Communication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.category = None
        """ Message category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Encounter leading to message.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medium = None
        """ Communication medium.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationPayload` items (represented as `dict` in JSON). """
        
        self.reason = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.received = None
        """ When received.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.sent = None
        """ When sent.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None
        """ in-progress | completed | suspended | rejected | failed.
        Type `str`. """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(Communication, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Communication, self).update_with_json(jsondict)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'medium' in jsondict:
            self.medium = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['medium'], self)
        if 'payload' in jsondict:
            self.payload = CommunicationPayload.with_json_and_owner(jsondict['payload'], self)
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'received' in jsondict:
            self.received = fhirdate.FHIRDate.with_json_and_owner(jsondict['received'], self)
        if 'recipient' in jsondict:
            self.recipient = fhirreference.FHIRReference.with_json_and_owner(jsondict['recipient'], self)
        if 'sender' in jsondict:
            self.sender = fhirreference.FHIRReference.with_json_and_owner(jsondict['sender'], self)
        if 'sent' in jsondict:
            self.sent = fhirdate.FHIRDate.with_json_and_owner(jsondict['sent'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)


class CommunicationPayload(fhirelement.FHIRElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) that was communicated to the recipient.
    """
    
    resource_name = "CommunicationPayload"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(CommunicationPayload, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CommunicationPayload, self).update_with_json(jsondict)
        if 'contentAttachment' in jsondict:
            self.contentAttachment = attachment.Attachment.with_json_and_owner(jsondict['contentAttachment'], self)
        if 'contentReference' in jsondict:
            self.contentReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['contentReference'], self)
        if 'contentString' in jsondict:
            self.contentString = jsondict['contentString']

