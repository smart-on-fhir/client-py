#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (xds-profile.profile.json) on 2014-10-31.
#  2014, SMART Platforms.


import io
import unittest
import json
from location import Location
from fhirdate import FHIRDate


class LocationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        with io.open(filename, 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        instance = Location(js)
        self.assertIsNotNone(instance, "Must have instantiated a test instance")
        return instance
    
    def testLocation1(self):
        inst = self.instantiate_from("../../fhir-parser/downloads/site/location-example-room.json")
        self.assertIsNotNone(inst, "Must have instantiated a Location instance")
    
        self.assertEqual(inst.description, "Old South Wing, Neuro Radiology Operation Room 1 on second floor")
        self.assertEqual(inst.identifier.value, "B1-S.F2.1.00")
        self.assertEqual(inst.managingOrganization.reference, "Organization/f001")
        self.assertEqual(inst.name, "South Wing Neuro OR 1")
        self.assertEqual(inst.partOf.reference, "Location/1")
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

