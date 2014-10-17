#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (order.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import CodeableConcept
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Narrative
import Organization
import Patient
import Practitioner
import Schedule


class Order(FHIRResource.FHIRResource):
    """ A request to perform an action.
    
    Scope and Usage An order resource describes a request that an action be
    performed. An order is expected to lead to one or more responses that
    describe the outcome of processing/handling the order. The order resource
    is focused on the process of actually requesting an action be performed;
    the actual action to be performed is detailed in a separate resource that
    contains the details. Note that orders are often called "requests", but
    this name is not used here since the word "request" is used differently
    elsewhere in this specification.
    
    Note that there are a variety of processes associated with making and
    processing orders. Some orders may be handled immediately by automated
    systems but most require real world actions by one or more humans. Some
    orders can only be processed when other real world actions happen, such as
    a patient actually presenting themselves so that the action to be performed
    can actually be performed. Often these real world dependencies are only
    implicit in the order details.
    """
    
    resource_name = "Order"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authority = None
        """ If required by policy.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the order was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ What action is being ordered.
        List of `FHIRReference` items referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Text - why the order was made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonResource = None
        """ Text - why the order was made.
        Type `FHIRReference` referencing `FHIRResource` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who initiated the order.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Patient this order is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.target = None
        """ Who is intended to fulfill the order.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.when = None
        """ When order should be fulfilled.
        Type `OrderWhen` (represented as `dict` in JSON). """
        
        super(Order, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Order, self).update_with_json(jsondict)
        if 'authority' in jsondict:
            self.authority = FHIRReference.FHIRReference.with_json_and_owner(jsondict['authority'], self, FHIRResource.FHIRResource)
        if 'date' in jsondict:
            self.date = FHIRDate.FHIRDate.with_json(jsondict['date'])
        if 'detail' in jsondict:
            self.detail = FHIRReference.FHIRReference.with_json_and_owner(jsondict['detail'], self, FHIRResource.FHIRResource)
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'reasonCodeableConcept' in jsondict:
            self.reasonCodeableConcept = CodeableConcept.CodeableConcept.with_json(jsondict['reasonCodeableConcept'])
        if 'reasonResource' in jsondict:
            self.reasonResource = FHIRReference.FHIRReference.with_json_and_owner(jsondict['reasonResource'], self, FHIRResource.FHIRResource)
        if 'source' in jsondict:
            self.source = FHIRReference.FHIRReference.with_json_and_owner(jsondict['source'], self, Practitioner.Practitioner)
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'target' in jsondict:
            self.target = FHIRReference.FHIRReference.with_json_and_owner(jsondict['target'], self, Organization.Organization)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'when' in jsondict:
            self.when = OrderWhen.with_json(jsondict['when'])


class OrderWhen(FHIRElement.FHIRElement):
    """ When order should be fulfilled.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code specifies when request should be done. The code may simply be
        a priority code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ A formal schedule.
        Type `Schedule` (represented as `dict` in JSON). """
        
        super(OrderWhen, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OrderWhen, self).update_with_json(jsondict)
        if 'code' in jsondict:
            self.code = CodeableConcept.CodeableConcept.with_json(jsondict['code'])
        if 'schedule' in jsondict:
            self.schedule = Schedule.Schedule.with_json(jsondict['schedule'])

