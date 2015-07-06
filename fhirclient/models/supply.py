#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Supply) on 2015-07-06.
#  2015, SMART Health IT.


from . import codeableconcept
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import period
from . import quantity


class Supply(domainresource.DomainResource):
    """ A supply -  request and provision.
    
    A supply - a  request for something, and provision of what is supplied.
    """
    
    resource_name = "Supply"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.dispense = None
        """ Supply details.
        List of `SupplyDispense` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.kind = None
        """ The kind of supply (central, non-stock, etc).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.orderedItem = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | dispensed | received | failed | cancelled.
        Type `str`. """
        
        super(Supply, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Supply, self).elementProperties()
        js.extend([
            ("dispense", "dispense", SupplyDispense, True),
            ("identifier", "identifier", identifier.Identifier, False),
            ("kind", "kind", codeableconcept.CodeableConcept, False),
            ("orderedItem", "orderedItem", fhirreference.FHIRReference, False),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("status", "status", str, False),
        ])
        return js


class SupplyDispense(fhirelement.FHIRElement):
    """ Supply details.
    
    Indicates the details of the dispense event such as the days supply and
    quantity of a supply dispensed.
    """
    
    resource_name = "SupplyDispense"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.destination = None
        """ Where the Supply was sent.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ External identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.receiver = None
        """ Who collected the Supply.
        List of `FHIRReference` items referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.status = None
        """ in-progress | dispensed | abandoned.
        Type `str`. """
        
        self.suppliedItem = None
        """ Medication, Substance, or Device supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """
        
        self.supplier = None
        """ Dispenser.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None
        """ Category of dispense event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.whenHandedOver = None
        """ Handover time.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.whenPrepared = None
        """ Dispensing time.
        Type `Period` (represented as `dict` in JSON). """
        
        super(SupplyDispense, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(SupplyDispense, self).elementProperties()
        js.extend([
            ("destination", "destination", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("quantity", "quantity", quantity.Quantity, False),
            ("receiver", "receiver", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("suppliedItem", "suppliedItem", fhirreference.FHIRReference, False),
            ("supplier", "supplier", fhirreference.FHIRReference, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
            ("whenHandedOver", "whenHandedOver", fhirdate.FHIRDate, False),
            ("whenPrepared", "whenPrepared", period.Period, False),
        ])
        return js

