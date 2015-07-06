#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
from . import deviceuserequest
from .fhirdate import FHIRDate


class DeviceUseRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceUseRequest", js["resourceType"])
        return deviceuserequest.DeviceUseRequest(js)
    
    def testDeviceUseRequest1(self):
        inst = self.instantiate_from("deviceuserequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceUseRequest instance")
        self.implDeviceUseRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceUseRequest", js["resourceType"])
        inst2 = deviceuserequest.DeviceUseRequest(js)
        self.implDeviceUseRequest1(inst2)
    
    def implDeviceUseRequest1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.text.div, "<div>To be filled out at a later time</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testDeviceUseRequest2(self):
        inst = self.instantiate_from("deviceuserequest-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceUseRequest instance")
        self.implDeviceUseRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceUseRequest", js["resourceType"])
        inst2 = deviceuserequest.DeviceUseRequest(js)
        self.implDeviceUseRequest2(inst2)
    
    def implDeviceUseRequest2(self, inst):
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/deviceuserequest-reasonRejected")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "MEDPREC")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "medical precaution")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://hl7.org/fhir/v3/ActReason")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.status, "rejected")
        self.assertEqual(inst.text.div, "<div>To be filled out at a later time</div>")
        self.assertEqual(inst.text.status, "generated")

