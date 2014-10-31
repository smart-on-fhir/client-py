#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (orderresponse.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier
import narrative
import order
import practitioner


class OrderResponse(fhirresource.FHIRResource):
    """ A response to an order.
    
    Scope and Usage The response to an order indicates the outcome of
    processing the order itself - whether it was accepted or rejected, or is
    still in process. The order response resource does not itself convey or
    represent information that arises as a result of performing the actual
    order, but it may have references to other resources that do have this
    information, in order to link between the original order and its outcome.
    """
    
    resource_name = "OrderResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authorityCodeableConcept = None
        """ If required by policy.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.authorityResource = None
        """ If required by policy.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.code = None
        """ pending | review | rejected | error | accepted | cancelled |
        replaced | aborted | complete.
        Type `str`. """
        
        self.date = None
        """ When the response was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Additional description of the response.
        Type `str`. """
        
        self.fulfillment = None
        """ Details of the outcome of performing the order.
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.request = None
        """ The order that this is a response to.
        Type `FHIRReference` referencing `Order` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.who = None
        """ Who made the response.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        super(OrderResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OrderResponse, self).update_with_json(jsondict)
        if 'authorityCodeableConcept' in jsondict:
            self.authorityCodeableConcept = codeableconcept.CodeableConcept.with_json(jsondict['authorityCodeableConcept'])
        if 'authorityResource' in jsondict:
            self.authorityResource = fhirreference.FHIRReference.with_json_and_owner(jsondict['authorityResource'], self, fhirresource.FHIRResource)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json(jsondict['date'])
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'fulfillment' in jsondict:
            self.fulfillment = fhirreference.FHIRReference.with_json_and_owner(jsondict['fulfillment'], self, fhirresource.FHIRResource)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json(jsondict['identifier'])
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self, order.Order)
        if 'text' in jsondict:
            self.text = narrative.Narrative.with_json(jsondict['text'])
        if 'who' in jsondict:
            self.who = fhirreference.FHIRReference.with_json_and_owner(jsondict['who'], self, practitioner.Practitioner)

