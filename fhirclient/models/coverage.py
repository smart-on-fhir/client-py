#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2015-04-08.
#  2015, SMART Health IT.


import coding
import domainresource
import fhirreference
import identifier
import period


class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan.
    
    Financial instrument which may be used to pay for or reimburse for health
    care products and services.
    """
    
    resource_name = "Coverage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bin = None
        """ BIN Number.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.contract = None
        """ Contract details.
        List of `FHIRReference` items referencing `Contract` (represented as `dict` in JSON). """
        
        self.dependent = None
        """ The dependent number.
        Type `int`. """
        
        self.group = None
        """ An identifier for the group.
        Type `str`. """
        
        self.identifier = None
        """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.issuer = None
        """ An identifier for the plan issuer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.network = None
        """ Insurer network.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """
        
        self.plan = None
        """ An identifier for the plan.
        Type `str`. """
        
        self.sequence = None
        """ The plan instance or sequence counter.
        Type `int`. """
        
        self.subPlan = None
        """ An identifier for the subsection of the plan.
        Type `str`. """
        
        self.subscriber = None
        """ Plan holder information.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.subscriberId = None
        """ Subscriber ID.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.type = None
        """ Type of coverage.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(Coverage, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Coverage, self).update_with_json(jsondict)
        if 'bin' in jsondict:
            self.bin = identifier.Identifier.with_json_and_owner(jsondict['bin'], self)
        if 'contract' in jsondict:
            self.contract = fhirreference.FHIRReference.with_json_and_owner(jsondict['contract'], self)
        if 'dependent' in jsondict:
            self.dependent = jsondict['dependent']
        if 'group' in jsondict:
            self.group = jsondict['group']
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'issuer' in jsondict:
            self.issuer = fhirreference.FHIRReference.with_json_and_owner(jsondict['issuer'], self)
        if 'network' in jsondict:
            self.network = identifier.Identifier.with_json_and_owner(jsondict['network'], self)
        if 'period' in jsondict:
            self.period = period.Period.with_json_and_owner(jsondict['period'], self)
        if 'plan' in jsondict:
            self.plan = jsondict['plan']
        if 'sequence' in jsondict:
            self.sequence = jsondict['sequence']
        if 'subPlan' in jsondict:
            self.subPlan = jsondict['subPlan']
        if 'subscriber' in jsondict:
            self.subscriber = fhirreference.FHIRReference.with_json_and_owner(jsondict['subscriber'], self)
        if 'subscriberId' in jsondict:
            self.subscriberId = identifier.Identifier.with_json_and_owner(jsondict['subscriberId'], self)
        if 'type' in jsondict:
            self.type = coding.Coding.with_json_and_owner(jsondict['type'], self)

