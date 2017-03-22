#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


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
        self.assertEqual(inst.identifier.value, "Order10284")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-12-31").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-12-31")
        self.assertEqual(inst.orderedItem.itemCodeableConcept.coding[0].code, "BlueTubes")
        self.assertEqual(inst.orderedItem.itemCodeableConcept.coding[0].display, "Blood collect tubes blue cap")
        self.assertEqual(inst.orderedItem.quantity.value, 10)
        self.assertEqual(inst.priority, "asap")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].code, "stock_low")
        self.assertEqual(inst.reasonCodeableConcept.coding[0].display, "Refill due to low stock")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

