#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


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
        self.assertEqual(inst.expirationDate.date, FHIRDate("2020-08-08").date)
        self.assertEqual(inst.expirationDate.as_json(), "2020-08-08")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "http:/goodhealthhospital/identifier/devices")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.manufactureDate.date, FHIRDate("2015-08-08").date)
        self.assertEqual(inst.manufactureDate.as_json(), "2015-08-08")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "25062003")
        self.assertEqual(inst.type.coding[0].display, "Feeding tube, device")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
    
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
        self.assertEqual(inst.contact[0].system, "url")
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
        inst = self.instantiate_from("device-example-udi1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice5(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice5(inst2)
    
    def implDevice5(self, inst):
        self.assertEqual(inst.expirationDate.date, FHIRDate("2014-11-20").date)
        self.assertEqual(inst.expirationDate.as_json(), "2014-11-20")
        self.assertEqual(inst.id, "example-udi1")
        self.assertEqual(inst.identifier[0].system, "http://acme.com/devices/pacemakers/octane/serial")
        self.assertEqual(inst.identifier[0].value, "1234-5678-90AB-CDEF")
        self.assertEqual(inst.identifier[1].type.coding[0].code, "SNO")
        self.assertEqual(inst.identifier[1].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[1].value, "10987654d321")
        self.assertEqual(inst.lotNumber, "7654321D")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.model, "PM/Octane 2014")
        self.assertEqual(inst.safety[0].coding[0].code, "mr-unsafe")
        self.assertEqual(inst.safety[0].coding[0].display, "MR Unsafe")
        self.assertEqual(inst.safety[0].coding[0].system, "urn:oid:2.16.840.1.113883.3.26.1.1")
        self.assertEqual(inst.safety[0].text, "MR Unsafe")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "468063009")
        self.assertEqual(inst.type.coding[0].display, "Coated femoral stem prosthesis, modular")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "Coated femoral stem prosthesis, modular")
        self.assertEqual(inst.udi.carrierAIDC, "XWQyMDExMDg1NzY3NDAwMjAxNzE3MTQxMTIwMTBOWUZVTDAx4oaUMjExOTI4MzfihpQ3MTNBMUIyQzNENEU1RjZH")
        self.assertEqual(inst.udi.carrierHRF, "{01}00844588003288{17}141120{10}7654321D{21}10987654d321")
        self.assertEqual(inst.udi.deviceIdentifier, "00844588003288")
        self.assertEqual(inst.udi.entryType, "barcode")
        self.assertEqual(inst.udi.issuer, "http://hl7.org/fhir/NamingSystem/gs1")
        self.assertEqual(inst.udi.jurisdiction, "http://hl7.org/fhir/NamingSystem/fda-udi")
        self.assertEqual(inst.udi.name, "FHIR® Hip System")
    
    def testDevice6(self):
        inst = self.instantiate_from("device-example-udi2.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice6(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice6(inst2)
    
    def implDevice6(self, inst):
        self.assertEqual(inst.expirationDate.date, FHIRDate("2014-02-01").date)
        self.assertEqual(inst.expirationDate.as_json(), "2014-02-01")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/device-din")
        self.assertEqual(inst.extension[0].valueIdentifier.system, "http://hl7.org/fhir/NamingSystem/iccbba-din")
        self.assertEqual(inst.extension[0].valueIdentifier.value, "A99971312345600")
        self.assertEqual(inst.id, "example-udi2")
        self.assertEqual(inst.manufactureDate.date, FHIRDate("2013-02-01").date)
        self.assertEqual(inst.manufactureDate.as_json(), "2013-02-01")
        self.assertEqual(inst.manufacturer, "Acme Devices, Inc")
        self.assertEqual(inst.status, "inactive")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.udi.deviceIdentifier, "A9999XYZ100T0474")
        self.assertEqual(inst.udi.issuer, "http://hl7.org/fhir/NamingSystem/iccbba-other")
        self.assertEqual(inst.udi.jurisdiction, "http://hl7.org/fhir/NamingSystem/fda-udi")
        self.assertEqual(inst.udi.name, "Bone,Putty Demineralized")
    
    def testDevice7(self):
        inst = self.instantiate_from("device-example-udi3.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice7(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice7(inst2)
    
    def implDevice7(self, inst):
        self.assertEqual(inst.expirationDate.date, FHIRDate("2020-02-02").date)
        self.assertEqual(inst.expirationDate.as_json(), "2020-02-02")
        self.assertEqual(inst.id, "example-udi3")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "SNO")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://hl7.org/fhir/identifier-type")
        self.assertEqual(inst.identifier[0].value, "XYZ456789012345678")
        self.assertEqual(inst.lotNumber, "LOT123456789012345")
        self.assertEqual(inst.manufactureDate.date, FHIRDate("2013-02-02").date)
        self.assertEqual(inst.manufactureDate.as_json(), "2013-02-02")
        self.assertEqual(inst.manufacturer, "GlobalMed, Inc")
        self.assertEqual(inst.model, "Ultra Implantable")
        self.assertEqual(inst.status, "inactive")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.udi.carrierHRF, "+H123PARTNO1234567890120/$$420020216LOT123456789012345/SXYZ456789012345678/16D20130202C")
        self.assertEqual(inst.udi.entryType, "manual")
        self.assertEqual(inst.udi.issuer, "http://hl7.org/fhir/NamingSystem/hibcc")
        self.assertEqual(inst.udi.jurisdiction, "http://hl7.org/fhir/NamingSystem/fda-udi")
        self.assertEqual(inst.udi.name, "FHIR® Ulltra Implantable")
    
    def testDevice8(self):
        inst = self.instantiate_from("device-example-udi4.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice8(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice8(inst2)
    
    def implDevice8(self, inst):
        self.assertEqual(inst.id, "example-udi4")
        self.assertEqual(inst.lotNumber, "RZ12345678")
        self.assertEqual(inst.manufacturer, "GlobalMed, Inc")
        self.assertEqual(inst.status, "inactive")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.udi.carrierHRF, "=)1TE123456A&)RZ12345678")
        self.assertEqual(inst.udi.issuer, "http://hl7.org/fhir/NamingSystem/iccbba-blood")
        self.assertEqual(inst.udi.jurisdiction, "http://hl7.org/fhir/NamingSystem/fda-udi")
    
    def testDevice9(self):
        inst = self.instantiate_from("device-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Device instance")
        self.implDevice9(inst)
        
        js = inst.as_json()
        self.assertEqual("Device", js["resourceType"])
        inst2 = device.Device(js)
        self.implDevice9(inst2)
    
    def implDevice9(self, inst):
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
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "86184003")
        self.assertEqual(inst.type.coding[0].display, "Electrocardiographic monitor and recorder")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.type.text, "ECG")

