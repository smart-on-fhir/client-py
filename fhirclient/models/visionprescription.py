#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.1.7108 (http://hl7.org/fhir/StructureDefinition/VisionPrescription) on 2015-09-24.
#  2015, SMART Health IT.


from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirelement
from . import fhirreference
from . import identifier
from . import quantity


class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.
    
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
        """ Who authorizes the vision product.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        super(VisionPrescription, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend([
            ("dateWritten", "dateWritten", fhirdate.FHIRDate, False),
            ("dispense", "dispense", VisionPrescriptionDispense, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("prescriber", "prescriber", fhirreference.FHIRReference, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False),
        ])
        return js


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
        """ Contact lens diameter.
        Type `float`. """
        
        self.duration = None
        """ Lens wear duration.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        self.eye = None
        """ right | left.
        Type `str`. """
        
        self.notes = None
        """ Notes for coatings.
        Type `str`. """
        
        self.power = None
        """ Contact lens power.
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
    
    def elementProperties(self):
        js = super(VisionPrescriptionDispense, self).elementProperties()
        js.extend([
            ("add", "add", float, False),
            ("axis", "axis", int, False),
            ("backCurve", "backCurve", float, False),
            ("base", "base", str, False),
            ("brand", "brand", str, False),
            ("color", "color", str, False),
            ("cylinder", "cylinder", float, False),
            ("diameter", "diameter", float, False),
            ("duration", "duration", quantity.Quantity, False),
            ("eye", "eye", str, False),
            ("notes", "notes", str, False),
            ("power", "power", float, False),
            ("prism", "prism", float, False),
            ("product", "product", coding.Coding, False),
            ("sphere", "sphere", float, False),
        ])
        return js

