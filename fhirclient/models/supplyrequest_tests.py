#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import supplyrequest
from .fhirdate import FHIRDate


class SupplyRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("SupplyRequest", js["resourceType"])
        return supplyrequest.SupplyRequest(js)
    
    def testSupplyRequest1(self):
        inst = self.instantiate_from("supplyrequest-example-simpleorder.json")
        self.assertIsNotNone(inst, "Must have instantiated a SupplyRequest instance")
        self.implSupplyRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("SupplyRequest", js["resourceType"])
        inst2 = supplyrequest.SupplyRequest(js)
        self.implSupplyRequest1(inst2)
    
    def implSupplyRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.authoredOn.as_json(), "2016-12-31")
        self.assertEqual(inst.category.coding[0].code, "central")
        self.assertEqual(inst.category.coding[0].display, "Central Stock Resupply")
        self.assertEqual(inst.id, "simpleorder")
        self.assertEqual(inst.identifier[0].value, "Order10284")
        self.assertEqual(inst.itemCodeableConcept.coding[0].code, "BlueTubes")
        self.assertEqual(inst.itemCodeableConcept.coding[0].display, "Blood collect tubes blue cap")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(inst.priority, "asap")
        self.assertEqual(inst.quantity.value, 10)
        self.assertEqual(inst.reasonCode[0].coding[0].code, "stock_low")
        self.assertEqual(inst.reasonCode[0].coding[0].display, "Refill due to low stock")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

