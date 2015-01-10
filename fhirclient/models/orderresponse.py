#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (orderresponse.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import fhirdate
import fhirreference
import fhirresource
import identifier


class OrderResponse(fhirresource.FHIRResource):
    """ A response to an order.
    """
    
    resource_name = "OrderResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authorityCodeableConcept = None
        """ If required by policy.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.authorityReference = None
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
        
        self.who = None
        """ Who made the response.
        Type `FHIRReference` referencing `Practitioner, Organization, Device` (represented as `dict` in JSON). """
        
        super(OrderResponse, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OrderResponse, self).update_with_json(jsondict)
        if 'authorityCodeableConcept' in jsondict:
            self.authorityCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['authorityCodeableConcept'], self)
        if 'authorityReference' in jsondict:
            self.authorityReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['authorityReference'], self)
        if 'code' in jsondict:
            self.code = jsondict['code']
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'fulfillment' in jsondict:
            self.fulfillment = fhirreference.FHIRReference.with_json_and_owner(jsondict['fulfillment'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'who' in jsondict:
            self.who = fhirreference.FHIRReference.with_json_and_owner(jsondict['who'], self)

