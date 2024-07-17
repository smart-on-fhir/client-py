#  Generated from FHIR 4.0.1-9346c8cc45, SMART Health IT.

import os
import io
import unittest
import json
from fhirclient.models import visionprescription
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.fhirdatetime import FHIRDateTime
from fhirclient.models.fhirinstant import FHIRInstant
from fhirclient.models.fhirtime import FHIRTime


class VisionPrescriptionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.path.join(os.path.dirname(__file__), '..', 'data', 'examples')
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("VisionPrescription", js["resourceType"])
        return visionprescription.VisionPrescription(js)
    
    def testVisionPrescription1(self):
        inst = self.instantiate_from("visionprescription-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a VisionPrescription instance")
        self.implVisionPrescription1(inst)
        
        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription1(inst2)
    
    def implVisionPrescription1(self, inst):
        self.assertEqual(inst.created.datetime, FHIRDateTime("2014-06-15").datetime)
        self.assertEqual(inst.created.as_json(), "2014-06-15")
        self.assertEqual(inst.dateWritten.datetime, FHIRDateTime("2014-06-15").datetime)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(inst.id, "33123")
        self.assertEqual(inst.identifier[0].system, "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value, "15013")
        self.assertEqual(inst.lensSpecification[0].add, 2.0)
        self.assertEqual(inst.lensSpecification[0].eye, "right")
        self.assertEqual(inst.lensSpecification[0].prism[0].amount, 0.5)
        self.assertEqual(inst.lensSpecification[0].prism[0].base, "down")
        self.assertEqual(inst.lensSpecification[0].product.coding[0].code, "lens")
        self.assertEqual(inst.lensSpecification[0].product.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.lensSpecification[0].sphere, -2.0)
        self.assertEqual(inst.lensSpecification[1].add, 2.0)
        self.assertEqual(inst.lensSpecification[1].axis, 180)
        self.assertEqual(inst.lensSpecification[1].cylinder, -0.5)
        self.assertEqual(inst.lensSpecification[1].eye, "left")
        self.assertEqual(inst.lensSpecification[1].prism[0].amount, 0.5)
        self.assertEqual(inst.lensSpecification[1].prism[0].base, "up")
        self.assertEqual(inst.lensSpecification[1].product.coding[0].code, "lens")
        self.assertEqual(inst.lensSpecification[1].product.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.lensSpecification[1].sphere, -1.0)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testVisionPrescription2(self):
        inst = self.instantiate_from("visionprescription-example-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a VisionPrescription instance")
        self.implVisionPrescription2(inst)
        
        js = inst.as_json()
        self.assertEqual("VisionPrescription", js["resourceType"])
        inst2 = visionprescription.VisionPrescription(js)
        self.implVisionPrescription2(inst2)
    
    def implVisionPrescription2(self, inst):
        self.assertEqual(inst.created.datetime, FHIRDateTime("2014-06-15").datetime)
        self.assertEqual(inst.created.as_json(), "2014-06-15")
        self.assertEqual(inst.dateWritten.datetime, FHIRDateTime("2014-06-15").datetime)
        self.assertEqual(inst.dateWritten.as_json(), "2014-06-15")
        self.assertEqual(inst.id, "33124")
        self.assertEqual(inst.identifier[0].system, "http://www.happysight.com/prescription")
        self.assertEqual(inst.identifier[0].value, "15014")
        self.assertEqual(inst.lensSpecification[0].add, 1.75)
        self.assertEqual(inst.lensSpecification[0].axis, 160)
        self.assertEqual(inst.lensSpecification[0].backCurve, 8.7)
        self.assertEqual(inst.lensSpecification[0].brand, "OphthaGuard")
        self.assertEqual(inst.lensSpecification[0].color, "green")
        self.assertEqual(inst.lensSpecification[0].cylinder, -2.25)
        self.assertEqual(inst.lensSpecification[0].diameter, 14.0)
        self.assertEqual(inst.lensSpecification[0].duration.code, "month")
        self.assertEqual(inst.lensSpecification[0].duration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.lensSpecification[0].duration.unit, "month")
        self.assertEqual(inst.lensSpecification[0].duration.value, 1)
        self.assertEqual(inst.lensSpecification[0].eye, "right")
        self.assertEqual(inst.lensSpecification[0].note[0].text, "Shade treatment for extreme light sensitivity")
        self.assertEqual(inst.lensSpecification[0].power, -2.75)
        self.assertEqual(inst.lensSpecification[0].product.coding[0].code, "contact")
        self.assertEqual(inst.lensSpecification[0].product.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.lensSpecification[1].add, 1.75)
        self.assertEqual(inst.lensSpecification[1].axis, 160)
        self.assertEqual(inst.lensSpecification[1].backCurve, 8.7)
        self.assertEqual(inst.lensSpecification[1].brand, "OphthaGuard")
        self.assertEqual(inst.lensSpecification[1].color, "green")
        self.assertEqual(inst.lensSpecification[1].cylinder, -3.5)
        self.assertEqual(inst.lensSpecification[1].diameter, 14.0)
        self.assertEqual(inst.lensSpecification[1].duration.code, "month")
        self.assertEqual(inst.lensSpecification[1].duration.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.lensSpecification[1].duration.unit, "month")
        self.assertEqual(inst.lensSpecification[1].duration.value, 1)
        self.assertEqual(inst.lensSpecification[1].eye, "left")
        self.assertEqual(inst.lensSpecification[1].note[0].text, "Shade treatment for extreme light sensitivity")
        self.assertEqual(inst.lensSpecification[1].power, -2.75)
        self.assertEqual(inst.lensSpecification[1].product.coding[0].code, "contact")
        self.assertEqual(inst.lensSpecification[1].product.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-visionprescriptionproduct")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Sample Contract Lens prescription</div>")
        self.assertEqual(inst.text.status, "generated")

