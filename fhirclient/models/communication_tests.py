#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import communication
from .fhirdate import FHIRDate


class CommunicationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Communication", js["resourceType"])
        return communication.Communication(js)
    
    def testCommunication1(self):
        inst = self.instantiate_from("communication-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Communication instance")
        self.implCommunication1(inst)
        
        js = inst.as_json()
        self.assertEqual("Communication", js["resourceType"])
        inst2 = communication.Communication(js)
        self.implCommunication1(inst2)
    
    def implCommunication1(self, inst):
        self.assertEqual(inst.category.coding[0].code, "Alert")
        self.assertEqual(inst.category.coding[0].system, "http://acme.org/messagetypes")
        self.assertEqual(inst.category.text, "Alert")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.3.4.5.6.7")
        self.assertEqual(inst.identifier[0].type.text, "Paging System")
        self.assertEqual(inst.identifier[0].value, "2345678901")
        self.assertEqual(inst.payload[0].contentString, "Patient 1 has a very high serum potassium value (7.2 mmol/L on 2014-Dec-12 at 5:55 pm)")
        self.assertEqual(inst.sent.date, FHIRDate("2014-12-12T18:01:10-08:00").date)
        self.assertEqual(inst.sent.as_json(), "2014-12-12T18:01:10-08:00")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.div, "<div>Patient has very high serum potassium</div>")
        self.assertEqual(inst.text.status, "generated")

