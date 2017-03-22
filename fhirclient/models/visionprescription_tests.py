#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import visionprescription
from .fhirdate import FHIRDate


class VisionPrescriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("VisionPrescription", js["resourceType"])
        return visionprescription.VisionPrescription(js)
    
    def testVisionPrescription1(self):
        inst = self.instantiate_from("visionprescription-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a VisionPrescription instance")
        self.implVisionPrescription1(inst)
        
        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription1(inst2)
    
    def implVisionPrescription1(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(inst.dispense[0].add, 1.75)
        self.assertEqual(inst.dispense[0].axis, 160)
        self.assertEqual(inst.dispense[0].backCurve, 8.7)
        self.assertEqual(inst.dispense[0].brand, "OphthaGuard")
        self.assertEqual(inst.dispense[0].color, "green")
        self.assertEqual(inst.dispense[0].cylinder, -2.25)
        self.assertEqual(inst.dispense[0].diameter, 14.0)
        self.assertEqual(inst.dispense[0].duration.code, "month")
        self.assertEqual(inst.dispense[0].duration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dispense[0].duration.unit, "month")
        self.assertEqual(inst.dispense[0].duration.value, 1)
        self.assertEqual(inst.dispense[0].eye, "right")
        self.assertEqual(inst.dispense[0].note[0].text, "Shade treatment for extreme light sensitivity")
        self.assertEqual(inst.dispense[0].power, -2.75)
        self.assertEqual(inst.dispense[0].product.coding[0].code, "contact")
        self.assertEqual(inst.dispense[0].product.coding[0].system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.dispense[1].add, 1.75)
        self.assertEqual(inst.dispense[1].axis, 160)
        self.assertEqual(inst.dispense[1].backCurve, 8.7)
        self.assertEqual(inst.dispense[1].brand, "OphthaGuard")
        self.assertEqual(inst.dispense[1].color, "green")
        self.assertEqual(inst.dispense[1].cylinder, -3.5)
        self.assertEqual(inst.dispense[1].diameter, 14.0)
        self.assertEqual(inst.dispense[1].duration.code, "month")
        self.assertEqual(inst.dispense[1].duration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.dispense[1].duration.unit, "month")
        self.assertEqual(inst.dispense[1].duration.value, 1)
        self.assertEqual(inst.dispense[1].eye, "left")
        self.assertEqual(inst.dispense[1].note[0].text, "Shade treatment for extreme light sensitivity")
        self.assertEqual(inst.dispense[1].power, -2.75)
        self.assertEqual(inst.dispense[1].product.coding[0].code, "contact")
        self.assertEqual(inst.dispense[1].product.coding[0].system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.id, "33124")
        self.assertEqual(inst.identifier[0].system, "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value, "15014")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].code, "myopia")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].system, "http://samplevisionreasoncodes.com")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Sample Contract Lens prescription</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testVisionPrescription2(self):
        inst = self.instantiate_from("visionprescription-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a VisionPrescription instance")
        self.implVisionPrescription2(inst)
        
        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription2(inst2)
    
    def implVisionPrescription2(self, inst):
        self.assertEqual(inst.dateWritten.date, FHIRDate("2014-06-15").date)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(inst.dispense[0].add, 2.0)
        self.assertEqual(inst.dispense[0].base, "down")
        self.assertEqual(inst.dispense[0].eye, "right")
        self.assertEqual(inst.dispense[0].prism, 0.5)
        self.assertEqual(inst.dispense[0].product.coding[0].code, "lens")
        self.assertEqual(inst.dispense[0].product.coding[0].system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.dispense[0].sphere, -2.0)
        self.assertEqual(inst.dispense[1].add, 2.0)
        self.assertEqual(inst.dispense[1].axis, 180)
        self.assertEqual(inst.dispense[1].base, "up")
        self.assertEqual(inst.dispense[1].cylinder, -0.5)
        self.assertEqual(inst.dispense[1].eye, "left")
        self.assertEqual(inst.dispense[1].prism, 0.5)
        self.assertEqual(inst.dispense[1].product.coding[0].code, "lens")
        self.assertEqual(inst.dispense[1].product.coding[0].system, "http://hl7.org/fhir/ex-visionprescriptionproduct")
        self.assertEqual(inst.dispense[1].sphere, -1.0)
        self.assertEqual(inst.id, "33123")
        self.assertEqual(inst.identifier[0].system, "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value, "15013")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

