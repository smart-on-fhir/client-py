#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import person
from .fhirdate import FHIRDate


class PersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Person", js["resourceType"])
        return person.Person(js)
    
    def testPerson1(self):
        inst = self.instantiate_from("person-example-f002-ariadne.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson1(inst)
        
        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson1(inst2)
    
    def implPerson1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1963").date)
        self.assertEqual(inst.birthDate.as_json(), "1963")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].text, "Ariadne Bor-Jansma")
        self.assertEqual(inst.name[0].use, "usual")
        self.assertEqual(inst.photo.contentType, "image/jpeg")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "home")
        self.assertEqual(inst.telecom[0].value, "+31201234567")
        self.assertEqual(inst.text.status, "generated")
    
    def testPerson2(self):
        inst = self.instantiate_from("person-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Person instance")
        self.implPerson2(inst)
        
        js = inst.as_json()
        self.assertEqual("Person", js["resourceType"])
        inst2 = person.Person(js)
        self.implPerson2(inst2)
    
    def implPerson2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "PleasantVille")
        self.assertEqual(inst.address[0].line[0], "534 Erewhon St")
        self.assertEqual(inst.address[0].postalCode, "3999")
        self.assertEqual(inst.address[0].state, "Vic")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.birthDate.date, FHIRDate("1974-12-25").date)
        self.assertEqual(inst.birthDate.as_json(), "1974-12-25")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].period.start.date, FHIRDate("2001-05-06").date)
        self.assertEqual(inst.identifier[0].period.start.as_json(), "2001-05-06")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.2.36.146.595.217.0.1")
        self.assertEqual(inst.identifier[0].type.coding[0].code, "MR")
        self.assertEqual(inst.identifier[0].type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "12345")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name[0].family, "Chalmers")
        self.assertEqual(inst.name[0].given[0], "Peter")
        self.assertEqual(inst.name[0].given[1], "James")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.name[1].given[0], "Jim")
        self.assertEqual(inst.name[1].use, "usual")
        self.assertEqual(inst.telecom[0].use, "home")
        self.assertEqual(inst.telecom[1].system, "phone")
        self.assertEqual(inst.telecom[1].use, "work")
        self.assertEqual(inst.telecom[1].value, "(03) 5555 6473")
        self.assertEqual(inst.telecom[2].system, "email")
        self.assertEqual(inst.telecom[2].use, "home")
        self.assertEqual(inst.telecom[2].value, "Jim@example.org")
        self.assertEqual(inst.text.status, "generated")

