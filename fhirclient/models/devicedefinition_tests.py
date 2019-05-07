#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import devicedefinition
from .fhirdate import FHIRDate


class DeviceDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceDefinition", js["resourceType"])
        return devicedefinition.DeviceDefinition(js)
    
    def testDeviceDefinition1(self):
        inst = self.instantiate_from("devicedefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceDefinition instance")
        self.implDeviceDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceDefinition", js["resourceType"])
        inst2 = devicedefinition.DeviceDefinition(js)
        self.implDeviceDefinition1(inst2)
    
    def implDeviceDefinition1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].value, "0")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p><p><b>identifier</b>: 0</p></div>")
        self.assertEqual(inst.text.status, "generated")

