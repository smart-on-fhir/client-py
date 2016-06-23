#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Coverage) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan.
    
    Financial instrument which may be used to pay for or reimburse health care
    products and services.
    """
    
    resource_name = "Coverage"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
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
        
        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend([
            ("bin", "bin", identifier.Identifier, False, None, False),
            ("contract", "contract", fhirreference.FHIRReference, True, None, False),
            ("dependent", "dependent", int, False, None, False),
            ("group", "group", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("issuer", "issuer", fhirreference.FHIRReference, False, None, False),
            ("network", "network", identifier.Identifier, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("plan", "plan", str, False, None, False),
            ("sequence", "sequence", int, False, None, False),
            ("subPlan", "subPlan", str, False, None, False),
            ("subscriber", "subscriber", fhirreference.FHIRReference, False, None, False),
            ("subscriberId", "subscriberId", identifier.Identifier, False, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirreference
from . import identifier
from . import period
