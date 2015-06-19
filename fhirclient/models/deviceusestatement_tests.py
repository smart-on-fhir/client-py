#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-06-19.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import deviceusestatement
from fhirdate import FHIRDate


class DeviceUseStatementTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return deviceusestatement.DeviceUseStatement(js)
    
    def testDeviceUseStatement1(self):
        inst = self.instantiate_from("deviceusestatement-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceUseStatement instance")
        self.implDeviceUseStatement1(inst)
        inst2 = deviceusestatement.DeviceUseStatement(inst.as_json())
        self.implDeviceUseStatement1(inst2)
    
    def implDeviceUseStatement1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>To be filled out at a later time</div>")
        self.assertEqual(inst.text.status, "generated")

