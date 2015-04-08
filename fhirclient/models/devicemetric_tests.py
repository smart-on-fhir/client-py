#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import devicemetric
from fhirdate import FHIRDate


class DeviceMetricTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = devicemetric.DeviceMetric(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testDeviceMetric1(self):
        inst = self.instantiate_from("devicemetric-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2ca810> instance")
    
        self.assertEqual(inst.category, "measurement")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.system, "http://goodcare.org/devicemetric/id")
        self.assertEqual(inst.identifier.value, "345675")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "150456")
        self.assertEqual(inst.type.coding[0].display, "MDC_PULS_OXIM_SAT_O2")
        self.assertEqual(inst.type.coding[0].system, "https://rtmms.nist.gov")
        self.assertEqual(inst.unit.coding[0].code, "262688")
        self.assertEqual(inst.unit.coding[0].display, "MDC_DIM_PERCENT")
        self.assertEqual(inst.unit.coding[0].system, "https://rtmms.nist.gov")

