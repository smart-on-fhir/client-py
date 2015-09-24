#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/SupplyDelivery) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity


class SupplyDelivery(domainresource.DomainResource):
    """ Delivery of Supply.
    
    Record of delivery of what is supplied.
    """
    
    resource_name = "SupplyDelivery"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
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
        
        super(SupplyDelivery, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SupplyDelivery, self).elementProperties()
        js.extend([
            ("destination", "destination", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("suppliedItem", "suppliedItem", fhirreference.FHIRReference, False),
            ("supplier", "supplier", fhirreference.FHIRReference, False),
            ("time", "time", fhirdate.FHIRDate, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
            ("whenPrepared", "whenPrepared", period.Period, False),
        ])
        return js

