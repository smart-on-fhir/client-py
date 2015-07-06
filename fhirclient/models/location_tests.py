#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 on 2015-07-06.
#  2015, SMART Health IT.


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
        inst = self.instantiate_from("location-example-ambulance.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation1(inst2)
    
    def implLocation1(self, inst):
        self.assertEqual(inst.description, "Ambulance provided by Burgers University Medical Center")
        self.assertEqual(inst.id, "amb")
        self.assertEqual(inst.mode, "kind")
        self.assertEqual(inst.name, "BUMC Ambulance")
        self.assertEqual(inst.physicalType.coding[0].code, "ve")
        self.assertEqual(inst.physicalType.coding[0].display, "Vehicle")
        self.assertEqual(inst.physicalType.coding[0].system, "http://hl7.org/fhir/location-physical-type")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "2329")
        self.assertEqual(inst.text.div, "<div>Mobile Clinic</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "AMB")
        self.assertEqual(inst.type.coding[0].display, "Ambulance")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
    
    def testLocation2(self):
        inst = self.instantiate_from("location-example-patients-home.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation2(inst2)
    
    def implLocation2(self, inst):
        self.assertEqual(inst.description, "Patient's Home")
        self.assertEqual(inst.id, "ph")
        self.assertEqual(inst.mode, "kind")
        self.assertEqual(inst.name, "Patient's Home")
        self.assertEqual(inst.physicalType.coding[0].code, "ho")
        self.assertEqual(inst.physicalType.coding[0].display, "House")
        self.assertEqual(inst.physicalType.coding[0].system, "http://hl7.org/fhir/location-physical-type")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div>Patient's Home</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "PTRES")
        self.assertEqual(inst.type.coding[0].display, "Patient's Residence")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
    
    def testLocation3(self):
        inst = self.instantiate_from("location-example-room.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation3(inst2)
    
    def implLocation3(self, inst):
        self.assertEqual(inst.description, "Old South Wing, Neuro Radiology Operation Room 1 on second floor")
        self.assertEqual(inst.id, "2")
        self.assertEqual(inst.identifier[0].value, "B1-S.F2.1.00")
        self.assertEqual(inst.mode, "instance")
        self.assertEqual(inst.name, "South Wing Neuro OR 1")
        self.assertEqual(inst.physicalType.coding[0].code, "ro")
        self.assertEqual(inst.physicalType.coding[0].display, "Room")
        self.assertEqual(inst.physicalType.coding[0].system, "http://hl7.org/fhir/location-physical-type")
        self.assertEqual(inst.status, "suspended")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "2329")
        self.assertEqual(inst.text.div, "<div>Burgers UMC, South Wing, second floor, Neuro Radiology Operation Room 1</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "RNEU")
        self.assertEqual(inst.type.coding[0].display, "Neuroradiology unit")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
    
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
        self.assertEqual(inst.mode, "kind")
        self.assertEqual(inst.name, "UK Pharmacies")
        self.assertEqual(inst.physicalType.coding[0].code, "jdn")
        self.assertEqual(inst.physicalType.coding[0].display, "Jurisdiction")
        self.assertEqual(inst.physicalType.coding[0].system, "http://hl7.org/fhir/location-physical-type")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div>UK Pharmacies</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "PHARM")
        self.assertEqual(inst.type.coding[0].display, "Pharmacy")
        self.assertEqual(inst.type.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
    
    def testLocation5(self):
        inst = self.instantiate_from("location-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
        self.implLocation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Location", js["resourceType"])
        inst2 = location.Location(js)
        self.implLocation5(inst2)
    
    def implLocation5(self, inst):
        self.assertEqual(inst.address.city, "Den Burg")
        self.assertEqual(inst.address.country, "NLD")
        self.assertEqual(inst.address.line[0], "Galapagosweg 91, Building A")
        self.assertEqual(inst.address.postalCode, "9105 PZ")
        self.assertEqual(inst.address.use, "work")
        self.assertEqual(inst.description, "Second floor of the Old South Wing, formerly in use by Psychiatry")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/location-alias")
        self.assertEqual(inst.extension[0].valueString, "Burgers University Medical Center, South Wing, second floor")
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/location-alias")
        self.assertEqual(inst.extension[1].valueString, "BU MC, SW, F2")
        self.assertEqual(inst.id, "1")
        self.assertEqual(inst.identifier[0].value, "B1-S.F2")
        self.assertEqual(inst.mode, "instance")
        self.assertEqual(inst.name, "South Wing, second floor")
        self.assertEqual(inst.physicalType.coding[0].code, "wi")
        self.assertEqual(inst.physicalType.coding[0].display, "Wing")
        self.assertEqual(inst.physicalType.coding[0].system, "http://hl7.org/fhir/location-physical-type")
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
        self.assertEqual(inst.text.div, "<div>Burgers UMC, South Wing, second floor</div>")
        self.assertEqual(inst.text.status, "generated")

