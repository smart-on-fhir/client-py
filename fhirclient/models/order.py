#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Order) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import timing


class Order(domainresource.DomainResource):
    """ A request to perform an action.
    """
    
    resource_name = "Order"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authority = None
        """ If required by policy.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the order was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ What action is being ordered.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Text - why the order was made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Text - why the order was made.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who initiated the order.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Patient this order is about.
        Type `FHIRReference` referencing `Patient, Group, Device, Substance` (represented as `dict` in JSON). """
        
        self.target = None
        """ Who is intended to fulfill the order.
        Type `FHIRReference` referencing `Organization, Device, Practitioner` (represented as `dict` in JSON). """
        
        self.when = None
        """ When order should be fulfilled.
        Type `OrderWhen` (represented as `dict` in JSON). """
        
        super(Order, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Order, self).update_with_json(jsondict)
        if 'authority' in jsondict:
            self.authority = fhirreference.FHIRReference.with_json_and_owner(jsondict['authority'], self)
        if 'date' in jsondict:
            self.date = fhirdate.FHIRDate.with_json_and_owner(jsondict['date'], self)
        if 'detail' in jsondict:
            self.detail = fhirreference.FHIRReference.with_json_and_owner(jsondict['detail'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'reasonCodeableConcept' in jsondict:
            self.reasonCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonCodeableConcept'], self)
        if 'reasonReference' in jsondict:
            self.reasonReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reasonReference'], self)
        if 'source' in jsondict:
            self.source = fhirreference.FHIRReference.with_json_and_owner(jsondict['source'], self)
        if 'subject' in jsondict:
            self.subject = fhirreference.FHIRReference.with_json_and_owner(jsondict['subject'], self)
        if 'target' in jsondict:
            self.target = fhirreference.FHIRReference.with_json_and_owner(jsondict['target'], self)
        if 'when' in jsondict:
            self.when = OrderWhen.with_json_and_owner(jsondict['when'], self)


class OrderWhen(fhirelement.FHIRElement):
    """ When order should be fulfilled.
    """
    
    resource_name = "OrderWhen"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code specifies when request should be done. The code may simply be
        a priority code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ A formal schedule.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(OrderWhen, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OrderWhen, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['code'], self)
        if 'schedule' in jsondict:
            self.schedule = timing.Timing.with_json_and_owner(jsondict['schedule'], self)

