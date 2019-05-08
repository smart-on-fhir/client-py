#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import medicinalproductmanufactured
from .fhirdate import FHIRDate


class MedicinalProductManufacturedTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MedicinalProductManufactured", js["resourceType"])
        return medicinalproductmanufactured.MedicinalProductManufactured(js)
    
    def testMedicinalProductManufactured1(self):
        inst = self.instantiate_from("medicinalproductmanufactured-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MedicinalProductManufactured instance")
        self.implMedicinalProductManufactured1(inst)
        
        js = inst.as_json()
        self.assertEqual("MedicinalProductManufactured", js["resourceType"])
        inst2 = medicinalproductmanufactured.MedicinalProductManufactured(js)
        self.implMedicinalProductManufactured1(inst2)
    
    def implMedicinalProductManufactured1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.manufacturedDoseForm.coding[0].code, "Film-coatedtablet")
        self.assertEqual(inst.manufacturedDoseForm.coding[0].system, "http://ema.europa.eu/example/manufactureddoseform")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.physicalCharacteristics.color[0], "Pink")
        self.assertEqual(inst.physicalCharacteristics.imprint[0], "894")
        self.assertEqual(inst.physicalCharacteristics.shape, "Oval")
        self.assertEqual(inst.quantity.unit, "1")
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.unitOfPresentation.coding[0].code, "Tablet")
        self.assertEqual(inst.unitOfPresentation.coding[0].system, "http://ema.europa.eu/example/unitofpresentation")

