#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/OrderResponse) on 2019-10-12.
#  2019, SMART Health IT.


from . import domainresource

class OrderResponse(domainresource.DomainResource):
    """ A response to an order.
    """
    
    resource_name = "OrderResponse"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
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
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("fulfillment", "fulfillment", fhirreference.FHIRReference, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("orderStatus", "orderStatus", str, False, None, True),
            ("request", "request", fhirreference.FHIRReference, False, None, True),
            ("who", "who", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import fhirdate
from . import fhirreference
from . import identifier
