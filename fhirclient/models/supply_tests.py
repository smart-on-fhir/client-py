#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import supply
from .fhirdate import FHIRDate


class SupplyTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Supply", js["resourceType"])
        return supply.Supply(js)
    
    def testSupply1(self):
        inst = self.instantiate_from("supply-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Supply instance")
        self.implSupply1(inst)
        
        js = inst.as_json()
        self.assertEqual("Supply", js["resourceType"])
        inst2 = supply.Supply(js)
        self.implSupply1(inst2)
    
    def implSupply1(self, inst):
        self.assertEqual(inst.dispense[0].identifier.system, "http://example.org/MM-Supply-Application")
        self.assertEqual(inst.dispense[0].identifier.use, "usual")
        self.assertEqual(inst.dispense[0].identifier.value, "12345")
        self.assertEqual(inst.dispense[0].quantity.code, "{each}")
        self.assertEqual(inst.dispense[0].quantity.system, "http://unitsofmeasure.org/")
        self.assertEqual(inst.dispense[0].quantity.units, "EA")
        self.assertEqual(inst.dispense[0].quantity.value, 1)
        self.assertEqual(inst.dispense[0].status, "dispensed")
        self.assertEqual(inst.dispense[0].type.coding[0].code, "device")
        self.assertEqual(inst.dispense[0].type.coding[0].display, "Device")
        self.assertTrue(inst.dispense[0].type.coding[0].primary)
        self.assertEqual(inst.dispense[0].type.coding[0].system, "http://hl7.org/fhir/supply-item-type")
        self.assertEqual(inst.dispense[0].whenHandedOver.date, FHIRDate("2014-12-06T15:42:15-08:00").date)
        self.assertEqual(inst.dispense[0].whenHandedOver.as_json(), "2014-12-06T15:42:15-08:00")
        self.assertEqual(inst.id, "102")
        self.assertEqual(inst.identifier.system, "http://example.org/OR-Supply-Application")
        self.assertEqual(inst.identifier.value, "23455")
        self.assertEqual(inst.kind.coding[0].code, "central")
        self.assertEqual(inst.kind.coding[0].display, "Central Supply")
        self.assertTrue(inst.kind.coding[0].primary)
        self.assertEqual(inst.kind.coding[0].system, "http://hl7.org/fhir/supply-type")
        self.assertEqual(inst.status, "received")
        self.assertEqual(inst.text.status, "generated")

