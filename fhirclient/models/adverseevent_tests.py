#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        self.assertEqual(inst.actuality, "actual")
        self.assertEqual(inst.category[0].coding[0].code, "product-use-error")
        self.assertEqual(inst.category[0].coding[0].display, "Product Use Error")
        self.assertEqual(inst.category[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/adverse-event-category")
        self.assertEqual(inst.date.date, FHIRDate("2017-01-29T12:34:56+00:00").date)
        self.assertEqual(inst.date.as_json(), "2017-01-29T12:34:56+00:00")
        self.assertEqual(inst.event.coding[0].code, "304386008")
        self.assertEqual(inst.event.coding[0].display, "O/E - itchy rash")
        self.assertEqual(inst.event.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.event.text, "This was a mild rash on the left forearm")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://acme.com/ids/patients/risks")
        self.assertEqual(inst.identifier.value, "49476534")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.seriousness.coding[0].code, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].display, "Non-serious")
        self.assertEqual(inst.seriousness.coding[0].system, "http://terminology.hl7.org/CodeSystem/adverse-event-seriousness")
        self.assertEqual(inst.severity.coding[0].code, "mild")
        self.assertEqual(inst.severity.coding[0].display, "Mild")
        self.assertEqual(inst.severity.coding[0].system, "http://terminology.hl7.org/CodeSystem/adverse-event-severity")
        self.assertEqual(inst.text.status, "generated")

