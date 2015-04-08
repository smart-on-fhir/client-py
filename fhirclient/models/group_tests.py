#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import group
from fhirdate import FHIRDate


class GroupTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = group.Group(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testGroup1(self):
        inst = self.instantiate_from("group-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2fe390> instance")
    
        self.assertTrue(inst.actual)
        self.assertEqual(inst.characteristic[0].code.text, "gender")
        self.assertFalse(inst.characteristic[0].exclude)
        self.assertEqual(inst.characteristic[0].valueCodeableConcept.text, "mixed")
        self.assertEqual(inst.characteristic[1].code.text, "owner")
        self.assertFalse(inst.characteristic[1].exclude)
        self.assertEqual(inst.characteristic[1].valueCodeableConcept.text, "John Smith")
        self.assertEqual(inst.code.text, "Horse")
        self.assertEqual(inst.id, "101")
        self.assertEqual(inst.name, "John's herd")
        self.assertEqual(inst.quantity, 25)
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>Herd of 25 horses</p>\n      \n      <p>Gender: mixed</p>\n      \n      <p>Owner: John Smith</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "additional")
        self.assertEqual(inst.type, "animal")

