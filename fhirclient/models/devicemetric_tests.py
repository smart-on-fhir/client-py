#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import devicemetric
from .fhirdate import FHIRDate


class DeviceMetricTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceMetric", js["resourceType"])
        return devicemetric.DeviceMetric(js)
    
    def testDeviceMetric1(self):
        inst = self.instantiate_from("devicemetric-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceMetric instance")
        self.implDeviceMetric1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceMetric", js["resourceType"])
        inst2 = devicemetric.DeviceMetric(js)
        self.implDeviceMetric1(inst2)
    
    def implDeviceMetric1(self, inst):
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

