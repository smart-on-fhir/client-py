#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-10-12.
#  2019, SMART Health IT.

from __future__ import unicode_literals
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
        inst = self.instantiate_from("flag-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag1(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag1(inst2)
    
    def implFlag1(self, inst):
        self.assertEqual(inst.category.coding[0].code, "admin")
        self.assertEqual(inst.category.coding[0].display, "Admin")
        self.assertEqual(inst.category.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.category.text, "admin")
        self.assertEqual(inst.code.coding[0].code, "bigdog")
        self.assertEqual(inst.code.coding[0].display, "Big dog")
        self.assertEqual(inst.code.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.code.text, "Patient has a big dog at his home. Always always wear a suit of armor or take other active counter-measures")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div>Large Dog warning for Peter Patient</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testFlag2(self):
        inst = self.instantiate_from("flag-example-encounter.json")
        self.assertIsNotNone(inst, "Must have instantiated a Flag instance")
        self.implFlag2(inst)
        
        js = inst.as_json()
        self.assertEqual("Flag", js["resourceType"])
        inst2 = flag.Flag(js)
        self.implFlag2(inst2)
    
    def implFlag2(self, inst):
        self.assertEqual(inst.category.coding[0].code, "infection")
        self.assertEqual(inst.category.coding[0].display, "Infection Control Level")
        self.assertEqual(inst.category.coding[0].system, "http://example.org/local")
        self.assertEqual(inst.code.coding[0].code, "l3")
        self.assertEqual(inst.code.coding[0].display, "Follow Level 3 Protocol")
        self.assertEqual(inst.code.coding[0].system, "http://example.org/local/if1")
        self.assertEqual(inst.id, "example-encounter")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div>Follow Infection Control Level 3 Protocol</div>")
        self.assertEqual(inst.text.status, "generated")

