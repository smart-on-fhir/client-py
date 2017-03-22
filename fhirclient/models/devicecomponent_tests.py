#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import devicecomponent
from .fhirdate import FHIRDate


class DeviceComponentTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("DeviceComponent", js["resourceType"])
        return devicecomponent.DeviceComponent(js)
    
    def testDeviceComponent1(self):
        inst = self.instantiate_from("devicecomponent-example-prodspec.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceComponent instance")
        self.implDeviceComponent1(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceComponent", js["resourceType"])
        inst2 = devicecomponent.DeviceComponent(js)
        self.implDeviceComponent1(inst2)
    
    def implDeviceComponent1(self, inst):
        self.assertEqual(inst.id, "example-prodspec")
        self.assertEqual(inst.identifier.value, "789123")
        self.assertEqual(inst.languageCode.coding[0].code, "en-US")
        self.assertEqual(inst.languageCode.coding[0].system, "http://tools.ietf.org/html/bcp47")
        self.assertEqual(inst.lastSystemChange.date, FHIRDate("2014-10-07T14:45:00Z").date)
        self.assertEqual(inst.lastSystemChange.as_json(), "2014-10-07T14:45:00Z")
        self.assertEqual(inst.operationalStatus[0].coding[0].code, "off")
        self.assertEqual(inst.operationalStatus[0].coding[0].display, "Off")
        self.assertEqual(inst.productionSpecification[0].productionSpec, "xa-12324-b")
        self.assertEqual(inst.productionSpecification[0].specType.coding[0].code, "serial-number")
        self.assertEqual(inst.productionSpecification[0].specType.coding[0].display, "Serial number")
        self.assertEqual(inst.productionSpecification[1].productionSpec, "1.1")
        self.assertEqual(inst.productionSpecification[1].specType.coding[0].code, "hardware-revision")
        self.assertEqual(inst.productionSpecification[1].specType.coding[0].display, "Hardware Revision")
        self.assertEqual(inst.productionSpecification[2].productionSpec, "1.12")
        self.assertEqual(inst.productionSpecification[2].specType.coding[0].code, "software-revision")
        self.assertEqual(inst.productionSpecification[2].specType.coding[0].display, "Software Revision")
        self.assertEqual(inst.productionSpecification[3].productionSpec, "1.0.23")
        self.assertEqual(inst.productionSpecification[3].specType.coding[0].code, "firmware-revision")
        self.assertEqual(inst.productionSpecification[3].specType.coding[0].display, "Firmware Revision")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "2000")
        self.assertEqual(inst.type.coding[0].display, "MDC_DEV_ANALY_SAT_O2_MDS")
        self.assertEqual(inst.type.coding[0].system, "urn:iso:std:iso:11073:10101")
    
    def testDeviceComponent2(self):
        inst = self.instantiate_from("devicecomponent-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a DeviceComponent instance")
        self.implDeviceComponent2(inst)
        
        js = inst.as_json()
        self.assertEqual("DeviceComponent", js["resourceType"])
        inst2 = devicecomponent.DeviceComponent(js)
        self.implDeviceComponent2(inst2)
    
    def implDeviceComponent2(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier.value, "0")
        self.assertEqual(inst.languageCode.coding[0].code, "en-US")
        self.assertEqual(inst.languageCode.coding[0].system, "http://tools.ietf.org/html/bcp47")
        self.assertEqual(inst.lastSystemChange.date, FHIRDate("2014-10-07T14:45:00Z").date)
        self.assertEqual(inst.lastSystemChange.as_json(), "2014-10-07T14:45:00Z")
        self.assertEqual(inst.measurementPrinciple, "optical")
        self.assertEqual(inst.operationalStatus[0].coding[0].code, "off")
        self.assertEqual(inst.operationalStatus[0].coding[0].display, "Off")
        self.assertEqual(inst.operationalStatus[0].coding[0].system, "urn:iso:std:iso:11073:10101")
        self.assertEqual(inst.parameterGroup.coding[0].code, "miscellaneous")
        self.assertEqual(inst.parameterGroup.coding[0].display, "Miscellaneous Parameter Group")
        self.assertEqual(inst.parameterGroup.coding[0].system, "urn:iso:std:iso:11073:10101")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "2000")
        self.assertEqual(inst.type.coding[0].display, "MDC_DEV_ANALY_SAT_O2_MDS")
        self.assertEqual(inst.type.coding[0].system, "urn:iso:std:iso:11073:10101")

