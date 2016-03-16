#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.3.0.7854 on 2016-03-16.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import measurereport
from .fhirdate import FHIRDate


class MeasureReportTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("MeasureReport", js["resourceType"])
        return measurereport.MeasureReport(js)
    
    def testMeasureReport1(self):
        inst = self.instantiate_from("measurereport-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a MeasureReport instance")
        self.implMeasureReport1(inst)
        
        js = inst.as_json()
        self.assertEqual("MeasureReport", js["resourceType"])
        inst2 = measurereport.MeasureReport(js)
        self.implMeasureReport1(inst2)
    
    def implMeasureReport1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>[Put rendering here]</div>")
        self.assertEqual(inst.text.status, "generated")

