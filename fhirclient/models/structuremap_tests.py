#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.0.11832 on 2017-03-22.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import structuremap
from .fhirdate import FHIRDate


class StructureMapTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("StructureMap", js["resourceType"])
        return structuremap.StructureMap(js)
    
    def testStructureMap1(self):
        inst = self.instantiate_from("structuremap-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureMap instance")
        self.implStructureMap1(inst)
        
        js = inst.as_json()
        self.assertEqual("StructureMap", js["resourceType"])
        inst2 = structuremap.StructureMap(js)
        self.implStructureMap1(inst2)
    
    def implStructureMap1(self, inst):
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "http://hl7.org/fhir")
        self.assertEqual(inst.date.date, FHIRDate("2017-03-09").date)
        self.assertEqual(inst.date.as_json(), "2017-03-09")
        self.assertEqual(inst.description, "Example Structure Map")
        self.assertEqual(inst.group[0].documentation, "test -> testValue")
        self.assertEqual(inst.group[0].input[0].mode, "source")
        self.assertEqual(inst.group[0].input[0].name, "test")
        self.assertEqual(inst.group[0].name, "Examples")
        self.assertEqual(inst.group[0].rule[0].name, "rule1")
        self.assertEqual(inst.group[0].rule[0].source[0].context, "Source")
        self.assertEqual(inst.group[0].rule[0].source[0].element, "test")
        self.assertEqual(inst.group[0].rule[0].source[0].type, "SourceClassA")
        self.assertEqual(inst.group[0].rule[0].source[0].variable, "t")
        self.assertEqual(inst.group[0].rule[0].target[0].context, "Destination")
        self.assertEqual(inst.group[0].rule[0].target[0].contextType, "variable")
        self.assertEqual(inst.group[0].rule[0].target[0].element, "testValue")
        self.assertEqual(inst.group[0].rule[0].target[0].transform, "copy")
        self.assertEqual(inst.group[0].typeMode, "none")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "urn:ietf:rfc:3986")
        self.assertEqual(inst.identifier[0].value, "urn:oid:37843577-95fb-4adb-84c0-8837188a7bf3")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "009")
        self.assertEqual(inst.jurisdiction[0].coding[0].display, "Oceania")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "http://unstats.un.org/unsd/methods/m49/m49.htm")
        self.assertEqual(inst.name, "ExampleMap")
        self.assertEqual(inst.publisher, "HL7 FHIR Standard")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Example Map")
        self.assertEqual(inst.url, "http://hl7.org/fhir/StructureMap/example")
        self.assertEqual(inst.version, "0.1")

