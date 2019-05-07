#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


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
        self.assertEqual(inst.calibration[0].state, "calibrated")
        self.assertEqual(inst.calibration[0].time.date, FHIRDate("2016-12-28T09:03:04-05:00").date)
        self.assertEqual(inst.calibration[0].time.as_json(), "2016-12-28T09:03:04-05:00")
        self.assertEqual(inst.calibration[0].type, "two-point")
        self.assertEqual(inst.category, "measurement")
        self.assertEqual(inst.color, "blue")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://goodcare.org/devicemetric/id")
        self.assertEqual(inst.identifier[0].value, "345675")
        self.assertEqual(inst.measurementPeriod.repeat.frequency, 1)
        self.assertEqual(inst.measurementPeriod.repeat.period, 1)
        self.assertEqual(inst.measurementPeriod.repeat.periodUnit, "s")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.operationalStatus, "on")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "150456")
        self.assertEqual(inst.type.coding[0].display, "MDC_PULS_OXIM_SAT_O2")
        self.assertEqual(inst.type.coding[0].system, "urn:iso:std:iso:11073:10101")
        self.assertEqual(inst.unit.coding[0].code, "262688")
        self.assertEqual(inst.unit.coding[0].display, "MDC_DIM_PERCENT")
        self.assertEqual(inst.unit.coding[0].system, "urn:iso:std:iso:11073:10101")

