#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import order
from .fhirdate import FHIRDate


class OrderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Order", js["resourceType"])
        return order.Order(js)
    
    def testOrder1(self):
        inst = self.instantiate_from("order-example-f201-physiotherapy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Order instance")
        self.implOrder1(inst)
        
        js = inst.as_json()
        self.assertEqual("Order", js["resourceType"])
        inst2 = order.Order(js)
        self.implOrder1(inst2)
    
    def implOrder1(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-03-05T12:00:00+01:00").date)
        self.assertEqual(inst.date.as_json(), "2013-03-05T12:00:00+01:00")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.reasonCodeableConcept.text, "It concerns a one-off order for consultation in order to evaluate the stairs walking ability of Roel.")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.when.code.coding[0].code, "394848005")
        self.assertEqual(inst.when.code.coding[0].display, "Normal priority")
        self.assertEqual(inst.when.code.coding[0].system, "http://snomed.info/sct")
    
    def testOrder2(self):
        inst = self.instantiate_from("order-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Order instance")
        self.implOrder2(inst)
        
        js = inst.as_json()
        self.assertEqual("Order", js["resourceType"])
        inst2 = order.Order(js)
        self.implOrder2(inst2)
    
    def implOrder2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-12-28T09:03:04+11:00").date)
        self.assertEqual(inst.date.as_json(), "2012-12-28T09:03:04+11:00")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.reasonCodeableConcept.text, "Standard admission testing")
        self.assertEqual(inst.text.div, "<div>Request for Prescription (on patient Donald DUCK @ Acme Healthcare, Inc. MR = 654321)</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.when.code.coding[0].code, "today")
        self.assertEqual(inst.when.code.coding[0].system, "http://acme.com/codes/request-priority")

