#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.4.0.3933 (visionprescription.profile.json) on 2015-01-10.
#  2015, SMART Platforms.


import codeableconcept
import coding
import fhirdate
import fhirelement
import fhirreference
import fhirresource
import identifier
import quantity


class VisionPrescription(fhirresource.FHIRResource):
    """ Prescription for Vision correction products for a patient.
    
    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """
    
    resource_name = "VisionPrescription"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dispense = None
        """ Vision supply authorization.
        List of `VisionPrescriptionDispense` items (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.prescriber = None
        """ Who authorizes the Vision product.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        super(VisionPrescription, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(VisionPrescription, self).update_with_json(jsondict)
        if 'dateWritten' in jsondict:
            self.dateWritten = fhirdate.FHIRDate.with_json_and_owner(jsondict['dateWritten'], self)
        if 'dispense' in jsondict:
            self.dispense = VisionPrescriptionDispense.with_json_and_owner(jsondict['dispense'], self)
        if 'encounter' in jsondict:
            self.encounter = fhirreference.FHIRReference.with_json_and_owner(jsondict['encounter'], self)
        if 'identifier' in jsondict:
            self.identifier = identifier.Identifier.with_json_and_owner(jsondict['identifier'], self)
        if 'patient' in jsondict:
            self.patient = fhirreference.FHIRReference.with_json_and_owner(jsondict['patient'], self)
        if 'prescriber' in jsondict:
            self.prescriber = fhirreference.FHIRReference.with_json_and_owner(jsondict['prescriber'], self)
        if 'reasonCodeableConcept' in jsondict:
            self.reasonCodeableConcept = codeableconcept.CodeableConcept.with_json_and_owner(jsondict['reasonCodeableConcept'], self)
        if 'reasonReference' in jsondict:
            self.reasonReference = fhirreference.FHIRReference.with_json_and_owner(jsondict['reasonReference'], self)


class VisionPrescriptionDispense(fhirelement.FHIRElement):
    """ Vision supply authorization.
    
    Deals with details of the dispense part of the supply specification.
    """
    
    resource_name = "VisionPrescriptionDispense"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.add = None
        """ Lens add.
        Type `float`. """
        
        self.axis = None
        """ Lens axis.
        Type `int`. """
        
        self.backCurve = None
        """ Contact lens back curvature.
        Type `float`. """
        
        self.base = None
        """ up | down | in | out.
        Type `str`. """
        
        self.brand = None
        """ Lens add.
        Type `str`. """
        
        self.color = None
        """ Lens add.
        Type `str`. """
        
        self.cylinder = None
        """ Lens cylinder.
        Type `float`. """
        
        self.diameter = None
        """ Contact Lens diameter.
        Type `float`. """
        
        self.duration = None
        """ Lens wear duration.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.eye = None
        """ right | left.
        Type `str`. """
        
        self.notes = None
        """ Notes for coatings.
        Type `str`. """
        
        self.power = None
        """ Contact Lens power.
        Type `float`. """
        
        self.prism = None
        """ Lens prism.
        Type `float`. """
        
        self.product = None
        """ Product to be supplied.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.sphere = None
        """ Lens sphere.
        Type `float`. """
        
        super(VisionPrescriptionDispense, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(VisionPrescriptionDispense, self).update_with_json(jsondict)
        if 'add' in jsondict:
            self.add = jsondict['add']
        if 'axis' in jsondict:
            self.axis = jsondict['axis']
        if 'backCurve' in jsondict:
            self.backCurve = jsondict['backCurve']
        if 'base' in jsondict:
            self.base = jsondict['base']
        if 'brand' in jsondict:
            self.brand = jsondict['brand']
        if 'color' in jsondict:
            self.color = jsondict['color']
        if 'cylinder' in jsondict:
            self.cylinder = jsondict['cylinder']
        if 'diameter' in jsondict:
            self.diameter = jsondict['diameter']
        if 'duration' in jsondict:
            self.duration = quantity.Quantity.with_json_and_owner(jsondict['duration'], self)
        if 'eye' in jsondict:
            self.eye = jsondict['eye']
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'power' in jsondict:
            self.power = jsondict['power']
        if 'prism' in jsondict:
            self.prism = jsondict['prism']
        if 'product' in jsondict:
            self.product = coding.Coding.with_json_and_owner(jsondict['product'], self)
        if 'sphere' in jsondict:
            self.sphere = jsondict['sphere']

