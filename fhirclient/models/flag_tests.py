#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import flag
from .fhirdate import FHIRDate


class FlagTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Flag", js["resourceType"])
        return flag.Flag(js)
    
    def testFlag1(self):
        inst = self.instantiate_from("flag-example-encounter.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag1(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag1(inst2)
    
    def implFlag1(self, inst):
        self.assertEqual(inst.category.coding[0].code, "infection")
        self.assertEqual(inst.category.coding[0].display, "Infection Control Level")
        self.assertEqual(inst.category.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.code.coding[0].code, "l3")
        self.assertEqual(inst.code.coding[0].display, "Follow Level 3 Protocol")
        self.assertEqual(inst.code.coding[0].system, "http://example.org/local/if1")
        self.assertEqual(inst.id, "example-encounter")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Follow Infection Control Level 3 Protocol</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testFlag2(self):
        inst = self.instantiate_from("flag-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag2(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag2(inst2)
    
    def implFlag2(self, inst):
        self.assertEqual(inst.category.coding[0].code, "admin")
        self.assertEqual(inst.category.coding[0].display, "Admin")
        self.assertEqual(inst.category.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.category.text, "admin")
        self.assertEqual(inst.code.coding[0].code, "bigdog")
        self.assertEqual(inst.code.coding[0].display, "Big dog")
        self.assertEqual(inst.code.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.code.text, "Patient has a big dog at his home. Always always wear a suit of armor or take other active counter-measures")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.period.end.date, FHIRDate("2016-12-01").date)
        self.assertEqual(inst.period.end.as_json(), "2016-12-01")
        self.assertEqual(inst.period.start.date, FHIRDate("2015-01-17").date)
        self.assertEqual(inst.period.start.as_json(), "2015-01-17")
        self.assertEqual(inst.status, "inactive")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Large Dog warning for Peter Patient</div>")
        self.assertEqual(inst.text.status, "generated")

