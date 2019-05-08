#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import namingsystem
from .fhirdate import FHIRDate


class NamingSystemTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("NamingSystem", js["resourceType"])
        return namingsystem.NamingSystem(js)
    
    def testNamingSystem1(self):
        inst = self.instantiate_from("namingsystem-example-id.json")
        self.assertIsNotNone(inst, "Must have instantiated a NamingSystem instance")
        self.implNamingSystem1(inst)
        
        js = inst.as_json()
        self.assertEqual("NamingSystem", js["resourceType"])
        inst2 = namingsystem.NamingSystem(js)
        self.implNamingSystem1(inst2)
    
    def implNamingSystem1(self, inst):
        self.assertEqual(inst.contact[0].name, "HL7 Australia FHIR Team")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7-australia.wikispaces.com/FHIR+Australia")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-31").date)
        self.assertEqual(inst.date.as_json(), "2015-08-31")
        self.assertEqual(inst.description, "Australian HI Identifier as established by relevant regulations etc.")
        self.assertEqual(inst.id, "example-id")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "AU")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.kind, "identifier")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "Austalian Healthcare Identifier - Individual")
        self.assertEqual(inst.publisher, "HL7 Australia on behalf of NEHTA")
        self.assertEqual(inst.responsible, "HI Service Operator / NEHTA")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "NI")
        self.assertEqual(inst.type.coding[0].display, "National unique individual identifier")
        self.assertEqual(inst.type.coding[0].system, "http://terminology.hl7.org/CodeSystem/v2-0203")
        self.assertEqual(inst.type.text, "IHI")
        self.assertEqual(inst.uniqueId[0].comment, "This value is used in Australian CDA documents")
        self.assertEqual(inst.uniqueId[0].type, "oid")
        self.assertEqual(inst.uniqueId[0].value, "1.2.36.1.2001.1003.0")
        self.assertEqual(inst.uniqueId[1].period.start.date, FHIRDate("2015-08-21").date)
        self.assertEqual(inst.uniqueId[1].period.start.as_json(), "2015-08-21")
        self.assertTrue(inst.uniqueId[1].preferred)
        self.assertEqual(inst.uniqueId[1].type, "uri")
        self.assertEqual(inst.uniqueId[1].value, "http://ns.electronichealth.net.au/id/hi/ihi/1.0")
        self.assertEqual(inst.usage, "Used in Australia for identifying patients")
    
    def testNamingSystem2(self):
        inst = self.instantiate_from("namingsystem-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a NamingSystem instance")
        self.implNamingSystem2(inst)
        
        js = inst.as_json()
        self.assertEqual("NamingSystem", js["resourceType"])
        inst2 = namingsystem.NamingSystem(js)
        self.implNamingSystem2(inst2)
    
    def implNamingSystem2(self, inst):
        self.assertEqual(inst.contact[0].name, "FHIR project team")
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2014-12-13").date)
        self.assertEqual(inst.date.as_json(), "2014-12-13")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.kind, "codesystem")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.name, "SNOMED CT")
        self.assertEqual(inst.publisher, "HL7 International on behalf of IHTSDO")
        self.assertEqual(inst.responsible, "IHTSDO & affiliates")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.uniqueId[0].type, "oid")
        self.assertEqual(inst.uniqueId[0].value, "2.16.840.1.113883.6.96")
        self.assertTrue(inst.uniqueId[1].preferred)
        self.assertEqual(inst.uniqueId[1].type, "uri")
        self.assertEqual(inst.uniqueId[1].value, "http://snomed.info/sct")

