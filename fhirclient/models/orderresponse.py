#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/OrderResponse) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirreference
import identifier


class OrderResponse(domainresource.DomainResource):
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
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the response was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None
        """ Additional description of the response.
        Type `str`. """
        
        self.fulfillment = None
        """ Details of the outcome of performing the order.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.orderStatus = None
        """ pending | review | rejected | error | accepted | cancelled |
        replaced | aborted | completed.
        Type `str`. """
        
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
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'fulfillment' in jsondict:
            self.fulfillment = fhirreference.FHIRReference.with_json_and_owner(jsondict['fulfillment'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'orderStatus' in jsondict:
            self.orderStatus = jsondict['orderStatus']
        if 'request' in jsondict:
            self.request = fhirreference.FHIRReference.with_json_and_owner(jsondict['request'], self)
        if 'who' in jsondict:
            self.who = fhirreference.FHIRReference.with_json_and_owner(jsondict['who'], self)

