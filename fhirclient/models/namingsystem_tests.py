#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import namingsystem
from fhirdate import FHIRDate


class NamingSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = namingsystem.NamingSystem(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testNamingSystem1(self):
        inst = self.instantiate_from("namingsystem-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e33fed0> instance")
    
        self.assertEqual(inst.date.date, FHIRDate("2014-12-13").date)
        self.assertEqual(inst.date.isostring, "2014-12-13")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "SNOMED CT")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div>\n      \n      <p>\n        <b>SNOMED CT</b>\n      </p>\n      \n      <p> oid: 2.16.840.1.113883.6.96</p>\n      \n      <p> uri: http://snomed.info/sct</p>\n    \n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "codesystem")
        self.assertEqual(inst.uniqueId[0].type, "oid")
        self.assertEqual(inst.uniqueId[0].value, "2.16.840.1.113883.6.96")
        self.assertEqual(inst.uniqueId[1].type, "uri")
        self.assertEqual(inst.uniqueId[1].value, "http://snomed.info/sct")

