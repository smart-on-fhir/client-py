#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/ReferralRequest) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirreference
import identifier
import period


class ReferralRequest(domainresource.DomainResource):
    """ A request for referral or transfer of care.
    
    Used to record and send details about a request for referral service or
    transfer of a patient to the care of another provider or provider
    organisation.
    """
    
    resource_name = "ReferralRequest"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.dateSent = None
        """ Date referral/transfer of care request is sent.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ A textual description of the referral.
        Type `str`. """
        
        self.encounter = None
        """ Encounter.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.fulfillmentTime = None
        """ Requested service(s) fulfillment time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifier of request.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient referred to care or transfer.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.priority = None
        """ Urgency of referral / transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None
        """ Reason for referral / Transfer of care request.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recipient = None
        """ Receiver of referral / transfer of care request.
        List of `FHIRReference` items referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.requester = None
        """ Requester of referral / transfer of care.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient` (represented as `dict` in JSON). """
        
        self.serviceRequested = None
        """ Service(s) requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.specialty = None
        """ The clinical specialty (discipline) that the referral is requested
        for.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None
        """ draft | requested | active | cancelled | accepted | rejected |
        completed.
        Type `str`. """
        
        self.supportingInformation = None
        """ Additonal information to support referral or transfer of care
        request.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.type = None
        """ Referral/Transition of care request type.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ReferralRequest, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ReferralRequest, self).update_with_json(jsondict)
        if 'dateSent' in jsondict:
            self.dateSent = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateSent'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'fulfillmentTime' in jsondict:
            self.fulfillmentTime = period.Period.with_json_and_owner(jsondict['fulfillmentTime'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'priority' in jsondict:
            self.priority = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['priority'], self)
        if 'reason' in jsondict:
            self.reason = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reason'], self)
        if 'recipient' in jsondict:
            self.recipient = fhirreference.FHIRReference.with_json_and_owner(jsondict['recipient'], self)
        if 'requester' in jsondict:
            self.requester = fhirreference.FHIRReference.with_json_and_owner(jsondict['requester'], self)
        if 'serviceRequested' in jsondict:
            self.serviceRequested = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['serviceRequested'], self)
        if 'specialty' in jsondict:
            self.specialty = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['specialty'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'supportingInformation' in jsondict:
            self.supportingInformation = fhirreference.FHIRReference.with_json_and_owner(jsondict['supportingInformation'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)

