#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from list import List
from fhirdate import FHIRDate


class ListTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = List(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testList1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/list-example-empty.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
    
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2012-11-26T07:30:23+11:00").date)
        self.assertEqual(inst.date.isostring, "2012-11-26T07:30:23+11:00")
        self.assertEqual(inst.emptyReason.coding[0].code, "nil known")
        self.assertEqual(inst.emptyReason.coding[0].display, "Nil Known")
        self.assertEqual(inst.emptyReason.coding[0].system, "http://hl7.org/fhir/special-values")
        self.assertEqual(inst.emptyReason.text, "The patient is not on any medications")
        self.assertEqual(inst.mode, "snapshot")
        self.assertEqual(inst.source.reference, "Patient/example")
        self.assertEqual(inst.text.div, "<div>\n      <p>The patient is not on any medications</p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testList2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/list-example-medlist.json")
        self.assertIsNotNone(inst, "Must have instantiated a List instance")
    
        self.assertEqual(inst.code.coding[0].code, "182836005")
        self.assertEqual(inst.code.coding[0].display, "Review of medication")
        self.assertEqual(inst.code.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.code.text, "Medication Review")
        self.assertEqual(inst.date.date, FHIRDate("2013-11-20T23:10:23+11:00").date)
        self.assertEqual(inst.date.isostring, "2013-11-20T23:10:23+11:00")
        self.assertEqual(inst.entry[0].flag[0].coding[0].code, "02")
        self.assertEqual(inst.entry[0].flag[0].coding[0].display, "Prescribed")
        self.assertEqual(inst.entry[0].flag[0].coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertEqual(inst.entry[0].item.display, "hydroxocobalamin")
        self.assertTrue(inst.entry[1].deleted)
        self.assertEqual(inst.entry[1].flag[0].coding[0].code, "02")
        self.assertEqual(inst.entry[1].flag[0].coding[0].display, "Cancelled")
        self.assertEqual(inst.entry[1].flag[0].coding[0].system, "http://nehta.gov.au/codes/medications/changetype")
        self.assertEqual(inst.entry[1].item.display, "Morphine Sulfate")
        self.assertEqual(inst.mode, "changes")
        self.assertEqual(inst.source.reference, "Patient/example")
        self.assertEqual(inst.text.div, "<div>\n      <p>The patient is not on any medications</p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")

