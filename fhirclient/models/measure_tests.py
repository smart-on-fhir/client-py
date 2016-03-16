#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 on 2016-03-16.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import measure
from .fhirdate import FHIRDate


class MeasureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Measure", js["resourceType"])
        return measure.Measure(js)
    
    def testMeasure1(self):
        inst = self.instantiate_from("measure-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure1(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure1(inst2)
    
    def implMeasure1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

