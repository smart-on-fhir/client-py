#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import relatedperson
from .fhirdate import FHIRDate


class RelatedPersonTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("RelatedPerson", js["resourceType"])
        return relatedperson.RelatedPerson(js)
    
    def testRelatedPerson1(self):
        inst = self.instantiate_from("relatedperson-example-f001-sarah.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson1(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson1(inst2)
    
    def implRelatedPerson1(self, inst):
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "f001")
        self.assertEqual(inst.identifier[0].system, "urn:oid:2.16.840.1.113883.2.4.6.3")
        self.assertEqual(inst.identifier[0].type.text, "BSN")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.name[0].family, "Abels")
        self.assertEqual(inst.name[0].given[0], "Sarah")
        self.assertEqual(inst.name[0].use, "usual")
        self.assertEqual(inst.relationship.coding[0].code, "SIGOTHR")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "mobile")
        self.assertEqual(inst.telecom[0].value, "0690383372")
        self.assertEqual(inst.telecom[1].system, "email")
        self.assertEqual(inst.telecom[1].use, "home")
        self.assertEqual(inst.telecom[1].value, "s.abels@kpn.nl")
        self.assertEqual(inst.text.status, "generated")
    
    def testRelatedPerson2(self):
        inst = self.instantiate_from("relatedperson-example-f002-ariadne.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson2(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson2(inst2)
    
    def implRelatedPerson2(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("1963").date)
        self.assertEqual(inst.birthDate.as_json(), "1963")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "f002")
        self.assertEqual(inst.name[0].text, "Ariadne Bor-Jansma")
        self.assertEqual(inst.name[0].use, "usual")
        self.assertEqual(inst.period.start.date, FHIRDate("1975").date)
        self.assertEqual(inst.period.start.as_json(), "1975")
        self.assertEqual(inst.photo[0].contentType, "image/jpeg")
        self.assertEqual(inst.relationship.coding[0].code, "SIGOTHR")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/v3/RoleCode")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "home")
        self.assertEqual(inst.telecom[0].value, "+31201234567")
        self.assertEqual(inst.text.status, "generated")
    
    def testRelatedPerson3(self):
        inst = self.instantiate_from("relatedperson-example-peter.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson3(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson3(inst2)
    
    def implRelatedPerson3(self, inst):
        self.assertEqual(inst.address[0].city, "PleasantVille")
        self.assertEqual(inst.address[0].line[0], "534 Erewhon St")
        self.assertEqual(inst.address[0].postalCode, "3999")
        self.assertEqual(inst.address[0].state, "Vic")
        self.assertEqual(inst.address[0].use, "home")
        self.assertEqual(inst.gender, "male")
        self.assertEqual(inst.id, "peter")
        self.assertEqual(inst.name[0].family, "Chalmers")
        self.assertEqual(inst.name[0].given[0], "Peter")
        self.assertEqual(inst.name[0].given[1], "James")
        self.assertEqual(inst.name[0].use, "official")
        self.assertEqual(inst.period.start.date, FHIRDate("2012-03-11").date)
        self.assertEqual(inst.period.start.as_json(), "2012-03-11")
        self.assertEqual(inst.photo[0].contentType, "image/jpeg")
        self.assertEqual(inst.photo[0].url, "Binary/f012")
        self.assertEqual(inst.relationship.coding[0].code, "C")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/v2/0131")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].use, "work")
        self.assertEqual(inst.telecom[0].value, "(03) 5555 6473")
        self.assertEqual(inst.text.status, "generated")
    
    def testRelatedPerson4(self):
        inst = self.instantiate_from("relatedperson-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a RelatedPerson instance")
        self.implRelatedPerson4(inst)
        
        js = inst.as_json()
        self.assertEqual("RelatedPerson", js["resourceType"])
        inst2 = relatedperson.RelatedPerson(js)
        self.implRelatedPerson4(inst2)
    
    def implRelatedPerson4(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.address[0].city, "Paris")
        self.assertEqual(inst.address[0].country, "FRA")
        self.assertEqual(inst.address[0].line[0], "43, Place du Marché Sainte Catherine")
        self.assertEqual(inst.address[0].postalCode, "75004")
        self.assertEqual(inst.gender, "female")
        self.assertEqual(inst.id, "benedicte")
        self.assertEqual(inst.identifier[0].system, "urn:oid:1.2.250.1.61")
        self.assertEqual(inst.identifier[0].type.text, "INSEE")
        self.assertEqual(inst.identifier[0].use, "usual")
        self.assertEqual(inst.identifier[0].value, "272117510400399")
        self.assertEqual(inst.name[0].family, "du Marché")
        self.assertEqual(inst.name[0].given[0], "Bénédicte")
        self.assertEqual(inst.photo[0].contentType, "image/jpeg")
        self.assertEqual(inst.photo[0].url, "Binary/f016")
        self.assertEqual(inst.relationship.coding[0].code, "N")
        self.assertEqual(inst.relationship.coding[0].system, "http://hl7.org/fhir/v2/0131")
        self.assertEqual(inst.relationship.coding[1].code, "WIFE")
        self.assertEqual(inst.relationship.coding[1].system, "http://hl7.org/fhir/v3/RoleCode")
        self.assertEqual(inst.telecom[0].system, "phone")
        self.assertEqual(inst.telecom[0].value, "+33 (237) 998327")
        self.assertEqual(inst.text.status, "generated")

