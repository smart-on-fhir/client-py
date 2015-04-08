#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import orderresponse
from fhirdate import FHIRDate


class OrderResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = orderresponse.OrderResponse(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testOrderResponse1(self):
        inst = self.instantiate_from("orderresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e359c10> instance")
    
        self.assertEqual(inst.date.date, FHIRDate("2012-12-28T13:10:56+11:00").date)
        self.assertEqual(inst.date.isostring, "2012-12-28T13:10:56+11:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.orderStatus, "completed")
        self.assertEqual(inst.text.div, "<div>Lab Report completed at 13:10 28-Dec 2012</div>")
        self.assertEqual(inst.text.status, "generated")

