#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2015-09-24.
#  2015, SMART Health IT.


from . import coding
from . import domainresource
from . import fhirreference
from . import identifier
from . import period


class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan.
    
    Financial instrument which may be used to pay for or reimburse health care
    products and services.
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
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("bin", "bin", identifier.Identifier, False),
            ("contract", "contract", fhirreference.FHIRReference, True),
            ("dependent", "dependent", int, False),
            ("group", "group", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("issuer", "issuer", fhirreference.FHIRReference, False),
            ("network", "network", identifier.Identifier, False),
            ("period", "period", period.Period, False),
            ("plan", "plan", str, False),
            ("sequence", "sequence", int, False),
            ("subPlan", "subPlan", str, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False),
            ("subscriberId", "subscriberId", identifier.Identifier, False),
            ("type", "type", coding.Coding, False),
        ])
        return js

