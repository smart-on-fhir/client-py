#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (supply.profile.json) on 2014-10-17.
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
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Location
import Medication
import Narrative
import Patient
import Period
import Practitioner
import Quantity


class Supply(FHIRResource.FHIRResource):
    """ A supply -  request and provision.
    
    Scope and Usage The scope of the supply resource is for supplies used in
    the healthcare process. This includes supplies specifically used in the
    treatment of patients as well as supply movement within an institution
    (transport a set of supplies from materials management to a service unit
    (nurse station). This resource does not include the provisioning of
    transportation services.
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
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | dispensed | received | failed | cancelled.
        Type `str`. """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        super(Supply, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Supply, self).update_with_json(jsondict)
        if 'dispense' in jsondict:
            self.dispense = SupplyDispense.with_json(jsondict['dispense'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'kind' in jsondict:
            self.kind = CodeableConcept.CodeableConcept.with_json(jsondict['kind'])
        if 'orderedItem' in jsondict:
            self.orderedItem = FHIRReference.FHIRReference.with_json_and_owner(jsondict['orderedItem'], self, Medication.Medication)
        if 'patient' in jsondict:
            self.patient = FHIRReference.FHIRReference.with_json_and_owner(jsondict['patient'], self, Patient.Patient)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])


class SupplyDispense(FHIRElement.FHIRElement):
    """ Supply details.
    
    Indicates the details of the dispense event such as the days supply and
    quantity of a supply dispensed.
    """
    
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
        """ in progress | dispensed | abandoned.
        Type `str`. """
        
        self.suppliedItem = None
        """ Medication, Substance, or Device supplied.
        Type `FHIRReference` referencing `Medication` (represented as `dict` in JSON). """
        
        self.supplier = None
        """ Dispenser.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.type = None
        """ Category of dispense event.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.whenHandedOver = None
        """ Handover time.
        Type `Period` (represented as `dict` in JSON). """
        
        self.whenPrepared = None
        """ Dispensing time.
        Type `Period` (represented as `dict` in JSON). """
        
        super(SupplyDispense, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SupplyDispense, self).update_with_json(jsondict)
        if 'destination' in jsondict:
            self.destination = FHIRReference.FHIRReference.with_json_and_owner(jsondict['destination'], self, Location.Location)
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'quantity' in jsondict:
            self.quantity = Quantity.Quantity.with_json(jsondict['quantity'])
        if 'receiver' in jsondict:
            self.receiver = FHIRReference.FHIRReference.with_json_and_owner(jsondict['receiver'], self, Practitioner.Practitioner)
        if 'status' in jsondict:
            self.status = jsondict['status']
        if 'suppliedItem' in jsondict:
            self.suppliedItem = FHIRReference.FHIRReference.with_json_and_owner(jsondict['suppliedItem'], self, Medication.Medication)
        if 'supplier' in jsondict:
            self.supplier = FHIRReference.FHIRReference.with_json_and_owner(jsondict['supplier'], self, Practitioner.Practitioner)
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])
        if 'whenHandedOver' in jsondict:
            self.whenHandedOver = Period.Period.with_json(jsondict['whenHandedOver'])
        if 'whenPrepared' in jsondict:
            self.whenPrepared = Period.Period.with_json(jsondict['whenPrepared'])

