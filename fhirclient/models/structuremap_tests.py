#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.6.0.9663 on 2016-08-31.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import structuremap
from .fhirdate import FHIRDate


class StructureMapTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("StructureMap", js["resourceType"])
        return structuremap.StructureMap(js)
    
    def testStructureMap1(self):
        inst = self.instantiate_from("structuremap-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureMap instance")
        self.implStructureMap1(inst)
        
        js = inst.as_json()
        self.assertEqual("StructureMap", js["resourceType"])
        inst2 = structuremap.StructureMap(js)
        self.implStructureMap1(inst2)
    
    def implStructureMap1(self, inst):
        self.assertEqual(inst.group[0].input[0].mode, "source")
        self.assertEqual(inst.group[0].input[0].name, "test")
        self.assertEqual(inst.group[0].name, "Examples")
        self.assertEqual(inst.group[0].rule[0].name, "rule1")
        self.assertEqual(inst.group[0].rule[0].source[0].context, "test")
        self.assertEqual(inst.group[0].rule[0].source[0].contextType, "variable")
        self.assertEqual(inst.group[0].rule[0].source[0].element, "test")
        self.assertTrue(inst.group[0].rule[0].source[0].required)
        self.assertEqual(inst.group[0].rule[0].source[0].variable, "t")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "Example Map")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/StructureMap/example")

