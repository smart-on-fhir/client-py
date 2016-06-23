#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SupplyRequest) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.
    
    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    
    resource_name = "SupplyRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the request was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.kind = None
        """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.orderedItem = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Why the supply item was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why the supply item was requested.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who initiated this order.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | completed | failed | cancelled.
        Type `str`. """
        
        self.supplier = None
        """ Who is intended to fulfill the request.
        List of `FHIRReference` items referencing `Organization` (represented as `dict` in JSON). """
        
        self.when = None
        """ When the request should be fulfilled.
        Type `SupplyRequestWhen` (represented as `dict` in JSON). """
        
        super(SupplyRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("kind", "kind", codeableconcept.CodeableConcept, False, None, False),
            ("orderedItem", "orderedItem", fhirreference.FHIRReference, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, True, None, False),
            ("when", "when", SupplyRequestWhen, False, None, False),
        ])
        return js


from . import backboneelement

class SupplyRequestWhen(backboneelement.BackboneElement):
    """ When the request should be fulfilled.
    """
    
    resource_name = "SupplyRequestWhen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Fulfilment code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ Formal fulfillment schedule.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(SupplyRequestWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequestWhen, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("schedule", "schedule", timing.Timing, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing
