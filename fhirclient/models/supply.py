#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Supply) on 2015-04-08.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period
import quantity


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
    
    def update_with_json(self, jsondict):
        super(Supply, self).update_with_json(jsondict)
        if 'dispense' in jsondict:
            self.dispense = SupplyDispense.with_json_and_owner(jsondict['dispense'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'kind' in jsondict:
            self.kind = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['kind'], self)
        if 'orderedItem' in jsondict:
            self.orderedItem = fhirreference.FHIRReference.with_json_and_owner(jsondict['orderedItem'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']


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
    
    def update_with_json(self, jsondict):
        super(SupplyDispense, self).update_with_json(jsondict)
        if 'destination' in jsondict:
            self.destination = fhirreference.FHIRReference.with_json_and_owner(jsondict['destination'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'quantity' in jsondict:
            self.quantity = quantity.Quantity.with_json_and_owner(jsondict['quantity'], self)
        if 'receiver' in jsondict:
            self.receiver = fhirreference.FHIRReference.with_json_and_owner(jsondict['receiver'], self)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'suppliedItem' in jsondict:
            self.suppliedItem = fhirreference.FHIRReference.with_json_and_owner(jsondict['suppliedItem'], self)
        if 'supplier' in jsondict:
            self.supplier = fhirreference.FHIRReference.with_json_and_owner(jsondict['supplier'], self)
        if 'type' in jsondict:
            self.type = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['type'], self)
        if 'whenHandedOver' in jsondict:
            self.whenHandedOver = fhirdate.FHIRDate.with_json_and_owner(jsondict['whenHandedOver'], self)
        if 'whenPrepared' in jsondict:
            self.whenPrepared = period.Period.with_json_and_owner(jsondict['whenPrepared'], self)

