#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-04-08.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import devicecomponent
from fhirdate import FHIRDate


class DeviceComponentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = devicecomponent.DeviceComponent(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testDeviceComponent1(self):
        inst = self.instantiate_from("devicecomponent-example-prodspec.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c7950> instance")
    
        self.assertEqual(inst.id, "example-prodspec")
        self.assertEqual(inst.identifier.type.text, "Handle ID")
        self.assertEqual(inst.identifier.value, "0")
        self.assertEqual(inst.languageCode.coding[0].code, "en-US")
        self.assertEqual(inst.languageCode.coding[0].system, "http://tools.ietf.org/html/bcp47")
        self.assertEqual(inst.lastSystemChange.date, FHIRDate("2014-10-07T14:45:00Z").date)
        self.assertEqual(inst.lastSystemChange.isostring, "2014-10-07T14:45:00Z")
        self.assertEqual(inst.operationalStatus[0].coding[0].code, "0")
        self.assertEqual(inst.operationalStatus[0].coding[0].display, "disconnected")
        self.assertEqual(inst.operationalStatus[0].coding[0].system, "urn:std:iso:11073:10101")
        self.assertEqual(inst.productionSpecification[0].productionSpec, "xa-12324-b")
        self.assertEqual(inst.productionSpecification[0].specType.coding[0].code, "1")
        self.assertEqual(inst.productionSpecification[0].specType.coding[0].display, "Serial number")
        self.assertEqual(inst.productionSpecification[1].productionSpec, "1.1")
        self.assertEqual(inst.productionSpecification[1].specType.coding[0].code, "3")
        self.assertEqual(inst.productionSpecification[1].specType.coding[0].display, "Hardware version")
        self.assertEqual(inst.productionSpecification[2].productionSpec, "1.12")
        self.assertEqual(inst.productionSpecification[2].specType.coding[0].code, "4")
        self.assertEqual(inst.productionSpecification[2].specType.coding[0].display, "Software version")
        self.assertEqual(inst.productionSpecification[3].productionSpec, "1.0.23")
        self.assertEqual(inst.productionSpecification[3].specType.coding[0].code, "5")
        self.assertEqual(inst.productionSpecification[3].specType.coding[0].display, "Firmware version")
        self.assertEqual(inst.text.div, "<div>\n			\n      <p>Example of a simple MDS from a pulse oximeter containment tree</p>\n		\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "2000")
        self.assertEqual(inst.type.coding[0].display, "MDC_DEV_ANALY_SAT_O2_MDS")
        self.assertEqual(inst.type.coding[0].system, "urn:std:iso:11073:10101")
    
    def testDeviceComponent2(self):
        inst = self.instantiate_from("devicecomponent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a <fhirclass.FHIRClass object at 0x10e2c7950> instance")
    
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.type.text, "Handle ID")
        self.assertEqual(inst.identifier.value, "0")
        self.assertEqual(inst.languageCode.coding[0].code, "en-US")
        self.assertEqual(inst.languageCode.coding[0].system, "http://tools.ietf.org/html/bcp47")
        self.assertEqual(inst.lastSystemChange.date, FHIRDate("2014-10-07T14:45:00Z").date)
        self.assertEqual(inst.lastSystemChange.isostring, "2014-10-07T14:45:00Z")
        self.assertEqual(inst.operationalStatus[0].coding[0].code, "0")
        self.assertEqual(inst.operationalStatus[0].coding[0].display, "disconnected")
        self.assertEqual(inst.operationalStatus[0].coding[0].system, "urn:std:iso:11073:10101")
        self.assertEqual(inst.text.div, "<div>\n			\n      <p>Example of a simple MDS from a pulse oximeter containment tree</p>\n		\n    </div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "2000")
        self.assertEqual(inst.type.coding[0].display, "MDC_DEV_ANALY_SAT_O2_MDS")
        self.assertEqual(inst.type.coding[0].system, "urn:std:iso:11073:10101")

