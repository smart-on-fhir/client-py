#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2017-03-22.
#  2017, SMART Health IT.


from . import domainresource

class SupplyDelivery(domainresource.DomainResource):
    """ Delivery of bulk Supplies.
    
    Record of delivery of what is supplied.
    """
    
    resource_type = "SupplyDelivery"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basedOn = None
        """ Fulfills plan, proposal or order.
        List of `FHIRReference` items referencing `SupplyRequest` (represented as `dict` in JSON). """
        
        self.destination = None
        """ Where the Supply was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.occurrenceDateTime = None
        """ When event occurred.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.occurrencePeriod = None
        """ When event occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.occurrenceTiming = None
        """ When event occurred.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.partOf = None
        """ Part of referenced event.
        List of `FHIRReference` items referencing `SupplyDelivery, Contract` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ Who collected the Supply.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | completed | abandoned | entered-in-error.
        Type `str`. """
        
        self.suppliedItem = None
        """ The item that is delivered or supplied.
        Type `SupplyDeliverySuppliedItem` (represented as `dict` in JSON). """
        
        self.supplier = None
        """ Dispenser.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.type = None
        """ Category of dispense event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(SupplyDelivery, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyDelivery, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, True, None, False),
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", fhirdate.FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", period.Period, False, "occurrence", False),
            ("occurrenceTiming", "occurrenceTiming", timing.Timing, False, "occurrence", False),
            ("partOf", "partOf", fhirreference.FHIRReference, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("suppliedItem", "suppliedItem", SupplyDeliverySuppliedItem, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class SupplyDeliverySuppliedItem(backboneelement.BackboneElement):
    """ The item that is delivered or supplied.
    
    The item that is being delivered or has been supplied.
    """
    
    resource_type = "SupplyDeliverySuppliedItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.itemCodeableConcept = None
        """ Medication, Substance, or Device supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.itemReference = None
        """ Medication, Substance, or Device supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        super(SupplyDeliverySuppliedItem, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyDeliverySuppliedItem, self).elementProperties()
        js.extend([
            ("itemCodeableConcept", "itemCodeableConcept", codeableconcept.CodeableConcept, False, "item", False),
            ("itemReference", "itemReference", fhirreference.FHIRReference, False, "item", False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js


import sys
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + '.period']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + '.timing']
