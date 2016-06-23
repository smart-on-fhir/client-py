#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2016-06-23.
#  2016, SMART Health IT.


from . import domainresource

class SupplyDelivery(domainresource.DomainResource):
    """ Delivery of Supply.
    
    Record of delivery of what is supplied.
    """
    
    resource_name = "SupplyDelivery"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.destination = None
        """ Where the Supply was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ Who collected the Supply.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | completed | abandoned.
        Type `str`. """
        
        self.suppliedItem = None
        """ Medication, Substance, or Device supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """
        
        self.supplier = None
        """ Dispenser.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.time = None
        """ Handover time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.type = None
        """ Category of dispense event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.whenPrepared = None
        """ Dispensing time.
        Type `Period` (represented as `dict` in JSON). """
        
        super(SupplyDelivery, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyDelivery, self).elementProperties()
        js.extend([
            ("destination", "destination", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True, None, False),
            ("status", "status", str, False, None, False),
            ("suppliedItem", "suppliedItem", fhirreference.FHIRReference, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, False, None, False),
            ("time", "time", fhirdate.FHIRDate, False, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
            ("whenPrepared", "whenPrepared", period.Period, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
