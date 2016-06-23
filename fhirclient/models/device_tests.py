#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2016-06-23.
#  2016, SMART Health IT.


import os
import io
import unittest
import json
from . import device
from .fhirdate import FHIRDate


class DeviceTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Device", js["resourceType"])
        return device.Device(js)
    
    def testDevice1(self):
        inst = self.instantiate_from("device-example-f001-feedingtube.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice1(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice1(inst2)
    
    def implDevice1(self, inst):
        self.assertEqual(inst.expiry.date, FHIRDate("2020-08-08").date)
        self.assertEqual(inst.expiry.as_json(), "2020-08-08")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http:/goodhealthhospital/identifier/devices")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.manufactureDate.date, FHIRDate("2015-08-08").date)
        self.assertEqual(inst.manufactureDate.as_json(), "2015-08-08")
        self.assertEqual(inst.status, "available")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "25062003")
        self.assertEqual(inst.type.coding[0].display, "Feeding tube, device")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.udi, "(01)00000123000017(10)ABC123(17)120415")
    
    def testDevice2(self):
        inst = self.instantiate_from("device-example-ihe-pcd.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice2(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice2(inst2)
    
    def implDevice2(self, inst):
        self.assertEqual(inst.id, "ihe-pcd")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "SNO")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].type.text, "Serial Number")
        self.assertEqual(inst.identifier[0].value, "AMID-123-456")
        self.assertEqual(inst.lotNumber, "12345")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "A.1.1")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "Vital Signs Monitor")
    
    def testDevice3(self):
        inst = self.instantiate_from("device-example-pacemaker.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice3(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice3(inst2)
    
    def implDevice3(self, inst):
        self.assertEqual(inst.contact[0].system, "phone")
        self.assertEqual(inst.contact[0].value, "ext 4352")
        self.assertEqual(inst.id, "example-pacemaker")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/devices/pacemakers/octane/serial")
        self.assertEqual(inst.identifier[0].value, "1234-5678-90AB-CDEF")
        self.assertEqual(inst.lotNumber, "1234-5678")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "PM/Octane 2014")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "octane2014")
        self.assertEqual(inst.type.coding[0].display, "Performance pace maker for high octane patients")
        self.assertEqual(inst.type.coding[0].system, "http://acme.com/devices")
    
    def testDevice4(self):
        inst = self.instantiate_from("device-example-software.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice4(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice4(inst2)
    
    def implDevice4(self, inst):
        self.assertEqual(inst.contact[0].system, "other")
        self.assertEqual(inst.contact[0].value, "http://acme.com")
        self.assertEqual(inst.id, "software")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/ehr/client-ids")
        self.assertEqual(inst.identifier[0].value, "goodhealth")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.text, "EHR")
        self.assertEqual(inst.url, "http://acme.com/goodhealth/ehr/")
        self.assertEqual(inst.version, "10.23-23423")
    
    def testDevice5(self):
        inst = self.instantiate_from("device-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice5(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice5(inst2)
    
    def implDevice5(self, inst):
        self.assertEqual(inst.contact[0].system, "phone")
        self.assertEqual(inst.contact[0].value, "ext 4352")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://goodcare.org/devices/id")
        self.assertEqual(inst.identifier[0].value, "345675")
        self.assertEqual(inst.identifier[1].type.coding[0].code, "SNO")
        self.assertEqual(inst.identifier[1].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[1].type.text, "Serial Number")
        self.assertEqual(inst.identifier[1].value, "AMID-342135-8464")
        self.assertEqual(inst.lotNumber, "43453424")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "AB 45-J")
        self.assertEqual(inst.note[0].text, "QA Checked")
        self.assertEqual(inst.note[0].time.date, FHIRDate("2015-06-28T14:03:32+10:00").date)
        self.assertEqual(inst.note[0].time.as_json(), "2015-06-28T14:03:32+10:00")
        self.assertEqual(inst.status, "available")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "86184003")
        self.assertEqual(inst.type.coding[0].display, "Electrocardiographic monitor and recorder")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "ECG")

