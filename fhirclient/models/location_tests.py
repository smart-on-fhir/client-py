#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import location
from .fhirdate import FHIRDate


class LocationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Location", js["resourceType"])
        return location.Location(js)
    
    def testLocation1(self):
        inst = self.instantiate_from("location-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation1(inst2)
    
    def implLocation1(self, inst):
        self.assertEqual(inst.address.city, "Den Burg")
        self.assertEqual(inst.address.country, "NLD")
        self.assertEqual(inst.address.line[0], "Galapagosweg 91, Building A")
        self.assertEqual(inst.address.postalCode, "9105 PZ")
        self.assertEqual(inst.address.use, "work")
        self.assertEqual(inst.alias[0], "BU MC, SW, F2")
        self.assertEqual(inst.alias[1], "Burgers University Medical Center, South Wing, second floor")
        self.assertEqual(inst.description, "Second floor of the Old South Wing, formerly in use by Psychiatry")
        self.assertEqual(inst.id, "1")
        self.assertEqual(inst.identifier[0].value, "B1-S.F2")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "instance")
        self.assertEqual(inst.name, "South Wing, second floor")
        self.assertEqual(inst.physicalType.coding[0].code, "wi")
        self.assertEqual(inst.physicalType.coding[0].display, "Wing")
        self.assertEqual(inst.physicalType.coding[0].system, "http://terminology.hl7.org/CodeSystem/location-physical-type")
        self.assertEqual(inst.position.altitude, 0)
        self.assertEqual(inst.position.latitude, 42.25475478)
        self.assertEqual(inst.position.longitude, -83.6945691)
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "2328")
        self.assertEqual(inst.telecom[1].system, "fax")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "2329")
        self.assertEqual(inst.telecom[2].system, "email")
        self.assertEqual(inst.telecom[2].value, "second wing admissions")
        self.assertEqual(inst.telecom[3].system, "url")
        self.assertEqual(inst.telecom[3].use, "work")
        self.assertEqual(inst.telecom[3].value, "http://sampleorg.com/southwing")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Burgers UMC, South Wing, second floor</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testLocation2(self):
        inst = self.instantiate_from("location-example-room.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation2(inst2)
    
    def implLocation2(self, inst):
        self.assertEqual(inst.alias[0], "South Wing OR 5")
        self.assertEqual(inst.alias[1], "Main Wing OR 2")
        self.assertEqual(inst.description, "Old South Wing, Neuro Radiology Operation Room 1 on second floor")
        self.assertEqual(inst.id, "2")
        self.assertEqual(inst.identifier[0].value, "B1-S.F2.1.00")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "instance")
        self.assertEqual(inst.name, "South Wing Neuro OR 1")
        self.assertEqual(inst.operationalStatus.code, "H")
        self.assertEqual(inst.operationalStatus.display, "Housekeeping")
        self.assertEqual(inst.operationalStatus.system, "http://terminology.hl7.org/CodeSystem/v2-0116")
        self.assertEqual(inst.physicalType.coding[0].code, "ro")
        self.assertEqual(inst.physicalType.coding[0].display, "Room")
        self.assertEqual(inst.physicalType.coding[0].system, "http://terminology.hl7.org/CodeSystem/location-physical-type")
        self.assertEqual(inst.status, "suspended")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "2329")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Burgers UMC, South Wing, second floor, Neuro Radiology Operation Room 1</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "RNEU")
        self.assertEqual(inst.type[0].coding[0].display, "Neuroradiology unit")
        self.assertEqual(inst.type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
    
    def testLocation3(self):
        inst = self.instantiate_from("location-example-ambulance.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation3(inst2)
    
    def implLocation3(self, inst):
        self.assertEqual(inst.description, "Ambulance provided by Burgers University Medical Center")
        self.assertEqual(inst.id, "amb")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "kind")
        self.assertEqual(inst.name, "BUMC Ambulance")
        self.assertEqual(inst.physicalType.coding[0].code, "ve")
        self.assertEqual(inst.physicalType.coding[0].display, "Vehicle")
        self.assertEqual(inst.physicalType.coding[0].system, "http://terminology.hl7.org/CodeSystem/location-physical-type")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "2329")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Mobile Clinic</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "AMB")
        self.assertEqual(inst.type[0].coding[0].display, "Ambulance")
        self.assertEqual(inst.type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
    
    def testLocation4(self):
        inst = self.instantiate_from("location-example-ukpharmacy.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation4(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation4(inst2)
    
    def implLocation4(self, inst):
        self.assertEqual(inst.description, "All Pharmacies in the United Kingdom covered by the National Pharmacy Association")
        self.assertEqual(inst.id, "ukp")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "kind")
        self.assertEqual(inst.name, "UK Pharmacies")
        self.assertEqual(inst.physicalType.coding[0].code, "jdn")
        self.assertEqual(inst.physicalType.coding[0].display, "Jurisdiction")
        self.assertEqual(inst.physicalType.coding[0].system, "http://terminology.hl7.org/CodeSystem/location-physical-type")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">UK Pharmacies</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "PHARM")
        self.assertEqual(inst.type[0].coding[0].display, "Pharmacy")
        self.assertEqual(inst.type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
    
    def testLocation5(self):
        inst = self.instantiate_from("location-example-patients-home.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation5(inst2)
    
    def implLocation5(self, inst):
        self.assertEqual(inst.description, "Patient's Home")
        self.assertEqual(inst.id, "ph")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "kind")
        self.assertEqual(inst.name, "Patient's Home")
        self.assertEqual(inst.physicalType.coding[0].code, "ho")
        self.assertEqual(inst.physicalType.coding[0].display, "House")
        self.assertEqual(inst.physicalType.coding[0].system, "http://terminology.hl7.org/CodeSystem/location-physical-type")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">Patient's Home</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "PTRES")
        self.assertEqual(inst.type[0].coding[0].display, "Patient's Residence")
        self.assertEqual(inst.type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")
    
    def testLocation6(self):
        inst = self.instantiate_from("location-example-hl7hq.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation6(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation6(inst2)
    
    def implLocation6(self, inst):
        self.assertEqual(inst.address.city, "Ann Arbor")
        self.assertEqual(inst.address.country, "USA")
        self.assertEqual(inst.address.line[0], "3300 Washtenaw Avenue, Suite 227")
        self.assertEqual(inst.address.postalCode, "48104")
        self.assertEqual(inst.address.state, "MI")
        self.assertEqual(inst.description, "HL7 Headquarters")
        self.assertEqual(inst.id, "hl7")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.mode, "instance")
        self.assertEqual(inst.name, "Health Level Seven International")
        self.assertEqual(inst.physicalType.coding[0].code, "bu")
        self.assertEqual(inst.physicalType.coding[0].display, "Building")
        self.assertEqual(inst.physicalType.coding[0].system, "http://terminology.hl7.org/CodeSystem/location-physical-type")
        self.assertEqual(inst.position.latitude, -83.69471)
        self.assertEqual(inst.position.longitude, 42.2565)
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "(+1) 734-677-7777")
        self.assertEqual(inst.telecom[1].system, "fax")
        self.assertEqual(inst.telecom[1].value, "(+1) 734-677-6622")
        self.assertEqual(inst.telecom[2].system, "email")
        self.assertEqual(inst.telecom[2].value, "hq@HL7.org")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type[0].coding[0].code, "SLEEP")
        self.assertEqual(inst.type[0].coding[0].display, "Sleep disorders unit")
        self.assertEqual(inst.type[0].coding[0].system, "http://terminology.hl7.org/CodeSystem/v3-RoleCode")

