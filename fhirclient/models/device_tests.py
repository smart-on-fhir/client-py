#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from device import Device
from fhirdate import FHIRDate


class DeviceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = Device(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testDevice1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/device-example-f001-feedingtube.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
    
        self.assertEqual(inst.text.div, "<div>\n      <p>\n        <b>Generated Narrative</b>\n      </p>\n      <p>\n        <b>type</b>: \n        <span title=\"Codes: {http://snomed.info/sct 25062003}\">Feeding tube, device</span>\n      </p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "25062003")
        self.assertEqual(inst.type.coding[0].display, "Feeding tube, device")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
    def testDevice2(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/device-example-ihe-pcd.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
    
        self.assertEqual(inst.identifier[0].label, "serialNumber")
        self.assertEqual(inst.identifier[0].value, "AMID-123-456")
        self.assertEqual(inst.lotNumber, "12345")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "A.1.1")
        self.assertEqual(inst.text.div, "<div>\n      <p>Acme Patient Monitor</p>\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "Vital Signs Monitor")

