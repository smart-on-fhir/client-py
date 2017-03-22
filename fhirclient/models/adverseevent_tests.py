#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import adverseevent
from .fhirdate import FHIRDate


class AdverseEventTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("AdverseEvent", js["resourceType"])
        return adverseevent.AdverseEvent(js)
    
    def testAdverseEvent1(self):
        inst = self.instantiate_from("adverseevent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a AdverseEvent instance")
        self.implAdverseEvent1(inst)
        
        js = inst.as_json()
        self.assertEqual("AdverseEvent", js["resourceType"])
        inst2 = adverseevent.AdverseEvent(js)
        self.implAdverseEvent1(inst2)
    
    def implAdverseEvent1(self, inst):
        self.assertEqual(inst.category, "AE")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.description, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.seriousness.coding[0].code, "Mild")
        self.assertEqual(inst.seriousness.coding[0].display, "Mild")
        self.assertEqual(inst.seriousness.coding[0].system, "http://hl7.org/fhir/adverse-event-seriousness")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "304386008")
        self.assertEqual(inst.type.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")

