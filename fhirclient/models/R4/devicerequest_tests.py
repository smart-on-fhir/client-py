#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-10-12.
#  2019, SMART Health IT.

from __future__ import unicode_literals
import os
import io
import unittest
import json
from . import devicerequest
from .fhirdate import FHIRDate


class DeviceRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceRequest", js["resourceType"])
        return devicerequest.DeviceRequest(js)
    
    def testDeviceRequest1(self):
        inst = self.instantiate_from("devicerequest-example-insulinpump.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest1(inst2)
    
    def implDeviceRequest1(self, inst):
        self.assertEqual(inst.authoredOn.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.authoredOn.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.codeCodeableConcept.coding[0].code, "43148-6")
        self.assertEqual(inst.codeCodeableConcept.coding[0].system, "http://loinc.org")
        self.assertEqual(inst.codeCodeableConcept.text, "Insulin delivery device panel")
        self.assertEqual(inst.groupIdentifier.value, "ip_request1")
        self.assertEqual(inst.id, "insulinpump")
        self.assertEqual(inst.identifier[0].value, "ip_request1.1")
        self.assertEqual(inst.instantiatesCanonical[0], "http://motivemi.com/artifacts/PlanDefinition/low-suicide-risk-order-set")
        self.assertEqual(inst.intent, "instance-order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.note[0].text, "this is the right device brand and model")
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2013-05-08T09:33:27+07:00").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2013-05-08T09:33:27+07:00")
        self.assertEqual(inst.performerType.coding[0].display, "Qualified nurse")
        self.assertEqual(inst.performerType.text, "Nurse")
        self.assertEqual(inst.priority, "routine")
        self.assertEqual(inst.reasonCode[0].text, "gastroparesis")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
    
    def testDeviceRequest2(self):
        inst = self.instantiate_from("devicerequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceRequest instance")
        self.implDeviceRequest2(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceRequest", js["resourceType"])
        inst2 = devicerequest.DeviceRequest(js)
        self.implDeviceRequest2(inst2)
    
    def implDeviceRequest2(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.intent, "original-order")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "completed")
        self.assertEqual(inst.text.status, "generated")

