#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import orderresponse
from .fhirdate import FHIRDate


class OrderResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("OrderResponse", js["resourceType"])
        return orderresponse.OrderResponse(js)
    
    def testOrderResponse1(self):
        inst = self.instantiate_from("orderresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a OrderResponse instance")
        self.implOrderResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("OrderResponse", js["resourceType"])
        inst2 = orderresponse.OrderResponse(js)
        self.implOrderResponse1(inst2)
    
    def implOrderResponse1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-12-28T13:10:56+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-12-28T13:10:56+11:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.orderStatus, "completed")
        self.assertEqual(inst.text.div, "<div>Lab Report completed at 13:10 28-Dec 2012</div>")
        self.assertEqual(inst.text.status, "generated")

