#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/OrderResponse) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


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
    
    def elementProperties(self):
        js = super(OrderResponse, self).elementProperties()
        js.extend([
            ("authorityCodeableConcept", "authorityCodeableConcept", codeableconcept.CodeableConcept, False),
            ("authorityReference", "authorityReference", fhirreference.FHIRReference, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("description", "description", str, False),
            ("fulfillment", "fulfillment", fhirreference.FHIRReference, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("orderStatus", "orderStatus", str, False),
            ("request", "request", fhirreference.FHIRReference, False),
            ("who", "who", fhirreference.FHIRReference, False),
        ])
        return js

