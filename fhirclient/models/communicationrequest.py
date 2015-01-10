#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (communicationrequest.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import attachment
import codeableconcept
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier


class CommunicationRequest(fhirresource.FHIRResource):
    """ Communication Request.
    
    A request to convey information. E.g., the CDS system proposes that an
    alert be sent to a responsible provider, the CDS system proposes that the
    public health agency be notified about a reportable condition.
    """
    
    resource_name = "CommunicationRequest"
    
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
        
        self.orderedOn = None
        """ When ordered or proposed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.payload = None
        """ Message payload.
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """
        
        self.priority = None
        """ Message urgency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Message recipient.
        List of `FHIRReference` items referencing `Patient, Device, RelatedPerson, Practitioner` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Requester of communication.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.scheduledTime = None
        """ When scheduled.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.sender = None
        """ Message sender.
        Type `FHIRReference` referencing `Patient, Practitioner, Device, RelatedPerson, Organization` (represented as `dict` in JSON). """
        
        self.status = None
        """ proposed | planned | requested | received | accepted | in progress
        | completed | suspended | rejected | failed.
        Type `str`. """
        
        self.subject = None
        """ Focus of message.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(CommunicationRequest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CommunicationRequest, self).update_with_json(jsondict)
        if 'category' in jsondict:
            self.category = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['category'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'medium' in jsondict:
            self.medium = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['medium'], self)
        if 'orderedOn' in jsondict:
            self.orderedOn = fhirdate.FHIRDate.with_json_and_owner(jsondict['orderedOn'], self)
        if 'payload' in jsondict:
            self.payload = CommunicationRequestPayload.with_json_and_owner(jsondict['payload'], self)
        if 'priority' in jsondict:
            self.priority = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['priority'], self)
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'recipient' in jsondict:
            self.recipient = fhirreference.FHIRReference.with_json_and_owner(jsondict['recipient'], self)
        if 'requester' in jsondict:
            self.requester = fhirreference.FHIRReference.with_json_and_owner(jsondict['requester'], self)
        if 'scheduledTime' in jsondict:
            self.scheduledTime = fhirdate.FHIRDate.with_json_and_owner(jsondict['scheduledTime'], self)
        if 'sender' in jsondict:
            self.sender = fhirreference.FHIRReference.with_json_and_owner(jsondict['sender'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)


class CommunicationRequestPayload(fhirelement.FHIRElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    
    resource_name = "CommunicationRequestPayload"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentAttachment = None
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None
        """ Message part content.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.contentString = None
        """ Message part content.
        Type `str`. """
        
        super(CommunicationRequestPayload, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(CommunicationRequestPayload, self).update_with_json(jsondict)
        if 'contentAttachment' in jsondict:
            self.contentAttachment = attachment.Attachment.with_json_and_owner(jsondict['contentAttachment'], self)
        if 'contentReference' in jsondict:
            self.contentReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['contentReference'], self)
        if 'contentString' in jsondict:
            self.contentString = jsondict['contentString']

